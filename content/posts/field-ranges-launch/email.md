# E-mail: lançamento do Field Ranges

Status: rascunho para aprovação do Rafael. Não enviado.
Único número usado: 1,42 bi de decisões pré-flop, 20bb+ (`numeros-verificados.md` §1), na linha "Dados: Aura · 1,42 bi de decisões · 20bb+". Sem frequência de fold, sem selo de fase nem pedido de feedback.
HTML pronto: `email-pt.html` e `email-en.html` (mesma pasta).

---

## PT

**Assunto (2 opções)**
1. Field Ranges chegou à Aura
2. Novo na Aura: o field, mão a mão

**Recomendado: a 1.** Anuncia o lançamento e nomeia o módulo, sem rodeio. (O `<title>` do HTML usa a 1.)

**Preheader:** Novo módulo da Aura: como o field joga cada mão no pré-flop, numa grade 13x13.

**Corpo (texto)**

Field Ranges chegou.
Novo módulo da Aura: como o field joga cada mão no pré-flop.

Uma grade 13x13, uma célula por mão. Você segue a trilha open, 3-bet, 4-bet e all-in numa mesa de 6 lugares e filtra por stack e buy-in.

Serve para ver onde o field joga diferente, mão a mão, e explorar isso na mesa.

Dados: Aura · 1,42 bi de decisões · 20bb+

Botão: Acesse grátis
Sob o botão: Com a sua conta grátis. Poker é jogo de habilidade e estudo. 18+.

---

## EN

**Subject (2 options)**
1. Field Ranges is live on Aura
2. New on Aura: the field, hand by hand

**Recommended: 1.** Announces the launch and names the module. (The HTML `<title>` uses it.)

**Preheader:** New Aura module: how the field plays every hand preflop, on a 13x13 grid.

**Body (text)**

Field Ranges is live.
New Aura module: how the field plays every hand preflop.

A 13x13 grid, one cell per hand. You follow the trail open, 3-bet, 4-bet and all-in on a 6-seat table and filter by stack and buy-in.

Use it to see where the field plays differently, hand by hand, and exploit it at the table.

Data: Aura · 1.42B decisions · 20bb+

Button: Get free access
Under the button: With your free account. Poker is a game of skill and study. 18+.

---

## Nota técnica

- **Imagem:** a grade 13x13 do app (`email/field-ranges-pt.png` e `-en.png`, 1200 px de largura, exibida a 552 px, fundo #0b1220, sem transparência), logo abaixo do texto e antes do botão. Só o cartão da grade com a legenda, sem título de spot, sem selo de fase e sem percentuais. Hospedar em `https://www.aurapoker.com/email/` antes do envio. Os `*.preview.html` usam o caminho relativo `email/` para abrir do disco.
- **Logo:** `https://www.aura.poker/email/aura-logo.png` (já hospedado).
- **Link do CTA (sempre a landing, nunca o app/login; `www.aurapoker.com` com www):**
  - PT: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=field-ranges-launch&utm_content=pt
  - EN: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=field-ranges-launch&utm_content=en
  - Só o logo continua hospedado em `https://www.aura.poker/email/` (padrão dos e-mails existentes); não é link de destino.
- **Descadastro:** placeholder `{{{RESEND_UNSUBSCRIBE_URL}}}` no rodapé, substituído pelo Resend no envio.
- **Layout:** 600px, tabelas, estilos inline, preheader oculto, botão âmbar `#D4A418`, linha de canais (Discord, WhatsApp, YouTube) e 18+ no rodapé, como na versão anterior.
- **Reply-to:** o e-mail não pede resposta, mas o remetente continua sendo o do padrão anterior (`manager@aurapoker.com` como reply-to). Confirmar antes do envio.
- **Não enviado.** Envio e lista são do Rafael.
