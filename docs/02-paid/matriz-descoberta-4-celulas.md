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

| # | Célula | Persona testada | Hipótese | Ativo-base |
|---|---|---|---|---|
| 1 | **SOLVER** | Reg que estuda solver | "Quem investe em teoria sente que decorar equilíbrio não descreve o oponente real" | adaptar `paid01-v2-field` |
| 2 | **EXPLOIT** | Jogador exploitativo | "Quem caça desvio quer o número do pool, não o ótimo" | adaptar `paid01-v3-leak` |
| 3 | **CATEGORIA** | MTT player sem contexto prévio | "O conceito se vende sozinho, sem precisar de solver/tracker como referência" | adaptar `reel-01-launch` |
| 4 | **TRACKER** | Usuário de HUD/tracker | "Quem já valoriza dado próprio entende na hora o valor do dado populacional" | **novo** |

**Por que essas 4:** cada uma corresponde a um comportamento observável e mutuamente distinto (estuda teoria / caça exploit / não usa nada / coleta dado próprio). Se as 4 fossem variações do argumento "o field desvia", elas atrairiam a mesma pessoa e o teste não separaria nada.

**Célula 3 é o controle conceitual** — a mais ampla, sem pressupor ferramenta. Se ela vencer, o conceito vende sem âncora; se perder para 1/2/4, o comprador é quem já usa alguma ferramenta.

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

### Célula 4 · TRACKER — `disc-04-tracker`
> **Kicker:** `Pra quem já usa tracker`
> **Gancho:** **"Seu tracker mostra as suas mãos."**
> *(beat)* **"E as outras 500 milhões?"**

- **Deve parar:** usuário de HUD/tracker — já paga por dado, entende amostragem
- **Deve rolar:** quem joga sem ferramenta nenhuma
- **Por quê:** é a persona com maior disposição a pagar comprovada (já assina ferramenta). A pergunta reenquadra escala como benefício

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
| Célula 4 | `disc-04-tracker` |

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

- [ ] **PO valida as 4 personas** (§1) — trocar alguma é decisão dele
- [ ] PO valida os 4 ganchos (§2) — é o que determina a legibilidade do teste
- [ ] Só então: fábrica produz roteiro completo + render **PT**, e o EN depois de aprovada a PT
