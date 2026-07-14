# Prompt pro Cursor — consolidar/rebasear/commitar a Fase 2

Copiar o bloco abaixo pro Cursor. Corrige 2 pontos do mapa dele + responde as 2 perguntas + manda finalizar.

---

> Você já mapeou a Fase 2 (boa análise). **2 correções ao seu mapa + respostas às suas 2 perguntas**, e então: consolidar sobre o `main` atual, rebasear e commitar (PR por repo, **sem merge**).
>
> **CORREÇÃO 1 — a CAPI/Subscribe NÃO precisam ser escritas do zero. Já existem.**
> `aura-api:origin/feat/marketing-tracking @23c4e82` (pushada — faça `git fetch origin`) traz prontos:
> - `ABE3_API/Services/MetaCapiService.cs` (+205): `SendCompleteRegistrationAsync` (`event_name=CompleteRegistration`, `event_id=reg_{userId}`), `SendSubscribeAsync` (`event_name=Subscribe`, `event_id=sub_{subscriptionId}`), endpoint `graph.facebook.com/{ver}/{pixelId}/events`, SHA256 do email.
> - `ABE3_API/Services/BillingService.cs` (+75): injeta `IMetaCapiService`, **guarda de idempotência** do Subscribe, chama `SendSubscribeAsync` no `HandleCheckoutSessionCompletedAsync`.
> - `IMetaCapiService`, `Helpers/MetaSettings.cs`, `Entities/Request/SignUpRequestDto.cs` (UTM/fbp/fbc), `Entities/Database/TblUser.cs` (colunas), `Services/UserService.cs` (`SignUp`: CompleteRegistration server + persist UTM), `Program.cs` (DI), `db/marketing_tracking.sql` (migração idempotente).
> → **Reutilize esse código — não crie um `MetaConversionsService` novo.** O commit é aditivo (+429/0); só o `UserService.cs` conflita (abaixo).
>
> **CORREÇÃO 2 — sua arquitetura/ordem estão certas, mantenha.** CAPI no `aura-api-production` (App Service, onde o webhook Stripe já aponta). Backend antes do front.
>
> **RESPOSTA Q1 (colunas UTM em prod):** não confirmadas — você viu certo, o brief estava otimista (a thread de Mídia Paga corrigiu). **Inclua a migração no escopo:** a `db/marketing_tracking.sql` de 23c4e82 é `ADD COLUMN IF NOT EXISTS` (idempotente) → rodar é seguro exista ou não. Não bloqueie código por isso.
>
> **RESPOSTA Q2 (WIP/branches):** parta do **`origin/main` limpo** em cada repo. Ignore os WIP: winback (aura_api) e `fix/ga4-app-tag` (novofront) — **este já foi mergeado via PR #24**, é obsoleto. Pode reusar `feat/marketing-tracking` **rebaseada no main** ou criar `feature/marketing-tracking-fase2` — desde que fique **em cima do main atual** (a branch antiga está ~15 commits atrás; PR dela como está reverteria o refactor de email/i18n — foi o quase-desastre do GA4).
>
> **Execução (3 PRs, backend primeiro):**
> 1. **aura-database / aura_api:** versionar/rodar a migração idempotente (`utm_*`/`referrer`/`fbp`/`fbc` no `tbl_user`).
> 2. **aura_api:** trazer 23c4e82 pro main. Conflito único em `UserService.cs` (sua branch é anterior ao refactor de email do main): **manter o `EmailDispatch.TrySendInBackground` do main** e **adicionar** só o marketing — injetar `_metaCapiService`+`_httpContextAccessor`, `SendCompleteRegistrationAsync(...)` após o welcome email, helper `GetRequestClientInfo`, gravar `utm/fbp/fbc` no `newUser`. **Build + teste de signup.** Subscribe: manter a guarda de idempotência + **filtro anti-legado** (não disparar pra `metadata.winback`/assinaturas migradas).
> 3. **aura-landing:** cherry-pick de `335d4cd` (`ConsentBanner`, `consent.ts`, `metaPixel` gated).
> 4. **aura-novofront:** cherry-pick de `62f0a5f` (`marketingAttribution.ts`, hook no `AuthContext`, `Login` signup+consent, `requests.ts` com campos UTM). Sua lista de arquivos-seguros está correta.
> 5. **Alinhar o contrato de consentimento** (você achou a divergência): landing `aura_consent`+`mc=1` vs app `aura_marketing_consent`. Escolha **UM** (sugestão: `aura_consent` + param `mc=1`) e alinhe os dois lados.
> 6. Deixar CAPI/Subscribe atrás de **feature-flag/env off** até os segredos entrarem — não quebra deploy.
>
> **Pré-requisitos humanos (paralelo — bloqueiam aceite, não código):** `META_CAPI_TOKEN` + `Stripe:WebhookSecret` no Azure Key Vault; confirmar preços USD no checkout (`prod_Uq1tafUe0H12h4`).
>
> **Regra absoluta:** nada disso ativa campanha nem gasta — mídia é só o Rafael.
>
> **Ao fechar:** avise a thread de Mídia Paga pro aceite (Events Manager: `CompleteRegistration` "Processado/deduplicado" + `Subscribe` do Stripe; UTM gravado no AuraBusiness).

---

**Fontes (branches pushadas, backup):** aura-landing `335d4cd` · aura-novofront `62f0a5f` · aura-api `23c4e82`. Contexto completo: [prompt-fase2-tracking.md](prompt-fase2-tracking.md).
