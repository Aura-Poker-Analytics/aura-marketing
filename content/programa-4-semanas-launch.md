# Programa de posts — 4 primeiras semanas (Launch Aura 2.0)

**Owner:** Rafael (aprova e publica tudo) · **Autor:** Fábrica de posts · **Início:** L = 08/07/2026
**Status:** proposta completa para autenticação. Nenhum post é publicado por agente — você publica/agenda.

**⚠️ Realinhado em 09/07 (2ª vez).** No dia do launch (08/07), o Rafael publicou **P2** (carrossel
"Meet Aura 2.0") em vez de **P1** (hero reveal) — inversão de ordem, sem prejuízo real (P2 já cobre o
essencial da mensagem de lançamento). Efeito prático: **P1 não vai mais pro feed** — publicar como
**Story hoje** (reforço "estamos no ar" pra quem não viu, sem competir/repetir o carrossel de ontem no
feed). O slot de feed de hoje passa a ser **P3**, e P4–P13 deslizam **-2 dias** para preencher o espaço.

Segue a pegada visual v2 (arco da aura, naipes, logos oficiais, mocks fiéis da UI). Todos os criativos já
renderizados em `instagram/output/` (caminhos por post abaixo). Editáveis via `instagram/templates/` +
`instagram/templates/deck.js` (cada post tem um `id` de deck; render = `template?p=<id>`).

---

## 0. Vale já sair com conteúdo em inglês? — recomendação

**Sim para a ARTE, não para a conta virar EN-only.** É o que o plano macro já decidiu e o que estes
criativos fazem:

- **Arte em EN** desde o D0. O vocabulário de poker é inglês nativo (BTN, c-bet, MDF, RFI) — o BR lê sem
  ruído, e não trava o alcance EN quando ele vier. Reescrever arte depois é caro; nascer bilíngue é grátis.
- **Legenda PT-BR primária + versão EN condensada** em cada post (formato abaixo). A base é 100% BR (710
  users) e o Meta distribui por geografia da base — então o texto que converte agora é PT, mas o EN já
  planta a semente e serve os poucos EN que chegam.
- **Não criar @ EN separada agora.** Regra de revisão do plano: só se em ~90 dias a audiência EN < 15% E EN
  virar prioridade comercial. Separar depois é barato; fundir é impossível.

Ou seja: **arte EN + legenda bilíngue PT-first**. É o melhor dos dois mundos e é o que está montado aqui.

---

## 1. Convenções

**Formato de legenda (todo post):**
```
[gancho PT-BR, 1 linha]

[corpo PT-BR, 2–4 linhas: o que a Aura faz + por que importa]

[CTA PT-BR]

—— EN ——
[versão condensada em inglês, 2–3 linhas + CTA]

[hashtags]
[18+ · jogo de habilidade/estudo]
```

**⚠️ Números nos criativos = ILUSTRATIVOS (mock da UI).** Estes posts mostram a *interface* da Aura com
dados de exemplo — não são stats puxados do banco. Por isso as legendas falam do **que o produto faz**
("veja como o field defende"), nunca afirmam um número como fato verificado. Posts de stat real (pilar P1,
"o pool folda X%") só saem depois dos números de solver/banco, com fonte na hora — não estão neste lote.

**Conjuntos de hashtags** (rotacionar; usar ~8–12 por post, nunca marca de concorrente):
- **Set A — global/EN:** `#poker #mtt #pokerstrategy #tournamentpoker #pokertraining #onlinepoker #pokertips #gtostrategy #pokerlife #cardplayer`
- **Set B — BR/nicho:** `#pokerbrasil #pokeronline #torneiodepoker #estudodepoker #pokerbr #mttpoker #jogadordepoker #pokercoaching #pokermindset #maisqueumjogo`

**CTA padrão:** na **arte** é EN ("Create free account", pra bater com a arte 100% EN); na **legenda** é PT-BR
("Crie sua conta grátis — link na bio"), onde a conversão da base BR acontece. EN condensado na legenda:
"Create your free account — link in bio".

