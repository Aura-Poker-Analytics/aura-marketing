# Análise das campanhas históricas — por que uma trouxe público aderente e as outras não

**Autor:** thread Mídia Paga (3 subagentes Sonnet, somente leitura) · **Data:** 2026-07-21
**Fonte:** Meta Ads MCP, conta `1598770224460932` ("Aura Business"), janela `maximum` (29/01/2026 – 21/07/2026)
**Gasto histórico total auditado:** R$ 529,18

> **Limitação metodológica declarada:** o *targeting spec* configurado (interesses, exclusões, faixas escolhidas) **não é exposto** por esta API — testado explicitamente. As conclusões usam (a) nome/estrutura dos ad sets, (b) `optimization_goal`, (c) CTA e criativo, e (d) o **breakdown de entrega real** (quem foi de fato impactado). Onde não há dado, está marcado como não disponível — nada foi inferido como se fosse medido.

---

## 1. As três campanhas

| Campanha | Objetivo | Gasto | Alcance | CTR | CPC | CPM |
|---|---|---|---|---|---|---|
| **Apresentando a Aura - 2026** | LINK_CLICKS | **R$ 505,03** | 60.134 | 2,11% | R$ 0,20 | **R$ 4,22** |
| **Video Preflop Youtube** | LINK_CLICKS | R$ 19,77 | 1.061 | **12,85%** | R$ 0,14 | R$ 17,40 |
| Apresentando a Aura - Engajamento | OUTCOME_ENGAGEMENT | R$ 4,38 | 168 | 0,56% | R$ 4,38 | R$ 24,47 |

## 2. O que NÃO explica a diferença (hipóteses testadas e refutadas)

| Hipótese | Veredito |
|---|---|
| Inventário ruim / Audience Network | ❌ **0% de Audience Network** nas duas. 100% Instagram |
| Vazamento geográfico | ❌ Ambas ~100% Brasil |
| Faixa etária errada | ❌ Ambas concentradas em 18-34 |
| Desktop / cliques acidentais | ❌ 100% mobile nas duas |
| Posicionamento | ❌ Ambas dominadas por Reels/Stories |

O CPM de R$4,22 **não** era fraude de inventário: é o preço natural de Reels (50,8%) + Stories (49,2%) com 0% de Feed. Mas era, sim, sintoma de **audiência pouco disputada** — barato porque era fácil, não porque era eficiente.

## 3. A causa raiz: três fatores que se somam

### 3a. 🔴 O `optimization_goal` era PROFILE_VISIT — o fator dominante

A campanha "Apresentando a Aura - 2026" está rotulada LINK_CLICKS **no nível de campanha**, mas seus **3 ad sets otimizam para `PROFILE_VISIT`**:

| Ad set | Optimization goal | Gasto | CTR |
|---|---|---|---|
| Aura \| LAL Seguidores 1% | PROFILE_VISIT | **R$ 377,54** | 2,42% |
| Aura \| LAL Seguidores 1–3% | PROFILE_VISIT | R$ 57,39 | 1,20% |
| Aura \| Amplo + Advantage+ | PROFILE_VISIT | R$ 70,10 | 1,18% |
| *(Video Preflop Youtube)* | **LINK_CLICKS** | R$ 19,77 | **12,85%** |

E o CTA de todos os 3 era **`VIEW_INSTAGRAM_PROFILE`** — mandava pro perfil do Instagram, **não pro site**.

**Isso explica literalmente o sintoma relatado.** Você pediu ao Meta "me traga gente que visita perfil" — e ele otimizou para encontrar quem completa essa ação barata. Visitar perfil é curiosidade, não intenção. O algoritmo entregou exatamente o que foi pedido: **visitantes de perfil baratos, que viram seguidores sem relação com o produto.**

### 3b. 🟠 Lookalike construída sobre semente contaminada (~1.000 seguidores)

Os dois maiores ad sets são lookalikes da base **"Aura | Seguidores IG (Base)" — apenas ~1.000 pessoas**, sem nenhuma camada de interesse em poker.

