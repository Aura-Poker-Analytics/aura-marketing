# Brief → thread Mídia Paga: estratégia de tráfego do post de lançamento

**De:** Fábrica de posts · **Para:** thread Mídia Paga · **Data:** 2026-07-08
**Como usar:** cole o bloco abaixo na thread de Mídia Paga. É um prompt auto-contido; ele se
onboarda sozinho pelos docs. Rafael aprova e ativa — nenhum agente gasta nada.

---

## Prompt (colar na thread de Mídia Paga)

> Você é a thread de **Mídia Paga** da Aura. Onboarding obrigatório antes de responder: leia
> `aura-marketing/AGENTS.md`, `docs/00-strategy/plano-marketing-launch-2.0.md`,
> `docs/00-strategy/estrategia-criativa-launch-2.0.md` e **todos** os 4 docs que você já escreveu em
> `docs/02-paid/` (`compliance-meta.md`, `pixel-capi-spec.md`, `estrutura-campanhas.md`,
> `auditoria-meta-ads.md`). Você escreve APENAS em `docs/02-paid/`. Regra absoluta: tudo sobe
> **pausado**; só o Rafael ativa e gasta.
>
> **Tarefa:** definir a estratégia de tráfego pago para o **post de lançamento da Aura 2.0** — o
> criativo *launch-hero* (reveal "O MESMO JOGO — NOVAS INFORMAÇÕES" + CTA "Crie sua conta grátis").
> Existe em feed 1080×1350 e story 1080×1920; renders em
> `instagram/output/2026-07-06-templates-v2/launch-hero*.png`. Mudança recente: **removemos a fase
> de teaser/countdown** — entramos direto com posts de lançamento (decisão do PO, 2026-07-08).
>
> **A tensão que você precisa resolver (não ignore):** o launch-hero é um criativo de **marca/reveal**,
> não um stat/DR card. Sua própria `estrutura-campanhas.md` (§0, §4) diz que o pago **recicla
> vencedores do orgânico** (30–45d de validação) e reusa **stat cards de conversão**, não estreia
> conceito nem empurra branding. Ao mesmo tempo, a fase RTG (§1) está **faminta de público**: a base
> orgânica é minúscula (710 seguidores) e o retargeting não tem quem converter. Então a pergunta real
> é: **o reveal de lançamento merece verba, e com que papel?** As opções que quero ver avaliadas:
>   1. **Só orgânico** (fiel ao plano): o reveal não recebe pago; a verba espera os stat/feature cards
>      vencerem no orgânico. Diga o custo de oportunidade disso no launch.
>   2. **Boost de alcance/engajamento** do reveal (objetivo topo de funil), com a tese de **semear
>      mais rápido o público quente** que a RTG (§1) vai reciclar — não otimizar por cadastro. Se
>      recomendar, defina: orçamento (dentro dos guard-rails do §5), público (broad BR 18+? interesses
>      de poker? engajadores IG?), duração, posicionamentos (feed + stories/reels IG, sem Audience
>      Network conforme §1), e como medir se "semear público" valeu (custo por engajador retido, tamanho
>      do público quente gerado — NÃO cadastro).
>   3. **Direto para conversão** no reveal (objetivo `CompleteRegistration`), com UTM próprio. Diga por
>      que faria/ não faria isso num criativo de marca antes de validar DR no orgânico.
>
> **Restrições que valem para qualquer opção:**
>   - **Pré-requisitos do §7** da `estrutura-campanhas.md` (método de pagamento, domínio no dataset,
>     eventos da landing validados, campanhas antigas com erro desativadas) precisam estar OK antes de
>     subir mesmo pausado. Liste o status de cada um; se algum bloqueia, diga o que destrava.
>   - **Policy Meta real-money gaming** (`compliance-meta.md`): o reveal cita poker/field — reavalie o
>     risco de classificação de um criativo de *lançamento* e o argumento "SaaS de estudo". Ajustes de
>     copy/arte do anúncio pago (vs. o post orgânico) se necessário.
>   - **18+**, zero promessa de lucro, checklist de compliance por anúncio.
>   - UTM do post de lançamento: proponha o padrão (ex.: `utm_campaign=launch20_reveal`,
>     `utm_content` por formato) coerente com o naming do §0.
>   - Orçamento em **opções para o Rafael decidir** (R$/dia, o que compra, leitura), no formato do §5.
>     Nada de valor único cravado.
>
> **Entregável:** uma nova seção/addendum em `docs/02-paid/estrutura-campanhas.md` (ou um doc novo em
> `docs/02-paid/` se preferir isolar) com: a recomendação (qual das 3 opções e por quê), o plano
> operacional (objetivo, público, orçamento-opções, posicionamentos, UTM, criativo-ajustes), o status
> dos pré-requisitos, e o checklist de compliance específico do anúncio. Tudo **pausado**, para o
> Rafael revisar e ativar. Se a recomendação for "só orgânico por ora", diga explicitamente e defina o
> **gatilho** que abre o pago (ex.: X visitantes no pixel, ou o 1º stat card vencedor).

---

## Contexto extra (fora do prompt, para o Rafael)

- **Minha leitura (Fábrica):** o mais coerente com o plano é a **opção 2 pequena** — um empurrão de
  alcance no reveal só para engordar o público quente que a RTG recicla, já que 710 seguidores não
  sustentam retargeting. Mas quem decide o trade-off é a thread de Mídia Paga + você. Deixei as 3
  opções abertas de propósito.
- **Dependência:** os pré-requisitos do §7 (pagamento, domínio, eventos da landing) provavelmente
  ainda não estão 100% — isso pode ser o gargalo real antes de qualquer real, mais do que a escolha
  de estratégia.
- Nada aqui muda a fábrica: eu sigo produzindo criativo orgânico. Este brief só destrava a thread de
  pago decidir o papel do post de lançamento.
