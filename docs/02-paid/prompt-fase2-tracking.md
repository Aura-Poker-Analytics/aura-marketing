# Fase 2 do rastreamento — brief engatilhado (pro dev/agente)

**Autor:** thread Mídia Paga · **Data:** 2026-07-12
**Quando disparar:** antes do **1º real de mídia paga** (não é pré-requisito do launch orgânico). É o que torna o pago **mensurável** — sem isso, gastar é chute.
**Base (ler antes):** [pixel-capi-spec.md](pixel-capi-spec.md) (contrato) · [definicao-pronto-tracking.md](definicao-pronto-tracking.md) (arquitetura cross-domain + DoD §5) · [handoff-landing-pixel-migracao.md](handoff-landing-pixel-migracao.md) (Stripe/Azure).

---

## 0. Estado atual (verificado no GitHub 2026-07-12) — LEIA PRIMEIRO

- ✅ **Fase 1 no ar:** landing (pixel+PageView+utm/fbclid nos CTAs+GA4) e app (pixel+PageView+CompleteRegistration) — ambos no `main`.
- ✅ **Código Fase 2 preservado no remote (backup feito 2026-07-12).** Estava só local (nesta máquina, num worktree) — agora pushado, sem PR/merge:
  - `aura-landing:feat/marketing-tracking` @ `335d4cd` — **consent gate LGPD** (`ConsentBanner.tsx`, `consent.ts`, `privacidade.html`, `useConsentRefresh.ts`) + UTM first-touch (`attribution.ts`, `appUrl.ts`, `metaPixel.ts`).
  - `aura-novofront:feat/marketing-tracking` @ `62f0a5f` — captura/persistência de UTM (`marketingAttribution.ts`, `AuthContext.tsx`, `MinhaConta.tsx`, `requests.ts`) + Login/index.
  - ✅ **`aura-api:feat/marketing-tracking` @ `23c4e82`** (pushado 2026-07-12) — **CAPI server + Subscribe + UTM-persist JÁ CODADOS.** Commit limpo/aditivo (+429, 0 deleções): `Services/MetaCapiService.cs` (+205), `IMetaCapiService`, `Helpers/MetaSettings.cs`, `Entities/Request/SignUpRequestDto.cs` (UTM/fbp/fbc), `Entities/Database/TblUser.cs` (colunas), `Services/UserService.cs` (CompleteRegistration server + UTM persist no signup), `Services/BillingService.cs` (+75, Subscribe), `Program.cs` (DI), `db/marketing_tracking.sql` (migração idempotente).
  - ✅ **Sem segredo vazado:** `appsettings.json` tem `Meta.AccessToken: ""` **vazio** — o token vem do Key Vault/env em runtime.

## 0b. Reframe: Fase 2 está CODADA (não a-construir) — falta CONSOLIDAR + secrets

As 4 peças existem, distribuídas em 3 branches `feat/marketing-tracking` (todas stale vs main, pushadas p/ backup):

| Peça | Onde | Estado |
|---|---|---|
| Consentimento LGPD | landing `335d4cd` | codado |
| UTM captura (front) | novofront `62f0a5f` | codado |
| CAPI (CompleteRegistration+Subscribe) + UTM persist + migração | aura-api `23c4e82` | codado |

> 🔴 **AVISO PRO CURSOR (quem está consolidando):** as branches `feat/marketing-tracking` estão **15 commits ATRÁS do main** (refactor de email + mais). **Se você continuar NA MESMA branch e abrir PR dela → main, vai REVERTER o refactor de email e outros commits** (exatamente o que quase aconteceu com o GA4). Antes de qualquer coisa: **`git rebase origin/main`** (ou merge do main pra dentro) da `feat/marketing-tracking`, resolvendo o conflito do `UserService.cs` **uma vez** (detalhe abaixo). Só depois de a branch estar em cima do main atual é que o PR fica limpo. As branches já estão pushadas (backup) — dá pra `git fetch` + rebase.

