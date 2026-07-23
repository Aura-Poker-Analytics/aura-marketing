# Campanha 1 — plano revisado (v2)

**Autor:** thread Mídia Paga · **Data:** 2026-07-21
**Insumos:** auditoria das campanhas históricas ([analise-campanhas-historicas.md](analise-campanhas-historicas.md)) + diagnóstico da conta via MCP + varredura de concorrentes na Meta Ads Library (2 subagentes, somente leitura).
**Status:** PROPOSTA — nada foi criado. Quando houver GO + orçamento, sobe tudo **PAUSADO** para revisão e ativação do Rafael.

---

## 0. O que mudou da v1 para a v2

| # | v1 | v2 | Motivo |
|---|---|---|---|
| 1 | Formato não especificado | **Vídeo vertical estilo Reels obrigatório** | O vencedor histórico (12,85% CTR) era vídeo nativo em Reels; o perdedor era carrossel estático. Entrega da conta é ~99% Reels/Stories |
| 2 | 1 criativo | **3 variantes competindo** | Com 1 peça não se separa "público ruim" de "criativo ruim" |
| 3 | UTM genérico | **UTM por anúncio** (`utm_content={{ad.name}}`) | `tbl_user` grava UTM → custo por cadastro POR CRIATIVO medido no nosso banco, imune a iOS/adblock |
| 4 | Compromisso de 30 dias | **Gates de decisão D3/D7/D14** | CPC estimado não é validável (sem benchmark pra conta); nunca ficar a mais de 1 semana de um ponto de saída |
| 5 | 1 conjunto | **2 conjuntos (teste de segmentação)** | A taxonomia de interesses é onde mora a contaminação — teste explícito: interesses específicos vs. amplo+criativo-filtro |
| 6 | Copy genérica de nicho | **Ângulo "dados reais do field" + PT-BR** | Varredura da Ads Library: ângulo desocupado + BR sub-servido (abaixo) |

## 1. Inteligência competitiva — o que a Ads Library mostrou

**Quem anuncia hoje no nicho:** GTOWizard (48 anúncios ativos no BR, copy 100% EN), Custom Poker Trainer AI, GTO LAB (curso), PolarizePoker (PT europeu), Railbird, Drivehud, Octopi, BBZPoker + times de staking BR (Gigantes, Nit, RPT — não são SaaS).

**Os 3 fatos que moldam nosso criativo:**

1. **Ninguém vende por dados populacionais reais.** Todos vendem feature ("Your PLO Solver Is Here"), resultado ("increase win-rate in weeks") ou medo ("Stop Losing to RNG"). O ângulo *"isso é o que 500M+ mãos reais mostram que o field realmente faz — não teoria"* está **desocupado**. É exatamente o nosso produto.
2. **BR está sub-servido em português.** GTOWizard roda 48 anúncios no BR **sem uma linha em PT-BR**. Só um player europeu (PolarizePoker) e um micro (Poker 101mod) falam português. Falar PT-BR com jargão local já é diferenciação.
3. **O ângulo medo/leak/variância ressoa no público lusófono** (é o padrão dos dois únicos anunciantes em PT). Vale uma variante.

## 2. Estrutura proposta (REVISADA — v2.1, refino após pergunta do PO "por que só 3 reels / por que não impulsionar os outros")

**Decisão 1 — nunca o botão "Impulsionar".** Boost empurra pra PROFILE_VISIT/engajamento — foi a causa do desastre dos R$505. Tudo roda pelo **Gerenciador de Anúncios**. Para reaproveitar criativos orgânicos, usar **"Usar publicação existente"** (não boost): roda o post existente como anúncio **mantendo a prova social** (views/curtidas/comentários que ele já acumulou) + dá controle total de objetivo/otimização/UTM.

**Decisão 2 — mais criativos, não menos.** Criativo é a alavanca #1 do Meta; o ideal é 5–6 peças competindo, não 3. Mix = **3 reels PT novos + 2–3 melhores criativos orgânicos existentes** (que carregam prova social que as peças novas não têm).

**Filtro para reaproveitar um criativo orgânico:** (a) vídeo, não carrossel estático (carrossel foi o perdedor); (b) jargão/produto na tela, não brand genérico; (c) já performou no orgânico (saves/shares). Posts product-forward (UI/módulos reais) são candidatos fortes. *(Seleção é do PO/fábrica — o MCP não expõe performance de post orgânico nesta conta.)*