---

## 2. Calendário (visão geral)

| # | Data | Semana | Pilar | Formato | Criativo (deck id) | Render |
|---|---|---|---|---|---|---|
| P1 | **Story hoje (09/07)** — não vai mais pro feed | 1 | L1 Reveal | Story | `w1-hero` | [story](../instagram/output/programa-4-semanas/semana-1/w1-p1-hero-story.png) |
| P2 | ✅ **publicado 08/07** (fora de ordem — serviu de post de launch) | 1 | L2 Module tour | Carrossel 5 | `meet-*` | [2026-07-10-carrossel-lancamento/](../instagram/output/2026-07-10-carrossel-lancamento/) |
| P3 | **09/07 (HOJE · feed)** | 1 | L4 Feature | Card | `w1-spot-hotspot` | [semana-1/w1-p3-spot-hotspot.png](../instagram/output/programa-4-semanas/semana-1/w1-p3-spot-hotspot.png) |
| P4 | 11/07 | 1 | L4 Feature | Card | `w1-spot-postflop` | [semana-1/w1-p4-spot-postflop.png](../instagram/output/programa-4-semanas/semana-1/w1-p4-spot-postflop.png) |
| P5 | 13/07 | 2 | L2 Module tour | Carrossel 4 | `w2-pre-*` | [semana-2/](../instagram/output/programa-4-semanas/semana-2/) |
| P6 | 16/07 | 2 | L3 Pergunta | Card | `w2-l3-defend` | [semana-2/w2-p6-l3-defend.png](../instagram/output/programa-4-semanas/semana-2/w2-p6-l3-defend.png) |
| P7 | 18/07 | 2 | L4 Feature/filtro | Card | `w2-spot-stage` | [semana-2/w2-p7-spot-stage.png](../instagram/output/programa-4-semanas/semana-2/w2-p7-spot-stage.png) |
| P8 | 20/07 | 3 | L2 Module tour | Carrossel 4 | `w3-post-*` | [semana-3/](../instagram/output/programa-4-semanas/semana-3/) |
| P9 | 23/07 | 3 | L3 Pergunta | Card | `w3-l3-rfi` | [semana-3/w3-p9-l3-rfi.png](../instagram/output/programa-4-semanas/semana-3/w3-p9-l3-rfi.png) |
| P10 | 25/07 | 3 | L5 CTA | Card | `meet-cta` | [semana-3/w3-p10-cta.png](../instagram/output/programa-4-semanas/semana-3/w3-p10-cta.png) |
| P11 | 27/07 | 4 | L2 How-to | Carrossel 4 | `w4-hs-*` | [semana-4/](../instagram/output/programa-4-semanas/semana-4/) |
| P12 | 30/07 | 4 | L4 Feature | Card | `w4-spot-preflop` | [semana-4/w4-p12-spot-preflop.png](../instagram/output/programa-4-semanas/semana-4/w4-p12-spot-preflop.png) |
| P13 | 01/08 | 4 | L5 CTA | Card | `meet-cta` | [semana-3/w3-p10-cta.png](../instagram/output/programa-4-semanas/semana-3/w3-p10-cta.png) |

Ritmo: semana de launch mais densa (4), depois 3/semana (alinhado à "sustentação" do plano). Stories: repostar
cada card no story no dia (o hero tem variante 9:16 pronta).

---

## SEMANA 1 — Launch

### P1 · STORY hoje (09/07) — não vai mais pro feed · L1 Reveal — hero "Now live"
`w1-hero` · **apenas Story** (P2 já cobriu o feed do launch) · [story](../instagram/output/programa-4-semanas/semana-1/w1-p1-hero-story.png) ·
[feed render existe se quiser reaproveitar depois](../instagram/output/programa-4-semanas/semana-1/w1-p1-hero.png)

