# Handoff — Pixel/Tracking na migração da landing (WordPress → Azure)

**Autor:** thread Mídia Paga · **Data:** 2026-07-08 · **Para:** o agente da landing page (+ Rafael/dev)
**Base:** [pixel-capi-spec.md](pixel-capi-spec.md) continua sendo o contrato de eventos canônico. Este doc adiciona a camada da migração e traz o **prompt pronto** pro agente da landing (§6).

---

## 1. Contexto da migração

- **Site velho** (`aurapoker.com`, WordPress na **Hostinger**): WooCommerce + Subscriptions + Stripe. **Vai ser aposentado** (esclarecimento do dev, 08/07) — o WooCommerce era só o **intermediário pro Stripe**; no fluxo novo **a cobrança é Stripe direto**. O WP/WooCommerce não some fisicamente, mas **não recebe mais nada** (sem tráfego/venda novos). Os ~51 clientes legados são **migrados** (adoção das assinaturas que já existem no Stripe) ou, no pior caso, cancelam e re-assinam (o dev prefere não). **Nada disso bloqueia o launch** (confirmado pelo dev).
- **Landing 2.0 nova**: **Azure Static Web App** `Aura-Landing-Page` (verificado via Azure MCP), mesmo resource group da API (`aura-api-production`, App Service) e do banco (`aura-production`, PostgreSQL). Front estático + API própria + Postgres — **não é mais WordPress**.
- **Decisão do PO:** reaproveitar o **mesmo pixel/dataset `1405949840871947`** na landing nova (mantém histórico de PageView e os públicos que dependem dele).
- **Pendente (Rafael decide):** o **domínio final** da landing nova e onde fica a loja. Enquanto não decidir, o pixel-capi-spec fica com `aurapoker.com` marcado como "confirmar".
- **Oferta (auditado no Stripe MCP, 08/07):** conta `acct_1PX6SEIsnKTRWBVc` (AURA ANALYTICS, livemode). Produto único **"AURA Plano Individual"** com 3 preços, **todos em USD**: **$29/mês** (default), **$149/6 meses**, **$259/ano**. → O evento `Subscribe` sai em **USD**, e a otimização por valor/LTV usa esses números ([medicao-otimizacao.md](medicao-otimizacao.md)). Assinaturas recorrentes **ativas** no Stripe hoje: ~1 (a busca retornou 1) — ou seja, os ~51 "customers" do WooCommerce são majoritariamente compra única/expirados; **a migração de legado é bem menor do que parecia** (dev confirmar contagem exata no dashboard).

## 2. Estado atual do tracking no site velho (auditado via WordPress MCP)

| Item | Estado | Observação |
|---|---|---|
| **PixelYourSite** (v11.2) | Ativo | É quem gerencia Meta Pixel + **CAPI** + GA4 no WP hoje. Dispara PageView/AddToCart/InitiateCheckout no dataset `1405949840871947` |
| **Meta for WooCommerce** (v3.7.4) | Ativo | Também empurra pixel/CAPI de eventos de loja → **risco de evento duplicado** com o PixelYourSite |
| Official Facebook Pixel | Inativo | ok (senão seriam 3) |
| Site Kit (Google) + Google for WooCommerce | Ativos | GA4/Google — fora do escopo Meta |
| Microsoft Clarity | Inativo | — |
| Consentimento | Cookie Notice (Hu-manity.co) | **Não migra** pro Azure — a landing nova precisa do próprio mecanismo de consentimento |
| Pagamento | WooCommerce Subscriptions + Stripe (+ CoinPayments) | Assinatura dos legados |

## 3. Riscos da migração (revisados após esclarecimento do dev)

Com o WooCommerce **aposentado** (não é uma loja viva em paralelo), o risco de poluição do dataset **se resolve sozinho** — a loja velha para de gerar eventos porque para de receber tráfego/venda. O que sobra é cuidado de **cutover**, não de arquitetura:

**R1 — Cutover limpo do pixel (o que importa agora).** Hoje quem dispara o pixel `1405949840871947` é o **PixelYourSite** (+ Meta for WooCommerce) no WP. Quando o domínio de produção apontar pra landing Azure, é preciso garantir que **só a landing nova** dispare — que o pixel do WP **pare** (WP fora do domínio de produção, ou os plugins Meta desativados). Senão, na janela de overlap, os dois disparam e duplicam. Eventos históricos já no dataset (AddToCart/InitiateCheckout antigos) são **inofensivos** — é dado velho, não polui o futuro.

**R2 — Cobrança agora é Stripe direto.** `Subscribe` deve vir do **webhook do Stripe** (sem intermédio do WooCommerce). Importante: **não** disparar `Subscribe` para os clientes **legados migrados** (eles não são conversão de mídia nova) — só para assinaturas **criadas pelo funil novo**. Migração de legado ≠ evento de conversão.

