# disc-01-solver · Célula 1 — SOLVER

**⚠️ MP4 v2.3 desatualizado — conteúdo mudou na v2.4 (ver abaixo). Precisa re-render** (PT já foi;
EN ainda não). `content/paid/AURA-DESCOBERTA/disc-01-solver.mp4` / `disc-01-solver-en.mp4` são a
v2.3, não refletem a cena 4 nova.
**Campanha:** descoberta (30d) · **Eixo:** persona · **`utm_content`:** `disc-01-solver`
**Base:** adapta `paid01-v2-field` · **Doc:** [matriz-descoberta-4-celulas.md](../../../docs/02-paid/matriz-descoberta-4-celulas.md) §2

## Persona-alvo
**Reg que estuda solver.** Já rodou solver, entende GTO, e sente a distância entre o que
estudou e o que encontra na mesa.
- **Deve parar:** quem já investiu tempo em estudo teórico
- **Deve rolar:** quem nunca abriu um solver — não decodifica GTO
- **Hipótese isolada:** a dor de investimento não-convertido ressoa?

## Alterações v2 (PO, 26/07)
- Dourado do `<em>`: cor **chapada** (`var(--amber)`) — sem gradiente/`background-clip`.
- Cena 1: **logo completa** (PNG Ativo 80@2x) via `heroLogo`.
- Cena 2: barra única de MDF **substituída** pelo shot `crop-exploit-cards.png` (6 sizes).
  Mensagem: comparar a resposta do field size a size (20%…overpot), cada um com a própria amostra.
- Frases reprovadas **apagadas** (não reusar): *"vê a distância"*, *"escolher a linha"*,
  *"com amostra por célula"*.

## Alterações v2.1 (PO, 26/07 — 2ª rodada)
- **Logo pequena do topo removida** (era duplicada com a logo grande da cena 1) — mudança de
  template, vale pras 4 células. Só sobrevive **1 logo por cena**, no topo, quando `heroLogo:true`.
- Cena 2 ("Defesa do field · size a size"): **legenda do rodapé removida** — fica só o shot.
- Cena 3 ("A tela real"): **deletada**. Repetia o mesmo shot da cena 2 sem legenda nova — o PO
  achou redundante. A célula caiu de 6 pra **5 cenas**.
- ⚠️ **DESVIO DE DURAÇÃO**: com a cena 3 fora, a célula soma **21,0s**, não 26,0s como as outras 3.
  Registrado no build (`build-descoberta.mjs` § `CELLS`) — decisão do PO, não bug.

## Alterações v2.4 (PO, 26/07 — 5ª rodada)
- Cena 4: headline **"O GTO é o começo" → "Descubra o que o field realmente faz."** — a pedido
  do PO, essa cena "vira anúncio da Aura" em vez de ser só a conclusão do gancho. Caption e mockup
  inalterados. ⚠️ Tradução EN desta cena ainda **não** foi atualizada (ver tabela EN abaixo).

## Cenas

| # | dur | Conteúdo | Consequência de decisão |
|---|---|---|---|
| 1 | 3,8s | **Logo completa** (única, no topo) · 🔴 **GANCHO LITERAL** — kicker `MTT · pra quem estuda solver` · **"Você decorou o GTO."** → *(beat)* **"Seu oponente não."** · legenda: *GTO é o ponto de partida. O adversário real é outro assunto.* | — |
| 2 | 4,7s | Shot Exploitative Sizes — 20%, 33%, 42%, 55%, 75%, overpot lado a lado · *sem legenda de rodapé* | — |
| 3 | 4,7s | Escala: 10,6M mãos nesse spot · 500M+ auditadas · 7 salas | *Toda frequência vem com amostra e intervalo de confiança* |
| 4 | 4,6s | **"Descubra o que o field realmente faz."** + **mockup dos 2 monitores** | *Ferramenta de estudo. Você continua decidindo na mesa* |
| 5 | 3,2s | **CTA (idêntico nos 4)** — `Criar conta grátis` · *Preview de cada módulo. Sem cartão.* | — |

**21,0s** (⚠️ ver desvio acima) · 9:16 1080×1920 · sem áudio · selo `500M+ mãos auditadas · 7 salas` no rodapé de **todas** as cenas · 18+ em todo quadro.

## Compliance conferido
Enquadrado como **ferramenta de estudo** · zero promessa de lucro/EV/winrate ·
MDF sempre **descritivo** — nunca "leak" ou "logo é explorável" ·
solver citado como **categoria**, nunca marca · sem dinheiro/fichas/luxo · todo número com amostra.

## Tradução EN (v2 — 26/07, ajustes do PO — aguardando pedido de render)
Vocabulário alinhado ao que já existe em EN no deck (`p1/p2/p3`, `b1/b2/b3`): `field`, `size by
size`, `500M+ audited hands · 7 rooms`, `Create free account`.

| # | PT (atual) | EN |
|---|---|---|
| 1 | kicker `MTT · pra quem estuda solver` · big `Você decorou o GTO.` → beat `Seu oponente não.` · caption `GTO é o ponto de partida. O adversário real é outro assunto.` | kicker `MTT · for solver students` · big `You memorized the GTO.` → beat `Your opponent didn't.` · caption `GTO is the starting point. The real opponent is a different matter.` |
| 2 | kicker `Defesa do field · size a size` · line `20%, 33%, 42%, 55%, 75%, overpot — lado a lado, cada um com a própria amostra.` | kicker **`Field Defense % · size by size`** · line `20%, 33%, 42%, 55%, 75%, overpot — side by side, each with its own sample.` |
| 3 | kicker `A base por trás disso` · stats `Mãos só nesse spot` / `Mãos auditadas` / `Salas cobertas` · caption `Toda frequência vem com tamanho de amostra e intervalo de confiança.` | kicker **`The database behind it`** · stats `Hands in this spot alone` / `Hands audited` / `Rooms covered` · caption `Every frequency comes with sample size and confidence interval.` |
| 4 | big **`Descubra o que o field realmente faz.`** · caption `Ferramenta de estudo. Você continua decidindo na mesa.` | ⚠️ **pendente** (era `GTO is the start`, texto PT mudou na v2.4) · caption `A study tool. You still make the call at the table.` |
| 5 (CTA) | `Criar conta grátis` · `Preview de cada módulo. Sem cartão.` | `Create free account` · `Preview of every module. No card.` |

Selo persistente (todas as cenas): `500M+ mãos auditadas · 7 salas` → `500M+ audited hands · 7 rooms`.
