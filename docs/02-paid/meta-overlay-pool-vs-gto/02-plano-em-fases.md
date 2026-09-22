# 02 · Plano de Meta Ads em fases: overlay GTO e Field vs GTO

**Escrito em:** 22/09/2026 · **Status:** plano, nada foi criado, editado ou ativado na Meta · **Linha de base:** `01-linha-de-base.md`

## 0. A tese em um parágrafo

O dinheiro de setembro não morreu por falta de criativo. Morreu por três coisas medidas:

- **Público errado no BR.** O interesse "poker" do IG BR é o ecossistema de bets.
- **Configuração mexida antes do gate.** O único recorte que produzia, identidade EN a ~R$ 25 por cadastro, foi trocado com 5 dias de vida.
- **Funil que não fecha.** O clique pago não chega ao cadastro com UTM nem `fbclid`, e não existe evento de assinatura para a Meta otimizar.

O overlay GTO muda a oferta: pela primeira vez a Aura tem uma novidade de categoria, e novidade de categoria foi o que converteu nos testes (PIONEIRO no BR, "plataforma" na EU). Por isso o plano é agressivo na Fase 2 e duro nas Fases 0 e 1. Nenhum real vai para mídia antes de o funil medir pagamento, e nenhuma escala acontece sem um gate que mostre custo por assinante.

## 1. Economia unitária (o número que decide cada corte)

| Item | Valor | Fonte / status |
|---|---|---|
| Individual | US$ 29/mês · R$ 159 no Woo legado | landing em prod; `wc_list_orders` |
| Plano GTO (overlay) | US$ 59/mês ≈ R$ 319 | `pricing-tiers-plan.md §3.1` · **não existe em prod** (`plan_tier` ausente) |
| Plano Top (overlay + Field vs GTO + 10 spots/mês) | US$ 89/mês ≈ R$ 481 | idem |
| Vida média do assinante | **desconhecida** | hipótese de trabalho: 4 meses, até o Stripe ser lido |
| **CAC-alvo (Fase 2)** | **R$ 600** | ≈ 2 meses do plano GTO, ou 4 do Individual; payback ≤ 3 meses no mix esperado |
| Conversão grátis→pago mínima para o CAC fechar | **CPC ÷ CAC** | com R$ 35 por cadastro → 5,8%; com R$ 40 → 6,7% |

A última linha é o critério de corte universal do plano. A Meta só compra cadastro. Se o cadastro custa R$ 40 e menos de 6,7% dos cadastros pagos viram assinatura em 30 dias, mais mídia só aumenta o prejuízo. Aí o problema é oferta ou ativação, e o plano manda parar.

**Regra de três para o zero:** zero assinatura em N cadastros atribuídos só prova que a taxa é menor que 3/N (95%). Com taxa mínima de 5,8%, **52 cadastros pagos com zero assinatura** encerram a aquisição. Antes disso, zero não prova nada (`PLAYBOOK §8.6`, corolário).

## 2. Quem é o público (skill target-audience, aplicada)

Os dados de hoje sustentam três arquétipos. Nenhum foi validado em entrevista; a lacuna de linguagem real (`product-marketing.md §9`) continua aberta, e a Fase 1 começa a fechá-la.

**A. O reg de MTT que já paga solver.** Joga MTT online na família PokerStars (89% do lake), ABI entre US$ 11 e US$ 109, BR ou Europa. Estuda algumas horas por semana e já assina uma ferramenta GTO. A frustração: o solver diz a linha de equilíbrio, mas o field do buy-in dele não joga equilíbrio, e o ajuste é feito no feeling. Ele compra quando uma ferramenta mostra *quanto* o field desvia *naquele spot*. Gatilhos: downswing, spot que incomodou, semana anterior a série (WCOOP/SCOOP). É o público principal do overlay.

