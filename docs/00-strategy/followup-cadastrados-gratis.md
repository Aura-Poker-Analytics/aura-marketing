# Followup com cadastrados e plano Grátis: diagnóstico e plano

**Data:** 23/10/2026 · **Sessão:** `aura-marketing · followup cadastrados e Grátis · plano` · **Branch:** `feat/followup-cadastrados-gratis`
**Skills usadas:** `product-marketing` (contexto v2 de 22/10), `analytics`, `onboarding`, `signup`, `cro`, `emails`, `churn-prevention`, `customer-research`, `ab-testing`, `ogilvy` (copy).
**Rodada 2 (23/10):** template novo, cupom de ativação proposto (§12), auditoria do que o Grátis vê no código (§13). Ver o changelog no fim.
**Estado:** plano e rascunhos. **Nada foi enviado, nenhuma automação foi criada no Resend, nada foi escrito no AuraBusiness.** Envio, automação ligada e cupom são do Rafael, com a frase dele.

> Nome de módulo: o antigo **Field Hotspots** passa a se chamar **Field Exploits** (decisão do Rafael, 23/10). Este doc e os rascunhos usam o nome novo.

## 0. Resumo em uma tela

| # | Número | Valor | Fonte |
| --- | --- | --- | --- |
| N1 | Cadastros em 90 dias | **39** usuários com `sign_up` (6 em 30 dias) | GA4, §1.1 Q1 |
| N2 | Cadastrados no Grátis | **~215** (último número; o atual não foi lido) | STATE do aura-main, 30/09, §1.1 Q5 |
| N3 | Pagantes ativos | **16** (Stripe 9, Woo 5, NOWPayments 2) | Stripe live 23/10 + diagnóstico de 22/10, §1.1 Q6 |
| N4 | Paywall → upgrade | **23** bateram no paywall, **9** clicaram em upgrade (39%), **0** `begin_checkout` medido | GA4, §1.1 Q1 |
| N5 | E-mail | 899 enviados em 30 dias, **98,9%** entregues; **abertura e clique não medidos** (tracking desligado) | Resend, §1.2 |

**O que o diagnóstico mostra:**
1. Não existe followup hoje. A escada de onboarding (D0/D7/D14/D21) rodou uma vez, em lote manual, em 29/08 (26 envios). O Resend tem 0 automações e 0 propriedades de contato. Quem se cadastrou depois de 29/08 não recebeu nada além dos broadcasts de lançamento.
2. Os broadcasts vão para o segmento General inteiro: Grátis, pagantes e cadastros em inglês recebem o mesmo e-mail em PT.
3. Nenhum envio é medido. Open e Click Tracking estão desligados no domínio `news.aurapoker.com`.
4. O gargalo do Grátis é a passagem paywall → compra: 39% clicam em upgrade, e nada é medido depois.
5. A Aura não recebe as mãos do usuário. Ela lê o field. Por isso "upload" não é o marco de ativação: o marco é a **primeira análise** (`analyze_result`). Os segmentos abaixo usam esse marco.

**O plano em uma frase:** três sequências curtas por segmento (ativação, upgrade, reativação), primeiro em lote semanal manual e depois por evento, com o tracking ligado antes do primeiro envio e um teste A/B na reativação do Grátis inativo, que é o maior grupo.

**Decisões que ficam com o Rafael:** §9. **Proposta de cupom para ativar o Grátis:** §12. **O que o Grátis vê, conferido no código:** §13.

## 1. Diagnóstico

### 1.1 Funil, com a consulta de cada número

Tudo só leitura e só agregado. Nenhum dado pessoal foi lido nem impresso.

| Q | Pergunta | Resposta | Consulta |
| --- | --- | --- | --- |
| Q1 | Funil por evento, 30 e 90 dias | `form_start` 31 / 101 · `sign_up` 6 / 39 · `analyze_result` 23 / 41 · `gate_hit` 12 / 23 · `upgrade_click` 6 / 9 · `begin_checkout` 0 / 0 · `purchase` 0 / 0 (usuários) | GA4 `run_report`, property 506294082, dimensão `eventName`, métrica `totalUsers`, janelas de 30 e 90 dias até 22/10, lido em 23/10 |
| Q2 | Funil ordenado | visita 531 → `form_start` 56 → `sign_up` 15 → `analyze_result` 14 → `gate_hit` 8 → `upgrade_click` 2 (90 dias). Vale só como proporção entre passos | GA4 `run_funnel_report`, mesmos passos, 90 dias, lido em 23/10 |
| Q3 | Origem e aparelho | 90 dias: meta/paid 1.357 sessões, direto 532, google/organic 167, e-mail/broadcast 48. Landing 1.439 usuários (1.289 no celular); app 435 (342 desktop) | GA4 `run_report`, `sessionSourceMedium` × `sessions`; `hostName` × `deviceCategory` × `totalUsers`, 90 dias, 23/10 |
| Q4 | Uso por módulo (90 dias até 21/10) | Preflop: viram 49, analisaram 39 · Postflop 35 / 22 · Node-by-Node 27 / 10 · Hotspot 16 / 8 | GA4 `run_report`, `eventName` × `customEvent:module` × `totalUsers` (diagnóstico de 22/10, `docs/03-analytics/diagnostico-funil-2026-11.md` §4, branch `docs/plano-marketing-skills`) |
| Q5 | Cadastrados no Grátis | **~215** em 30/09 (`trial/trial`), mais 70 `individual/não-trial`. Contagem atual não lida | `aura-main/STATE.md`, linha da reativação da coorte (30/09). A consulta atual está em §1.4 (SQL 5.1) |
| Q6 | Pagantes e ex-pagantes | Stripe live: 14 assinaturas, **9 ativas** (5 BRL, 4 USD), 3 canceladas, 2 `incomplete_expired`, 11 clientes. Mais Woo 5 e NOWPayments 2 = **16 ativos**. Ex-pagantes: **31** (cruzamento Stripe × Woo, 22/10) | `stripe_api_read` em `subscriptions` (status=all), contagem por status e moeda, 23/10; Woo e NOWPayments informados pelo Rafael em 22/10 |
| Q7 | Tempo até pagar | Dos 11 clientes do Stripe com fatura paga, **9 pagaram no mesmo dia** em que o cliente foi criado, 1 em ~21 dias, 1 em ~305 dias. **Não mede cadastro → pagamento**: o cliente do Stripe nasce no checkout. O tempo real sai do `CreateDate` do AuraBusiness (SQL 5.5) | `stripe_api_read` em `customers` e `invoices` (status=paid), diferença entre `customer.created` e a primeira `invoice.paid`, 23/10 |
| Q8 | Novas assinaturas por mês | jul 4, ago 3, set 2, out 3 | Stripe, diagnóstico de 22/10 |

