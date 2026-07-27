# Matriz de descoberta — 4 células (campanha paga 30d)

**Autor:** thread Mídia Paga · **Data:** 2026-07-25 · **Idioma:** PT apenas (validação do PO antes do EN)
**Objetivo da campanha:** DESCOBRIR QUAIS PERFIS ressoam com o conceito da Aura. **Não é conversão.**
**Status:** proposta pra validação. Nada renderizado, nada ativado.

---

## 0. O princípio que organiza tudo

4 reels só viram dado interpretável se cada um **isolar uma hipótese de persona**. 4 variações do mesmo argumento ensinam CTR agregado — não ensinam *quem*.

Cada célula abaixo mira uma **população diferente**, identificada pela **ferramenta/comportamento que ela já tem**. Isso é deliberado: ferramenta prévia é o proxy mais legível de perfil, e o gancho consegue nomeá-la sem citar concorrente.

**⚠️ Decisão de PO:** as 4 personas abaixo são minha proposta, com justificativa. Se você quiser trocar uma (ex.: testar "jogador de bolha/ICM" no lugar do tracker), é sua chamada — o desenho aguenta a substituição sem mudar o resto.

---

## 1. A matriz

**Dois eixos** (decisão do PO, 2026-07-25): 3 células testam **persona** (*quem* ressoa) + 1 testa **posicionamento** (*novidade ressoa por si só?*).

| # | Célula | Eixo | O que testa | Ativo-base |
|---|---|---|---|---|
| 1 | **SOLVER** | persona | Reg que estuda solver — "teoria não descreve o oponente real" | adaptar `paid01-v2-field` |
| 2 | **EXPLOIT** | persona | Jogador exploitativo — "quer o número do pool, não o ótimo" | adaptar `paid01-v3-leak` |
| 3 | **CATEGORIA** | persona | MTT player sem contexto — "o conceito vende sozinho" | adaptar `reel-01-launch` |
| 4 | **PIONEIRO** | **posicionamento** | "Ser inédito é, por si, razão de parar o scroll?" | **novo** |

**Célula 4 substituiu TRACKER** (proposta anterior). Motivo do PO, e ele está certo: **a Aura não rivaliza com tracker** — tracker mostra *as suas* mãos, a Aura mostra as do *field*. São complementares. Posicionar contra convidaria a pergunta errada ("substitui meu HUD?"). A menção a tracker sobrevive só na **negação** da célula 3, que é o uso correto.

**Célula 3 segue sendo o controle** — a mais ampla, sem pressupor ferramenta. Se vencer, o conceito vende sem âncora.

**Célula 3 vs 4 é a comparação mais interessante do teste:** as duas definem categoria, mas 3 define **por negação** ("não é X nem Y" — seguro, comparativo) e 4 **por afirmação** ("isso é novo" — ousado, sem referência). Descobrir qual funciona vale pro posicionamento inteiro da marca, não só pro anúncio.

---

## 2. Primeiros frames (entrega central)

Regra: o 1º frame é o **instrumento de medição**. Ele precisa fazer a pessoa certa parar **e a errada rolar** — frame vago coleta ruído demográfico e destrói a legibilidade do teste.

### Célula 1 · SOLVER — `disc-01-solver`
> **Kicker:** `MTT · pra quem estuda solver`
> **Gancho:** **"Você decorou o GTO."**
> *(beat)* **"Seu oponente não."**

> ⚠️ **Atualizado na produção (PO, 25/07, 2ª rodada): "equilíbrio" → "GTO".**
> Mais direto para a persona, que já usa o termo. Registrado aqui para a Mídia Paga não
> trabalhar com a versão anterior. **Este é o gancho literal vigente.**

- **Deve parar:** reg que já rodou solver e sente a distância entre estudo e mesa
- **Deve rolar:** quem nunca abriu um solver — não decodifica "equilíbrio"
- **Por quê:** ataca a dor de investimento não-convertido. É a única célula que fala com quem *já estuda*

### Célula 2 · EXPLOIT — `disc-02-exploit`
> **Kicker:** `Postflop · c-bet de 55% do pote`
> **Gancho:** **"A matemática diz 64,5%."**
> *(beat)* **"O field defende 57,7%."**

