# Públicos Meta — Build-Spec (como criar)

**Autor:** thread Mídia Paga · **Data:** 2026-07-08 · **Status:** pronto para execução manual na UI
**Fonte do diagnóstico:** [publicos-diagnostico.md](publicos-diagnostico.md) — este doc NÃO repete o D1–D6/P1–P8, só traduz o plano em passo a passo de criação. Naming segue [estrutura-campanhas.md](estrutura-campanhas.md) §0. Eventos citados seguem [pixel-capi-spec.md](pixel-capi-spec.md).

> **Por que isso existe:** a semente atual (`Aura | Seguidores IG (Base)`) tem **menos de 1.000 pessoas** e os lookalikes/salvo gerados a partir dela estão fracos e sobre-empilhados (diagnóstico D1–D3). Esta build-spec é o conserto — recria a semente maior, limpa o salvo, e prepara os públicos de site que só existirão depois que o pixel novo da landing rodar.
>
> **Sobre IDs numéricos:** capturar o ID de cada público criado (para referência em specs futuras) depende do MCP oficial da Meta, que hoje está parado — login errado autorizado, ver [mcp-meta-identidade.md](mcp-meta-identidade.md). Enquanto isso não for corrigido pelo Rafael, **todos os públicos abaixo são criados pela UI do Gerenciador de Anúncios** (Públicos → Criar público). Nenhum passo aqui depende do MCP.
>
> **Regra absoluta que não muda:** criar/editar público **não gasta dinheiro** — pode ser feito livremente pelo agente/Rafael. Subir ou ativar **campanha**, isso sim, só o Rafael faz.

---

## 0. Onde criar (caminho na UI)

> 🔴 **PRÉ-REQUISITO DESCOBERTO AO VIVO (2026-07-12):** o dataset/pixel `1405949840871947` **NÃO está conectado à conta de anúncios `1598770224460932`** (verificado em Configurações → Contas de anúncios → Aura Business → **Ativos conectados: "Nenhum ativo conectado"**). Enquanto isso não for corrigido:
> - **Não dá pra criar público de SITE** (visitantes P4, convertidos P5) nessa conta — a UI só oferece criar um pixel NOVO (o que fragmentaria os dados — NÃO fazer).
> - **Campanhas não conseguem otimizar** pelos eventos do pixel (CompleteRegistration/Subscribe). Isso bloqueia o funil pago inteiro, não só os públicos.
> - **Públicos que NÃO dependem do pixel** (IG engajadores P1; salvos de interesse P3/EN) **podem ser criados mesmo assim.**
>
> **Correção (ação de config — ~1 min):** Configurações da empresa → **Fontes de dados → Conjuntos de dados e pixels** → selecionar `Aura – Website Data Set` → aba **Contas de anúncios** (ou "Conectar ativos") → **Adicionar** a conta `Aura Business 1598770224460932`. *(Alternativa: na conta de anúncios → Ativos conectados → Conectar fonte de dados.)* É atribuição de ativo (não gasta), mas mexe em config da conta — feito pelo Rafael, ou por mim com um "go" explícito.

Business Manager **Aura Poker Analytics** (`830069129552748`) → conta de anúncios **Aura Business** (`1598770224460932`) → **Gerenciador de Públicos** (Events Manager / Ads Manager → Públicos) → botão **Criar público** → escolher o tipo (Personalizado / Semelhante / Salvo).

Todos os públicos abaixo nascem **BR · 18+** salvo indicação contrária.

---

## 1. P1 — Nova semente: engajadores IG 365d

Substitui a lógica "só seguidores" por "todo mundo que engajou". É a base de tudo que vem depois (lookalike P2/P7, salvo P3).

