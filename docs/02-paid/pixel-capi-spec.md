# Spec: Meta Pixel + Conversions API — Landing 2.0

**Autor:** thread Mídia Paga · **Data:** 2026-07-04 · **Deadline de implementação: antes de 10/07 (launch da landing)**
**Público deste doc:** dev da landing. É handoff — dá pra implementar sem contexto de marketing.

---

> **Addendum migração (2026-07-08):** a landing 2.0 saiu do WordPress e virou uma **Azure Static Web App** (`Aura-Landing-Page`) com API própria (`aura-api-production`) e Postgres. O contrato de eventos abaixo continua válido; a adaptação à arquitetura Azure, os riscos de dataset e o prompt do dev estão em [handoff-landing-pixel-migracao.md](handoff-landing-pixel-migracao.md). Domínio final ainda a confirmar.

## 0. O que já existe (auditado em 04/07)

- **Dataset/Pixel existente:** `Aura – Website Data Set` — **ID `1405949840871947`** — no BM Aura Poker Analytics (830069129552748), integração "Pixel da Meta" (browser only), site `aurapoker.com`.
- Eventos hoje: `PageView` ativo (recebido há 5h), `InitiateCheckout` e `AddToCart` sem atividade há 9 dias (provavelmente do site/checkout antigo).
- **Decisão: REUSAR este dataset na landing nova.** Não criar pixel novo — o histórico de PageView alimenta públicos de retargeting desde já, e trocar de ID zera isso.
- Sem CAPI hoje. Esta spec adiciona.

## 1. Pixel (browser)

Base code em TODAS as páginas da landing, no `<head>`:

```html
<script>
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '1405949840871947');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=1405949840871947&ev=PageView&noscript=1"/></noscript>
```

## 2. Eventos (contrato)

Só estes 3 eventos padrão. Não disparar AddToCart/InitiateCheckout na landing nova.

| Evento | Quando dispara | Canal | Parâmetros |
|---|---|---|---|
| `PageView` | Toda pageview | Browser | (automático) |
| `CompleteRegistration` | Conta **free** criada com sucesso (confirmação real do backend, não o submit do form) | Browser **e** Server (dedup) | `content_name: 'free_account'`, `status: true` |
| `Subscribe` | Assinatura **paga** confirmada (webhook do gateway de pagamento) | **Server only** | `value: <preço 1º ciclo>`, `currency: 'BRL'` (ou moeda cobrada), `predicted_ltv` opcional |

Browser, na tela/rota de sucesso do cadastro free:

```js
fbq('track', 'CompleteRegistration',
  { content_name: 'free_account', status: true },
  { eventID: 'reg_<user_id>' }   // OBRIGATÓRIO — dedup com o evento server
);
```

## 3. Conversions API (server)

**Por quê:** iOS/adblock derrubam o pixel browser; CompleteRegistration e Subscribe são os eventos de otimização — precisam chegar por servidor.

- **Endpoint:** `POST https://graph.facebook.com/v23.0/1405949840871947/events`
- **Access token:** gerar em Events Manager → Configurações do dataset → Conversions API → "Gerar token de acesso". **→ env var `META_CAPI_TOKEN`, nunca commitar** (regra do repo).

Payload de referência (`CompleteRegistration`; `Subscribe` idem trocando nome/params):

```json
{
  "data": [{
    "event_name": "CompleteRegistration",
    "event_time": 1752105600,
    "event_id": "reg_<user_id>",
    "action_source": "website",
    "event_source_url": "https://aurapoker.com/signup/success",
    "user_data": {
      "em": ["<sha256 do email lowercase/trim>"],
      "client_ip_address": "<ip do request>",
      "client_user_agent": "<user-agent do request>",
      "fbp": "<cookie _fbp>",
      "fbc": "<cookie _fbc, se existir>"
    },
    "custom_data": { "content_name": "free_account" }
  }]
}
```

Regras:
- **Dedup:** `event_name` + `event_id` idênticos no browser e no server. Padrão de `event_id`: `reg_<user_id>` e `sub_<subscription_id>` (determinístico, idempotente em retry de webhook).
- `em` sempre sha256 de email normalizado (lowercase, sem espaços). IP/UA em claro (a API exige assim).
- Capturar `_fbp`/`_fbc` no form de cadastro e persistir junto do usuário — o webhook de pagamento (que dispara `Subscribe` dias depois) precisa deles para matching.
- `Subscribe` dispara no evento de pagamento confirmado do gateway (ex.: Stripe `checkout.session.completed` / `invoice.paid` do 1º ciclo), **uma vez por assinatura**.

## 4. UTM — captura e persistência

Convenção (alinhada ao plano de marketing; orgânico já usa `utm_source=instagram&utm_medium=organic&utm_campaign=launch20`):

| Param | Orgânico IG | Pago Meta |
|---|---|---|
| `utm_source` | `instagram` | `meta` |
| `utm_medium` | `organic` | `paid_social` |
| `utm_campaign` | `launch20` | nome da campanha (ex.: `rtg_br_launch20`) |
| `utm_content` | — | nome do criativo/anúncio |

Implementação (é o que liga o gasto ao KPI norte — conta free atribuída):
1. No primeiro pageview com UTM, persistir os params (localStorage ou cookie 1st-party, TTL 30d, **first-touch**: não sobrescrever se já existe).
2. No cadastro free, gravar os UTMs no registro do usuário (colunas/JSON em AuraBusiness).
3. Nos anúncios, as URLs já virão com UTM — o dev só precisa garantir que query params não são perdidos em redirects (inclusive www→apex e http→https).

## 5. Consentimento (LGPD/GDPR)

- Banner de cookies com opt-in ANTES de `fbq('init')` para tráfego EU; para BR, mínimo aviso + opt-out. Se a landing usa um CMP, pixel entra na categoria "marketing".
- Sem consentimento de marketing: não disparar pixel browser; CAPI só com dados que tenham base legal (na prática: não enviar).

## 6. Checklist de aceite (antes de 10/07)

- [ ] `PageView` chegando de `aurapoker.com`* em Events Manager → Eventos de teste (usar Test Code do dataset)
- [ ] `CompleteRegistration` browser+server com MESMO `event_id` → Events Manager mostra "Processado (deduplicado)"
- [ ] `Subscribe` server chegando no fluxo de pagamento de teste
- [ ] `_fbp`/`_fbc` persistidos no cadastro
- [ ] UTMs persistidos e gravados na conta criada (validar no AuraBusiness)
- [ ] Token CAPI em env var, fora do git
- [ ] Events Manager → Diagnóstico sem erros novos

\* **Pendência que o Rafael resolve no Business Manager (não é código):** confirmar o domínio final da landing; se for `aurapoker.com`, (a) aceitar o alerta "confirme o domínio" no Diagnóstico do dataset e (b) verificar o domínio no BM (Adequação e segurança → Domínios). Se a landing for em outro domínio/subdomínio, me avisar — muda o allowlist e a verificação.
