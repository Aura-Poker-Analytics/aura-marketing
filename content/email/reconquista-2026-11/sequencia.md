# Reconquista de ex-pagantes: sequência de nov/2026

**Status:** rascunho para aprovação do Rafael. Nada enviado, nenhum cupom criado.
**Criado:** 22/10/2026 · **Sessão:** `aura · plano de marketing` · **Skills:** `emails`, `churn-prevention`
**Base:** decisões Q16 e D2 em `docs/00-strategy/entendimento-compartilhado-2026-11.md` e `docs/03-analytics/diagnostico-funil-2026-11.md`.

## Visão geral

| Campo | Valor |
| --- | --- |
| Nome | Reconquista 2026-11 |
| Público | **31 ex-pagantes** (pagaram e hoje não assinam em nenhum meio). Brasil 30, Portugal 1; BRL 29, USD 2; 22 com a última cobrança há mais de 6 meses. Contagem de 22/10 (Stripe × Woo × Resend, só agregados). |
| Gatilho | Lançamento do Pool vs GTO, seg. 02/11 |
| Objetivo | Assinatura do Individual com o código da oferta. Meta do plano: 8 a 10 reconquistados. |
| Oferta | Metade do primeiro mês, válida de 02/11 a 16/11 |
| E-mails | 4: 02/11, 05/11, 09/11 e 16/11, às 10h de Brasília |
| Idioma | PT para os 31 (Portugal fala português). Os e-mails não citam preço em moeda, para servir a quem paga em BRL e em USD. |
| Saída | Assinou (checar Stripe, Woo e NOWPayments antes de cada envio), descadastrou ou deu bounce |
| Remetente | `Aura Poker Analytics <news@news.aurapoker.com>`, reply-to `manager@aurapoker.com` (padrão dos envios anteriores). Assinatura: ver decisão R2. |
| CTA | Landing `www.aurapoker.com` (decisão D2), com `utm_source=email&utm_medium=email&utm_campaign=reconquista-2026-11&utm_content=e<n>`. O `cta_click` da landing (aura-landing#26) precisa estar no ar antes de 02/11 para medir a passagem para o app. |

## Decisões do Rafael antes do envio

| # | Pergunta | Recomendação |
| --- | --- | --- |
| R1 | Cupom no Stripe | Valor fixo de uso único com o mesmo valor de meio mês do Individual: R$ 75 em BRL e US$ 14,50 em USD (`currency_options`). Código de promoção `VOLTA`, validade até 16/11 23:59 (Brasília), máximo de 40 resgates. Valor fixo, e não 50%, porque o cupom vale para o produto Individual inteiro: 50% num plano anual daria R$ 647 de desconto. O checkout de produção aceita código (`AllowPromotionCodes = true`, binário `0813590`). |
| R2 | Quem assina | "Rafael, fundador da Aura" no lugar de "Equipe Aura". Ex-pagantes respondem mais a uma pessoa, e o e-mail 3 pede resposta. |
| R3 | Como enviar | Batch transacional do Resend com `List-Unsubscribe` (como em 30/09), sem criar segmento: o plano do Resend limita a 3 segmentos. A lista fica fora do git. |
| R4 | E-mail 2 | O spot do e-mail 2 sai dos 8 spots de 02/11, com números conferidos por você logado, no mesmo padrão dos `numeros-verificados`. Sem isso, o e-mail 2 não sai. |

## E-mail 1: o que mudou (seg. 02/11, 10h)

**Assunto:** Desde que você saiu, a Aura ganhou o GTO
**Preview:** Hoje entra o Pool vs GTO. Para quem já foi assinante, o primeiro mês volta pela metade até 16/11.

---

Você já foi assinante da Aura. Escrevo porque o produto que você conheceu mudou bastante.

Hoje a Aura mostra o GTO ao lado do field:

- **Modo GTO:** o número e a faixa GTO ao lado do que o field faz, no flop, turn e river.
- **Field Ranges:** o range que o field abre e defende, mão a mão, comparado ao GTO.
- **Pool vs GTO, a partir de hoje:** 8 spots onde o field mais se afasta do GTO, cada um com o exploit pronto para usar.

Para quem já assinou, o primeiro mês do plano Individual sai pela metade com o código **VOLTA**, até 16/11.

**[Ver a nova Aura]**

O Modo GTO está incluso no plano Individual por tempo limitado.

Rafael
Fundador da Aura

---

## E-mail 2: um spot desta semana (qui. 05/11, 10h)

**Assunto:** O spot onde o field mais se afasta do GTO esta semana
**Preview:** Um dos 8 spots do Pool vs GTO, com o número do field, o do GTO e o exploit.

> ⛔ Gate R4: os números entram só depois de conferidos logado no Pool vs GTO de 02/11. O texto abaixo é a forma; os `[...]` são preenchidos com os números da tela.

---

Um dos 8 spots que entraram no Pool vs GTO na segunda:

**[situação: posições, pote, stack, textura do flop, ação]**

O field [folda / paga / aposta] **[X]%**. O GTO [folda / paga / aposta] **[Y]%** (faixa [a]–[b]%).

**Como explorar:** [frase do exploit da tela, no tom "When villain calls, bluff less and bet mostly for value on the flop."]

É um spot, não a média do field. Os outros 7 estão no app.

O código **VOLTA** vale até 16/11: o primeiro mês do Individual sai pela metade.

**[Ver os 8 spots]**

Rafael

---

## E-mail 3: 8 spots novos e uma pergunta (seg. 09/11, 10h)

**Assunto:** Mais 8 spots hoje, e uma pergunta rápida
**Preview:** O Pool vs GTO ganhou spots novos. E eu queria saber o que te fez sair.

---

Hoje entraram mais 8 spots no Pool vs GTO.

Também queria te perguntar uma coisa: o que te fez cancelar a Aura? Pode ser uma linha só, respondendo este e-mail. Eu leio todas, e isso decide o que a gente constrói a seguir.

Se quiser voltar, o código **VOLTA** vale até domingo, 16/11.

**[Ver os spots novos]**

Rafael

---

## E-mail 4: último dia (dom. 16/11, 10h)

**Só para quem não assinou** (conferir no Stripe antes do envio).

**Assunto:** O código VOLTA vence hoje
**Preview:** Metade do primeiro mês do Individual, até 23:59 de hoje.

---

Último lembrete: o código **VOLTA** vence hoje às 23:59. Com ele, o primeiro mês do plano Individual sai pela metade.

Desde o dia 2, o Pool vs GTO já tem 16 spots com o exploit de cada um.

**[Voltar para a Aura]**

Depois disto, não mando mais nada sobre essa oferta.

Rafael

---

## Medição

| Métrica | Fonte | Referência |
| --- | --- | --- |
| Entregues, aberturas, cliques | Resend, por e-mail | — |
| Passagem para o app | GA4: `cta_click` com `utm_campaign=reconquista-2026-11` (depende do aura-landing#26 no ar) | — |
| Reconquistados | Stripe: resgates do código `VOLTA` | meta de 8 a 10 dos 31 |
| Motivos de saída | Respostas ao e-mail 3, registradas sem dado pessoal em `docs/03-analytics/` | entrada para a fase 3 e para o `customer-research` |

## Checklist de envio (para cada e-mail)

1. O Rafael aprovou o texto do e-mail.
2. O cupom e o código `VOLTA` estão criados no Stripe live (R1).
3. A lista foi refeita no dia: os 31, menos quem assinou, se descadastrou ou deu bounce.
4. Para o e-mail 2, os números foram conferidos logado (R4).
5. A landing está no ar com o `cta_click` (aura-landing#26).
6. Primeiro um envio de teste para o Rafael, depois o envio real, em levas: 2 e depois os demais.