**R3 — Duplo disparo pré-existente no WP.** PixelYourSite **e** Meta for WooCommerce estão ativos juntos hoje — já pode estar duplicando. Como o WP vai sair de cena, isso morre no cutover; só cuidar pra não deixar os dois vivos no domínio de produção durante a transição.

## 4. Onde pixel e CAPI entram na arquitetura Azure

- **Browser (pixel):** código `fbq` no front da Static Web App `Aura-Landing-Page` — PageView em toda página; CompleteRegistration na tela de sucesso do cadastro free; (Subscribe preferencialmente server-side).
- **CAPI (server-side):** endpoint na **API própria** (`aura-api-production` App Service) OU numa **Azure Function** da Static Web App (managed API). Dispara:
  - `CompleteRegistration` quando o backend confirma a conta free criada (Postgres) — dedup com o browser via `event_id`.
  - `Subscribe` no webhook de pagamento confirmado (Stripe) — server-side, uma vez por assinatura.
- **Token da CAPI:** em variável de ambiente / Azure Key Vault — **nunca no código nem no repo**.
- **UTM:** capturar no primeiro acesso (first-touch), persistir no registro do usuário no Postgres, e mandar no `user_data`/`custom_data` da CAPI. É o que liga o gasto de mídia ao KPI (conta free via UTM).

## 5. Domínio — CONFIRMADO: `aurapoker.com` (08/07)

A landing nova fica em **`aurapoker.com`** — o **mesmo domínio do site atual**. Implicações:
- **É cutover, não domínio novo:** o WordPress sai de `aurapoker.com` e a Azure SWA entra. Continuidade pro pixel (o histórico de PageView já é desse domínio).
- **Cuidado do cutover (R1):** no momento do repoint, garantir que o WP pare de servir/disparar em `aurapoker.com` — senão os dois disparam o mesmo pixel e duplicam. Como é o mesmo domínio, isso se resolve com o repoint (só um serve por vez), desde que o WP não fique acessível no domínio de produção.
- **Ações do Rafael no BM (destravadas):** (a) aceitar o alerta "confirme o domínio" no Diagnóstico do dataset; (b) verificar `aurapoker.com` em Adequação e segurança → Domínios. Como já é o domínio do site, é confirmar, não trocar.
- O agente da landing ainda reporta **onde a CAPI roda** no PR.

---

## 6. PROMPT PRO AGENTE DA LANDING (copy-paste)

> **Contexto:** você trabalha no repo da landing 2.0 da Aura — uma **Azure Static Web App** (`Aura-Landing-Page`, resource group `Aura-resource-group`), com API própria (`aura-api-production`, App Service) e banco PostgreSQL (`aura-production`). O WordPress/WooCommerce antigo (Hostinger) está sendo **aposentado** (cobrança nova é Stripe direto). Sua tarefa: instrumentar todo o rastreamento de marketing + o evento de assinatura da landing nova.
>
> **Setup de trabalho:**
> - Crie uma **branch nova a partir da `main`** (ex.: `feat/marketing-tracking`). Não faça merge sozinho — abra **PR** no final pra revisão.
> - **Paralelize com subagentes mais baratos** (Sonnet/Haiku): as frentes 1–5 abaixo são independentes o bastante pra rodar em paralelo.
> - **Zero segredo no código/repo** — tokens em env var / Azure Key Vault.
>
> **Frentes a implementar:**
> 1. **Pixel Meta (browser)** — reusar o pixel/dataset `1405949840871947` (NÃO criar novo). `fbq` base + `PageView` em todas as páginas. Capturar cookies `_fbp`/`_fbc`.
> 2. **CompleteRegistration** (conta free criada): browser na tela de sucesso do cadastro com `eventID` = `reg_<user_id>`, **e** server (CAPI) quando o backend confirma a conta — mesmo `event_id` pra deduplicar.
> 3. **Conversions API (server-side)** — endpoint em Azure Function (managed API da SWA) ou rota da `aura-api-production`. `POST https://graph.facebook.com/v23.0/1405949840871947/events`. `user_data`: `em` (sha256 do email), `client_ip_address`, `client_user_agent`, `fbp`, `fbc`. Token em env/Key Vault.
> 4. **Subscribe via Stripe direto** — conta **`acct_1PX6SEIsnKTRWBVc`** (AURA ANALYTICS, livemode). Produto **"AURA Plano Individual"** (`prod_Uq1tafUe0H12h4`), preços em **USD**: `price_1TqLpgIsnKTRWBVcebHjviGn` = **$29/mês** (default), `price_1TqLpgIsnKTRWBVcXwXa6cgY` = **$149/6 meses**, `price_1TqLpgIsnKTRWBVcHKFLaKf4` = **$259/ano**. Configurar **webhook do Stripe** (`checkout.session.completed` / `invoice.paid` do 1º ciclo): (a) provisionar acesso do usuário; (b) disparar `Subscribe` (CAPI) com `value` = valor do 1º ciclo, `currency` = `"usd"`, `event_id` = `sub_<subscription_id>`, **uma vez por assinatura**. **NÃO** disparar `Subscribe` para clientes legados migrados — só funil novo.
> 5. **UTM** — capturar `utm_source/medium/campaign/content` no 1º acesso (first-touch, não sobrescrever), persistir no registro do usuário (Postgres), incluir na CAPI. Garantir que sobrevivem a redirects (www↔apex, http→https). É o que liga o gasto de mídia ao KPI (conta free via UTM).
> 6. **Consentimento (LGPD)** — banner/CMP próprio (o Cookie Notice do WP não migra). Sem consentimento de marketing, não dispara pixel browser.
> 7. **NÃO** disparar eventos de e-commerce da loja WooCommerce antiga neste pixel — a landing nova é só funil de cadastro/assinatura.
>
> **Reportar de volta pra thread de Mídia Paga (no PR):**
> - **Domínio final** da landing (pra allowlist do dataset + verificação no BM).
> - Onde a CAPI roda (Azure Function da SWA vs. `aura-api-production`).
> - Checklist de aceite: `PageView` do domínio novo; `CompleteRegistration` "Processado (deduplicado)" no Events Manager; `Subscribe` chegando do Stripe; `_fbp`/`_fbc` persistidos; UTM gravado na conta; token fora do git.
>
> **Regra:** nada aqui gasta mídia; é instrumentação. Ativação de campanha é só do Rafael.