- **Deve parar:** quem procura desvio de população e entende MDF
- **Deve rolar:** quem não sabe o que é MDF (o jargão filtra sozinho)
- **Por quê:** é o gancho com maior densidade técnica — testa o extremo do filtro por jargão
- **Compliance:** os dois números lado a lado, **descritivo**. Não dizer "leak", "abaixo do MDF logo explorável"

### Célula 3 · CATEGORIA — `disc-03-categoria`
> **Kicker:** `MTT`
> **Gancho:** **"Não é solver. Não é tracker."**
> *(beat)* **"É o que o field inteiro faz."**
> **Selo:** `O mesmo jogo — novas informações`

- **Deve parar:** qualquer jogador de MTT (o mais amplo dos quatro)
- **Deve rolar:** não-jogadores
- **Por quê:** define a categoria por negação — a forma mais rápida de um estranho entender em 2s. É o **controle** do experimento

### Célula 4 · PIONEIRO — `disc-04-pioneiro`
Testa **posicionamento**, não persona: novidade/ineditismo é razão suficiente pra parar o scroll?

**✅ APROVADO PELO PO (25/07): versão (a), com a terminologia da casa incorporada.**

> **Kicker:** `Inteligência de field · MTT` *(EN: `Field intelligence · MTT`)*
> **Gancho:** **"Isso não existia."**
> **Linha:** **"Mass Data Analysis aplicada a MTT."**

> ⚠️ **Atualizado na produção (PO, 26/07, v2): legenda do rodapé removida.**
> A frase *«500M+ mãos lidas como população — não como amostra.»* era literal aprovada e
> fazia parte do instrumento (sentir → nomear → **provar**). O PO pediu a remoção das
> legendas queimadas em todas as cenas do disc-04 (e do disc-02). O instrumento vigente
> fica **gancho + linha**; a prova numérica permanece no **selo persistente** do rodapé
> (`500M+ mãos auditadas · 7 salas`) em todas as cenas. **Não subir com a spec antiga.**

**Sequência deliberada (v2):** o gancho faz *sentir* o ineditismo → a linha *nomeia* a categoria.
A substanciação numérica fica no selo persistente (§3.2), não na caixa de legenda.

**"Mass Data Analysis" em inglês dentro do criativo PT é proposital** — segue a regra de jargão da casa (RFI, MDF, field ficam em EN nas duas línguas). E funciona **especificamente nesta célula**: aqui o termo desconhecido *é* a mensagem (categoria nova). Nas células 1 e 2 seria ruído — lá o objetivo é compreensão imediata.

<details><summary>Versão (b) — descartada, registrada pra histórico</summary>

> *"A primeira ferramenta de field intelligence do mundo."*

Descartada por ser claim de superioridade: risco de reprova da Meta por superlativo não-substanciado, exposição a report de concorrente, e — o mais caro — público técnico e cético, onde um único contraexemplo conhecido vira munição contra a marca. Ineditismo tautológico ("primeiro na categoria que eu mesmo nomeei") também é publicitariamente fraco.
</details>

- **Deve parar:** quem é atraído por ser early adopter; quem já sentiu que falta uma categoria
- **Deve rolar:** quem só reage a dor concreta (esses param nas células 1 e 2)

**Por que recomendo (a):** *"primeira do mundo"* é **claim de superioridade** e traz três riscos concretos — (1) a Meta reprova superlativo não-substanciado com alguma frequência; (2) concorrente pode reportar; (3) **o público é técnico e cético** — se alguém conhecer qualquer ferramenta de dado populacional, o claim vira munição contra a marca, e o custo de credibilidade é maior que o ganho de gancho. Além disso, "primeiro numa categoria que eu mesmo nomeei" é tautológico e publicitariamente fraco.

A versão (a) **entrega a mesma sensação de ineditismo** — mas por demonstração ("isso não existia" + a capacidade real), e é defensável linha a linha. Regra clássica: *mostre a novidade, não anuncie que é novidade.*

**Se você escolher (b)**, dá pra rodar — mas só depois de você confirmar que não existe ferramenta pública de dado populacional de MTT que invalide o claim. É verificação sua (conhecimento de mercado), não minha.

> **Nota de compliance:** "solver" e "tracker" são **categorias**, não marcas. Nunca nomear GTO Wizard, PokerTracker, Hold'em Manager etc.

---

## 3. Roteiro (padrões que sustentam o gancho)

