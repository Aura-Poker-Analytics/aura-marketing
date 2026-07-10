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
| P13 | 01/08 | 4 | L5 CTA | Card | `w4-cta-month` | [semana-4/w4-p13-cta-month.png](../instagram/output/programa-4-semanas/semana-4/w4-p13-cta-month.png) *(pendente render)* |

Ritmo: semana de launch mais densa (4), depois 3/semana (alinhado à "sustentação" do plano). Stories: repostar
cada card no story no dia (o hero tem variante 9:16 pronta).

---

## SEMANA 1 — Launch

### P1 · STORY hoje (09/07) — não vai mais pro feed · L1 Reveal — hero "Now live"
`w1-hero` · **apenas Story** (P2 já cobriu o feed do launch) · [story](../instagram/output/programa-4-semanas/semana-1/w1-p1-hero-story.png) ·
[feed render existe se quiser reaproveitar depois](../instagram/output/programa-4-semanas/semana-1/w1-p1-hero.png)

> **PT-BR**
> A Aura 2.0 tá no ar. E ela não é tracker nem solver. ♠️
>
> Solver te mostra o equilíbrio teórico. Tracker te mostra as SUAS mãos. A Aura te mostra o que o field de
> MTT realmente faz — a estratégia da população inteira, medida em 500M+ mãos auditadas de 7 salas.
>
> São 3 módulos:
> • Preflop — como o field abre, dá 3-bet e defende, por posição e stack
> • Postflop — a reação do pool a cada sizing e street, com o MDF na barra
> • Hotspot — os leaks do field ranqueados, do mais explorável pro menos
>
> Fatie qualquer spot por 20+ filtros (buy-in, estágio, textura de board, tipo de vilão…). O módulo Hotspot
> inteiro é grátis, sem cartão.
>
> Para de decorar o equilíbrio. Começa a explorar o field. 👉 Conta grátis no link da bio.
>
> —— EN ——
> Aura 2.0 is live — not a tracker, not a solver. Field intelligence: what the MTT population actually does,
> across 500M+ audited hands from 7 sites. Three modules — Preflop, Postflop, Hotspot — sliceable by 20+
> filters. The full Hotspot module is free, no card. Stop memorizing equilibrium; start exploiting the field.
> Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokerbrasil #pokeronline #estudodepoker #pokertraining #mttpoker #pokerlife
> 18+ · poker é jogo de habilidade e estudo

**Compliance:** ✅ sem promessa de lucro ✅ sem dinheiro/luxo ✅ 18+ ✅ sem dado de cliente ✅ sem concorrente nominal · nº: n/a (sem stat).

---

### P2 · ✅ PUBLICADO 08/07 (fora de ordem, serviu de post de launch) · L2 Module tour — CARROSSEL "Meet Aura 2.0" (5 slides)
`meet-capa → meet-preflop → meet-postflop → meet-hotspot → meet-cta` · [pasta](../instagram/output/2026-07-10-carrossel-lancamento/)

