# AURA-036: form curto e 30 dias de Aura sem cartão para quem responder

**Data:** 09/11/2026 · **Pedido do Rafael (via HUB):** "dispara o email, dando um mes de graça na Aura sem cartão de credito pra quem preencher o form com no minimo x caracteres" · **Meta que move:** Aura, 35 pagantes em 31/12 e cadastros ≥ 10 por semana (`_ops/metas-trimestre.md`). O objetivo imediato é entender por que 0 de 32 cadastros da SINAL01 abriram o checkout.
**Estado:** rascunho. **Nada foi enviado, executado ou gravado no AuraBusiness.** O comando da §3 é texto: só roda com a frase do Rafael. O "x" ficou em aberto: o padrão da HUB é **150 caracteres somados** nas respostas abertas, e o Rafael pode trocar.
**Marcas:** `[medido: fonte, data]`, `[inferido]`, `[não conferido]`.

## 1. Quem recebe (só contagem)

32 cadastros da SINAL01 (`utm_source=meta`, `utm_campaign=aura-sinal01`, desde 29/10), todos Grátis ativos, sem Stripe, sem `subscription_id`, sem `billing_provider`, sem fim de período, nenhum superusuário [medido: `tbl_user`, SELECT agregado, 09/11].

| Corte | PT | EN | Total |
| --- | --- | --- | --- |
| **Pelo país do cadastro (regra do Rafael de 02/11: PT só BR e PT)** | **26** (BR) | **6** (VE, GB, AT, DE) | 32 |
| Pelo criativo do anúncio (o que a HUB mandou) | 27 | 5 | 32 |

A diferença é 1 pessoa: a de Venezuela veio de anúncio em português, e a regra do país a manda para EN [medido: `tbl_user.country` e `utm_content`, 09/11]. **O plano usa o país: 26 em PT e 6 em EN.** Nenhum e-mail está neste doc nem vai ao git.

**Sobreposição com o A1:** 16 dos 32 estão no lote de 18 do A1 (que ainda não saiu) [medido: ids do `lote-2026-11-01.csv` × a lista dos 32, 09/11]. Pela regra do calendário (uma pessoa, uma sequência; 1 e-mail a cada 3 dias), **este e-mail do form entra no lugar do A1 para essas pessoas**: o A1 não foi enviado. Os outros 2 do lote (link da bio) seguem na escada normal. Quem recebe o form só entra no A2 e no A3 depois de 3 dias do form, e só se não respondeu. **Linha proposta para o `_ops/email-calendario-2026-11.md` (a HUB aplica; fica fora da pasta desta sessão):** na linha "Cadastros novos da Meta", trocar "A1 com o sim do Rafael" por "**AURA-036: e-mail de 30 dias na Aura (resposta ao e-mail ou form) no lugar do A1 para os 32 da SINAL01 (26 em português e 6 em inglês); o A1 segue só para os 2 do link da bio; A2 e A3 só 3 dias depois do pedido AURA-036 e só para quem não respondeu**".

## 2. Versão escolhida: responder o e-mail (o form foi descartado em 09/11)

**O Rafael escolheu "Responder o e-mail" em 09/11.** Valem `resp-pt.html` e `resp-en.html`, com o assunto e a primeira linha nas palavras dele (PT 54 caracteres, acima dos 50 da regra; EN 59). Os arquivos `form-*.html` saíram do PR. O texto abaixo sobre o form fica só como registro.

### 2.0 Como era a proposta das duas versões

A HUB propôs (09/11) trocar o form por **"responda este e-mail"** com as mesmas perguntas: não depende de ferramenta nova e a resposta chega pelo e-mail de resposta do batch `[não conferido: o reply-to precisa ser uma caixa lida ou o inbound do Resend; hoje é manager@aurapoker.com]`. O Rafael escolhe. As duas peças estão prontas: `resp-pt.html` e `resp-en.html` (botão abre a resposta) e `form-pt.html` e `form-en.html` (botão para `[LINK DO FORM]`). Na versão por e-mail a soma de 150 caracteres é conferida lendo a resposta, sem planilha; o `Id` sai do remetente, por SELECT no dia, sem gravar e-mail em arquivo.

