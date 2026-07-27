# AURA-DISC01 — estado no Meta e passos finais do Rafael

**Criado via MCP em 2026-07-25 · TUDO PAUSADO · nada gasta até o Rafael ativar.**
Design: [matriz-descoberta-4-celulas.md](matriz-descoberta-4-celulas.md)

## Estrutura criada

**Campanha `AURA-DISC01 · descoberta de publico` — ID `120248642473060327`**
Objetivo `OUTCOME_ENGAGEMENT` · **sem CBO** (orçamento por conjunto = verba igual garantida por célula)

| Célula | Ad set ID | Orçamento |
|---|---|---|
| `DISC-01-SOLVER` | `120248642477030327` | R$ 12,50/dia |
| `DISC-02-EXPLOIT` | `120248642479130327` | R$ 12,50/dia |
| `DISC-03-CATEGORIA` | `120248642484920327` | R$ 12,50/dia |
| `DISC-04-PIONEIRO` | `120248642485980327` | R$ 12,50/dia |

**Já configurado nos 4 (idêntico — variável de controle):**
- Otimização **ThruPlay** · cobrança por impressão · lance automático
- Geo **Brasil** · idade **21–47** · gênero **aberto**
- Posicionamento: **Instagram Reels + Stories** (sem Feed, sem Facebook, sem Audience Network, sem Messenger)
- **Advantage+ Audience DESLIGADA** (`advantage_audience: 0`)

## ⚠️ O que falta — parte do Rafael

### 1. Segmentação (nos 4 conjuntos, idêntica)
Não dá pra setar via MCP: este servidor não expõe busca de interesses, e inventar ID é rejeitado pela Meta.

### ✅ REALIDADE DA TAXONOMIA (verificado pelo PO no painel, 25/07)

A lista original era otimista. O que **existe de fato**:

| Termo | Existe? | Tamanho (global) | Usar? |
|---|---|---|---|
| **PokerStars** | ✅ | 25–29M | ✅ sim |
| **Campeonato Mundial de Pôquer** (WSOP) | ✅ | 20M | ✅ sim |
| **World Poker Tour** | ✅ | 20M | ✅ sim |
| Cargo `Professional Poker Player` | ✅ | **1.000** | ❌ **descartar** |
| GGPoker · partypoker · PokerNews · Hendon Mob | ❌ não existem | — | — |
| Times de staking BR | ❌ não indexados | — | — |

### ✅ CONFIGURAÇÃO FINAL (PO, 25/07) — **1,7–2M com a demografia aplicada** ✔ na faixa

| Interesse | Qualidade do sinal |
|---|---|
| **poker strategy** | 🟢 o melhor — **intenção de estudo**, não afinidade de marca. É literalmente o que a Aura vende |
| **poker tournament** | 🟢 MTT-específico |
| **world poker tour** | 🟢 circuito/jogador sério |
| **texas holdem poker** | 🟠 **o mais diluído** — pega também app social/grátis (jogador casual que não joga MTT). Mantido pelo volume |

⚠️ **`texas holdem poker` é o primeiro a cortar** se no D3 alguma célula vier com `% masculino` < 80% ou engajamento estranho. Os outros três são todos de jogador sério.

*(A busca do PO encontrou termos melhores que a lista original — `poker strategy` em especial. PokerStars/WSOP ficaram de fora da seleção final.)*

⚠️ **Os tamanhos mostrados na busca são GLOBAIS.** O número que importa é o estimador **após** BR + 21–47 — esperado 1,5–3M. Conferir no painel direito, não na caixa de busca.

**Cargo descartado — a Ressalva 1 se confirmou:** 1.000 pessoas prova que o padrão observado nas bios do **Instagram** não existe no campo de trabalho do **Facebook** (de onde a Meta puxa). Adicionar 1.000 num público de milhões não move nada.

### ⚠️ Exclusão de interesse NÃO EXISTE MAIS
A Meta **removeu** a exclusão da segmentação detalhada em boa parte das contas. Não dá pra excluir cassino/apostas/bingo por interesse. Consequências:
- O risco é **menor que no histórico** mesmo assim: os interesses são **marcas de poker** (não o "Poker" genérico, que era o contaminado) + otimização **ThruPlay** (não `PROFILE_VISIT`, a causa real) + **jargão do criativo**.
- **O criativo passa a carregar toda a filtragem** — por necessidade, não por escolha.
- **O gate do D3 fica mais crítico:** `% masculino` < 80% em alguma célula = contaminação. Reação disponível é trocar/ajustar criativo, já que targeting não dá margem.

**Ainda vale tentar (taxonomia é irregular):** `Texas hold'em` · `Torneio de pôquer` · `Pôquer online` · `PokerStars Brasil`. Se aparecerem com volume, somar.

**Ferramentas de nicho (GTO Wizard etc.) não existem na taxonomia** — a Meta só indexa marcas com escala de consumo. Não há como mirar "quem usa solver" por targeting; **é exatamente por isso que a célula 1 (SOLVER) existe** — o gancho encontra quem o targeting não alcança.

- **Opcional:** excluir o público `Aura | IG Engajadores 365d` (contaminado) na seção **Públicos personalizados** — essa exclusão ainda existe, é a de interesse que sumiu.

> **Teste de sanidade:** alvo **1,5–3M** após BR + idade. Abaixo de 1M satura; acima de 5M dilui.

### 2. Os 4 anúncios (1 por conjunto)
Bloqueado até a fábrica entregar os reels. Depois:
1. Subir os 4 MP4 na **Biblioteca de mídia**
2. Me avisar → **eu crio os 4 anúncios via MCP** com nome = `utm_content` e os parâmetros de URL

Nomes obrigatórios (viram `utm_content`): `disc-01-solver` · `disc-02-exploit` · `disc-03-categoria` · `disc-04-pioneiro`

### 3. Método de pagamento
Único bloqueio pra qualquer coisa ir ao ar.

### 4. (Opcional) Converter em teste A/B formal
Os 4 conjuntos já garantem **verba igual** por célula. O que o teste A/B nativo adiciona é **audiência mutuamente exclusiva** (ninguém vê duas células). Na prática, com frequência esperada ~1,0–1,5 e público de 2–5M, a sobreposição é pequena — então **os 4 conjuntos são suficientes**. Se quiser o rigor extra, dá pra criar pelo fluxo de A/B Test do painel a partir desses conjuntos.

## Campanha antiga
`AURA-PAID01` (ID `120248596900120327`, 2 conjuntos BR/PT + Intl/EN) segue **pausada**. Era o desenho de conversão, hoje substituído por esta. **Recomendação: deixar pausada** como esqueleto da fase 2 — a configuração já está feita e serve quando o internacional voltar.

## Regra absoluta
Tudo pausado. Ativação é exclusivamente do Rafael.
