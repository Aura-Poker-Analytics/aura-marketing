# E-mail: lançamento do Field Ranges (Beta)

Status: rascunho para aprovação do Rafael. Não enviado.
Único número usado: BTN 56,9% e EP 39,0% de fold contra 3-bet não all-in (`numeros-verificados.md` §3, rodapé de decisões, dentro do quadro Onde explorar). O exemplo "CO abre, SB dá 3-bet all-in" é só o spot, sem frequência.
HTML pronto: `email-pt.html` e `email-en.html` (mesma pasta).

---

## PT

**Assunto (2 opções)**
1. Field Ranges chegou, em Beta
2. CO abre, SB dá 3-bet all-in: como o field responde

**Recomendado: a 2.** Traz o spot concreto na própria linha; a 1 é só anúncio. (O `<title>` do HTML usa a 2.)

**Preheader:** Field Ranges (Beta): uma grade 13x13 por spot, mão a mão. Abra um spot que você joga e conte o que faltou.

**Corpo (texto)**

Selo: BETA

Field Ranges: veja como o field responde, mão a mão.
Uma grade 13x13 por spot pré-flop.

Cada célula é uma mão, e a cor mostra o que o field faz com ela. Você segue a trilha open, 3-bet, 4-bet, all-in, escolhe as posições na mesa e filtra por stack e buy-in.

Exemplo: o CO abre e o SB dá 3-bet all-in. A grade mostra a resposta do CO, mão a mão: quais mãos pagam e quais folda. Contra all-in não existe raise, só call ou fold, então a leitura é direta: você vê onde o field defende mais ou menos e ajusta o seu all-in a partir daí.

[imagem] Legenda: CO abre, SB dá 3-bet all-in: a resposta do CO, mão a mão. Azul paga, cinza folda.

Onde explorar: BTN folda 56,9% e EP 39,0% contra 3-bet (não all-in). Mesma ação, field diferente por posição: contra o BTN o seu 3-bet tende a ter mais fold equity; contra o EP, pede mais critério.

Está em Beta, e a sua leitura conta. Abra um spot que você joga e diga o que faltou ou o que ficou confuso: é só responder este e-mail ou falar com a gente no Discord (https://discord.gg/wYquSmUtAK).

Botão: Abrir o Field Ranges
Sob o botão: Com a sua conta grátis. Poker é jogo de habilidade e estudo. 18+.

---

## EN

**Subject (2 options)**
1. Field Ranges is here, in Beta
2. CO opens, SB 3-bets all-in: how the field responds

**Recommended: 2.** Same reason as PT: concrete spot in the subject line. (The HTML `<title>` uses it.)

**Preheader:** Field Ranges (Beta): a 13x13 grid for every spot, hand by hand. Open a spot you play and tell us what is missing.

**Body (text)**

Badge: BETA

Field Ranges: see how the field responds, hand by hand.
A 13x13 grid for every preflop spot.

Each cell is a hand, and the color shows what the field does with it. You follow the trail open, 3-bet, 4-bet, all-in, pick positions on the table and filter by stack and buy-in.

Example: the CO opens and the SB 3-bets all-in. The grid shows the CO's response, hand by hand: which hands call and which fold. Against an all-in there is no raise, only call or fold, so the read is direct: you see where the field defends more or less and adjust your all-in from there.

[image] Caption: CO opens, SB 3-bets all-in: the CO's response, hand by hand. Blue calls, gray folds.

Where to exploit: BTN folds 56.9% and EP 39.0% facing a 3-bet (not all-in). Same action, different field by position: against the BTN your 3-bet tends to carry more fold equity; against EP, it needs more care.

It is in Beta, and your read counts. Open a spot you play and tell us what is missing or confusing: just reply to this email or talk to us on Discord (https://discord.gg/wYquSmUtAK).

Button: Open Field Ranges
Under the button: With your free account. Poker is a game of skill and study. 18+.

---

## Nota técnica

- **Imagem:** o arquivo a hospedar é `content/posts/field-ranges-launch/mockups/grade-allin-pt.png` (PT) e `mockups/grade-allin-en.png` (EN). Publicar como `https://www.aura.poker/email/field-ranges-grade-allin-pt.png` e `.../field-ranges-grade-allin-en.png` (hospedadas, não anexos). Os HTMLs usam width=532 e height=596 (proporção do mockup, ~1316x1475); conferir a altura se o arquivo for reexportado. O alt é o do mockup grade-allin da seção Landing do `copy.md`. A imagem também é link para o CTA.
- **Logo:** `https://www.aura.poker/email/aura-logo.png` (já hospedado, do padrão).
- **Link do CTA:**
  - PT: https://www.aura.poker/?utm_source=email&utm_medium=email&utm_campaign=field-ranges-launch&utm_content=pt
  - EN: https://www.aura.poker/?utm_source=email&utm_medium=email&utm_campaign=field-ranges-launch&utm_content=en
- **Descadastro:** placeholder `{{{RESEND_UNSUBSCRIBE_URL}}}` no rodapé, exatamente como no padrão; substituído pelo Resend no envio.
- **Padrão seguido:** `aura-main/aura-marketing/content/email/reativacao-conta-gratis.html` (600px, tabelas, estilos inline, preheader oculto, botão âmbar `#D4A418`). Ajustes: selo BETA no cabeçalho, rótulo "Fale com a gente" na linha de links (Discord, WhatsApp, YouTube), 18+ no rodapé.
- **Remetente e reply-to:** o convite diz "responda este e-mail", então o reply-to tem de ser uma caixa lida (padrão anterior: `manager@aurapoker.com`). Confirmar antes do envio.
- **Não enviado.** Envio e lista são do Rafael.
