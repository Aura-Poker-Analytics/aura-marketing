# Diagnóstico do funil da Aura (fase 1 do plano de marketing de nov/2026)

**Data:** 22/10/2026 · **Sessão:** `aura · plano de marketing` · **Skill:** `analytics`
**Fontes (todas lidas em 22/10, só leitura, só agregados):**
- GA4, property 506294082, 90 dias até 21/10;
- Stripe live (API, sem Sigma);
- Meta Ads, conta Aura Business;
- pagantes do WooCommerce e do NOWPayments informados pelo Rafael.

Os docs de jul–set não entram como prova.

> Amostras pequenas: os cortes abaixo têm de dezenas a poucas centenas de usuários. Servem para achar onde olhar, não para fechar taxa.

## 1. O funil em números (90 dias)

| Etapa | Usuários | Leitura |
| --- | --- | --- |
| Visitantes novos | 1.824 | 71% vieram do Paid Social (campanhas hoje pausadas) |
| Começaram o cadastro (`form_start`) | 102 | **5,6%** |
| Cadastraram (`sign_up`) | 40 | 39% de quem começa |
| Usaram um módulo (`analyze_result`) | 40 | O funil ordenado liga só 15 dos 40 cadastros a uso (ver §4) |
| Bateram no paywall (`gate_hit`) | 23 | |
| Clicaram em upgrade | 9 | 39% de quem bate no paywall |
| Checkout e compra | sem medição até 21/10 | |
| **Pagantes ativos hoje** | **16** | Stripe 9, Woo 5, NOWPayments 2. MRR no Stripe: ~R$ 708 + US$ 109 |

Ex-pagantes: **31** (Stripe e Woo cruzados, sem ativos, sem reembolsados e sem suprimidos). Brasil 30, Portugal 1. 22 deles pagaram pela última vez há mais de 6 meses.

## 2. Os três vazamentos, em ordem de tamanho

### V1. A landing quase não manda ninguém ao cadastro

| Host | Usuários | Duração média | Começaram o cadastro |
| --- | --- | --- | --- |
| `www.aurapoker.com` (landing) | 1.447 | 55 s | 4 (0,3%) |
| `www.aura.poker` (app) | 441 | 382 s | 98 |

- 32 dos 40 cadastros passaram por `/Login` do app.
- O tráfego pago caiu na landing: 1.288 visitantes, 8 começaram o cadastro.
- Quase todo cadastro vem de quem já chega ao app (direto, e-mail, bio).
- O clique no CTA da landing não é medido (`cta_click` é um follow-up pendente no aura-landing). Por isso não se sabe se o problema é o CTA, a passagem de domínio (`aurapoker.com` → `aura.poker`) ou o público.

**Leitura:** antes de comprar mais tráfego, medir e consertar a passagem da landing para o cadastro. É o maior vazamento e afeta todo canal que aponta para a landing, inclusive o e-mail, cuja regra é sempre linkar a landing.

### V2. O celular não chega ao formulário

| Aparelho | Visitantes | Começaram | Taxa |
| --- | --- | --- | --- |
| Desktop | 461 | 78 | 17% |
| Celular | 1.361 | 24 | **1,8%** |

O tráfego do Instagram (pago e orgânico) é quase todo de celular. O app de análise é de desktop. O caminho natural do celular é capturar o e-mail e mandar a pessoa para o desktop, e esse caminho não existe.

### V3. O paywall gera clique, e depois o funil some

23 batem no paywall, 9 clicam em upgrade, e nada é medido depois. O Stripe registra cerca de 3 assinaturas novas por mês. Não dá para saber quantos dos 9 cliques viraram compra.

## 3. Mercado

| País | Visitantes | Começaram | Cadastros | Pagantes ativos (Stripe) |
| --- | --- | --- | --- | --- |
| Brasil | 1.154 | 68 | 24 | 5 |
| **Portugal** | 99 | 10 | **7** | **3** |
| EUA | 314 | 0 | 0 | 0 |
| Reino Unido | 29 | 4 | 3 | 0 |
| Alemanha | 23 | 3 | 1 | 0 |
| Suécia, Irlanda, Canadá, Áustria, Holanda, Finlândia | 108 somados | 1 | 0 | 0 |

- **Portugal é o melhor sinal fora do Brasil:** 7 cadastros e 3 pagantes, com 99 visitantes, sem esforço dirigido. Fala português, paga em USD. Não estava na lista de países da Q8.
- EUA: 314 visitantes e nenhum cadastro, o que confirma deixá-los fora.
- Dos países-alvo da Q8, só o Reino Unido (3) e a Alemanha (1) cadastraram.
- Não há página de entrada em inglês com tráfego. O inglês converte o cadastro a 26%, contra 40% em PT.

## 4. Ativação

| Módulo | Viram | Rodaram análise |
| --- | --- | --- |
| Preflop | 49 | 39 |
| Postflop | 35 | 22 |
| Node-by-Node | 27 | 10 |
| Hotspot | 16 | 8 |
| Field Trends | 9 | — |

O Preflop é a porta de entrada. Os módulos de GTO (Modo GTO, Field Ranges com GTO) entraram em out/2026, sem histórico suficiente nesta janela.

## 5. Medição: o que impede decidir

