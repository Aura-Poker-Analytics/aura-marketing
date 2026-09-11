# board01-1560-carrossel · Carrossel 4:5 (EN)

**Campanha:** AURA-BOARD01 · **`utm_content`:** `board01-1560-carrossel-en`
**Entrega:** 5 cards PNG 1080×1350 nesta pasta, numerados `-01` a `-05` (a ordem é a ordem de upload)

Versão estática do reel [board01-1560-boards](../../reels/board01-1560-boards/roteiro.md) — mesma
promessa, mesmos painéis. O conceito, os números e a checagem de compliance estão lá; aqui só o que
é específico do formato.

## Por que carrossel além do reel

Os painéis são **densos**. No reel, a cena de Size distribution dura 4,4s — ninguém lê seis barras
com número em 4,4s. No carrossel cada painel fica parado o tempo que o leitor quiser, que é o que
esse conteúdo pede. Não substitui o reel: o reel ganha alcance, o carrossel ganha leitura.

## Os 5 cards

| # | título | painel |
|---|---|---|
| 01 | **1,560 boards.** | superfície de seleção, tudo aberto |
| 02 | **Three clicks.** | board definido — Two-tone, OESD possible, ace high |
| 03 | **The sizes it used.** | Size distribution |
| 04 | **Defense vs MDF.** | Exploitative Sizes |
| 05 | CTA — *Study the field. Free to start.* | — |

Cinco cards = os quatro painéis distintos que existem, sem repetir nenhum, mais o CTA.

## Três decisões de formato que custaram render

1. **`fitContain` (novo flag opt-in no `carrossel-slide`).** O padrão do template é
   `object-fit: cover`, que corta a imagem — e num print de produto o que se perde são justamente as
   bordas e a coluna de números da direita. O flag é opt-in pra não mexer nos carrosséis que já
   dependem do `cover`.

2. **Teto de 740px na altura do painel.** Sem teto os cards 1 e 2 empurravam o texto e o rodapé pra
   fora dos 1350px. 740 é o maior valor em que os cinco fecham.

3. **`?compact=1` no mockup de resultado.** Tira o rail de Active Context e o "Total". Sem isso o
   painel de Size distribution só cabia encolhido a ~745px de largura, e aí o texto voltava a ficar
   ilegível — que é exatamente o problema que o carrossel existe pra resolver. Com o compact ele cabe
   em largura quase cheia.

**Títulos de uma linha e corpo de uma linha** são requisito, não estilo: título de duas linhas come
~150px e derruba o painel abaixo do limite legível.

## ⚠️ Não usar `carrossel-capa` nesta campanha

O mock de UI dela é um Exploit Card com `−14 pts · Confiança alta · 480k mãos` **hardcoded no
template** — dado fabricado. O card 01 aqui é um `carrossel-slide` fazendo as vezes de capa. Se for
usar a capa em outro post, troque esses valores antes.

## Compliance específico do formato

Cards 03 e 04 **não afirmam "nesse board"** — mesma razão do reel: os números do painel são reais mas
vêm do print `CO/BB` **sem** filtro de board, e o rail de contexto foi removido pelo `compact`. As
legendas descrevem **o que volta**, não de que recorte. Quando o output real de um bucket filtrado
chegar, isso muda nos dois formatos de uma vez.

## Legenda EN (para postar)

> **1,560 board buckets** in Postflop Analysis. 73 on the flop, 615 on the turn, 872 on the river.
>
> One row per attribute, and you switch on whatever you want:
> **Pairing** — Unpaired, Paired · **Tone** — Rainbow, Two-tone, Monotone · **Connectedness** —
> Disconnected, OESD possible, Connected · **High card** — from low to A
>
> On the turn and the river, three more rows: **what the card changed** — a flush draw that appeared,
> a flush that completed, an overcard that came, a straight on board.
>
> The filters stack. Two-tone, with OESD possible, ace high: three clicks.
>
> Then you run it — and you get which size the field used, and how much it defended against each one
> vs MDF.
>
> Not "postflop" in general. The board you actually wanted to study.
>
> Free to start · aurapoker.com · 18+

## Como regerar

```
node instagram/build-board1560.mjs --en            # os mockups (rode antes, se faltarem)
node instagram/build-board1560-carrossel.mjs       # os 5 cards
```
Cards: `deck.js` (`cb-1-en`…`cb-5-en`). O build renderiza sozinho as variantes `-c` (compactas) do
painel de resultado.
