# E-mail: lançamento do Modo GTO

Status: rascunho com números fechados; não publicado. Não enviado, e nada foi criado no Resend.
Números: todos de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10), exemplo (a). O único número verificado do e-mail é o do exemplo (um spot): field folda 46,0%, GTO folda 38,8% (faixa 37,1–40,4%), 5,6 pp acima do topo da faixa. Sem número de escala, sem pré-flop concreto, sem contagem de mãos.
HTML: existe (`email-pt.html` e `email-en.html`; para abrir do disco, `email-pt.preview.html` e `email-en.preview.html`). A imagem do e-mail EN é a captura recortada do card de 33% do app; a PT são as duas barras renderizadas pela build (o app em PT mistura formatos decimais).
**Só enviar depois do passo 6 do roteiro de go-live.** O botão leva à landing, mas o texto promete o módulo.

---

## PT

**Assunto (2 opções)**
1. Novo na Aura: Modo GTO
2. O GTO e o field, lado a lado, no mesmo spot

**Recomendado: a 1.** O assunto anuncia o módulo pelo nome; a ideia do lado a lado abre o corpo logo depois. A 2 fica como alternativa se o Rafael preferir abrir pela ideia.

**Preheader:** Novo na Aura: Modo GTO. O número GTO e a faixa GTO ao lado do número do field, onde há referência.

**Corpo (texto)**

Novo na Aura: Modo GTO
O GTO e o field na mesma tela.

Ao lado do número do field, agora o número GTO e a faixa GTO, onde há referência. No pós-flop: SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP. No pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

Botão: Conhecer o Modo GTO
Sob o botão: O Modo GTO está incluído no plano Individual por tempo limitado. A conta grátis segue com o field e a comparação com o MDF. Poker é jogo de habilidade e estudo. 18+.

---

## EN

**Subject (2 options)**
1. New on Aura: GTO Mode
2. GTO and the field, side by side, in the same spot

**Recommended: 1.** The subject announces the module by name; the side-by-side idea opens the body right after. Option 2 stays as the alternative if Rafael prefers to open with the idea.

**Preheader:** New on Aura: GTO Mode. The GTO number and the GTO range next to the field number, where a reference exists.

**Body (text)**

New on Aura: GTO Mode
GTO and the field on the same screen.

Next to the field number, now the GTO number and the GTO range, where a reference exists. Postflop: SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop. Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Button: See GTO Mode
Under the button: GTO Mode is included in the Individual plan for a limited time. The free account keeps the field and the MDF comparison. Poker is a game of skill and study. 18+.

---

## Nota técnica

- **Imagem:** `email/modo-gto-pt.png` e `email/modo-gto-en.png` (1200 px, geradas pela build). EN: captura recortada do card de 33% do app (`_ops/golive-gto-2026-10-04/prints/prod/postflop-en.png`: 46.0%, GTO 38.8% (37.1–40.4), Overfold +5.6 pp). PT: as duas barras renderizadas pela build (46,0% / 38,8% / faixa 37,1–40,4), porque o app em PT mistura 46.0% e 38,8% (bug do front). A captura vem do front no SHA de produção (aura-novofront 429c093) lendo a API local com os snapshots do go-live, não da conta de produção; o teste logado do Rafael confere os mesmos valores antes do envio. Sem selo Beta, e-mail ou nick. Hospedar em `https://www.aurapoker.com/email/` antes do envio (HUB/Rafael).
- **Logo:** `https://www.aura.poker/email/aura-logo.png` (já hospedado).
- **Link do CTA (sempre a landing, nunca o app/login; `www.aurapoker.com` com www):**
  - PT: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=pt
  - EN: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=en
  - Só o logo continua hospedado em `https://www.aura.poker/email/`; não é link de destino.
- **Descadastro:** placeholder `{{{RESEND_UNSUBSCRIBE_URL}}}` no rodapé, substituído pelo Resend no envio.
- **Layout:** 600px, tabelas, estilos inline, preheader oculto, botão âmbar `#D4A418`, linha de canais (Discord, WhatsApp, YouTube) e 18+ no rodapé, igual ao e-mail do Field Trends.
- **Botão:** "Conhecer o Modo GTO" / "See GTO Mode", por instrução da HUB; não usar "Acesse grátis", porque a conta grátis não vê o número GTO.
- **Frase sob o botão (decisão da HUB, 08/10):** "O Modo GTO está incluído no plano Individual por tempo limitado. A conta grátis segue com o field e a comparação com o MDF." / "GTO Mode is included in the Individual plan for a limited time. The free account keeps the field and the MDF comparison." Ela depende da publicação do P-61 (abertura do Modo GTO ao plano Individual). Sem preço, sem o plano Modo GTO como produto à venda, sem "plano Top", sem "prévia" nem "borrado".
- **Promoção (não citar ainda):** o plano Modo GTO pelo preço do Individual, por tempo limitado, só entra quando a HUB confirmar que o checkout cobra o promocional. Até lá, nenhuma peça cita preço do GTO nem o plano Modo GTO como produto à venda.
- **Reply-to:** o e-mail não pede resposta; o remetente segue o padrão anterior (`manager@aurapoker.com` como reply-to). Confirmar antes do envio.
- **Não enviado.** Envio e lista são do Rafael.