**B. Quem estuda a fundo e dá aula** (é o usuário do ECOSYSTEM §6.6). Pede composição do range numa linha, EV por mão e a expansão do open-raise por etapa do torneio. Fala o vocabulário do solver e pensa em etapa, não só em posição e stack. Precisa de evidência em escala para a aula e para o conteúdo ("mas o field faz isso mesmo?"). Compra a profundidade (plano Top, Field vs GTO, Spots do mês) e multiplica: cada aula com tela da Aura é distribuição. Atenção: dois dos três pedidos dele o produto ainda não atende (EV por mão fora dos Spots do mês; eixo de etapa travado no dado). Os anúncios não podem prometer isso.

**C. O grinder subindo de limite.** Estuda em grupo e em Discord, é sensível a preço e entra pelo grátis. Não é o público da mídia paga agressiva. É o público do orgânico e do e-mail, e vira pagante quando bate no cadeado de bolha/ITM/mesa final.

**Para quem não é, e o que se exclui:** apostador de bet e cassino (o pool que contaminou o BR), jogador casual de app social, jogador só de cash, quem joga só GGPoker/Party/888 (0% do lake) e quem procura "ganhar dinheiro rápido". Nenhum anúncio deve atrair essas pessoas: sem ficha, sem mesa de cassino, sem promessa de ganho.

## 3. Fase 0 · Pré-requisitos (R$ 0 em mídia)

**Entra quando:** hoje. **Sai quando:** os 12 itens abaixo estiverem verdes, cada um com a sua prova. **Duração esperada:** 1 a 2 semanas de dev.

| # | Item | Pronto quando (prova verificável) | Dono |
|---|---|---|---|
| 0.1 | CTAs da landing repassam `utm_*` e `fbclid` para o app | clique de teste com UTM gera conta com `utm_source` preenchido no `tbl_user` (query agregada, sem PII) | dev landing + app |
| 0.2 | App grava `_fbc` a partir do `fbclid` e envia `fbc`/`fbp` no `CompleteRegistration` (pixel + CAPI, mesmo `event_id`) | Events Manager mostra `fbc` ≥ 60% no evento; EMQ do `CompleteRegistration` ≥ 7,0 | dev app |
| 0.3 | **Evento de assinatura:** webhook Stripe (`invoice.paid` / `checkout.session.completed`) dispara `Purchase` via CAPI com `value`/`currency` e `purchase` via GA4 Measurement Protocol, marcado como evento-chave | um pagamento de teste aparece nos dois; sem isso nenhum KPI deste plano é medível | dev API |
| 0.4 | Landing dedicada `/gto` (PT) e `/gto/en` com formulário na própria página (e-mail + buy-in médio) disparando `Lead` (pixel + CAPI) | lead de teste no Events Manager e no GA4; spec em `03-posicionamento-e-mensagem.md §5` | dev landing |
| 0.5 | Cadastro abre em PT quando vem da landing PT; campos obrigatórios no mobile reduzidos a nome, e-mail e senha | teste no celular: formulário em PT com 3 campos | dev app |
| 0.6 | E-mail D0 da escada de onboarding dispara no cadastro com link "abra no desktop" | cadastro de teste recebe o e-mail em < 5 min | dev + Resend |
| 0.7 | Report diário volta a rodar (parou em 10/09) ou é substituído por uma query semanal de coorte: cadastros por semana, grátis→pago em 14/30 dias, por `utm_campaign` | primeira execução com números agregados | analytics |
| 0.8 | Públicos criados (pelo PO): visitantes 180d, visualizadores de vídeo ≥ 50% 365d, lista de cadastros e lista de pagantes (para exclusão e upgrade) | públicos com tamanho ≥ 1.000 onde a Meta exige | PO |
| 0.9 | Business Manager com verificação de empresa, domínio verificado e 2FA | status no Centro de Segurança | PO |
| 0.10 | Filtro de palavras ocultas anti-bet nos comentários do IG | lista de `plano-fuga-das-bets.md §2C` ativa | PO |
| 0.11 | Personagem "analista da Aura" aprovado e fluxo de divulgação de IA definido | `06-stack-ia.md §2` e `07-compliance.md` | PO |
| 0.12 | Paywall e gating no ar | ✅ já feito: #46 em prod desde 22/09, gating ligado | — |

