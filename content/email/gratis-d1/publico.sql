-- Público do e-mail do dia seguinte (Grátis D1, Q23 aprovada em 04/11/2026). Só leitura, no AuraBusiness.
-- Conta Grátis ativa, criada há 20 a 28 h (create_date em UTC), sem 2º login (ultimo_login no mesmo dia do cadastro, ou nulo).
-- Fora: contas internas e de agentes, superuser e quem tem assinatura.
-- Fora também, no momento do envio e fora do SQL: e-mail na supressão do Resend (list-suppressions) e contato com unsubscribed=true
-- (get-contact; 404 = não é contato, pode receber). O batch transacional não filtra isso sozinho (regra de 15/10).
-- Nunca repetir: antes de enviar, tirar quem já está em content/email/gratis-d1/enviados-ids.txt (só Ids).
-- Idioma: PT para country BR, PT, AO ou MZ; EN para os demais países; PT quando o país é nulo (o tbl_user não guarda o idioma do cadastro).
select "Id",
       email,
       create_date,
       ultimo_login,
       country,
       case when coalesce(upper(country), 'BR') in ('BR', 'PT', 'AO', 'MZ') then 'pt' else 'en' end as lang
from public.tbl_user
where trial = true
  and plan_tier = 'trial'
  and active = true
  and coalesce(superuser, false) = false
  and stripe_subscription_id is null
  and coalesce(time, '') <> 'agentes-internos'
  and lower(email) not like '%@aurapoker.com'
  and create_date >= (now() at time zone 'utc') - interval '28 hours'
  and create_date <  (now() at time zone 'utc') - interval '20 hours'
  and (ultimo_login is null or ultimo_login::date = create_date::date)
order by create_date;
