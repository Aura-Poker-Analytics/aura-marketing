# KPIs do Post de Lançamento — Dia 1

**Autor:** thread Mídia Paga · **Verificado ao vivo:** 2026-07-09 (manhã), ~17-19h após publicação
**Post:** "Aura 2.0 não foi um update..." — publicado 08/07/2026, 22:35, @aurapokeranalytics
**Método:** Chrome no Meta Business Suite (Insights do post + Insights da conta) + Events Manager do dataset `1405949840871947`. Sem MCP oficial da Meta (segue desconectado). **100% orgânico — nenhum boost/impulsão ativo**, conforme combinado.

---

## 1. Desempenho do post (Instagram)

| Métrica | Valor |
|---|---|
| Visualizações | 679 |
| Alcance (contas) | 225 |
| Interações líquidas | 17 |
| — Curtidas/reações | 14 |
| — Comentários | 2 |
| — Compartilhamentos | 1 |
| — Salvamentos | **0** |

**Leitura:** taxa de interação sobre alcance ≈ 7,5% (225→17), na média/acima da média pra Instagram. **Zero salvamentos é esperado** — é post de reveal/anúncio de marca, não um stat card (conteúdo denso de dado é o que puxa salvamento; ver a discussão de [launch-hero-trafego.md](launch-hero-trafego.md) sobre por que reveal ≠ criativo de conversão).

**Demografia do alcance:** 93,3% homens · faixa dominante 25-34 (50%) e 35-44 (35,3%) — bate com o ICP (grinder de MTT intermediário-avançado).

## 2. Conta (últimos 28 dias — na prática, = este post, conta estava parada há 60d)

| Métrica | Valor |
|---|---|
| Visualizações (conta) | ~1,1 mil |
| Alcance (conta) | 348 |
| Interações com conteúdo | 28 |
| Novos seguidores | 18 |
| **Deixaram de seguir** | **23** |
| Conversas iniciadas (DM) | 3 (2 novos contatos) |

⚠️ **Saldo de seguidores é levemente negativo** (18 ganhos − 23 perdidos ≈ −5), consistente com a queda observada de 710→706 seguidores. Normal em post de reveal/rebrand (alguém que seguia por um motivo específico sai quando o produto muda) — vale acompanhar se persiste nos próximos posts, mas não é motivo de alarme num N pequeno.

## 3. Sinal no site/pixel (Events Manager, dataset `1405949840871947`)

| Evento | Total | Última vez |
|---|---|---|
| PageView | 167 (+62 desde a última checagem) | há 1 hora |
| **Concluir inscrição (CompleteRegistration)** | **4 — evento NOVO, não existia antes** | **há 4 horas** |
| Iniciar finalização da compra (legado WooCommerce) | 6 | há 1 dia (inativo, esperado) |
| Adicionar ao carrinho (legado WooCommerce) | 5 | há 1 dia (inativo, esperado) |

**Achado importante:** o evento `CompleteRegistration` **está disparando de verdade** — a instrumentação (pelo menos a parte browser da Fase 1, possivelmente mais) já está no ar e capturando cadastro. Isso é adiantado em relação ao que eu sabia da última auditoria.

## 4. O que NÃO dá pra afirmar ainda (gap honesto)

- **Não consigo atribuir os 4 `CompleteRegistration` a ESTE post especificamente.** O Events Manager não quebra por origem/UTM nessa tela, e a landing ainda **não propaga UTM/fbclid** no CTA (gap já registrado em [status-cutover-verificado.md](status-cutover-verificado.md)). Sem isso, não dá pra separar "veio do post de ontem" de "veio de busca direta/outro canal".
- **Sem acesso ao AuraBusiness/Postgres** nesta sessão (Supabase MCP pede autorização; o Postgres do Azure MCP, mesmo se conectasse, historicamente bate no servidor legado, não no `aura-production` — ver `aura-context/docs/00-index/estado-atual.md`). O KPI norte de verdade (conta free por UTM) só fecha quando isso for resolvido.
- PageView subiu 62 na janela — correlação forte com o post (a conta estava sem postar há 60 dias), mas **correlação, não prova**.

## 5. Resumo pra decisão

Primeiro post de lançamento em conta que estava parada: **alcance/engajamento saudáveis pro tamanho da base, zero saves (esperado pro formato), leve perda de seguidores (observar), e — o mais importante — o pixel de cadastro já está vivo e pegando conversão real.** Nenhuma ação de mídia paga necessária agora; RTG segue aguardando GO + volume de visitantes conforme o plano. Prioridade técnica: fechar a propagação de UTM no CTA da landing pra próxima vez esse relatório vir com atribuição de verdade, não só correlação.
