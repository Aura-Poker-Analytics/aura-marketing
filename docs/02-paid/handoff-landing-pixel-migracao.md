# Handoff — Pixel/Tracking na migração da landing (WordPress → Azure)

**Autor:** thread Mídia Paga · **Data:** 2026-07-08 · **Para:** o agente da landing page (+ Rafael/dev)
**Base:** [pixel-capi-spec.md](pixel-capi-spec.md) continua sendo o contrato de eventos canônico. Este doc adiciona a camada da migração e traz o **prompt pronto** pro agente da landing (§6).

---

## 1. Contexto da migração

- **Site velho** (`aurapoker.com`, WordPress na **Hostinger**): WooCommerce + Subscriptions + Stripe. **Vai ser aposentado** (esclarecimento do dev, 08/07) — o WooCommerce era só o **intermediário pro Stripe**; no fluxo novo **a cobrança é Stripe direto**. O WP/WooCommerce não some fisicamente, mas **não recebe mais nada** (sem tráfego/venda novos). Os ~51 clientes legados são **migrados** (adoção das assinaturas que já existem no Stripe) ou, no pior caso, cancelam e re-assinam (o dev prefere não). **Nada disso bloqueia o launch** (confirmado pelo dev).
- **Landing 2.0 nova**: **Azure Static Web App** `Aura-Landing-Page` (verificado via Azure MCP), mesmo resource group da API (`aura-api-production`, App Service) e do banco (`aura-production`, PostgreSQL). Front estático + API própria + Postgres — **não é mais WordPress**.
- **Decisão do PO:** reaproveitar o **mesmo pixel/dataset `1405949840871947`** na landing nova (mantém histórico de PageView e os públicos que dependem dele).
- **Pendente (Rafael decide):** o **domínio final** da landing nova e onde fica a loja. Enquanto não decidir, o pixel-capi-spec fica com `aurapoker.com` marcado como "confirmar".

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

## 5. Domínio (bloqueio pendente do Rafael)

Qualquer que seja o domínio final da landing nova, ele precisa: (a) entrar no **allowlist do dataset** (Diagnóstico do Events Manager) e (b) ser **verificado no Business Manager** (Adequação e segurança → Domínios). O agente da landing deve **reportar o domínio final** assim que definido pra Mídia Paga atualizar o pixel-capi-spec e o Rafael verificar no BM.

---

## 6. PROMPT PRO AGENTE DA LANDING (copy-paste)

> **Contexto:** você trabalha na landing 2.0 da Aura, uma **Azure Static Web App** (`Aura-Landing-Page`, resource group `Aura-resource-group`), com API própria (`aura-api-production`, App Service) e banco PostgreSQL (`aura-production`). Estamos migrando de um WordPress/WooCommerce antigo (Hostinger, `aurapoker.com`) que fica só pros clientes legados. Sua tarefa é instrumentar o rastreamento de marketing da landing nova.
>
> **Fonte da verdade dos eventos:** `aura-marketing/docs/02-paid/pixel-capi-spec.md` — leia e siga o contrato (eventos, dedup, UTM, consentimento). Este prompt adapta aquilo à arquitetura Azure.
>
> **Requisitos:**
> 1. **Reusar o pixel/dataset Meta `1405949840871947`** (não criar novo). Instalar o `fbq` base + `PageView` em todas as páginas do front.
> 2. **`CompleteRegistration`** (conta free criada): disparar no browser na tela de sucesso do cadastro, com `eventID` determinístico (`reg_<user_id>`), **e** no server (CAPI) quando o backend confirmar a criação da conta — mesmo `event_id` para deduplicar.
> 3. **`Subscribe`** (assinatura paga): disparar **server-side** no webhook de pagamento confirmado (Stripe), uma vez por assinatura, `event_id` = `sub_<subscription_id>`, com `value` e `currency`.
> 4. **CAPI**: implementar o endpoint server-side numa Azure Function da Static Web App (managed API) **ou** em rota da `aura-api-production`. `POST https://graph.facebook.com/v23.0/1405949840871947/events`. Token da CAPI em **env var / Key Vault**, nunca no código/repo. Enviar `em` (sha256 do email), `client_ip_address`, `client_user_agent`, `fbp`, `fbc`.
> 5. **UTM**: capturar `utm_source/medium/campaign/content` no primeiro acesso (first-touch, não sobrescrever), persistir no registro do usuário no Postgres, e incluir na CAPI. Garantir que os params sobrevivem a redirects (www↔apex, http→https).
> 6. **Consentimento (LGPD)**: a landing nova precisa do próprio banner/CMP (o Cookie Notice do WP antigo não migra). Sem consentimento de marketing, não disparar o pixel browser.
> 7. **NÃO** disparar eventos de e-commerce da loja legada (AddToCart/Purchase de WooCommerce) neste pixel — a landing nova é só funil de cadastro/assinatura. (A loja antiga será separada num pixel próprio.)
>
> **Reportar de volta pra thread de Mídia Paga:**
> - O **domínio final** da landing (pra allowlist do dataset + verificação no BM).
> - Onde a CAPI roda (Azure Function da SWA vs. `aura-api-production`).
> - Confirmação item a item do checklist de aceite do `pixel-capi-spec.md` §6 (PageView, CompleteRegistration dedup "Processado", Subscribe, `_fbp/_fbc` persistidos, UTM gravado na conta, token fora do git).
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
