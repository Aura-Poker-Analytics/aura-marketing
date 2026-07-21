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

## 2. Estrutura proposta

```
Campanha: AURA-PAID01-CLIQUES (objetivo: Tráfego)
│   Orçamento por conjunto (ABO) — garante gasto nos dois braços do teste
│
├── Conjunto A — "Interesses específicos"  (R$25/dia)
│     Interesses: PokerStars, GGPoker, trackers/solvers, mídia do circuito
│       (conferir disponibilidade real no construtor)
│     Exclusões: cassino, apostas esportivas, bingo, jogos de azar
│     ❌ NUNCA o interesse "poker" isolado
│     Geo: BR · Idade: 20–45 · Posicionamentos: só Instagram (Reels/Stories/Feed)
│
└── Conjunto B — "Amplo + criativo-filtro"  (R$25/dia)
      Sem interesses (amplo), mesmas exclusões demográficas/geo
      Hipótese: o jargão do criativo filtra melhor que a taxonomia contaminada
      (foi o mecanismo real do vencedor histórico)
```

**Cada conjunto recebe os mesmos 3 criativos** — o leilão mata as peças fracas.

Otimização: **cliques no link / visualizações da LP** (não conversão — ~15 conv/semana não sai do aprendizado; limiar é ~50).
Nada de Advantage+ audience expansion. Nada de Audience Network/Messenger (exclusão explícita).

## 3. Os 3 criativos (vídeo vertical 9:16, PT-BR, 15–30s)

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

## 7. Fase 2 (gatilho, não data)

Com **~100 cadastros limpos** acumulados (pago + orgânico):
1. LAL sobre **convertidos** (semente limpa)
2. Migrar otimização pra `CompleteRegistration` (volume viável)
3. Retargeting sobre os públicos de pixel (a essa altura com centenas de pessoas limpas)
4. Avaliar EN (mercado global sub-servido é oportunidade também — GTOWizard domina EN, mas ninguém tem o ângulo de dados populacionais)

---

**Regra absoluta:** nada disso ativa campanha nem gasta um centavo. Tudo sobe pausado; ativação é exclusivamente do Rafael.
