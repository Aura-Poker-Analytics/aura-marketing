# Brief → thread Fábrica de posts: lançamento da **seleção de textura de board (Beta)**

**De:** thread de produto/orquestração · **Para:** Fábrica de posts · **Data:** 2026-08-17
**Status do produto:** no ar em produção (`www.aura.poker`) desde 2026-08-17, com badge **Beta** na UI.
**Como usar:** cole o bloco de prompt abaixo na thread da Fábrica de posts. É auto-contido.

---

## Contexto para quem for escrever (não vai no post)

A seleção de textura de board saiu de dentro do popover de Filtros e virou uma **faixa própria acima
do dashboard**, no Postflop Analysis e no Node-by-Node. O ganho não é cosmético: antes existia **um
único** controle de conectividade para as três streets, então o filtro trocava de significado ao mudar
de aba e recortes cruzando streets eram **inexprimíveis**.

O que passou a existir:

- **Estrutura por street** (flop, turn, river) numa tabela só — conectividade, naipe, overcard, high
  card e pareamento, lado a lado.
- **Cenários prontos** que preenchem a estrutura: *Conectou no turn*, *Conectou no river*, *Conectou
  no turn ou river*, *Abriu draw no turn*, *Flush completou no turn/river*.
- **Boards de exemplo** que seguem a estrutura selecionada (até 3, sorteados), deixando visível o que
  o recorte significa.
- **Definir um board concreto** e ver as categorias se marcarem sozinhas.
- Combinações impossíveis ficam **desabilitadas** em vez de devolver tela vazia.

### Números verificados (banco direto, 2026-08-17) — regra de ouro cumprida

| Recorte | Amostra |
|---|---|
| "Conectou no turn" (flop não-conectado → turn conectado) | **4.599.550** |
| "Conectou no river" | **2.133.856** |
| "Flush completou no turn" | **2.403.883** |

Fonte: `public.tbl_final_turnoop` / `tbl_final_riveroop` no `aura-production`, somando `totalcount`.
Qualquer número novo que a Fábrica quiser usar **tem que ser puxado na hora** da mesma fonte — ou sai
rotulado como ilustrativo.

### Verdade importante para não prometer errado

As estatísticas **agregam todos os boards do recorte** — os boards mostrados são **exemplos** da
estrutura, não o board analisado. Isso está explícito na UI e o copy não pode sugerir o contrário.

---

## Prompt (colar na thread da Fábrica de posts)

> Você é a **Fábrica de posts** da Aura. Onboarding obrigatório antes de responder: leia
> `aura-marketing/AGENTS.md`, `docs/00-strategy/plano-marketing-launch-2.0.md` e
> `brand/brand-kit.md`. Tom **técnico-afiado, de reg pra reg** — tom guru/get-rich é proibido.
> Regra de ouro dos números: stat sem fonte verificada não sai, ou sai rotulado "ilustrativo".
> Você escreve neste repo; **quem publica é o Rafael**.
>
> **Tarefa:** produzir o pacote de lançamento da **seleção de textura de board (Beta)**, que já está
> no ar em produção. O brief completo, com o que mudou e os números verificados, está em
> `content/posts/board-texture-beta/brief-fabrica-de-posts.md` — leia antes de escrever.
>
> **Entregáveis:**
>
> 1. **Mockups da feature** (o ponto de partida — sem eles o resto não convence):
>    - Capture ou reconstrua a faixa BOARD em 3 estados: (a) cenário *Conectou no river* aplicado,
>      com a estrutura marcada nas três streets; (b) boards de exemplo visíveis, mostrando que a
>      mesma estrutura tem vários boards; (c) o fluxo "Definir exemplo de board" marcando as
>      categorias sozinho.
>    - Se for reconstruir em vez de screenshot, use a paleta institucional do brand-kit e as cores
>      semânticas de ação. As cartas do produto usam face creme com naipe colorido (4 cores) — mantenha
>      essa identidade, ela é nossa.
>    - Salve em `content/posts/board-texture-beta/mockups/`.
>
> 2. **Post de feed 1080×1350** + **story 1080×1920**, com copy PT e EN. Ângulo sugerido (desafie se
>    achar melhor): a pergunta que antes não dava para fazer. Ex.: *"flop desconectado que conecta no
>    river"* — 2,1M de mãos nesse recorte, e antes você não conseguia pedir isso.
>
> 3. **E-mail para a base**, PT e EN, assunto + preheader + corpo curto. O e-mail deve levar ao
>    produto, não explicar tudo: um exemplo concreto, um número verificado, um CTA.
>
> 4. **Aviso de Beta**: a feature está marcada Beta na UI. O copy deve refletir isso com honestidade —
>    "primeira versão, queremos feedback" é um ângulo bom com nossa base de regs, não uma fraqueza.
>
> **Não invente número.** Os três da tabela do brief estão verificados; para qualquer outro, peça a
> quem tem acesso ao banco ou marque como ilustrativo.
