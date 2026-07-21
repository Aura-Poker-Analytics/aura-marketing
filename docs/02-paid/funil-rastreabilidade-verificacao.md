# Verificação de rastreabilidade do funil — trabalho autônomo 2026-07-20

**Autor:** thread Mídia Paga (autônomo, subagentes Sonnet) · **Método:** 3 auditorias de código nos repos deployados (`origin/main`) + App Insights de produção + `tbl_user` + `az` CLI + bundle no ar. Tudo verificado empírica ou por leitura de código, com file:line.

**Veredito de uma linha:** a instrumentação está **correta e deployada ponta a ponta** — o `null` de UTM era 100% o redirect (já corrigido via Linktree→www), não bug de código. Restam **2 questões reais**: (1) o consent gate suprime GA4/Pixel por padrão (decisão LGPD, não bug), e (2) falta 1 validação de caminho completo (cadastro-teste humano). A **atribuição de primeira-parte (UTM→`tbl_user`) funciona independente de consentimento** — é a nossa fonte confiável.

---

## 1. O que foi PROVADO (não assumido)

### Infra de produção — tudo verde (via `az`)
- `aura-api-production` App Settings: **`Meta__AccessToken` preenchido**, `Stripe__ApiSecret` e `Stripe__WebhookSecret` preenchidos. CAPI **não é no-op**.
- `tbl_user` (prod): as 8 colunas `utm_source/medium/campaign/term/content/referrer/fbp/fbc` **existem** (`text`). Migração rodou.

### CAPI disparando de verdade (via App Insights, 21d)
- `15/07` → "Meta CAPI: evento CompleteRegistration (**reg_316**) enviado."
- `17/07` → "Meta CAPI: evento CompleteRegistration (**reg_317**) enviado."
- **0 exceptions** de tracking/signup/CAPI. Nenhum log de no-op (confirma token setado).
- Subscribe: só 1 assinatura (usuário 305, **08/07**, anterior ao deploy da CAPI de 14/07) → **Subscribe nunca foi exercitado** (esperado, sem conversão paga pós-deploy).
- ⚠️ "enviado" = a API fez a chamada HTTP; **não** prova que a Meta aceitou o evento. Confirmar no Events Manager (ação no BM).

### Código deployado — auditado nos 3 repos (todos mergeados em `origin/main`)
| Repo | Merge | Estado |
|---|---|---|
| `aura_api` | PR #9 (`17acd4f`, 14/07) | CAPI + UTM persist + Subscribe **em main** |
| `aura-novofront` | PR #25 (`8e65b07`) | captura UTM + pixel gated **em main** |
| `aura-landing` | PR #4 (`5784953`, 15/07) | pixel + UTM first-touch + consent gate **em main** |

**Cadeia ponta a ponta correta, sem o bug clássico de divergência de nome de campo:**
- App envia camelCase (`utmSource`, `utmMedium`, …, `fbp`, `fbc`) no `POST /api/user/signup`.
- DTO C# (`SignUpRequestDto`) recebe `UtmSource`…; ASP.NET `JsonSerializerDefaults.Web` liga **case-insensitive** → bate.
- `UserService.SignUp` copia os 8 campos pro `newUser` e salva; depois chama `SendCompleteRegistrationAsync` (`event_id=reg_<userId>`, dedup com o browser).
- Front dispara `trackCompleteRegistration(userId)` com `eventID=reg_<userId>`; `fbclid→fbc` sintetizado no formato da Meta.
- CTAs da landing propagam `utm_*+fbclid` e apontam pro **`www.aura.poker`** (com www) — correto.

### Contrato do endpoint (pra qualquer teste futuro)
`POST /api/user/signup` — obrigatórios: `email` (válido), `password` (≥8), `acceptedTerms:true`. Opcionais: `name`, `discord`, `turnstileToken` (condicional), `utmSource/utmMedium/utmCampaign/utmTerm/utmContent/referrer/fbp/fbc` (**camelCase**, snake_case NÃO liga).

## 2. Por que os UTMs estavam null (encerrado)
Não é código. É o redirect GoDaddy apex→www comendo os `?utm_*` antes de chegarem no front (ver [diagnostico-atribuicao-redirect.md](diagnostico-atribuicao-redirect.md)). Corrigido apontando o Linktree pro `www`. Os 3 cadastros pós-deploy (315–317) têm null porque chegaram sem UTM na URL — a API gravou null porque foi o que recebeu. Correto.

## 3. As 2 questões reais que restam

