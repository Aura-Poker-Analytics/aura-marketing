# Grátis que não assina: plano de ataque por país e idioma

**Data:** 02/11/2026 · **Papel:** `casa:growth`, pela skill `campanha` · **Pedido:** Rafael, 02/11 ("redirecionar comunicações em inglês a depender do país") · **Meta que move:** Aura, 35 pagantes em 31/12 (marco de 24 em 30/11) e cadastros novos ≥ 10 por semana (`_ops/metas-trimestre.md`).
**Estado:** plano. **Nada foi enviado, gasto nem criado** no Stripe ou no Resend. Leitura só de agregados: `tbl_user` do AuraBusiness (SELECT), GA4 (property da Aura) e o cupom `R6eSQeTK` no Stripe live. Nenhum e-mail, nome ou nick foi lido ou gravado.
**Junto com este plano:** o primeiro e-mail EN da escada, em `content/email/gratis-por-pais/` (§8).

## 0. Resumo em 8 linhas

1. **O país está preenchido em 100% dos cadastros desde 09/2026 (35 de 35), mas em 0 dos 209 anteriores.** Na base Grátis inteira são 35 de 244 (14,3%). A pergunta "de onde vem o país" tem resposta para o fluxo novo; o estoque antigo continua sem resposta.
2. **As outras fontes não salvam o estoque.** `ultima_lat/long` está preenchida em 77 de 244, mas todas valem 0,0. O domínio do e-mail diz `.br` em 6 de 244 (2,5%). O criativo da Meta prevê PT bem (11 de 12) e prevê mal o EN (4 de 6). O GA4 tem `ui_lang` em 90 de 493 logados (18,3%) e só em agregado. Não existe coluna de idioma nem de fuso.
3. **Regra (Rafael, 02/11: "é só deduzir a lingua pelo país. se nao for BR ou PT mandar em ingles"):** PT só para BR e PT; EN para todo o resto, AO, MZ e CV incluídos; ES fica fora. **País vazio = PT.** Dos 35 com país, 26 são PT (74,3%). O idioma sai do país no dia do envio e **não se grava idioma no cadastro**.
4. **País vazio (209 do estoque antigo) fica em PT:** é a base antiga e brasileira, e se a mistura fosse igual à dos 35 com país, até 26% estariam no idioma errado. É um risco aceito pelo Rafael, sem trabalho de engenharia.
5. **O país muda três coisas, não só o idioma:** a moeda da oferta (BR em BRL, resto em USD), o horário de envio e o idioma do código. O VOLTE50 já cobre as duas moedas: o cupom `R6eSQeTK` tem `currency_options` com BRL 7500 e USD 1450 (lido no Stripe live com o campo expandido), então o EN usa o próprio VOLTE50.
6. **A escada tem de ser reajustada ao calendário:** o A2 em D2 fere a regra de 1 e-mail a cada 3 dias. Passa a D3 e o A3 a D6 (§4).
7. **Volume de EN é pequeno:** cerca de 1 a 2 cadastros EN por semana. Nenhum teste de idioma tem poder; a leitura é descritiva e mensal (§7).
8. **Nenhuma ficha pendente deste plano.** A oferta única (VOLTE50, 50% por 3 meses, também em dólar) e a regra de idioma por país (sem gravar `lang`) são decisões do Rafael de 02/11.

## 1. De onde vem o país e o idioma de cada Grátis

Base: Grátis que não assina = `plan_tier = 'trial'`, sem cliente nem assinatura no Stripe, sem superusuário e sem `@aurapoker.com`: **244 pessoas** (02/11). Dessas, 26 se cadastraram nos últimos 30 dias.

