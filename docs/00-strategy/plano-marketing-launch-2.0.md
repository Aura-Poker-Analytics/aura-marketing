# Plano de Marketing — Lançamento Aura 2.0

**Versão:** 2026-07-04 · **Owner:** Rafael (PO, aprova tudo) · **Autor:** QG estratégico (thread de marketing IA)
**Status:** GO parcial — repo e brand kit aprovados; conta bilíngue = recomendação em vigor salvo objeção; L = 10/07/2026.

---

## A. Estratégico (horizonte 90 dias)

**Posicionamento:** *Solvers te mostram o equilíbrio. A Aura te mostra o adversário.*
Ferramenta do jogador explorador — dados reais de 500M+ mãos do pool, não teoria.
Tagline de launch (herdada da apresentação de marca 2024): **"O MESMO JOGO — NOVAS INFORMAÇÕES."**

**Objetivo do trimestre:** funil mensurável IG → landing → **plano free** → assinatura.
KPI norte = **contas free atribuídas via UTM** (fundo do funil na AuraBusiness). Seguidor é vanity metric.

**Oferta (mudança 2026-07-04):** não existe mais trial 7d. O antigo trial vira **plano free permanente** com travas de usabilidade (demo). Isso melhora o CTA de IG: fricção menor ("crie sua conta grátis", sem relógio), e o upgrade acontece dentro do produto quando o usuário bate nas travas.

**ICP:** grinder de MTT intermediário-avançado que já estuda (solver/curso). Não precisa ser convencido a estudar — precisa ser convencido de que *estudar o pool > decorar o equilíbrio*.

**Mercados:** BR (base atual: 710 users, 100% BR) + EN (mesma persona, fora do BR).

**Decisão de conta/idioma:** manter **@aurapokeranalytics** e torná-la bilíngue.
- Arte em EN (vocabulário de poker é inglês: BTN, c-bet, MDF — lê nativo pro BR).
- Legenda PT-BR + EN condensado.
- Regra de revisão: se em 90 dias a audiência EN < ~15% E EN for prioridade comercial, criar @ EN dedicado com o acervo já validado. Separar depois é barato; fundir é impossível.
- Risco monitorado: Meta distribui por geografia da base (BR-pesada) → alcance EN cresce devagar no início. Mitigação: hashtags EN, colabs EN, Reels com áudio EN.

**Vantagem competitiva de conteúdo:** ninguém mais posta "o pool folda X% aqui" com amostra de milhões — concorrente posta range de solver. Cada stat post é demo do produto disfarçada de conteúdo.

## B. Tático

**Canal único até estabilizar: Instagram.** YouTube/X/Discord = pós-launch.

**Pilares:**
| # | Pilar | Peso | Formato principal |
|---|---|---|---|
| P1 | "O pool erra assim" — stat real + leitura exploratória | 30% | stat card 1080×1350 + story |
| P3 | Conceito em 60s — MDF, overfold, pool vs GTO | 25% | carrossel 5–7 slides |
| P2 | Feature spotlight — tela real + o que responde | 20% | card ou carrossel de 3 |
| P4 | Bastidores/launch — countdown, changelog humano | 15% | card + stories |
| P5 | Sessão de estudo com a Aura (proto prova-social) | 10% | carrossel 6–8 |

**Arco comprimido (L = 10/07/2026):**
| Fase | Datas | Tema | CTA |
|---|---|---|---|
| Teaser relâmpago | 06–09/07 | 1 stat forte/dia + countdown stories | seguir/salvar |
| Launch week | 10–17/07 | 2.0 no ar + features, ~1 post/dia | **conta grátis — link na bio** |
| Sustentação | 18/07+ | 3 posts/semana (P1+P3 core) + P5 | conta grátis (soft) |

**Plano B:** se a landing atrasar, a launch week desliza junto; o teaser não depende dela.

**Caminho crítico:** 04–05/07 aprovação plano+templates → 06/07 lote teaser no ar → 07–09/07 produção launch week.
⚠️ Dados: fix fold/raise (24aed77) sem deploy → números saem do **banco direto** (`frequency_nextaction_1/2/3` = fold/raise/call, canônico).

**Tráfego pago = fase 2.** Orgânico valida criativos (30–45d) → Pixel/CAPI na landing → 1º real em retargeting (quente, barato) → só depois lookalike. ⚠️ Policy Meta real-money gaming: SaaS de estudo tem bom argumento, mas exige doc próprio antes do 1º gasto. Budget inicial sugerido: R$30–50/dia.

**Analytics:** IG Insights (alcance/saves/cliques bio) → GA4 na landing (UTM: `utm_source=instagram&utm_medium=organic&utm_campaign=launch20`) → AuraBusiness (contas free + upgrades). Auditoria do GA4 existente = tarefa da semana do launch.

## C. Operacional

**Arquitetura de "equipe de marketing IA" — papéis, não threads:**
- **QG estratégico (thread persistente #1):** estratégia, calendário, aprovações, review semanal, docs. Não produz arte em escala.
- **Fábrica de posts (thread persistente #2, neste repo):** recebe calendário+templates aprovados e roda Workflow por lote. Os "especialistas" são subagentes efêmeros por post: *analista de dados* (puxa e valida o número), *copywriter* (PT+EN), *designer* (render HTML→screenshot), *QA de compliance* (checklist §Compliance). Nascem por lote, morrem no fim — o conhecimento fica nos docs deste repo, não na memória de agente.
- **Mídia paga (thread #3, futura):** só quando ativar tráfego pago.
- **Rafael:** aprova post a post e publica/agenda no Meta Business Suite (~20min/semana). Nenhum agente publica nada, nunca.

**Por que não N agentes persistentes "funcionários":** não compartilham memória entre si, exigem re-briefing constante, coordenam por arquivos de qualquer jeito, e o gate humano é o Rafael. Papéis codificados em prompts de Workflow + docs = mesma especialização, zero overhead de coordenação. Este repo é o "manual do funcionário": qualquer sessão nova fica onboarded lendo `AGENTS.md` + `docs/`.

**Fluxo semanal em regime:**
seg: QG propõe semana → Rafael aprova → fábrica produz → Rafael revisa e agenda tudo → sex: QG lê Insights+AuraBusiness → review e ajuste de rota.

**Regra de ouro dos números:** todo stat puxado na hora de fonte verificada (banco direto ou API pós-fix). Sem verificação → rotular "ilustrativo" ou não sai.

## Compliance (checklist de QA por post)
- [ ] Sem promessa de ganho financeiro / renda / "lucro garantido"
- [ ] Sem imagem de dinheiro/luxo clickbait
- [ ] 18+ visível onde couber
- [ ] Nenhum nome/dado de cliente ou jogador identificável; nenhum email/conta em screenshot
- [ ] Sem comparativo nominal com concorrente
- [ ] Número verificado na fonte + rodapé de amostra ("dados: Aura · amostra de X mãos")

## Pendências
- [ ] Confirmação final do Rafael: conta bilíngue na @aurapokeranalytics
- [ ] Templates HTML (gate de aprovação visual)
- [ ] Lote teaser (gate post a post)
- [ ] Auditoria IG (perfil/insights via Chrome) + 73 artes do Canva ("AURA - Posts")
- [ ] Auditoria GA4 + eventos de conversão da landing nova
- [ ] Doc de tráfego pago (fase 2)
