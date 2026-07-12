# Estrutura de Campanhas Meta — Launch 2.0

**Autor:** thread Mídia Paga · **Data:** 2026-07-04 · **Status:** proposta para decisão do PO (orçamento em §5)
**Regra absoluta:** tudo sobe **PAUSADO**. Ativação, sempre e somente, pelo Rafael. Nenhum agente gasta um centavo.

Conta: **Aura Business** `1598770224460932` (BRL) · Pixel/dataset `1405949840871947` · IG @aurapokeranalytics.

**Addendums (2026-07-08):** este doc é o hub da estrutura; frentes detalhadas em docs próprios:
- [launch-hero-trafego.md](launch-hero-trafego.md) — tráfego do post de lançamento (reveal). Introduz uma fase **BOOST** (topo de funil, alcance/engajamento) que antecede a RTG.
- [publicos-build-spec.md](publicos-build-spec.md) — passo a passo de criação dos públicos novos (semente P1, salvo limpo P3, visitantes, exclusão de convertidos).
- [readiness-dia10.md](readiness-dia10.md) — painel go/no-go dos pré-requisitos até 10/07.
- [medicao-otimizacao.md](medicao-otimizacao.md) — funil, KPIs, valor/LTV (oferta USD) e regras de decisão pra otimizar.
- [handoff-landing-pixel-migracao.md](handoff-landing-pixel-migracao.md) — pixel/CAPI na landing Azure + prompt do dev + Stripe direto.

---

## 0. Princípios (herdados do plano de marketing)

- KPI norte: **conta free atribuída via UTM** — otimização para `CompleteRegistration`, não clique.
- Orgânico valida criativo primeiro (30–45d); pago **recicla vencedores**, não estreia conceito.
- 18+ em toda campanha; zero promessa de lucro (checklist do `compliance-meta.md` §3 vale por anúncio).
- Sequência: **retargeting quente → frio BR pequeno → frio EN** — na ordem, cada fase só abre com a anterior lida.

**Naming convention:** `AURA_<FASE>_<GEO>_<OBJETIVO>` / ad set `<publico>_<janela>` / ad `<pilar>_<criativo>_<formato>`. Ex.: `AURA_RTG_BR_CADASTRO > ig_engagers_90d > p1_overfoldBTN_1350`.

## 1. Fase RTG — Retargeting (primeira a subir)

**Por quê primeiro:** público quente, CPM baixo, menor exposição ao classificador de policy, e é o público que o orgânico do launch week está criando agora.

| | Campanha `AURA_RTG_BR_CADASTRO` |
|---|---|
| Objetivo | Vendas/Conversões → evento `CompleteRegistration` (fallback tráfego se <10 conv/sem: ver §6) |
| Ad set 1 | **Engajadores IG** @aurapokeranalytics — 90d (stories+feed+reels). Est.: base pequena (710 seguidores, alcance do teaser conta) — janela larga de propósito |
| Ad set 2 | **Visitantes da landing** 30d (pixel `PageView`), excluindo `CompleteRegistration` 180d |
| Exclusões (ambos) | Quem já criou conta (custom audience `CompleteRegistration` 180d) — não pagar por quem já converteu |
| Geo/idade | BR · 18+ |
| Posicionamentos | Feed IG + Stories/Reels IG (manual; sem Audience Network/FB right column — não temos Página FB ativa e o criativo é IG-nativo) |
| Destino | Landing com UTM: `utm_source=meta&utm_medium=paid_social&utm_campaign=rtg_br_launch20&utm_content={{ad.name}}` |

**Quando sobe (pausada):** já pode subir na semana do launch. **Quando ativa (decisão Rafael):** ver "Gate de ativação" abaixo — o guia antigo "≥500 visitantes OU 17/07" ficou stale (17/07 chegou sem o pool formado).

### Gate de ativação — atualizado pós-launch (2026-07-09), split por mercado

O gate NÃO é uma data — é **tracking + criativo + pool**, e é diferente por mercado (porque orgânico alcança BR mas **não alcança EN — nunca**; a base é 100% BR):

| Mercado | Orgânico valida/enche pool? | Gate pra ligar o pago |
|---|---|---|
| **BR (RTG quente)** | Sim — visitantes/engajadores BR acumulam de graça | (1) pool retargetável ≥ ~1.000 · (2) tracking Fase 2 ok · (3) ≥1 criativo vencedor no orgânico |
| **EN (frio)** | **Não — impossível** | (1) tracking Fase 2 ok · (2) criativo EN (já bilíngue) · (3) decisão do PO. **Sem pool quente → frio desde o dia 1** (interesse/broad, geos anglófonas, USD casa melhor) |

**Decisão do PO (2026-07-09): rodar os dois em paralelo** — RTG quente BR (barato) + teste frio EN (caro, CPM anglófono 2-4×), com orçamentos separados.

**Bloqueio comum aos dois = tracking Fase 2** (UTM no CTA + CAPI — ver [handoff-landing-pixel-migracao.md](handoff-landing-pixel-migracao.md)). Gastar em EN frio sem atribuição = pior cenário. **Prioridade #1: fechar isso com o dev.** Até lá, orgânico segue (enche pool BR + valida criativo BR), mas não é pré-requisito de tempo pra EN — EN é gated só no tracking + decisão.

## 2. Fase F1 — Frio BR (teste pequeno)

Abre somente com RTG rodando e custo/conta free conhecido (referência interna de CPA).

