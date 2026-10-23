# Reconquista de ex-pagantes: sequência de nov/2026

**Status:** rascunho para aprovação do Rafael. Nada enviado. Cupom `8YS32mA8` e código `VOLTA` criados no Stripe live em 23/10.
**Criado:** 22/10/2026 · **Sessão:** `aura · plano de marketing` · **Skills:** `emails`, `churn-prevention`
**Base:** decisões Q16 e D2 em `docs/00-strategy/entendimento-compartilhado-2026-11.md` e `docs/03-analytics/diagnostico-funil-2026-11.md`.

## Visão geral

| Campo | Valor |
| --- | --- |
| Nome | Reconquista 2026-11 |
| Público | **31 ex-pagantes** (pagaram e hoje não assinam em nenhum meio). Brasil 30, Portugal 1; BRL 29, USD 2; 22 com a última cobrança há mais de 6 meses. Contagem de 22/10 (Stripe × Woo × Resend, só agregados). |
| Gatilho | Lançamento da campanha na seg. 26/10 (Rafael, 23/10). Field Exploits (ex-Pool vs GTO) no ar desde 22/10: janela de 8 spots, toda segunda entram 2 novos e saem os 2 mais antigos (`release_rule.py`, `WINDOW = 8`, `PER_WEEK = 2`); 1.ª troca em 02/11 |
| Objetivo | Assinatura do Individual com o código da oferta. Meta do plano: 8 a 10 reconquistados. |
| Oferta | 80% de desconto no primeiro mês do plano Individual mensal (R$ 150 → R$ 30; US$ 29 → US$ 5,80), código `VOLTA`, de 26/10 a 16/11 |
| E-mails | 4: seg. 26/10, qui. 29/10, seg. 02/11 e dom. 16/11, às 10h de Brasília |
| Nome | O app só mostra "Field Exploits" depois do aura-novofront#187 (rascunho em 23/10, hoje a tela diz "Field Hotspots"). Se o #187 não estiver no ar na segunda, trocar o nome nos e-mails por "Field Hotspots". |
| Idioma | PT para os 31 (Portugal fala português). Os e-mails não citam preço em moeda, para servir a quem paga em BRL e em USD. |
| Saída | Assinou (checar Stripe, Woo e NOWPayments antes de cada envio), descadastrou ou deu bounce |
| Remetente | `Aura Poker Analytics <news@news.aurapoker.com>`, reply-to `manager@aurapoker.com` (padrão dos envios anteriores). Assinatura: ver decisão R2. |
| CTA | Landing `www.aurapoker.com` (decisão D2), com `utm_source=email&utm_medium=email&utm_campaign=reconquista-2026-11&utm_content=e<n>`. O `cta_click` da landing (aura-landing#26) precisa estar no ar antes de 02/11 para medir a passagem para o app. |

## Decisões do Rafael antes do envio

| # | Pergunta | Recomendação |
| --- | --- | --- |
| R1 | Cupom no Stripe | ✅ Feito em 23/10 (Rafael: "só no mensal o desconto valido pra 1 mes"). Cupom `8YS32mA8`: R$ 120 / US$ 23,20 fixos, uma cobrança, só no produto Individual, 40 usos, até 16/11 23:59. Código `VOLTA` (`promo_1UTnpAIsnKTRWBVcpVEV4Nm5`). O Stripe não limita cupom por preço: no semestral e no anual o desconto também é de R$ 120. |
| R2 | Quem assina | "Rafael, fundador da Aura" no lugar de "Equipe Aura". Ex-pagantes respondem mais a uma pessoa, e o e-mail 3 pede resposta. |
| R3 | Como enviar | Batch transacional do Resend com `List-Unsubscribe` (como em 30/09), sem criar segmento: o plano do Resend limita a 3 segmentos. A lista fica fora do git. |
| R4 | E-mail 2 | ✅ Números preenchidos em 23/10 a partir do `numeros-verificados.md` do Field Exploits (spot `utg_bb@25`, c-bet de 50%). Falta só a conferência logada do Rafael antes de 29/10. |

## E-mail 1: o que mudou (seg. 26/10, 10h)

**Assunto:** Desde que você saiu, a Aura ganhou o GTO
**Preview:** O Field Exploits mostra spots em que o field se afasta forte do GTO. Para quem já assinou, 80% de desconto no primeiro mês até 16/11.

---

Você já foi assinante da Aura. Escrevo porque o produto que você conheceu mudou bastante.

Hoje a Aura mostra o GTO ao lado do field:

- **Modo GTO:** o número e a faixa GTO ao lado do que o field faz, no flop, turn e river.
- **Field Ranges:** o range que o field abre e defende, mão a mão, comparado ao GTO.
- **Field Exploits:** 8 spots em que o field se afasta forte do GTO, em pares e stacks diferentes, cada um com o exploit pronto para usar. Toda segunda entram 2 novos.

Para quem já assinou, o primeiro mês do plano Individual mensal sai com **80% de desconto**, de R$ 150 por R$ 30, com o código **VOLTA** no checkout. Vale até 16/11.

**[Ver a nova Aura]**

O Modo GTO está incluso no plano Individual por tempo limitado.

Rafael
Fundador da Aura

---

## E-mail 2: um spot desta semana (qui. 29/10, 10h)

**Assunto:** Um spot em que o field erra contra o GTO esta semana
**Preview:** Um dos 8 spots do Field Exploits, com o número do field, o do GTO e o exploit.

> Números verificados (HUB, 23/10): `content/posts/field-exploits-launch/numeros-verificados.md` na main do aura-marketing, linhas 32 e 86–92 (`tbl_pool_vs_gto_rank` × `tbl_pool_vs_gto_release`, snapshot 20261015; ranking refeito sobre 20261022 com conteúdo idêntico). Spot `utg_bb@25`, `bet_50`, que também é o spot do Grátis. A janela vale até a troca de 02/11. Sem contagem de mãos no e-mail (regra de 08/10). ⛔ Gate R4: o Rafael confere logado antes do envio.

---

Um dos 8 spots do Field Exploits desta semana:

**UTG contra BB, 25bb, pote simples (SRP), flop A-high two-tone, sem par, com OESD possível. O UTG dá c-bet de 50%.**

O field folda **53,8%**. O GTO folda **73,5%** (faixa 67,5–79,5%).

**Como explorar:** o BB defende demais contra c-bet. Blefe menos e aposte mais por value.

É um spot, não a média do field. Os outros 7 estão no app.

O código **VOLTA** vale até 16/11: o primeiro mês do Individual mensal sai por R$ 30.

**[Ver os 8 spots]**

Rafael

---

## E-mail 3: 2 spots novos e uma pergunta (seg. 02/11, 10h)

**Assunto:** 2 spots novos hoje, e uma pergunta rápida
**Preview:** O Field Exploits ganhou spots novos. E eu queria saber o que te fez sair.

---

Hoje entraram 2 spots novos no Field Exploits.

Também queria te perguntar uma coisa: o que te fez cancelar a Aura? Pode ser uma linha só, respondendo este e-mail. Eu leio todas, e isso decide o que a gente constrói a seguir.

Se quiser voltar, o código **VOLTA** vale até domingo, 16/11.

**[Ver os spots novos]**

Rafael

---

## E-mail 4: último dia (dom. 16/11, 10h)

**Só para quem não assinou** (conferir no Stripe antes do envio).

**Assunto:** O código VOLTA vence hoje
**Preview:** 80% de desconto no primeiro mês do Individual, até 23:59 de hoje.

---

Último lembrete: o código **VOLTA** vence hoje às 23:59. Com ele, o primeiro mês do plano Individual mensal sai por R$ 30 em vez de R$ 150.

Desde 26/10, o Field Exploits recebeu 6 spots novos, cada um com o exploit.

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
2. ✅ O cupom e o código `VOLTA` estão criados no Stripe live (R1).
3. A lista foi refeita no dia: os 31, menos quem assinou, se descadastrou ou deu bounce.
4. Para o e-mail 2, os números foram conferidos logado (R4).
7. Aprovado pelo Rafael em 23/10 ("Restante aprovado"), com o lançamento na seg. 26/10.
5. A landing está no ar com o `cta_click` (aura-landing#26).
6. Primeiro um envio de teste para o Rafael, depois o envio real, em levas: 2 e depois os demais.