**Leitura:**
- **Ativação existe.** Quem se cadastra usa: 41 usuários analisaram algo em 90 dias, a porta de entrada é o Preflop (39).
- **O paywall gera intenção.** 23 bateram nele e 9 clicaram em upgrade. Nenhum e-mail fala com essa pessoa hoje.
- **O depois do clique é escuro.** `begin_checkout` e `purchase` só contam desde o deploy do aura-novofront#185 (22/10). A compra pelo servidor (aura-api#120) está desligada.
- **A base grande é o Grátis parado.** São ~215 contas Grátis contra 6 cadastros novos por mês. Reativar essa base move mais que otimizar o boas-vindas.

### 1.2 E-mail: o que existe

| Item | Estado em 23/10 | Fonte |
| --- | --- | --- |
| Escada de onboarding | 4 e-mails (D0 fatiar, D7 classes, D14 upgrade, D21 cupom) + reativação de agosto, em `content/email/` (branch `feature/descoberta-reels-v2`). Rodou uma vez, em 29/08: 26 envios (D0 2, D7 8, D14 16). Sem evidência de envio depois | `docs/02-paid/escada-onboarding-emails.md`; `get-email-metrics` |
| Automação | **0** automações, **0** templates, **0** propriedades de contato, 1 topic ("Onboarding — dicas de estudo") | Resend: `list-automations`, `list-templates`, `list-contact-properties`, `list-topics`, 23/10 |
| Segmentos | 3 (limite do plano): Board Selection leads, Field Ranges não receberam, General | Resend `list-segments`, 23/10 |
| Broadcasts | 9, todos enviados; o último foi o Modo GTO, 21/10, 253 enviados, 250 entregues, para o General | Resend `list-broadcasts` / `get-broadcast`, 23/10 |
| Métricas (24/09 a 23/10) | 899 enviados, 889 entregues (98,9%), 10 bounces, 0 reclamações, 0 descadastros, **aberturas e cliques = 0 porque o tracking está desligado** | Resend `get-email-metrics`, 23/10 (a retenção é de ~30 dias) |
| Domínio | `news.aurapoker.com`, verificado; **Open Tracking off, Click Tracking off** | Resend `list-domains`, 23/10 |

**Problemas que o plano corrige:**
1. Sem tracking, nenhum envio pode ser comparado. Pré-requisito P1.
2. D21 vencido ("até 30/09", R$ 37): aposentado.
3. D0, D7 e a reativação de agosto apontam para `www.aura.poker`. A regra é a landing `www.aurapoker.com` com UTM. Os rascunhos novos seguem a regra (ver a decisão R3 em §9).
4. O General inclui pagantes e cadastros em inglês. Todo envio deste plano exclui pagantes e ex-pagantes em reconquista.
5. Descadastro inconsistente (mailto no lote, link do Resend no broadcast). Padrão novo em P4.
6. Não há versão em inglês, e a aquisição B2C nova é em inglês (decisão Q2 de 22/10).

### 1.3 O que o Grátis mostra hoje

Lido do `origin/main` do aura-novofront (`c1f5658`) e do aura_api (`e5d0be4`) em 23/10. Detalhe com arquivo e linha na nota `followup-diag-gratis.md` da pasta de notas da sessão HUB.

