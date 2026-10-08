# Modo GTO: copy de lançamento

Status: rascunho com marcadores; não publicado. Sem commit. Entra no ar em 08/10/2026.
@aurapokeranalytics: a confirmar pelo Rafael. URLs com UTM prontas na tabela abaixo.
Fonte única dos números: `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md`, que **ainda não existe**. Nenhum número foi inventado: todo valor é um marcador `[[N1..N6]]` e está mapeado no bloco "Números usados" no fim.
Peças deste pacote: Discord (também em `discord.md`), Instagram (feed, story, carrossel), landing e e-mail (em `email.md`).

> **Candidato para a HUB confirmar (não usado no texto).** O roteiro de go-live (`03-roteiro-go-live.md`, passo 6) traz um spot que serve ao eixo "field folda acima da faixa GTO": SB×BB 3-bet, 30.1–60bb, Unpaired Rainbow Disconnected A, Fold vs Flop CBet, GTO 25,2% (19,2–31,2), com field ≈ 34% e Overfold. O "≈ 34%" é aproximado; o arquivo de números precisa trazer o valor exato do dia, medido na Azure. O mesmo spot tem turn (Fold vs Second Barrel, GTO 28,8%, 21,8–35,8) se a HUB quiser um segundo exemplo. Nada disso entrou no texto; os marcadores seguem abertos.

## Pendências de produto (conferir antes de aprovar)
1. **Só publicar depois do passo 6 do roteiro (teste logado do Rafael).** O link leva ao app e o texto promete o módulo; nada sai antes de o Modo GTO estar ligado (passos 4 e 5) e conferido.
2. **Pré-flop 20261007 (atualização da HUB).** O RFI de CO e BTN a 40bb entra no lançamento (pré-flop `20261007`, aprovado e mesclado) e as peças o dizem como fato. O cabeçalho do `03-roteiro-go-live.md` ainda fala em `20261005` e diz que o `20261007` vem depois. Seguimos a HUB; vale o roteiro ser corrigido para as peças e o produto dizerem a mesma coisa.
3. **Reação a raise: só o que existe.** As peças dizem "inclusive a reação a raise no flop do SRP, nas linhas de raise do tamanho do bet". Apertei o "no SRP" do briefing para "no flop do SRP" porque a tabela de reação a raise (`tbl_gto_flop_node`) é do flop; se existir reação a raise no turn, trocar. Num 3-bet CO×BB a 40bb a reação a raise não tem GTO (exclusão até regerar, 6 células de 3-bet re-resolvidas a 40/60bb), então nenhuma peça diz "toda reação a raise em todo spot". Nenhum exemplo do pacote pode ser reação a raise em 3-bet.
4. **Pré-flop "em cada célula".** O briefing diz que cada célula da grade traz GTO e desvio; o roteiro mede isso a 20–30bb e a cobertura varia por spot e stack. As peças dizem "a grade traz o GTO e o desvio em cada célula" sem listar spots. Se houver célula sem GTO na tela, trocar por "nas células da grade".
5. **O que o Grátis vê (resolvido pela HUB, lido do código).** Conta Grátis (e Individual) não vê número GTO nem faixa; segue com o field e a comparação com o MDF, e o GTO aparece como cadeado "Disponível no Modo GTO", que abre o upgrade "Desbloqueie o Modo GTO". Frase única usada em todas as peças, PT: "O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO." EN: "GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan." Os CTAs são "Conhecer o Modo GTO" / "See GTO Mode"; nenhum CTA diz "grátis". Nenhuma peça fala em "prévia" nem "borrado": o que o Grátis vê é um cadeado. Individual é plano pago e também não vê GTO; por isso as peças dizem "plano Modo GTO" e não "planos pagos".
6. **O exemplo é um spot, não a média do field.** Toda peça diz "é um spot, não a média do field". O "como explorar" do texto (field folda acima da faixa GTO, então o c-bet de bluff tem mais fold equity do que o GTO) **só vale se o spot escolhido tiver o field acima do topo da faixa GTO no fold contra o c-bet**. Se a HUB escolher outro spot, ajustar. Se o field ficar abaixo da faixa, trocar a leitura para: "O field folda abaixo da faixa GTO, então aqui o c-bet de bluff tem menos fold equity do que o GTO; estude o c-bet por valor." / EN: "The field folds below the GTO range, so here the bluff c-bet has less fold equity than GTO; study value c-bets."
7. **Gancho e título de arte usam só o % central do N3.** O N3 traz o % GTO e a faixa (de–a). No gancho (legenda, slide 1, título da arte) usar só o % central; a faixa vai no corpo.
8. **Nome em inglês.** Usei "GTO Mode" (é o rótulo do toggle e das FAQs do aura-landing). Confirmar.
9. **Torneios vanilla.** O produto mostra a ressalva de metodologia (GTO se refere a torneios Vanilla) só dentro do ⓘ e da página de Metodologia, por decisão do Rafael. Nenhuma peça a repete; o spot do exemplo e a célula de pré-flop (N5) devem ser de torneio Regular, para não contradizer a ressalva.
10. **Sem "Beta" e sem preço.** O Modo GTO não aparece como Beta e nenhuma peça cita preço. Se o Rafael quiser o convite a feedback, entra como frase extra no Discord.
11. **`product-truth-aura.md`** não existe neste worktree. Li `AGENTS.md`, `brand/brand-kit.md`, o plano de marketing, o roteiro de go-live e os modelos do Field Trends e do PR 1. Se o arquivo existir em outro lugar, vale uma conferência das frases de produto.
12. **Landing.** O texto da landing é o do modo de lançamento do `aura-landing` (flag `VITE_LAUNCH_MODO_GTO`); a lista de cobertura por posição segue fora do texto, porque não está fechada.