**⚠️ Reescrito em 09/07 (correção pós-publicação):** slide 02 (Preflop) estava subvendendo o módulo — só
citava 3 ações (RFI/3-bet/defesa) e 2 dimensões (posição/stack), quando o produto cobre RFI, 3-bet, 4-bet,
squeeze, cold call e a família steal, por posição, stack, buy-in, estágio, formato e arquétipo de vilão.
Slide 04 (Hotspot) não gritava o diferenciador real: Hotspot é **completo e grátis, sem trava de filtros**
— o ativo de oferta mais forte do produto. Slide 05 (CTA) tinha gating errado ("Hotspot + Preflop
included", implicando os dois completos e grátis) — corrigido para Hotspot completo grátis + Preflop/
Postflop como amostra grátis, com "500M+ audited" no lugar de "500M+ real MTT hands". Fonte de verdade:
`instagram/templates/deck.js` (chaves `meet-*`), já atualizado.

Slides: 01 capa "Meet Aura 2.0" · 02 Preflop (mesa+tabela, leque completo de ações/dimensões) · 03 Postflop
(bet/check/raise/fold por street, IP vs OOP, MDF) · 04 Hotspot (leak card, "completo e grátis, sem trava de
filtro") · 05 CTA (gating correto: Hotspot completo grátis + Preflop/Postflop amostra grátis).

> **PT-BR**
> Conheça a Aura 2.0 por dentro. 👉 arrasta.
>
> Três módulos, uma ideia: o que a população de MTT REALMENTE faz, medido em 500M+ mãos auditadas — não o
> que o solver diz.
> • Preflop: RFI, 3-bet, 4-bet, squeeze, cold call e steal — por posição, stack, buy-in, estágio e tipo de
> torneio.
> • Postflop: bet, check, raise e fold do pool, street a street (flop/turn/river), com a linha de MDF na
> barra.
> • Hotspot: TODOS os leaks do field, sem trava de filtro — 100% grátis, sempre.
>
> Hotspot completo e grátis pra sempre. Preflop e Postflop têm amostra grátis pra começar.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> Meet Aura 2.0. Three modules, one idea: what the MTT field actually does — not what the solver says.
> Full Hotspot, free forever, zero filter lock. Preflop + Postflop, free sample to start. 500M+ audited
> hands. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokertraining #pokerbrasil #estudodepoker #mttpoker #pokercoaching #pokermindset
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ sem promessa de lucro ✅ sem dinheiro/luxo ✅ 18+ ✅ sem dado de cliente ✅ sem concorrente
nominal · números nos slides = **ilustrativos (mock de UI)**; legenda não afirma stat de banco. Gating
corrigido conforme verdade canônica: Hotspot completo e grátis (regra oficial do dono); Preflop/Postflop =
amostra grátis (buy-in ≤$22, Vanilla, Early Game), não "included".

---

### P3 · 09/07 · HOJE (feed) · L4 Feature — Hotspot spotlight
`w1-spot-hotspot` · [render](../instagram/output/programa-4-semanas/semana-1/w1-p3-spot-hotspot.png)

> **PT-BR**
> Hotspot: completo e grátis. Sem trava, sem pegadinha. 🔥
>
> O módulo Hotspot varre o field inteiro e ranqueia os spots mais exploráveis por street (flop/turn/river).
> Cada card mostra a defesa real do pool vs o MDF, o desvio em pontos e um selo de confiança pelo tamanho da
> amostra — e ainda dá pra recortar por posição e textura de board sem sair da tela. Diferente do Preflop e
> do Postflop, aqui não tem amostra limitada: o módulo Hotspot é seu inteiro, sem trava de filtro, no plano
> grátis.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> Hotspot: full and free, no lock. It scans the whole field and ranks the pool's most exploitable spots by
> street, with real defense vs MDF, deviation in points, and a sample-size confidence badge on every card —
> plus drill-down by position and board texture. The entire module is free, no filter lock. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokertraining #pokerbrasil #pokeronline #estudodepoker #mttpoker #cardplayer
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ tudo ok · nº ilustrativo (mock de UI) · reforça claim aprovada "Hotspot completo e grátis,
sem trava de filtros" (verdade canônica §2/§9). ⚠️ Ver pendência operacional abaixo antes de publicar.

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
> O range do pool não é segredo. Em 60 segundos, veja como ele realmente joga. 👉
>
> O módulo Preflop cobre RFI, 3-bet, 4-bet, squeeze e steal — por posição, stack, buy-in, estágio do torneio
> (do early ao mesa final) e formato (Vanilla, KO, Mystery Bounty). Cruza tudo com o arquétipo de quem age:
> reg agressivo, reg tight ou fish.
>
> Amostra grátis pra sempre: buy-in até $22, Vanilla, Early Game. Já o Hotspot é completo e grátis, sem
> trava de filtro nenhuma.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> The pool's range isn't a secret. Preflop covers RFI, 3-bet, 4-bet, squeeze & steal — by position, stack,
> buy-in, tournament stage (early to final table) and format (Vanilla/KO/Mystery), crossed with reg vs fish.
> Free sample: ≤$22 buy-in, Vanilla, Early Game. Hotspot? Full & free, no filter lock. Link in bio.
>
> Set A: #poker #mtt #mttpoker #pokerstrategy #tournamentpoker #pokerbrasil #pokeronline #estudodepoker #pokertips #pokertraining
> Set B (rotação): #poker #mtt #mttpoker #pokerstrategy #pokerranges #icmpoker #pokerbrasil #estudodepoker #pokercoaching #tournamentpoker
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ hook trocado (era vago: "field opens too much"); CTA corrigida — deixa claro que é amostra
grátis (buy-in ≤$22, Vanilla, Early Game) e que o Hotspot é o item completo e grátis; puxa estágio/ICM,
formato de torneio e arquétipo de vilão como diferenciadores · nº ilustrativo (mock de UI) · sem concorrente nominal.

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
`meet-cta` (criativo corrigido — Hotspot é o módulo completo/grátis; Preflop citado só como amostra) ·
[render](../instagram/output/programa-4-semanas/semana-3/w3-p10-cta.png) *(pendente re-render)*

> **PT-BR**
> Estude o field. De graça — sem letra miúda. ♠️
>
> Plano grátis pra sempre, sem cartão. O Hotspot Analysis vem completo nesse plano: os leaks mais
> exploráveis do pool, por street, sem trava de filtro — sobre 500M+ mãos reais e auditadas de MTT.
> Preflop e Postflop entram com amostra grátis pra você sentir o produto; a profundidade total (todos
> os buy-ins, formatos e estágios) fica no plano pago, quando você quiser.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> Study the field. Free — no fine print. Forever-free plan, no card. Hotspot Analysis is complete in
> it: every exploitable leak, by street, no filter lock, across 500M+ audited MTT hands. Preflop and
> Postflop start free-to-sample; full depth unlocks on the paid plan. Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #pokerbrasil #pokeronline #estudodepoker #mttpoker #pokertips #maisqueumjogo
> 18+ · jogo de habilidade/estudo
>
> **Set B (rotação — repost/story):** #poker #mtt #pokerstrategy #tournamentpoker #pokertraining #pokerbrasil #pokeronline #estudodepoker #pokermindset #mttpoker

**Compliance:** ✅ corrigido 09/07 — a versão anterior dizia "Hotspot + Preflop included", o que implicava
acesso completo ao Preflop no grátis (banido — Preflop grátis é só amostra: buy-in ≤$22, Vanilla, Early
Game). Agora a arte (`meet-cta`) cita só o Hotspot como módulo 100% completo/grátis nos bullets; a legenda
menciona Preflop/Postflop como "amostra grátis" explicitamente. "500M+ mãos reais e auditadas" (não
"bilhões"). Sem promessa de lucro, sem dinheiro/luxo, sem concorrente nominal, 18+. Caption distinta de
P13 (gancho e estrutura diferentes; P13 tem criativo `w4-cta-month` próprio). Nº ilustrativo: n/a (arte
sem stat solto).

---

## SEMANA 4

### P11 · 27/07 · L2 How-to — CARROSSEL "From leak to line" (4 slides)
`w4-hs-capa → w4-hs-slide1 → w4-hs-slide2 → w4-hs-cta` · [pasta](../instagram/output/programa-4-semanas/semana-4/)

> **PT-BR**
> De leak a linha: como usar um exploit card. 👉
>
> 1) Leia a carta: a barra de defesa do pool aquém da marca de MDF = o field folda demais ali. 2) Tome a
> linha: contra um field que superfolda, um c-bet pequeno e frequente ataca esse gap. A carta te diz onde;
> você traz a agressão.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> From leak to line: how to use an exploit card. Read the card (defense below MDF = the field over-folds),
> then attack that gap with a small, frequent c-bet. Link in bio.
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
> RFI, 3-bet e defesa por posição, com os deltas (mais largo/mais tight que a referência) já embutidos e
> coloridos — e mais de 20 filtros combináveis: posição, stack, buy-in, estágio do torneio, formato
> (Vanilla/KO/Mystery Bounty) e até o arquétipo do vilão (reg agressivo, reg tight, fish).
>
> Amostra grátis para sempre: buy-in até $22, torneios Vanilla, fase Early Game. O range completo (todos os
> buy-ins, formatos e estágios) é do plano pago — mas o Hotspot Analysis já vem completo e grátis, sem trava
> de filtro nenhuma.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> The whole field, one screen. RFI, 3-bet and defense by position, deltas built in, plus 20+ stackable
> filters — position, stack, buy-in, stage, format, villain type.
>
> Free sample up to $22 buy-in, Vanilla, Early Game; full range is paid. Hotspot Analysis stays fully free,
> no filter caps.
>
> Link in bio.
>
> #poker #mtt #pokerstrategy #tournamentpoker #estudodepoker #pokerbrasil #pokeronline #mttpoker #pokertips #pokercoaching
> 18+ · jogo de habilidade/estudo
>
> **Set B (rotação — repost/story):** #poker #mtt #pokertraining #onlinepoker #cardplayer #torneiodepoker #pokerbr #jogadordepoker #pokermindset #maisqueumjogo

