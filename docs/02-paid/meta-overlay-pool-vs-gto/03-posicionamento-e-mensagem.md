# 03 · Posicionamento, mensagem e página de destino

Base: `_strategy/aura.md`, `_strategy/AURA-UX-BLUEPRINT.md`, `.agents/product-marketing.md`, `brand/brand-kit.md`, a verdade de produto levantada em 22/09 (resumo no §4) e a Biblioteca de Anúncios (`08-concorrencia.md`). Skills aplicadas: jg-brand-positioning (Dunford + Neumeier), brand-messaging, ogilvy, copywriting, page-cro.

## 1. Posicionamento (Dunford, cinco componentes)

| Componente | Resposta | Confiança |
|---|---|---|
| **Alternativas competitivas** | 1) solver/treinador GTO (a linha ótima, sem o field); 2) tracker/HUD (as próprias mãos, amostra pequena); 3) coach e Discord (leitura do field no feeling); 4) não fazer nada: estudar GTO e supor que o field joga GTO | pesquisada (Biblioteca, dossiê) |
| **Atributos únicos** | 500M+ mãos auditadas de MTT (família PokerStars); a frequência real do field e a referência GTO **no mesmo spot, board a board** (1.520 solves, 12,76M células no turn/river); um feed que ranqueia os desvios do field em bb de EV; a série trimestral do field desde 2023; todo número com `n` e intervalo de confiança; **uma porta que se recusa a mostrar a referência quando ela é imprecisa** (SE > 5,00 pp) | medida (docs de produto) |
| **Valor** | parar de ajustar no feeling: ver *quanto* o field do seu buy-in desvia do equilíbrio *naquele spot*, e se a amostra sustenta o ajuste | inferida, não validada em entrevista |
| **Clientes mais aderentes** | reg de MTT online da família PokerStars que já paga solver; quem estuda a fundo e dá aula (`02 §2`) | inferida |
| **Categoria** | *Field intelligence*, e com o Modo GTO fica concreta: "o GTO e o field na mesma tela". Não "solver", porque aí perde para quem tem marca; não "tracker", porque aí perde para quem tem HUD | decisão de marca existente, reforçada |

**Teste de unicidade (Neumeier):**
> A Aura é a única ferramenta de estudo de MTT que mostra, no mesmo spot, o que o GTO faz e o que o field realmente faz, medido em 500M+ mãos, e que se recusa a mostrar o número quando a amostra não sustenta.

**Trueline** (a coisa verdadeira que um concorrente não pode dizer): *"O solver sabe o equilíbrio. Só a Aura sabe o field."*

**A primeira evidência de usuário para a tese:** o depoimento de Paulo "Galator" Moraes (17/09/2026, `09-depoimentos.md`, autorização pendente) diz que ele encontrou "padrões do field onde a simples frequência de fold ou call possibilitam exploits". É a tese do produto na voz de um usuário: a frequência real do field, medida, é o que gera o exploit. É também a primeira linguagem verbatim de cliente para a lacuna do `product-marketing.md §9`. O depoimento de braga'-'279 (19/09) sustenta o arquétipo B: "uso os dados como referência para começar estudos e investigar linhas".

**Teste de troca:** nenhum anunciante da Biblioteca usa dado de field agregado como gancho (`08-concorrencia.md`). GTOWizard vende capacidade do solver ("Preflop ICM Solving Is Live"); os Geckos e o Custom Poker Trainer vendem velocidade ("in weeks"); Upswing vende história de mão; o reglifepoker (BR) vende sistema de estudo. O ângulo está livre.

## 2. Mensagem

**A promessa, uma só (Ogilvy):**
> **Veja onde o field do seu buy-in sai do GTO, spot a spot.**

Benefício e não feature, deliverable pelo produto como ele é (frequência, não EV por mão), e único.

**A grande ideia: "o gap".** O produto já desenha a ideia: no gráfico do Field vs GTO a legenda literal é **"gap = leak"**, e o Modo GTO põe duas barras lado a lado no Postflop. A campanha inteira é essa distância, e a marca registrada visual é a barra âmbar entre a linha do GTO e a linha do field. O mnemônico falado é *"olha o gap"*.

