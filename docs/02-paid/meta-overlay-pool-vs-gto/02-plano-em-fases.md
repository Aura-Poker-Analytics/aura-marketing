# 02 · Plano de Meta Ads em fases: R$ 1.000 com o Modo GTO no ar

**Revisão:** 25/09/2026, substitui a versão de 22/09 (R$ 1.400 + R$ 2.940) e o teto de R$ 200 de 24/09 (B3) · **Status:** plano. Nada foi criado, editado, pausado ou ativado na Meta; a conta e o pixel foram só lidos · **Linha de base:** `01-linha-de-base.md`

## 0. O que mudou em 25/09, e a tese em uma tela

Duas mudanças do Rafael:

1. **Orçamento total de R$ 1.000.** Não é mais uma fase de pré-lançamento seguida de um lançamento agressivo; é um teste só.
2. **O Modo GTO está no ar.** O anúncio leva ao plano GTO com checkout, e a lista de espera (B5) deixa de ser o destino. Some a Fase 1 de "lista de espera", some o `Lead` como evento de otimização.

O que não mudou: a mídia de setembro morreu por público errado no BR, configuração mexida antes do gate e um funil que não fechava, não por falta de criativo (`01 §2`). Com R$ 1.000 isso pesa mais, não menos: não há verba para errar duas vezes.

| | Resposta curta |
|---|---|
| O que R$ 1.000 compra | **10 a 40 cadastros** no histórico da conta (§1). Nenhum evento sai da fase de aprendizado |
| Evento de otimização | **`CompleteRegistration`** (cadastro grátis). Não a venda, não `InitiateCheckout` (§1.3) |
| Público | um só: **identidade EN, 11 países da Europa**, a receita da DISC02-EU (§2.1) |
| Criativos | **3**, todos já produzidos, re-renderizados sem o "500M+" (§8) |
| Fases | Fase 1 · teste, **R$ 600** (3 × R$ 20/dia × 10 dias) · Fase 2 · concentração, **R$ 400** (R$ 40/dia × 10 dias), só se o gate passar |
| Para gastar mais | uma assinatura GTO atribuída à Meta **e** o CAC estimado com número medido (B4) abaixo do alvo (§6) |
| O que R$ 1.000 não prova | que o CAC fecha. Prova o custo por cadastro de cada criativo, se o funil conta cada passo e, com sorte, a primeira venda |

## 1. Economia unitária e o que R$ 1.000 compra

### 1.1 Os números que decidem

| Item | Valor | Fonte e estado |
|---|---|---|
| Plano GTO, mensal | US$ 49 · R$ 250 | A13 (24/09), landing #11 `pricing.ts`. **R$ fica fora do criativo até a A14** |
| Plano GTO, semestral | US$ 249 · R$ 1.245 | idem |
| Plano GTO, anual | US$ 439 · R$ em disputa (A16) | idem |
| Vida média do assinante | **desconhecida** | Stripe não lido; B4 autoriza a leitura agregada |
| Grátis → pago por coorte | **desconhecido** | AuraBusiness não lido; B4 autoriza, com o sim do Rafael na sessão |
| **CAC-alvo (hipótese)** | **R$ 500** (≈ US$ 98) | 2 meses do plano GTO; vira número real quando o Stripe der a vida média. Era R$ 600 com o GTO a R$ 319 |

**Critério universal (mantido):** a Meta compra cadastro. O CAC é `custo por cadastro ÷ taxa cadastro → pago`. Com o alvo de R$ 500, cada custo por cadastro exige uma taxa mínima:

| Custo por cadastro | Taxa cadastro → pago mínima para o CAC ≤ R$ 500 |
|---:|---:|
| R$ 25 | 5,0% |
| R$ 44 | 8,8% |
| R$ 60 | 12,0% |
| R$ 75 | 15,0% |
| R$ 103,53 (média da conta) | 20,7% |

Acima de R$ 60 por cadastro, o CAC só fecha com uma conversão que nenhum SaaS de nicho sustenta com tráfego frio. Por isso **R$ 60 é o teto de custo por cadastro deste plano**.

### 1.2 Quantas conversões R$ 1.000 compra (histórico da conta, `01 §2`)

| Referência histórica de custo por cadastro | Cadastros com R$ 1.000 | Assinaturas se 5% pagarem |
|---|---:|---:|
| Média da conta, jul–set (R$ 103,53) | 9–10 | 0,5 |
| DISC02-EU inteira, otimizando cadastro (R$ 75,48) | 13 | 0,7 |
| Melhor criativo EN, `disc02-plataforma-mda-en` (R$ 62) | 16 | 0,8 |
| Melhor célula BR, PIONEIRO (R$ 44,20) | 22 | 1,1 |
| Janela de identidade EN, 02–06/09 (~R$ 25; 4 cadastros, amostra minúscula) | 40 | 2,0 |

