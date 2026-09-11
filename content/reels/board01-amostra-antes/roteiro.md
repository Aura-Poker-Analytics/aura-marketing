# board01-amostra-antes · Anúncio de lançamento — seleção de board (Postflop)

**Campanha:** AURA-BOARD01 · **`utm_content`:** `board01-amostra-antes` · **EN:** `board01-amostra-antes-en`
**Entrega:** `content/paid/AURA-BOARD01/` — MP4 9:16 **19,40s** (PT e EN) + capas 1080×1920
**Mockups:** `instagram/templates/shots/mockup-board-*` — 4 passos × PT/EN × 2 variantes (reel e wide)

**Ângulo escolhido:** o mais forte dos três do brief — *você vê o tamanho da amostra antes de
clicar*. Os outros dois (riscado no impossível, multi-seleção) entram como prova, não como manchete.

---

## Cenas (corte seco)

| # | dur | Conteúdo |
|---|---|---|
| 1 | 3,2s | **GANCHO** — logo · `Postflop · Textura de board` · **"Quantas mãos tem atrás desse filtro?"** |
| 2 | 3,8s | `Antes de clicar` · *"Cada chip mostra quanto da amostra ele segura."* · painel no estado de abertura (tudo em **Todos**, massa em cada chip) |
| 3 | 4,6s | `Clicou em Two-tone` · *"A fileira **Conectividade recalcula sozinha**."* · painel recalculado · **push-in lento** |
| 4 | 4,2s | `Monotone + pareado não existe` · *"O chip **risca sozinho** — sem tela vazia."* · **Pareado 0,00%** riscado |
| 5 | 3,6s | **CTA** — *Seleção de board, agora em uma superfície só* · `Grátis pra começar` · Sem cartão · aurapoker.com |

**As cenas 2 e 3 têm layout idêntico de propósito.** Mesma largura de painel, mesma posição, legenda
de uma linha nas duas — então o corte seco entre elas **lê como o recálculo acontecendo**. Era o
passo 2 do brief ("os números da linha Conectividade recalculam na frente da câmera"), que num vídeo
sem cursor só dá pra contar por corte. É por isso que as legendas dessas duas cenas são curtas: se
uma quebrar em duas linhas, o painel desce e a emenda deixa de funcionar.

**Capa estática** = cena 3 (passo 2 congelado, massa visível em todos os chips), exatamente como o
brief pediu para o caso de não ser GIF.

9:16 1080×1920 · sem áudio · selo `500M+ mãos auditadas · 7 salas` em todas as cenas · 18+ em todo
quadro · zonas seguras conferidas com `--guides` antes do encode.

---

## O mockup

`instagram/templates/mockup-board-facets.html` — **recriado**, não é captura.

**As porcentagens não foram inventadas.** A distribuição medida do flop está embutida no template e
cada chip é recalculado com a mesma matemática do produto: a massa de um nível é **condicionada aos
outros atributos já selecionados**. Por isso a fileira Conectividade muda sozinha entre o passo 1 e
o passo 2 — ninguém digitou aqueles números, eles saem do dado.

Pelo mesmo motivo o **Pareado risca sozinho** no passo 4: não existe nenhuma linha
pareado+monotone no extrato, então a massa dá 0,00% e o chip desabilita. Nada de tabela de
combinações impossíveis escrita à mão.

Duas variantes, geradas juntas:

| variante | tamanho | uso |
|---|---|---|
| `mockup-board-sN.png` | 912×820 (@2×) | dentro do anúncio 9:16 — painel **estreito, tipo grande** |
| `mockup-board-wide-sN.png` | 1180×468 (@2×) | imagem solta (post, carrossel, docs) |

A variante `reel` existe porque a larga, reduzida pra caber num quadro 9:16, deixa o texto do chip
ilegível no celular. Ela sobe de escala em vez de descer, e as fileiras quebram em duas linhas — o
que sobra de altura no 9:16 absorve isso de graça.

O canvas é **medido, não chutado**: a página publica `fit:LxA` no `<title>` e o build lê isso antes
de tirar o screenshot. Margem sobrando viraria faixa clara dentro do `.shotframe`.

---

## Legenda — PT

> Todo filtro de textura de board te deixa descobrir tarde demais que o número bonito na tela foi
> construído em cima de quase nada.
>
> No Postflop Analysis, cada chip agora mostra **quanto da sua amostra ele segura** — recalculado a
> cada clique. Você vê a massa **antes** de filtrar, não depois.
>
> A textura mais comum segura ~30% da sua amostra. A mais rara, menos de 1%. Filtrar às cegas entre
> essas duas pontas é a diferença entre ler sinal e ler ruído.
>
> O que mudou:
> • A massa aparece no chip, antes do clique.
> • Combinação impossível fica **riscada** em vez de devolver tela vazia. Monotone e pareado não
>   coexistem — duas cartas do mesmo rank têm naipes diferentes.
> • **Multi-seleção**: "Rainbow ou Two-tone" numa consulta só.
>
> Três superfícies viraram uma: uma fileira por atributo — Pareamento, Tom, Conectividade, Carta
> alta — e, no turn e no river, o que a carta mudou. São 13 famílias de board.
>
> **Não é dado novo.** Nenhuma estatística nova, nenhum reparse. É o filtro ficando honesto sobre o
> tamanho da amostra.
>
> Grátis pra começar · aurapoker.com · 18+

