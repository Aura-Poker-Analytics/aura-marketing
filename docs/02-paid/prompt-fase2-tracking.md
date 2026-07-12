# Fase 2 do rastreamento — brief engatilhado (pro dev/agente)

**Autor:** thread Mídia Paga · **Data:** 2026-07-12
**Quando disparar:** antes do **1º real de mídia paga** (não é pré-requisito do launch orgânico). É o que torna o pago **mensurável** — sem isso, gastar é chute.
**Base (ler antes):** [pixel-capi-spec.md](pixel-capi-spec.md) (contrato) · [definicao-pronto-tracking.md](definicao-pronto-tracking.md) (arquitetura cross-domain + DoD §5) · [handoff-landing-pixel-migracao.md](handoff-landing-pixel-migracao.md) (Stripe/Azure).

---

## 0. Estado atual (verificado no GitHub 2026-07-12) — LEIA PRIMEIRO

- ✅ **Fase 1 no ar:** landing (pixel+PageView+utm/fbclid nos CTAs+GA4) e app (pixel+PageView+CompleteRegistration) — ambos no `main`.
- ⚠️ **O código Fase 2 está LOCAL, não pushado.** O agente disse "parkada na branch `feat/marketing-tracking`" — mas essa branch **não existe no remote** de novofront nem de landing. Ou seja: só existe na máquina de quem trabalhou. **1º passo: recuperar/pushar esse trabalho** (ou reimplementar se perdido). Risco real de perda.
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