### 1.3 Isso tira a Meta da fase de aprendizado? Não

A Meta sai do aprendizado com cerca de **50 eventos de otimização por conjunto de anúncios em 7 dias**. Com R$ 1.000 em ~20 dias, a verba é ~R$ 50 por dia somando tudo:

- **A venda (`Subscribe`, que a CAPI já dispara; `Purchase` não existe):** 0 na vida da conta. Mesmo no melhor cenário, 1 a 2 em todo o teste. Seriam precisos ~50 por semana: **impossível**.
- **`CompleteRegistration`:** para 50 por semana num conjunto, a R$ 60 cada, seriam R$ 3.000 por semana. O plano gasta ~R$ 140 a R$ 280 por semana por conjunto e compra de 2 a 11 cadastros. **Também não sai**; o conjunto fica em "aprendizado limitado" o tempo todo.
- **`InitiateCheckout`:** tem menos volume que o cadastro, porque o checkout vem depois do cadastro no funil, e hoje **não existe no pixel** (0 eventos nos últimos 7 dias, e nenhum código dispara, `§3.2`). **Pior ainda.**

**Consequência honesta:** com R$ 1.000, a Meta não "aprende" a achar comprador. O que o teste faz é **comparar três criativos pelo mesmo evento**, com o público fixo que já produziu, e medir, por fora da Meta, quantos desses cadastros chegam ao checkout e pagam. Otimizar por `CompleteRegistration` é escolher o evento mais profundo que existe com volume para a Meta ter *algum* sinal.

## 2. Quem é o público

Os arquétipos de 22/09 continuam valendo; nenhum foi validado em entrevista.

- **A · O reg de MTT que já paga solver.** Família PokerStars, ABI de US$ 11 a US$ 109, BR ou Europa. O solver dá a linha de equilíbrio, o field do buy-in dele não joga equilíbrio. É o comprador do plano GTO.
- **B · Quem estuda a fundo e dá aula.** Compra a profundidade e multiplica. Dois dos três pedidos dele (EV por mão, eixo de etapa) o produto ainda não atende; o anúncio não promete.
- **C · O grinder subindo de limite.** Sensível a preço, entra pelo grátis. Não é público de mídia paga.

**Para quem não é:** apostador de bet e cassino, jogador casual de app social, só cash, só GGPoker/Party/888 (0% do lake), quem procura "ganhar dinheiro rápido".

### 2.1 Por que um mercado só, e por que EN

Com R$ 1.000, dois mercados dividem o sinal ao meio e nenhum dos dois conclui nada. O mercado escolhido é **identidade EN** (interesses PokerStars + Professional Poker Player; IE, NL, NO, SE, GB, FI, DK, AT, PT, DE, MT; 21–50):

1. **É o único recorte que já produziu** a preço aceitável: ~R$ 25 por cadastro na janela de 02–06/09, com o conjunto a R$ 20/dia (`01 §2`). Foi trocado com 5 dias de vida e morreu. Aqui ele reabre igual e **não é tocado antes do gate** (`PLAYBOOK-midia-paga-do-zero.md §8.6`).
2. **O checkout em dólar não depende da A14.** A divergência medida é do real (R$ 762/1.325 contra R$ 745/1.295 da landing). Quem vem pela página em inglês paga em dólar.
3. **Não tem o ruído de bet** que contaminou o interesse "poker" no IG BR (`plano-fuga-das-bets.md`).
4. **O app e o Modo GTO são em inglês.** O cadastro não troca de idioma no meio do caminho.

O custo: CPM de R$ 35 a R$ 48, de 5 a 10 vezes o do BR, e o BR é 75,5% do tráfego da landing. **O BR fica para quando houver CAC medido**: ele pede um teste próprio (Advantage+ sem interesse, criativo em PT, a A14 fechada) e não cabe em R$ 1.000 junto com o EN. Se o Rafael preferir o BR mesmo assim, a troca é de um conjunto por outro, nunca dos dois ao mesmo tempo.

## 3. O funil com o Modo GTO no ar, e o que tem de ser verdade antes do 1º real (Fase 0, R$ 0)

### 3.1 O caminho

