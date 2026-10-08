# Modo GTO: copy de lançamento

Status: rascunho com marcadores; não publicado. Sem commit. Entra no ar em 08/10/2026.
@aurapokeranalytics: a confirmar pelo Rafael. URLs com UTM prontas na tabela abaixo.
Fonte única dos números: `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md`, que **ainda não existe**. Nenhum número foi inventado: todo valor é um marcador `[[N1..N6]]` e está mapeado no bloco "Números usados" no fim.
Peças deste pacote: Discord (também em `discord.md`), Instagram (feed, story, story da capa em PT, carrossel só em EN), landing e e-mail (em `email.md`).

> **Regra de texto das artes (Rafael, 08/10): "muita informação, muito texto; não pode ter tanto texto em nenhum post".** Cada arte tem no máximo UM título curto (~6 palavras) e, se precisar, UMA linha de apoio (~10 palavras). A imagem fala: barras field × GTO lado a lado, com os números. O detalhe vai para a legenda. Fora das artes: kicker, selo, CTA empilhado e rodapé longo. Em toda arte só ficam o `@aurapokeranalytics` e o `18+`, pequenos. O link é o sticker/link na bio, não texto de arte. A frase do plano Grátis fica na legenda e no e-mail, não nas artes.

> **Candidato para a HUB confirmar (não usado no texto).** O roteiro de go-live (`03-roteiro-go-live.md`, passo 6) traz um spot que serve ao eixo "field folda acima da faixa GTO": SB×BB 3-bet, 30.1–60bb, Unpaired Rainbow Disconnected A, Fold vs Flop CBet, GTO 25,2% (19,2–31,2), com field ≈ 34% e Overfold. O "≈ 34%" é aproximado; o arquivo de números precisa trazer o valor exato do dia, medido na Azure. O mesmo spot tem turn (Fold vs Second Barrel, GTO 28,8%, 21,8–35,8) se a HUB quiser um segundo exemplo. Nada disso entrou no texto; os marcadores seguem abertos.

## Pendências de produto (conferir antes de aprovar)
1. **Só publicar depois do passo 6 do roteiro (teste logado do Rafael).** O link leva ao app e o texto promete o módulo; nada sai antes de o Modo GTO estar ligado (passos 4 e 5) e conferido.
2. **Pré-flop 20261007 (atualização da HUB).** O RFI de CO e BTN a 40bb entra no lançamento (pré-flop `20261007`, aprovado e mesclado) e as peças o dizem como fato. O cabeçalho do `03-roteiro-go-live.md` ainda fala em `20261005` e diz que o `20261007` vem depois. Seguimos a HUB; vale o roteiro ser corrigido.
3. **Reação a raise: só o que existe.** As peças dizem "no flop do SRP". Apertei o "no SRP" do briefing para "no flop do SRP" porque a tabela de reação a raise (`tbl_gto_flop_node`) é do flop; se existir reação a raise no turn, trocar. Num 3-bet CO×BB a 40bb a reação a raise não tem GTO (exclusão até regerar, 6 células de 3-bet re-resolvidas a 40/60bb), então nenhuma peça diz "toda reação a raise em todo spot". A captura do slide 3 não pode mostrar esse caso.
4. **Pré-flop "em cada célula".** O briefing diz que cada célula da grade traz GTO e desvio; o roteiro mede isso a 20–30bb e a cobertura varia por spot e stack. As legendas dizem "em cada célula da grade". Se houver célula sem GTO na tela, trocar por "nas células da grade".
5. **O que o Grátis vê (resolvido pela HUB, lido do código).** Conta Grátis (e Individual) não vê número GTO nem faixa; segue com o field e a comparação com o MDF, e o GTO aparece como cadeado "Disponível no Modo GTO", que abre o upgrade "Desbloqueie o Modo GTO". Frase única, PT: "O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO." EN: "GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan." Ela vive na legenda, no Discord, na landing e no e-mail, nunca na arte. Os CTAs são "Conhecer o Modo GTO" / "See GTO Mode"; nenhum diz "grátis". Nenhuma peça fala em "prévia" nem "borrado": o que o Grátis vê é um cadeado. Individual é plano pago e também não vê GTO; por isso as peças dizem "plano Modo GTO" e não "planos pagos".
6. **O exemplo é um spot, não a média do field.** As legendas dizem isso. O "como explorar" (field folda acima da faixa GTO, então o c-bet de bluff tem mais fold equity do que o GTO) **só vale se o spot escolhido tiver o field acima do topo da faixa GTO no fold contra o c-bet**. Se a HUB escolher outro spot, ajustar. Se o field ficar abaixo da faixa, trocar a leitura para, PT: "O field folda abaixo da faixa GTO, então aqui o c-bet de bluff tem menos fold equity do que o GTO; estude o c-bet por valor." / EN: "The field folds below the GTO range, so here the bluff c-bet has less fold equity than GTO; study value c-bets." Nas artes, o título da arte de exemplo ("Mesmo spot, dois números") vale nos dois casos.
7. **Números nas barras.** As artes mostram o N2 e o N3 nas barras: o % central do N3 no rótulo e a faixa (de–a) como sombreado da barra do GTO. A diferença (N4) e o spot (N1, salvo no feed) ficam na legenda.
8. **Nome em inglês.** Usei "GTO Mode" (é o rótulo do toggle e das FAQs do aura-landing). Confirmar.
9. **Torneios vanilla.** O produto mostra a ressalva de metodologia (GTO se refere a torneios Vanilla) só dentro do ⓘ e da página de Metodologia, por decisão do Rafael. Nenhuma peça a repete; o spot do exemplo e a célula de pré-flop (N5) devem ser de torneio Regular, para não contradizer a ressalva.
10. **Sem "Beta" e sem preço.** Se o Rafael quiser o convite a feedback, entra como frase extra no Discord.
11. **`product-truth-aura.md`** não existe neste worktree. Li `AGENTS.md`, `brand/brand-kit.md`, o plano de marketing, o roteiro de go-live e os modelos do Field Trends e do PR 1. Se o arquivo existir em outro lugar, vale uma conferência das frases de produto.
12. **Landing.** O texto da landing é o do modo de lançamento do `aura-landing` (flag `VITE_LAUNCH_MODO_GTO`); a lista de cobertura por posição segue fora do texto, porque não está fechada.
13. **Carrossel só em EN (Rafael, 08/10).** A capa tem versão PT-BR em story 1080x1920. As legendas PT e EN do carrossel ficam. Não há story EN da capa: a capa EN é o slide 1 do carrossel.

