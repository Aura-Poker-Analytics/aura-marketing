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

Não há `staticwebapp.config.json` no repo `aura-landing` → o redirect é **config de plataforma** (binding de domínio custom do Static Web App), não código.

## O fix (escolher um; A é o correto de longo prazo)

**Opção A — apex serve o app direto + canonicaliza pra www preservando a query (recomendado)**
1. No recurso Static Web App: parar de tratar o apex como "redirect pro primário". Bindar `aurapoker.com` como domínio que **serve** o app (igual www).
2. Adicionar `staticwebapp.config.json` na raiz do `aura-landing` com redirect canônico que **preserva path+query**:
```json
{
  "globalHeaders": { "X-Aura-Canonical": "www" },
  "responseOverrides": {},
  "navigationFallback": { "rewrite": "/index.html" }
}
```
> ⚠️ O SWA não faz host-rewrite condicional via config sozinho de forma confiável — se for por essa via, o mais garantido é canonicalizar **no cliente** (JS na landing: se `location.hostname === 'aurapoker.com'`, `location.replace('https://www.aurapoker.com' + location.pathname + location.search)`). Isso **preserva a query** de forma determinística e é 100% sob controle do repo. Custa 1 redirect client-side, aceitável.

**Opção B — corrigir o redirect de plataforma pra preservar path+query**
- No Azure, o redirect apex→www do SWA aponta pra raiz do primário. Se der pra configurar como "preserve path/query", ativar. (Nem toda config de SWA expõe isso — por isso a Opção A é mais robusta.)

**Mitigação imediata (não depende de deploy):** o Rafael troca o destino no Linktree pra `https://www.aurapoker.com/?utm_...` (com www). Isso já para o sangramento enquanto o fix estrutural sobe. Faça o fix mesmo assim — gente que digita o domínio cru ou vem de outros links continua perdendo UTM.

## Bônus GA4 (não é seu, mas pro seu radar)
O property `506294082` (`G-82QPEX5EJS`) recebe hostnames misturados: `localhost` (61 pv), `www.aura.poker` (o app, 12 pv), `beta.aura.poker`, `loja.aurapoker.com`, preview `*.azurestaticapps.net`. O app **não** deveria mandar pro mesmo stream da landing. Se o app estiver com `G-82QPEX5EJS` em algum lugar além do `G-KL9K2FYVV2`, remover. A limpeza dos filtros (internal traffic / hostname) o Rafael faz no painel Admin.

## Aceite (como a Mídia Paga confirma)
```bash
curl -sSL -o /dev/null -w "%{url_effective}\n" "https://aurapoker.com/?utm_source=instagram&utm_medium=bio&utm_campaign=launch20"
# esperado: https://www.aurapoker.com/?utm_source=instagram&utm_medium=bio&utm_campaign=launch20  (query preservada)
```
Depois: 1 cadastro real ponta-a-ponta → `utm_*`/`fbp`/`fbc` preenchidos no `tbl_user` + `CompleteRegistration` "deduplicado" no Events Manager.