> **PT-BR**
> A Aura 2.0 está no ar. 🎯
>
> O mesmo jogo — novas informações. A Aura não é tracker nem solver: é inteligência do *field*. A estratégia
> real da população de MTT, medida em 500M+ mãos e filtrada por posição, stack, buy-in e estágio do torneio.
> Solvers te mostram o equilíbrio. A Aura te mostra o adversário.
>
> Crie sua conta grátis — link na bio. Sem cartão.
>
> —— EN ——
> Aura 2.0 is live. Not a tracker, not a solver — field intelligence: the real strategy of the MTT
> population, across 500M+ hands. Create your free account — link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokerbrasil #pokeronline #estudodepoker #pokertraining #maisqueumjogo #pokerlife
> 18+ · poker é jogo de habilidade e estudo

**Compliance:** ✅ sem promessa de lucro ✅ sem dinheiro/luxo ✅ 18+ ✅ sem dado de cliente ✅ sem concorrente nominal · nº: n/a (sem stat).

---

### P2 · ✅ PUBLICADO 08/07 (fora de ordem, serviu de post de launch) · L2 Module tour — CARROSSEL "Meet Aura 2.0" (5 slides)
`meet-capa → meet-preflop → meet-postflop → meet-hotspot → meet-cta` · [pasta](../instagram/output/2026-07-10-carrossel-lancamento/)

Slides: 01 capa "Meet Aura 2.0" · 02 Preflop (mesa+tabela) · 03 Postflop (ações+reações+MDF) · 04 Hotspot (leak card) · 05 CTA grátis.

> **PT-BR**
> Conheça a Aura 2.0 por dentro. 👉 arrasta.
>
> Três módulos, uma ideia: te mostrar o que a população de MTT REALMENTE faz — não o que o solver diz.
> • Preflop: como o field abre, dá 3-bet e defende por posição e stack.
> • Postflop: a reação do pool a cada linha e sizing, com a linha de MDF na barra.
> • Hotspot: os leaks exploráveis do field, ranqueados pra você.
> Tudo começa no plano grátis.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> Meet Aura 2.0. Three modules, one idea: what the MTT field actually does, not what the solver says.
> Preflop, Postflop, Hotspot — start free. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokertraining #pokerbrasil #pokeronline #estudodepoker #mttpoker #pokertips
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · números nos slides = **ilustrativos (mock de UI)**; legenda não afirma stat.

---

### P3 · 09/07 · HOJE (feed) · L4 Feature — Hotspot spotlight
`w1-spot-hotspot` · [render](../instagram/output/programa-4-semanas/semana-1/w1-p3-spot-hotspot.png)

> **PT-BR**
> Os leaks do field, ranqueados. 🔥
>
> O módulo Hotspot varre o field e te entrega os spots onde a população é mais explorável — com a defesa do
> pool contra o MDF na mesma barra. Você vê na hora onde o field folda demais e onde dá pra atacar. Incluído no
> plano grátis.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> The field's leaks, ranked. Hotspot surfaces the pool's most exploitable spots — pool defense vs MDF on one bar.
> Included in the free plan. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #estudodepoker #pokerbrasil #pokeronline #pokercoaching #mttpoker #pokermindset
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI).

---

### P4 · 11/07 · L4 Feature — Postflop spotlight
`w1-spot-postflop` · [render](../instagram/output/programa-4-semanas/semana-1/w1-p4-spot-postflop.png)

> **PT-BR**
> Leia o pool, street a street. ♠️
>
> No Postflop você escolhe o spot e o sizing, e a Aura mostra a reação do field — fold, call, raise — com a
> linha de MDF na barra pra você enxergar over/under-defesa na hora. Dá pra filtrar por limite, posição e
> estágio do torneio.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> Read the pool, street by street. Pick spot + sizing; see the field's fold/call/raise with MDF on the bar.
> Filter by stake, position, stage. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokertraining #pokerbrasil #pokeronline #estudodepoker #mttpoker #pokertips
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI).

---

## SEMANA 2

### P5 · 13/07 · L2 — CARROSSEL "Preflop in 60s" (4 slides)
`w2-pre-capa → w2-pre-slide1 → w2-pre-slide2 → w2-pre-cta` · [pasta](../instagram/output/programa-4-semanas/semana-2/)