## Regra de leitura do exemplo
O exemplo é um spot (N1), com o field (N2) e o GTO com a faixa (N3) lado a lado, e a diferença (N4). Frase padrão das legendas, PT: "O field folda acima da faixa GTO, então aqui o c-bet de bluff tem mais fold equity do que o GTO. É um spot, não a média do field. Confira no seu board." EN: "The field folds above the GTO range, so here the bluff c-bet has more fold equity than GTO. This is one spot, not the field average. Check it on your board." Sem promessa de resultado.

## URLs por peça
Regra: Discord leva ao app (`https://www.aura.poker/`); Instagram e e-mail levam à landing (`https://www.aurapoker.com/`). Parâmetros: `utm_source=<fonte>&utm_medium=<meio>&utm_campaign=modo-gto-launch&utm_content=<peça>`.

| Peça | Idioma | Destino | utm_source | utm_content | URL |
|---|---|---|---|---|---|
| Discord PT | PT | app | discord | discord-pt | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt |
| Discord EN | EN | app | discord | discord-en | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en |
| Feed (link na bio) | PT e EN | landing | instagram | feed | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=feed |
| Story (sticker de link) | PT e EN | landing | instagram | story | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=story |
| Story da capa do carrossel (sticker de link) | PT | landing | instagram | story-capa-pt | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=story-capa-pt |
| Carrossel, só EN (link na bio) | EN (legenda PT e EN) | landing | instagram | carrossel-en | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=carrossel-en |
| Landing (botão de CTA, para o cadastro no app) | PT e EN | app | landing | modo-gto (utm_medium=website) | https://www.aura.poker/Login?tab=signup&utm_source=landing&utm_medium=website&utm_campaign=modo-gto-launch&utm_content=modo-gto |
| E-mail PT | PT | landing | email | pt | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=pt |
| E-mail EN | EN | landing | email | en | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=en |

Observação: para o botão da landing mantive `utm_source=landing`, como no Field Trends. Ajustar se o Rafael preferir outro valor.

## Rodapé
- **Artes:** só `@aurapokeranalytics · 18+`, pequeno. Sem "Ferramenta de estudo", sem "Dados:", sem selo empilhado.
- **Legendas, landing e e-mail:** PT "Ferramenta de estudo. 18+." / EN "Study tool. 18+." (na landing, também "A Aura não é site de apostas e não oferece jogo.").

---

# (a) Instagram

## Texto final de cada arte (título + apoio)

Marcadores `[[N..]]` entram nas barras ou na captura; não são texto corrido. Em toda arte: `@aurapokeranalytics · 18+`, pequeno, e mais nada.