```
anúncio (Reels/Feed/Stories IG+FB, identidade EN)
  │  utm_source=meta · utm_medium=paid_social · utm_campaign=gto-r1000 · utm_content=<slug do criativo> · fbclid
  ▼
landing /?lang=en (home; /gto quando houver o R6) — aura-landing #11 em modo de lançamento:
  │  VITE_LAUNCH_MODO_GTO=1, VITE_LAUNCH_FIELD_VS_GTO=0
  │  PageView (pixel, só com consentimento) · CTA de cadastro, ou "Assinar o Modo GTO" no card do plano
  │  buildAppUrl repassa utm_* + fbclid (+ fbp e mc=1 com consentimento) + lang
  ▼
app /Login?tab=signup  — SEM parâmetro de plano
  │  CompleteRegistration (pixel + CAPI)  ← evento de otimização
  ▼
dentro do app: clique no Modo GTO → modal de upgrade (A1 do brief 12) → Stripe Checkout do plano GTO
  │  ← 🔴 HOJE O FRONT NÃO PEDE O PLANO GTO NO CHECKOUT (§3.2); é parte do go-live
  │  InitiateCheckout  ← NÃO EXISTE
  ▼
assinatura paga
     Subscribe (CAPI, no checkout.session.completed)  ← EXISTE; Purchase não existe e não é preciso
```

**Home ou `/gto`:** os três criativos desta rodada vendem a plataforma de field, não o toggle (§8). Por isso o destino deles é a **home** (`/?lang=en`), cujo hero no #11 já é a janela do Postflop com o Modo GTO ligado: o anúncio mostra o field, e a página mostra o field e o GTO lado a lado. A **`/gto`** (página C, "Criar conta e ver o gap") fica para o R6, o anúncio que vende o toggle, quando ele for produzido. Nas duas, o card do plano GTO mostra preço em modo de lançamento. O diagrama acima vale para as duas. **A lista de espera deixa de ser destino** (B5 aplicado: Resend agora, rota na API só com orçamento maior). Com a flag do Modo GTO ligada, o formulário para de oferecer o Modo GTO e só sobra o Field vs GTO. O `Lead` que ele dispara não entra na otimização.

**`VITE_LAUNCH_FIELD_VS_GTO` fica desligada.** Ligada, ela publica "spots novos todo mês" no card Top e no FAQ, e essa é a promessa da A12b, que espera a HUB.

### 3.2 Evento, Pixel/CAPI e UTM: o que existe e o que falta

Levantado em 25/09, só leitura: código da landing na branch do #11 (`feat/landing-redesign`), app e API na `main` e o pixel `1405949840871947` pelo MCP da Meta, nos últimos 7 dias.

| Passo | Existe hoje | Falta | Dono |
|---|---|---|---|
| **UTM e `fbclid` landing → app** | ✅ no #11: `buildAppUrl` (`src/lib/appUrl.ts:43-74`) repassa `utm_*` e `fbclid` (URL atual → último toque → primeiro toque), `lang` sempre, `fbp` e `mc=1` só com consentimento. Na landing em produção **não**: é o furo medido em 22/09 | **merge do #11** | Rafael |
| **UTM no cadastro** | ✅ app: `marketingAttribution.ts` guarda em `aura_attribution_v1` e manda no cadastro. API grava `UtmSource/Medium/Campaign/Term/Content`, `Referrer`, `Fbp` e `Fbc` no `tbl_user` (`TblUser.cs:108-122`) | ⚠️ o app trava o **primeiro toque**: quem já tinha registro fica com a origem antiga (acoplamento landing → app já registrado no STATE do aura-main). No público frio EN pesa pouco | sessão própria no `aura-novofront` |
| **`PageView`** | ✅ landing e app. Landing: só depois do "Aceitar" no banner (opt-in). App: opt-out | — | — |
| **`CompleteRegistration`** (evento de otimização) | ✅ pixel no app (`eventID reg_<user_id>`) **e** CAPI na API (`MetaCapiService.cs`, mesmo `event_id`, com `fbc`/`fbp`). Medido no pixel: 3 eventos nos últimos 7 dias, 2 deles pelo servidor, então a CAPI está viva | a EMQ e a cobertura de `fbc` não foram relidas desde 22/09 (EMQ do `PageView` 6,1; `fbc` 7,7%). Com o #11 no ar, o `fbc` deve subir; conferir no Events Manager no D1 | Rafael (Events Manager) |
| **Checkout do plano GTO a partir do anúncio** | ⚠️ a API aceita `planId: gto` e moeda (`CreateCheckoutSessionRequest.cs`, `ResolvePriceId`) | 🔴 **o front da `main` não pede o plano.** `CreateCheckoutSessionRequest` do app (`src/types/api/requests.ts:245-249`) só tem `userId`, `billingOptionId` e `currency`. Nenhum `plan`/`tier` na URL, nem no Login, nem na Minha Conta: **hoje um cadastro novo só consegue comprar o Individual.** O conserto é o A1 do brief 12 (o modal de upgrade conhecer o tier GTO), que está no roteiro do go-live (A7). A landing também não passa plano (`docs/lancamento-modo-gto.md`, "sem parâmetro de plano") | go-live do Modo GTO (Rafael) |
| **`InitiateCheckout`** | ❌ não existe em lugar nenhum (0 no pixel em 7 dias; nem front nem API) | não bloqueia o teste: a otimização é por cadastro. Para ler cadastro → checkout por criativo, basta **contar as Checkout Sessions criadas no Stripe por conta com `utm_content`**, em agregado. Se for criado depois, `fbq('track','InitiateCheckout')` no `handleSubscribe` da Minha Conta | leitura: sessão de medição (B4) |
| **Venda (`Subscribe`)** | ✅ CAPI na API, no `checkout.session.completed`, `event_id sub_<subscriptionId>`, com guarda de idempotência e fora de winback e legado | ⚠️ `currency` fixa em `"usd"` e o `value` sai de um mapa de price id. **Conferir que os 6 price ids do GTO estão no mapa**, senão a venda do GTO chega sem valor ou não chega. Nenhuma venda nos 7 dias, então nada foi provado em produção. Evento `Purchase` não existe; para a Meta, `Subscribe` é o evento de assinatura e basta | sessão do overlay (go-live) |
| **GA4** | ✅ `sign_up` no app; `generate_lead` e `cta_click` na landing | ❌ `begin_checkout` e `purchase` não existem. Não bloqueia: a venda é medida pelo Stripe e pelo AuraBusiness (B4), não pelo GA4 | — |
| **Lista de espera** | ✅ no #11: função do SWA → Resend, com `Lead` no pixel | **deixa de ser destino** (B5). Fica ligada só para o Field vs GTO | — |