| Campo | Valor |
|---|---|
| **Nome exato** | `Aura \| IG Engajadores 365d` |
| **Tipo** | Personalizado → Fontes da Meta → **Conta do Instagram** |
| **Fonte** | Conta @aurapokeranalytics (`17841468976680108`) |
| **Regra/definição** | Selecionar **"Todos que engajaram com sua empresa"** (não restringir a "seguidores" nem a "enviou mensagem") — inclui curtida, salvamento, comentário, visita ao perfil, interação com anúncio, clique em CTA |
| **Janela de retenção** | **365 dias** (máximo permitido) — maximiza o tamanho da semente; com a base atual pequena (710 seguidores), qualquer corte menor devolve uma semente ainda mais frágil |
| **Inclusões/exclusões** | Nenhuma — captura o funil de engajamento inteiro de propósito |
| **Quando criar** | **Agora, pré-launch.** Não depende de nada da landing — é dado que já existe no IG hoje |
| **Para que fase serve** | Fonte de semente para lookalike (P2) e para o ad set "Engajadores IG" da campanha `AURA_RTG_BR_CADASTRO` (RTG, ad set 1 — ver estrutura-campanhas.md §1). Manter o público antigo `Aura | Seguidores IG (Base)` intocado, só como referência histórica — não apagar |

**Checklist:**
- [ ] Criar público personalizado → Instagram → "todos que engajaram" → 365d
- [ ] Nomear exatamente `Aura | IG Engajadores 365d`
- [ ] Confirmar tamanho estimado na tela de criação (esperado: maior que os <1.000 atuais, mas ainda pequeno — registrar o número real para o diagnóstico)
- [ ] Não excluir nem editar o público antigo `Aura | Seguidores IG (Base)`

---

## 2. P3 — Público salvo de interesse BR (limpo)

Resolve D3: o salvo atual (`Aura Business`) cruza lookalike ∩ cargo "Professional Poker Player", o que anula o lookalike e encolhe o alcance a quase nada. Este é o substituto — só interesse, sem interseção com lookalike.

| Campo | Valor |
|---|---|
| **Nome exato** | `Aura \| Salvo Interesse Poker BR` |
| **Tipo** | Público salvo |
| **Fonte** | Segmentação por interesse (não usa nenhum público personalizado como base) |
| **Regra/definição** | Localização: **Brasil**. Idade: **18+**. Interesses (condição **OU** entre eles, nunca E): **Poker, Texas hold'em, PokerStars, GGPoker, World Series of Poker**. **Não** adicionar cargo/emprego "Professional Poker Player" (segmento minúsculo, enviesado a US, quase vazio no BR — causa raiz do D3). **Não** intersectar com o lookalike #2/#3 nem com a nova semente P1 |
| **Janela de retenção** | N/A (público salvo não expira — é uma segmentação, não uma lista de pessoas) |
| **Inclusões/exclusões** | Nenhuma exclusão neste público em si; a exclusão de convertidos (P5) é aplicada **no nível do ad set**, não aqui |
| **Quando criar** | **Agora, pré-launch.** Segmentação por interesse não depende de pixel nem de dado próprio |
| **Para que fase serve** | Ad set 1 da campanha `AURA_F1_BR_CADASTRO` (frio BR — estrutura-campanhas.md §2), como alternativa **OU** ao lookalike (nunca junto) |

**Checklist:**
- [ ] Criar público salvo → Localização BR · Idade 18+
- [ ] Adicionar os 5 interesses listados, todos em modo "OU" (segmentação ampliada, não restritiva)
- [ ] Confirmar que NÃO há campo de cargo/emprego adicionado
- [ ] Confirmar que NÃO há nenhum público personalizado/lookalike incluído na mesma regra
- [ ] Nomear exatamente `Aura | Salvo Interesse Poker BR`
- [ ] (Opcional, não bloqueante) Marcar o salvo antigo `Aura Business` como deprecated no nome ou anotação — decisão do Rafael se quer manter para comparação

---

## 3. P4 — Públicos de site: visitantes da landing (30d e 7d)

Dependem do pixel novo (`1405949840871947`, já reutilizado na landing — ver pixel-capi-spec.md §0) estar recebendo `PageView` de `aurapoker.com`. **Não existem hoje** (diagnóstico: "nenhuma custom audience de visitantes ainda").

