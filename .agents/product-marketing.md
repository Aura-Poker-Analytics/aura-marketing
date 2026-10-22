# Product Marketing Context — Aura Poker Analytics

**Document version:** v2
**Last updated:** 2026-10-22
**Mantido por:** sessão `aura · plano de marketing` · formato da skill `product-marketing` (coreyhaines31/marketingskills)
**Fontes, em ordem de confiança:** (1) decisões do Rafael de 22/10 (`docs/00-strategy/entendimento-compartilhado-2026-11.md`); (2) Stripe, GA4 e Meta lidos em 22/10; (3) `aura-main/STATE.md` e o `copy.md` do Modo GTO (regras de 15/10). Os docs de jul–set (`product-truth-aura.md`, `docs/02-paid/*`) são só pista: o Rafael disse em 22/10 que "foram construídos PORCAMENTE".

> Confiança: ✅ verificado · 🟡 inferido de material interno · 🔴 lacuna, nunca pesquisado com cliente.
> ⚠️ O `product-truth-aura.md` de 09/07 diz que a Aura "não compara com GTO". Isso deixou de valer: desde 01–15/10 o GTO está no produto (Modo GTO, Field vs GTO) e o Pool vs GTO entra em 02/11. Para claims de GTO, a fonte é o `copy.md` do Modo GTO e os `numeros-verificados` do aura-main.

## Product Overview ✅
**One-liner:** O que o field de MTT realmente faz, ao lado do GTO, spot a spot.
**What it does:** Mede as frequências reais da população de MTT online (pré-flop, pós-flop, nó a nó) e, desde out/2026, mostra o número GTO e a faixa GTO ao lado do field. O jogador vê onde o field se afasta do GTO e como explorar.
**Product category:** inteligência de field de MTT (PT "inteligência de field", EN "field intelligence"). Não é tracker (não mostra o resultado do herói) nem solver (não resolve spots; usa referência GTO pronta).
**Product type:** SaaS web (app em `www.aura.poker`, landing em `www.aurapoker.com`).
**Business model:** freemium.
- Grátis: sem cartão, com amostra de cada módulo e uma amostra do GTO.
- Individual: R$ 150/mês ou US$ 29/mês; US$ 149 por semestre; US$ 259 ou R$ 1.295 por ano.
- O Modo GTO está incluso no Individual por tempo limitado.
- Planos GTO e Top estão criados no Stripe, sem lançamento.
- **Team Mode será aposentado** (decisão de 22/10). O B2B passa a ser o pacote de contas por volume e o relatório por encomenda.

**Módulos no ar:** Preflop Analysis, Postflop Analysis (com showdown value), Hotspot, Node-by-Node, Field Ranges (com Field vs GTO), Field Trends, Modo GTO (flop, turn e river) e Pool vs GTO (a flag liga em 02/11: 8 spots novos em 02/11 e mais 8 em 09/11; o Grátis vê 1).

## Target Audience
**Target:** grinder de MTT online intermediário a avançado, que já estuda (solver, curso ou coach), com buy-ins de ~US$ 11 a 215. 🟡
**Decision-makers:** o próprio jogador (B2C); no B2B, o head coach ou o dono do time ou stable.
**Primary use case:** saber onde o field do seu buy-in erra contra o GTO e o que fazer diferente.
**Jobs to be done:** 🟡
- Priorizar o que estudar primeiro (onde o desvio é maior e mais frequente).
- Ajustar a estratégia ao field real, além do equilíbrio.
- (coach) Mostrar ao aluno, com dado, como o field joga um spot.

**Mercados (decisão de 22/10):**
- A aquisição B2C principal é em inglês: Reino Unido, Canadá, Alemanha, Holanda, Áustria e nórdicos. Os EUA ficam fora.
- O Brasil entra por coaches e B2B. Motivo, nas palavras do Rafael: o mercado de regs brasileiro "está muito concentrado em times, fica dificil dessas pessoas assinarem".

## Personas
| Persona | Cares about | Challenge | Value we promise |
|---|---|---|---|
| Grinder que estuda (B2C, EN) | subir de buy-in, estudar com foco | o solver dá o equilíbrio, mas não diz onde o field desvia | os spots onde o field se afasta do GTO, com o exploit |
| Head coach (BR e EN) | material de aula com dado, reputação | explicar o field ao aluno sem dado próprio | o field e o GTO na tela, comissão de 30% por aluno |
| Dono do time ou stable (B2B) | resultado do time, custo por jogador | padronizar o estudo do time | pacote de contas com desconto e relatório do field do time |

🔴 Nenhuma persona foi validada com entrevista. Os head coaches que já assinam (gremistaak, Paulo Moraes, Ganso e outros) são a primeira fonte de entrevista.

## Problems & Pain Points 🟡
**Core problem:** o jogador estuda equilíbrio, mas joga contra um field que não está em equilíbrio, e não sabe onde está a diferença.
**Why alternatives fall short:**
- O solver mostra o ótimo teórico, não o adversário.
- O tracker mostra a amostra do próprio jogador, pequena demais para ler a população.
- O coach mostra a leitura dele, sem dado de população em escala.

