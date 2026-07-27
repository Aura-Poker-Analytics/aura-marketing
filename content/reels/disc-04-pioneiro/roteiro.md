# disc-04-pioneiro · Célula 4 — PIONEIRO

**⚠️ MP4 v2.3 desatualizado — conteúdo mudou na v2.4 (ver abaixo). Precisa re-render.**
`content/paid/AURA-DESCOBERTA/disc-04-pioneiro.mp4` / `disc-04-pioneiro-en.mp4` são a v2.3, não
refletem a cena 2 nova.
**Campanha:** descoberta (30d) · **Eixo:** ⚠️ **POSICIONAMENTO** (não persona) · **`utm_content`:** `disc-04-pioneiro`
**Base:** novo · **Doc:** [matriz-descoberta-4-celulas.md](../../../docs/02-paid/matriz-descoberta-4-celulas.md) §2

## O que testa
Não é uma persona: testa se **novidade/ineditismo é razão suficiente pra parar o scroll**.
- **Deve parar:** quem é atraído por ser early adopter; quem já sentiu que falta uma categoria
- **Deve rolar:** quem só reage a dor concreta (esses param nas células 1 e 2)
- Versão aprovada: **(a)**, com a terminologia da casa.

## A sequência do gancho é deliberada (doc §2)
**Sentir → nomear.** O gancho faz *sentir* o ineditismo; a linha *nomeia* a categoria.
⚠️ **v2 (26/07):** a legenda do rodapé (*500M+ mãos lidas como população…*) foi **removida**
por pedido do PO (igual às legendas do disc-02). O instrumento do teste passa a ser
**gancho + linha**; o selo de prova persistente no rodapé (`500M+ mãos auditadas · 7 salas`)
continua em todas as cenas. Doc §2 atualizado.

## Alterações v2 (PO, 26/07)
- Dourado chapado · **legendas (`caption`) removidas de TODAS as cenas**.
- Cena 3: mockup **novo** do Preflop capturado a 2× do `aura-novofront` (`mockup-preflop-app.png`).
  O mockup de Postflop 2× ficou **bloqueado** (LOCAL sem dados postflop/`_pooled`).
- Cena 4: painel de filtros real (6 estágios) — inalterado.

## Alterações v2.1 (PO, 26/07 — 2ª rodada)
- Cena 1 recebeu a **logo completa** no topo (`heroLogo:true`) — vale pras 4 células
  (mudança de template: logo pequena removida, só sobrevive a logo grande).
- **Rebalanceamento de ênfase na cena 1** (pedido do PO: *"deixar com mais ênfase = Inteligência
  de Field MTT; 'isso não existia' tá predominando muito; Mass Data Analysis... move mais pra
  baixo"*). Palavras seguem 🔴 **LITERAIS** — só a tipografia mudou:
  - Kicker `Inteligência de field · MTT` ganhou peso (`kickerLg`, 42px vs 29px) — compete de
    igual com o headline, não fica como rótulo pequeno.
  - Headline `"Isso não existia."` **encolheu** (`bigSm`, 76px vs 104px) — parava de dominar o frame.
  - Linha `"Mass Data Analysis aplicada a MTT."` desceu (margin-top) — mais respiro antes dela.

## Alterações v2.2 (PO, 26/07 — 3ª rodada)
- Cena 3 ("A tela real" — mockup 2× do Preflop): **deletada** a pedido do PO. A célula caiu de
  6 pra **5 cenas**, mesmo padrão aplicado ao disc-01 na v2.1.
- ⚠️ **DESVIO DE DURAÇÃO**: com a cena 3 fora, a célula soma **21,0s**, não 26,0s como disc-02/03.
  Registrado no build (`build-descoberta.mjs` § `CELLS`) — decisão do PO, não bug.

## Alterações v2.3 (PO, 26/07 — 4ª rodada)
- Cena 3 (painel de filtros real): kicker **"Do early à mesa final" → "Do Early-Game à Mesa
  Final"** — casa com o nome exato do primeiro estágio mostrado no painel (`Early Game`).

## Alterações v2.4 (PO, 26/07 — 5ª rodada)
- Cena 2: kicker **"População, não amostra" → "Os padrões do field a um clique de distância."**
  a pedido do PO. ⚠️ Tradução EN desta cena ainda **não** foi atualizada.

## Cenas

| # | dur | Conteúdo | Consequência de decisão |
|---|---|---|---|
| 1 | 3,8s | **Logo completa no topo** · 🔴 **GANCHO LITERAL** — kicker `Inteligência de field · MTT` (em destaque) · **"Isso não existia."** (menor) → *(beat)* linha **"Mass Data Analysis aplicada a MTT."** (mais abaixo) · *sem legenda de rodapé* | — |
| 2 | 4,7s | **"Os padrões do field a um clique de distância."** — **mockup dos 2 monitores** | — |
| 3 | 4,7s | **Painel de filtros real** — kicker `Do Early-Game à Mesa Final` · os 6 estágios NOMEADOS | — |
| 4 | 4,6s | "Inteligência de field" · *O mesmo jogo — novas informações* | *Ferramenta de estudo* |
| 5 | 3,2s | **CTA (idêntico nos 4)** — `Criar conta grátis` · *Preview de cada módulo. Sem cartão.* | — |

**21,0s** (⚠️ ver desvio acima) · 9:16 1080×1920 · sem áudio · selo no rodapé de **todas** as cenas · 18+ em todo quadro.

## Compliance conferido
O gancho aprovado afirma **ineditismo por demonstração**, não superioridade.
Todo número com amostra · sem marca de concorrente · ferramenta de estudo · sem dinheiro/fichas/luxo.

## Tradução EN (v2 — 26/07, ajustes do PO — aguardando pedido de render)
Vocabulário alinhado ao que já existe em EN no deck (`p1/p2/p3`, `b1/b2/b3`) — `Field
intelligence · MTT` é tradução literal já usada em outras células (`p3-s1-en`/`b3-s1-en`).
`"Population"` trocado por `"field"` pra manter o termo consistente com as outras 3 células
(nenhuma usa `"pool"`).

| # | PT (atual) | EN |
|---|---|---|
| 1 | kicker `Inteligência de field · MTT` (em destaque) · big `Isso não existia.` (menor) → beat `Mass Data Analysis aplicada a MTT.` | kicker `Field intelligence · MTT` (em destaque) · big **`This never existed.`** (menor) → beat `Mass Data Analysis applied to MTT.` |
| 2 | kicker **`Os padrões do field a um clique de distância.`** — mockup dos 2 monitores | ⚠️ **pendente** (era `The field's data, not a sample`, texto PT mudou na v2.4) |
| 3 | kicker `Do Early-Game à Mesa Final` — painel de filtros real (6 estágios) | kicker `From Early Game to the Final Table` — painel de filtros real (nomes dos estágios já nascem em EN no mockup) |
| 4 | big `Inteligência de field` · line `O mesmo jogo — novas informações.` | big `Field intelligence` · line `The same game — new information.` |
| 5 (CTA) | `Criar conta grátis` · `Preview de cada módulo. Sem cartão.` | `Create free account` · `Preview of every module. No card.` |

Selo persistente (todas as cenas): `500M+ mãos auditadas · 7 salas` → `500M+ audited hands · 7 rooms`.
