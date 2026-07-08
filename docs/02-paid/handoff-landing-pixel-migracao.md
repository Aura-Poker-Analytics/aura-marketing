# Handoff — Pixel/Tracking na migração da landing (WordPress → Azure)

**Autor:** thread Mídia Paga · **Data:** 2026-07-08 · **Para:** o agente da landing page (+ Rafael/dev)
**Base:** [pixel-capi-spec.md](pixel-capi-spec.md) continua sendo o contrato de eventos canônico. Este doc adiciona a camada da migração e traz o **prompt pronto** pro agente da landing (§6).

---

## 1. Contexto da migração

- **Site velho** (`aurapoker.com`, WordPress na **Hostinger**): WooCommerce + Subscriptions + Stripe atendendo os **clientes antigos** (~51 customers). **Fica** rodando, só pros legados.
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

## 3. Dois riscos da migração a resolver

**R1 — Poluição do dataset (o mais importante).** Se a landing nova reusa o pixel `1405949840871947` **e** a loja WooCommerce antiga continua disparando nele (PixelYourSite/Meta-for-WooCommerce), o dataset mistura dois funis: venda legada + cadastro SaaS do launch. Isso suja públicos ("todos os visitantes" vira loja+landing), atribuição e otimização.
→ **Recomendação:** na loja antiga, apontar PixelYourSite/Meta-for-WooCommerce para um **pixel separado** (ou desligar os eventos Meta de lá). A landing nova fica sozinha no `1405949840871947`, limpa pro funil de cadastro. *(Ação no WordPress velho — não é o agente da landing; é Rafael/dev do WP.)*

**R2 — Evento duplicado já hoje.** PixelYourSite **e** Meta for WooCommerce ativos ao mesmo tempo podem duplicar eventos Meta. Se a loja antiga vai continuar, escolher **um** deles como fonte de verdade do Meta e desativar o outro.

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
- A decisão de R1 (pixel separado pra loja legada) deve ser registrada quando o Rafael/dev do WP executar.