**Decisão 3 — língua vira teste, não regra.** Os orgânicos existentes são EN e têm prova social. Testá-los custa zero → rodar EN antigos + PT novos no mesmo público e deixar o `tbl_user` dizer qual língua gera cadastro mais barato. (Produção nova segue PT — §6b — mas não se assume que PT vence; mede-se.)

**Decisão 4 — estrutura simples primeiro (concentra budget):**

```
Campanha: AURA-PAID01-CLIQUES (objetivo: Tráfego)
│
└── 1 Conjunto — "Amplo + criativo-filtro"  (R$50/dia)
      Amplo (sem interesses), Geo BR, Idade 20–45, só Instagram (Reels/Stories/Feed)
      Exclusões: cassino, apostas esportivas, bingo, jogos de azar
      5–6 criativos (3 PT novos + 2–3 orgânicos existentes via "usar publicação")
      Hipótese central: o jargão do criativo filtra melhor que a taxonomia
      (foi o mecanismo real do vencedor histórico)
```

Por que 1 conjunto e não 2: R$50/dia é pequeno; dividir deixa cada criativo com dado de menos, e nosso próprio achado diz que **criativo > targeting**. Geo = amplo internacional (§6b), não BR. **Só dividir num 2º conjunto SE o amplo entregar sujo no D3** (% masculino baixo, ou país-lixo dominando os cadastros) — complexidade progressiva. Candidatos a 2º conjunto, nessa ordem: (a) **LAL worldwide sobre a base limpa** (§5b — testar contra o amplo), (b) interesses específicos (solvers/trackers, nunca "poker" isolado).

Otimização: **cliques no link / visualizações da LP** (não conversão — volume insuficiente pra sair do aprendizado). Rede de segurança: como cada criativo tem UTM próprio e o cadastro grava no `tbl_user`, clique-lixo é detectado pelo dado real (clica mas não cadastra), não pela métrica da Meta.
Nada de Advantage+ audience expansion. Nada de Audience Network/Messenger.

## 3. Os 3 criativos (vídeo vertical 9:16, **EN** — revisado v2.2, 15–30s)

| # | Ângulo | Gancho (direção de copy) | Base de evidência |
|---|---|---|---|
| **V1** | Réplica do vencedor: jargão preflop | "RFI do field no BTN é 44%. O solver diz 48%. Essa diferença é EV." | Formato/tema do post de 12,85% CTR |
| **V2** | Dados reais vs. teoria (ângulo desocupado) | "Solver mostra o equilíbrio. A Aura mostra o que 500M+ mãos reais fazem de verdade." | Lacuna confirmada na Ads Library |
| **V3** | Leak/medo (padrão que ressoa em PT) | "Seu redline não é azar. É leak — e o field te mostra onde." | Padrão dos anunciantes PT |

Destino de todos: `https://www.aurapoker.com/?utm_source=meta&utm_medium=paid&utm_campaign=paid01&utm_content={{ad.name}}&utm_term={{adset.name}}`
(parâmetros dinâmicos da Meta → cada cadastro no `tbl_user` diz qual anúncio o gerou)
CTA: **site**, nunca perfil do IG.

## 4. Gates de decisão (substituem o "30 dias")

| Gate | Métrica | Verde | Vermelho → ação |
|---|---|---|---|
| **D3** | **% masculino no alcance** (breakdown gender) | >85% | <80% → pausar conjunto vazado; revisar interesses |
| D3 | Frequência | <2 | >2,5 → público pequeno demais, ampliar |
| **D7** | CTR por criativo | >4% em ≥1 peça | peça <2% → pausar a peça (não a campanha) |
| D7 | CPC real | ≤R$1,50 | >R$2,50 → hipótese de custo furada, reavaliar orçamento |
| D7 | Cobertura `fbc` no dataset (EMQ) | subindo vs. 25% | estagnada → investigar propagação do fbclid |
| **D14** | **Custo por cadastro** (medido no `tbl_user` via utm_content) | <R$25 | >R$40 → parar e replanejar |
| D14 | Conjunto A vs. B | — | O perdedor claro é pausado; o orçamento consolida no vencedor |

**Por que % masculino como alarme precoce:** foi a impressão digital que separou o público bom (94,7% M) do ruim (61% M) na auditoria — e aparece em 48h, semanas antes do custo por cadastro estabilizar.

## 4c. Orçamento em tranches (o R$1.500 é TETO, não compromisso de 30 dias)

| Semana | Gasto | Portão |
|---|---|---|
| 1 | R$ 350 (R$50×7) | D3: %masc >85% · D7: ≥1 criativo >4% CTR, CPC ≤R$1,50 |
| 2 | R$ 350 | mata criativos fracos; só continua se D7 passou |
| 3–4 | até R$ 800 | D14: custo/cadastro <R$25 no `tbl_user` → escala/ajusta/para |