**Compliance:** ✅ corrigido 09/07 — antes underselava (sem citar os 20+ filtros) e a linha "Incluído no plano
grátis" implicava acesso completo ao Preflop no grátis. Agora: menciona os 20+ filtros combináveis e deixa
explícito que o Preflop grátis é **amostra** (buy-in ≤$22, Vanilla, Early Game — resto é pago), com o Hotspot
citado como o módulo que É completo e grátis. Nº ilustrativo (mock de UI). Sem concorrente nominal, sem
promessa de lucro.

---

### P13 · 01/08 · L5 CTA — "1 mês de Aura 2.0 no ar" (criativo novo, distinto de P10)
`w4-cta-month` (criativo próprio — **não** reaproveita `meet-cta` de P10) · [render](../instagram/output/programa-4-semanas/semana-4/w4-p13-cta-month.png) *(pendente gerar — deck já configurado)*

> **PT-BR**
> Um mês de Aura 2.0 no ar. ♠️
>
> Hotspot completo e grátis pra sempre — os leaks mais fortes do field, por street, sem trava de filtro.
> Preflop e Postflop têm amostra grátis pra sempre (buy-in até $22, torneios Vanilla, fase Early Game); o
> resto do field é liberado no plano pago. Tudo sobre 500M+ mãos reais e auditadas de MTT, em 7 salas
> cobertas. Se ainda não criou sua conta, esse mês inteiro já tinha field pra explorar.
>
> Crie sua conta grátis — link na bio.
>
> —— EN ——
> One month of Aura 2.0, live. Hotspot: full leak board, free forever. Preflop + Postflop: free sample to
> start (buy-in ≤$22, Vanilla, Early Game) — full field on the paid plan. 500M+ audited hands, 7 rooms
> covered. Link in bio.
>
> #poker #mtt #tournamentpoker #pokertraining #gtostrategy #pokerbrasil #pokeronline #estudodepoker #mttpoker #pokermindset
> 18+ · jogo de habilidade/estudo