> **PT-BR**
> O field abre demais. Em 60 segundos, veja onde. 👉
>
> O módulo Preflop mostra como a população abre, dá 3-bet e defende — com os deltas (mais largo/mais tight que
> a referência) em verde e vermelho. É a sua primeira leitura antes do flop, e você filtra por stack e estágio.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> The field opens too much — see where, in 60s. Preflop shows how the pool opens/3-bets/defends, with deltas
> vs reference. Filter by stack & stage. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #estudodepoker #pokerbrasil #pokeronline #mttpoker #pokercoaching #pokertips
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI).

---

### P6 · 16/07 · L3 Pergunta — "Quanto o BB realmente defende?"
`w2-l3-defend` · [render](../instagram/output/programa-4-semanas/semana-2/w2-p6-l3-defend.png)

> **PT-BR**
> Quanto o BB REALMENTE defende contra um c-bet? 🤔
>
> O solver te dá o número do equilíbrio. A Aura te dá o número do *field* — e eles não são iguais. Quando a
> defesa do pool fica abaixo da linha de MDF, essa diferença é o seu exploit. Confira qualquer spot no Hotspot,
> de graça.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> How much does the BB really defend vs a c-bet? The solver gives you equilibrium; Aura gives you the field —
> and the gap is your exploit. Check any spot in Hotspot, free. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #estudodepoker #pokerbrasil #pokeronline #mttpoker #pokermindset #pokertips
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI) · sem concorrente nominal ("solvers", genérico).

---

### P7 · 18/07 · L4 Feature/filtro — Estágio de torneio
`w2-spot-stage` · [render](../instagram/output/programa-4-semanas/semana-2/w2-p7-spot-stage.png)

> **PT-BR**
> O field da bolha é outro animal. 🫧
>
> A Aura separa por estágio do torneio — early, pré-bolha, bolha, ITM, mesa final. Sob pressão de ICM a
> população superfolda de um jeito que nenhum solver modela, porque solver dá a resposta ICM-perfeita, não o
> que o field faz. Achado 100% MTT.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> The bubble field is a different animal. Aura splits by tournament stage — where ICM pressure makes the pool
> over-fold in ways no solver models. Pure MTT edge. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #icmpoker #pokerbrasil #pokeronline #estudodepoker #mttpoker #pokercoaching
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI).

---

## SEMANA 3

### P8 · 20/07 · L2 — CARROSSEL "Postflop — read the pool" (4 slides)
`w3-post-capa → w3-post-slide1 → w3-post-slide2 → w3-post-cta` · [pasta](../instagram/output/programa-4-semanas/semana-3/)

> **PT-BR**
> Leia o pool, não o solver. 👉
>
> No Postflop cada sizing conta: 33%, 66%, overbet — o field reage diferente a cada um, e a Aura separa a
> resposta do pool por tamanho. Quando a barra de defesa fica aquém da marca de MDF, aquele gap é o seu
> exploit, visível num relance.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> Read the pool, not the solver. Postflop splits the field's response by every sizing you use — and when the
> defense bar falls short of MDF, that gap is your exploit. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokertraining #pokerbrasil #pokeronline #estudodepoker #mttpoker #pokertips
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI).

---

### P9 · 23/07 · L3 Pergunta — "Seu pool abre demais o CO?"
`w3-l3-rfi` · [render](../instagram/output/programa-4-semanas/semana-3/w3-p9-l3-rfi.png)

> **PT-BR**
> Seu pool abre demais no CO? 📈
>
> Abrir mais largo que a referência não é aleatório — o field tem uma forma que você consegue ler. Onde ele
> abre demais E folda demais depois, dá pra dar 3-bet mais leve e explorar. O grid de Preflop mostra isso de
> graça.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> Does your pool over-open the CO? Wider than reference isn't random — it's a shape you can read. 3-bet lighter
> where it over-opens and over-folds. Preflop grid, free. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #estudodepoker #pokerbrasil #pokeronline #mttpoker #pokercoaching #pokermindset
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI).

