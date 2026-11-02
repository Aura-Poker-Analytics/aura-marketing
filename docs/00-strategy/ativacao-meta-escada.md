# Ativação dos cadastrados da Meta: escada, lote de 01/11 e rotina semanal

**Data:** 01/11/2026 (madrugada de 02/11) · **Agente:** A1 do workforce (P-108) · **Branch:** `feat/ativacao-meta-p1`
**Estado:** rascunhos. **Nada foi enviado.** Duas broadcasts em RASCUNHO no Resend (A1 PT e A1 EN). Nenhum contato criado, nenhuma automação, nada escrito no AuraBusiness, nenhum e-mail no git.
**Regras que valem aqui:** e-mail a usuário só com o "sim" do Rafael digitado na sessão; MKT-D4 proíbe automação de envio antes da ficha de LGPD; CTA sempre para `www.aurapoker.com` com UTM; sem promessa de ganho; nada de "plano GTO". Base: `followup-cadastrados-gratis.md` §4.1, §4.3 e §12.

## 1. A escada

Origem: `tbl_user.utm_source` em `meta` ou `instagram` (SINAL01 pago e o link da bio). Todos entram como Grátis. O dia conta a partir do **primeiro envio** (D0 = dia do A1), não do cadastro, porque ninguém recebeu nada até aqui.

| Passo | Quando | Gatilho (quem entra) | Assunto PT | Assunto EN | Arquivo | UTM (`campaign` / `content`) |
| --- | --- | --- | --- | --- | --- | --- |
| **A1** boas-vindas | D0 (lote de hoje: cadastro há até 7 dias) | todo cadastro da Meta ainda não contatado | Sua conta na Aura está pronta: comece pelo c-bet do flop | Your Aura account is ready: start with the flop c-bet | `ativacao-meta/a1-pt.html`, `a1-en.html` | `ativacao-meta` / `a1`, `a1-en` |
| **A2** spot da semana | D2 | quem **não** fez a primeira análise (`analyze_result`) | O spot da semana no Field Exploits, aberto no seu Grátis | This week's Field Exploits spot, open on your Free plan | `a2-pt.html`, `a2-en.html` | `ativacao-meta` / `a2`, `a2-en` |
| **A3** travou? | D5 | quem segue sem primeira análise | Travou em algum passo? | Stuck on a step? | `a3-pt.html`, `a3-en.html` | `ativacao-meta` / `a3`, `a3-en` |
| **U1** paywall | até 24 h do `gate_hit` | bateu no paywall | O spot que você abriu continua do outro lado do cadeado | The spot you opened is still behind the lock | `followup-u1-paywall.html`, `ativacao-meta/u1-en.html` | `upgrade-meta` / `u1`, `u1-en` |
| **U2** cupom | 72 h depois do `gate_hit`, sem assinatura | só quem bateu no paywall e não assinou (80% com cupom `Ph7y2HU9`, 20% controle sem cupom) | 30% no seu primeiro mês do Individual, até [DATA] | 30% off your first month of Individual, until [DATE] | `ativacao-meta/u2-pt.html`, `u2-en.html` | `upgrade-meta` / `u2-cupom`, `u2-cupom-en` |

Ordem de envio e regras:
1. **A1 para todos**, no mesmo dia. É o único passo que sai sem condição.
2. **A2 e A3 só para quem não analisou.** Quem fez a primeira análise sai da escada de ativação e passa a ser lido como Grátis com uso (§4.2 do plano). Quem bateu no paywall vai direto ao U1, mesmo que esteja em A2 ou A3.
3. **U2 só depois do U1 e só com `gate_hit`.** Hoje os 18 não têm `gate_hit` conhecido (§2), então **nenhum entra no U2**. Código do lote criado pelo Rafael no Stripe (`ATIVAddmm`, apontando para `Ph7y2HU9`, limite = tamanho do lote com cupom, 7 dias, `first_time_transaction`).
4. **Um e-mail por pessoa por semana** (teto do MKT-D4): A1 → A2 no D2 e A3 no D5 já cabem se o A2 sair só para quem não analisou; se o Rafael preferir o teto estrito, A2 vai para o D7 e A3 para o D12. Recomendação: manter D2/D5 só porque cada passo tem gatilho de "sem análise" e a base é pequena; ele decide.
5. **Saída:** descadastro, bounce, assinatura ou 3 envios sem abertura. Excluídos sempre: pagantes, superusuários, `@aurapoker.com`.
6. **Idioma:** país BR, PT, AO, MZ → PT; os demais países do lote → EN (VE e outros hispânicos: ver §2).

Voz: grinder, termos de poker em inglês (field, c-bet, flop, spot, buy-in), "a Aura" no feminino em PT, assinatura do Rafael. O A1 pede uma resposta ("qual buy-in você mais joga?"): as respostas viram linguagem do cliente para o contexto de produto.

Pendente antes de qualquer envio: preencher `[SPOT]` do A2 com o `free_week` da semana, conferido logado com a conta dos agentes (G2); teste real no Gmail e Outlook (é envio, só com o sim do Rafael); tracking já está ligado desde 28/10.

## 2. Lote de hoje (18 cadastros)