## Regra de leitura do exemplo
O exemplo é um spot (N1), com o field (N2) e o GTO com a faixa (N3) lado a lado, e a diferença (N4). Frase padrão, PT: "O field folda acima da faixa GTO, então aqui o c-bet de bluff tem mais fold equity do que o GTO. É um spot, não a média do field. Confira no seu board." EN: "The field folds above the GTO range, so here the bluff c-bet has more fold equity than GTO. This is one spot, not the field average. Check it on your board."
Frase de benefício (slide 5): acima da faixa, estudar ampliar o c-bet de bluff; abaixo, estudar o c-bet por valor. Sem promessa de resultado.

## URLs por peça
Regra: Discord leva ao app (`https://www.aura.poker/`); Instagram e e-mail levam à landing (`https://www.aurapoker.com/`). Parâmetros: `utm_source=<fonte>&utm_medium=<meio>&utm_campaign=modo-gto-launch&utm_content=<peça>`.

| Peça | Destino | utm_source | utm_content | URL |
|---|---|---|---|---|
| Discord PT | app | discord | discord-pt | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt |
| Discord EN | app | discord | discord-en | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en |
| Feed (link na bio) | landing | instagram | feed | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=feed |
| Story (sticker de link) | landing | instagram | story | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=story |
| Carrossel (link na bio) | landing | instagram | carrossel | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=carrossel |
| Landing (botão de CTA, para o cadastro no app) | app | landing | modo-gto (utm_medium=website) | https://www.aura.poker/Login?tab=signup&utm_source=landing&utm_medium=website&utm_campaign=modo-gto-launch&utm_content=modo-gto |
| E-mail PT | landing | email | pt | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=pt |
| E-mail EN | landing | email | en | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=en |

Observação: para o botão da landing mantive `utm_source=landing`, como no Field Trends. Ajustar se o Rafael preferir outro valor.

## Rodapé padrão (um só)
- PT: "Ferramenta de estudo · 18+" (com "Dados: Aura · [[N6]]" na frente, só se o N6 existir)
- EN: "Study tool · 18+" (with "Data: Aura · [[N6]]" in front, only if N6 exists)
Nas artes, o rodapé leva também @aurapokeranalytics e o selo 18+.

---

# (a) Instagram

## Legenda do feed (1080x1350)

Texto na arte (PT):
- Selo (pílula âmbar) + kicker: NOVO · MODO GTO
- Título: O GTO FOLDA [[N3: % GTO do mesmo spot e a faixa (de–a)]]. O FIELD FOLDA [[N2: % de fold do field no exemplo]].
- Spot, uma vez só: [[N1: spot do exemplo — posições, stack, board/textura]]
- Diagrama lado a lado: barra do field e barra do GTO com a faixa; rótulo da diferença: [[N4: diferença field − GTO em pp]] pp
- CTA (âmbar): Conhecer o Modo GTO · link na bio
- Rodapé: @aurapokeranalytics · Ferramenta de estudo · 18+