Aplicar aos 4, mantendo o que a v3 do AURA-PAID01 validou:

1. **Consequência de DECISÃO por cena.** Todo dado fecha com o que ele muda na hora de agir — nunca com resultado financeiro. ✅ *"Você sabe contra qual perfil está antes de apertar o botão"* · ❌ *"Você ganha mais"*
2. **Prova social persistente:** selo discreto no rodapé em todas as cenas — `500M+ mãos auditadas · 7 salas`. Não deixar pro último frame.
3. **Produto real em tela** já na cena 1 (print, não recriação vetorial) e uma cena de tela cheia no meio.
4. **CTA idêntico nos 4** — é variável de controle: `Criar conta grátis` + `Preview de cada módulo. Sem cartão.`
5. **26s, crossfade 0,4s**, corte seco onde as duas cenas tiverem texto denso.
6. **18+ visível** em todos os quadros · sem dinheiro/fichas/luxo no visual.

---

## 4. UTM (1 por reel, estável)

| Reel | `utm_content` |
|---|---|
| Célula 1 | `disc-01-solver` |
| Célula 2 | `disc-02-exploit` |
| Célula 3 | `disc-03-categoria` |
| Célula 4 | `disc-04-pioneiro` |

Nome do arquivo = nome do anúncio = `utm_content`. **Não renomear depois de subir** — quebra a série do relatório.

---

## 5. HANDOFF → thread Mídia Paga (bloco colável)

> **Campanha de DESCOBERTA — 4 células, 30 dias**
>
> **Objetivo:** ThruPlay / engajamento. **NUNCA CompleteRegistration** — com ~0 conversões a Meta estreitaria a entrega num bolso minúsculo e mataria a amplitude de que a descoberta depende.
>
> **Estrutura: TESTE A/B (split test) nativo da Meta, 4 células.** ⚠️ **Corrigido 25/07** — a versão anterior dizia "1 conjunto com 4 anúncios competindo", e isso **quebraria o experimento**: com 4 anúncios num conjunto, a Meta concentra 70–90% das impressões no vencedor em 24–72h e as outras 3 células ficam sem amostra. Ótimo pra conversão, fatal pra descoberta — a gente quer o perfil de **cada** célula, não só do vencedor.
>
> O split test resolve os dois problemas de uma vez: audiência dividida em grupos **mutuamente exclusivos** (cada pessoa vê **uma** célula só → zero saturação) e **orçamento igual garantido** por célula → amostras comparáveis. Abre-se mão da eficiência de otimização, o que é aceitável: nesta fase dado limpo > eficiência.
>
> **Matemática do orçamento:** R$50/dia ÷ 4 = **R$12,50/célula/dia** (~R$375/mês cada). Acima do mínimo da conta (R$5,16), mas magro — em mercados de CPM alto os breakdowns ficam ruidosos. **Decisão do PO:** manter 4 células com leitura **direcional** (recomendado), cortar pra 3 (R$16,67 cada), ou subir pra R$100/dia (R$25 cada, dado sólido).
>
> **Sobre saturação:** não é risco material aqui. A Meta deduplica entrega dentro do conjunto, anúncios do mesmo conjunto não competem entre si, e o orçamento é pequeno demais — referência da própria conta: R$505 → 60k alcance → **frequência 1,99**. Com pool de milhões, a frequência esperada fica em ~1,0–1,5.
>
> **Público: AMPLO.** Sem pré-segmentação dura — o **gancho é o filtro**. Pré-segmentar enviesaria a própria descoberta (a gente encontraria só quem já escolheu). Manter: geo definido, 18+, exclusão de cassino/apostas, só Instagram. ❌ Nunca o interesse "poker" isolado (agrega cassino — aprendizado registrado).
>
> **Como ler a descoberta:** breakdowns do Gerenciador (**idade · gênero · posicionamento · região · dispositivo**) cruzados com `utm_content`. Cada célula tem `utm_content` próprio, então o corte sai direto. Funciona independente de on-site.
>
> **Definição de sucesso (não é cadastro):**
> - **Custo por engajador qualificado** (ThruPlay / visualização 15s+) por célula
> - **PERFIL que mais engajou por célula** — este é o entregável real: quais faixas/regiões/posicionamentos concentram engajamento em cada enquadramento
> - Cadastro é bônus, **não é métrica de decisão** nesta fase
>
> **O que a campanha constrói:** a semente de público que hoje não existe (<1.000, D1/D5 do `publicos-diagnostico`) e os interesses vencedores — insumo das campanhas de conversão depois.
>
> **Regra absoluta:** sobe pausado, Rafael ativa.

