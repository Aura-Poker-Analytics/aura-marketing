# E-mail: lançamento do Modo GTO ("GTO em todas as ações")

Status: rascunho com marcadores pendentes; não publicado. Não enviado, e nada foi criado no Resend. Versão de 13/10/2026.
Números: de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10), exemplo (a): field folda 46,0%, GTO folda 38,8% (faixa 37,1–40,4%). Um exemplo só (CO × BB) e uma comparação só (field contra GTO). A HUB deve reconfirmar esses valores no snapshot de produção de 13/10. Sem número de escala, sem pré-flop concreto, sem contagem de mãos.
Marcadores a tirar antes de enviar: `[[CONFIRMAR-COBERTURA]]` (cobertura "em todas as ações do pós-flop", pendente da HUB) e `[[CONFIRMAR-PREFLOP]]` (pré-flop, confirmar se mudou). Nunca enviar com marcador.
HTML: `email-pt.html` e `email-en.html` são da versão de 08/10 e **precisam ser atualizados por outro agente** conforme este arquivo (ver "Para quem atualiza o HTML"). Este arquivo não mexe no HTML nem nas imagens.
**Só enviar depois do teste logado do Rafael, do P-61 no ar (Modo GTO aberto ao Individual), da versão "GTO em todas as ações" em produção e da confirmação dos marcadores.** O botão leva à landing, mas o texto promete o módulo.

---

## PT

**Assunto (2 opções)**
1. Novo na Aura: Modo GTO
2. [[CONFIRMAR-COBERTURA]] O GTO em todas as ações do pós-flop, ao lado do field

**Recomendado: a 1.** Anuncia o módulo pelo nome e não depende da confirmação da cobertura. Se a HUB confirmar a cobertura, a 2 é a mais forte: abre pela novidade da versão.

**Preheader:** [[CONFIRMAR-COBERTURA]] O GTO em todas as ações do pós-flop, ao lado do field. Escolha o spot, clique em Apply e compare.

**Corpo (texto)**

Novo na Aura: Modo GTO
O GTO e o field na mesma tela.

[[CONFIRMAR-COBERTURA]] Agora em todas as ações do pós-flop, inclusive as aberturas do agressor: cada uma com o número GTO e a faixa GTO ao lado da frequência do field. Escolha o spot, clique em Apply e veja os dois juntos. A cada clique, o app mostra o que falta para ver o GTO.

Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO. É um spot, não a média do field. Confira no seu board.

[[CONFIRMAR-PREFLOP]] No pré-flop, o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

Botão: Conhecer o Modo GTO
Sob o botão: O Modo GTO está incluído no plano Individual por tempo limitado. A conta grátis segue com o field e a comparação com o MDF. Poker é jogo de habilidade e estudo. 18+.

---

## EN

**Subject (2 options)**
1. New on Aura: GTO Mode
2. [[CONFIRMAR-COBERTURA]] GTO in every postflop action, next to the field

**Recommended: 1.** It announces the module by name and does not depend on the coverage confirmation. If the HUB confirms the coverage, option 2 is the stronger one: it opens with what is new in this version.

**Preheader:** [[CONFIRMAR-COBERTURA]] GTO in every postflop action, next to the field. Pick the spot, hit Apply and compare.

**Body (text)**

New on Aura: GTO Mode
GTO and the field on the same screen.

[[CONFIRMAR-COBERTURA]] Now in every postflop action, including the aggressor's openings: each one with the GTO number and the GTO range next to the field frequency. Pick the spot, hit Apply and see both together. At every click, the app shows what is missing to see GTO.

Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8%. This is one spot, not the field average. Check it on your board.

[[CONFIRMAR-PREFLOP]] Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

Button: See GTO Mode
Under the button: GTO Mode is included in the Individual plan for a limited time. The free account keeps the field and the MDF comparison. Poker is a game of skill and study. 18+.

---

## Para quem atualiza o HTML (outro agente)

- Trocar o parágrafo de cobertura, o bloco do exemplo e o assunto/preheader pelo texto acima, **sem os marcadores `[[...]]`** (só depois da confirmação da HUB).
- O exemplo do corpo agora cita só "46,0% contra 38,8%" (sem a faixa e sem o "5,6 pp" no texto). A imagem do e-mail (`email/modo-gto-pt.png` e `-en.png`) segue com os números de 08/10 (46,0%, 38,8%, faixa 37,1–40,4%, +5,6 pp); não contradiz o texto. Refazer a imagem só se a reconfirmação trocar algum número.
- Mantém: botão âmbar, frase do plano sob o botão, rodapé com descadastro e 18+.

## Nota técnica

- **Imagem:** `email/modo-gto-pt.png` e `email/modo-gto-en.png` (1200 px, geradas pela build). EN: captura recortada do card de 33% do app (`_ops/golive-gto-2026-10-04/prints/prod/postflop-en.png`: 46.0%, GTO 38.8% (37.1–40.4), Overfold +5.6 pp). PT: as duas barras renderizadas pela build (46,0% / 38,8% / faixa 37,1–40,4), porque o app em PT mistura 46.0% e 38,8% (bug do front). A captura vem do front no SHA de produção de 08/10 (aura-novofront 429c093) lendo a API local com os snapshots do go-live, não da conta de produção; o teste logado do Rafael confere os mesmos valores antes do envio. Sem selo de versão, e-mail ou nick. Hospedar em `https://www.aurapoker.com/email/` antes do envio (HUB/Rafael).
- **Logo:** `https://www.aura.poker/email/aura-logo.png` (já hospedado).
- **Link do CTA (sempre a landing, nunca o app/login; `www.aurapoker.com` com www):**
  - PT: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=pt
  - EN: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=en
  - Só o logo continua hospedado em `https://www.aura.poker/email/`; não é link de destino.
- **Descadastro:** placeholder `{{{RESEND_UNSUBSCRIBE_URL}}}` no rodapé, substituído pelo Resend no envio.
- **Layout:** 600px, tabelas, estilos inline, preheader oculto, botão âmbar `#D4A418`, linha de canais (Discord, WhatsApp, YouTube) e 18+ no rodapé, igual ao e-mail do Field Trends.
- **Botão:** "Conhecer o Modo GTO" / "See GTO Mode", por instrução da HUB; não usar "Acesse grátis", porque a conta grátis não vê o número GTO.
- **Frase sob o botão (HUB, 08/10, P-61):** "O Modo GTO está incluído no plano Individual por tempo limitado. A conta grátis segue com o field e a comparação com o MDF." / "GTO Mode is included in the Individual plan for a limited time. The free account keeps the field and the MDF comparison." Depende da publicação do P-61. Sem preço, sem plano Modo GTO à venda, sem plano Top. **Pendência: a HUB confirma depois o que entra sobre planos nesta versão.**
- **Promoção (não citar ainda):** o plano Modo GTO pelo preço do Individual, por tempo limitado, só entra quando a HUB confirmar que o checkout cobra o promocional. Até lá, nenhuma peça cita preço do GTO nem o plano Modo GTO como produto à venda.
- **Reply-to:** o e-mail não pede resposta; o remetente segue o padrão anterior (`manager@aurapoker.com` como reply-to). Confirmar antes do envio.
- **Não enviado.** Envio e lista são do Rafael.