Texto na arte (EN):
- Seal (amber pill) + kicker: NEW · GTO MODE
- Title: GTO FOLDS [[N3]]. THE FIELD FOLDS [[N2]].
- Spot, once: [[N1]]
- Side-by-side diagram: field bar and GTO bar with the range; difference label: [[N4]] pp
- CTA (amber): See GTO Mode · link in bio
- Footer: @aurapokeranalytics · Study tool · 18+

Nota de arte: título com só o % central do N3; a faixa (de–a) aparece no diagrama. Cores semânticas: fold teal `#015A6B`; a barra de diferença em âmbar (o gap). Nenhum número fora dos marcadores.

Legenda PT:
```
O GTO folda [[N3: % GTO do mesmo spot e a faixa (de–a)]]. O field folda [[N2: % de fold do field no exemplo]]. Mesmo spot.

Novo na Aura: Modo GTO. Ao lado de cada número do field, o número GTO e a faixa GTO.

Exemplo: [[N1: spot do exemplo — posições, stack, board/textura]]. Fold contra o c-bet: field [[N2]], GTO [[N3]]. Diferença de [[N4: diferença field − GTO em pp]] pp.

O field folda acima da faixa GTO, então aqui o c-bet de bluff tem mais fold equity do que o GTO. É um spot, não a média do field. Confira no seu board.

No pós-flop: SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP. No pré-flop: o GTO e o desvio em cada célula da grade, inclusive o RFI de CO e BTN a 40bb.

O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO.

Conhecer o Modo GTO, link na bio. Salve para estudar.

Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

Legenda EN:
```
GTO folds [[N3: GTO % of the same spot and the range (from–to)]]. The field folds [[N2: field fold % in the example]]. Same spot.

New on Aura: GTO Mode. Next to every field number, the GTO number and the GTO range.

Example: [[N1: example spot — positions, stack, board/texture]]. Fold to the c-bet: field [[N2]], GTO [[N3]]. A gap of [[N4: field − GTO difference in pp]] pp.

The field folds above the GTO range, so here the bluff c-bet has more fold equity than GTO. This is one spot, not the field average. Check it on your board.

Postflop: SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop. Preflop: the GTO and the deviation in every grid cell, including the CO and BTN RFI at 40bb.

GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan.

See GTO Mode, link in bio. Save it for study.

Study tool. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

## Story (1080x1920)

Texto na arte (PT):
- Topo: logo; pílula NOVO + MODO GTO
- Centro: "Mesmo spot, dois números." / "Field: [[N2]]  ·  GTO: [[N3]]" / "O field folda acima da faixa GTO?" / spot em letra pequena: [[N1]]
- Diagrama lado a lado, só com rótulos: Field, GTO e [[N4]] pp
- Base: "Veja o gap no seu spot." / botão "Conhecer o Modo GTO" / rodapé "Ferramenta de estudo · 18+" / selo 18+

Texto na arte (EN):
- Top: logo; NEW + GTO MODE pill
- Center: "Same spot, two numbers." / "Field: [[N2]]  ·  GTO: [[N3]]" / "Does the field fold above the GTO range?" / small spot line: [[N1]]
- Side-by-side diagram, labels only: Field, GTO and [[N4]] pp
- Bottom: "See the gap in your spot." / button "See GTO Mode" / footer "Study tool · 18+" / 18+ badge

Nota de arte: a arte traz a pergunta, não o veredito. O botão é o sticker de link do Instagram. Sticker de enquete opcional (fora da arte): "Qual spot você quer ver com o GTO ao lado?" com as opções "SRP" e "3-bet" / "Which spot do you want to see with GTO next to it?" with "SRP" and "3-bet".

## Carrossel (7 slides, 1080x1350)

Títulos em caixa alta, corpo em sentence case. Rodapé padrão em todos os slides (@aurapokeranalytics, "Ferramenta de estudo · 18+" / "Study tool · 18+", selo 18+) e indicador "n / 7" no topo. Os slides 2 a 4 usam capturas do app (imagem), não texto de arte.

### Slide 1: gancho
- PT: pílula NOVO + MODO GTO / título "ONDE O FIELD SAI DO GTO?" / sub "Modo GTO: o número GTO e a faixa GTO ao lado de cada número do field."
- EN: NEW + GTO MODE pill / title "WHERE DOES THE FIELD LEAVE GTO?" / sub "GTO Mode: the GTO number and the GTO range next to every field number."
- Número: nenhum.