| # | Falha | Efeito | Conserto | Dono |
| --- | --- | --- | --- | --- |
| M1 | `begin_checkout` e `purchase` sem nenhum evento desde 21/10 | Receita e checkout invisíveis. Com 0 `upgrade_click` no período, o zero pode ser só falta de compra. **Não está provado que estejam quebrados.** | Conferir com um checkout de teste até o `begin_checkout` (sem pagar), no DebugView. Depois, `purchase` pelo servidor (Measurement Protocol, follow-up do aura_api já descrito) | sessão aura-novofront / aura_api |
| M2 | Clique no CTA da landing não medido (`cta_click`) | V1 sem causa | Evento na landing, com o destino | sessão aura-landing (brief já existe) |
| M3 | Page_view do app em dobro (5 a 6 por sessão em `/field-ranges`) | Taxas por página e por sessão infladas | Desligar o page_view por histórico na medição otimizada do GA4 | **Rafael** (pendência do STATE desde 20/10) |
| M4 | Só `sign_up` é evento-chave | GA4 e Meta otimizam só por cadastro | Marcar `begin_checkout` e `purchase` como chave (o `begin_checkout` já foi marcado em 20/10, conferir) | Rafael, no GA4 |
| M5 | `sign_up` conta mais que `form_start` no celular e no Paid Social | Taxa de formulário não confiável nesses cortes | Conferir onde o `form_start` dispara no fluxo do celular | sessão aura-novofront |
| M6 | Sujeira: `loja.aurapoker.com` (10 sessões) e `localhost`; 7% de landing `(not set)`; `/Login` × `/login`, `/preflop` × `/pre-flop` | Ruído pequeno | Filtro de hostname no GA4; normalizar caminhos | Rafael (filtro) e front |
| M7 | Pixel: `CompleteRegistration` sem `fbp`/`fbc`; qualidade de correspondência entre 5 e 6,1 | O Meta não liga cadastro ao clique | `fbp`, `fbc` e `external_id` no evento, mais o envio pelo servidor (CAPI) | sessão aura-novofront / aura_api |
| M8 | Dimensão de usuário `aura_user_id` não criada | Não dá para ligar GA4 ao pagante | Criar a dimensão no GA4 | Rafael (pendência do STATE) |

## 6. Decisões do Rafael sobre o diagnóstico (22/10)

| # | Decisão | Fonte |
| --- | --- | --- |
| D1 | **Portugal entra como mercado prioritário**, junto com Reino Unido, Canadá, Alemanha, Holanda, Áustria e nórdicos | Rafael: "1 sim" |
| D2 | **A reconquista aponta para a landing**, que foi muito reformulada e deve causar impacto. Por isso, o `cta_click` da landing tem de estar medido antes de 02/11. | Rafael: "mas tivemos uma reformulação grande da landing, entao talvez seria bom pra causar WOW?" |
| D3 | **Conversão e medição antes do pago**, com sessões paralelas para o conserto | Rafael: "3 sim fique a vontade pra rodar subagentes pro conserto." |

## 7. O que muda no plano

1. **A fase 3 (conversão) sobe de prioridade e passa à frente do pago.** O primeiro trabalho é a passagem da landing ao cadastro (V1) e a captura de e-mail no celular para continuar no desktop (V2). Comprar tráfego antes disso repete os 1.288 visitantes pagos com 8 cadastros.
2. **A medição (M1, M2, M4, M7) é pré-requisito da verba**, como decidido na Q3.
3. **Portugal entra como candidato a mercado prioritário.** Decisão do Rafael na abertura da fase 2.
4. **A reconquista segue para 02/11, em PT.** Dos 31 ex-pagantes, 30 são do Brasil e 29 pagaram em BRL. A versão em inglês fica para 1 pessoa (Portugal paga em USD, mas fala português: mandar PT com preço em USD, ou só PT).
5. O e-mail aponta para a landing (regra), e a landing é o maior vazamento (V1). Para os ex-pagantes, que já têm login, vale abrir uma exceção e mandar o CTA direto para o app. **Decisão do Rafael.**

## 8. Consertos abertos em 22/10 (sessões paralelas, PRs em rascunho, sem merge)

| Falha | PR | O que faz |
| --- | --- | --- |
| M1, M5, M7 e caminhos duplicados | [aura-novofront#185](https://github.com/Aura-Poker-Analytics/aura-novofront/pull/185) | Prova que `begin_checkout` e `purchase` disparam (o zero era falta de checkout); garante que saiam antes do salto de página; `form_start` uma vez por tentativa; `fbp`, `fbc` e `external_id` com hash no `CompleteRegistration`; normaliza `/Login` e `/preflop` |
| M2 e V2 | [aura-landing#26](https://github.com/Aura-Poker-Analytics/aura-landing/pull/26) | `cta_click` em todo CTA para o app; linker entre domínios no gtag; captura de e-mail no celular atrás de `VITE_MOBILE_EMAIL_CAPTURE` (desligada) |
| Compra pelo servidor | [aura-api#120](https://github.com/Aura-Poker-Analytics/aura-api/pull/120) | `invoice.paid` → `purchase` no GA4 (Measurement Protocol) e `Subscribe` na CAPI da Meta, desligados por padrão |

**Pendências do Rafael para esses PRs entrarem:**
- App settings da API: `Ga4__Enabled`, `Ga4__MeasurementId`, `Ga4__ApiSecret`, `Meta__SubscribeFromInvoiceEnabled` e `Meta__AccessToken` (se faltar).
- Evento `invoice.paid` no webhook do Stripe.
- No GA4, registrar `cta_id`, `cta_destination` e `cta_lang` como dimensões de evento.
- Decidir a dupla contagem da primeira compra no GA4 (navegador e servidor). Recomendação da sessão da API: tirar do `purchase` do navegador a marcação de evento-chave.
- A captura no celular só deve ser ligada com uma automação no Resend que de fato mande o link.
