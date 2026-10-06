# Field Ranges (Beta): copy de lançamento

Status: rascunho para aprovação do Rafael. Não publicado, sem commit.
@aurapokeranalytics: a confirmar pelo Rafael. URLs com UTM prontas na tabela abaixo.
Fonte única dos números: `numeros-verificados.md` (mesma pasta). Stacks de 20bb+, todos os buy-ins.

## URLs por peça
Base: `https://www.aura.poker/` + `?utm_source=<fonte>&utm_medium=social&utm_campaign=field-ranges-beta&utm_content=<peça>`

| Peça | utm_source | utm_content | URL |
|---|---|---|---|
| Discord PT | discord | discord-pt | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-ranges-beta&utm_content=discord-pt |
| Discord EN | discord | discord-en | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-ranges-beta&utm_content=discord-en |
| Feed (link na bio) | instagram | feed | https://www.aura.poker/?utm_source=instagram&utm_medium=social&utm_campaign=field-ranges-beta&utm_content=feed |
| Story (sticker de link) | instagram | story | https://www.aura.poker/?utm_source=instagram&utm_medium=social&utm_campaign=field-ranges-beta&utm_content=story |
| Carrossel (link na bio) | instagram | carrossel | https://www.aura.poker/?utm_source=instagram&utm_medium=social&utm_campaign=field-ranges-beta&utm_content=carrossel |
| Landing (botão de CTA) | landing | landing | https://www.aura.poker/?utm_source=landing&utm_medium=social&utm_campaign=field-ranges-beta&utm_content=landing |

Observação: para a landing o `utm_source` não estava na lista (discord|instagram); usei `landing`. Ajustar se o Rafael preferir outro valor.

## Rodapés padrão (dois, conforme o número usado)
- **Rodapé DECISÕES** (qualquer arte que use 56,9% e 39,0%, e as sem número de fold):
  - PT: "Dados: Aura · 1,42 bi de decisões · 20bb+ · 18+"
  - EN: "Data: Aura · 1.42B decisions · 20bb+ · 18+"
- **Rodapé MÃOS** (onde o número usado é o 13%/AA ou o 96,4 mi):
  - PT: "Dados: Aura · 96,4 mi de mãos com cartas conhecidas · 20bb+ · 18+"
  - EN: "Data: Aura · 96.4M hands with known cards · 20bb+ · 18+"

Qual rodapé vale por peça: feed = decisões; story = mãos (único lugar do 13%/AA); slides 1 a 6 = decisões (o slide 5 agora cita só o 1,42 bi). Regra: nenhuma arte mistura número de decisões e de mãos sob o mesmo rodapé.
Regras de leitura: "decisões" nunca é "mãos"; o fold de 56,9% e 39,0% é contra 3-bet não all-in; o 13% do AA é "paga em vez de dar 3-bet". Na UI os botões se chamam 3Bet/4Bet; no texto corrido usamos 3-bet/4-bet.

---

# (a) Instagram

## Legenda do feed (1080x1350)

Texto na arte (PT):
- Título: ONDE O FIELD JOGA DIFERENTE
- Spot, uma vez só: Contra 3-bet (não all-in)
- Linha 1: BTN folda 56,9%
- Linha 2: EP folda 39,0%
- Rodapé: DECISÕES
- Números usados: 56,9% e 39,0% (seção 3)
- Nota ao designer: sem marcador de 50% e sem eixo 0/50/100 (vale também para o slide 4).

Texto na arte (EN):
- Title: WHERE THE FIELD PLAYS DIFFERENTLY
- Spot, once: Facing a non-all-in 3-bet
- Line 1: BTN folds 56.9%
- Line 2: EP folds 39.0%
- Footer: DECISIONS

Legenda PT:
```
O BTN abre o range mais largo e é quem mais desiste contra 3-bet (não all-in): 56,9% de fold. O EP folda 39,0%.

Mesma ação, field diferente por posição. Se o BTN larga mais da metade das vezes, o seu 3-bet tende a ter mais fold equity ali. Contra o EP, o 3-bet pede mais critério.

O Field Ranges mostra isso numa grade 13x13, mão a mão, com a trilha open, 3-bet, 4-bet, all-in. Stacks de 20bb+, todos os buy-ins. Uma leitura do field a partir de mais de um bilhão de decisões reais.

Crie sua conta grátis, link na bio.

Dados: Aura, 1,42 bi de decisões. 18+.

#poker #pokerMTT #pokerestudo #pokerstrategy #aurapoker
```

Legenda EN:
```
The BTN opens the widest range and is the position that gives up the most against a non-all-in 3-bet: 56.9% fold. EP folds 39.0%.

Same action, different field by position. If the BTN folds more than half the time, your 3-bet tends to carry more fold equity there. Against EP, the 3-bet needs more care.

Field Ranges shows it on a 13x13 grid, hand by hand, following the trail open, 3-bet, 4-bet, all-in. 20bb+, all buy-ins. A read of the field built from over a billion real decisions.

Create your free account, link in bio.

Data: Aura, 1.42B decisions. 18+.

#poker #MTT #pokerstrategy #pokerstudy #aurapoker
```

