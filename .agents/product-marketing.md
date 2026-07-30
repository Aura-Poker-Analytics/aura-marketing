# Product Marketing Context — Aura Poker Analytics

**Versão:** 1.0 · **Criado:** 2026-07-29 · **Mantido por:** thread Mídia Paga
**Formato:** skill `product-marketing` ([coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)) — 12 seções canônicas.
**Fontes:** `docs/00-strategy/product-truth-aura.md` (gabarito), `brand/brand-kit.md`, `docs/02-paid/*`, landing em produção, pesquisa na Meta Ads Library (07/2026).

> **Legenda de confiança:** ✅ documentado e verificado · 🟡 inferido de material interno · 🔴 **LACUNA — nunca pesquisado com cliente real**

---

## 1. Product Overview ✅

**Categoria própria:** inteligência de exploit da **população (field) de MTT**. Mede o que o field **realmente faz** (frequências observadas), não teoria.

- **NÃO é tracker** — não mostra winrate/ROI/bankroll pessoal do herói.
- **NÃO é solver** — não compara com GTO, não tem overlay solver×pool, não calcula EV. Hoje é **100% descritivo** (frequência observada) + um sinal de exploit: pressão de fold vs MDF (heurística, nunca chamada de "GTO").

**Módulos:** Hotspot (exploit cards ranqueados por desvio de MDF, com selo de confiança) · Preflop (RFI/3bet/4bet por posição, stack, estágio, tipo de torneio) · Postflop (árvore de ação, sizing em %pot, defesa vs MDF por street) · Node-by-Node (árvore navegável, `n` por nó) · Team Mode.

**Pricing:** Grátis $0 pra sempre sem cartão (= **preview de cada módulo**) · Individual $29/mês · $149/6m · $259/ano. Team sob consulta.

---

## 2. Target Audience 🟡

**Declarado pelo PO:** majoritariamente **masculino, 21–47 anos**, Brasil (mercado inicial), jogadores de MTT online.

**Segmentação disponível na prática:** interesses de plataforma resolvem apenas `Poker strategy`, `World Poker Tour`, `Poker tournament` — ferramentas de nicho (solvers, trackers) **não existem** na taxonomia. Cargo "Professional Poker Player" = ~1.000 pessoas (sinal inexistente).

🔴 **Lacuna:** não há segmentação por nível de investimento em estudo, buy-in médio, ou volume jogado — que provavelmente são os eixos que separam comprador de curioso. Nunca medido.

---

## 3. Personas 🟠

Quatro hipóteses foram **inventadas para a campanha de descoberta** (AURA-DISC01), não validadas com cliente:

| # | Persona hipotética | Enquadramento testado |
|---|---|---|
| 1 | Reg que estuda solver | "Você decorou o GTO. Seu oponente não." |
| 2 | Jogador exploitativo | "A matemática diz 64,5%. O field defende 57,7%." |
| 3 | MTT player sem contexto (**controle**) | "Não é solver. Não é tracker." |
| 4 | Early adopter / atraído por ineditismo | "Isso não existia." |

🔴 **Estas são hipóteses, não personas.** Persona real exige pesquisa com usuário: rotina de estudo, ferramentas que já paga, gatilho de compra. A campanha de descoberta existe justamente para começar a resolver isso — mas ela mede *reação a mensagem*, não *quem a pessoa é*.

---

## 4. Problems & Pain Points 🟡

**Inferidos** (do posicionamento, não de entrevista):
- Solver mostra equilíbrio teórico, mas o oponente real não joga equilíbrio
- Tracker mostra as **suas** mãos — amostra pequena, nada sobre a população
- Estudar sem saber onde o field desvia = otimizar no vácuo
- Ferramentas existentes exigem interpretar output complexo

🔴 **Nenhuma dor foi confirmada por cliente.** Não sabemos qual delas dói mais, nem se alguma delas é a dor que faz alguém pagar.

---

## 5. Competitive Landscape ✅

Levantado na Meta Ads Library (07/2026), anúncios **ativos**:

| Concorrente | Ângulo que usa | Mercado |
|---|---|---|
| GTOWizard | feature/solver ("Your PLO Solver Is Here") | global, **48 anúncios no BR sem uma linha em PT** |
| Custom Poker Trainer AI | resultado ("increase your win-rate in weeks") | global |
| PolarizePoker | medo/isolamento ("Estudas sozinho?") | Europa/PT |
| Railbird | anti-complexidade do solver | global |
| Drivehud | feature (HUD all-in-one) | global |
| Times de staking BR (Gigantes, Nit, RPT…) | coaching/staking | BR |

**Padrões de mensagem no mercado:** feature-first (mais comum) · resultado/winrate · medo/leak · simplificação anti-solver · isca grátis.

**🎯 Ângulo desocupado:** **ninguém vende por dado populacional.** Todos vendem teoria, resultado ou coaching. E o BR está sub-servido em português.

---

## 6. Differentiation ✅

**A diferença estrutural:** solver mostra o **ótimo teórico**; tracker mostra **a sua amostra**; a Aura mostra **o que a população inteira faz** — 500M+ mãos auditadas, 7 salas.

**Tagline:** *"O mesmo jogo — novas informações."*

**Defensabilidade:** o ativo é o dataset (volume + parser proprietário + atualização trimestral), não a interface. Difícil de copiar sem o mesmo volume de mãos.

---

## 7. Objections & Anti-Personas 🔴 **LACUNA CRÍTICA**

**Nunca documentado.** Objeções plausíveis, todas **não testadas**:

