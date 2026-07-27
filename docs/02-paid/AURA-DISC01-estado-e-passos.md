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

No construtor de público de **cada** conjunto:
- **Incluir (interesses):** PokerStars · GGPoker · partypoker · World Series of Poker · World Poker Tour · PokerNews · Hendon Mob
- **Incluir (Dados demográficos → Trabalho → Cargos):** Professional Poker Player · Poker Player · Jogador de Poker
- **Explorar:** times de staking BR (Gigantes, Nit, RPT, CPC, Red Line) se existirem como interesse/empregador
- **Excluir:** Cassino · Jogos de cassino · Apostas · Apostas esportivas · Bingo · Caça-níqueis
- ❌ **Nunca** o "Poker" genérico isolado (agrega cassino)
- **Opcional:** excluir o público `Aura | IG Engajadores 365d` (contaminado pelas campanhas antigas)

> **Teste de sanidade:** adicione uma camada por vez e observe o estimador. Alvo **2–5M**. Abaixo de 1M satura; acima de 8M dilui. Se o *cargo* quase não mover o ponteiro, é a ressalva IG-bio × perfil-Facebook se confirmando — deixe lá mesmo assim, não custa.

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
