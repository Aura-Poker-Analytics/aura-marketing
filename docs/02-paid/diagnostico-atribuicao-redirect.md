# Diagnóstico: por que a atribuição está zerada — o redirect apex→www

**Autor:** thread Mídia Paga · **Data:** 2026-07-20 · **Método:** GA4 Data API (property `506294082`) + `curl` no domínio real + inspeção do bundle JS no ar + `tbl_user` em produção. Tudo verificado, nada assumido.

**TL;DR:** não é tag faltando nem consentimento. O redirect **`aurapoker.com` → `www.aurapoker.com`** responde `301` com `Location: https://www.aurapoker.com` **cru — sem path e sem query string**. Como o link da bio (Linktree) usa o domínio **sem www**, todo visitante do Instagram perde os UTMs *antes* de a landing (e o GA4/pixel) carregarem. Uma linha de config de domínio explica o funil de atribuição inteiro estar em branco.

---

## 1. A evidência (reproduzível)

```
$ curl -I "https://aurapoker.com/?utm_source=instagram&utm_medium=bio&utm_campaign=launch20"
HTTP/1.1 301 Moved Permanently
Location: https://www.aurapoker.com          ← domínio cru: sem "/", sem "?utm_..."
```

- **A origem do 301 é o Domain Forwarding da GoDaddy — NÃO é Azure** (confirmado 2026-07-20 via `az` CLI + DNS):
  - Nameservers do domínio: `ns09/ns10.domaincontrol.com` + `dns.jomax.net` → **GoDaddy**.
  - Apex `aurapoker.com` resolve pra `3.33.251.168`, com header `Server: ...ec2.internal` → **serviço de encaminhamento da GoDaddy** (roda em AWS), que 301-a pra `https://www.aurapoker.com` cru.
  - `www.aurapoker.com` → CNAME → `jolly-flower-0b6161c0f.7.azurestaticapps.net` (o SWA, serve o app OK).
  - No Azure, o SWA `Aura-Landing-Page` tem **só `www.aurapoker.com`** como custom domain — **o apex nem está bindado lá**.
- Não existe `staticwebapp.config.json` / `vercel.json` / `_redirects` no repo `aura-landing`, e nenhuma config de Azure toca nisso → **o fix é no painel da GoDaddy (registrador), não em código nem em Azure.**
- As tags estão corretas no bundle no ar (`https://www.aurapoker.com/assets/index-*.js`): GA4 `G-82QPEX5EJS`, pixel `1405949840871947`, `fbq`, `aura_consent`. **Não é tag ausente** — é o UTM sendo apagado antes de chegar nelas.

## 2. Por que isso explica TODOS os sintomas

| Sintoma observado | Causa via redirect |
|---|---|
| `launch20` = **0 sessões** no GA4 (01–19/07) | UTM morre no 301, nunca chega no gtag |
| 100% do tráfego do launch caiu em `(direct)/(none)` | sem UTM **e** sem referrer preservado → GA4 não tem o que atribuir |
| `utm_source`/`utm_campaign`/`fbp`/`fbc` = **null** nos 10 cadastros reais | o app nunca recebe os UTMs — eles já morreram na porta da landing |
| As 8 sessões `instagram/social/bio` (14/06–06/07) tinham tag, as do launch não | até 06/07 o **WordPress** servia o apex direto, sem redirect www → UTM sobrevivia. Pós-cutover Azure, o 301 passou a comê-los |

> Nuance: parte do `(direct)` do launch também é o in-app browser do Instagram (sem referrer por natureza). Mas mesmo esse tráfego **deveria** trazer o UTM da URL — e não traz, por causa do redirect. O redirect é a causa dominante e determinística.

## 3. "GA4 no esquema antigo" — o que realmente é

Não é a tag: é o **mesmo property/measurement ID (`G-82QPEX5EJS`) herdado da era WordPress**, hoje recebendo hostnames misturados. Breakdown de pageviews (01/06–19/07, property `506294082`):

| hostName | pageviews | leitura |
|---|---|---|
| `aurapoker.com` | 150 | landing (maioria era-WP) |
| **`localhost`** | **61** | 🗑️ dev local |
| `www.aurapoker.com` | 21 | landing (pós-cutover) |
| **`www.aura.poker`** | 12 | 🗑️ o **app** vazando pro property da landing |
| **`beta.aura.poker`** | 4 | 🗑️ beta antigo |
| **`loja.aurapoker.com`** | 3 | 🗑️ WooCommerce legado |
| **`*.azurestaticapps.net`** | 2 | 🗑️ preview do Azure |

≈70 de ≈253 pageviews (**~28%**) são lixo (dev/beta/loja/preview/app). Mesma poluição no pixel Meta (`localhost`/`beta.aura.poker`/`invalid.invalid`), documentada em [status-cutover-verificado.md §3](status-cutover-verificado.md).

## 4. Plano de correção (por dono)

### 4a. 🔴 P0 — parar de perder UTM (destrava toda a mensuração)
- **Fix imediato (Rafael, Linktree, ~30s):** trocar o destino do link pra **com www**: `https://www.aurapoker.com/?utm_source=instagram&utm_medium=bio&utm_campaign=launch20`. Pula o encaminhamento da GoDaddy — o UTM sobrevive na hora. Não depende de deploy nem de mexer em DNS.
- **Fix estrutural (quem tem acesso à GoDaddy):** ver [handoff-betiato-redirect-ga4.md](handoff-betiato-redirect-ga4.md). Ou (a) reconfigurar o Forwarding da GoDaddy pra **preservar path+query**, ou (b) parar o forwarding e bindar o apex direto no SWA (custom domain + validação TXT + registro apex), aí o apex serve o app sem 301 lossy. **Não é tarefa de Azure isolado** — sem o passo no registrador, o Azure sozinho não resolve.

### 4b. 🟠 Higiene do GA4 (Rafael, painel Admin — a Data API/MCP é só leitura, não edita config)
1. **Data filter "internal traffic"** excluindo `localhost` (e IPs de dev).
2. **Filtro/segmento de hostname** mantendo só `aurapoker.com` + `www.aurapoker.com`.
3. **Separar o app** (`aura.poker`, stream próprio `G-KL9K2FYVV2`) do property da landing — hoje vazam juntos.
4. **Referral exclusion** de `linktr.ee` + **cross-domain** `aurapoker.com ↔ aura.poker`.
5. Marcar `CompleteRegistration`/`sign_up` como **evento-chave**.

### 4c. 🟡 Pixel Meta (Rafael, BM)
- Allowlist de domínios no Events Manager + confirmar/verificar `aura.poker` (segue pendente no BM — ver [auditoria-meta-ads.md](auditoria-meta-ads.md) G5).

## 5. Como validar que consertou (aceite)
1. Abrir `https://aurapoker.com/?utm_source=instagram&utm_medium=bio&utm_campaign=launch20` e confirmar que a URL final **mantém** `?utm_...`.
2. GA4 (Tempo real ou relatório D+1): sessão com `source=instagram / medium=bio / campaign=launch20`.
3. Fazer 1 cadastro real ponta-a-ponta → conferir no `tbl_user` que `utm_source/medium/campaign/fbp/fbc` vieram **preenchidos** (hoje: null em 10/10).
4. Events Manager: `CompleteRegistration` "Processado (deduplicado)".

**Regra absoluta:** nada disso ativa campanha nem gasta — é instrumentação. Ativação é só do Rafael.
