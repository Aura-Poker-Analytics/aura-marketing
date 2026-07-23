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

**Decisão 4 — estrutura por idioma×geo (v2.3, decisão do PO: PT→BR, EN→resto).** Usa os reels PT já prontos no arm quente (BR) e serve a tese global no arm EN, com a economia dos dois **medida em separado**.

```
Campanha: AURA-PAID01 — Tráfego, budget por conjunto (ABO)
│
├── Conjunto A — BR/PT     (R$25/dia)
│     Criativos: 3 reels PT (prontos, content/paid/AURA-PAID01) + orgânicos PT c/ prova social
│     Geo: Brasil + Portugal · Idade 20–45 · só Instagram · Excl: cassino/apostas/bingo
│
└── Conjunto B — Intl/EN   (R$25/dia)
      Criativos: 3 reels EN (a renderizar) + orgânicos EN c/ prova social
      Geo APERTADO no início: GB, CA, AU, DE, NL, IE, NZ, SE, NO, DK, FI
        (BR/PT EXCLUÍDOS — são do conjunto A; alargar p/ ES/IT/PL/MX/AR/CL com dado)
      Excl: cassino/apostas/bingo
```

**Sem sobreposição de geo** entre A e B (senão competem entre si). **Gates rodam por conjunto** → custo/cadastro BR vs internacional em separado (responde "o global é viável ou só o BR converte?"). 

Trade-off honesto: R$50/dia dividido = cada arm aprende mais devagar; o **arm EN é o ponto fraco** (R$25 em países caros). Mitigação: lista EN apertada no início + paciência (ou mais budget). Realocar budget entre A e B no D14 conforme custo/cadastro.

Otimização: **cliques no link / LP views** (ambos). Nada de Advantage+ expansion, Audience Network, Messenger.
2º nível (só se um arm vier sujo no D3): LAL worldwide sobre base limpa (§5b) ou interesses específicos (solvers/trackers, nunca "poker" isolado).

Otimização: **cliques no link / visualizações da LP** (não conversão — volume insuficiente pra sair do aprendizado). Rede de segurança: como cada criativo tem UTM próprio e o cadastro grava no `tbl_user`, clique-lixo é detectado pelo dado real (clica mas não cadastra), não pela métrica da Meta.
Nada de Advantage+ audience expansion. Nada de Audience Network/Messenger.

## 3. Os 3 criativos (vídeo vertical 9:16, 15–30s)

> **STATUS 2026-07-22:** os 3 reels foram ENTREGUES pela fábrica em `content/paid/AURA-PAID01/` (9:16, ~18s, sem áudio, thumbs). Bem feitos, guard-rails conferidos. **Dois pontos:**
> - A fábrica **corrigiu erros de product-truth do brief original** (abaixo): V1 não usa "solver diz 48%" (número inventado + overlay que a Aura não faz) → usa reg agressivo 50% vs tight 35% (real); V3 não usa "seu redline" (Aura não vê suas mãos) → "o leak é do field". Os ganchos na tabela abaixo são os do brief antigo; **valem os do README entregue**.
> - Estão em **PT** (feitos sob v2.1). Pivô v2.2 → precisam de **versão EN** pro alvo global (copy EN das cenas já redigida, fiel às versões corrigidas — render é trocar chaves em `deck.js` + `build-paid.mjs`). **Os PT viram o arm BR/Portugal**, não são descartados.

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

- [x] Rafael: **2FA feito** + **verificação da empresa solicitada** (aguardando veredito da Meta) — 2026-07-22
- [~] Vertical do negócio: campo não é editável na UI (Meta infere pela categoria da Página, que já é "Software"). Item **encerrado** — efeito marginal, sem ação possível direta
- [ ] Rafael: método de pagamento (só no GO)
- [ ] Produzir os 3 vídeos (fábrica de posts/Canva — fora do escopo desta thread)
- [ ] Betiato (opcional, não bloqueia): checkout live + estorno pra provar `Subscribe`
- [ ] Mídia Paga: subir estrutura **PAUSADA** → revisão do Rafael → ativação DELE

## 6b. Estratégia de mercado e idioma (REVISADA v2.2 — decisão do PO: alvo é global, criativo EN)

**Correção de rumo:** a v2.1 recomendava "BR primeiro, global depois". O PO corrigiu — **o objetivo do negócio é global**, e a direção de criativo EN foi decidida em outra thread. A tese global deve ser **testada**, não adiada. (Pricing em USD confirma a ambição global.)

**Não se escolhe BR ou global — escolhe-se EN + amplo internacional, e o Brasil se captura por mérito.** Com base morna no BR + CPM barato, o BR tende a se sobressair nos resultados junto de todos os outros mercados. Alcance global + eficiência BR na mesma campanha; o `tbl_user` (quebra por país) mostra a mistura real em vez de a gente adivinhar.

- **Criativo: inglês.** Os 3 reels em produção passam pra EN. A ideia de PT-diferenciação (gap BR-PT da Ads Library) é secundária à tese global — arquivada, não perseguida agora.
- **Targeting: amplo, mas com LISTA DE PAÍSES de mercados reais de poker** (decisão do PO — "amplo internacional" ≠ "mundo inteiro"; trava o floor contra país-lixo sem mercado de poker). O criativo com jargão filtra *dentro* da lista (filtro duplo geo+jargão). Lista de partida (refinada pelo custo/cadastro por país no `tbl_user`):
  - **Core (dia 1):** BR, CA, DE, GB, NL, SE, NO, DK, FI, AT, IE, AU, NZ, PT, ES, IT, PL, CZ, RO, MX, AR, CL.
  - **Opt-in do PO (não-lixo, caso à parte):** 🇺🇸 US (maior/mais rico, mas CPM caro + casa do GTOWizard → recomendo começar SEM, adicionar com criativo vencedor + budget); 🇮🇳 Índia (mercado grande mas ARPU baixo → fora do 1º teste).
  - UI bilíngue (EN+PT) confirmada pelo PO → global é "localizar anúncio", não produto. Reforça a tese.
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