| Área | Grátis | Pago (Individual) |
| --- | --- | --- |
| Recorte global | buy-in até US$ 22, só Vanilla, etapas Início e Meio, últimos 2 anos | todos os buy-ins, KO e Mystery, todas as etapas |
| Preflop | aberto no recorte; stats por size borradas | tudo |
| Postflop | uma reação livre por street (c-bet IP no flop, second barrel IP no turn, third barrel IP no river); Modo GTO em amostra (Fold por size com número no spot aberto; Call e Raise mostram GTO e faixa, sem o número do field) | Facing Actions completo, quebra por size, Modo GTO com os 4 números |
| Node-by-Node | flop inteiro | turn e river |
| Field Exploits (rota `/exploits`) | **1 dos 8 spots do Individual, inteiro** (número do field, número do GTO, faixa e "como explorar"); só a grade por size fica trancada, e a linha "+N spots" | os **8 spots** da janela da semana (aura-api#122, aura-novofront#186, #187 e #188 mesclados; front publicado em 23/10) |
| Exploit card do Painel | um exploit fixo | um exploit novo por semana |
| Aura IA | **não está no ar.** Cota aprovada: 5 perguntas por mês no Grátis, 100 no Individual | idem |
| Paywall | todo CTA leva a `/MinhaConta?subscribe=1`; botões "Fazer upgrade" e "Ver planos" | — |
| Sino de Novidades | lê `tbl_user_notification`; publicação por `POST /api/notifications/changelog` (superusuário, sem tela); **vai a todos os `Active=true`, sem filtro de plano** | — |
| Preço | Individual R$ 150 / US$ 29 por mês, US$ 259 por ano; mantido por 90 dias (Q11). Sem trial no app; cupom só de parceiro e da reconquista | — |

**Consequências para a copy:**
- O Individual já vê os 8 spots do Field Exploits (PRs mesclados em 23/10). Antes do primeiro envio, conferir logado numa conta Individual (gate G1).
- Não citar a Aura IA em e-mail enquanto ela não estiver no ar. Quando estiver, "5 perguntas por mês" é o argumento de upgrade natural do Grátis (gatilho: cota batida).
- O sino não segmenta: ele serve para novidade que vale a todos, não para empurrar upgrade.

### 1.4 O que faltou medir e a consulta que falta

O AuraBusiness (`tbl_user`, servidor `aura-production`) não tinha ferramenta de leitura nesta sessão: o MCP `postgres-azure-analytics` não resolve o host, e o `-prod` aponta para o lake `aura_database`, que não tem tabela de usuário. Ler o AuraBusiness é permitido; estas consultas, só SELECT e só agregado, ficam para quem tiver acesso (nomes de coluna a conferir com `\d public.tbl_user`):

```sql
-- 5.1 base por plano
SELECT trial AS gratis, "Active" AS ativo, count(*)
FROM public.tbl_user WHERE NOT superuser GROUP BY 1, 2;

-- 5.3 Grátis ativo x inativo (proxy: último login)
SELECT count(*) FILTER (WHERE ultimo_login >= now() - interval '14 days') AS gratis_ativo_14d,
       count(*) FILTER (WHERE ultimo_login <  now() - interval '14 days' OR ultimo_login IS NULL) AS gratis_inativo,
       count(*) AS gratis_total
FROM public.tbl_user WHERE trial AND NOT superuser;

-- 5.5 cadastros por semana (confere com o sign_up do GA4)
SELECT date_trunc('week', "CreateDate") AS semana, count(*)
FROM public.tbl_user WHERE "CreateDate" >= now() - interval '90 days'
GROUP BY 1 ORDER BY 1;
```

| Lacuna | Efeito | Como fechar |
| --- | --- | --- |
| Contagem atual dos 4 segmentos | o plano usa ~215 (30/09) como ordem de grandeza | SQL 5.1 e 5.3 acima |
| Primeira análise por usuário | o segmento S1/S2 só sai do GA4, que não tem e-mail e perde quem recusa cookies | marco `first_analysis_at` em `tbl_user`, gravado pela API (P2) |
| Tempo cadastro → pagamento | Q7 não mede isso | `CreateDate` × primeira `invoice.paid`; a API do #120 pode gravar `first_paid_at` |
| Abertura e clique | nenhuma comparação de e-mail possível | P1 |

## 2. Princípios do redesenho

Tirados das skills e aplicados ao caso:

1. **Um marco de ativação: a primeira análise com o GTO ao lado.** (`onboarding`) O "aha" da Aura é ver, num spot do seu buy-in, o que o field faz e onde a faixa GTO fica. O Grátis já entrega isso no c-bet IP do flop. Todo e-mail de ativação leva a esse spot.
2. **Um e-mail, um trabalho, um CTA.** (`emails`)
3. **Gatilho por comportamento quando der, lote semanal até lá.** (`emails`, `onboarding`) Sem automação nem propriedade de contato no Resend, a fase 1 é um lote semanal manual montado a partir das consultas da §1.4. A fase 2 troca o lote por evento da API.
4. **Falar com quem bateu no paywall em até 24 h.** (`cro`, `churn-prevention`: risco e intenção são sinais de curto prazo) É o maior sinal de compra que o app gera, e hoje ninguém fala com ele.
5. **A promessa é o resultado, não o mecanismo.** (`ogilvy`, memória do repo) "Escolha o spot do seu buy-in, veja o que o field faz e onde fica a faixa GTO", com prova de escala ("mais de 400 mil torneios").
6. **Perguntar e guardar a resposta.** (`customer-research`, modo 3) O boas-vindas pede uma linha de resposta (buy-in e o que estuda hoje). As respostas viram a linguagem do cliente que falta no contexto de produto (🔴 em "Customer Language").
7. **Limpar a lista em vez de insistir.** (`churn-prevention`, `emails`) A reativação termina com "fica ou sai"; quem não abrir em 3 envios sai do topic de dicas.
8. **Desconto só por comportamento, uma vez por conta.** O preço de tabela fica mantido (Q11). O cupom de ativação da §12 entra só para quem bateu no paywall e não assinou, com prazo curto, e nunca é anunciado em público.

## 3. Segmentos

O pedido falava em "upload". Como a Aura não recebe as mãos do usuário, o marco é a primeira análise. Mapeamento:

| Segmento | Definição | Fonte para montar o lote | Tamanho |
| --- | --- | --- | --- |
| **S1. Cadastrado sem uso** ("sem upload") | cadastro há 0–14 dias, sem nenhum `analyze_result` | AuraBusiness `CreateDate` + `first_analysis_at` (P2); até lá, `user_id` do GA4 × `analyze_result` | ~6 por mês (N1) |
| **S2. Usou e está no Grátis** ("com upload e no Grátis") | Grátis com pelo menos uma análise, cadastro há até 30 dias, sem `gate_hit` | idem | sem contagem (§1.4) |
| **S3. Grátis ativo** | Grátis com login nos últimos 14 dias; prioridade para quem teve `gate_hit` nos últimos 7 dias | SQL 5.3 + `gate_hit` do GA4 por `aura_user_id` | 12 com `gate_hit` em 30 dias (Q1) |
| **S4. Grátis inativo** | Grátis sem login há mais de 14 dias | SQL 5.3 | a maior parte dos ~215 (N2) |

**Exclusões em todo envio:** pagantes ativos (Stripe, Woo, NOWPayments); ex-pagantes enquanto a reconquista de 02/11–16/11 roda; superusuários e contas internas; bounce permanente e descadastro. **Idioma:** cadastro de fora do Brasil e de Portugal recebe a versão EN.

## 4. As sequências

Convenções de todos os e-mails:
- Remetente `Aura Poker Analytics <news@news.aurapoker.com>`, reply-to `manager@aurapoker.com`, assinatura "Rafael, fundador da Aura" (recomendação R2 da reconquista).
- CTA para `https://www.aurapoker.com/` com `utm_source=email&utm_medium=email&utm_campaign=<sequência>&utm_content=<id>`. O `cta_click` da landing (aura-landing#26) mede a passagem para o app.
- Termos de poker em inglês, "a Aura" no feminino, porcentagem com vírgula. Nada de "pp", "ponte" ou bastidor.
- Número de spot só a partir de tela conferida logado (padrão `numeros-verificados`). Nos rascunhos, os números ficam como `[...]`.

### 4.1 Ativação (S1): `utm_campaign=ativacao`

**Gatilho:** `sign_up`. **Objetivo:** primeira análise com o GTO ao lado. **Saída:** primeira análise → passa para a 4.2.

| ID | Quando | Canal | Assunto | Ideia do corpo | CTA | Métrica |
| --- | --- | --- | --- | --- | --- | --- |
| **A1** ✏️ | D0 (no lote: cadastro dos últimos 7 dias) | e-mail | Sua conta na Aura está pronta: comece pelo c-bet do flop | O que o Grátis abre (recorte até US$ 22, Vanilla, Início e Meio); o caminho de 3 passos até o c-bet IP no flop com a faixa GTO; o Spot da semana no Field Exploits; pedido de resposta: "qual buy-in você mais joga?" | **Abrir meu primeiro spot** → landing, `utm_content=a1` | primeira análise em 7 dias; taxa de resposta |
| A2 | D2, só sem análise | e-mail | O spot da semana no Field Exploits, aberto no seu Grátis | Um spot concreto, com o número do field e a faixa GTO, e onde ele está no app | **Ver o spot da semana** → landing, `a2` | primeira análise em 7 dias |
| A3 | D5, só sem análise | e-mail | Travou em algum passo? | Texto curto, pessoal, sem botão grande: o que costuma travar (filtro fora do recorte Grátis cai no cadeado) e uma pergunta aberta para responder | link simples para a landing, `a3` | respostas; primeira análise em 7 dias |

### 4.2 Grátis com uso (S2): `utm_campaign=gratis-uso`

**Gatilho:** primeira análise. **Objetivo:** chegar ao limite do Grátis num spot que importa (gerar `gate_hit` com contexto). **Saída:** `gate_hit` → 4.3; assinatura.

| ID | Quando | Canal | Assunto | Ideia do corpo | CTA | Métrica |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | +1 dia da primeira análise | e-mail | Você viu o flop. O turn e o river estão no Node-by-Node | Do c-bet IP para a árvore: o Grátis navega o flop inteiro; mostrar o que o turn acrescenta | **Abrir o Node-by-Node** → landing, `g1` | uso do Node-by-Node; `gate_hit` |
| G2 | +7 dias | e-mail | Um exploit novo toda semana (o seu está fixo) | O exploit card do Painel: no Grátis fica fixo, no Individual troca toda semana. Mostrar o desta semana | **Ver planos** → landing `#planos`, `g2` | `upgrade_click` |
| — | quando houver novidade | sino | (título da novidade) | Lançamentos que valem para todos (ex.: Spot da semana trocou). Nunca empurrar upgrade pelo sino, porque ele não segmenta | link no app | clique no sino (sem medição hoje) |

### 4.3 Grátis ativo que bateu no paywall (S3): `utm_campaign=upgrade`

**Gatilho:** `gate_hit` (ideal em até 24 h; no lote, quem bateu nos últimos 7 dias). **Objetivo:** assinatura do Individual. **Saída:** assinatura; 14 dias sem novo `gate_hit` → volta à 4.2.

| ID | Quando | Canal | Assunto | Ideia do corpo | CTA | Métrica |
| --- | --- | --- | --- | --- | --- | --- |
| **U1** ✏️ | até 24 h do `gate_hit` (lote: últimos 7 dias) | e-mail | O spot que você abriu continua do outro lado do cadeado | O que o Individual abre, ligado ao que o Grátis tranca (buy-ins acima de US$ 22, KO e Mystery, todas as etapas, turn e river, Modo GTO com os 4 números, exploit novo por semana); preço mensal e a âncora do anual | **Ver planos** → landing `#planos`, `u1` | `upgrade_click` → `begin_checkout` → `purchase` por `utm_content` |
| U2 | +3 dias (72 h), sem assinatura | e-mail | 30% no seu primeiro mês do Individual, até [DATA] (rascunho `followup-u2-cupom.html`) | O mesmo quadro Grátis × Individual do U1, mais o código pessoal do cupom de ativação (§12) e a data de validade. Quem cai no grupo de controle recebe o U2 sem cupom | **Usar meu código** → landing `#planos`, `u2` | resgate do código; assinatura em 14 dias, cupom × controle |
| U3 | +7 dias, sem assinatura | e-mail | Uma pergunta antes de você decidir | Pesquisa de uma pergunta ("o que falta para assinar?": preço, tempo, não sei usar, o dado não é do meu jogo, outro) com resposta por link ou por e-mail | link da pesquisa | respostas; assinatura em 14 dias |

Quando a Aura IA estiver no ar: **U-IA**, no gatilho "cota de 5 perguntas batida", assunto "Suas 5 perguntas do mês acabaram", CTA para planos (100 por mês no Individual).

### 4.4 Grátis inativo (S4): `utm_campaign=reativacao-gratis`

**Gatilho:** 14 dias sem login (fase 1: lote único para a base atual, depois mensal). **Objetivo:** voltar a analisar; limpar a lista. **Saída:** login; descadastro; 3 envios sem abertura → sai do topic.

| ID | Quando | Canal | Assunto | Ideia do corpo | CTA | Métrica |
| --- | --- | --- | --- | --- | --- | --- |
| **R1** ✏️ | D0 do lote (≥ 7 dias depois do e-mail de lançamento do Field Exploits) | e-mail | Desde o seu último login, a Aura ganhou o GTO | Novidade: Modo GTO (field e faixa GTO no flop, turn e river), Field Ranges com GTO, Field Exploits. O que o Grátis abre de cada um, hoje | **Ver a nova Aura** → landing, `r1-a` / `r1-b` (teste A/B, §6) | login em 7 dias por variante |
| R2 | +5 dias, sem login | e-mail | Volte para a Aura com 30% no primeiro mês, até [DATA] (80% do lote, `followup-r2-cupom.html`); o controle de 20% recebe "O spot da semana no Field Exploits" | Cupom de ativação (§12, gatilho B) para quem nunca bateu no paywall; no controle, um spot com número e o exploit | **Usar meu código** → landing `#planos`, `r2-cupom` (controle: `r2`) | login em 7 dias e assinatura em 14 dias, cupom × controle |
| R3 | +12 dias, sem login | e-mail | Continuo te mandando dicas de estudo? | "Fica ou sai": um clique para continuar, um para sair; pergunta opcional de por que parou | dois links: ficar (landing, `r3-fica`) e sair (descadastro) | descadastro; respostas; limpeza |

### 4.5 Captura no celular (fora dos 4 segmentos, depende do aura-landing#26)

Quando a captura de e-mail no celular for ligada (`VITE_MOBILE_EMAIL_CAPTURE`), entra um **M1** imediato: "Seu link para abrir a Aura no computador", com o link da landing e `utm_campaign=captura-celular`. A flag só liga com a automação que manda esse e-mail (diagnóstico de 22/10, §8).

### 4.6 Inglês

A1, U1 e R1 ganham versão EN antes do primeiro lote que inclua cadastro de fora do Brasil e de Portugal. Assuntos propostos: A1 "Your Aura account is ready: start with the flop c-bet"; U1 "The spot you opened is still behind the lock"; R1 "Since your last login, Aura added GTO".

## 5. Pré-requisitos (antes do primeiro envio)

| # | O quê | Dono | Bloqueia |
| --- | --- | --- | --- |
| P1 | Ligar Open Tracking e Click Tracking no domínio `news.aurapoker.com` | Rafael (configuração da conta) | o teste A/B e toda métrica de e-mail |
| P2 | Marcos no AuraBusiness gravados pela API: `first_analysis_at`, `last_gate_hit_at`, `lang`; e envio desses dados ao Resend como propriedades de contato ou eventos (`send-event`) | sessão no aura_api; a migration aditiva no AuraBusiness é do Rafael | fase 2 (automação). A fase 1 funciona sem isso |
| P3 | Excluir pagantes do General, ou criar um segmento "Grátis" (o plano do Resend limita a 3; trocar o "Board Selection leads", que é de setembro) | HUB + Rafael | todo envio para o Grátis |
| P4 | Descadastro único: link do Resend nos broadcasts e `List-Unsubscribe` no batch | sessão de envio | conformidade e limpeza |
| G1 | Conferir logado, numa conta Individual, que os 8 spots do Field Exploits abrem (os PRs #122, #186, #187 e #188 estão mesclados desde 23/10) | Rafael ou sessão com login | U1 e o E1 da reconquista |
| G2 | Números de spot conferidos logado | Rafael ou sessão com login | A2, R2 |

## 6. Teste A/B priorizado

**Escolha:** o assunto e o ângulo do **R1** para o Grátis inativo. É o único grupo com volume para ler algo (a maior parte dos ~215), e o envio não depende de automação. Ativação (6 por mês) e upgrade (12 por mês) não têm volume para teste.

| Campo | Valor |
| --- | --- |
| Hipótese | Porque o Grátis inativo saiu antes do Modo GTO, acreditamos que um spot concreto com o número do field e a faixa GTO no assunto e no topo traz mais gente de volta do que a lista de novidades, para o Grátis inativo. Saberemos quando o login em 7 dias da variante B superar o da A |
| A (controle) | "Desde o seu último login, a Aura ganhou o GTO" + lista de 3 novidades (rascunho R1) |
| B | "[posição] vs [posição], c-bet no flop: o field folda [X]%, o GTO [Y]%" + um spot e o exploit no topo; a lista de novidades vira uma linha |
| Divisão | 50/50 aleatória, estratificada por idioma |
| Métrica principal | usuários com login em até 7 dias (AuraBusiness `tbl_login_event`), por variante |
| Secundárias | clique (Resend, depois de P1), sessões por `utm_content` no GA4, `analyze_result` em 7 dias |
| Guardrails | descadastro e reclamação por variante; parar a variante com reclamação acima de 0,3% |
| Amostra | ~100 por variante. Com base de ~5% de volta em 7 dias, só um efeito muito grande (de ~5% para ~15%) seria detectável. **O teste é direcional**: decide o ângulo dos próximos envios (R2, reconquista, lançamentos) e é repetido no próximo lote antes de virar regra |
| Duração | um envio, leitura em 7 dias, sem espiar antes |
| Registro | resultado em `.agents/product-marketing.md` → Learnings, com status `watch` até a repetição |

ICE dos candidatos: R1 assunto (I 6, C 5, E 9 = 6,7) > U1 com e sem preço no corpo (I 7, C 4, E 4 = 5,0) > A1 CTA direto ao app × landing (I 6, C 6, E 3 = 5,0; pouco volume).

## 7. Métricas e metas

| Métrica | Base hoje | Meta 60 dias | Fonte |
| --- | --- | --- | --- |
| Cadastro → primeira análise em 7 dias | sem leitura por coorte (41 analisaram, 39 cadastraram em 90 dias) | 70% | GA4 hoje; `first_analysis_at` depois de P2 |
| `gate_hit` → `upgrade_click` | 39% (9 de 23) | 50% | GA4 |
| `upgrade_click` → `purchase` | não medido | medir (base) | GA4 desde 22/10 + aura-api#120 |
| Grátis inativo → login em 7 dias depois do R1 | sem base | 10% | AuraBusiness |
| Assinaturas novas vindas do Grátis | ~3 por mês, todas as origens (Q8) | 6 por mês | Stripe × `utm_campaign` |
| Clique por e-mail | não medido | base no primeiro lote | Resend, depois de P1 |
| Descadastro por envio | 0 | < 1% | Resend |

Ligação com a meta do plano (45 pagantes em 31/01/2027, saindo de 16): este plano mira **+10 assinaturas do Grátis** até 31/01, das ~29 que faltam.

## 8. Rollout

| Fase | Quando | O quê | Depende de |
| --- | --- | --- | --- |
| 0 | esta semana | Rafael decide §9; tracking ligado (P1); contagens da §1.4 | Rafael |
| 1a | ≥ 7 dias depois do e-mail de lançamento do Field Exploits, sem cruzar com a reconquista (02–16/11) | R1 com o teste A/B para o Grátis inativo, em lote | P1, P3, P4, frase do Rafael |
| 1b | semanal, a partir do mesmo dia | lote de A1 (cadastros da semana) e U1 (quem bateu no paywall na semana) | P3, frase do Rafael para o lote recorrente |
| 2 | depois de P2 | A1–A3, G1–G2, U1–U3 e R1–R3 por gatilho, como automações do Resend | P2, frase do Rafael para ligar cada automação |
| 3 | quando a Aura IA estiver no ar | U-IA na cota batida | go-live da Aura IA |

## 9. Decisões do Rafael

| # | Decisão | Recomendação |
| --- | --- | --- |
| R1 | Ligar Open e Click Tracking no `news.aurapoker.com` | **Sim.** Sem isso nenhum e-mail deste plano pode ser comparado |
| R2 | Envio dos lotes (R1 com teste A/B, A1 e U1 semanais) e, depois, ligar as automações | Aprovar a fase 1 em lote; a fase 2 vai automação por automação |
| R3 | CTA dos e-mails de ativação (A1–A3, G1): a regra manda para a landing, mas o usuário já tem conta e a landing perde ~70% na passagem para o app (V1 do diagnóstico de 22/10) | Manter a landing nos rascunhos, como manda a regra, e abrir exceção só para a ativação (CTA direto ao app com UTM), igual à exceção proposta para os ex-pagantes |
| R4 ✅ aprovada e ampliada (23/10) | Oferta para o Grátis (reaberta na rodada 2) | **Cupom de ativação de 30% no primeiro mês**, só no gatilho "bateu no paywall e não assinou em 72 h", validade de 7 dias, uso único, uma vez por conta, só no Stripe, com grupo de controle. Proposta completa na §12. Criar o cupom é do Rafael |
| R5 | Liberar o segmento "Board Selection leads" (setembro) para virar "Grátis" no Resend | Sim |
| R6 | Assinatura pessoal ("Rafael, fundador da Aura") nos e-mails do Grátis | Sim, igual à reconquista |

## 10. Rascunhos e template

| ID | Arquivo | Segmento | Prints (desktop e 390 px) |
| --- | --- | --- | --- |
| A1 | `content/email/followup-a1-boas-vindas.html` | S1 | `content/email/_template/prints/followup-a1-boas-vindas-*.png` |
| U1 | `content/email/followup-u1-paywall.html` | S3 | `content/email/_template/prints/followup-u1-paywall-*.png` |
| R1 | `content/email/followup-r1-reativacao.html` (variante A do teste) | S4 | `content/email/_template/prints/followup-r1-reativacao-*.png` |

São os três primeiros da fase 1, um por alavanca (ativação, upgrade, reativação), e os únicos que saem sem automação. A versão EN e a variante B do R1 entram depois das decisões R1 a R3.

**Template v2 (rodada 2, 23/10).** O Rafael achou o template antigo "horrível". O novo é gerado por `content/email/_template/build_followup.py` (`python -I content/email/_template/build_followup.py`); os HTML não se editam à mão.
- **Identidade:** a paleta dark da landing (`aura-landing/src/styles/globals.css`, `.theme-a`): fundo `#0F1526`, cartão `#13192E`, painel `#1C2B47`, borda `#2F435C`, texto `#F5F6F8` / `#C3C7D1` / `#9AA0AE`, dourado `#D4A418` no botão. Montserrat, a fonte da landing, onde o cliente carrega webfont (Apple Mail, iOS); Arial nos demais.
- **Uma peça forte por e-mail**, no lugar da lista de ♠: no A1, o caminho de três passos até o primeiro spot; no U1, o quadro Grátis × Individual linha a linha; no R1, um quadro field × GTO de um spot de pós-flop desenhado em tabela, sem imagem hospedada (CO vs BB, flop K-high two-tone, fold contra c-bet de 33%: field 46,0%, GTO 38,8%, faixa de 37,1% a 40,4%; fonte `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md`, exemplo (a)). A imagem `modo-gto-pt.png` saiu: o cabeçalho dela usa o nome antigo "Field vs GTO" e mistura a grade de pré-flop com o cartão de pós-flop.
- **Pouco texto (corte de 23/10, pedido da HUB no gosto do Rafael):** cada e-mail tem só título, uma frase, a peça visual, o botão e uma linha de pergunta. No A1, cada passo tem um subtítulo de no máximo uma linha. O U1 ficou com 5 linhas no quadro e uma linha de preço. O R1 é título, frase e o quadro do spot. A linha "Modo GTO incluso no plano Individual por tempo limitado" repete, palavra por palavra, o que a landing mostra hoje (conferido no ar em 23/10). O parágrafo do Field Exploits saiu do A1; ele fica para o A2.
- **Compatibilidade:** só tabelas e estilo inline. O `<style>` do head só ajusta o celular (padding, título e botão de largura cheia), e o Outlook o ignora sem quebrar. As imagens vêm de URLs públicas que respondem 200 (conferido em 23/10). Prints feitos no Chrome headless; o de 390 px é de um iframe com 390 px exatos.
- **Pendente antes do envio:** teste real no Gmail (web e app) e no Outlook, com um envio de teste para um endereço interno (é envio, então só com a frase do Rafael); versão EN; tirar o comentário de rascunho da linha 2.

**Revisão de marca da rodada 1 (agente `aura-revisor-marca`, 23/10): OK COM RESSALVAS**, com as correções aplicadas e mantidas na v2.

## 11. Fontes

- Notas da sessão (fora do repo, pasta de notas da HUB): `followup-diag-emails.md`, `followup-diag-banco.md`, `followup-diag-ga4.md`, `followup-diag-gratis.md`, todas de 23/10.
- Branch `docs/plano-marketing-skills`: `.agents/product-marketing.md` (v2), `docs/03-analytics/diagnostico-funil-2026-11.md`, `docs/00-strategy/entendimento-compartilhado-2026-11.md`, `content/email/reconquista-2026-11/sequencia.md`.
- Branch `feature/descoberta-reels-v2`: `docs/02-paid/escada-onboarding-emails.md`, `content/email/onboarding-*.html`.
- `aura-main/STATE.md` e `_ops/perguntas-po-2026-10-23.md`.
- Rodada 2: notas `followup-r2-gratis-codigo.md` (código de `origin/main`, aura-api `9fda00f` e aura-novofront `54086c0`, 23/10) na pasta de notas da HUB.

## 12. Cupom para ativar o Grátis (aprovado em 23/10; criar o cupom é do Rafael)

**Decisão do Rafael (23/10, repassada pela HUB):** "FOLLOWUP R4 tambem enviamos o cupom pra quem nao bate no paywall mas nao volta a acessar. restante ok." A R4 está aprovada e ampliada para dois gatilhos.

| Campo | Gatilho A: bateu no paywall | Gatilho B: não voltou (ampliação do Rafael) |
| --- | --- | --- |
| Quem | Grátis que bateu no paywall (`gate_hit`) e não assinou em 72 h | Grátis que **nunca** bateu no paywall, recebeu o R1 (reativação) e não fez login em 5 dias. Na prática, 19 ou mais dias sem login |
| E-mail | **U2 com cupom** (`content/email/followup-u2-cupom.html`) | **R2 com cupom** (`content/email/followup-r2-cupom.html`), que substitui o R2 "spot da semana" para 80% do lote |
| Por que nesse ponto | é o sinal de compra mais quente do funil | o R1 dá valor sem desconto primeiro; o cupom só vai para quem o R1 não trouxe de volta, para não ensinar a base a esperar desconto |
| Controle | 20% sorteados recebem o U2 sem cupom | 20% sorteados recebem o R2 sem cupom (o spot da semana) |
| Frequência | uma vez por conta, para sempre (um cupom de ativação por conta, A ou B) | idem |
| Métrica | assinatura em 14 dias, cupom × controle | login em 7 dias e assinatura em 14 dias, cupom × controle |

**Oferta (igual nos dois):** 30% no primeiro mês do Individual mensal, como valor fixo: R$ 45 de desconto (paga R$ 105) ou US$ 9 (paga US$ 20). Validade de 7 dias a partir do envio. Fica bem abaixo do cupom da reconquista que já existe no Stripe ("Reconquista: 80% no primeiro mês", R$ 120 de desconto, máximo de 40), para não premiar quem cancela.

**Guardrails:**
- se mais de 60% das assinaturas novas em 8 semanas usarem cupom, cortar ou reduzir;
- retenção no segundo mês: com cupom × sem cupom;
- código nunca em público (procurar o prefixo no Discord e nas redes).

**Canal:** só o Stripe, que aceita código no checkout (`AllowPromotionCodes = true`). O NOWPayments (cripto) não tem campo de cupom, e o WooCommerce não é o checkout do app.

### 12.1 Especificação para o Rafael criar no Stripe (live, conta AURA ANALYTICS)

Lido no Stripe live em 23/10, só leitura: produto Individual `prod_Uq1tafUe0H12h4` ("AURA Plano Individual"). Cupons que já existem: `8YS32mA8` (reconquista, R$ 120, uso máximo 40), `AURA80` e `discount_80`.

**1 cupom, criado uma vez:**

| Campo | Valor |
| --- | --- |
| Nome | `Ativação Grátis: 30% no primeiro mês` |
| ID | `ATIVACAO30` |
| Tipo | valor fixo (`amount_off`), não porcentagem: porcentagem num anual daria R$ 388 de desconto |
| Valor | `amount_off = 4500`, `currency = brl`; `currency_options.usd.amount_off = 900` |
| Duração | `duration = once` (só a primeira fatura) |
| Produto | `applies_to.products = [prod_Uq1tafUe0H12h4]` |
| Limite total | `max_redemptions = 200` (teto de segurança) |
| Metadata | `campanha = ativacao-gratis-2026-11` |

**1 promotion code por lote e por gatilho** (fase 1, envio em lote):

| Campo | Valor |
| --- | --- |
| Código | `ATIVA` + dia e mês do envio para o gatilho A (ex.: `ATIVA0411`); `VOLTE` + dia e mês para o gatilho B (ex.: `VOLTE1111`). Prefixos diferentes medem cada gatilho no Stripe |
| Cupom | `ATIVACAO30` |
| Restrição | `restrictions.first_time_transaction = true` (só quem nunca pagou: exclui ex-pagantes e assinantes) |
| Limite | `max_redemptions` = tamanho do lote com cupom (os 80%) |
| Validade | `expires_at` = envio + 7 dias, 23:59 de Brasília |
| Metadata | `gatilho = A` ou `B`, `lote = <data>` |

Por que código por lote, e não código pessoal, nesta fase: com o envio em lote e sem automação, um código pessoal pede um promotion code por pessoa, criado no Stripe a cada lote. O código por lote, com limite do tamanho do lote, 7 dias e a restrição de primeira compra, dá quase a mesma proteção com uma ação do Rafael por lote. Quando a automação da fase 2 existir, o código passa a ser pessoal (`max_redemptions = 1`), criado pela automação.

**O que o Rafael faz:** criar o cupom `ATIVACAO30` uma vez e, antes de cada lote, o promotion code daquele lote. A sessão de envio preenche `[CÓDIGO]` e `[DATA]` nos e-mails com esses valores.

## 13. O que o Grátis vê hoje (conferido no código, rodada 2)

Lido de `origin/main` em 23/10: aura-api `9fda00f` e aura-novofront `54086c0`. Detalhe com arquivo e linha na nota `followup-r2-gratis-codigo.md`.

**A pergunta do Rafael: "A ideia é dar spot plano individual de graça pra ele ver certo?"**
Sim. O Grátis vê 1 dos 8 spots do Field Exploits do Individual, inteiro: o número do field, o do GTO, a faixa e o "como explorar". Só a grade por size fica trancada. O spot não é sorteado nem escolhido na mão: é o marcado `free_week` no calendário da janela. Hoje é o UTG vs BB com 25 big blinds, que também é o de maior desvio dos 8 da janela. A partir de 02/11, o spot grátis é o primeiro do par que entra toda segunda. Funciona como amostra porque é um spot real do pago, completo, com a linha "+N spots" mostrando o que fica do outro lado.

| Módulo | O que o Grátis vê | O que fica trancado |
| --- | --- | --- |
| Recorte global | buy-in até US$ 22, Vanilla, etapas de início e meio, últimos 2 anos | o resto |
| Preflop | o módulo inteiro dentro do recorte | stats por sub-size, quebras além de stack, GTO |
| Postflop | c-bet IP no flop e as reações no flop, turn e river (ações 1, 4 e 7); filtro de textura do flop; fold por size com número só no spot BTN vs BB, SRP, 30 a 60 big blinds | as outras reações, a quebra por size fora do spot aberto, textura do turn e do river |
| Modo GTO | amostra no spot aberto | o resto |
| Node-by-Node | o flop inteiro | turn e river (paywall no front, 403 na API) |
| Field Ranges | o RFI do CO **com a comparação GTO** e a reação do BB ao open do CO | os outros nós |
| Field Trends | só as duas stats de c-bet IP, no buy-in da categoria 1, sem filtro | o resto |
| Field Exploits | 1 dos 8 spots, inteiro | os outros 7 e a grade por size |
| Painel | um exploit card fixo (a primeira semana gravada) | o exploit novo de cada semana |

**Frases corrigidas nesta rodada:**

| Onde | Antes | Agora | Por quê |
| --- | --- | --- | --- |
| A1 | "O Spot da semana, um dos spots em que o field mais se afasta do GTO, também fica aberto no Grátis" | "Toda semana, um dos 8 spots do plano Individual fica aberto no Grátis, inteiro: o número do field, o do GTO e como explorar" | o spot grátis é o do calendário (`free_week`), não necessariamente o de maior desvio |
| A1 | "Essa reação fica aberta no Grátis" | "Essa reação fica aberta no Grátis, no flop, no turn e no river" | as ações 1, 4 e 7 estão livres |
| U1 | sem a linha do Field Exploits (gate G1) | "Field Exploits: 1 spot / os 8 da semana" | o Individual já vê os 8 (PRs mesclados em 23/10) |
| R1 | "o open do CO no Field Ranges" | "o open do CO e a reação do BB", ao lado do GTO | o Grátis vê as duas, com a comparação GTO |
| §1.3 | "o Individual vê o Grátis no Field Exploits" | "o Individual vê os 8 spots" | mudou com os PRs de 23/10 |

**Ponto de produto (não é de marketing):** a grade por size do spot grátis é trancada só no navegador; a API manda os números ao Grátis. Trancar de verdade é mudança na API (sessão no aura_api, se o Rafael quiser).

## 14. Execução do envio (rodada 3, 23/10)

Ordem fixada pela HUB: (a) rascunho, (b) teste para o Rafael, (c) conferência logada do spot, (d) descadastro e supressão, (e) 1º lote só com o vai da HUB.

| Passo | Estado em 23/10 | Detalhe |
| --- | --- | --- |
| R1 tracking | ⛔ não persistiu | `update-domain` do Resend com `openTracking` e `clickTracking` responde sucesso, mas o domínio `news.aurapoker.com` segue com os dois desligados (duas tentativas, relido). O login do Resend no Chrome do Rafael é de outro time (doublecheck.poker). Falta um clique do Rafael no time da Aura: Domains › news.aurapoker.com › Configuration |
| R5 segmento | ✅ renomeado | "Board Selection 09/2026 — leads (174)" virou "Grátis" (id `eab79cc8-…`), sem apagar contato. ⚠️ O conteúdo ainda são os 174 leads de setembro, não os Grátis |
| (a) rascunho | ✅ | broadcast "RASCUNHO · R1 reativação Grátis (A) · NÃO ENVIAR" (`f185d44e-…`), no segmento Grátis, não enviada |
| (b) teste | ✅ | A1, U1 e R1 enviados só para o e-mail do Rafael, com assunto `[TESTE …]`. Os três chegaram na caixa de entrada do Gmail (não no spam), com a logo oficial e o layout certo no Gmail web |
| (c) spot logado | ⛔ bloqueado | o app abre na tela de login no Chrome do Rafael; a sessão não digita senha. Falta o Rafael entrar e conferir o CO vs BB, flop K-high two-tone, c-bet de 33% (field 46,0%, GTO 38,8%, faixa 37,1–40,4%) |
| (d) supressão | ✅ parcial | 2 endereços suprimidos no Resend, os dois por bounce, nenhuma reclamação. O descadastro dos lotes em batch usa `List-Unsubscribe` mailto; o da broadcast usa o link do Resend |
| (e) 1º lote | ⛔ sem tamanho | o lote do R1 (Grátis sem login há 14+ dias, sem pagantes e sem ex-pagantes) só sai do AuraBusiness, que não tem ferramenta de leitura nesta sessão (o MCP `postgres-azure-analytics` aponta para um host que não existe). Caminhos: consertar o host do MCP (o banco de usuários é o AuraBusiness, no servidor `aura-production`) ou o Rafael exportar os e-mails pelo SQL 5.3 |

## Changelog

- Rodada 3 (23/10): decisões R1 a R6 do Rafael; R4 ampliada (gatilho B, quem não volta); rascunhos U2 e R2 com cupom; spec do cupom no Stripe (§12.1); tracking e segmento no Resend (§14).

- Rodada 2 (23/10): template v2 com prints; R4 reaberta com o cupom de ativação (§12); auditoria do Grátis no código e frases corrigidas (§13); G1 trocado por conferência logada; U2 com cupom.
- Rodada 1 (23/10): diagnóstico, segmentos, sequências, teste A/B e rascunhos A1, U1 e R1 (aura-marketing#12).