| Arte | Formato | Idioma | Título | Apoio (uma linha) | O que a imagem mostra |
|---|---|---|---|---|---|
| Feed | 1080x1350 | PT | Mesmo spot, dois números | [[N1: spot do exemplo — posições, stack, board/textura]] | Barras field × GTO lado a lado: [[N2]] e [[N3]], faixa GTO sombreada |
| Feed | 1080x1350 | EN | Same spot, two numbers | [[N1]] | Barras field × GTO: [[N2]] e [[N3]], faixa GTO sombreada |
| Story | 1080x1920 | PT | O field folda mais que o GTO? | Veja o gap no seu spot. | Barras field × GTO: [[N2]] e [[N3]]; sticker de link "Conhecer o Modo GTO" |
| Story | 1080x1920 | EN | Does the field fold more than GTO? | See the gap in your spot. | Barras field × GTO: [[N2]] e [[N3]]; link sticker "See GTO Mode" |
| Story da capa do carrossel | 1080x1920 | PT | Onde o field sai do GTO? | Novo: Modo GTO | Barras field × GTO com o gap em âmbar ([[N2]], [[N3]]); sticker de link "Conhecer o Modo GTO" |
| Carrossel 1 (capa) | 1080x1350 | EN | Where does the field leave GTO? | New: GTO Mode | Mesma imagem da capa PT |
| Carrossel 2 | 1080x1350 | EN | Same spot, two numbers | (nenhum) | Só as barras e os dois números: [[N2]] e [[N3]] |
| Carrossel 3 | 1080x1350 | EN | Postflop: GTO and range | SRP and 3-bet, flop and turn. Raise response on SRP flop. | Captura do Postflop com o Modo GTO ligado |
| Carrossel 4 | 1080x1350 | EN | Preflop: GTO and deviation | Includes CO and BTN RFI at 40bb. | Captura da grade com a célula do [[N5: exemplo de pré-flop — célula, GTO e field, desvio]] destacada |
| Carrossel 5 | 1080x1350 | EN | GTO Mode is a paid plan | (nenhum) | O cadeado "Disponível no Modo GTO" do app |
| Carrossel 6 (CTA) | 1080x1350 | EN | See GTO Mode | Link in bio. | Logo e fundo da marca |

Notas de arte:
- **Cores:** fold em teal `#015A6B`; a distância entre a barra do field e a do GTO em âmbar (o gap). Faixa GTO sombreada em volta da barra do GTO.
- **Slide 3 (carrossel):** a captura não pode mostrar reação a raise de 3-bet CO×BB a 40bb (sem GTO).
- **Slide 4:** o N5 aparece só dentro da captura, destacado na célula, de torneio Regular. Nenhum texto de arte repete o número.
- **Slide 5:** cadeado do app. Sem "prévia", sem borrado, sem preço. A frase do plano Grátis fica na legenda.
- **Sem story EN da capa:** a capa EN é o slide 1 do carrossel.
- **Enquete opcional no story (fora da arte):** "Qual spot você quer ver com o GTO ao lado?" com as opções "SRP" e "3-bet" / "Which spot do you want to see with GTO next to it?" with "SRP" and "3-bet".

## Legendas

### Legenda do feed
PT:
```
O GTO folda [[N3: % GTO do mesmo spot e a faixa (de–a)]]. O field folda [[N2: % de fold do field no exemplo]]. Mesmo spot.

Novo na Aura: Modo GTO. Ao lado de cada número do field, o número GTO e a faixa GTO.

Exemplo: [[N1: spot do exemplo — posições, stack, board/textura]]. Diferença de [[N4: diferença field − GTO em pp]] pp no fold contra o c-bet. O field folda acima da faixa GTO, então aqui o c-bet de bluff tem mais fold equity do que o GTO. É um spot, não a média do field. Confira no seu board.

Pós-flop: SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP. Pré-flop: o GTO e o desvio em cada célula da grade, inclusive o RFI de CO e BTN a 40bb.

O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO.

Conhecer o Modo GTO, link na bio. Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
GTO folds [[N3: GTO % of the same spot and the range (from–to)]]. The field folds [[N2: field fold % in the example]]. Same spot.

New on Aura: GTO Mode. Next to every field number, the GTO number and the GTO range.

Example: [[N1: example spot — positions, stack, board/texture]]. A gap of [[N4: field − GTO difference in pp]] pp on the fold to the c-bet. The field folds above the GTO range, so here the bluff c-bet has more fold equity than GTO. This is one spot, not the field average. Check it on your board.

Postflop: SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop. Preflop: the GTO and the deviation in every grid cell, including the CO and BTN RFI at 40bb.

GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan.

See GTO Mode, link in bio. Study tool. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

### Legenda do carrossel e da capa
PT (usar também com o story da capa, se o Rafael postar legenda):
```
Onde o field sai do GTO?

Novo na Aura: Modo GTO. Ao lado de cada número do field, o número GTO e a faixa GTO, no pós-flop (SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP) e no pré-flop (o GTO e o desvio em cada célula da grade, inclusive o RFI de CO e BTN a 40bb).