Se a Semana 1 vier ruim, o gasto foi R$350, não R$1.500. Nunca a mais de 7 dias de um ponto de saída.

## 5. Premissas declaradas como não-validadas

- **CPC R$0,50–1,50 é hipótese.** A Meta não tem benchmark pra esta conta (histórico insuficiente). O CPC histórico de R$0,14–0,20 era de PROFILE_VISIT (ação barata) — não serve de referência. Os 3 primeiros dias são o benchmark real.
- **Opportunity Score 100/100 da conta é artefato de conta vazia** — não é validação de nada.
- Projeção honesta a R$50/dia por 30d: CPC R$0,50 → ~150 cadastros · R$1,00 → ~75 · R$1,50 → ~50 (a 5% de conversão da LP).

## 6. Pré-lançamento (checklist)

- [ ] Rafael: verificação da empresa + 2FA no BM (G6/G7 — ~20 min)
- [ ] Rafael: corrigir **vertical do negócio** no BM: está "Publishing/Online Only Publications" → Software/SaaS (achado do diagnóstico; distorce otimização e benchmarks)
- [ ] Rafael: método de pagamento (só no GO)
- [ ] Produzir os 3 vídeos (fábrica de posts/Canva — fora do escopo desta thread)
- [ ] Betiato (opcional, não bloqueia): checkout live + estorno pra provar `Subscribe`
- [ ] Mídia Paga: subir estrutura **PAUSADA** → revisão do Rafael → ativação DELE

## 6b. Estratégia de mercado e idioma (REVISADA v2.2 — decisão do PO: alvo é global, criativo EN)

**Correção de rumo:** a v2.1 recomendava "BR primeiro, global depois". O PO corrigiu — **o objetivo do negócio é global**, e a direção de criativo EN foi decidida em outra thread. A tese global deve ser **testada**, não adiada. (Pricing em USD confirma a ambição global.)

**Não se escolhe BR ou global — escolhe-se EN + amplo internacional, e o Brasil se captura por mérito.** Com base morna no BR + CPM barato, o BR tende a se sobressair nos resultados junto de todos os outros mercados. Alcance global + eficiência BR na mesma campanha; o `tbl_user` (quebra por país) mostra a mistura real em vez de a gente adivinhar.

- **Criativo: inglês.** Os 3 reels em produção passam pra EN. A ideia de PT-diferenciação (gap BR-PT da Ads Library) é secundária à tese global — arquivada, não perseguida agora.
- **Targeting: amplo internacional.** Com ~$10/dia, o algoritmo acha o inventário que converte mais barato e evita o US caro sozinho (se autocorrige). Ler país no `tbl_user` → dobrar aposta na Fase 2.
- **Copy do anúncio: EN.**

**Caveats do global (medir, não temer):**
- **Diluição de país-lixo:** amplo mundial puxa cadastro barato de mercado que não paga $29 (ARPU baixo). Mitigação: país por cadastro no `tbl_user` → excluir os que inundam sem converter.
- **Política de poker por país:** alguns sinalizam criativo poker-adjacente. Aura está fora do escopo gambling (`compliance-meta.md`), mas esperar revisão manual esporádica.

**⚠️ Dependência de pricing (agora MAIS crítica no global):** produto cobra em USD. Branch `feature/stripe-brl-checkout` — confirmar deploy. Não bloqueia a Campanha 1 (cadastro free), mas bloqueia a Fase 2 de receita. No global, USD é nativo pra maioria; o BRL toggle serve o arm brasileiro.

**Pergunta aberta que define a facilidade do global:** a UI do produto é EN, PT ou ambos? UI só-EN → global é natural e a estratégia acima é limpa; UI PT → global exige localização de **produto**, não só de anúncio (e aí o BR volta a ser o arm mais forte no curto prazo).

## 7. Fase 2 (gatilho, não data)

Com **~100 cadastros limpos** acumulados (pago + orgânico):
1. LAL sobre **convertidos** (semente limpa)
2. Migrar otimização pra `CompleteRegistration` (volume viável)
3. Retargeting sobre os públicos de pixel (a essa altura com centenas de pessoas limpas)
4. Avaliar EN (mercado global sub-servido é oportunidade também — GTOWizard domina EN, mas ninguém tem o ângulo de dados populacionais)

---

**Regra absoluta:** nada disso ativa campanha nem gasta um centavo. Tudo sobe pausado; ativação é exclusivamente do Rafael.