## Story (1080x1920)

Nota ao designer (todas as artes de Instagram): sem selo, kicker nem texto "Beta"; o kicker é só "FIELD RANGES". Sem convite a feedback nas artes e legendas.

Texto na arte (PT), 3 telas curtas em um único story:
- Topo: FIELD RANGES
- Centro: "AA no BB contra open do CO: o field só paga 13%." + "(84% dão 3-bet não all-in, 3% vão all-in)"
- Base: "Veja a grade, mão a mão." + botão "Conta grátis" + "18+"
- Números usados: 13%, 84%, 3% (seção 4). Rodapé: MÃOS.

Texto na arte (EN):
- Top: FIELD RANGES
- Center: "AA in the BB vs a CO open: the field only calls 13%." + "(84% non-all-in 3-bet, 3% all-in)"
- Bottom: "See the grid, hand by hand." + button "Free account" + "18+"

Instrução ao designer (fora do texto da arte): o botão de CTA é o sticker de link do Instagram, com o texto "Conta grátis" / "Free account". Sticker de enquete opcional: "Você 3-beta AA ali?" / "Do you 3-bet AA there?" com opções Sempre / Às vezes. / Always / Sometimes.

## Carrossel (6 slides, 1080x1350)

Títulos em caixa alta, corpo em sentence case. Rodapé por slide indicado em cada um.

### Slide 1: gancho
- PT: título "COMO O FIELD JOGA, MÃO A MÃO" / sub "Veja o que ele faz de verdade."
- EN: title "HOW THE FIELD PLAYS, HAND BY HAND" / sub "See what it really does."
- Número: nenhum. Rodapé: DECISÕES.

### Slide 2: a grade
- PT: título "UMA GRADE, UM SPOT" / corpo "13x13: cada célula é uma mão. A cor mostra o que o field faz: paga ou folda." / destaque "CO abre, SB dá 3-bet all-in: veja a resposta do CO, mão a mão."
- EN: title "ONE GRID, ONE SPOT" / body "13x13: each cell is a hand. Color shows what the field does: call or fold." / highlight "CO opens, SB 3-bets all-in: see the CO's response, hand by hand."
- Arte: grade 13x13 na paleta do app (call azul, fold slate), igual ao mockup grade-allin; sem raise, porque contra all-in o CO só paga ou folda. Sem percentuais por célula. Número: nenhum. Rodapé: DECISÕES.

### Slide 3: a trilha
- PT: título "SIGA A MÃO" / corpo "Open, 3-bet, 4-bet, all-in. Escolha as posições na mesa de 6 lugares e filtre por stack e buy-in." / destaque "90 situações com a grade pronta."
- EN: title "FOLLOW THE HAND" / body "Open, 3-bet, 4-bet, all-in. Pick positions on the 6-seat table and filter by stack and buy-in." / highlight "90 spots with the grid ready."
- Número: 90 situações (seção 2). Rodapé: DECISÕES.

### Slide 4: exemplo de exploit
- PT: título "ONDE EXPLORAR" / corpo "Contra 3-bet (não all-in), o BTN folda 56,9%. O EP folda 39,0%." / destaque "BTN larga mais da metade: o seu 3-bet tende a ter mais fold equity. EP: mais critério."
- EN: title "WHERE TO EXPLOIT" / body "Facing a non-all-in 3-bet, the BTN folds 56.9%. EP folds 39.0%." / highlight "BTN gives up more than half: your 3-bet tends to carry more fold equity. EP: more care."
- Números: 56,9% e 39,0% (seção 3). Rodapé: DECISÕES. O AA/13% fica só no story.

### Slide 5: base e CTA
- PT: título "A BASE POR TRÁS DA GRADE" / corpo "Leitura do field sobre 1,42 bi de decisões pré-flop reais. Stacks de 20bb+, todos os buy-ins." / botão "Conta grátis"
- EN: title "THE DATA BEHIND THE GRID" / body "A read of the field over 1.42B real preflop decisions. 20bb+ stacks, all buy-ins." / button "Free account"
- Número: 1,42 bi de decisões (seção 1). Rodapé: DECISÕES.

### Slide 6: CTA
- PT: título "ABRA O FIELD RANGES" / corpo "Crie sua conta grátis e veja o seu próximo spot." / botão "Link na bio" / "18+"
- EN: title "OPEN FIELD RANGES" / body "Create your free account and see your next spot." / button "Link in bio" / "18+"
- Número: nenhum. Rodapé: DECISÕES.