**Por que não se gasta antes:** com 0.1 a 0.3 quebrados, a Meta otimiza às cegas. Ela não vê de onde veio o cadastro (`fbc` em 7,7%) e não vê pagamento nenhum. Foi isso que produziu 12 cadastros e zero assinaturas. Gastar antes da Fase 0 é repetir setembro.

**Custo da Fase 0:** mídia R$ 0. Ferramentas de produção de criativo: ~US$ 100/mês (~R$ 540), stack tier 1 de `06-stack-ia.md`. Pode começar já, porque a produção dos reels da Fase 1 corre em paralelo ao dev.

## 4. Fase 1 · Pré-lançamento (4 semanas, a partir do fim da Fase 0)

**Objetivo:** montar a lista de espera do overlay com gente qualificada. Provar que o funil fecha (pelo menos 1 assinatura atribuída à Meta, vinda do que já está no ar). Medir, pela primeira vez, a conversão grátis→pago por coorte de mídia.

**O que se anuncia:** só o que está em produção (Preflop, Postflop, Hotspot, textura de board) e o overlay como **"em breve"**, com tela marcada "prévia". Nenhum número do overlay como "no ar" (endpoints em 404 em prod; ver `03 §4`).

### 4.1 Estrutura de campanha

| Campanha | Público | Otimização | Criativos | Por que existe |
|---|---|---|---|---|
| **F1-A · Lista EN** | Identidade: interesses PokerStars + Professional Poker Player; os mesmos 11 países da DISC02-EU (IE, NL, NO, SE, GB, FI, DK, AT, PT, DE, MT); 21–50 | `Lead` (form da `/gto/en`) | 3–5 em formato flexível (R2, R5, R9 em EN) | é o único recorte que já produziu; reabrir igual e **não mexer até o gate** |
| **F1-B · Lista BR/PT** | Advantage+ audience, sem interesse; BR + PT; sugestão 21–47; exclui cadastrados e pagantes | `Lead` (form da `/gto`) | 3–5 (R1, R2, R3, R5, R9) | teste controlado. O BR frio falhou otimizando clique e engajamento; aqui a otimização é por evento profundo e o criativo usa jargão como filtro |
| **F1-C · Quente** | visitantes 180d + visualizadores ≥ 50% + cadastrados grátis que não pagam | `CompleteRegistration` para visitantes; `Purchase` para cadastrados (quando 0.3 estiver no ar) | R3, R4, P1, P3, P6 (módulos no ar + upgrade) | é onde o primeiro assinante atribuído deve aparecer |

**Posicionamentos:** Reels, Stories e Feed de IG e FB. **Audience Network desligada**, porque é inventário de app e junta tráfego acidental.

**Kill switch pré-registrado (o único toque permitido antes do gate):** se no D3 a sessão média na `/gto` vinda de uma célula estiver abaixo de 5 s (assinatura de bot/bet, `plano-fuga-das-bets.md`), a célula pausa. Qualquer outra mudança espera o gate.

### 4.2 Orçamento em três cenários (4 semanas)

| Cenário | Diário | Total | Distribuição | Resultado esperado a R$ 15/lead e R$ 40/cadastro |
|---|---:|---:|---|---|
| Conservador | R$ 25 | **R$ 700** | F1-A R$ 15 · F1-C R$ 10 | ~47 leads, ou ~17 cadastros se tudo fosse cadastro |
| **Base (recomendado)** | R$ 50 | **R$ 1.400** | F1-A R$ 20 · F1-B R$ 20 · F1-C R$ 10 | ~93 leads, ou ~35 cadastros |
| Agressivo | R$ 90 | **R$ 2.520** | F1-A R$ 30 · F1-B R$ 30 · F1-C R$ 15 · teste de criativo R$ 15 | ~168 leads, ou ~63 cadastros |

