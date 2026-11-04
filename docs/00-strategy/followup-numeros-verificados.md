# Followup do Grátis: números verificados

Fonte única dos números do R1 e do R2 (frente A2, meta Aura 35 pagantes). Cada número tem fonte e hora de leitura. Não há e-mail neste arquivo: o cruzamento usou o md5 do e-mail. Plano e lotes: `followup-cadastrados-gratis.md` §14 e `followup-r2-lote-20261104.txt`.

## Leitura de 04/11/2026, por volta das 17h UTC

| Id | Número | R1 (`f185d44e`, 28/10 17:41 UTC) | R2 cupom VOLTE50 (`5cebc687`, 04/11 13:31 UTC) | R2 controle (`8616882a`, 04/11 13:37 UTC) | Fonte |
| --- | --- | --- | --- | --- | --- |
| N1 | Enviados | 185 | 143 | 37 | Resend `list-broadcast-recipients`: sent no controle; delivered mais bounced nos outros dois |
| N2 | Entregues | 182 | 142 | 37 | Resend, tipo delivered |
| N3 | Bounces | 3, transitórios | 1, transitório | 0 | Resend, tipo bounced |
| N4 | Abriram (destinatários únicos) | 34, ou 18,7% dos entregues | 15, ou 10,6% | 4, ou 10,8% | Resend, tipo opened |
| N5 | Aberturas (eventos) | 38 | 16 | 4 | Resend, tipo opened |
| N6 | Clicaram | 1 (link da landing, `utm_content=r1-a`) | 0 | 0 | Resend, tipo clicked e `list-broadcast-clicked-links` |
| N7 | Descadastros e reclamações | 0 e 0 | 0 e 0 | 0 e 0 | Resend, tipos unsubscribed e complained |
| N8 | Fizeram login depois do envio | 2 (Ids 322 e 357, os dois ainda em trial), 1 deles abriu o e-mail | 0 | 0 | `tbl_user.ultimo_login` (UTC assumido) cruzado por md5 com os entregues |
| N9 | Assinaram | 0 | 0 | 0 | Stripe: nenhuma assinatura criada depois de 27/10 (a última, do Id 371, é de 27/10 às 21:51 UTC); Woo: 2 pedidos desde 28/10, ambos renovações de pagantes que não estavam em nenhum lote |
| N10 | Usos do VOLTE50 | não se aplica | 0 de 184 | não se aplica | Stripe `promotion_codes`, VOLTE50 (`promo_1UXLEo…`), expira em 30/11 |
| N11 | Sessões no GA4 | 2 sessões e 2 usuários (`reativacao-gratis / r1-a`) | ainda não aparece | ainda não aparece | GA4 property 506294082, de 28/10 até hoje, origem email |

## O que estes números permitem dizer

- **R1, com 7 dias:** a abertura foi razoável (18,7%), mas o e-mail quase não gerou ação: 1 clique, 2 logins e nenhuma assinatura. Não dá para atribuir os 2 logins ao e-mail. O `ultimo_login` guarda só o último acesso, e só 1 dos 2 abriu o e-mail.
- **R2, com 3 a 4 horas:** é cedo demais para qualquer leitura. A abertura de 10,6% no cupom e de 10,8% no controle é parcial. A leitura que vale é a de 11/11 (logins em 7 dias) e a de 18/11 (assinaturas e usos do VOLTE50, cupom contra controle).
- **Limites da medição:**
  - O Resend não dá a data de cada abertura.
  - O login vem do `ultimo_login`, não do histórico de eventos.
  - O GA4 leva de 24 a 48 h para consolidar.