---

## 6. Pendências antes de renderizar

- [x] ~~PO valida as personas~~ — **25/07:** TRACKER cortado (não rivalizamos com tracker), PIONEIRO no lugar
- [x] ~~PO escolhe a versão da célula 4~~ — **25/07: versão (a)**, com `Inteligência de field` + `Mass Data Analysis aplicada a MTT`
- [x] ~~PO valida os ganchos das células 1–3~~ — **25/07: aprovados como estão**
- [x] ~~**LIBERADO:** fábrica produz os 4 roteiros + render PT~~ — **ENTREGUE (v1):** 4 roteiros + MP4
- [x] ~~**v2 (26/07):** PO valida PNGs de preview em `instagram/output/desc-preview/`~~ — **26/07:
  feedback recebido, ver v2.1 abaixo.**
- [x] ~~**v2.1 (26/07, 2ª rodada):** PO valida os novos PNGs de preview~~ — **26/07: feedback
  recebido, ver v2.2 abaixo.**
- [x] ~~**v2.2 (26/07, 3ª rodada):** PO valida os novos PNGs de preview~~ — **26/07: feedback
  recebido, ver v2.3 abaixo.**
- [x] ~~**v2.3 (26/07, 4ª rodada):** PO valida os novos PNGs de preview~~ — **26/07: aprovado,
  render completo autorizado.**
- [x] ~~Render final PT + EN dos 8 anúncios (4 células × 2 idiomas)~~ — **26/07: ENTREGUE (v2.3).**
  ⚠️ **Desatualizado pela v2.4** (ver abaixo) — precisa re-render antes de qualquer validação.
- [x] ~~**v2.4 (26/07, 5ª rodada):** PO valida os novos PNGs de preview~~ — **26/07: feedback
  recebido, ver v2.5 abaixo** (disc-02 s4 faltou o ajuste de terminologia + troca de ordem s3/s4).
- [ ] **v2.5 (26/07, 6ª rodada):** PO valida os novos PNGs de preview do disc-02 (ordem de cenas
  trocada + terminologia + texto de fechamento) — **antes** de re-encodar os 8 MP4
- [ ] **Sincronizar as traduções EN pendentes** — disc-01 s4, disc-03 s3, disc-04 s2 (da v2.4) e
  disc-02 s4/nova-headline (da v2.4/v2.5, marcadas "⚠️ pendente" nos roteiros) — antes do próximo
  render PT+EN
- [ ] v2: mockup Postflop 2× do app real (disc-01 cena 2, disc-02 — trocada por
  `mockup-two-devices.png` na v2.2) — bloqueado no LOCAL (`tbl_*_pooled` inexistente; ver nota
  técnica no fim desta seção). Fora do critical path.
- [ ] PO faz a validação final dos 8 MP4 (assista antes de subir — o preview em PNG não capta
  Ken Burns/timing) — só depois do re-render v2.5
- [ ] Mídia Paga: subir campanha de descoberta (pausada) quando o PO aprovar os 8 MP4

### v2.5 produção (26/07, 6ª rodada) — feedback do PO sobre os PNGs v2.4 (disc-02)
- **disc-02:** sub-label da cena "vs overpot" (então cena 3) ficou faltando o ajuste de
  terminologia da v2.2 — `"distância no overpot"` → **`"Overfold vs MDF"`** (PT e EN).
- **disc-02:** cena 3 (headline + mockup, da v2.4) e cena "vs overpot" **trocaram de ordem** — a
  "vs overpot" passa a vir antes da headline, agrupando as duas comparações numéricas antes da
  transição pro mockup. Só a ordem no `ids` do `build-descoberta.mjs` mudou; conteúdo de cada
  cena continua o mesmo.
- **disc-02:** caption **"Baseado em dados, não palpite."** saiu da cena de headline (ficaria
  repetida 2x seguidas) e passou pra linha de fechamento da cena 5, no lugar de
  `"Descrição, não palpite."`.