| Fonte | O que diz | Cobertura (de 244) | Serve? |
| --- | --- | --- | --- |
| `tbl_user.country` | país do cadastro | **35 (14,3%)**; 35 de 35 desde 09/2026; 0 de 209 antes | **Sim. Chave principal** para o fluxo novo |
| `tbl_user.ultima_lat/long` | última posição | 77 (31,6%), todas 0,0 | Não: valor de preenchimento, sem posição |
| `tbl_user.time` (time de poker, texto livre) | pista de origem BR | 40 de 209 sem país (19,1%); nomes de times brasileiros na maioria | Só como pista fraca; não vira regra |
| Domínio do e-mail | `.br` / `.pt` | 6 de 244 (2,5%); 234 são `.com`, `.net` e semelhantes | Não |
| `utm_campaign` / criativo da Meta | idioma do anúncio | 31 de 244 (12,7%) | Parcial: criativo `-br` bate com PT em 11 de 12; criativo `-en` bate com não-PT em 4 de 6 |
| `heard_about`, `referrer` | origem declarada | 34 e 6 | Não diz idioma |
| GA4 `ui_lang` (usuário logado) | idioma da interface | 90 de 493 logados desde 01/09 (18,3%): 69 em português e 21 em inglês | Só agregado: sem ligação por pessoa |
| GA4 por país | geo por IP | quase todo o tráfego, mas por visitante | Serve para dimensionar o público, não para escolher o e-mail de uma pessoa |
| Moeda do checkout | BRL ou USD | só quem abriu checkout: 3 usuários desde 01/09 | Não cobre o Grátis |
| Fuso | — | não existe coluna | Não |
| `lang` no cadastro | — | não existe coluna | Decidido em 02/11: não se grava. O idioma sai do país no dia do envio |

Como o país é distribuído nos 35 com dado: BR 23, GB 4, PT 3, VE 1, RU 1, AU 1, IT 1, DE 1. Em PT (BR e PT): 26 (74,3%). Em EN (o resto): 9 (25,7%).
O tráfego do site em geral é bem mais internacional que o cadastro: no GA4 desde 01/08, os visitantes novos são 754 do Brasil em português, 274 dos EUA em inglês, 92 de Portugal e 40 do Reino Unido. Quem se cadastra é majoritariamente brasileiro; quem só visita não é.

**Pontos cegos assumidos:**
- O estoque antigo (209) não tem país. Não há como inferi-lo só pelo que está no banco. O fallback é PT.
- O `time` não é geografia; foi medido para saber se rende e não rende.
- GA4 `ui_lang` e `aura_user_id` existem, mas o GA4 não exporta a lista por pessoa pelo conector. Só serve de conferência de proporção.

## 2. Regra de idioma

| País do cadastro | Idioma do e-mail | Moeda da oferta | Observação |
| --- | --- | --- | --- |
| BR | PT | BRL | Brasil é 65,7% dos 35 com país (23) |
| PT | PT | a confirmar | Idioma PT. A moeda que o checkout mostra a quem está em Portugal precisa de conferência na primeira leitura |
| qualquer outro, AO, MZ e CV incluídos (GB, IE, US, CA, AU, NZ, DE, NL, nórdicos, IT, RU, VE...) | EN | USD | Regra do Rafael de 02/11. A Aura só tem preço em BRL e USD |
| vazio | **PT** | BRL | Fallback. 74,3% dos que têm país são PT, e o estoque antigo veio da comunidade brasileira |
| ES (MX, AR, CO, ES...) | **fora por ora** → EN | USD | Só abre com 20 cadastros hispânicos em 30 dias. Hoje: 1 (VE), que vai em EN pela regra |

Exceções por pista, em ordem: (1) se o país existe, ele manda; (2) se o país é vazio e o criativo da Meta é `-en`, **não** muda: o criativo `-en` acerta pouco (4 de 6). Ou seja: **só o país muda o idioma.**

Chave de dados: nenhuma lista em arquivo. O lote é feito no dia, com id e idioma, e o e-mail só vive no Resend.

## 3. Quem recebe o quê: o público "Grátis que não assina"

O calendário (`_ops/email-calendario-2026-11.md`) ordena os públicos assim: ex-pagante > assinatura parada no Woo > **Grátis antigo (R2)** > **cadastro novo da Meta (A1)**. Este plano fica dentro dessa ordem e define o que acontece depois de cada porta de entrada.

