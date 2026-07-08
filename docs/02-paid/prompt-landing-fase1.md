# Prompt — Fase 1 do rastreamento (agente da landing) + onboarding dos agentes

**Autor:** thread Mídia Paga · **Data:** 2026-07-08
**Como usar:** cole o **Bloco A** (contexto) no início da conversa com o agente da landing **e** com o agente do front, pra ambos ficarem alinhados. Depois cole o **Bloco B** (tarefa) pro agente da landing, que é quem implementa a Fase 1 inteira.

---

## Bloco A — Onboarding (colar nos dois agentes: landing e front)

> Você está implementando o **rastreamento de marketing da Aura**. O plano e o contrato completos estão no repo **`aura-marketing`** (sibling dos repos de código, sob `aura-main/`), em **`docs/02-paid/`**. **Leia antes de codar**, nesta ordem:
> 1. **`definicao-pronto-tracking.md`** — arquitetura cross-domain (landing vs app) + faseamento + definição de pronto. **LEIA PRIMEIRO.**
> 2. **`pixel-capi-spec.md`** — contrato de eventos (PageView, CompleteRegistration, Subscribe, CAPI, UTM, dedup por `eventID`).
> 3. **`handoff-landing-pixel-migracao.md`** — contexto da migração (WordPress→Azure), Stripe direto, riscos de cutover.
> 4. **`medicao-otimizacao.md`** — como os eventos viram KPI (pra entender *por que* cada evento importa).
>
> **Resumo do modelo:** o funil cruza **2 domínios**. **Landing** (`aurapoker.com`) = pixel + `PageView` + link de signup carregando `utm_*`+`fbclid`. **App** (novofront) = `PageView` + `CompleteRegistration` (cadastro) + `Subscribe` (assinatura) + CAPI. **Mesmo pixel/dataset `1405949840871947` nos dois.** **Fase 1 (agora)** = só eventos de **browser**, sem backend/segredo. **Fase 2 (antes do 1º real de mídia paga)** = CAPI server, Subscribe via webhook Stripe, UTM persistido na conta, consentimento. Regra absoluta: nada disso ativa campanha — mídia é só o Rafael.

---

## Bloco B — Tarefa Fase 1 (colar pro agente da landing)

> **Escopo:** implementar a **Fase 1** do rastreamento (só browser, sem backend, sem segredo, sem webhook). Trabalhe numa **branch provisória a partir da `main`** (ex.: `feat/tracking-fase1`) — **não** misture com o refactor grande em andamento. Abra **PR** no final (sem merge). Se o pixel colidir com o refactor no merge, sinalize no PR pra ser re-aplicado.
>
> ### A) Na LANDING (`aurapoker.com`)
> 1. Pixel base `fbq` + `fbq('track','PageView')` — dataset **`1405949840871947`** (não criar novo) — no shell/head, em todas as páginas.
> 2. **Link/CTA de signup** (que aponta pro app): **propagar `utm_*` + `fbclid`** na query string do destino (ex.: `.../signup?utm_source=…&utm_campaign=…&fbclid=…`). Capturar esses params da URL da própria landing (vindos do anúncio) e repassar. **Este é o elo que faz a atribuição sobreviver ao pulo de domínio — não pule.**
> 3. Consentimento: se já houver banner/CMP, só dispare o pixel com consentimento de marketing; se não houver, deixe um `TODO` (LGPD entra na Fase 2).
>
> ### B) No APP (novofront) — parte browser da Fase 1
> 4. Pixel base + `PageView` (mesmo dataset `1405949840871947`).
> 5. **`CompleteRegistration` browser-only** na conclusão do cadastro — disparar **na troca de rota do SPA** (não só em reload), com `eventID = 'reg_<user_id>'` (id real do usuário, pra deduplicar quando a CAPI entrar na Fase 2).
> 6. Capturar `utm_*`/`fbclid` da URL de entrada do app (pelo menos em estado; a **persistência no banco** é Fase 2).
> - ⚠️ **Se o app já tem instrumentação completa commitada (local, sem push): NÃO reimplemente.** Só garanta que os eventos de **browser** (PageView, CompleteRegistration) vão ao ar e que as partes **server (CAPI/Subscribe)** ficam **inertes** (env não setado / feature-flag off) até a Fase 2. Se você não tem acesso ao repo do app, sinalize e passe este contexto pro agente do front.
>
> ### NÃO fazer agora (é Fase 2, antes do pago)
> CAPI server-side, evento `Subscribe`/webhook Stripe, persistência de UTM no banco, consentimento completo. **Não** disparar eventos da loja WooCommerce antiga neste pixel.
>
> ### Cutover
> Quando `aurapoker.com` apontar pro Azure, garanta (ou sinalize pra quem faz o DNS) que o **pixel do WordPress velho seja desligado** (PixelYourSite + Meta for WooCommerce) — senão haverá **duplo disparo**.
>
> ### Reportar no PR
> - Em quais arquivos/rotas o pixel entrou (landing **e** app).
> - Que o **CTA propaga `utm_*`+`fbclid`**.
> - Bater a **checklist da Fase 1** de `aura-marketing/docs/02-paid/definicao-pronto-tracking.md` §4.

---

**Validação (Mídia Paga, depois do deploy):** assim que estiver no ar em `aurapoker.com` + domínio do app, a thread de Mídia Paga valida via Chrome + Events Manager (Definição de Pronto §6).