### 2.1 O form (3 perguntas obrigatórias e 1 opcional), se o Rafael preferir form

**Ferramenta: ainda não existe.** Não há form criado em nenhum lugar do hub nem na landing (busca por Tally e Google Forms em `aura-landing/src` e `aura-marketing`: 0 resultados) [medido: grep, 09/11], e esta sessão não tem ferramenta que crie Google Forms ou Tally. **Quem cria é o Rafael ou a HUB**, em Google Forms (aceita validação por tamanho de texto e grava o e-mail do respondente). O texto abaixo é para colar.

**Título:** Dois minutos para a Aura ficar melhor (e 30 dias do Individual para você)
**Texto de abertura:** Você abriu a conta na Aura e não assinou. Responda com sinceridade. Quem responder com pelo menos 150 caracteres no total ganha 30 dias do plano Individual na conta, sem cartão de crédito. Eu leio tudo.

| # | Pergunta (resposta longa) | Obrigatória | Validação |
| --- | --- | --- | --- |
| 0 | E-mail da sua conta na Aura (o mesmo do cadastro) | sim | e-mail; coletar o e-mail do respondente |
| 1 | O que você esperava da Aura quando se cadastrou? | sim | texto com no mínimo 40 caracteres |
| 2 | O que achou difícil ou confuso no uso? | sim | texto com no mínimo 40 caracteres |
| 3 | O que faltou para você assinar? | sim | texto com no mínimo 40 caracteres |
| 4 | O que você mudaria na Aura? | não | — |

**Como se aplica o "150 somados":** o Google Forms não soma campos. A validação por pergunta (40 + 40 + 40 = 120 no mínimo) impede resposta vazia, e a soma de 150 é conferida na planilha de respostas: `=LEN(B2)+LEN(C2)+LEN(D2)+LEN(E2)>=150`. Só ganha o mês quem fecha 150 [inferido: o Rafael pode trocar o número; a planilha é só uma coluna]. A planilha de respostas tem e-mail: fica no Google do Rafael, **nunca no git**.
**Versão EN:** o mesmo form em inglês, para os 6 de EN (um segundo link; o texto vem do e-mail em EN). 

## 3. O mecanismo da recompensa: 30 dias do Individual na conta

### 3.1 Como a conta vira Individual hoje [medido: código e banco, 09/11]

- O app lê o plano pelo `trial` (claim `trial` no token, `AuthService.cs:35`) e por `active`. Grátis é `trial = true`. Individual é `trial = false` com `active = true`. O plano pago grava `subscription_id = '1'` (enum `Plan.Individual`).
- Quando um pagamento avulso (cripto) é creditado, o código faz exatamente isto (`AvulsoSubscriptionCredit.cs`): `trial = false`, `active = true`, `fromTrial` = o `trial` anterior, `subscription_id = '1'`, `billing_provider`, `renewal_reminder_stage = 0` e `subscription_period_end` = agora + duração. Estender a partir de um fim ainda futuro soma ao que resta.
- **O rebaixamento automático só existe para `billing_provider = 'nowpayments'`** (`RenewalReminderService.cs`: seleciona `billing_provider == "nowpayments"` e, passado o período mais 3 dias, volta `trial = true`; também manda os e-mails de renovação). Qualquer outro provedor **não volta sozinho para o Grátis**. Um 30 dias com outro valor precisa de um passo de volta agendado (§3.4).
- **Na `main` do `aura_api` o plano que vale é o `plan_tier`** (não só o `trial`): o token carrega o claim `plan_tier`, e `RequireTier` (Modo GTO, Field Exploits, Field Ranges com GTO, Coach) lê esse claim. `PlanTierWriter` mantém a regra `trial = true` se e só se `plan_tier = 'trial'`; `trial = false` exige `plan_tier` em individual, gto ou top (`PlanTierWriter.cs`). **O comando ajusta os dois juntos, e o `plan_tier = 'individual'` é obrigatório, não cosmético.** O token novo sai no próximo login ou renovação (`AuthController`: reemissão a partir do `tbl_user`) `[medido: código, origin/main do aura_api, 09/11]`. A guarda do checkout (só bloqueia `nowpayments`) e a estrutura de `showSubscribeFlow` e `isLegacyManagedSubscription` no front foram conferidas também em `origin/main` do `aura_api` e do `aura-novofront`.
- Os 32 estão limpos: nenhum tem `subscription_id`, `billing_provider`, fim de período ou Stripe [medido: SELECT agregado, 09/11].