| Coorte | Quem | Hoje | Idioma | Porta |
| --- | --- | --- | --- | --- |
| **C1 Novo** | cadastro há até 14 dias | 18 da Meta (13 em português, 5 em inglês) | por país | A1 |
| **C2 Antigo** | cadastro há mais de 30 dias, sem login recente | 184 (147 cupom, 37 controle) | PT (sem país) | R2 de 04/11 |
| **C3 Com uso** | fez ao menos 1 análise, no Grátis | não medido por pessoa (GA4: 55 usuários com `analyze_result` desde 01/09) | por país | espera `first_analysis_at` (P2) |
| **C4 Bateu no paywall** | teve `gate_hit` | GA4: 25 usuários desde 01/09 | por país | U1 e U2 |

Sempre excluídos: quem assinou (Stripe, Woo e NOWPayments conferidos antes de cada envio), superusuário, `@aurapoker.com`, descadastro e bounce.

## 4. A escada, em PT e EN

**Ajuste obrigatório ao calendário.** O plano anterior (`ativacao-meta-escada.md` §1) põe A2 em D2 e A3 em D5. Com A1 em D0, o A2 em D2 fica a 2 dias do A1 e fere o mínimo de 3. **A2 passa para D3 e o A3 para D6.** O mesmo vale para o U1: se o `gate_hit` cai a menos de 3 dias do último envio, o U1 espera e sai no 3.º dia (a fila é por pessoa, não por sequência).

| Passo | Momento | Gatilho (comportamento) | O que diz | Oferta e código | PT | EN |
| --- | --- | --- | --- | --- | --- | --- |
| **A1** | D0 (o dia do sim do Rafael) | cadastro novo, ainda sem e-mail da Aura | Abra o spot do Grátis, veja o field e a faixa GTO; pede o buy-in | sem oferta | `ativacao-meta/a1-pt.html` | `ativacao-meta/a1-en.html` |
| **A2** | A1 + 3 dias | **não fez análise** | O spot da semana no Field Exploits, aberto no Grátis | sem oferta | `a2-pt.html` | `a2-en.html` |
| **A3** | A2 + 3 dias | **segue sem análise** | "Travou em algum passo?" | sem oferta | `a3-pt.html` | `a3-en.html` |
| **U1** | até 24 h do `gate_hit`, respeitando os 3 dias | **bateu no limite** | O spot que você abriu continua do outro lado do cadeado | sem oferta | `followup-u1-paywall.html` | `ativacao-meta/u1-en.html` |
| **U2** | 72 h depois do `gate_hit`, sem assinar | bateu no limite e não assinou | 50% nos 3 primeiros meses do Individual mensal | **`VOLTE50` em BRL e em USD** (`currency_options`); 20% de controle sem código | `ativacao-meta/u2-pt.html` (ajustar a oferta) | `ativacao-meta/u2-en.html` (ajustar) |
| **R2** | 04/11, 10h BRT (calendário) | Grátis antigo, sem login depois do R1 | 8 novidades em 60 dias + o código | `VOLTE50` até 30/11, só 1.ª compra; 20% de controle | `followup-r2-cupom.html` | **EN novo** (§8), com o `VOLTE50` em dólar |
| **R3** | 27/11, 10h BRT (3 dias antes do vencimento) | R2 recebido, sem compra | "Seu código vence em 3 dias", sem repetir as novidades | o mesmo código | a escrever depois da leitura do R2 | idem |

**Janela de envio por idioma.** PT às 10h de Brasília, como o calendário. EN às **15h de Brasília** (18h em Londres e Dublin, 13h em Nova York): o EN é majoritariamente Reino Unido e Irlanda, e 10h de Brasília cai às 13h lá, no meio do expediente. Hipótese a medir, não regra.

**Saída da escada:** assinou, descadastrou, bounce, ou 3 envios sem abertura (regra do MKT-D4).