Uma LAL replica **semelhança comportamental/demográfica genérica** com a semente. Se a semente de uma conta nova já contém amigos, curiosos e seguidores de compromisso, a LAL **amplifica esse ruído** para 1,3–2,9 milhões de pessoas.

### 3c. 🟢 O criativo do "Preflop" funcionou como filtro natural

O anúncio vencedor era um **post nativo impulsionado** sobre estratégia de **preflop** — jargão técnico hiper-específico. O conteúdo se auto-seleciona: só quem entende o termo e se importa com o tema para o scroll e clica.

Os outros 3 usavam **o mesmo carrossel institucional** ("Revolucione seu jeito de explorar o field") — mensagem genérica de marca, que não filtra ninguém.

## 4. A impressão digital nos dados: gênero

| | Apresentando a Aura - 2026 | Video Preflop Youtube |
|---|---|---|
| Masculino | **61–65%** | **94,7%** |
| Feminino | **35–38%** | 4,6% |
| CTR 18-24 | 2,11% | **15,63%** |
| CTR 25-34 | ~2,2% | **12,15%** |

Quase **4 em cada 10 impactos foram mulheres** na campanha grande — desproporcional para o público real de MTT. É a assinatura de uma lookalike "parecida com seguidores de Instagram" (que espelha a base ampla do IG) em vez de público filtrado por comportamento de poker.

O CPM caro do "Preflop" (R$17,40) é o **preço normal de audiência disputada e qualificada** — reforça que "barato" nas outras era sintoma, não eficiência.

## 5. ⚠️ Consequência que afeta o plano atual

O público **"Aura | IG Engajadores 365d" (8.600–10.100 pessoas)** — que eu havia recomendado como Camada 1 do primeiro teste pago — foi **parcialmente construído por essas campanhas**. Visitas de perfil e engajamento gerados pelos ad sets de PROFILE_VISIT entram nesse pool.

**Ou seja: retargetear esses 9k pode significar re-alcançar justamente o público irrelevante que essas campanhas trouxeram.** Revisa a recomendação anterior — o tamanho existe, mas a qualidade é suspeita.

Os públicos **limpos** hoje são os pequenos: Site Visitantes (20) e Convertidos CompleteRegistration (20) — pequenos porque o consent gate bloqueava o pixel até 21/07, e que **agora crescem** com sinal limpo.

## 6. Princípio para o próximo real

> **O público que você constrói é função do que você otimizou.** Otimizar por visita de perfil constrói uma audiência de visitantes de perfil. Otimizar por cadastro constrói uma audiência de cadastrantes.

Regras derivadas, para a Fase B:

1. **Nunca otimizar por PROFILE_VISIT** para aquisição. Otimizar pela ação mais profunda que o orçamento sustentar — no nosso caso, `CompleteRegistration` (agora rastreável e provado).
2. **CTA para o site**, nunca `VIEW_INSTAGRAM_PROFILE`.
3. **Criativo com jargão específico** (preflop, ranges, ICM, field) filtra melhor que qualquer segmentação de interesse disponível — foi o que entregou 12,85% de CTR com R$19,77.
4. **Não construir lookalike sobre a base de seguidores.** Esperar ~100 cadastros reais e construir a LAL sobre **convertidos** — semente pequena mas limpa vale mais que semente grande e ruidosa.
5. **Desconfiar de CPM barato.** Nesta conta, CPM baixo foi indicador de audiência irrelevante, não de eficiência.

## 7. O que segue não disponível

- Targeting spec configurado (interesses/exclusões) — não exposto pela API
- Corpo/legenda do post impulsionado "Preflop" — não recuperável via campos de creative
- Métrica direta de "seguidores ganhos por campanha" — não disponível; a inferência de qualidade usa gênero + CTR como proxies

**Regra absoluta mantida:** auditoria 100% somente leitura. Nada foi criado, ativado, pausado ou impulsionado.