**What it costs them:** horas de estudo em spots que pouco importam contra o field real. 🔴 Não confirmado com cliente.
**Emotional tension:** 🔴 lacuna.

## Competitive Landscape ✅ (Ads Library, 07/2026)
**Direct:** nenhum vende dado de população de MTT ao lado do GTO.
**Secondary:**
- GTO Wizard e solvers: vendem equilíbrio. A referência interna de convenção nunca é citada em peça.
- Railbird, Drivehud e trackers: amostra própria.

**Indirect:** coaching e staking (times brasileiros como Gigantes, Nit e RPT). No Brasil, esses times são o canal, não o concorrente.

## Differentiation ✅
- Única ferramenta com o field medido e o GTO lado a lado, spot a spot.
- Recortes que o solver não modela: etapa do torneio, tipo (Regular, KO, Mystery), perfil do adversário (reg ou fish).
- Pool vs GTO: uma lista semanal dos spots onde o field mais se afasta do GTO, cada um com o exploit.

**Why customers choose us:** 🔴 nunca perguntado. A hipótese é "economiza tempo de estudo e diz o que explorar".

## Objections 🔴 (hipóteses; validar nas entrevistas com coaches)
| Objection | Response |
|---|---|
| "Já pago solver" | O solver dá o equilíbrio; a Aura mostra onde o field se afasta dele. Os dois se complementam. |
| "Dado de população não me diz o que fazer neste spot" | O Pool vs GTO e o Modo GTO mostram o desvio do field no spot, contra o GTO, com a faixa. |
| "O dado representa os torneios que eu jogo?" | Filtros por buy-in, etapa e tipo de torneio. Nunca citar a proporção por sala. |
| "Mais uma ferramenta para aprender" | 🔴 sem resposta. A ativação é o maior vazamento medido. |

**Anti-persona:** jogador de cash game, jogador casual ou de app social, quem procura promessa de lucro, e o público de bets (o pago frio no Instagram Brasil entregou para esse público).

## Switching Dynamics 🔴
**Push:** 🔴 não pesquisado.
**Pull:** dado novo (field ao lado do GTO), lançamentos frequentes.
**Habit:** o jogador já tem rotina de estudo com solver ou coach. Por isso o coach é o melhor canal: a Aura entra na rotina que já existe.
**Anxiety:** confiança no dado e tempo para aprender. Resposta: intervalo e amostra em cada número, e o texto curto na tela.

## Customer Language 🔴
**Problem (verbatim):** nenhum coletado. Fonte prevista: entrevistas com coaches e pagantes, e comentários do Paulo "Galator" (19/10), que geraram o projeto de legibilidade.
**Words to use:** termos de poker em inglês nas duas línguas (c-bet, delayed c-bet, RFI, 3-bet, overfold, overdefend, field, spot, range); "a Aura" (feminino); em PT, porcentagem com vírgula.
**Words to avoid:**
- "ponte" (proibida em qualquer lugar);
- "pp" na tela (usar "%");
- "solver" e "size" em texto PT do app;
- "pool" no lugar de "field" em copy;
- jargão de bastidor (snapshot, cube, n mínimo);
- selo de desconfiança ("leia com desconfiança");
- "c-bet atrasada" (usar "delayed c-bet");
- promessa de lucro, EV ou winrate.

**Glossary:**
| Term | Meaning |
|---|---|
| Field | a população de jogadores medida |
| Faixa GTO | o intervalo do número GTO; o desvio se mede até o topo ou a base da faixa |
| Overfold / Overdefend | o field folda ou defende mais do que a faixa GTO |
| Modo GTO | o número e a faixa GTO ao lado do field, no flop, turn e river |
| Pool vs GTO | lista semanal dos spots com maior desvio, com o exploit |

## Brand Voice ✅
| Attribute | Means | Doesn't mean | Example line |
|---|---|---|---|
| De reg para reg | técnico, termos de poker em inglês | professoral, didático demais | "When villain calls, bluff less and bet mostly for value on the flop." (aprovada pelo Rafael, 08/10) |
| Diagnóstico e ação | diz o desvio e o que fazer | justificar a teoria | "Aqui o field folda mais do que o GTO." |
| Honesto com o dado | "É um spot, não a média do field" | selo de desconfiança ou bastidor técnico | "Confira no seu board." |
| Pouco texto | arte com título curto e no máximo uma linha | parágrafo em arte | título de ~6 palavras e apoio de ~10 |

**Tone by context:**
- Lançamento: data e o que mudou; "por tempo limitado" só para a inclusão do GTO.
- E-mail: CTA sempre para a landing `www.aurapoker.com`.
- Social: carrossel em EN com legenda bilíngue; capa PT só como story.
- Erros e app: curto, sem bastidor.

**Never use (and why):** "bilhões" e "500M+ mãos" (sem proveniência); "todas as situações" e "todos os spots" para a cobertura do GTO (ela é parcial); cadência de atualização ("toda semana", "todo mês") para a cobertura do GTO; depoimento fictício.