**O relatório de UTM que fecha a conta** (sem dado pessoal, dentro da B4): cadastros por `utm_content` com `utm_campaign = gto-r1000`, e quantos deles têm assinatura GTO paga em 7, 14 e 30 dias. É um `SELECT count(*) … GROUP BY` no AuraBusiness, e **só roda com o sim do Rafael na sessão**.

### 3.3 Fase 0: o mínimo antes do primeiro real

Doze itens em 22/09 viraram oito, porque o #11 resolveu o repasse de UTM e o Modo GTO trocou a lista de espera pelo checkout. Cada um tem a sua prova, e nenhum real vai para mídia com algum deles vermelho.

| # | Item | Pronto quando (prova) | Dono |
|---|---|---|---|
| 0.1 | **Modo GTO no ar** para um assinante GTO (flag `GtoOverlay:Enabled`, deploy da API, re-promote do flop) | smoke com login real: o toggle responde 200 com o selo "pronta" num par coberto | Rafael (roteiro do doc 08 §8.4/§8.5) |
| 0.2 | **Um cadastro novo consegue comprar o plano GTO** (A1 do brief 12: o modal de upgrade conhece o tier GTO e abre o checkout do GTO) | uma conta de teste sai do cadastro, clica no Modo GTO, chega ao Stripe Checkout do **GTO** (não do Individual) e vê o preço em US$ | go-live |
| 0.3 | **Landing #11 mergeada** com `VITE_LAUNCH_MODO_GTO=1` e `VITE_LAUNCH_FIELD_VS_GTO` desligada | `www.aurapoker.com` servindo hero "New · GTO Mode", card GTO com preço; FAQ sem "spots novos todo mês" | Rafael |
| 0.4 | **UTM atravessa até a conta** | um clique de teste com `utm_campaign=gto-r1000-teste` gera conta com `UtmCampaign` preenchido (contagem agregada) | Rafael (a leitura no AuraBusiness pede o sim dele) |
| 0.5 | **`Subscribe` do GTO chega à Meta com valor** | os price ids do GTO no mapa do CAPI; conferido no código ou numa venda de teste | sessão do overlay |
| 0.6 | **Os 3 criativos re-renderizados sem "500M+"** (§8.2), com o BOARD01 pushado antes (§9, item 10) | três `.mp4` novos com o selo "400K+ tournaments · 7 rooms", conferidos no quadro | sessão de marketing (local, R$ 0) |
| 0.7 | **Conta de anúncio pronta:** forma de pagamento válida, verificação da empresa, domínio `aurapoker.com` verificado, 2FA | Centro de Segurança e Configurações de pagamento no BM | Rafael |
| 0.8 | **Filtro anti-bet nos comentários** do IG | a lista de `plano-fuga-das-bets.md §2C` ativa | Rafael |

