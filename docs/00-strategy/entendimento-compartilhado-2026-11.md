# Entendimento compartilhado: plano de marketing da Aura (nov/2026)

**Sessão:** `aura · plano de marketing · grill-me` · **Início:** 22/10/2026
Registro da fase 0 (entrevista). Fatos levantados por subagentes, só leitura; decisões do Rafael anotadas com as palavras dele.

## Fatos de partida (22/10/2026)

### Funil medido (GA4, property 506294082, até 21/10)

| Etapa | 90 dias | 28 dias |
| --- | --- | --- |
| Visitantes novos (`first_visit`) | 1.824 | 106 |
| Começaram o cadastro (`form_start`, usuários) | 102 | 30 |
| Cadastros (`sign_up`) | 40 | 6 |
| Usaram o produto (`analyze_result`, usuários) | 40 | 22 |
| Bateram no paywall (`gate_hit`, usuários) | 23 | 12 |
| Clicaram em upgrade (`upgrade_click`, usuários) | 9 | 6 |
| Checkout e compra | sem medição: `begin_checkout` e `purchase` entraram no ar em 21–22/10 | |

- Tráfego de 90 dias: Paid Social 1.357 sessões, Direct 539, Organic Search 183, Organic Social 100, Referral 97, Email 82. Com o pago pausado, os últimos 28 dias têm cerca de 265 sessões.
- **Pagantes no Stripe live (22/10, leitura pela API; o Sigma não está contratado):**

  | Ativas | Plano | Quantas |
  | --- | --- | --- |
  | Em BRL | mensal R$ 150 | 4 |
  | Em BRL | anual R$ 1.295 | 1 |
  | Em USD | mensal US$ 29 | 3 (uma com cancelamento marcado) |
  | Em USD | anual US$ 259 | 1 |

  - Total de ativas: **9**. MRR de cerca de R$ 708 mais US$ 109.
  - Por país: Brasil 5, Portugal 3, Uzbequistão 1.
  - Novas por mês: jul 4, ago 3, set 2, out 3. Cancelamentos: 2 em agosto.
  - Já pagaram nos últimos 12 meses **44 clientes** (41 sem os reembolsados), e só 9 seguem ativos. Ou seja, cerca de 32 ex-pagantes podem ser reconquistados.
  - Não conferido: se ainda existem pagantes legados do Woo fora do Stripe. Em 18/07 eram 8, com MRR de R$ 1.410 (`_strategy/aura.md`).

### Mídia paga (Meta, conta Aura Business)

- Gasto total histórico de cerca de R$ 1.771, distribuído em 7 campanhas. Só a DISC02-EU (cadastro, Europa em inglês) está ativa: 8 cadastros por R$ 604, cerca de R$ 75 cada.
- O público "poker" no Instagram Brasil frio está tomado por bets: tempo de sessão de 0,1 a 2,7 s, contra 90 a 200 s do tráfego não pago na mesma página (`docs/02-paid/plano-fuga-das-bets.md`, 12/08).
- O pago para a Europa em inglês foi o único que gerou cadastro. A campanha morreu ao ter a configuração trocada três vezes em 14 dias (`PLAYBOOK-midia-paga-do-zero.md` §8.6).
- Instagram: o tempo médio de engajamento por sessão foi 98,7 s vindo da bio, 15,6 s no pago da Europa e 0,2 a 2,7 s no pago frio do Brasil. Conclusão do doc de 31/08: o Instagram é meio de funil, não topo.
- Teto anterior de mídia: R$ 1.500, com cerca de R$ 1.161 gastos até 14/09.
- O impulsionamento com interesse "Esportes", lembrado pelo Rafael, **não está documentado em lugar nenhum**.

### Outros fatos

- **Base de e-mail:** algumas centenas de contatos, com segmentos de 174 e 192. Foram 9 broadcasts desde 30/07, o último o lançamento do Modo GTO (21/10, 250 entregues).
- **Preço:** Individual por R$ 150, R$ 745 e R$ 1.295 (BRL), ou US$ 29, US$ 149 e US$ 259. Os planos Modo GTO e Top estão criados no Stripe, com lançamento pendente.
- **Gatilho de pivô do blueprint** (18/10, ≥ 200 signups e < 2% de conversão e nenhuma stable fechada levam a concierge/B2B): **a data passou e ninguém avaliou.**
- **Contradições abertas nos docs:**
  - o cupom D21 aparece como 50% num documento e 75% em outro;
  - a causa do público ruim (evento de otimização ou pool de bets);
  - o papel do pago (desligado ou Search mais EN).

## Rodadas

### Rodada 1 (22/10): decidida

| # | Decisão | Fonte |
| --- | --- | --- |
| Q1 | Métrica principal: **assinantes pagantes ativos**, prazo 31/01/2027. Cadastro e seguidor são métricas de apoio. A meta numérica sai da base atual (rodada 2). | Rafael: "restante todo de acordo" |
| Q2 | **Internacionalizar já.** O mercado principal de aquisição passa a ser o inglês. | Rafael: "a impressao que eu tenho é que o mercado de regs brasileiro está muito concentrado em times, fica dificil dessas pessoas assinarem infelizmente. Estava pensando em tentar internacionalizar já." |
| Q3 | Verba nova só depois do rastreio consertado. Teto de R$ 1.500 nos 60 dias, com corte por custo por assinante. A divisão entre células é refeita na rodada 2 por causa da Q2. | Rafael: de acordo |
| Q4 | 3 h/semana do Rafael: 1 h para aprovar lotes e 2 h para gravar 2 ou 3 vídeos curtos. Sem lives no início. | Rafael: de acordo |
| Q5 | Parcerias com coaches e times, com cupom ou comissão por assinante, mais o Discord próprio. YouTube longo depois dos 90 dias. | Rafael: de acordo |
| Q6 | Escopo: só a Aura. Os lançamentos (Pool vs GTO em 02/11, Modo GTO) entram como ganchos. | Rafael: de acordo |
| Q7 | Plano segue, com gatilho novo: se a meta da Q1 não for atingida em 31/01/2027, reabrir a conversa de concierge/B2B. O canal de parceiros testa o B2B em paralelo. | Rafael: de acordo |

### Rodada 2 (22/10): em andamento