| Campo | `Visitantes landing 30d` | `Visitantes landing 7d` |
|---|---|---|
| **Nome exato** | `Aura \| Site Visitantes 30d` | `Aura \| Site Visitantes 7d` |
| **Tipo** | Personalizado → Fontes da Meta → **Website** | idem |
| **Fonte** | Dataset/Pixel `Aura – Website Data Set` (`1405949840871947`) | idem |
| **Regra/definição** | Evento **PageView**, "todos os visitantes do site" (sem filtro de URL — a landing é o site inteiro) | idem, janela menor |
| **Janela de retenção** | **30 dias** — janela padrão de retargeting, cobre todo o ciclo de decisão do launch | **7 dias** — sub-segmento "quente recente", para priorizar frequência em quem visitou há pouco |
| **Inclusões/exclusões** | Excluir `Aura \| Convertidos CompleteRegistration 180d` (P5) assim que esse público existir — não pagar por quem já criou conta | idem |
| **Quando criar** | **Só depois que o pixel novo estiver disparando PageView de `aurapoker.com` com volume** (checklist pixel-capi-spec.md §6 fechado). Criar o público em si pode ser feito assim que houver qualquer tráfego real — Meta permite criar com poucos dias de dado, ele só cresce depois | idem |
| **Para que fase serve** | Ad set 2 da campanha `AURA_RTG_BR_CADASTRO` (RTG — estrutura-campanhas.md §1) | Reforço de frequência dentro do mesmo ad set 2, ou variante de teste separada se o Rafael quiser split |

**Checklist:**
- [ ] Confirmar no Events Manager que `PageView` está chegando de `aurapoker.com` (não do domínio antigo) — pré-condição
- [ ] Criar `Aura | Site Visitantes 30d` → Website → PageView → todos → 30d
- [ ] Criar `Aura | Site Visitantes 7d` → Website → PageView → todos → 7d
- [ ] Aplicar exclusão de P5 nos dois assim que P5 existir (a exclusão pode ser adicionada depois, editando o ad set — não precisa recriar o público)
- [ ] Registrar a data em que cada um foi criado (referência para saber quando terá massa suficiente)

---

## 4. P5 — Convertidos CompleteRegistration 180d (para exclusão)

Sem isto, todo frio e retargeting paga para reimpactar quem já criou conta — desperdício direto assim que o pixel novo começar a povoar (diagnóstico D6).

| Campo | Valor |
|---|---|
| **Nome exato** | `Aura \| Convertidos CompleteRegistration 180d` |
| **Tipo** | Personalizado → Fontes da Meta → **Website** |
| **Fonte** | Dataset/Pixel `1405949840871947`, evento `CompleteRegistration` (browser + CAPI, dedup por `event_id` — ver pixel-capi-spec.md §2/§3) |
| **Regra/definição** | Evento específico **CompleteRegistration** (não PageView) — captura só quem completou o cadastro free confirmado pelo backend |
| **Janela de retenção** | **180 dias** — cobre o ciclo entre criar conta free e eventualmente assinar; longo o bastante para não reabrir exclusão cedo demais |
| **Inclusões/exclusões** | É, ele próprio, uma lista de **exclusão** a ser aplicada em: ad set 1 e 2 do RTG, ad set 1/2/3 do F1, e F2 quando existir. Não tem exclusão interna própria |
| **Quando criar** | **Assim que `CompleteRegistration` estiver disparando de verdade** (checklist pixel-capi-spec.md §6: browser+server deduplicado aparecendo como "Processado" no Events Manager). Pode criar o público com 0 pessoas no dia 1 — ele populua sozinho; não precisa esperar volume para criar, só precisa que o evento exista |
| **Para que fase serve** | Exclusão universal em RTG (estrutura-campanhas.md §1) e F1 (§2); mesma lógica se aplicará a F2 |