### Slide 2: o exemplo, lado a lado
- PT: título "MESMO SPOT, DOIS NÚMEROS" / spot "[[N1: spot do exemplo — posições, stack, board/textura]]" / cards "Field folda [[N2: % de fold do field no exemplo]]" e "GTO folda [[N3: % GTO do mesmo spot e a faixa (de–a)]]" / destaque "Diferença: [[N4: diferença field − GTO em pp]] pp" / microtexto "Um spot, não a média do field."
- EN: title "SAME SPOT, TWO NUMBERS" / spot "[[N1]]" / cards "Field folds [[N2]]" and "GTO folds [[N3]]" / highlight "Gap: [[N4]] pp" / microcopy "One spot, not the field average."
- Arte: duas barras fold lado a lado (teal `#015A6B`), a faixa GTO sombreada em volta da barra do GTO e a distância em âmbar entre as duas.

### Slide 3: pós-flop com a faixa e a reação a raise
- PT: título "PÓS-FLOP: GTO E FAIXA EM CADA NÚMERO" / corpo "SRP e 3-bet, flop e turn. Ao lado do número do field, o número GTO e a faixa GTO. Inclusive a reação a raise no flop do SRP, nas linhas de raise do tamanho do bet." / destaque "Field fora da faixa GTO: é aí que você olha primeiro."
- EN: title "POSTFLOP: GTO AND RANGE ON EVERY NUMBER" / body "SRP and 3-bet, flop and turn. Next to the field number, the GTO number and the GTO range. Including the response to a raise on the SRP flop, on the raise lines at the bet size." / highlight "Field outside the GTO range: that is where you look first."
- Arte: captura do Postflop com o Modo GTO ligado, mostrando uma linha de raise com o GTO. Não mostrar reação a raise de 3-bet CO×BB a 40bb (sem GTO).
- Números: nenhum no texto (a captura só mostra números do arquivo de números).

### Slide 4: pré-flop com a célula, o GTO e o desvio
- PT: título "PRÉ-FLOP: A CÉLULA COM O DESVIO" / corpo "Na grade do Preflop Analysis, cada célula traz o GTO e o desvio do field, inclusive o RFI de CO e BTN a 40bb." / destaque "[[N5: exemplo de pré-flop — célula, GTO e field, desvio]]"
- EN: title "PREFLOP: THE CELL WITH THE DEVIATION" / body "In the Preflop Analysis grid, every cell carries the GTO and the field deviation, including the CO and BTN RFI at 40bb." / highlight "[[N5]]"
- Arte: captura da grade com a célula do N5 destacada (desvio colorido).

### Slide 5: o que fazer com o gap
- PT: título "O QUE FAZER COM O GAP" / corpo "Field acima da faixa GTO no fold contra o c-bet: estude ampliar o c-bet de bluff. Abaixo da faixa: estude o c-bet por valor." / destaque "Confira no seu spot, não na média."
- EN: title "WHAT TO DO WITH THE GAP" / body "Field above the GTO range on the fold to the c-bet: study widening the bluff c-bet. Below the range: study the value c-bet." / highlight "Check your spot, not the average."
- Número: nenhum.

### Slide 6: é do plano Modo GTO (penúltimo)
- PT: título "É DO PLANO MODO GTO" / corpo "O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO."
- EN: title "IT IS ON THE GTO MODE PLAN" / body "GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan."
- Arte: o cadeado "Disponível no Modo GTO" do app. Sem "prévia", sem borrado, sem preço.

### Slide 7: CTA
- PT: pílula NOVO + MODO GTO / título "CONHEÇA O MODO GTO" / corpo "O GTO e o field no mesmo spot." / botão "Link na bio" / "18+"
- EN: NEW + GTO MODE pill / title "SEE GTO MODE" / body "GTO and the field in the same spot." / button "Link in bio" / "18+"

Nota de arte: pílula âmbar "NOVO" / "NEW" nos slides 1 e 7; kicker MODO GTO / GTO MODE nos demais.