Os R$ 15 por lead são hipótese: não existe evento `Lead` na história da conta. O gate do D7 recalibra a tabela.

### 4.3 KPIs da Fase 1, amarrados a pagamento

| Nível | KPI | Meta | Linha de base |
|---|---|---|---|
| Norte | assinaturas pagas atribuídas (coorte da Fase 1, 30 dias) | ≥ 1, e grátis→pago medido | 0 |
| Guia | custo por lead qualificado (buy-in ≥ US$ 11 no form) | ≤ R$ 15 | não existe |
| Guia | custo por cadastro grátis | ≤ R$ 40 | R$ 103,53 (conta) · R$ 75,48 (EU) |
| Guia | landing → cadastro | ≥ 4% | 1,75% |
| Saúde | sessão média na `/gto` | ≥ 30 s | 51,7 s (landing, todas as fontes) |
| Saúde | cobertura `fbc` | ≥ 60% | 7,7% |
| Saúde | taxa de gancho (3 s ÷ impressões, lida no Gerenciador) | ≥ 25% | não medida |

### 4.4 Critérios de corte (escritos antes de olhar o resultado)

- **Por célula, no D7:** custo por lead > R$ 30 (2× a meta) ou custo por cadastro > R$ 80 → pausa a célula. Entre 1× e 2× → segue sem mexer até o D14.
- **Por célula, no D14:** custo por lead > R$ 19 (1,25× a meta) → pausa. O que sobrar recebe o orçamento das pausadas.
- **Por criativo, no D7:** gasto ≥ R$ 60 sem nenhum lead → o criativo sai do conjunto. Isso não reseta o aprendizado como mexer em público ou em otimização.
- **Fase inteira, no D28:** custo por cadastro consolidado > R$ 60 → a Fase 2 abre no cenário conservador e não escala. Zero assinatura com < 52 cadastros → inconclusivo, segue. Zero com ≥ 52 → a Fase 2 não abre em aquisição fria; só upgrade da base.

## 5. Fase 2 · Lançamento agressivo (6 semanas a partir do dia em que o overlay entra em produção)

**Gatilho de entrada (tudo verdadeiro no mesmo dia):**