**Checklist:**
- [ ] Confirmar `CompleteRegistration` "Processado (deduplicado)" no Events Manager antes de criar (senão o público nasce e fica vazio sem sinal de que está errado)
- [ ] Criar público personalizado → Website → evento CompleteRegistration → 180d
- [ ] Nomear exatamente `Aura | Convertidos CompleteRegistration 180d`
- [ ] Adicionar como exclusão em RTG ad set 1 e 2 assim que existir (editar ad set, não recriar campanha)
- [ ] Adicionar como exclusão em F1 ad set 1/2/3 quando F1 for montado

---

## 5. P6 — Conversão personalizada "conta free criada" (rede de segurança)

Hoje **zero** conversões personalizadas na conta. Esta é a rede de segurança caso o evento `CompleteRegistration` falhe em disparar (dedup quebrado, bug no backend, etc.) — baseada em URL, não em evento explícito, então funciona mesmo se o `fbq('track', 'CompleteRegistration', ...)` não rodar.

| Campo | Valor |
|---|---|
| **Nome exato** | `Aura - Conta Free Criada (URL)` |
| **Tipo** | Conversão personalizada (Events Manager → Conversões Personalizadas → Criar) |
| **Fonte** | Regra baseada em **URL**, sobre o dataset `1405949840871947` |
| **Regra/definição** | URL contém `/signup/success` (a mesma rota de sucesso citada em pixel-capi-spec.md §3, `event_source_url`) — dispara em cima de qualquer `PageView` que bata nessa URL, independente do evento `CompleteRegistration` ter disparado |
| **Janela de retenção** | N/A (conversão personalizada é uma regra viva sobre eventos existentes, não uma lista com expiração) |
| **Inclusões/exclusões** | Nenhuma — é regra de URL pura |
| **Quando criar** | **Só depois que a rota `/signup/success` existir em produção** e estiver confirmada com o dev da landing (mesma URL do pixel-capi-spec.md). Pode ser criada em paralelo ao P5, não depende dele |
| **Para que fase serve** | Não é público — é **evento de otimização alternativo**. Serve como fallback de objetivo de campanha se `CompleteRegistration` nativo não acumular volume (o fallback de objetivo já previsto em estrutura-campanhas.md §6: trocar otimização se <10 conv/sem por 2 semanas). Também pode alimentar um público personalizado de "site" baseado nesta conversão, se o evento nativo continuar instável |

**Checklist:**
- [ ] Confirmar com o dev a URL exata de sucesso do cadastro (pixel-capi-spec.md cita `/signup/success` — validar se não mudou)
- [ ] Events Manager → Conversões Personalizadas → Criar → baseada em URL → "contém `/signup/success`"
- [ ] Nomear exatamente `Aura - Conta Free Criada (URL)`
- [ ] Testar disparo com Test Events antes de confiar nela como fallback

---

## 6. P2/P7 — Lookalike: rebuild a partir da nova semente

Dois momentos distintos — não confundir.

### 6a. Agora / pré-launch — lookalike de teste leve (P2)

| Campo | Valor |
|---|---|
| **Nome exato** | `Aura \| Semelhante BR 1% - IG Engajadores 365d` |
| **Tipo** | Lookalike (Semelhante) |
| **Fonte** | Público semente = `Aura \| IG Engajadores 365d` (P1, **não** o antigo "Seguidores IG (Base)") |
| **Regra/definição** | 1% da população do Brasil, localização BR |
| **Janela de retenção** | N/A (lookalike é recalculado periodicamente pela Meta enquanto a semente existir) |
| **Inclusões/exclusões** | Nenhuma na criação do público em si |
| **Quando criar** | **Agora, pré-launch** — mas entra na campanha só como **teste de baixo peso** (ad set 3 secundário do F1), nunca como aposta principal. Diagnóstico D1/D4: semente ainda pequena e BR-only, então a prioridade de frio é interesse (P3) + Advantage+ broad, não lookalike |
| **Para que fase serve** | F1 frio BR (estrutura-campanhas.md §2, ad set 2), rotulado como teste secundário até ter dado de performance |