### Legenda do carrossel
PT:
```
O Field Ranges mostra o que o field faz de verdade, mão a mão.

Exemplo: contra 3-bet (não all-in) o BTN folda 56,9%, o EP 39,0%. E o AA do BB contra open do CO só paga 13% das vezes. Cada leitura vira uma decisão sua: onde 3-betar mais, onde pedir mais critério.

Grade 13x13, trilha open, 3-bet, 4-bet, all-in, mesa de 6 lugares e filtros de stack e buy-in. 90 situações, 20bb+. Uma leitura do field a partir de mais de um bilhão de decisões reais.

Salve para estudar.

Crie sua conta grátis, link na bio.

Dados: Aura, 1,42 bi de decisões (o 13% do AA vem de 96,4 mi de mãos com cartas conhecidas). 18+.

#poker #pokerMTT #pokerestudo #pokerstrategy #aurapoker
```
EN:
```
Field Ranges shows what the field really does, hand by hand.

Example: facing a non-all-in 3-bet the BTN folds 56.9%, EP 39.0%. And AA in the BB against a CO open only calls 13% of the time. Each read becomes your decision: where to 3-bet more, where to take more care.

13x13 grid, trail open, 3-bet, 4-bet, all-in, 6-seat table and stack and buy-in filters. 90 spots, 20bb+. A read of the field built from over a billion real decisions.

Save it for study.

Create your free account, link in bio.

Data: Aura, 1.42B decisions (the AA 13% comes from 96.4M hands with known cards). 18+.

#poker #MTT #pokerstrategy #pokerstudy #aurapoker
```

---

# (b) Landing

@aurapokeranalytics: a confirmar pelo Rafael. URL do CTA: ver a linha "Landing" da tabela "URLs por peça" no topo.

## Título
- PT: Veja como o field joga cada mão
- EN: See how the field plays every hand

## Subtítulo
- PT: Field Ranges (Beta): uma grade 13x13 para cada spot pré-flop, com a trilha open, 3-bet, 4-bet e all-in. Leitura do field a partir de mais de um bilhão de decisões reais, stacks de 20bb+, todos os buy-ins.
- EN: Field Ranges (Beta): a 13x13 grid for every preflop spot, following the trail open, 3-bet, 4-bet and all-in. A read of the field built from over a billion real decisions, 20bb+ stacks, all buy-ins.

## 3 bullets
PT:
- Mão a mão: em CO abre e SB dá 3-bet all-in, veja quanto o field dá call e fold com cada mão do CO.
- Siga a trilha: escolha as posições na mesa de 6 lugares, avance de open a all-in e filtre por stack e buy-in. 90 situações com grade.
- Ache onde explorar: contra 3-bet (não all-in), o BTN dá fold em 56,9% das vezes. O EP, em 39,0%. Base de 1,42 bi de decisões e 96,4 mi de mãos com cartas conhecidas.

EN:
- Hand by hand: in CO opens and SB 3-bets all-in, see how often the field calls and folds with every CO hand.
- Follow the trail: pick positions on the 6-seat table, step from open to all-in and filter by stack and buy-in. 90 spots with a grid.
- Find where to exploit: facing a non-all-in 3-bet, the BTN folds 56.9% of the time. EP folds 39.0%. Built on 1.42B decisions and 96.4M hands with known cards.

Nota de rodapé da seção (PT): "O fold de 56,9% e 39,0% é contra 3-bet não all-in e conta decisões, não mãos. Leitura do field a partir de mais de um bilhão de decisões reais. Beta: conte o que faltou."
Footnote (EN): "The 56.9% and 39.0% folds are against non-all-in 3-bets and count decisions, not hands. A read of the field built from over a billion real decisions. Beta: tell us what is missing."
CTA: PT "Criar conta grátis" / EN "Create free account".
Números usados na landing: 56,9%, 39,0% (seção 3), 90 (seção 2), 1,42 bi, 96,4 mi (seção 1). Esses números ficam só no texto, nunca atribuídos a uma imagem.

## Alt text das 3 imagens

### Imagem 1: grade 13x13 num spot de all-in
- PT: "Grade 13x13 de mãos de poker no spot CO abre e SB dá 3-bet all-in, mostrando a resposta do CO. Cada célula é uma mão, colorida pela frequência de fold e de call do field."
- EN: "13x13 poker hand grid for the spot CO opens and SB 3-bets all-in, showing the CO's response. Each cell is a hand, colored by the field's fold and call frequency."

### Imagem 2: trilha da mão com a mesa
- PT: "Painel do Field Ranges (Beta): mesa de 6 lugares com CO abrindo e SB dando 3-bet, botões de próximo passo (4Bet e 4Bet all-in) e filtros de stack efetivo e buy-in."
- EN: "Field Ranges (Beta) panel: 6-seat table with CO opening and SB 3-betting, next-step buttons (4Bet and 4Bet all-in) and effective stack and buy-in filters."

### Imagem 3: contraste entre dois spots
- PT: "Duas grades 13x13 lado a lado: como o BB responde ao open do EP e ao open do CO. Cada célula é uma mão, colorida por fold, call, 3-bet e 3-bet all-in."
- EN: "Two 13x13 grids side by side: how the BB responds to an EP open and to a CO open. Each cell is a hand, colored by fold, call, 3-bet and 3-bet all-in."
- Nota para o designer: a imagem 3 não mostra percentuais. Não atribuir a ela o 56,9% nem o 39,0% (esses vêm do fold do open contra 3-bet, outro spot).

---