**Consolidação = trazer as adições pro `main` atual** — via rebase da branch (recomendado, mesma branch) OU cherry-pick dos commits. **Nunca** PR da branch stale como está.
- Front (landing/novofront): cherry-pick provavelmente mais limpo — validar.
- **Backend (aura-api): 1 conflito semântico em `UserService.cs`** — a branch de marketing é anterior ao **refactor de email do main** (`EmailDispatch.TrySendInBackground` novo; `_emailService`/`SmtpEmailSender`/`EmailTemplateRenderer` removidos). O cherry-pick mecânico conflita porque o código de marketing referencia classes de email que o main deletou. **Correto:** re-aplicar SÓ as adições de CAPI/UTM (injetar `_metaCapiService`+`_httpContextAccessor`, chamar `SendCompleteRegistrationAsync` após o welcome email do main, helper `GetRequestClientInfo`, gravar utm/fbp/fbc no `newUser`) sobre o `UserService.cs` ATUAL — **+ build + teste de signup**. É trabalho do dev/agente do backend (toca caminho crítico de cadastro), não cherry-pick cego.
- ⚠️ **Migração de colunas UTM já em prod (inerte)** — segundo o agente, o banco já tem as colunas pra persistir UTM (não estão sendo preenchidas ainda).
- 🔴 **Lição do PR #24 (não repetir):** branches antigas (`feat/pixel-fase1`) estão **muito atrás do main** — mergear a branch inteira reverteria i18n/componentes. **Não mergear branch stale: rebase/cherry-pick sobre o `main` atual** e conferir o diff (deve tocar só nos arquivos de tracking).

## 1. As 4 peças da Fase 2

### 1a. UTM/fbclid persistido na conta (a "última milha" da atribuição)
- Hoje: o CTA da landing **carrega** `utm_*`+`fbclid` → o app **captura em estado** (Fase 1). Falta **salvar no registro do usuário** no cadastro (as colunas já existem em prod, inertes).
- Gravar: `utm_source/medium/campaign/content` + `fbclid`, **first-touch** (não sobrescrever), no `tbl_user` (ou equivalente) no momento do signup.
- **Por quê:** é o que fecha o KPI norte — "conta free por UTM" no AuraBusiness. Sem isso, não dá pra dizer qual campanha gerou qual cadastro no seu próprio banco.

### 1b. CAPI (Conversions API) server-side
- Endpoint server (Azure Function da SWA ou rota da `aura-api-production`): `POST https://graph.facebook.com/v23.0/1405949840871947/events`.
- Disparar `CompleteRegistration` (server) quando o backend confirma a conta → **dedup com o browser via `event_id` = `reg_<user_id>`** (o browser já manda esse eventID).
- `user_data`: `em` (sha256 do email), `client_ip_address`, `client_user_agent`, `fbp`, `fbc`.
- **Recupera** os ~20-30% de eventos que iOS/adblock derrubam do browser.

### 1c. Subscribe via webhook do Stripe
- Conta Stripe `acct_1PX6SEIsnKTRWBVc` · produto `prod_Uq1tafUe0H12h4` · preços USD: $29/mês, $149/6m, $259/ano.
- No webhook (`checkout.session.completed` / `invoice.paid` do 1º ciclo): disparar `Subscribe` (CAPI) `value` = 1º ciclo, `currency="usd"`, `event_id="sub_<subscription_id>"`, **uma vez por assinatura**.
- ⚠️ **Não** disparar `Subscribe` pra legado migrado — só funil novo.

### 1d. Consentimento (LGPD)
- Banner/CMP próprio (a landing/app não têm — hoje é TODO). Sem consentimento de marketing → não dispara pixel/CAPI.

## 2. Pré-requisitos que NÃO são código (infra/segredos — humano)

- [ ] **Token da CAPI** (Events Manager → dataset → Conversions API → gerar) → **Azure Key Vault** / env do app. Nunca no repo.
- [ ] **Webhook do Stripe** registrado apontando pra API/Function + **signing secret** no Key Vault.
- [ ] Confirmar produto/preços do Stripe (§1c) no checkout real.

## 3. Definição de pronto da Fase 2 (aceite — Mídia Paga confere)

- [ ] `CompleteRegistration` aparece **"Processado (deduplicado)"** no Events Manager (browser+server, mesmo `event_id`).
- [ ] `Subscribe` chegando do webhook Stripe (USD, 1×/assinatura), não pra legado.
- [ ] `utm_*`/`fbclid` **gravados na conta** → validar atribuição no AuraBusiness.
- [ ] `_fbp`/`_fbc` capturados no app pro matching da CAPI.
- [ ] Diagnóstico do dataset sem erros novos; consentimento respeitado.

## 4. Ordem sugerida

1. **Recuperar/pushar o código Fase 2** local (§0) — ou reimplementar. Branch nova a partir do `main` atual (não a stale).
2. Infra/segredos (§2): token CAPI + webhook Stripe no Key Vault.
3. Codar as 4 peças (§1) → PR → review do Betiato → deploy.
4. Aceite (§3) pela Mídia Paga no Events Manager + AuraBusiness.
5. Só então o pago fica **mensurável** → destrava o 1º real (BR + EN), sempre com GO do Rafael.

**Regra absoluta:** nada aqui ativa campanha nem gasta — é instrumentação. Ativação é só do Rafael.