**Checklist:**
- [ ] Criar lookalike com fonte = P1 (confirmar que P1 já existe antes deste passo — ordem importa)
- [ ] 1%, BR
- [ ] Nomear exatamente `Aura | Semelhante BR 1% - IG Engajadores 365d`
- [ ] Não apagar os lookalikes antigos (#2/#3 da semente "Seguidores IG") ainda — deixar rodar em paralelo até comparar, ou marcar como legado

### 6b. Pós-launch, quando houver ~50–100 cadastros free — rebuild definitivo (P7)

| Campo | Valor |
|---|---|
| **Nome exato** | `Aura \| Semelhante BR 1% - Cadastros Free` (e opcional `1-3%` como segunda faixa) |
| **Tipo** | Lookalike (Semelhante) |
| **Fonte** | Público semente = `Aura \| Convertidos CompleteRegistration 180d` (P5) — **não** mais o IG |
| **Regra/definição** | 1% (e depois 1–3% se precisar de mais alcance) da população do Brasil |
| **Janela de retenção** | N/A |
| **Inclusões/exclusões** | Nenhuma |
| **Quando criar** | **Só quando P5 tiver massa suficiente — guia do diagnóstico: ~50–100 cadastros free acumulados** (a Meta tecnicamente aceita sementes menores, mas abaixo disso a qualidade cai pelo mesmo motivo que criou D1). Antes disso, não recriar — o lookalike de P2 (6a) já cobre o teste de baixo peso |
| **Para que fase serve** | Substitui P2 como ad set de lookalike no F1 assim que existir — intenção de "criou conta" é sinal muito mais forte que "seguiu/engajou no IG" (fecha D1/D2 definitivamente). Também é o candidato natural de semente para P8 (lookalike EN), quando houver cadastros fora do BR |

**Checklist:**
- [ ] Monitorar contagem de P5 (Events Manager mostra tamanho do público personalizado)
- [ ] Ao cruzar ~50–100, criar o novo lookalike com fonte = P5
- [ ] Trocar o ad set de lookalike do F1 para apontar para este público novo
- [ ] Deixar o lookalike de IG (6a) desativado ou removido do ad set, sem apagar o público (histórico)

---

## 7. Ordem de execução recomendada

| Ordem | Público | Pré-requisito | Pode fazer hoje? |
|---|---|---|---|
| 1 | P1 — `Aura \| IG Engajadores 365d` | Nenhum | ✅ Sim |
| 2 | P3 — `Aura \| Salvo Interesse Poker BR` | Nenhum | ✅ Sim |
| 3 | P2 (6a) — Lookalike 1% a partir de P1 | P1 criado | ✅ Sim (assim que P1 existir) |
| 4 | P6 — Conversão personalizada URL | Rota `/signup/success` confirmada em produção | ⏳ Após deploy da landing (pré ou pós 10/07, o que vier primeiro) |
| 5 | P4 — Visitantes 30d/7d | Pixel disparando PageView de `aurapoker.com` com volume | ⏳ Pós-launch (10/07 em diante) |
| 6 | P5 — Convertidos CompleteRegistration 180d | Evento `CompleteRegistration` deduplicado confirmado | ⏳ Pós-launch, assim que o evento validar |
| 7 | P7 (6b) — Lookalike a partir de cadastros free | P5 com ~50–100 pessoas | ⏳ Pós-launch, quando houver volume |
| 8 | P8 — Semente EN | Cadastros com massa fora do BR | ⏳ Mais adiante — fora do escopo desta build-spec (ver diagnóstico §3) |

---

## 8. O que esta build-spec NÃO cobre

- **P8 (semente EN):** não há dado suficiente ainda; fica para quando a base de cadastros tiver massa internacional (diagnóstico §3, "Pós-launch, quando houver volume").
- **IDs numéricos dos públicos:** não capturados aqui — dependem do MCP reconectado com a conta certa (ver mcp-meta-identidade.md). Até lá, os nomes exatos acima são a chave de identificação confiável na UI.
- **Subida/ativação de campanha:** fora de escopo por regra absoluta. Esta build-spec só cria públicos (não gasta); associar públicos a ad sets e ativar é decisão e ação do Rafael.