## Legenda — EN

> Every board-texture filter lets you find out too late that the pretty number on screen was built
> on almost nothing.
>
> In Postflop Analysis, each chip now shows **how much of your sample it holds** — recomputed on
> every click. You see the mass **before** you filter, not after.
>
> The most common texture holds ~30% of your sample. The rarest, under 1%. Filtering blind between
> those two ends is the difference between reading signal and reading noise.
>
> What changed:
> • The mass shows on the chip, before the click.
> • Impossible combinations are **struck out** instead of returning an empty screen. Monotone and
>   paired cannot coexist — two cards of the same rank have different suits.
> • **Multi-select**: "Rainbow or Two-tone" in a single query.
>
> Three surfaces became one: one row per attribute — Pairing, Tone, Connectedness, High card — and,
> on the turn and river, what the card changed. 13 board families.
>
> **This is not new data.** No new stats, no reparse. It's the filter getting honest about sample
> size.
>
> Free to start · aurapoker.com · 18+

---

## Vocabulário (não negociado)

**Desconectado · OESD possível · Conectado.** Nunca "seco": o eixo mede só potencial de sequência, e
"monotone seco" é um absurdo — AsKs9s é tudo menos seco.
**Rainbow, Two-tone, Monotone, Overcard, Flush draw** ficam em inglês nos dois idiomas — é o
vernáculo do jogador em PT-BR. Travado no template e no deck.

Decimais: vírgula no PT, ponto no EN (o mockup troca junto, via `?lang=en`).

## Compliance conferido

- **Zero contagem absoluta de mãos** em qualquer asset. O painel de referência tem uma linha de
  contagem embaixo da massa; ela foi **removida de propósito** do mockup. Só percentual sai daqui.
- **Nada promete dado novo.** O anúncio fala de filtro e de amostra, nunca de estatística nova — o
  próprio CTA é "uma superfície só", não "novos dados".
- Sem promessa de lucro/EV/winrate · sem dinheiro/fichas · sem tom guru · sem concorrente citado ·
  grátis = **começar** (preview), nunca "completo grátis" · 18+ em todo quadro.

---

## ⚠️ Dois números do brief que eu não consegui reproduzir

Recalculei a distribuição a partir do extrato que veio na referência de interação. Dois batem, dois
não:

| brief | recalculado | |
|---|---|---|
| 13 famílias de board | **13** | ✅ bate exato |
| textura mais comum ~30% | **30,84%** | ✅ bate |
| textura mais rara 0,78% | **0,75%** | ⚠️ não bate |
| 64 classes-folha | **73** | ⚠️ não bate |

Por isso **nenhum dos dois divergentes saiu no criativo nem na legenda**: escrevi "menos de 1%"
(verdadeiro sob as duas leituras) e não citei contagem de folhas. O `0,75%` aparece **na tela** do
passo 4, como o chip `Conectado` sob Monotone — que é exatamente a família mais rara. Se eu tivesse
posto `0,78%` na legenda, o leitor atento veria os dois números brigando no mesmo post.

Provável causa: o extrato da referência é do banco local e a própria referência avisa que não é
número de produção. **Me diz qual é o de produção** e eu ajusto — é um número em cada arquivo.

---

## Próximo post sugerido (não produzido)

O **ângulo de bastidor** do brief não cabe num anúncio de 19s e é forte demais pra perder: a grade
3×3 foi apagada porque tom e conectividade são estatisticamente independentes — as 9 células eram o
produto das 3+3 marginais, com desvio de 0,05 ponto percentual. *Deletamos uma feature porque o dado
disse que ela era redundante.* Isso é carrossel orgânico, não anúncio: vende rigor melhor que
qualquer adjetivo, mas precisa de espaço pra explicar.

## Como regerar

```
node instagram/build-board01.mjs             # PT — mockups + cenas + MP4 + capa
node instagram/build-board01.mjs --en        # EN
node instagram/build-board01.mjs --guides    # só renderiza, com zonas seguras
node instagram/build-board01.mjs --nomock    # reaproveita os mockups (itera só a copy)
node instagram/build-board01.mjs --mock      # só os 16 mockups
```
Cenas: `deck.js` (`bf-s1`…`bf-cta` e `bf-s1-en`…`bf-cta-en`).