Ficou de fora de propósito: cadastro em PT e e-mail D0 (o teste é em EN), públicos de retargeting (sem verba para eles), report de coorte automatizado (a leitura agregada da B4 substitui) e o personagem de IA (nenhum dos três criativos usa o analista).

## 4. Fase 1 · Teste de criativo (R$ 600, 10 dias)

### 4.1 Estrutura

| Campanha | Conjunto | Público | Otimização | Orçamento |
|---|---|---|---|---:|
| **GTO-R1000 · teste** (objetivo Leads, conversão no site, evento `CompleteRegistration`, como a DISC02-EU; **sem** CBO) | T1 · `<criativo 1>` | identidade EN (§2.1) | `CompleteRegistration` | R$ 20/dia |
| | T2 · `<criativo 2>` | o mesmo, idêntico | idem | R$ 20/dia |
| | T3 · `<criativo 3>` | o mesmo, idêntico | idem | R$ 20/dia |

- **Um criativo por conjunto** (ABO), como na DISC01: verba igual garantida por criativo. Com três anúncios num conjunto só, a Meta põe quase tudo no primeiro que render clique barato, e os outros dois nunca recebem verba para serem julgados.
- **R$ 20/dia por conjunto** é o diário da janela que produziu (DISC02-EU, 02–06/09).
- **Posicionamentos:** Reels, Stories e Feed de IG e FB. **Audience Network desligada.**
- **Atribuição:** 7 dias após o clique, 1 dia após a visualização (padrão).
- **Os 18 mercados que a Meta lista como proibidos para gambling** ficam fora, por precaução (`07 §1`). Nenhum dos 11 países está nessa lista, mas a checagem é por anúncio.
- **Nomes** (viram `utm_content`): o slug do criativo, sem sufixo novo, para bater com o histórico.

**Duração:** 10 dias corridos, D1 a D10. **Total:** 3 × R$ 20 × 10 = **R$ 600**.

### 4.2 Critérios de corte, escritos antes de olhar

Meta de custo por cadastro: **≤ R$ 60** (§1.1). Os cortes são por criativo, e nenhum outro toque é permitido antes do D10: nada de trocar público, otimização ou orçamento no meio da janela (anti-padrão `PLAYBOOK §8.6`, que custou o único recorte bom de setembro).

| Quando | Regra | Ação |
|---|---|---|
| D3 | sessão média na `/gto` vinda do conjunto < 5 s (GA4, por `utm_content`) | pausa o conjunto: é tráfego de bot ou bet |
| a qualquer momento | gasto ≥ **R$ 120** (2× a meta) com **0 cadastro** | pausa o conjunto |
| D7 | custo por cadastro > **R$ 90** (1,5× a meta) | pausa o conjunto; a verba não é redistribuída (sai da conta, não do teste) |
| D10 | fim do teste | o vencedor é o de **menor custo por cadastro, com ≥ 2 cadastros e custo ≤ R$ 60**. Empate: vence quem tiver mais cadastros que chegaram ao checkout (§3.2) |
| sempre | 3 reprovações da Meta por "gambling" no mesmo tema | para de subir variação e segue o `07 §5` |

Leitura complementar, que não corta nada mas entra no relatório do D10: taxa de gancho (3 s ÷ impressões, lida no Gerenciador), custo por ThruPlay, custo por visita à página de destino e **cadastro → checkout iniciado** por criativo.

### 4.3 O que a Fase 1 entrega

Custo por cadastro de cada um dos 3 criativos, em ~6 a 24 cadastros no total; se o funil conta cada passo com a `utm_content` certa; e quantos dos cadastros abriram o checkout do GTO. **Não entrega o CAC.** Zero assinaturas em 16 cadastros só provam que a taxa é menor que 3/16 = 19% (regra de três, 95%): inconclusivo, não fracasso.

## 5. Fase 2 · Concentração (R$ 400, 10 dias, só com gate)

**Entra quando**, no D10: pelo menos um criativo passou no critério de vencedor do §4.2. **Se nenhum passou, os R$ 400 não são gastos.** Voltam para o Rafael com o relatório, e a próxima sessão é de oferta ou de página, não de anúncio.

| Conjunto | O que é | Orçamento |
|---|---|---:|
| **V1 · vencedor** | o conjunto vencedor da Fase 1, **o mesmo** (não duplicado), com o diário subido de R$ 20 para R$ 40 | R$ 40/dia × 10 dias = **R$ 400** |

