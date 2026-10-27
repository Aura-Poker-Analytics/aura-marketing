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
| Q6 | Escopo: só a Aura. Os lançamentos (Field Exploits em 02/11, Modo GTO) entram como ganchos. | Rafael: de acordo |
| Q7 | Plano segue, com gatilho novo: se a meta da Q1 não for atingida em 31/01/2027, reabrir a conversa de concierge/B2B. O canal de parceiros testa o B2B em paralelo. | Rafael: de acordo |

### Rodada 2 (22/10): decidida, com três pontos reabertos

| # | Decisão | Fonte |
| --- | --- | --- |
| Q8 | Países em inglês primeiro: Reino Unido, Canadá, Alemanha, Holanda, Áustria e nórdicos. Fora os EUA. Espanhol depois. | Rafael: "Restante gostei muito!" |
| Q9 | **O Team Mode como ferramenta será aposentado** (o time sobe os próprios dados). O B2B continua, mas por outro caminho (rodada 3). | Rafael: "vamos aposentar o team mode como ferramenta (em que o time upa seus dados etc). pensar em outra estratégia pra entrar pelo B2B...?" |
| Q10 | Conta única @aurapokeranalytics, feed em inglês e stories em PT. Revisão em 90 dias. | Rafael: de acordo |
| Q11 | Preço mantido nos 90 dias. Teste de 7 dias do pago só com cupom de parceiro. | Rafael: de acordo |
| Q12 | Orgânico em inglês: coaches com comissão de 30%, X/Twitter, Reddit (r/poker, r/MTT) e shorts no YouTube. Sem 2+2. | Rafael: de acordo |
| Q13 | Verba: R$ 1.050 na DISC02-EU reeditada, R$ 300 em remarketing e R$ 150 na célula "Esportes". | Rafael: de acordo (a célula depende da Q14) |
| Q14 | Os posts do impulsionamento antigo foram achados no histórico do Instagram. O público aparece só como "pessoas que você escolhe por meio de direcionamento", sem detalhe. | Rafael |
| Q15 | 25 ativos em 14 semanas é **"excessivamente conservador"**. Meta refeita na rodada 3. | Rafael |
| Q16 | Reconquista dos ex-pagantes como primeira ação: 50% no primeiro mês, válida por 14 dias, disparo junto com o Field Exploits em 02/11. | Rafael: de acordo |

**Base corrigida pelo Rafael (22/10):** além das 9 do Stripe, há **5 assinantes no WooCommerce** (frente fechada para entradas novas) e **2 no NOWPayments**. Total de **16 pagantes ativos**.

**Fora do escopo do plano, registrado para o produto:** aposentar o Team Mode afeta a landing (card "Team, fale conosco"), o app e o `STATE.md` do aura-main (§1 lista o Team Mode em produção). Isso precisa de uma sessão própria no aura-main e no aura-landing.

### Rodada 3 (22/10): decidida, Q17 sem resposta

| # | Decisão | Fonte |
| --- | --- | --- |
| Q17 | Meta proposta: 45 ativos (60 esticado), saindo de 16. **Sem resposta**, reperguntada na rodada 4. | (aberta) |
| Q18 | B2B por três caminhos: **(a) pacote de contas por volume, (c) relatório do field por encomenda e (d) licença ou comissão para coaches.** Head coaches que já assinam a Aura são a porta de entrada: gremistaak, Paulo Moraes, Ganso, entre outros. | Rafael: "Q18 a) c) e d). Temos alguns head coaches que ja assinam a plataforma. Como o gremistaak, paulo moraes, ganso, etc." |
| Q19 | O Rafael olhou a segunda conta de anúncios. O impulsionamento foi feito pelo botão do Instagram, e ele acha que isso não deixa rastro no Meta Ads. | Rafael |

### Rodada 4 (22/10): decidida

