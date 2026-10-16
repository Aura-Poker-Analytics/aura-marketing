# E-mail: lançamento do Modo GTO (GTO no flop, turn e river, com as aberturas do agressor)

Status: rascunho sem marcadores abertos; não publicado. Não enviado, e nada foi criado no Resend. Versão de 15/10/2026 (anuncia "no ar" e a inclusão do GTO no Individual por tempo limitado, decisão do Rafael via HUB), números fechados em 14/10. **O Rafael aprovou, direto, em 15/10, o assunto e o corpo do e-mail (PT e EN); o corpo não muda.**
Números: exemplo (a) de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10): field folda 46,0%, GTO folda 38,8%. A cobertura segue `aura-main/_ops/golive-gto-2026-10-14/numeros-verificados-lancamento.md` (14/10). Um exemplo só (CO × BB) e uma comparação só (field contra GTO). Sem número de escala, sem pré-flop concreto, sem contagem de mãos, sem o exemplo de abertura.
**Só enviar depois do teste logado do Rafael, do P-61 no ar (Modo GTO aberto ao Individual), da conferência do preço (29 / 150) no Stripe pelo Rafael, do GATE B1 (data interna a honrar e reconciliação da landing publicada, sessão do aura-landing), do GATE A2 (amostra do GTO na conta grátis), do **GATE P-53** (o teste logado do Rafael confirma que a visão Field vs GTO está ligada em produção para o Individual e que o AA mostra +21 (20,9 pp arredondado) e as marcas 132 / 148 / 74 do SB RFI 50bb+; a imagem do e-mail mostra essa grade), da hospedagem das imagens (aura-landing#17) e da versão de 13/10 em produção.** O botão leva à landing, mas o texto promete o módulo.

---

## PT

**Assunto (aprovado pelo Rafael em 15/10):** O GTO no flop, turn e river, ao lado do field

Este é o assunto de envio e o `<title>` do HTML. Alternativa **não usada** (descartada na aprovação): "Modo GTO no ar".

**Preheader:** Incluso no plano Individual, por tempo limitado. O GTO no flop, turn e river, ao lado do field.

**Corpo (texto)**

Modo GTO no ar
O GTO e o field na mesma tela.

Agora no flop, turn e river, inclusive as aberturas do agressor no turn e no river (second barrel, delayed c-bet e third barrel): o número GTO e a faixa GTO ao lado da frequência do field. Escolha o spot, clique em Apply e veja os dois juntos. A faixa de status do app guia cada clique até ter GTO.

Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO. É um spot, não a média do field. Confira no seu board.

No pré-flop, o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

Botão: Conhecer o Modo GTO
Sob o botão: O Modo GTO está incluso no plano Individual (R$ 150/mês) por tempo limitado. A conta grátis inclui uma amostra do GTO. Poker é jogo de habilidade e estudo. 18+.

---

## EN

**Subject (approved by Rafael on 15/10):** GTO on the flop, turn and river, next to the field

This is the sending subject and the HTML `<title>`. **Unused** alternative (dropped at approval): "GTO Mode is live".

**Preheader:** Included in the Individual plan, for a limited time. GTO on the flop, turn and river, next to the field.

**Body (text)**

GTO Mode is live
GTO and the field on the same screen.

Now on the flop, turn and river, including the aggressor's openings on the turn and river (second barrel, delayed c-bet and third barrel): the GTO number and the GTO range next to the field frequency. Pick the spot, hit Apply and see both together. The app's status bar guides you, click by click, until GTO is there.

Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8%. This is one spot, not the field average. Check it on your board.

Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

Button: See GTO Mode
Under the button: GTO Mode is included in the Individual plan (US$ 29/month) for a limited time. The free account includes a sample of GTO. Poker is a game of skill and study. 18+.

---

## Nota técnica

- **Imagem (versão de 15/10):** `email/modo-gto-pt.png` e `email/modo-gto-en.png` (1200 px, geradas pela build) agora levam um **mockup de produto**: a janela do app com a grade 13×13 do Field vs GTO (neutra de idioma) e um cartão com as barras field × GTO do c-bet de 33% renderizadas pela build, com formato por idioma: PT 46,0% × 38,8%, EN 46.0% × 38.8%, faixa 37,1–40,4% (as mesmas do exemplo (a); o texto do e-mail continua citando só 46,0% × 38,8%). Substitui a captura recortada do card (EN) e as duas barras soltas (PT). A janela é composta com a captura real da grade e o cartão renderizado. **A grade é uma captura real do app** (front main `204cc8f`, API local do P-53 com pin `20261010` e conta paga de teste, 15/10); o cartão do c-bet de 33% é renderizado pela build, com "%" na faixa. Rótulo dentro da imagem: "Field vs GTO · SB open (RFI) · 50bb+". Imagem de 530 px de largura no corpo. **Alt text:** PT "Janela do app com a grade de mãos do Field vs GTO no pré-flop (SB, RFI, 50bb+) e, sobreposto, o cartão do exemplo do e-mail: fold contra c-bet, field 46,0%, GTO 38,8%, faixa GTO 37,1–40,4%." / EN "App window with the Field vs GTO hand grid on the preflop (SB, RFI, 50bb+) and, overlaid, the card for the email's example: fold against a c-bet, field 46.0%, GTO 38.8%, GTO range 37.1–40.4%." **Limitação aceita:** no celular a grade e a legenda do cartão ficam pequenas; o texto do e-mail repete os números. O texto do e-mail não cita os números do Field vs GTO (nem o AA nem as marcas); sem selo de versão, e-mail ou nick. Os números do exemplo foram confirmados em produção em 14/10, e o teste logado do Rafael os confere antes do envio. **Hospedar em `https://www.aurapoker.com/email/` antes do envio (aura-landing#17).**
- **Logo:** `https://www.aura.poker/email/aura-logo.png` (já hospedado).
- **Link do CTA (botão para a landing, nunca o app/login; `www.aurapoker.com` com www):**
  - PT: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=pt
  - EN: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=en
  - Só o logo continua hospedado em `https://www.aura.poker/email/`; não é link de destino.
- **Descadastro:** placeholder `{{{RESEND_UNSUBSCRIBE_URL}}}` no rodapé, substituído pelo Resend no envio.
- **Layout:** 600px, tabelas, estilos inline, preheader oculto, botão âmbar `#D4A418`, linha de canais (Discord, WhatsApp, YouTube) e 18+ no rodapé, igual ao e-mail do Field Trends.
- **Botão:** "Conhecer o Modo GTO" / "See GTO Mode", por instrução da HUB; não usar "Acesse grátis", porque a conta grátis inclui só uma amostra do GTO.
- **Frase sob o botão (decisão do Rafael via HUB, 13/10: "fazendo parte do plano de 29 por tempo limitado"; 15/10: a inclusão do GTO no Individual é a temporária):** PT "O Modo GTO está incluso no plano Individual (R$ 150/mês) por tempo limitado. A conta grátis inclui uma amostra do GTO." / EN "GTO Mode is included in the Individual plan (US$ 29/month) for a limited time. The free account includes a sample of GTO." R$ 150 e US$ 29 são o preço do Individual; o temporário é a inclusão do GTO. Valor conferido pela HUB em `aura-landing` `src/content/pricing.ts` e `aura-novofront` `billingPlans.ts` (US$ 29/mês no checkout em EN, R$ 150/mês no checkout em PT). Moeda nunca trocada: PT só "R$ 150/mês", EN só "US$ 29/month". Sem data de fim, sem "últimas horas" nem "só hoje", sem preço travado, sem promessa de que quem assina agora mantém o GTO, sem preço futuro nem plano GTO à parte. **Pendências: o Rafael confere no Stripe que o checkout cobra 29 / 150 hoje; GATE B1 (data interna a honrar e reconciliação da landing publicada, em `copy.md` Pendência 8); GATE A2 (o teste logado do Rafael confere a amostra do GTO na conta Grátis, um spot do flop com a reação ao c-bet, e que o resto fica trancado; sem isso, a frase sai); depende também do P-61 no ar. Não enviar antes.**
- **Fora do e-mail:** plano Modo GTO à parte, plano Top, desconto semestral/anual e qualquer promoção.
- **Reply-to:** o e-mail não pede resposta; o remetente segue o padrão anterior (`manager@aurapoker.com` como reply-to). Confirmar antes do envio.
- **Não enviado.** Envio e lista são do Rafael.