**Fila por pessoa (regra de implementação):** cada pessoa tem uma data do último envio. Qualquer passo só entra se `hoje − último envio ≥ 3 dias`; senão espera. Um passo de coorte maior vence um de coorte menor no mesmo dia. Isso cobre também o broadcast de lançamento, que conta como envio.

## 5. Como o R2 de 04/11 e o A1 entram no desenho

| Data | Envio | Quem | Idioma | Condição |
| --- | --- | --- | --- | --- |
| **04/11, 10h** | R2 com `VOLTE50` e as novidades (calendário) | 184 do Grátis antigo | PT (sem país) | sim do Rafael |
| **A1: no dia do sim** | A1 | os 18 de 30/10 a 01/11 (13 em português, 5 em inglês), refeito no dia | por país | sim do Rafael; segmento próprio depois do R2 (a HUB combina) |
| A1 + 3 | A2 | quem não analisou | por país | checagem no GA4 na véspera |
| A1 + 6 | A3 | quem seguir sem análise | por país | idem |
| 27/11, 10h | R3 | R2 sem compra | PT, e EN para quem já tiver país | leitura do R2 em D+3 (07/11) e D+7 (11/11) |

Não há cruzamento: os 18 do A1 se cadastraram depois do R1 (28/10); o R2 é do Grátis antigo. A lista de cada envio é refeita no dia e exclui quem está num público de prioridade maior. O A1 pode sair no mesmo dia do R2: são pessoas diferentes.
**Efeito da regra de 3 dias no A2 que estava marcado para 04/11:** como o A1 ainda espera o sim, o A2 não pode sair em 04/11. Se o A1 sair em 03/11, o A2 vai a 06/11 e o A3 a 09/11; se sair em 04/11, a 07/11 e a 10/11.

## 6. Fichas ao Rafael (dinheiro e envio são dele)

**Resolvido em 02/11 (HUB), sem ficha:**
- **Cupom em dólar:** não é preciso criar nada. O `VOLTE50` (`R6eSQeTK`) vale em BRL (7500) e em USD (1450, 50% de US$ 29), 3 meses, só no Individual, até 30/11 (`currency_options`, lido no Stripe live). A primeira versão deste plano dizia que só valia em BRL: o conector que usei não mostra `currency_options`.
- **Oferta única:** o Grátis que não assina tem uma oferta só, o `VOLTE50` (50% por 3 meses), no R2, no U2 e no R3. É a decisão do Rafael de 02/11; o 30% no 1.º mês (`Ph7y2HU9`) sai da escada do Grátis. Guardrail: se mais de 60% das assinaturas novas em 8 semanas usarem cupom, cortar ou reduzir.

**LANG-COUNTRY (respondida pelo Rafael em 02/11, sem ficha):** "nao precisa. é só deduzir a lingua pelo país. se nao for BR ou PT mandar em ingles." Não se grava `lang` nem `country` novos: o idioma sai do `country` no dia do envio, PT só para BR e PT, EN para o resto, país vazio em PT. O estoque antigo sem país segue em PT.

**Envio** (o portão não muda): cada passo continua com o "sim" digitado, por envio. Nada deste plano autoriza envio.

## 7. Métrica de sucesso por coorte e idioma (funil G0)

Funil: **cadastro → 1.ª análise → `gate_hit` → `upgrade_click` → `begin_checkout` → `purchase`**, com o idioma e a coorte como cortes. Fonte do passo: GA4 (evento, com `utm_campaign` do e-mail) e Stripe (resgate do código). Janelas: D+3 e D+7 depois do último e-mail de cada passo.

