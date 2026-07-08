# Definição de Pronto — Rastreamento (funil cross-domain + validação)

**Autor:** thread Mídia Paga · **Data:** 2026-07-08
**Correção de arquitetura (08/07):** o **cadastro e a assinatura acontecem no APP (novofront, beta.aura.poker → oficial)**, NÃO na landing de marketing. O funil cruza **dois domínios**. Isto corrige a premissa de [pixel-capi-spec.md](pixel-capi-spec.md) (que assumia a tela de sucesso na landing) e complementa o [handoff-landing-pixel-migracao.md](handoff-landing-pixel-migracao.md).

---

## 1. Quem dispara o quê (funil de 2 propriedades)

| Propriedade | Papel | Eventos |
|---|---|---|
| **Landing** `aurapoker.com` | marketing / topo | pixel base + **PageView**. CTA leva ao app **com `utm_*` + `fbclid` no link**. |
| **App** novofront (beta→oficial) | cadastro + assinatura | pixel base + **PageView** + **CompleteRegistration** + **Subscribe** + **CAPI** (server). Captura UTM/fbclid da URL e **persiste na conta**. |

- **Mesmo pixel/dataset `1405949840871947` nos dois** — funil único, não dois pixels.
- **Elo crítico:** UTM + `fbclid` precisam **atravessar** landing → app (via query string no CTA) e ser **persistidos no app** no cadastro. Sem isso, o KPI norte (conta free via UTM) não fecha.

## 2. Faseamento nesta arquitetura

**FASE 1 — pro dia 10 (browser, sem backend):**
- Landing: pixel base + `PageView`.
- App: pixel base + `PageView` + `CompleteRegistration` **browser-only** na conclusão do cadastro (com `eventID` = `reg_<user_id>`).
- CTA da landing anexa `utm_*` + `fbclid` no link pro app (barato — já preserva atribuição desde o dia 1).

**FASE 2 — antes do 1º real de mídia paga:**
- CAPI server-side no app (dedup do CompleteRegistration, recupera iOS/adblock).
- `Subscribe` via webhook Stripe (USD; uma vez/assinatura; **não** pra legado migrado).
- UTM/fbclid **persistidos na conta** e enviados na CAPI.
- Consentimento (LGPD) próprio.

## 3. Sobre a instrumentação COMPLETA já pronta (commit local sem push)

**Não descartar.** Separar por dependência:
- **Browser (PageView, CompleteRegistration)** → funciona sem backend → **pode ir ao ar já** (Fase 1).
- **Server (CAPI, Subscribe)** → depende de: token da CAPI no env/Key Vault do app + webhook do Stripe registrado + cobrança Stripe-direto finalizada. Enquanto não ligar, manter **inerte** (env não setado / feature-flag off). → "**Parkar pra Fase 2**" vale **só pro server-side**; o browser sobe agora.

## 4. Definição de PRONTO — FASE 1 (bater item a item antes de considerar "no ar")

- [ ] Pixel base carrega na **landing** (`aurapoker.com`) e no **app** — mesmo ID `1405949840871947`.
- [ ] `PageView` dispara na landing e no app.
- [ ] `CompleteRegistration` dispara **no app** na conclusão do cadastro — **na troca de rota** (SPA), não só num reload — com `eventID` = `reg_<user_id>`.
- [ ] Landing no ar em `aurapoker.com` (**cutover DNS** feito) e app no domínio oficial.
- [ ] **Pixel do WordPress velho desligado** (PixelYourSite + Meta for WooCommerce) — sem duplo disparo.
- [ ] CTA da landing → app **carrega `utm_*` + `fbclid`**.
- [ ] Consentimento respeitado (ou TODO de Fase 2 registrado).
- [ ] Sem **CSP** bloqueando `connect.facebook.net` / `facebook.com/tr`.
- [ ] Rafael no BM: alerta de domínio aceito + `aurapoker.com` verificado.
- [ ] **Validado no Events Manager:** PageView (landing + app) e CompleteRegistration (app) chegando, com `eventID` presente.

## 5. Definição de PRONTO — FASE 2 (antes do 1º real gasto)

- [ ] CAPI server ativa (token no Key Vault) → `CompleteRegistration` aparece **"Processado (deduplicado)"** no Events Manager.
- [ ] `Subscribe` disparando do **webhook Stripe** (USD, uma vez por assinatura), **não** pra legado migrado.
- [ ] `utm_*`/`fbclid` persistidos na conta → validar atribuição no **AuraBusiness**.
- [ ] Domínio(s) verificado(s) no BM; Diagnóstico do dataset sem erros novos.
- [ ] `_fbp`/`_fbc` capturados no app pro matching da CAPI.

## 6. Como a Mídia Paga valida (quando estiver no ar)

1. **Chrome** na landing e no app: confirmar `fbq` carregando e o request `facebook.com/tr` disparando (PageView; e CompleteRegistration ao concluir cadastro).
2. **Events Manager** (no BM): PageView dos dois domínios + CompleteRegistration do app, com `eventID`.
3. Conferir que **não há duplo disparo** (WP velho desligado).

Merge + deploy **não** garante nada disso sozinho — só a validação acima confirma.