- **Por que o mesmo conjunto, e não um novo:** duplicar zera o pouco histórico que ele juntou. Um salto de R$ 20 para R$ 40 reabre o aprendizado, mas o conjunto nunca saiu dele (§1.3), então o custo é baixo. Alternativa, se o Rafael preferir não mexer: R$ 25/dia por 16 dias.
- **Se o 2º colocado também passou no critério (≤ R$ 60 com ≥ 2 cadastros):** R$ 20/dia para cada um por 10 dias, em vez de R$ 40 num só.
- **Cortes da Fase 2:** custo por cadastro acumulado > R$ 90 no D5 → pausa e devolve o resto. Frequência > 3 na semana → pausa (o público de identidade EN é pequeno).

### 5.1 Ângulos para a rodada seguinte, se houver

A matriz de 22/09 continua como banco para quando houver verba: G (o gap), L (ranking de leaks), H (honestidade do número), T (o field mudou) e N (isso não existia), em três formatos (tela real, analista de IA, estático), roteirizados no `04-reels.md` e no `05-posts-carrosseis.md`. O primeiro a produzir é o **R6 `um-clique-o-gap`**: tela real do toggle, sem avatar, sem voz, o único que vende exatamente o que o destino vende (§8.3).

## 6. Orçamento por fase, e o que precisa ser verdade para gastar mais

| Fase | Mídia | Quando entra | Quando passa para a próxima |
|---|---:|---|---|
| 0 · Pré-requisitos | **R$ 0** | hoje | os itens do §3.3 verdes, cada um com prova, e o §9 respondido |
| 1 · Teste de criativo | **R$ 600** (R$ 60/dia × 10 dias) | Fase 0 verde | D10 com um vencedor (§4.2) |
| 2 · Concentração | **R$ 400** (R$ 40/dia × 10 dias) | vencedor no D10 | fim do orçamento |
| **Total** | **R$ 1.000** | | ~20 dias de mídia |

Ferramentas de IA: **R$ 0 nesta rodada.** Os três criativos já existem, e a re-renderização é local (`instagram/build-*.mjs`). O stack de ~US$ 100/mês do `06-stack-ia.md` só entra quando houver verba para produzir o R6 e o analista.

### 6.1 Para gastar mais que R$ 1.000, as três coisas têm de ser verdade

1. **Uma assinatura do plano GTO atribuída à Meta**, provada no disco: a conta com `utm_source=meta` e `utm_campaign=gto-r1000` gravada no cadastro, e uma assinatura GTO paga no Stripe. Lido por `SELECT` agregado (contagem por `utm_campaign`, sem e-mail nem id), dentro da B4.
2. **A taxa cadastro → pago medida numa coorte**, não na campanha: cadastros por semana e por `utm_source` no AuraBusiness e quantos pagaram em 30 dias. É a leitura que a B4 autorizou; **o AuraBusiness pede o sim do Rafael na sessão, antes da consulta**. Esta sessão não fez essa leitura.
3. **CAC estimado ≤ CAC-alvo:** `custo por cadastro da Fase 1 ÷ taxa cadastro → pago da coorte ≤ R$ 500`, e o R$ 500 recalculado com a vida média lida no Stripe (B4). Se a vida média vier abaixo de 2 meses, o alvo cai junto.

Com as três verdadeiras, o próximo degrau é o cenário de R$ 70/dia do plano de 22/09 (R$ 2.940 em 6 semanas), com a escala de +20% a cada 3 dias. Sem as três, **mais mídia só aumenta o prejuízo**: o problema passa a ser oferta ou ativação.

**Regra do zero (mantida para o futuro):** 52 cadastros pagos acumulados sem nenhuma assinatura param toda a aquisição fria. R$ 1.000 não chega lá (no máximo ~40 cadastros no melhor cenário), então o zero desta rodada é inconclusivo.

## 7. O que roda de graça ao lado da mídia

Nada aqui é feito por agente: são recomendações para o Rafael, que dispara.

- **E-mail do lançamento para a base** (267 contas, 52 grátis ativas, ex-pagantes do Woo). É o canal de menor CAC e o que mais provavelmente traz as **primeiras** assinaturas GTO. São essas assinaturas que medem a taxa grátis → pago que a mídia precisa (§6.1, item 2). A landing já guarda a lista de espera no Resend (B5); quem entrou nela recebe o aviso do lançamento.
- **Orgânico:** os mesmos 3 criativos saem primeiro no perfil. Os números orgânicos do D1 ao D3 servem de sinal extra, não de critério.
- **Google Search** (eixo A do `plano-fuga-das-bets.md`): fora do escopo, e fora dos R$ 1.000.
- **Quem dá aula:** cortesia do plano GTO para 3 a 5 coaches, com permissão escrita e sem roteiro imposto. Gera a prova social que falta, sem depoimento inventado.

## 8. Os criativos: os três que cabem em R$ 1.000

