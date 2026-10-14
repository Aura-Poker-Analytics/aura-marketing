# E-mail: lançamento do Modo GTO (GTO no flop, turn e river, com as aberturas do agressor)

Status: rascunho sem marcadores abertos; não publicado. Não enviado, e nada foi criado no Resend. Versão de 13/10/2026, números fechados em 14/10.
Números: exemplo (a) de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10): field folda 46,0%, GTO folda 38,8%. A cobertura segue `aura-main/_ops/golive-gto-2026-10-14/numeros-verificados-lancamento.md` (14/10). Um exemplo só (CO × BB) e uma comparação só (field contra GTO). Sem número de escala, sem pré-flop concreto, sem contagem de mãos, sem o exemplo de abertura.
**Só enviar depois do teste logado do Rafael, do P-61 no ar (Modo GTO aberto ao Individual), da conferência do preço (29 / 150) no Stripe pelo Rafael, da hospedagem das imagens (aura-landing#17) e da versão de 13/10 em produção.** O botão leva à landing, mas o texto promete o módulo.

---

## PT

**Assunto (2 opções)**
1. Novo na Aura: Modo GTO
2. O GTO no flop, turn e river, ao lado do field

**Recomendado: a 1.** Anuncia o módulo pelo nome. A 2 fica como alternativa se o Rafael preferir abrir pela novidade da versão.

**Preheader:** O GTO no flop, turn e river, ao lado do field. Escolha o spot, clique em Apply e compare.

**Corpo (texto)**

Novo na Aura: Modo GTO
O GTO e o field na mesma tela.

Agora no flop, turn e river, inclusive as aberturas do agressor no turn e no river (second barrel, delayed c-bet e third barrel): o número GTO e a faixa GTO ao lado da frequência do field. Escolha o spot, clique em Apply e veja os dois juntos. A faixa de status do app guia cada clique até ter GTO.

Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO. É um spot, não a média do field. Confira no seu board.

No pré-flop, o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

Botão: Conhecer o Modo GTO
Sob o botão: O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF. Poker é jogo de habilidade e estudo. 18+.

---

## EN

**Subject (2 options)**
1. New on Aura: GTO Mode
2. GTO on the flop, turn and river, next to the field

**Recommended: 1.** It announces the module by name. Option 2 stays as the alternative if Rafael prefers to open with what is new in this version.

**Preheader:** GTO on the flop, turn and river, next to the field. Pick the spot, hit Apply and compare.

**Body (text)**

New on Aura: GTO Mode
GTO and the field on the same screen.

Now on the flop, turn and river, including the aggressor's openings on the turn and river (second barrel, delayed c-bet and third barrel): the GTO number and the GTO range next to the field frequency. Pick the spot, hit Apply and see both together. The app's status bar guides you, click by click, until GTO is there.

Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8%. This is one spot, not the field average. Check it on your board.

Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

Button: See GTO Mode
Under the button: GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison. Poker is a game of skill and study. 18+.

---

## Nota técnica

- **Imagem:** `email/modo-gto-pt.png` e `email/modo-gto-en.png` (1200 px, geradas pela build). EN: captura recortada do card de 33% do app (`_ops/golive-gto-2026-10-04/prints/prod/postflop-en.png`: 46.0%, GTO 38.8% (37.1–40.4), Overfold +5.6 pp). PT: as duas barras renderizadas pela build (46,0% / 38,8% / faixa 37,1–40,4), porque o app em PT mistura 46.0% e 38,8% (bug do front). A captura vem do front no SHA de produção de 08/10 (aura-novofront 429c093) lendo a API local com os snapshots do go-live, não da conta de produção; os mesmos números foram confirmados em produção em 14/10, e o teste logado do Rafael os confere antes do envio. Sem selo de versão, e-mail ou nick. **Hospedar em `https://www.aurapoker.com/email/` antes do envio (aura-landing#17).**
- **Logo:** `https://www.aura.poker/email/aura-logo.png` (já hospedado).
- **Link do CTA (sempre a landing, nunca o app/login; `www.aurapoker.com` com www):**
  - PT: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=pt
  - EN: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=en
  - Só o logo continua hospedado em `https://www.aura.poker/email/`; não é link de destino.
- **Descadastro:** placeholder `{{{RESEND_UNSUBSCRIBE_URL}}}` no rodapé, substituído pelo Resend no envio.
- **Layout:** 600px, tabelas, estilos inline, preheader oculto, botão âmbar `#D4A418`, linha de canais (Discord, WhatsApp, YouTube) e 18+ no rodapé, igual ao e-mail do Field Trends.
- **Botão:** "Conhecer o Modo GTO" / "See GTO Mode", por instrução da HUB; não usar "Acesse grátis", porque a conta grátis não vê o número GTO.
- **Frase sob o botão (decisão do Rafael via HUB, 13/10: "fazendo parte do plano de 29 por tempo limitado"):** PT "O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF." / EN "GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison." Valor conferido pela HUB em `aura-landing` `src/content/pricing.ts` e `aura-novofront` `billingPlans.ts` (US$ 29/mês no checkout em EN, R$ 150/mês no checkout em PT). Moeda nunca trocada: PT só "R$ 150/mês", EN só "US$ 29/month". Sem data de fim, sem "últimas horas" nem "só hoje". **Pendência: o Rafael confere no Stripe que o checkout cobra 29 / 150 hoje; depende também do P-61 no ar. Não enviar antes.** (HTML: atualizar a frase sob o botão nos dois idiomas.)
- **Fora do e-mail:** plano Modo GTO à parte, plano Top, desconto semestral/anual e qualquer promoção.
- **Reply-to:** o e-mail não pede resposta; o remetente segue o padrão anterior (`manager@aurapoker.com` como reply-to). Confirmar antes do envio.
- **Não enviado.** Envio e lista são do Rafael.