### 3.2 Por que `billing_provider = 'cortesia-aura036'`, e não `nowpayments`

Com `nowpayments` o serviço de renovação mandaria e-mails de "renove pela aba Cripto" a quem nunca pagou, e voltaria o plano sozinho, mas também tocaria quem pagou de verdade. Um valor próprio marca a cortesia, **não entra na contagem de pagantes** (a contagem oficial exige pagamento confirmado, `metas-trimestre.md`; quem lê a meta deve excluir `billing_provider like 'cortesia%'`) e permite desfazer só ela.

### 3.3 O comando (NÃO EXECUTAR: escrita no AuraBusiness, só com a frase do Rafael)

`:ids` é a lista de `Id` dos respondentes que fecharam 150 caracteres. A ligação entre o e-mail do form e o `Id` é feita no dia, por quem executa, com um SELECT por e-mail, **sem gravar e-mail em arquivo nem no git**.

```sql
BEGIN;

-- backup só do que vai mudar (DDL aditiva, IF NOT EXISTS)
CREATE TABLE IF NOT EXISTS aura036_backup (
  "Id" integer PRIMARY KEY,
  trial boolean, active boolean, plan_tier text, subscription_id varchar,
  billing_provider text, subscription_period_end timestamptz,
  renewal_reminder_stage integer, concedido_em timestamptz DEFAULT now()
);

INSERT INTO aura036_backup ("Id", trial, active, plan_tier, subscription_id, billing_provider,
                            subscription_period_end, renewal_reminder_stage)
SELECT "Id", trial, active, plan_tier, subscription_id, billing_provider,
       subscription_period_end, renewal_reminder_stage
FROM tbl_user
WHERE "Id" = ANY(:ids)
  AND plan_tier = 'trial' AND trial AND active
  AND subscription_id IS NULL AND billing_provider IS NULL
  AND stripe_customer_id IS NULL AND stripe_subscription_id IS NULL
  AND COALESCE(superuser, false) = false
ON CONFLICT ("Id") DO NOTHING;

UPDATE tbl_user u
SET trial = false,
    plan_tier = 'individual',
    subscription_id = '1',
    billing_provider = 'cortesia-aura036',
    subscription_period_end = now() + interval '30 days',
    renewal_reminder_stage = 0
FROM aura036_backup b
WHERE u."Id" = b."Id"
  AND u.billing_provider IS NULL
RETURNING u."Id", u.subscription_period_end;

-- conferir: o número de linhas é igual ao de respondentes elegíveis e nenhuma linha é de Stripe.
-- Se bater: COMMIT;  Se não: ROLLBACK;
```

**Guardas:** só muda quem está limpo (Grátis, ativo, sem provedor, sem Stripe, não superusuário); o `ON CONFLICT DO NOTHING` e `billing_provider IS NULL` tornam o comando seguro de rodar duas vezes; `active` não muda; nenhum e-mail é enviado pelo banco (o "trial virou assinatura" só sai pelo serviço, não por SQL).

### 3.4 Rollback e volta aos 30 dias

```sql
-- Rollback imediato (desfaz a concessão, mesmo antes de 30 dias):
BEGIN;
UPDATE tbl_user u
SET trial = b.trial, active = b.active, plan_tier = b.plan_tier,
    subscription_id = b.subscription_id, billing_provider = b.billing_provider,
    subscription_period_end = b.subscription_period_end,
    renewal_reminder_stage = b.renewal_reminder_stage
FROM aura036_backup b
WHERE u."Id" = b."Id" AND u.billing_provider = 'cortesia-aura036'
RETURNING u."Id";
COMMIT;  -- conferir as linhas antes
```