| Objeção provável | Temos resposta? |
|---|---|
| "Já pago solver, pra que outra ferramenta?" | ❌ não articulada |
| "Dado de população não me diz o que fazer NESTE spot" | ❌ e é uma objeção legítima (ver §10 do gabarito: MDF é descritivo) |
| "Como sei que a amostra representa os torneios que EU jogo?" | 🟡 parcial (filtros por buy-in/estágio existem, mas nunca usados como resposta) |
| "É mais uma coisa pra aprender a usar" | ❌ não endereçada |
| "500M mãos de quais salas? Jogo em sala que não está aí" | ⚠️ **sensível** — ~89% do volume é família PokerStars (uso interno, não publicável) |

**Anti-personas (quem NÃO é cliente):** jogador de cash game · jogador casual/app social · quem busca promessa de lucro rápido · quem joga sem estudar.
🔴 **Nenhuma delas está excluída em nenhum canal** — e a campanha atual está entregando exatamente para app social (ver §12).

---

## 8. Switching Dynamics 🔴 **LACUNA CRÍTICA — provavelmente a mais custosa**

Framework push/pull/habit/anxiety. Nosso estado:

| Força | O que a Aura faz hoje |
|---|---|
| **Pull** (atração pelo novo) | ✅ **é tudo que fazemos** — "olha esse dado", "isso não existia" |
| **Push** (insatisfação com o atual) | ❌ quase nada — só a célula 1 tangencia ("você decorou o GTO") |
| **Habit** (inércia da rotina atual) | ❌ **zero** — nunca endereçamos que o cara já tem uma rotina de estudo |
| **Anxiety** (medo de trocar) | ❌ **zero** — nunca endereçamos "vou ter que aprender outra ferramenta", "confio nesse dado?" |

**Por que isso importa agora:** um jogador que estuda **já tem um jeito de estudar**. Nossa comunicação apresenta informação nova sem nunca dar razão para **mudar de rotina**. Curiosidade sem push/habit/anxiety gera clique e não gera adoção — que é compatível com o que a campanha está mostrando.

---

## 9. Customer Language 🔴 **LACUNA CRÍTICA**

**Zero linguagem verbatim de cliente.** Toda a copy (ads, landing, posts) foi escrita internamente a partir do gabarito de produto.

O que temos: **jargão técnico correto** (RFI, 3bet, MDF, field, ICM, overfold) — validado como filtro de público, com evidência (o criativo com jargão denso fez 12,85% de CTR historicamente).

O que **não** temos: como o grinder brasileiro **descreve a própria frustração** com as próprias palavras. Nunca houve entrevista, nem leitura sistemática de fórum/Discord/comentário.

⚠️ **A skill é explícita nisso:** ela pede *"verbatim customer language over polished descriptions"*. Nós temos exclusivamente o polido.

**Consequência:** a copy é tecnicamente correta e pode estar emocionalmente muda. Estamos falando **sobre** o problema, não **como** quem tem o problema.

---

## 10. Brand Voice ✅

- **Tom:** técnico-afiado, de reg pra reg. 🚫 **PROIBIDO tom guru/get-rich.**
- **Jargão fica em inglês** nas duas línguas (RFI, MDF, field, ICM) — é como o público fala.
- **Categoria:** "Inteligência de field" (PT) / "Field intelligence" (EN). Método: **Mass Data Analysis (MDA)**, não traduzir.
- **Visual:** sem dinheiro, fichas empilhadas como riqueza, ou luxo. Telas do produto e gráficos são o visual.

---

## 11. Proof Points ✅

**Aprovados:** 500M+ mãos auditadas (nunca "bilhões") · 7 salas cobertas · 100% anonimizado · toda frequência com **intervalo de confiança (Wilson) + tamanho de amostra** · atualização trimestral · selo de confiança por amostra nos exploit cards (High ≥5.000 / Med ≥1.000 / Low <1.000).

**Proibidos:** promessa de lucro/EV/winrate · "solver overlay"/"vs GTO" · proporção de volume por sala · "Hotspot completo grátis" · *"defesa abaixo do MDF = leak explorável"* (o sinal é descritivo — ver §10 do gabarito).

🔴 **Prova social: inexistente.** Os depoimentos que estavam na landing eram **fictícios** e foram sinalizados para remoção. Não há caso de uso real, número de usuários publicável, nem depoimento verdadeiro. **Num mercado técnico e cético, isso é uma lacuna séria** — e todos os concorrentes têm alguma forma de prova.

---

## 12. Goals 🟡

**Fase atual (descoberta, 30d, R$1.500):** descobrir **qual enquadramento ressoa com qual perfil**. Sucesso = perfil identificado + custo por engajador qualificado. **Não** é conversão.

**Estado real em 29/07 (D3):** ~R$100 gastos · 218 sessões pagas · **94% de rejeição, 2,2s de sessão média** · **0 cadastros atribuídos ao pago**. Landing está saudável (orgânico fica 116s), então o problema é qualidade de tráfego. Otimização trocada de cliques → visualizações de página; campanha pausada aguardando reativação.

**Próximas fases:** ~100 cadastros limpos → lookalike sobre convertidos → otimização por conversão → mercado internacional (EN) com o gancho vencedor.

---

## Changelog

**1.0 — 2026-07-29** · Criação. Consolidado de `product-truth-aura.md`, `brand-kit.md`, pesquisa na Ads Library e docs de mídia paga. Três lacunas críticas identificadas e marcadas: **Objeções (§7)**, **Switching Dynamics (§8)** e **Customer Language (§9)** — nenhuma delas jamais pesquisada com cliente real. Prova social registrada como inexistente (§11).