### 8.1 A escolha

Três, porque é o máximo que R$ 1.000 julga: a R$ 20/dia por 10 dias, cada um recebe R$ 200, o bastante para atingir o corte de R$ 120 sem cadastro. Com quatro, nenhum chegaria lá antes do D7.

| Slot | Criativo (arquivo) | Por que entra | Dado de base |
|---|---|---|---|
| **T1 · controle** | `disc02-plataforma-mda-en` (`content/paid/AURA-DISC02/disc02-plataforma-mda-en.mp4`, 26,2 s) | o melhor EN medido: venceu o de stat no mesmo público frio | R$ 62 por cadastro · R$ 1,95 por ThruPlay (DISC02-EU) |
| **T2 · novidade** | `disc-04-pioneiro-en` (`content/paid/AURA-DESCOBERTA/disc-04-pioneiro-en.mp4`, 15,0 s) | "This never existed." é o ângulo N, o único que converteu no BR frio, e é o mais próximo da mensagem de lançamento entre os prontos. Nunca rodou em EN | R$ 44,20 por cadastro na célula PIONEIRO (BR) |
| **T3 · produto no ar** | `board01-1560-boards-en` (`content/paid/AURA-BOARD01/board01-1560-boards-en.mp4`, 24,2 s) | o mais novo: mostra a tela de resultado real do Postflop ("1,560 boards. Pick yours."), uma promessa só. Nunca rodou. ⚠️ **Só existe no checkout `aura-main/aura-marketing`, branch `feature/descoberta-reels-v2`, em 5 commits sem push** (`4c5f933`…`dd5f7ec`, de 11/09 em diante), junto com o `PLAYBOOK §8.6` que este plano cita. Precisa de push dessa branch antes de subir | sem histórico |

**Sem "overlay":** os três roteiros foram lidos e nenhum usa a palavra nem "vs GTO"; o da DISC02 traz a regra "sem vs GTO/overlay" escrita. **Sem promessa pendente:** nenhum promete cadência (A12/A12b), preço em real (A14), EV, lucro ou winrate. **Sem pessoa:** nenhum usa o analista de IA (B1 não se aplica) nem depoimento (B2 não se aplica). Todos fecham com "Create free account"/"Free to start · No card", que é verdade: o cadastro é grátis, e o upgrade para o GTO acontece dentro do app.

**O que nenhum dos três faz:** mostrar o Modo GTO. Nenhum criativo pronto mostra, porque não havia footage do toggle antes do go-live. É por isso que o destino é a home, cujo hero mostra o Modo GTO (§3.1). O **R6 `um-clique-o-gap`** (`04-reels.md`) é o primeiro a produzir quando o Modo GTO estiver no ar para uma conta de gravação: tela real do toggle, sem avatar, sem voz, sem ferramenta paga (Screen Studio + o pipeline HTML existente). **Se ficar pronto antes do D1, ele entra no lugar do T3**, com destino na `/gto`. Não entra como quarto criativo.

### 8.2 O que tem de mudar neles antes de subir (0.6)

- 🔴 **O selo "500M+ audited hands · 7 rooms" sai dos três.** Ele está gravado no rodapé de todas as cenas. O PO tirou o "500M+" da landing (escolha de 23/09, sem proveniência medida; `aura-context/docs/08-planning/landing-redesign/00-fase-a.md` §2.1 e §7), e o #11 usa "400K+ tournaments" com link para `/metodologia`. Anúncio com "500M+" levando a uma página que diz "400K+" quebra a coerência e sustenta um número que a própria empresa deixou de sustentar. **Troca:** `400K+ tournaments · 7 rooms` (o texto EN do B6), re-renderizado pelos builds que já existem: `instagram/build-disc02.mjs`, `build-descoberta.mjs`, `build-board01.mjs`. É troca de string e render local, sem custo.
- **`disc02-plataforma-mda-en`, cena 1:** "The world's only Field Intelligence (MDA) platform" é alegação de unicidade. Passou na revisão da Meta em agosto; fica, mas precisa ser defensável se alguém contestar (CONAR). Se o Rafael preferir tirar o risco, a troca é "Field Intelligence (MDA) for MTT", sem "only".
- **`disc-04-pioneiro-en`, cena 2:** a tradução EN está atrás do PT (roteiro, v2.4), e o `.mp4` EN é de 27/07. O kicker EN antigo ("The field's data, not a sample") é verdadeiro e pode ficar; conferir no quadro qual versão foi renderizada.
- **Os três:** conferir no quadro que nenhum número mudou desde o render (BOARD01 de 11/09, DISC02 de 12/08, PIONEIRO de 27/07). Os dois DISC só trazem números de escala, sem stat de spot.