**Volta aos 30 dias (obrigatória, o app não volta sozinho):** o mesmo `UPDATE`, rodado em D+30 com os filtros extras `AND u.subscription_period_end <= now() AND u.stripe_subscription_id IS NULL AND u.stripe_customer_id IS NULL`. Quem assinou nesse meio tempo pelo Stripe **não é tocado** (tem `stripe_subscription_id`). **O checkout do Stripe não limpa o `billing_provider`** (`BillingService.cs`, conclusão do checkout só grava `stripe_customer_id` e os dados da assinatura), então um pagante vindo da cortesia continua com `billing_provider = 'cortesia-aura036'`: por isso a contagem de pagantes não pode excluir só `cortesia%` e a volta precisa dos dois filtros do Stripe. Agendar essa volta no dia da concessão (tarefa agendada, só com a frase do Rafael para rodar). **O agendamento é condição para conceder o primeiro mês:** sem ele a frase "ao fim a conta volta ao Grátis" do e-mail seria falsa.

### 3.4b Passo antes da concessão: rótulo do `billing_provider` que não vaza na tela

O front (`aura-novofront` na `main`) **só compara** `billingProvider` com `'nowpayments'` e `'stripe'` (`MinhaConta.tsx`, `CryptoSubscriptionPanel.tsx`) e nunca o escreve na tela `[medido: código, 09/11]`. O valor `cortesia-aura036` cai no ramo "assinante legado gerenciado" e não aparece. **Fica `cortesia-aura036`.** Reconferir na tela, com a conta dos agentes, junto com a frase do SQL, e se algum texto novo passar a exibir o campo, trocar por um valor neutro (ex.: `cortesia`).

### 3.5 Riscos e o que o código já responde

Teste com a conta dos agentes **não feito**: ele exige um `UPDATE` no AuraBusiness. Esta sessão só tem leitura no banco, e escrita no AuraBusiness é da lista do Rafael (R-002). O que se pôde conferir lendo o `aura_api` (`BillingService.cs`), com `[medido: código, 09/11]`:

1. **Checkout para quem está em cortesia: a API abre, a tela esconde.** `CreateCheckoutSessionAsync` só bloqueia `billing_provider = 'nowpayments'` ativo e não trial; um provedor próprio passa. No front (`aura-novofront`, `MinhaConta.tsx`), `showSubscribeFlow` vem do `isTrial` do token: com `trial = false` o fluxo de assinar some, e quem tem `hasSubscription` sem assinatura do Stripe cai no painel de "assinante legado gerenciado" (`isLegacyManagedSubscription`), com a data do fim. **Durante os 30 dias a pessoa não vê o botão de assinar pela tela de conta**; ao voltar ao Grátis (D+30) o fluxo volta. O token só muda no próximo login `[medido: código, 09/11]`. Isso é um custo da oferta: quem quiser assinar antes do fim não tem caminho na tela.
2. **Status do app para a cortesia:** `HasSubscription = true`, `IsActive = true`, `PlanName = Individual`, `CurrentPeriodEnd` = o fim dos 30 dias, `BillingProvider` devolvido como o valor cru `cortesia-aura036` (não é "stripe" nem "nowpayments"). Se a tela mostrar esse texto, aparece um nome interno ao usuário `[não conferido]`.
3. **`plan_tier`:** na `main` é o claim que libera Modo GTO e Field Exploits; o comando o escreve junto com `trial` e respeita a regra do `PlanTierWriter`. O `PlanTierWriter` não mexe em `subscription_id`; o comando o grava como `'1'` para que a tela de conta enxergue a assinatura (a conta legada com `hasSubscription` precisa dele) `[inferido]`. A volta em D+30 desfaz os dois juntos pelo backup. **Falta só o teste real na tela, com a conta dos agentes, junto com a frase do SQL** `[não conferido]`.
4. **Contagem de pagantes:** depende da consulta de cada painel `[não conferido]`. Regra segura: não é pagante quem tem `billing_provider like 'cortesia%'` **e** `stripe_subscription_id is null`.
5. **Sem e-mail:** o `UPDATE` direto não dispara o e-mail "trial virou assinatura"; o app não avisa a pessoa da data. O e-mail da recompensa precisa dizer os 30 dias.