Exemplo: [[N1: spot do exemplo — posições, stack, board/textura]]. O field folda [[N2: % de fold do field no exemplo]] contra o c-bet; o GTO folda [[N3: % GTO do mesmo spot e a faixa (de–a)]]. Diferença de [[N4: diferença field − GTO em pp]] pp. Acima da faixa GTO, o c-bet de bluff tem mais fold equity do que o GTO. Abaixo, estude o c-bet por valor. É um spot, não a média do field. Confira no seu board.

O Modo GTO é um plano pago. A conta grátis segue com o field e a comparação com o MDF; o número GTO e a faixa são do plano Modo GTO.

Conhecer o Modo GTO, link na bio. Salve para estudar. Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
Where does the field leave GTO?

New on Aura: GTO Mode. Next to every field number, the GTO number and the GTO range, postflop (SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop) and preflop (the GTO and the deviation in every grid cell, including the CO and BTN RFI at 40bb).

Example: [[N1: example spot — positions, stack, board/texture]]. The field folds [[N2: field fold % in the example]] to the c-bet; GTO folds [[N3: GTO % of the same spot and the range (from–to)]]. A gap of [[N4: field − GTO difference in pp]] pp. Above the GTO range, the bluff c-bet has more fold equity than GTO. Below it, study the value c-bet. This is one spot, not the field average. Check it on your board.

GTO Mode is a paid plan. The free account keeps the field and the MDF comparison; the GTO number and range are on the GTO Mode plan.

See GTO Mode, link in bio. Save it for study. Study tool. 18+.

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

Texto completo, com URLs, em `discord.md` (mesma pasta). PT e EN, até cerca de 1.200 caracteres cada (cerca de 1.050 PT e 1.080 EN com valores típicos nos marcadores; recontar depois de preencher), 3 emojis funcionais (📊 título, 🔎 convite, 👉 CTA). **Só postar depois do passo 6 do roteiro.** A regra de pouco texto vale para artes; o Discord segue como estava.

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

Texto, assuntos, preheader e notas técnicas em `email.md`. Assunto recomendado: a 1 ("Novo na Aura: Modo GTO" / "New on Aura: GTO Mode"). Botão "Conhecer o Modo GTO" / "See GTO Mode". HTML não produzido nesta rodada. O mockup do e-mail segue a regra das artes: as duas barras e os dois números, sem texto extra.

---

## Números usados (marcadores; fonte: `numeros-verificados.md`, ainda inexistente)

| Marcador | O que entra | Onde aparece |
|---|---|---|
| [[N1: spot do exemplo — posições, stack, board/textura]] | Posições, stack e board/textura do spot, com o rótulo exato da tela | **Arte:** linha de apoio do feed (PT e EN). **Texto:** legendas do feed e do carrossel, Discord, landing bullet 3, e-mail. Fora do feed, as artes não trazem o spot |
| [[N2: % de fold do field no exemplo]] | % de fold do field contra o c-bet no spot N1 | **Arte:** barra do field no feed, no story, no story da capa e no carrossel slide 2. **Texto:** legendas, Discord, landing, e-mail |
| [[N3: % GTO do mesmo spot e a faixa (de–a)]] | % GTO do fold no mesmo spot e a faixa GTO (de–a) | **Arte:** barra do GTO (% central no rótulo, faixa como sombreado) nas mesmas artes do N2. **Texto:** gancho das legendas do feed (só o % central), legendas, Discord, landing, e-mail |
| [[N4: diferença field − GTO em pp]] | N2 menos o % GTO central do N3, em pp, sem arredondar a mais do que a tela | **Só texto:** legendas, Discord, landing, e-mail. Não vai em arte |
| [[N5: exemplo de pré-flop — célula, GTO e field, desvio]] | Uma célula da grade: qual célula, GTO, field e desvio, de torneio Regular | **Arte:** só dentro da captura do slide 4 do carrossel, na célula destacada. Nenhum texto de arte repete o número |
| [[N6: 1 número de escala/cobertura, SE o arquivo trouxer; senão omita a frase]] | Um número de escala ou cobertura | **Só landing** (nota de rodapé). Saiu das artes. Omitir se o arquivo não trouxer |

Regras: N2, N3 e N4 têm de vir do mesmo spot e da mesma leitura. Nenhum número do texto pode ser atribuído a uma imagem que mostre outro.

## Marcadores pendentes (lista completa)
- [[N1: spot do exemplo — posições, stack, board/textura]]
- [[N2: % de fold do field no exemplo]]
- [[N3: % GTO do mesmo spot e a faixa (de–a)]]
- [[N4: diferença field − GTO em pp]]
- [[N5: exemplo de pré-flop — célula, GTO e field, desvio]]
- [[N6: 1 número de escala/cobertura, SE o arquivo trouxer; senão omita a frase]]
- Não há marcador de RFI CO/BTN 40bb (virou fato, por decisão da HUB) nem de "o que o Grátis vê" (frase da HUB aplicada).