## Proof Points
**Metrics:**
- "Mais de 400 mil torneios" (landing, nota de metodologia).
- "Mais de 2.100 spots de flop" com GTO (snapshot de 15/10; a data acompanha o snapshot).
- Números de spot só a partir dos `numeros-verificados` do aura-main.

**Customers:** 16 pagantes ativos (22/10). Head coaches assinantes: gremistaak, Paulo Moraes, Ganso. 🔴 Nenhum autorizou ainda o uso do nome; pedir junto com a proposta de parceria.
**Testimonials:** 🔴 nenhum real. A meta da parceria com coaches inclui depoimento.

## Goals ✅ (decididos em 22/10)
**Business goal:** 45 pagantes ativos até 31/01/2027, saindo de 16. Alvo esticado: 60. Abaixo de 30, reabre a conversa de pivô para concierge/B2B.
**Conversion action:** assinatura do Individual (`purchase`). Cadastro e seguidor são métricas de apoio.
**Current metrics:**
| Métrica | Valor |
|---|---|
| Pagantes ativos (22/10) | 16 (Stripe 9, Woo 5, NOWPayments 2) |
| MRR no Stripe | ~R$ 708 + US$ 109 |
| Visitantes novos em 90 dias (GA4) | 1.824 |
| Cadastros em 90 dias | 40 (2,2% dos visitantes novos) |
| Ex-pagantes no Stripe | ~32 |

## Paid Ads
**Target CPA:** decidir por custo por assinante, não por cadastro. Referência histórica: ~R$ 75 por cadastro na DISC02-EU.
**Hard floor:** cortar a célula que não trouxer assinante dentro da verba dela.
**Monthly budget:** teto de R$ 1.500 em 60 dias, só depois de a medição estar consertada.
- R$ 1.050 na DISC02-EU reeditada;
- R$ 300 em remarketing;
- R$ 150 na célula "Esportes" em inglês.

**Conversions that count:**
| Action | Means | Value | Feeds bidding? |
|---|---|---|---|
| CompleteRegistration / `sign_up` | cadastro | apoio | sim, até haver volume de compra |
| Subscribe / `purchase` | assinatura | principal | sim, quando houver volume |

**Known tracking weaknesses:**
- `begin_checkout` e `purchase` só existem desde 21–22/10.
- O `purchase` pelo servidor ainda não existe.
- O `fbp` e o `fbc` não vão no CompleteRegistration.
- A qualidade de correspondência do evento está entre 5 e 6,1.
- O page_view no GA4 conta duas vezes até o Rafael desligar a medição otimizada.

**Campaigns:**
- DISC02-EU: cadastro na Europa em inglês. A única que gerou cadastro.
- As outras estão pausadas.

**Agent may:** ler, comparar, sinalizar, rascunhar, recomendar.
**Agent may not (without approval):** mudar verba, pausar ou lançar, editar rastreio, publicar anúncio.

## Learnings
| Date | Learning | Evidence | Applies to | Status |
|---|---|---|---|---|
| 2026-10-22 | O B2C no Brasil é difícil porque os regs estão nos times; adquirir via coaches e B2B | decisão do Rafael | todos os canais BR | active |
| 2026-10-22 | 4 dos 9 pagantes do Stripe pagam em USD de fora do Brasil, sem esforço dirigido | Stripe, 22/10 | mercado EN | watch |
| 2026-10-22 | DISC02-EU é a única campanha com cadastro: 8 por R$ 603,80 | Meta Ads MCP, 22/10 | ads EN | watch |
| 2026-10-22 | Dos 102 que começam o cadastro, 40 terminam em 90 dias | GA4, 22/10 | signup, cro | active |

> **Docs de jul–set não são prova (Rafael, 22/10: "foram construídos PORCAMENTE").** O que vem de `docs/02-paid/*`, `product-truth-aura.md` e da v1 deste contexto só entra como hipótese a reconferir no dado. Ficam como pistas, sem status active:
> - pago frio no Instagram Brasil entregando para público de bets (`plano-fuga-das-bets.md`);
> - DISC02-EU morta por troca de configuração (`PLAYBOOK` §8.6);
> - otimização por PROFILE_VISIT com público errado;
> - cupom AURAVOLTOU com 0 resgates;
> - post de spot com CTR de 12,85%.
| 2026-10-08 | Arte com muito texto é rejeitada: um título curto e no máximo uma linha | Rafael, 08/10 | social, ad-creative | active |

## Changelog
- v2 (2026-10-22) — Reposicionamento: a Aura agora mostra o GTO ao lado do field (Modo GTO, Field vs GTO, Pool vs GTO), o que derruba o "não compara com GTO" da v1. Mercado B2C passa a ser o inglês; Brasil via coaches e B2B; Team Mode aposentado. Metas de 22/10, pagantes medidos, "500M+ mãos" retirado das provas, seção Paid Ads e Learnings criadas.
- v1 (2026-07-29) — Contexto inicial da thread Mídia Paga (branch `feature/descoberta-reels-v2`), com três lacunas críticas: objeções, switching dynamics e linguagem do cliente.