**Hierarquia de mensagem:**

| Camada | Texto |
|---|---|
| Tagline da marca (fica) | O mesmo jogo — novas informações. |
| Linha da campanha | O solver mostra o equilíbrio. A Aura mostra o gap do field. |
| Promessa | Veja onde o field do seu buy-in sai do GTO, spot a spot. |
| Prova 1 (escala) | 500M+ mãos de MTT auditadas · 7 salas |
| Prova 2 (referência) | 1.520 solves; 12,7 milhões de decisões de turn e river na referência |
| Prova 3 (honestidade) | quando a referência é imprecisa, a Aura mostra "indisponível" em vez de um número |
| Prova 4 (tempo) | 12 trimestres de field desde 2023 (Field Trends) |
| Oferta Fase 1 | lista de espera; enquanto isso, o grátis mostra o field hoje |
| Oferta Fase 2 | plano GTO; o grátis mostra a prévia borrada |

**Por público:**

| Público | Dor na língua dele (hipótese, validar na Fase 1) | Mensagem |
|---|---|---|
| A · reg que paga solver | "Estudei o spot no solver e o field não joga aquilo." | "Seu solver não sabe o que o field do $22 faz. A Aura sabe." |
| B · quem estuda a fundo e dá aula | "Meu aluno pergunta: mas o field faz isso mesmo?" | "Leve o número do field para a aula, com `n` e intervalo." |
| C · grinder subindo | "Não sei onde focar o estudo." | "Comece pelos spots onde o field mais sai do GTO." (o feed ranqueado) |

### Nomes comerciais: duas decisões do PO

1. **Não usar "overlay" em anúncio.** Em MTT, *overlay* é o buraco do garantido (prize pool abaixo do GTD), a palavra mais conhecida do jogador de torneio. "Overlay GTO" num anúncio lê como "torneio com overlay". **Recomendação:** chamar o recurso de **Modo GTO**, que é literalmente o toggle `GtoModeToggle`, e manter "overlay" só como nome interno.
2. **"Pool vs GTO" vira "Field vs GTO".** A regra da marca é "field, nunca pool" (`content/reels/disc03-classes-cbet/roteiro.md`), e o próprio gráfico do módulo já rotula a série como "Field". O título da tela (`poolVsGto.json`) diz "Pool vs GTO". **Recomendação:** trocar o título na i18n antes do lançamento. É uma chave de texto, não mapper.

Neste pacote, os roteiros usam **Modo GTO** e **Field vs GTO**. Se o PO decidir diferente, é trocar as duas expressões.

## 3. Banco de provas: o que pode e o que não pode

| Pode dizer (com fonte) | Fonte |
|---|---|
| 500M+ mãos auditadas (nunca "bilhões") | confirmado pelo dono em 09/07 (`docs/00-strategy/product-truth-aura.md`) |
| 7 salas | idem; **nunca** citar proporção por sala |
| 1.520 solves; 12,76M células de turn e river | `aura-context/docs/08-planning/turn-river-gto/01-ingest-design-v8.md` |
| referência casada board a board, e recusada quando imprecisa | `aura-context/docs/05-schema/gto-serving-contract.md §4` |
| 12 trimestres de field, desde 2023-Q3 | `field_trends_staging`, delta 0 contra `public.*` (22/09) |
| Flop CBet IP, SRP, EP vs BB: Reg Aggro 85,2% (n 2,4M) × Reg Tight 77,6% (n 804k) | validado pelo PO (`content/reels/disc03-classes-cbet/roteiro.md`) |
| "A matemática diz 64,5%. O field defende 57,7%." | célula DISC-02 (`docs/02-paid/matriz-descoberta-4-celulas.md`) · **revalidar o spot no dia** |