1. `LoadPostflopGtoCoverage` e `GtoNumbers` respondem 200 em prod (hoje, 404).
2. Flag `GtoOverlay:Enabled` ligada.
3. Migration `plan_tier` aplicada.
4. Checkout do plano GTO vendendo em BRL.
5. Porta `SE ≤ 5,00 pp` mergeada (#27).
6. Smoke do PO com login real.

**Duas ondas:**

- **2a · Overlay GTO** (plano GTO). Abre no dia do deploy.
- **2b · Field vs GTO** (plano Top). Abre quando o módulo sair de branch para prod. Hoje não tem PR; o pool comparável só existe como snapshot local.

Se 2b não estiver pronto, 2a roda sozinha e 2b vira a "segunda notícia" do mês 2. Uma segunda notícia é exatamente o que um lançamento precisa para não morrer na semana 3.

### 5.1 Sequência do dia 0

| Quando | O quê |
|---|---|
| D-1 | smoke em prod pelo PO; gravação das telas reais do overlay (os reels R6–R8 dependem disso: hoje não há footage do toggle) |
| D0 manhã | e-mail para a lista de espera e para a base grátis (Resend, custo zero); reel orgânico R6 no perfil |
| D0 | F2-C (upgrade) liga com 40% do orçamento do dia nos 3 primeiros dias: é a coorte mais quente |
| D0 | F2-A e F2-B ligam com os criativos vencedores da Fase 1 re-editados com a tela real |
| D3 | kill switch de sessão (mesma regra da Fase 1) |
| D7 | gate 1 (abaixo) |
| D14 | gate 2 e decisão de escala |
| D30 | leitura da coorte: grátis→pago da Fase 2 |

### 5.2 Estrutura de campanha

| Campanha | Público | Otimização | Peso no orçamento |
|---|---|---|---:|
| **F2-A · Lançamento BR/PT** | Advantage+ audience (herda o aprendizado da F1-B se ela passou no gate; senão identidade BR + lookalike 1% de cadastrados) | `CompleteRegistration` | 30% |
| **F2-B · Lançamento EN** | identidade EN (F1-A) + Advantage+ EN nos mesmos 11 países | `CompleteRegistration` | 25% |
| **F2-C · Upgrade** | lista de espera + cadastrados grátis + visitantes 30d | `Purchase` (ou `InitiateCheckout` se o `Purchase` tiver < 10 eventos/semana) | 30% |
| **F2-D · Teste de criativo** | orçamento por anúncio (ABO), R$ 20/dia por criativo novo, 3 criativos novos por semana | igual à F2-A | 15% |

Vencedor da F2-D (menor custo por cadastro com sessão ≥ 30 s depois de R$ 80 gastos) entra na F2-A ou F2-B na segunda-feira seguinte. **Os conjuntos da F2-A/B nunca recebem troca de público nem de otimização no meio da janela.**

### 5.3 Matriz de teste de criativo

Cinco ângulos × três formatos. Cada ângulo nasce de um fato do produto (`03 §2`).

| Ângulo | Tela-estrela | F1 · tela real + texto, sem voz | F2 · analista da Aura (IA) + tela | F3 · carrossel/estático |
|---|---|---|---|---|
| **G · O gap** (field e GTO na mesma tela) | toggle MDF ↔ GTO no Postflop; gap chart | R6 | R10 | P7 |
| **L · Ranking de leaks em bb** | feed Field vs GTO | R7 | R12 | P8 |
| **H · Honestidade do número** (a porta que recusa) | selo "Comparação GTO indisponível" | R8 | — | P9 |
| **T · O field mudou** | Field Trends, linha trimestral | R11 | — | P10 |
| **N · Isso não existia** (categoria nova; venceu no BR) | tela composta | R1, R2 | R5, R9 | P1 |

**Rodada 1 do D0:** R6, R7 (se 2b), R8, R10, R1 re-editado, P7. **Leitura:** taxa de gancho (3 s ÷ impressão), custo por ThruPlay, custo por cadastro, sessão. **Hipótese a derrubar primeiro:** avatar (F2) contra tela pura (F1) no mesmo ângulo G (R10 × R6). A Ogilvy diz que tela real demonstrando vence; o avatar só fica se bater a tela pura em custo por cadastro.

### 5.4 Orçamento em três cenários (6 semanas)

| Cenário | Diário | Total 6 semanas | Cadastros esperados a R$ 35 | Assinaturas a 5,8% | Condição para usar |
|---|---:|---:|---:|---:|---|
| Conservador | R$ 70 | **R$ 2.940** | ~84 | ~5 | entrada padrão; ou teto se a Fase 1 fechou com custo por cadastro > R$ 60 |
| **Base (recomendado como teto inicial)** | R$ 150 | **R$ 6.300** | ~180 | ~10 | D7 com custo por cadastro ≤ R$ 45 e sessão ≥ 30 s |
| Agressivo | R$ 300 | **R$ 12.600** | ~360 | ~21 | D14 com CAC ≤ R$ 600 medido em pelo menos 2 assinaturas atribuídas |

**Escala:** +20% no diário a cada 3 dias enquanto o CAC da coorte ficar ≤ R$ 600. Nunca mais que isso de uma vez, porque um salto grande reabre o aprendizado.

**Em voz alta:** o cenário agressivo custa quase 10 vezes o MRR de hoje (R$ 1.260). Ele só se paga se a conversão grátis→pago da coorte for ≥ 5,8%, e esse número hoje não existe. Por isso o agressivo é destravado por gate, não por calendário.

### 5.5 KPIs da Fase 2

| Nível | KPI | Meta |
|---|---|---|
| Norte | CAC pago (gasto ÷ assinaturas atribuídas, coorte de 30 dias) | ≤ R$ 600 |
| Norte | assinaturas do plano GTO/Top no mês do lançamento | ≥ 10 no cenário base |
| Guia | custo por cadastro | ≤ R$ 35 |
| Guia | grátis→pago em 14 dias (coorte Meta) | ≥ 4% |
| Guia | F2-C: custo por assinatura de upgrade | ≤ R$ 300 |
| Saúde | frequência na F2-C | ≤ 3,5/semana (público pequeno satura rápido) |
| Saúde | sessão, `fbc`, taxa de gancho | mesmas da Fase 1 |

### 5.6 Critérios de corte da Fase 2

- **D7:** custo por cadastro > R$ 70 na F2-A ou F2-B → a campanha volta ao cenário conservador e perde o direito de escalar até o D14.
- **D14:** CAC medido > R$ 900 (1,5× a meta) com ≥ 2 assinaturas → corta aquisição fria e mantém só a F2-C.
- **Regra do zero:** 52 cadastros pagos acumulados com zero assinatura → **para toda a aquisição fria.** Mais mídia não resolve oferta nem ativação, e a próxima sessão é de produto, não de anúncio.
- **Fadiga:** custo por cadastro de um criativo sobe 40% contra a própria primeira semana → troca pelo próximo da F2-D.
- **Sempre:** reprovação da Meta por "gambling" em 3 anúncios do mesmo tema → para de subir variações e segue o `07-compliance.md §5`.

## 6. Orçamento recomendado por fase (o que vai ao HUB)

| Fase | Mídia | Ferramentas | Destrava a próxima quando |
|---|---:|---:|---|
| 0 · Pré-requisitos | **R$ 0** | ~R$ 540/mês | os 12 itens do §3 com prova |
| 1 · Pré-lançamento | **R$ 1.400** (base, 4 semanas) | idem | D28: custo por cadastro ≤ R$ 60 e ≥ 1 assinatura atribuída, ou < 52 cadastros sem assinatura (inconclusivo) |
| 2 · Lançamento | **R$ 2.940 garantidos, teto de R$ 6.300** (base); agressivo de R$ 12.600 só com gate | ~R$ 1.600/mês (tier 2) | D14 com CAC ≤ R$ 600 |

**Total comprometido antes de qualquer prova de CAC: R$ 4.340.** Para passar disso, é preciso ter assinatura atribuída na mão.

## 7. O que roda de graça ao lado da mídia (e vem antes dela)

- **E-mail para a base:** 267 contas, 52 grátis ativas e os ex-pagantes do Woo. Anúncio do overlay no D0, com o mesmo gancho do melhor reel. É o canal de menor CAC que existe.
- **Orgânico:** os 12 reels do `04-reels.md` saem primeiro no perfil. Só o que performar no orgânico vira anúncio na F2-D (`plano-instagram-medio-longo-prazo.md §3`: "só amplificar post que já performou").
- **Google Search** (eixo A do `plano-fuga-das-bets.md`): a keyword "gto wizard" continua sendo a de maior intenção. Fora do escopo deste plano, mas é o contraponto natural à Meta, e a landing `/gto` serve aos dois.
- **Quem dá aula:** acesso de cortesia ao plano Top para 3 a 5 coaches BR, em troca de usarem a tela nas aulas, com permissão escrita e sem roteiro imposto. Isso gera a prova social que falta (`product-marketing.md §11`), com consentimento e sem depoimento inventado.