### Legenda do carrossel
PT:
```
Onde o field sai do GTO?

Novo na Aura: Modo GTO. Ao lado de cada número do field, o número GTO e a faixa GTO, no pós-flop (SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP) e no pré-flop (o GTO e o desvio em cada célula da grade, inclusive o RFI de CO e BTN a 40bb).

Exemplo: [[N1: spot do exemplo — posições, stack, board/textura]]. O field folda [[N2: % de fold do field no exemplo]] contra o c-bet; o GTO folda [[N3: % GTO do mesmo spot e a faixa (de–a)]]. Diferença de [[N4: diferença field − GTO em pp]] pp. Acima da faixa GTO, o c-bet de bluff tem mais fold equity do que o GTO. É um spot, não a média do field. Confira no seu board.

O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO.

Conhecer o Modo GTO, link na bio. Salve para estudar.

Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
Where does the field leave GTO?

New on Aura: GTO Mode. Next to every field number, the GTO number and the GTO range, postflop (SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop) and preflop (the GTO and the deviation in every grid cell, including the CO and BTN RFI at 40bb).

Example: [[N1: example spot — positions, stack, board/texture]]. The field folds [[N2: field fold % in the example]] to the c-bet; GTO folds [[N3: GTO % of the same spot and the range (from–to)]]. A gap of [[N4: field − GTO difference in pp]] pp. Above the GTO range, the bluff c-bet has more fold equity than GTO. This is one spot, not the field average. Check it on your board.

GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan.

See GTO Mode, link in bio. Save it for study.

Study tool. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

---

# (b) Landing

@aurapokeranalytics: a confirmar pelo Rafael. URL do CTA: ver a linha "Landing" da tabela "URLs por peça".

## Kicker (acima do título, com a pílula de novo)
- PT: Novo na Aura · Modo GTO
- EN: New on Aura · GTO Mode

## Título
- PT: O GTO e o field na mesma tela.
- EN: GTO and the field on the same screen.

## Subtítulo
- PT: Modo GTO: o número GTO e a faixa GTO ao lado de cada número do field, no pós-flop e no pré-flop. Veja onde o field sai da faixa e estude esse spot.
- EN: GTO Mode: the GTO number and the GTO range next to every field number, postflop and preflop. See where the field leaves the range and study that spot.

## 3 bullets
PT:
- Pós-flop: SRP e 3-bet, flop e turn, com o número GTO e a faixa GTO ao lado do field, inclusive a reação a raise no flop do SRP, nas linhas de raise do tamanho do bet.
- Pré-flop: a grade traz o GTO e o desvio em cada célula, inclusive o RFI de CO e BTN a 40bb.
- Exemplo: [[N1: spot do exemplo — posições, stack, board/textura]]. O field folda [[N2: % de fold do field no exemplo]] contra o c-bet; o GTO folda [[N3: % GTO do mesmo spot e a faixa (de–a)]]. Diferença de [[N4: diferença field − GTO em pp]] pp. Acima da faixa GTO, o c-bet de bluff tem mais fold equity do que o GTO. É um spot, não a média do field. Confira no seu board.

EN:
- Postflop: SRP and 3-bet, flop and turn, with the GTO number and the GTO range next to the field, including the response to a raise on the SRP flop, on the raise lines at the bet size.
- Preflop: the grid carries the GTO and the deviation in every cell, including the CO and BTN RFI at 40bb.
- Example: [[N1]]. The field folds [[N2]] to the c-bet; GTO folds [[N3]]. A gap of [[N4]] pp. Above the GTO range, the bluff c-bet has more fold equity than GTO. This is one spot, not the field average. Check it on your board.

Nota de rodapé da seção (PT): "Um spot, não a média do field. Ferramenta de estudo · 18+. A Aura não é site de apostas e não oferece jogo." [Se o N6 existir: "Dados: Aura · [[N6: 1 número de escala/cobertura, SE o arquivo trouxer; senão omita a frase]]."]
Footnote (EN): "One spot, not the field average. Study tool · 18+. Aura is not a betting site and does not offer gambling." [If N6 exists: "Data: Aura · [[N6]]."]

CTA: PT "Conhecer o Modo GTO" / EN "See GTO Mode".
Frase sob o CTA, PT: "O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO." / EN: "GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan."

## Alt text das imagens (2)
### Imagem 1: o exemplo lado a lado
- PT: "Duas barras de fold no mesmo spot do pós-flop: a do field e a do GTO, com a faixa GTO em volta da barra do GTO e a diferença entre elas em destaque."
- EN: "Two fold bars for the same postflop spot: the field and the GTO, with the GTO range around the GTO bar and the gap between them highlighted."
### Imagem 2: a grade do pré-flop
- PT: "Grade de mãos do Preflop Analysis em que cada célula mostra o GTO e o desvio do field, com o desvio colorido."
- EN: "Preflop Analysis hand grid where each cell shows the GTO and the field deviation, with the deviation color-coded."

Nota para o designer: as imagens só mostram os números do arquivo de números verificados. Não atribuir a nenhuma imagem os números do texto. Não mostrar preço nem "prévia".

---

# (c) Discord

Texto completo, com URLs, em `discord.md` (mesma pasta). PT e EN, até cerca de 1.200 caracteres cada (cerca de 1.050 PT e 1.080 EN com valores típicos nos marcadores; recontar depois de preencher), 3 emojis funcionais (📊 título, 🔎 convite, 👉 CTA). **Só postar depois do passo 6 do roteiro.**

**PT**
```
📊 **Novo na Aura: Modo GTO**