**Compliance:** ✅ sem promessa de lucro (removida a linha "deixando dinheiro na mesa" da v. anterior — reframe
para "field pra explorar") ✅ gating correto (Hotspot completo/grátis · Preflop+Postflop = amostra grátis, não
"incluído" de graça inteiro) ✅ "500M+ auditadas" (não "bilhões") ✅ sem dinheiro/luxo ✅ 18+ ✅ sem dado de
cliente ✅ sem concorrente nominal · nº: n/a (sem stat solto, só claims aprovadas).

---

## 3. Pendências / notas para você

- **Prints reais:** todos os mocks aceitam `screenshotSrc` no deck — quando você me passar screenshots reais do
  beta (dark, sem dado de cliente), eu troco os mocks por telas de verdade sem mexer no layout.
- **Números ilustrativos:** nenhum post afirma stat como fato. Quando os números de solver/banco entrarem, abro
  a linha P1 de stat cards reais (com fonte na hora) — não estão neste lote de propósito.
- **Ordem/datas** são sugestão; realoco fácil. Se quiser mais/menos posts por semana, eu ajusto o deck e re-renderizo.
- **Autenticação:** me diga "aprovado" (ou aponte ajustes por post/id) e o lote está pronto pra você agendar no
  Meta Business Suite. Eu nunca publico.
- **⚠️ Pendência operacional — Hotspot "completo e grátis, sem trava":** P3 e P12 agora afirmam isso na legenda
  (aprovado pelo dono, é LEI de marketing). Mas em 09/07 o código em produção (`entitlements.ts`, commit
  2026-07-06) e a landing (`pricing.ts`, commit 2026-07-07) ainda mostravam um Hotspot "teased" — 2 exploit
  cards por bucket no grátis + filtros de buy-in/formato/estágio travados. Antes de publicar P3, confirme
  que engenharia já ajustou `getModuleAccess('hotspot')`/`HOTSPOT_FREE_VISIBLE_LIMIT` para refletir "full",
  ou reconfirme a regra olhando o produto ao vivo — senão a legenda promete algo que o app ainda não entrega.