| Não pode dizer | Por quê |
|---|---|
| "Modo GTO já disponível" / tela do Modo GTO sem "prévia" (Fase 1) | endpoints em 404 em prod em 22/09 |
| "GTO em qualquer spot" | a porta recusa spots; cobertura: 4 pares SRP a 25/40bb, turn/river |
| "EV por mão" fora dos Spots do mês | o produto responde quanto e onde o field desvia, não quanto custa por mão |
| "Cobre GGPoker / Party / 888" | 0% do lake |
| "Ganhe mais", "aumente seu lucro", "winrate", "ROI" | política da Meta, CONAR e CDC (`07-compliance.md`) |
| Qualquer número do Field vs GTO como definitivo | o pool comparável é snapshot local; o topo do ranking (JhJd7s 0,32 bb) já foi corrigido uma vez de 0,60 bb |
| Depoimento que não seja de um usuário real, identificado e com consentimento escrito | CONAR e CDC; e o analista da Aura é personagem, não cliente |
| Nome de concorrente no texto do anúncio | regra de marca |

**Regra de ouro dos números (mantida):** todo número de anúncio é conferido na tela no dia da gravação, com rodapé de amostra (`n`). Se não der para conferir, entra como "ilustrativo" ou não entra.

## 4. O que está no ar, o que não está (22/09/2026)

| Recurso | Estado | Pode ser herói de anúncio? |
|---|---|---|
| Preflop, Postflop, Hotspot, textura de board | em produção | sim, em todas as fases |
| Paywall (401/403 viram paywall) | em produção desde 22/09 | sim (é o que o upgrade mostra) |
| Modo GTO (flop, turn, river) | código na main do `aura_api` com flag desligada; #27 sem merge; `plan_tier` ausente em prod; **sem footage** | só na Fase 1 como "em breve"; herói na Fase 2 |
| Field vs GTO (feed ranqueado) | branches sem PR; pool em snapshot local; há screenshots reais em `aura-context/docs/08-planning/pool-vs-gto/assets/` | Fase 1 "em breve" com tela marcada "prévia do beta"; Fase 2b |
| Field Trends | branches pushadas sem PR, aguardando teste do PO; **sem footage** | Fase 2 (ou antes, se subir antes) |

## 5. Página de destino (page-cro)

### 5.1 A landing de hoje, no teste de cinco segundos

A landing (`www.aurapoker.com`) tem **um trabalho**: levar à conta grátis. O visível acima da dobra: "Field Intelligence para jogadores e times de MTT", o subtítulo sobre "milhões de mãos auditadas… spots que realmente geram EV", CTA "Comece grátis" e uma tabela de Preflop rotulada **"demonstração ilustrativa"**.

- *O que é:* legível para quem conhece o termo *field intelligence*.
- *Para quem:* claro.
- *O que eu ganho:* vago.
- *Prova visual:* ilustrativa, não real.

**Veredito: passa pela metade.**

| # | Severidade | Achado (com número) | Correção |
|---|---|---|---|
| 1 | Crítica | Só 3,9% de quem vê a landing chega ao app; 86% da landing é mobile e o CTA manda para outro domínio | formulário na própria página na `/gto` (e-mail + buy-in); o app vem depois, por e-mail, no desktop |
| 2 | Crítica | CTA não repassa `utm_*`/`fbclid` (medido 22/09) | Fase 0, item 0.1 |
| 3 | Crítica | produto visual com prova "ilustrativa": o hero não é tela real | vídeo de 15 s da tela real no hero (é o mesmo asset dos reels) |
| 4 | Maior | card Grátis diz "Hotspot Analysis — exploração completa"; desde o #26 (prod, 22/09) o Grátis toma 403 no Hotspot em `$1K+`, FinalTable e KO | trocar para "Hotspot — recorte grátis (≤ $22, Early Game)" · risco de CDC |
| 5 | Maior | subtítulo promete "spots que realmente geram EV"; fora dos Spots do mês o produto não calcula EV | trocar por "spots onde o field mais desvia" |
| 6 | Maior | preço só em US$, com aviso de conversão, para um público 75,5% BR | mostrar R$ (a decisão de preço BRL é do PO) |
| 7 | Maior | cadastro abre em inglês depois de uma página em português, com 7 campos | Fase 0, item 0.5 |
| 8 | Maior | zero prova social | cortesia a coaches com permissão escrita (`02 §7`); nunca inventar |
| 9 | Menor | 9 CTAs concorrentes (Comece grátis ×5, Ver módulos, Assinar, Fale conosco, Discord) | na `/gto`, um CTA primário |
| 10 | Menor | "Dados reais do field. Não teoria." contradiz o lançamento de uma comparação com GTO | na `/gto`: "O GTO e o field na mesma tela" |