| # | Decisão | Fonte |
| --- | --- | --- |
| Q17 | **Meta: 45 pagantes ativos em 31/01/2027** (saindo de 16). Alvo esticado: 60. Abaixo de 30, reabre a conversa de pivô. | Rafael: "Restante ok" |
| Q20 | Coaches: conta paga grátis enquanto parceiro, 30% recorrente por 12 meses sobre os assinantes do cupom, 7 dias de teste para o aluno; em troca, uso em aula e depoimento. O Rafael faz o primeiro contato; eu preparo a proposta de uma página. **Sem kit de aula.** Controle manual por cupom do Stripe até 10 coaches. | Rafael: "o kit de aula nao precisa. restante ok" |
| Q21 | Relatório do field por encomenda: os 10 maiores desvios do field contra o GTO no buy-in e nas salas do time, entregue em 5 dias úteis. O primeiro é grátis para o time de um coach parceiro; depois, R$ 800. | Rafael: "Restante ok" |
| Q22 | Pacote de contas: 25% a partir de 5 contas e 35% a partir de 10, fatura única do Stripe, sem desenvolvimento no app. Conta para a comissão do coach. | Rafael: "Restante ok" |
| Q23 | **Campo opcional de Instagram no cadastro da Aura**, para mapear contas com muitos seguidores (candidatos a parceiro). | Rafael: "acho legal termos um campo opcional de instagram no cadastro da aura tambem pra mapearmos contas com muitos seguidores." |

### Rodada 5 (22/10): confirmação

| # | Decisão | Fonte |
| --- | --- | --- |
| Q24 | Campo de Instagram opcional, **fora do formulário de cadastro**: no onboarding ou em "Minha conta", com o propósito dito ("para conectarmos você com coaches e a comunidade"). Sessão própria no aura-novofront e no aura_api; a migration aditiva no AuraBusiness é do Rafael. | Rafael: "sim" |

**Fase 0 fechada em 22/10/2026.** O Rafael confirmou o entendimento compartilhado abaixo ("sim").

## Síntese do entendimento (confirmada em 22/10)

**Meta:** de 16 para 45 pagantes ativos até 31/01/2027 (60 esticado; abaixo de 30 reabre o pivô).

**Mercados:** aquisição B2C em inglês (Reino Unido, Canadá, Alemanha, Holanda, Áustria, nórdicos). O Brasil entra pelos coaches e pelo B2B, e o B2C brasileiro fica só com e-mail para a base e stories em PT.

**Frentes, em ordem de início:**

1. **Medição** (semanas 1–2): `begin_checkout` e `purchase` no ar (21–22/10), conferir; `purchase` pelo servidor; `fbp`/`fbc` no cadastro; pendências do GA4 com o Rafael; campo opcional de Instagram no cadastro (sessão no app).
2. **Reconquista** (disparo em 02/11, com o Field Exploits): sequência para os ~32 ex-pagantes do Stripe e os do Woo, com 50% no primeiro mês e validade de 14 dias. O envio é do Rafael.
3. **Coaches** (a partir da semana 1): proposta de uma página; o Rafael contata gremistaak, Paulo Moraes, Ganso e outros. Os mesmos termos valem para coaches em inglês.
4. **B2B:** pacote de contas por volume e relatório do field por encomenda (o primeiro grátis para o time de um coach).
5. **Conversão:** formulário de cadastro (dois terços desistem) e ativação até o paywall.
6. **Pago** (só depois da medição): R$ 1.500 em 60 dias, divididos em R$ 1.050 para a DISC02-EU reeditada, R$ 300 de remarketing e R$ 150 na célula "Esportes" em inglês. A configuração não muda por 14 dias e o corte é por custo por assinante.
7. **Orgânico em inglês:** feed em inglês, X/Twitter, Reddit e shorts, a partir de 2 ou 3 vídeos por semana do Rafael.

**Fica com o Rafael:** envio de e-mail, verba, publicação, preço e cupons, o contato com os coaches e a migration do campo de Instagram no AuraBusiness.

**Pendências de produto fora do plano:** aposentar o Team Mode (landing, app, STATE do aura-main); campo de Instagram no cadastro (aura-novofront, aura_api e migration no AuraBusiness).