### 3a. 🔴 Consent gate suprime GA4 + Pixel por padrão (decisão, não bug)
Desde 15/07 (PR #4), **nada de GA4 nem Pixel dispara até o clique em "Aceitar"** — bloqueio binário, **sem Google Consent Mode v2** (sem modelagem cookieless). Quem ignora o banner, fecha a aba, ou está no in-app browser do Instagram (clique em overlay difícil, localStorage efêmero) → **zero telemetria**, nem sessão anônima.

**Impacto:** GA4/Pixel pós-15/07 subcontam pesado; e quando rodar mídia, o pixel só marca quem consente → otimização mutilada.

**Importante — o que NÃO é afetado:** a captura de **UTM→`tbl_user` NÃO é consent-gated** (só `fbp`/`fbc` são). Então **a atribuição de primeira-parte funciona sempre** — "qual campanha gerou qual conta free" continua rastreável no nosso banco, com ou sem consentimento.

**Recomendação (precisa de decisão sua/legal — não mexi):** implementar **Consent Mode v2** — `gtag('consent','default',{ analytics_storage:'denied', ad_storage:'denied' })` antes do load + `update` no aceite. LGPD é mais flexível que GDPR; analytics sob legítimo interesse com sinais default é defensável e recupera modelagem agregada. Alternativa: default `granted` pra analytics (não-pixel) fora da UE. É PR na `aura-landing` — deixo pronto pro Betiato quando você decidir a postura.

### 3c. 🟠 GA4 é cego pra conversão de cadastro (gap descoberto via Admin API)
Lendo o GA4 Admin API (ADC readonly) confirmei:
- **2 data streams intencionais no mesmo property `506294082`:** "Aura Landing Page" (`www.aurapoker.com`, `G-82QPEX5EJS`) + "Plataforma Aura" (`aura.poker`, `G-KL9K2FYVV2`). **Não é vazamento** — é setup correto pra funil cross-domain. (Corrige recomendação anterior de "separar o app": manter juntos, filtrar só o lixo.)
- **Eventos-chave = `purchase`, `close_convert_lead`, `qualify_lead`** — todos legado WooCommerce/CRM; `purchase` nem dispara.
- **Eventos recebidos (28d):** page_view, session_start, scroll, click, form_start, begin_checkout(5), add_to_cart(4). **NÃO existe `sign_up` nem `CompleteRegistration`.** O app dispara CompleteRegistration só pro **pixel Meta**, nunca pro GA4 → **o GA4 não enxerga a conversão de cadastro**. Só dá pra medir visita, não signup.
- **Fix (code, novofront, aditivo):** disparar `gtag('event','sign_up')` no sucesso do cadastro (junto do `trackCompleteRegistration` que já existe), depois marcar `sign_up` como evento-chave e limpar os 3 legados. Deixo pro Betiato — é consent-gated também, então casa com a decisão do 3a.

### 3b. 🟡 Falta 1 validação de caminho completo (cadastro-teste humano)
Tudo acima prova que o código está certo e a CAPI dispara. O que **nenhuma auditoria prova** é o caminho real fim-a-fim com UTM: IG→bio(www)→landing→app→signup, resultando em `utm_source=instagram` gravado no `tbl_user` + `CompleteRegistration` "deduplicado" no Events Manager. **Só um humano no celular fecha isso.** Não fiz cadastro sintético autônomo porque dispara evento real na Meta + email, e o caminho via API pularia justamente a landing/redirect que queremos validar.

## 4. Hardening de código (Betiato, baixa prioridade — não bloqueia nada)
1. Fixar o contrato JSON com `[JsonPropertyName("utmSource")]` etc. no `SignUpRequestDto` — hoje depende da config global do `AddJsonOptions`; se alguém mudar, UTM vira null **sem erro**.
2. CAPI é fire-and-forget (`_ = SendCompleteRegistrationAsync(...)`) — se o processo reciclar logo após o signup, o evento pode se perder sem sinal. Considerar outbox/fila se a entrega da CAPI virar crítica pra otimização paga.

## 5. Checklist pra quando você voltar (nada aqui gasta mídia)
- [ ] **Cadastro-teste no celular** (IG→bio→signup) → me avisa que eu confiro `utm_*`/`fbp` no `tbl_user` + dedup no Events Manager. **(fecha 3b)**
- [ ] **Decidir postura de consentimento** (Consent Mode v2 vs default granted p/ analytics) → eu preparo o PR da landing. **(resolve 3a)**
- [ ] **Events Manager**: confirmar que `reg_316`/`reg_317` chegaram (prova que a Meta aceita, não só "enviado"). **(BM)**
- [ ] **GA4 Admin** (higiene, corrigido): filtro internal traffic `localhost`; filtro de hostname mantendo **`aurapoker.com` + `aura.poker`** e excluindo beta/loja/preview; **cross-domain** entre os 2 streams; referral exclusion `linktr.ee`; adicionar evento `sign_up` (código app, §3c) e marcá-lo como evento-chave; limpar os 3 eventos-chave legados (`purchase`/`close_convert_lead`/`qualify_lead`). **(te guio ao vivo)**
- [ ] **BM**: verificar domínio `aura.poker` no dataset.
- [ ] (Opcional) hardening §4 pro Betiato.

**Regra absoluta mantida:** nada aqui ativou campanha nem gastou. Toda ação de mídia é sua.