- Ver detalhes cena a cena em [disc-02-exploit/roteiro.md](../../content/reels/disc-02-exploit/roteiro.md).

### v2.4 produção (26/07, 5ª rodada) — feedback do PO sobre os MP4 v2.3
- **disc-01 cena 4:** headline "O GTO é o começo" → **"Descubra o que o field realmente faz."**
  — pedido do PO pra essa cena "virar anúncio da Aura" em vez de só concluir o gancho.
- **disc-02 cena 3** ("A tela real, filtrada por textura"): mesmo tratamento — kicker trocado por
  headline `big` **"Descubra o que o field faz em cada textura de board."** + caption nova
  **"Baseado em dados, não palpite."**
- **disc-03 cena 3** ("A tela real"): texto que estava no caption (rodapé) subiu pra `line`
  (acima do print, mais em destaque) — pedido do PO. Caption eliminado, sem duplicar o texto.
- **disc-04 cena 2:** kicker "População, não amostra" → **"Os padrões do field a um clique de
  distância."**
- ⚠️ **As 4 traduções EN correspondentes ainda não foram atualizadas** — marcadas "pendente" nos
  roteiros. Os 8 MP4 da v2.3 ficaram desatualizados (conteúdo mudou); precisam de re-render depois
  da aprovação destes PNGs + sincronização do EN.

### v2.3 produção (26/07, 4ª rodada) — feedback do PO sobre os PNGs v2.2 + render final
- **disc-02:** cena 5 — `"tamanho"` → **`"size"`** na linha de fechamento (loanword já
  estabelecido no deck, ver §2).
- **disc-04:** cena 3 (painel de filtros) — kicker `"Do early à mesa final"` →
  **`"Do Early-Game à Mesa Final"`**, casando com o nome do estágio mostrado no painel.
- **Traduções EN das 4 células** — entregues e revisadas em 2 rodadas (`The database behind it`,
  `Field Defense %`, `Real Data, not a guess.`, `This never existed.`, `The field's data, not a
  sample` — ver roteiros de cada célula, seção "Tradução EN").
- **Render final autorizado pelo PO** — 8 MP4 (4 células × PT/EN) encodados e entregues em
  `content/paid/AURA-DESCOBERTA/`, mesma duração/estrutura documentada em cada roteiro (21,0s
  disc-01/04, 26,0s disc-02/03). `build-descoberta.mjs` ganhou 4 entradas `-en` em `CELLS`,
  reaproveitando os mesmos `durs`/`anim` das células PT correspondentes.

### v2.2 produção (26/07, 3ª rodada) — feedback do PO sobre os PNGs v2.1
- **disc-02:** cena 2 — sub-label `distância vs MDF` → **`Overfold vs MDF`**. Cena 3 (bloqueada
  no LOCAL) — troca do crop antigo (`crop-disconnected-col.png`) pelo mockup **`mockup-two-devices.png`**
  (mesmo asset já usado nas cenas de fechamento de disc-01/03/04), a pedido do PO em vez de manter
  um print desatualizado como placeholder.
- **disc-03:** sem mudanças — **PO aprovou como estava** ("Disc 3 ok").
- **disc-04:** cena 3 ("A tela real", mockup 2× do Preflop) **deletada** a pedido do PO — célula
  cai de 6 pra **5 cenas**, mesmo padrão do disc-01 na v2.1. **Desvio de duração**: soma **21,0s**
  em vez de 26,0s (registrado no build, igual disc-01).

### v2.1 produção (26/07, 2ª rodada) — feedback do PO sobre os PNGs v2
- **Template (vale pras 4 células):** logo pequena do topo (`.mark`, ícone+wordmark SVG) removida —
  ficava duplicada com a logo grande (`heroLogo`) nas cenas 1. Agora só existe **1 logo por cena**,
  no topo do palco, e só quando `heroLogo:true`.
- **Mockups do front:** PO perguntou por que os shots continuam sendo prints antigos (`crop-*.png`)
  em vez de capturas novas do `aura-novofront`. Resposta curta: **Postflop está bloqueado no LOCAL**
  (tabelas `tbl_final_*_pooled` / `tbl_action_statistics_pooled` não existem; ver nota técnica
  abaixo). Preflop **já usa** captura real 2× (`mockup-preflop-app.png`, disc-04 cena 3). Os shots
  de Postflop (disc-01, disc-02, disc-04 cena 1) continuam nos crops antigos até isso destravar —
  não é decisão de design, é bloqueio de dado local.