| | Campanha `AURA_F1_BR_CADASTRO` |
|---|---|
| Objetivo | Conversões → `CompleteRegistration` |
| Ad set 1 | Interesses poker BR: Poker, Texas hold 'em, PokerStars, GGPoker, World Series of Poker + refino por comportamento (engajamento com conteúdo de poker). Tamanho alvo 1–5M |
| Ad set 2 | **Lookalike 1–3%** dos cadastrados (subir quando a seed `CompleteRegistration` ≥ ~300; antes disso, seed = visitantes da landing) |
| Ad set 3 (teste B) | Advantage+ audience (broad 18+ BR) — deixar o algoritmo procurar; frequentemente ganha do interesse em custo |
| Geo/idade | BR · 18+ · homens+mulheres (não restringir gênero) |
| Criativos | Só vencedores do RTG/orgânico (ver §4) |

**Timing:** agosto (após 30–45d de validação orgânica, conforme plano). Não subir junto com RTG.

## 3. Fase F2 — Frio EN (depois)

Mesma estrutura da F1, quando F1 tiver CPA aceitável e a landing tiver versão EN.

- Geo: pacote inicial **US+CA+UK+AU+IE** (CPM alto, ICP denso). Alternativa barata para testar copy EN: **Europa nórdica/NL/DE**.
- **Excluir sempre os 18 mercados proibidos da policy de gambling** (lista no `compliance-meta.md` §1) — precaução de classificação, custo zero de alcance útil.
- Moeda da conta é BRL — ok, só lembrar que CPM US em BRL assusta no relatório.
- Campanha: `AURA_F2_EN_CADASTRO`.

## 4. Criativos exigidos (brief pra Fábrica de posts)

Reaproveitar **vencedores do orgânico** (critério: top saves + alcance no IG Insights; P1 stat cards são os candidatos naturais — cada stat é demo do produto).

| Formato | Uso | Specs |
|---|---|---|
| **1080×1350** (4:5) | Feed IG | Zona segura: título na metade superior; CTA textual "Crie sua conta grátis" |
| **1080×1920** (9:16) | Stories/Reels | Margem 250px topo / 340px base livres (UI do IG); versão com movimento leve (zoom/counter) rende CPM melhor |

Por ad set: **mínimo 2, ideal 3–4 criativos** (o leilão precisa de opção). Copy: PT no BR, EN puro na F2 (não bilíngue no anúncio). Todo criativo passa no checklist de compliance (§3 do compliance-meta.md) + regra de ouro dos números (stat verificado ou não sai).

**Pedido concreto à fábrica (quando RTG for aprovado):** 3 stat cards vencedores adaptados para 4:5 com CTA + as 3 versões 9:16. Nada de arte nova.

## 5. Orçamento — OPÇÕES PARA DECISÃO ✋

Premissas: CPM IG BR retargeting R$15–30, frio R$20–40; CTR 1–2%; conversão landing→free 15–30% (chute honesto, calibrar na 1ª semana). Números são para ORDEM DE GRANDEZA, não promessa.

### Fase RTG (público pequeno — teto natural)

| Opção | R$/dia | R$/mês | O que compra | Leitura |
|---|---|---|---|---|
| A 💡 | **30** | ~900 | ~1.5–2k impressões/dia; frequência controlada num público de poucos milhares | **Recomendada.** Público quente pequeno satura rápido; mais verba = frequência 8+, não mais contas |
| B | 50 | ~1.500 | Idem com frequência maior | Só se o público de visitantes passar de ~3–5k rápido |
| C | 100 | ~3.000 | Satura o público em dias | Não recomendo para RTG agora |

### Fase F1 — frio BR

| Opção | R$/dia | R$/mês | O que compra | Leitura |
|---|---|---|---|---|
| A | 30 | ~900 | ~1k impressões/dia frio | Sai do learning devagar (semanas); barato porém lento |
| B 💡 | **50** | ~1.500 | ~10–15 contas free/sem se o funil segurar | **Recomendada.** Mínimo que dá sinal em 2–3 semanas |
| C | 100 | ~3.000 | Learning em ~1 sem; leitura rápida | Se quiser velocidade e o caixa permitir |

### Fase F2 — frio EN

Decidir depois da F1. Referência: começar no equivalente a **US$10–20/dia** (R$55–110) — CPM anglófono come R$30/dia sem gerar leitura.

**Guard-rail geral:** kill switch se CPA > 3× a referência da fase anterior por 7 dias corridos. Limite de gasto da conta (Meta impôs R$105,49/dia hoje — sobe com histórico de pagamento; cobrir na auditoria).

## 6. Regras de operação (quando houver GO)

- Tudo criado **pausado**; print/nomenclatura pra revisão do Rafael; ele ativa no Gerenciador.
- Fallback de objetivo: se `CompleteRegistration` < 10/semana no ad set por 2 semanas, trocar otimização para "visitas à landing" até o volume voltar (conversão sub-10/sem não sai do learning nunca).
- Review semanal (sex, junto do ritual do QG): gasto, CPM, CTR, custo/conta free por UTM no AuraBusiness (fonte da verdade — não o número de conversão do Ads Manager, que superconta).
- Mudança de orçamento >20%/dia reseta learning — ajustar 1×/semana no máximo.

## 7. Pré-requisitos antes de QUALQUER real (ver auditoria-meta-ads.md)

Sem isso, nada sobe nem pausado: método de pagamento na conta, campanhas antigas com erro de pagamento DESATIVADAS, domínio confirmado no dataset, eventos da landing validados (checklist do pixel-capi-spec.md §6).