### 5.2 A `/gto` (Fase 1: lista de espera) — texto pronto

> **Revisão de 25/09:** a lista de espera deixou de ser destino de anúncio (B5; Modo GTO no ar). A `/gto` que vale é a do aura-landing#11 em modo de lançamento (`VITE_LAUNCH_MODO_GTO=1`), cujo CTA é "Criar conta e ver o gap". Este texto fica como referência do que a página diz; o funil está no `02 §3`.

**Uma página, um trabalho:** entrar na lista. CTA secundário, visualmente menor: criar conta grátis.

> **Kicker:** Em breve na Aura · Modo GTO
>
> **H1:** O GTO e o field de MTT na mesma tela.
>
> **Subtítulo:** Veja, board a board, onde a população que você enfrenta sai do equilíbrio. Medido em 500M+ mãos de torneio.
>
> **Hero:** vídeo de 15 s, sem som, da tela real (Field vs GTO: o gap chart acendendo), com o selo "prévia do beta".
>
> **Formulário:** E-mail · Seu buy-in médio (até $11 / $11–$33 / $33–$109 / $109+) · botão **Entrar na lista do Modo GTO**
> Microcopy: *Sem cartão. Você recebe um e-mail no dia em que abrir.*
>
> **Como funciona (3 passos):** Escolha o spot no Postflop → Ligue o Modo GTO → Veja o gap entre o que o GTO faz e o que o field faz.
>
> **Por que confiar:** Quando a referência não é precisa o bastante, a Aura não inventa: mostra "Comparação GTO indisponível". Todo número vem com o tamanho da amostra.
>
> **O que cobre hoje:** potes single-raised dos pares UTG×BB, BTN×BB, BTN×SB e CO×BTN, a 25bb e 40bb, flop, turn e river. Mais pares e stacks entram por ondas.
>
> **Enquanto isso:** O Preflop, o Postflop e o Hotspot já estão no ar, com um recorte grátis. [Criar conta grátis]
>
> **FAQ:** Substitui meu solver? (Não. O solver calcula a linha; a Aura mostra onde o field sai dela.) · Cobre GGPoker? (Não. A Aura cobre 7 salas, e GGPoker, partypoker e 888 não estão entre elas. A lista de salas é decisão do PO publicar; a proporção por sala não se publica.) · Uso na mesa? (Não. É ferramenta de estudo, fora da mesa.) · Quanto vai custar? (preço do plano GTO, decisão do PO)
>
> **Rodapé:** Ferramenta de estudo · 18+ · A Aura não é site de apostas e não oferece jogo.

**Na Fase 2**, a mesma página troca o kicker para "Novo", o formulário para o CTA **Criar conta e ver o gap** (cadastro em PT, com UTM) e acrescenta o preço do plano GTO em R$.

### 5.3 Coerência anúncio → página

O ângulo do anúncio chega em `utm_content`, e a página troca só o H1 (variante por parâmetro, sem página nova):

| Ângulo (`02 §5.3`) | H1 da `/gto` |
|---|---|
| G · O gap | O GTO e o field de MTT na mesma tela. |
| L · Ranking de leaks | Os spots onde o field mais sai do GTO, em ordem. |
| H · Honestidade | Um número GTO só aparece quando a amostra aguenta. |
| T · O field mudou | O field de 2023 não é o field de hoje. |
| N · Isso não existia | Isso não existia: o GTO e o field no mesmo spot. |

### 5.4 O que medir antes da próxima mudança

`Lead` e `CompleteRegistration` por `utm_content`; sessão média por célula; rolagem até o formulário (evento `scroll` 50%); taxa de formulário iniciado (`form_start`, que já existe no GA4) ÷ enviado.