### 8.3 O que ficou de fora e por quê

| Criativo | Por que não |
|---|---|
| `disc03-classes-cbet-en` | perdeu para o de plataforma no mesmo público (R$ 88,95 contra R$ 62) |
| `disc-03-categoria` | promete "atualização trimestral": cadência sem rotina (A12) |
| `disc-01-solver`, `disc-02-exploit` | células da DISC01 com no máximo um cadastro cada (só a PIONEIRO passou de um) |
| `paid01-v1/v2/v3` | não aparecem em nenhuma campanha da conta (`01 §2`); ficam como reserva, depois do "500M+" trocado |
| `reel-01-launch`, `reel-02-tour` | "Aura 2.0 is live" é notícia de julho, e o "500M+" está no quadro e na legenda |
| posts estáticos (`escala-500m` e outros) | "500M+" e "refreshed quarterly" no card (A12); os outros não têm dado de mídia paga para competir com os três vídeos |
| R1–R12 e P1–P10 (`04`, `05`) | roteiros, não peças prontas. O R5 depende do "500M+" no próprio gancho e está bloqueado; os do analista (R5, R9, R10, R12) exigem o stack de IA pago |

## 9. O que depende do Rafael antes de ligar

Nada liga sem os itens desta lista. Nenhum agente cria, pausa ou altera campanha: o MCP da Meta é só leitura.

| # | Decisão ou ação | Por que trava | Onde |
|---|---|---|---|
| 1 | **Go-live do Modo GTO:** aprovar cada passo do roteiro (re-promote do flop, deploy da API, flag `GtoOverlay:Enabled`, smoke com login real), **incluindo o A1 do brief 12**, que é o que deixa um cadastro novo comprar o GTO | sem isso o anúncio leva a um produto que o cliente não consegue comprar (§3.2) | sessão do overlay; `aura-context/docs/08-planning/turn-river-gto/08-go-live-flop-chipev.md` §8.4/§8.5 |
| 2 | **A14:** alinhar no Stripe os valores em real dos preços em uso (R$ 762/1.325 → R$ 745/1.295) | o teste é em EN e paga em dólar, então a A14 **não trava este teste**. Trava qualquer anúncio em PT e qualquer preço em real no criativo | painel do Stripe, ou a sessão do overlay com o seu sim |
| 3 | **A16:** anual em real do GTO e do Top | o card da landing mostra "preço anual em definição" até lá. Não trava o teste EN | HUB |
| 4 | **Merge do #11 com `VITE_LAUNCH_MODO_GTO=1`**, e antes disso ler a `/metodologia` (B6). `VITE_LAUNCH_FIELD_VS_GTO` fica desligada até a HUB avisar da A12b | é o que repassa UTM e `fbclid` ao app e o que troca o "500M+" por "400K+" | aura-landing#11 |
| 5 | **Autorizações dos depoimentos** (B2): texto final por escrito do Paulo "Galator" e do braga, este sem a tag [GTOW] | **não travam este teste**: nenhum dos três criativos usa depoimento. Travam a rodada seguinte e o bloco de prova da landing | `09-depoimentos.md` |
| 6 | **Conta de anúncio e pagamento:** forma de pagamento válida na conta `1598770224460932`, verificação da empresa, domínio verificado e 2FA no BM | sem forma de pagamento a campanha não entrega; sem verificação, a primeira reprovação por "gambling" não tem para onde recorrer (`07 §5`) | Business Manager |
| 7 | **Criar a campanha** do §4.1, exatamente como está, e só ela | o agente não cria nada | Gerenciador de Anúncios |
| 8 | **Sim para a leitura agregada do AuraBusiness** na sessão de medição do D10 e do D30 (B4) | é o que mede cadastro → pago e diz se há CAC | sessão de medição |
| 9 | **Autenticar o Stripe** numa sessão de leitura (B4) | vida média e churn, que viram o CAC-alvo real no lugar dos R$ 500 | sessão de medição |
| 10 | **Push da `feature/descoberta-reels-v2`** do checkout `aura-main/aura-marketing` (5 commits locais: BOARD01 e `PLAYBOOK §8.6`), pela sessão dona dele | o T3 e a regra de não mexer antes do gate só existem nesse disco | sessão de marketing daquele checkout |

**O que já está decidido e não volta ao Rafael:** B1 (o analista de IA, com "personagem gerado por IA" no vídeo, não usado nesta rodada), B3 (fase 1 aprovada; teto trocado de R$ 200 para R$ 1.000 em 25/09), B5 (lista no Resend, fora do destino), A11 ("Modo GTO" em público) e A12 (sem cadência na copy).