Leitura só de SELECT no `postgres-azure-business` em 01/11 (colunas `Id`, `create_date`, `country`, `utm_*`, `ultimo_login`, `trial`, `plan_tier`, `active`, `superuser`, sinal de Stripe, domínio interno). Sem e-mail em arquivo. Lista de ids em `content/email/ativacao-meta/lote-2026-11-01.csv`.

| Resumo | Valor |
| --- | --- |
| Cadastros com `utm_source` meta ou instagram desde 30/10 | **18** (16 SINAL01 pago, 2 do link da bio, campanha `organico`) |
| Idioma | **14 PT** (13 BR + 1 VE) e **4 EN** (GB 3, DE 1) |
| Plano | 18 Grátis (`plan_tier = trial`), 0 pagantes, 0 com Stripe, 0 superusuários, 0 `@aurapoker.com` |
| Voltaram depois do dia do cadastro | **0** (`ultimo_login` cai sempre no dia da criação) |
| Receberam e-mail da Aura | **0** |
| Passo de cada um (envio em 02/11) | A1 hoje para os 18. Idade no envio: 8 com D0 (cadastro 01/11), 9 com D1 (31/10), 1 com D2 (30/10) |
| Próximo | A2 em 04/11 e A3 em 07/11, só para quem seguir sem análise |

Lacunas que o banco não responde, e o que fazer:
- **Primeira análise e `gate_hit`** não estão em `tbl_user` (vêm do GA4 por `aura_user_id`, ou do `first_analysis_at` do P2, ainda não existe). Por isso A2/A3/U2 ficam condicionais e a checagem acontece na véspera de cada passo.
- **Venezuela (id 378):** veio pelo criativo `b-br` (PT). Recomendação: PT; o Rafael pode mudar para EN.
- **Dois cadastros de bio (379, 384)** são orgânicos: a mesma escada serve, mas não contam como Meta pago.

Segmento: o plano do Resend tem 3 segmentos e todos estão em uso. Os dois rascunhos A1 ficaram presos ao segmento `65da31a5` ("R1 Grátis inativo 28/10") só porque a broadcast exige um segmento; o nome diz "NÃO ENVIAR". **Esse segmento guarda os 147 do cupom do R2 do follow-up e não pode ser esvaziado, rebatizado nem usado pelo A1** (correção de 02/11, pedido da HUB). O A1 precisa de segmento próprio com os 18 do lote. Quando o R2 tiver saído, a HUB combina qual dos 3 segmentos é liberado; só então os rascunhos são religados a ele. Criar contato é escrita no Resend e só acontece com o sim do Rafael digitado nesta sessão.

## 3. Rotina semanal que monta o lote (proposta, nada criado)

É a "regra amarrada": **toda semana, os novos cadastros da Meta ganham um lote pronto para o Rafael aprovar.**

| Item | Proposta |
| --- | --- |
| Quando | segunda 07:00 (Brasília), depois da leitura do placar da semana |
| Onde roda | fase 1: tarefa agendada local (`mcp__scheduled-tasks`) ou rotina `/schedule`, usando o MCP `postgres-azure-business` (só leitura) e o MCP do Resend (só rascunho). Fase 2: Container Apps Job no repo `growth-ops` (decisão da HUB), quando a ficha de LGPD sair |
| O que lê | `tbl_user` com `utm_source in ('meta','instagram')`, `create_date` desde o último lote, excluindo superusuário, `@aurapoker.com`, quem tem Stripe/assinatura e quem já está no registro de lotes |
| O que grava | só `content/email/ativacao-meta/lote-<data>.csv` (ids, país, idioma, dia, passo; nunca e-mail) e o STATE; rascunhos no Resend por passo × idioma, já com o nome "RASCUNHO · NÃO ENVIAR" |
| Passo de cada id | por idade desde o último envio registrado e pelas condições do §1 (A2/A3 só sem análise; U1/U2 só com `gate_hit`, lidos do GA4 por `aura_user_id`) |
| O que entrega | um cartão à HUB: tamanho do lote por idioma e passo, assuntos, links de prévia, e a pergunta "posso enviar?" |
| **O que não faz sozinha** | **enviar** (nem broadcast, nem batch); criar contato ou segmento no Resend; criar cupom ou promotion code; escrever no AuraBusiness; pôr e-mail em arquivo ou git; ligar automação. Tudo isso exige o "sim" do Rafael digitado, por lote |
| Guardrails | teto de 1 e-mail por pessoa por semana; para se o lote tiver mais de 40 pessoas (anomalia); loga cada execução com o número de ids lidos |

Dependência: o registro de quem já recebeu cada passo precisa de um lugar. Fase 1: o próprio CSV de lotes (ids). Fase 2: `first_analysis_at`, `last_gate_hit_at` e `lang` em `tbl_user` (P2 do plano) e evento no Resend.

## 4. O que o Rafael decide

| # | Decisão | Recomendação |
| --- | --- | --- |
| 1 | Enviar o A1 hoje a 14 PT e 4 EN | Sim, em dois envios (PT e EN) |
| 2 | VE em PT ou EN | PT |
| 3 | A2 em D2 e A3 em D5, ou D7 e D12 pelo teto estrito | D2/D5, só para quem não analisou |
| 4 | Aprovar a rotina semanal como tarefa agendada local | Sim, só rascunho |