## 4. O e-mail

Texto em `content/email/form-30dias/email.md` (PT e EN, pelo `casa:copywriter`; revisão do `casa:revisor` em `notas.md`). **Nenhum código de cupom, nenhum preço.** O botão leva ao form.
**Exceção ao R-037 (CTA de e-mail na landing):** aqui o CTA é o form (versão A) ou a resposta ao e-mail (versão B, `mailto`, sem UTM; a medição vem da contagem de respostas), fora da landing; o link leva `utm_campaign=form-30dias&utm_content=<idioma>` para o GA4 ler o clique. Pedir à HUB que confirme a exceção.
**Envio:** a broadcast do Resend exige um segmento, e o plano tem 3. O segmento `65da31a5` (liberado para a ativação Meta) é **um só** e não separa PT de EN. Recomendação: **envio por batch transacional** (padrão do R1 e do R3 da reconquista, com `List-Unsubscribe`), PT para 26 pessoas e EN para 6, com a mesma peça. Os dois rascunhos no Resend ficam apenas como prévia, nomeados "NÃO ENVIAR (envio por batch)". O envio é do Rafael, com o "sim" digitado nesta sessão (R-007).

## 4b. Reply-to e o batch (preparação, nada enviado)

- **Reply-to: `manager@aurapoker.com`**, o mesmo dos envios anteriores. **Conferido no Resend em 09/11:** o domínio `news.aurapoker.com` tem *Receiving disabled* e a conta tem **0 inboxes**, então as respostas **não** chegam pelo inbound do Resend. Elas dependem da caixa `manager@aurapoker.com` ser lida pelo Rafael `[não conferido: nenhuma ferramenta desta sessão lê essa caixa]`. Para o envio sair, o Rafael confirma que lê essa caixa, ou o Resend passa a receber (ligar *Receiving*, é mudança de DNS e configuração dele).
- **Batch:** `send-batch-emails`, um e-mail por pessoa, 26 com `resp-pt` (assunto PT) e 6 com `resp-en` (assunto EN), remetente `Aura Poker Analytics <news@news.aurapoker.com>`, reply-to acima, `List-Unsubscribe`. Os e-mails dos 32 saem do `tbl_user` (SELECT por `Id`, país BR ou PT = PT, resto = EN) **só no momento do envio**, em memória, sem arquivo nem git. Antes: tirar quem já assinou ou descadastrou.
- **Frase de envio, do Rafael nesta sessão:** "AURA-036 sim: enviar a pesquisa (versão resposta) aos 32 da SINAL01, 26 em português e 6 em inglês". Só com ela e com o reply-to conferido.

## 5. Ordem de execução (nada acontece antes das duas frases)

| # | Passo | Quem | Precisa de |
| --- | --- | --- | --- |
| 1 | Criar o form em PT e EN, copiar o link | Rafael ou HUB | — |
| 2 | Trocar `[LINK DO FORM]` nos dois e-mails e regenerar | esta sessão | o link |
| 3 | Testar a concessão numa conta de teste dos agentes | esta sessão | frase do Rafael só se tocar produção; teste em conta dos agentes |
| 4 | Enviar o e-mail, em português para 26 e em inglês para 6 (batch) | esta sessão | **sim do Rafael digitado aqui** (R-007) |
| 5 | A cada resposta: conferir 150 caracteres na planilha | Rafael ou HUB | — |
| 6 | Rodar o comando da §3.3 com os `Id` aprovados | esta sessão | **frase do Rafael** (escrita no AuraBusiness) |
| 7 | Agendar a volta aos 30 dias (§3.4) | esta sessão | idem |
| 8 | Ler resultado D+3 e D+7: respostas, motivos de não assinar, assinaturas | casa:growth | — |

**Leitura honesta:** o form tem poucas respostas esperadas (32 pessoas). É uma entrevista, não um teste. [inferido] Com a resposta ao e-mail da Aura em torno de 10% a 20%, esperar de 3 a 6 respostas.