---

## 7. O que muda nos docs de Mídia Paga depois disso

- Quando o domínio final for definido: atualizar [pixel-capi-spec.md](pixel-capi-spec.md) §0/§6 (hoje assume `aurapoker.com`) e [publicos-build-spec.md](publicos-build-spec.md) P4 (visitantes de site) com o domínio certo.
- [readiness-dia10.md](readiness-dia10.md): o item 🔴 "pixel/CAPI na landing" agora tem dono e arquitetura claros (Azure SWA + API). Segue sendo o único bloqueio real do dia 10.
- A decisão de R1 virou "cutover limpo" (não "pixel separado") — registrar quando o cutover de domínio acontecer.

---

## 8. Passos pra deixar correto (checklist por dono)

**A. Tracking / pixel — pré e durante o cutover** *(Mídia Paga + agente da landing)*
- [ ] Definir o **domínio final** da landing nova (bloqueio pendente do Rafael).
- [ ] Agente da landing instrumenta o pixel `1405949840871947` na Azure SWA conforme §6 (PageView, CompleteRegistration dedup, Subscribe via Stripe).
- [ ] No cutover, **desligar o disparo do pixel no WP velho** (desativar PixelYourSite + Meta for WooCommerce, ou tirar o WP do domínio de produção) — evitar duplo disparo.
- [ ] Allowlist do domínio no Diagnóstico do dataset + **verificar domínio no Business Manager**.
- [ ] Validar no Events Manager: PageView do domínio novo, CompleteRegistration "Processado (deduplicado)", Subscribe chegando do Stripe.

**B. Cobrança Stripe direto** *(dev; Mídia Paga só depende do evento)*
- [ ] Assinatura nova cobrada **direto no Stripe**; `Subscribe` (CAPI) dispara no **webhook do Stripe**, uma vez por assinatura.
- [ ] **Não** disparar `Subscribe` para legados migrados (só funil novo).
- [ ] (Se quiser que eu audite produtos/preços/webhooks do Stripe, **autorizar o MCP do Stripe** — hoje está conectado mas pedindo autenticação; sem isso não consigo ler o Stripe.)

**C. Migração dos clientes legados** *(dev — Betiato; NÃO bloqueia o launch)*
- [ ] Tentar **adotar as assinaturas que já existem no Stripe** (criadas via WooCommerce) no app novo — casar por Stripe customer/email e liberar acesso **sem re-assinar**.
- [ ] Fallback (último caso): cancelar + pedir re-assinatura.
- [ ] Rodar essa frente **em paralelo** ao launch — o dev já preparou com o Cursor os passos de repontar beta→oficial.

**D. Desativação graciosa do WP velho** *(dev do WP)*
- [ ] Manter os dados do WooCommerce (não apagar), mas ele não recebe mais nada.
- [ ] Garantir que nada no WP velho continua disparando pixel/CAPI no domínio de produção após o cutover.

**Não bloqueia o dia 10:** só o item **A** (pixel na landing nova) está no caminho crítico do launch — e é o mesmo 🔴 do [readiness-dia10.md](readiness-dia10.md). B, C e D correm em paralelo, sem travar o lançamento.