---

### P10 · 25/07 · L5 CTA — "Study the field. Free."
`meet-cta` · [render](../instagram/output/programa-4-semanas/semana-3/w3-p10-cta.png)

> **PT-BR**
> Estude o field. De graça. ♠️
>
> Plano grátis pra sempre, sem cartão. Hotspot (leaks ranqueados) + Preflop inclusos, sobre 500M+ mãos
> reais de MTT. O upgrade acontece dentro do produto, quando você quiser mais profundidade.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> Study the field. Free. Forever free plan, no card — Hotspot + Preflop included, over 500M+ real MTT
> hands. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokerbrasil #pokeronline #estudodepoker #mttpoker #pokertips #maisqueumjogo
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · sem stat.

---

## SEMANA 4

### P11 · 27/07 · L2 How-to — CARROSSEL "From leak to line" (4 slides)
`w4-hs-capa → w4-hs-slide1 → w4-hs-slide2 → w4-hs-cta` · [pasta](../instagram/output/programa-4-semanas/semana-4/)

> **PT-BR**
> De leak a linha: como usar um exploit card. 👉
>
> 1) Leia a carta: a barra de defesa do pool aquém da marca de MDF = o field folda demais ali. 2) Tome a
> linha: contra um field que superfolda, um c-bet pequeno lucra. A carta te diz onde; você traz a agressão.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> From leak to line: how to use an exploit card. Read the card (defense below MDF = the field over-folds),
> then take the line (small c-bet prints vs an over-folding field). Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokertraining #pokerbrasil #pokeronline #estudodepoker #mttpoker #pokercoaching
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI).

---

### P12 · 30/07 · L4 Feature — Preflop grid
`w4-spot-preflop` · [render](../instagram/output/programa-4-semanas/semana-4/w4-p12-spot-preflop.png)

> **PT-BR**
> O field inteiro, numa tela. 🗺️
>
> RFI, 3-bet e defesa por posição — com os deltas (mais largo/mais tight que a referência) já embutidos e
> coloridos. É a leitura de preflop da população em um lugar só. Incluído no plano grátis.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> The whole field, one screen. RFI, 3-bet and defense by position, with deltas vs reference built in and
> color-coded. Free tier. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #estudodepoker #pokerbrasil #pokeronline #mttpoker #pokertips #pokercoaching
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI).

---

### P13 · 01/08 · L5 CTA — reforço grátis (fim do mês)
`meet-cta` (mesmo criativo de P10) · [render](../instagram/output/programa-4-semanas/semana-3/w3-p10-cta.png)

> **PT-BR**
> Um mês de Aura 2.0. Já criou a sua conta? ♠️
>
> Plano grátis pra sempre, sem cartão — Hotspot + Preflop sobre 500M+ mãos reais de MTT. Se você ainda tá
> decorando o equilíbrio em vez de explorar o field, tá deixando dinheiro na mesa.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> One month of Aura 2.0 — created your account yet? Forever free plan, no card. Stop memorizing equilibrium
> and start exploiting the field. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokerbrasil #pokeronline #estudodepoker #mttpoker #pokermindset #maisqueumjogo
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · sem stat.

---

## 3. Pendências / notas para você

- **Prints reais:** todos os mocks aceitam `screenshotSrc` no deck — quando você me passar screenshots reais do
  beta (dark, sem dado de cliente), eu troco os mocks por telas de verdade sem mexer no layout.
- **Números ilustrativos:** nenhum post afirma stat como fato. Quando os números de solver/banco entrarem, abro
  a linha P1 de stat cards reais (com fonte na hora) — não estão neste lote de propósito.
- **Ordem/datas** são sugestão; realoco fácil. Se quiser mais/menos posts por semana, eu ajusto o deck e re-renderizo.
- **Autenticação:** me diga "aprovado" (ou aponte ajustes por post/id) e o lote está pronto pra você agendar no
  Meta Business Suite. Eu nunca publico.
