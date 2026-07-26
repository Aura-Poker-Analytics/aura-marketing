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
> **Gancho:** **"Você decorou o equilíbrio."**
> *(beat)* **"Seu oponente não."**

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

**⚠️ Duas versões — decisão do PO, e a escolha tem consequência:**

**(a) Versão substanciável (recomendada)**
> **Kicker:** `Field intelligence · MTT`
> **Gancho:** **"Isso não existia."**
> *(beat)* **"500M+ mãos de MTT — lidas como população, não como amostra."**

**(b) Versão reivindicatória (a que você pediu)**
> **Kicker:** `Field intelligence · MTT`
> **Gancho:** **"A primeira ferramenta de field intelligence do mundo."**
> *(beat)* **"Mass Data Analysis aplicada a MTT."**

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
> **Estrutura:** 1 campanha · **1 conjunto** · 4 anúncios competindo. Um conjunto só — dividir em 4 fragmentaria o orçamento e cada célula ficaria sem volume pra ler.
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

- [x] ~~PO valida as personas~~ — **feito 25/07:** TRACKER cortado (não rivalizamos com tracker), PIONEIRO entra no lugar
- [ ] **PO escolhe a versão da célula 4:** (a) substanciável *"Isso não existia"* ou (b) reivindicatória *"primeira do mundo"* — ver riscos em §2
- [ ] PO valida os ganchos das células 1–3 (§2) — é o que determina a legibilidade do teste
- [ ] Só então: fábrica produz roteiro completo + render **PT**, e o EN depois de aprovada a PT

## 7. Nota de posicionamento (fora do escopo do anúncio)

O ângulo pioneiro tem valor **além** desta campanha: a varredura da Ads Library confirmou que **nenhum concorrente vende por dado populacional** — todos vendem feature, resultado ou medo. Então o território "field intelligence / MDA" está **desocupado no espaço publicitário**, independente de quem chegou primeiro no mundo. Isso é substanciável (é observação do que está no ar) e é um argumento mais forte que o superlativo.

Se a célula 4 vencer, a recomendação é elevar esse enquadramento de "um criativo" pra **posicionamento da marca** — e aí ele pede consistência na landing, no perfil e no produto, não só no anúncio.