- **disc-01:** cena 2 perdeu a legenda de rodapé; cena 3 ("A tela real", repetia o shot da cena 2)
  foi **deletada** — célula caiu de 6 pra 5 cenas, **21,0s** (desvio dos 26,0s das outras 3,
  registrado no build).
- **disc-02:** aprovado como estava, sem mudança de conteúdo.
- **disc-03:** cena 3 perdeu a legenda `produto real, não mockup` do print; cena 5 perdeu a
  legenda de rodapé.
- **disc-04:** rebalanceamento tipográfico da cena 1 (palavras seguem literais) — kicker
  `Inteligência de field · MTT` ganhou peso, headline `"Isso não existia."` encolheu, linha
  `"Mass Data Analysis..."` desceu. Motivo: o headline estava dominando o frame e a categoria
  (que é o ponto da célula 4) ficava em segundo plano.

**Nota técnica — por que Postflop não roda no LOCAL:** `FreqService.IsPooledEligible` só usa
`tbl_*_pooled`/`tbl_action_statistics_pooled` quando **nenhum filtro opcional** está ativo
(`Finest:Enabled=true` no LOCAL). Essas tabelas `_pooled` **não existem** no Postgres LOCAL — só
existem `_cube` (`tbl_final_flopip_cube` etc., com dado real, +400M linhas). Selecionando qualquer
filtro (textura de board, stack, etc.) a rota muda pra `_cube` e deveria funcionar; não foi validado
ponta a ponta ainda porque a investigação foi interrompida a pedido do Rafael no meio da sessão.
Quem pegar isso depois: comece por aí (nenhuma tabela precisa ser criada, só selecionar um filtro
antes de "Analisar").

### ⚠️ Desvio de produção registrado (fábrica → Mídia Paga)
**§3.5 pede crossfade 0,4s; os 4 saíram com CORTE SECO.** Motivo medido: cada cena tem Ken Burns
próprio, então no meio do crossfade a cena que sai e a que entra estão em **escalas diferentes** — os
elementos fixos (logo, rodapé e o **selo de prova do §3.2**) aparecem duplicados e deslocados. Como o
§3.2 exige o selo em *todas* as cenas, o defeito atingiria *todas* as transições, não só as densas.
Corte seco aplicado **igualmente nos 4**, então não afeta a comparabilidade — mas se a Mídia Paga
preferir o crossfade, é reverter uma constante no build e re-encodar.

### v2 produção (26/07) — o que mudou vs o design 25/07
- Dourado do `<em>`: cor chapada (sem gradiente/`brightGold`)
- Logo completa PNG nas cenas 1 de disc-01/02/03
- disc-01 cena 2: shot size-a-size (não mais barra única)
- disc-02 e disc-04: legendas queimadas removidas (ver §2 célula 4)
- Build: flag `--frames-only` para o PO aprovar PNGs antes do encode

> **Status 26/07:** ganchos literais intactos (exceto remoção da legenda do disc-04, registrada acima).
> Qualquer mudança de gancho ainda invalida a comparabilidade e volta pra esta mesa.

### Glossário de marca (usar consistente nos 4 reels)
| Termo | PT | EN |
|---|---|---|
| Categoria | **Inteligência de field** | **Field intelligence** |
| Método | **Mass Data Analysis (MDA)** | idem — não traduzir |
| Jargão técnico | RFI, 3bet, MDF, field, ICM | idem — não traduzir |
| Tagline | *O mesmo jogo — novas informações* | *Same game — new information* |

## 7. Nota de posicionamento (fora do escopo do anúncio)

O ângulo pioneiro tem valor **além** desta campanha: a varredura da Ads Library confirmou que **nenhum concorrente vende por dado populacional** — todos vendem feature, resultado ou medo. Então o território "field intelligence / MDA" está **desocupado no espaço publicitário**, independente de quem chegou primeiro no mundo. Isso é substanciável (é observação do que está no ar) e é um argumento mais forte que o superlativo.

Se a célula 4 vencer, a recomendação é elevar esse enquadramento de "um criativo" pra **posicionamento da marca** — e aí ele pede consistência na landing, no perfil e no produto, não só no anúncio.