| Coorte × idioma | Métrica principal | Métrica de apoio | Base hoje | Fonte |
| --- | --- | --- | --- | --- |
| C1 Novo, PT | cadastro → 1.ª análise em 7 dias | clique no A1 (`cta_click`) | GA4: 55 usuários com análise para 27 cadastros (`sign_up`) desde 01/09, sem leitura por coorte | GA4; `first_analysis_at` depois de P2 |
| C1 Novo, EN | idem | idem | 4 de 18 no primeiro lote | idem |
| C2 Antigo, PT | login em 7 dias depois do R2 e **resgate do `VOLTE50`** | abertura, clique | 0 resgates (cupom criado em 02/11) | Resend, Stripe |
| C4 Bateu no paywall, PT e EN | `gate_hit` → `purchase` em 14 dias | resgate do código; cupom × controle | 25 usuários com `gate_hit`; 3 com `begin_checkout`; 3 com `purchase` desde 01/09 | GA4, Stripe |
| Todos | descadastro por envio | bounce | < 1% (referência do plano de follow-up) | Resend |

**Tamanho e leitura honesta.**
- Novos por semana: ~6 (26 em 30 dias; meta do trimestre ≥ 10). EN: cerca de 1 a 2 por semana. Em 4 semanas o EN soma ~6 a 8 pessoas.
- Com dezenas de pessoas, só se distingue diferença enorme do acaso: **nenhum teste de idioma ou de cupom declara vencedor.** A leitura é descritiva e agrupada em 4 semanas.
- O segmento de cupom do R2 (147 contra 37 de controle) é a única comparação com algum poder, e mesmo ela é direcional.

**Regra de decisão, escrita antes do número:**
1. Se o EN chegar a ≥ 20 destinatários em 28 dias e **0** assinaturas, não se muda a oferta: abre-se uma ficha de investigação (copy, moeda, horário), sem cortar o EN.
2. Se o resgate do VOLTE50 em dólar for 0 com ≥ 10 cliques de EN, a hipótese passa a ser preço em dólar, não idioma.
3. Se a taxa de descadastro de qualquer coorte passar de 1% em um envio, pausa e ficha.
4. A leitura de D+3 e D+7 vai para o `resultado.md` da campanha; quem lê é o G1.

## 8. O primeiro e-mail EN da escada

**R2 EN (para o público EN do Grátis que não assina):** reaproveita o `novidades()` do #60 com a lista em inglês, e uma caixa com o VOLTE50 em dólar.
- `content/email/gratis-por-pais/r2-en-cupom.html`: com o `VOLTE50` (US$ 14,50 por mês em vez de US$ 29).
- `content/email/gratis-por-pais/r2-en-controle.html`: o mesmo e-mail sem código, para os 20% de controle.
- Gerador: `content/email/_template/build_gratis_pais.py`. Prévia no navegador em 680 e 390 px e revisão do `casa:revisor` registradas em `content/email/gratis-por-pais/notas.md`.
- Bloqueio: o sim do Rafael. O `[SPOT]` não existe aqui, porque o R2 usa as novidades.

## 9. O que fica de fora

- ES, até 20 cadastros hispânicos em 30 dias.
- A automação por gatilho (MKT-D4: depende da ficha de LGPD). O lote continua manual e semanal.
- Qualquer contato, segmento ou cupom criado: tudo isso é "sim" do Rafael.
- Backfill do país do estoque antigo: não será feito (decisão de 02/11).

## 10. Consultas e fontes

- `tbl_user` (AuraBusiness, SELECT agregado, 02/11): base de 244 por `plan_tier = 'trial'`, sem Stripe, sem superusuário, sem `@aurapoker.com`; contagens de `country`, `ultima_lat/long`, `time`, domínio do e-mail, `utm_*` e `heard_about`, por mês de cadastro.
- GA4 (property da Aura), 01/08 a 02/11: `country × language × newUsers`; `customUser:ui_lang` com `aura_user_id` preenchido; `eventName` × `totalUsers` para `sign_up`, `analyze_result`, `gate_hit`, `cta_click`, `begin_checkout`, `purchase`.
- Stripe live (somente leitura): cupom `R6eSQeTK`, `amount_off` 7500, `currency` brl, 3 meses, 184 usos, `redeem_by` 30/11/2026.
- Preço do Individual em dólar: US$ 29 (`content/email/reconquista-2026-11/sequencia.md`, oferta do e-mail 1).
- Calendário: `_ops/email-calendario-2026-11.md` (02/11).