Ao lado de cada número do field, o número GTO e a faixa GTO. Onde o field sai da faixa, está o spot para estudar.

**Exemplo de spot**
[[N1: spot do exemplo — posições, stack, board/textura]]
Fold contra o c-bet: field [[N2: % de fold do field no exemplo]], GTO [[N3: % GTO do mesmo spot e a faixa (de–a)]]. Diferença: [[N4: diferença field − GTO em pp]] pp.
O field folda acima da faixa GTO, então aqui o c-bet de bluff tem mais fold equity do que o GTO. É um spot, não a média do field. Confira no seu board.

**O que você vê**
- Pós-flop: SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP
- Pré-flop: o GTO e o desvio em cada célula da grade, inclusive o RFI de CO e BTN a 40bb

🔎 Abra um spot que você joga e olhe o gap.

O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO.
👉 Conhecer o Modo GTO: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt
```

**EN**
```
📊 **New on Aura: GTO Mode**

Next to every field number, the GTO number and the GTO range. Where the field leaves the range, that is the spot to study.

**Example spot**
[[N1: example spot — positions, stack, board/texture]]
Fold to the c-bet: field [[N2: field fold % in the example]], GTO [[N3: GTO % of the same spot and the range (from–to)]]. Gap: [[N4: field − GTO difference in pp]] pp.
The field folds above the GTO range, so here the bluff c-bet has more fold equity than GTO. This is one spot, not the field average. Check it on your board.

**What you see**
- Postflop: SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop
- Preflop: the GTO and the deviation in every grid cell, including the CO and BTN RFI at 40bb

🔎 Open a spot you play and look at the gap.

GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan.
👉 See GTO Mode: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en
```

---

# (d) E-mail

Texto, assuntos, preheader e notas técnicas em `email.md`. Assunto recomendado: a 1 ("Novo na Aura: Modo GTO" / "New on Aura: GTO Mode"). Botão "Conhecer o Modo GTO" / "See GTO Mode". HTML não produzido nesta rodada.

---

## Números usados (marcadores; fonte: `numeros-verificados.md`, ainda inexistente)

| Marcador | O que entra | Onde aparece |
|---|---|---|
| [[N1: spot do exemplo — posições, stack, board/textura]] | Posições, stack e board/textura do spot, com o rótulo exato da tela | Discord, feed (arte e legenda), story, carrossel slide 2 e legenda, landing bullet 3, e-mail |
| [[N2: % de fold do field no exemplo]] | % de fold do field contra o c-bet no spot N1 | idem |
| [[N3: % GTO do mesmo spot e a faixa (de–a)]] | % GTO do fold no mesmo spot e a faixa GTO (de–a) | idem; gancho e título da arte usam só o % central |
| [[N4: diferença field − GTO em pp]] | N2 menos o % GTO central do N3, em pp, sem arredondar a mais do que a tela | idem |
| [[N5: exemplo de pré-flop — célula, GTO e field, desvio]] | Uma célula da grade: qual célula, GTO, field e desvio, de torneio Regular | Carrossel slide 4 (e onde a HUB quiser um pré-flop concreto) |
| [[N6: 1 número de escala/cobertura, SE o arquivo trouxer; senão omita a frase]] | Um número de escala ou cobertura | Rodapé da landing e rodapé das artes; omitir se o arquivo não trouxer |

Regras: N2, N3 e N4 têm de vir do mesmo spot e da mesma leitura. Nenhum número do texto pode ser atribuído a uma imagem que mostre outro.

## Marcadores pendentes (lista completa)
- [[N1: spot do exemplo — posições, stack, board/textura]]
- [[N2: % de fold do field no exemplo]]
- [[N3: % GTO do mesmo spot e a faixa (de–a)]]
- [[N4: diferença field − GTO em pp]]
- [[N5: exemplo de pré-flop — célula, GTO e field, desvio]]
- [[N6: 1 número de escala/cobertura, SE o arquivo trouxer; senão omita a frase]]
- Não há mais marcador de RFI CO/BTN 40bb (virou fato, por decisão da HUB) nem de "o que o Grátis vê" (frase da HUB aplicada).
