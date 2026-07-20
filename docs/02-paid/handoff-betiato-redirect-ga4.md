# Handoff Betiato — corrigir o redirect apex→www (mata a atribuição)

**De:** thread Mídia Paga · **Data:** 2026-07-20 · **Prioridade:** 🔴 P0 (bloqueia toda a mensuração de mídia)
**Contexto completo:** [diagnostico-atribuicao-redirect.md](diagnostico-atribuicao-redirect.md)

## O problema em 1 parágrafo

O redirect `aurapoker.com` → `www.aurapoker.com` está respondendo **`301` com `Location: https://www.aurapoker.com` cru — sem path e sem query string**. O link da bio (Instagram/Linktree) usa o domínio **sem www**, então todo visitante perde os `?utm_*` no redirect, antes da landing carregar. Resultado: 100% do tráfego do launch caiu em `(direct)` no GA4, e `utm_source/fbp/fbc` estão **null em 10/10 cadastros** no `tbl_user`. As tags (GA4 `G-82QPEX5EJS`, pixel `1405949840871947`) estão certas no bundle — o UTM é apagado antes de chegar nelas.

## Reproduzir

```bash
curl -I "https://aurapoker.com/?utm_source=x&utm_campaign=y"
# HTTP/1.1 301 Moved Permanently
# Location: https://www.aurapoker.com     ← perde "/", perde "?utm_..."
```

## Onde está o redirect (verificado 2026-07-20 via `az` CLI + DNS) — é GoDaddy, não Azure

- Nameservers: `ns09/ns10.domaincontrol.com` + `dns.jomax.net` → **DNS na GoDaddy**.
- Apex `aurapoker.com` → `3.33.251.168`, header `Server: ...ec2.internal` → **Domain Forwarding da GoDaddy** (roda em AWS) 301-ando pra `https://www.aurapoker.com` cru.
- `www.aurapoker.com` → CNAME → `jolly-flower-0b6161c0f.7.azurestaticapps.net` (o SWA `Aura-Landing-Page`, serve o app OK).
- No Azure, o SWA tem **só `www` como custom domain — o apex nem está bindado**. Logo, `az staticwebapp` / config de repo **não corrigem** — o fix é no **painel da GoDaddy**.

## O fix (escolher um; A é o correto de longo prazo)

**Opção A — bindar o apex direto no SWA (recomendado, sem 301 lossy)**
1. GoDaddy: **desligar o Domain Forwarding** de `aurapoker.com`.
2. Azure: adicionar `aurapoker.com` como 2º custom domain no SWA `Aura-Landing-Page` (`az staticwebapp hostname set ...`), que gera um **token TXT de validação** + o registro de apex a criar.
3. GoDaddy: criar o TXT de validação e o registro de apex (A/alias) que o Azure indicar. Apex passa a **servir o app direto** — UTMs sobrevivem.
4. (Opcional) canonicalizar pra www **no cliente**, aí sim preservando query: no `aura-landing`, se `location.hostname === 'aurapoker.com'` → `location.replace('https://www.aurapoker.com' + location.pathname + location.search)`. Só funciona depois do passo 3 (o app precisa carregar no apex). **Esse passo 4 é o único que eu (thread Mídia Paga) consigo entregar via PR no repo** — os passos 1–3 são GoDaddy+Azure.

**Opção B — manter forwarding, mas preservar path/query**
- No painel de Forwarding da GoDaddy, ver se o plano permite "forward with path"/preservar query. É menos confiável que a Opção A (o comportamento varia), mas é o fix mais rápido no registrador se a Opção A demorar.

**Mitigação imediata (não depende de ninguém além do Rafael, ~30s):** trocar o destino no Linktree pra `https://www.aurapoker.com/?utm_...` (com www). Para o sangramento na hora. Faça o fix estrutural mesmo assim — quem digita o domínio cru ou vem de outros links continua perdendo UTM.

## Bônus GA4 (não é seu, mas pro seu radar)
O property `506294082` (`G-82QPEX5EJS`) recebe hostnames misturados: `localhost` (61 pv), `www.aura.poker` (o app, 12 pv), `beta.aura.poker`, `loja.aurapoker.com`, preview `*.azurestaticapps.net`. O app **não** deveria mandar pro mesmo stream da landing. Se o app estiver com `G-82QPEX5EJS` em algum lugar além do `G-KL9K2FYVV2`, remover. A limpeza dos filtros (internal traffic / hostname) o Rafael faz no painel Admin.

## Aceite (como a Mídia Paga confirma)
```bash
curl -sSL -o /dev/null -w "%{url_effective}\n" "https://aurapoker.com/?utm_source=instagram&utm_medium=bio&utm_campaign=launch20"
# esperado: https://www.aurapoker.com/?utm_source=instagram&utm_medium=bio&utm_campaign=launch20  (query preservada)
```
Depois: 1 cadastro real ponta-a-ponta → `utm_*`/`fbp`/`fbc` preenchidos no `tbl_user` + `CompleteRegistration` "deduplicado" no Events Manager.
