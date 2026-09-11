# board01-1560-boards · Anúncio — seleção de board no Postflop (EN)

**Campanha:** AURA-BOARD01 · **`utm_content`:** `board01-1560-boards-en`
**Entrega:** `content/paid/AURA-BOARD01/board01-1560-boards-en.mp4` — 9:16 · **24,20s** · 6,2 MB · sem áudio · + capa 1080×1920
**Status:** EN renderizado e pronto pra postar. **PT ainda não feito** (falta criar as cenas `bd-*` sem sufixo no deck).

Substitui `board01-amostra-antes`, recusado — aquele vendia **mecanismo** ("veja as classes
colapsando") em vez de **promessa**. Os arquivos do recusado foram para
`content/paid/AURA-BOARD01/_recusado/` pra não serem postados por engano.

---

## A promessa

**Escolha o board, receba a análise dele.** Uma promessa só, executada inteira (Ogilvy).
O empilhamento vira *um* beat de três cliques; o payoff é a tela de resultado.

**Mnemônico da campanha: 1.560 boards.**

| street | buckets pesquisáveis |
|---|---|
| flop | 73 |
| turn | 615 |
| river | 872 |
| **total** | **1.560** |

Contados no extrato da referência de interação (combinações de atributos presentes nos dados).

## Cenas (corte seco)

| # | dur | Conteúdo |
|---|---|---|
| 1 | 3,4s | **GANCHO** — logo · `Postflop · Aura` · **"1,560 boards. Pick yours."** |
| 2 | 4,0s | `How many boards you can query` · *"73 on the flop · 615 on the turn · 872 on the river."* · painel de seleção aberto |
| 3 | 4,4s | `Three clicks` · *"Two-tone. OESD possible. Ace high."* · painel com os três chips ligados (3.80% · 1 classe) |
| 4 | 4,4s | `Analyze` · *"Which size the field actually used."* · **painel de resultado — Size distribution** · push-in lento |
| 5 | 4,4s | `And how it defended` · *"Real defense against MDF, size by size."* · **painel de resultado — Exploitative Sizes** |
| 6 | 3,6s | **CTA** — *You build the scenario you want to analyze* · `Free to start` · No card · aurapoker.com |

9:16 1080×1920 · sem áudio · selo `500M+ audited hands · 7 rooms` em todas as cenas · 18+ em todo
quadro · zonas seguras conferidas com `--guides` antes do encode (a cena 4 é a de painel mais alto e
foi verificada em recorte no tamanho real).

**O painel de resultado sai em duas cenas** (`?part=sizes` e `?part=expl`). Inteiro ele tem 1.180px
de altura e não cabe na zona segura sem encolher o texto até borrar — justamente na cena onde o
anúncio precisa ser lido. Dividido, cada seção ganha uma legenda própria e dois beats de payoff.

---

## Mockups

Ambos **recriados** em HTML/CSS, não são capturas.

| arquivo | o quê |
|---|---|
| `mockup-board-facets.html` | superfície de seleção · `?step=1` aberto, `?step=5` = o board definido |
| `mockup-board-results.html` | a análise que volta · `?part=sizes` / `?part=expl` |

**Painéis em inglês nos dois idiomas.** A UI do produto é em inglês, então o mesmo asset serve ao
anúncio PT e ao EN — mesma decisão do DISC03. Só o texto do anúncio troca de idioma.

**As porcentagens do painel de seleção não foram inventadas:** a distribuição medida está embutida e
cada chip é recalculado com a matemática do produto (massa de um nível condicionada aos outros
atributos já ligados). É por isso que `Paired` aparece riscado em 0,00% quando Monotone entra — não
existe linha pareado+monotone nos dados.

---

## ⚠️ A cena 4/5 não afirma "nesse board" — e o motivo importa

Os números do painel de resultado são **reais**, transcritos de `shots/postflop-ref.png`, que é
output do produto. Mas o contexto daquele print é `SRP · RFI: CO · Caller: BB · Last 2 Years`,
**sem filtro de board**.

Então:
- o rail de **Active Context** do mockup **não** declara filtro de board (`BOARD_FILTER = false`);
- as legendas das cenas 4 e 5 descrevem **o que volta** ("which size the field actually used",
  "real defense against MDF"), e **não** de que recorte.

Colar "on that board" em cima desses números seria número de um recorte com rótulo de outro.

**Para fechar isso:** o output real de um bucket filtrado — sugestão `SRP · RFI: CO · Caller: BB ·
Two-tone + OESD possible + Ace high`, com o % da ação, a size distribution e os Exploitative Sizes.
Chegando, viram dois arrays em `mockup-board-results.html`, `BOARD_FILTER = true`, e as legendas
passam a poder afirmar o recorte.

## ⚠️ O `1.560` depende de um número em disputa

O brief da feature diz **64 classes-folha** no flop; o extrato da referência me dá **73** — e é o 73
que entra na soma do 1.560. Se produção for 64, o número da campanha muda (1.551) e o anúncio
precisa de re-render. Mesma pendência do `0,78%` vs `0,75%` recalculado.

## Compliance conferido

- Zero promessa de lucro/EV/winrate · sem tom guru · sem dinheiro/fichas · sem concorrente citado
- `Overfold`, `MDF`, `Exploitative Sizes` são rótulos do próprio produto — o anúncio **mostra** o que
  a tela devolve e **não infere exploit** em cima disso
- grátis = **começar** (preview), nunca "completo grátis" · 18+ em todo quadro
- Vocabulário travado: Desconectado / OESD possível / Conectado — nunca "seco".
  Rainbow / Two-tone / Monotone / Overcard em inglês nos dois idiomas

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
node instagram/build-board1560.mjs --en             # mockups + cenas + MP4 + capa
node instagram/build-board1560.mjs --en --guides    # só renderiza, com zonas seguras
node instagram/build-board1560.mjs --en --nomock    # reaproveita os mockups
```
Cenas: `deck.js` (`bd-s1-en`…`bd-cta-en`).
