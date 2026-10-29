# Copy Meta Ads: estudo de sinal 01 (pós-Andromeda)

Status: rascunho para aprovação do Rafael. Nada publicado. Autor: copywriter Aura. Data: 2026-10-29.

4 ângulos, cada um para um público diferente. PT-BR para Brasil. EN para UK, CA, DE, NL, AT.

## Fonte dos números

Todos os números vêm de `content/posts/field-exploits-launch/numeros-verificados.md`, seção 2 ("Exemplo concreto: o 1.º spot"), consultas Q1 e Q5, snapshot 20261015, ranking refeito sobre a referência `20261022`. É o spot UTG vs BB, 25bb, SRP, flop A-high two-tone.

| Número usado | Valor | Onde aparece |
| --- | --- | --- |
| Fold do field no c-bet de 50% | 53,8% (EN 53.8%) | A |
| Fold do GTO nesse c-bet | 73,5% (EN 73.5%) | A |
| Desvio fora da faixa do GTO | 13,7% abaixo da faixa (EN 13.7% below the range) | D |
| Spot grátis da semana | 1 | C |

Nenhum outro número foi usado. Em B não há contagem de spots, para não depender de número do ranking.

Atenção ao Rafael: o spot Grátis troca toda segunda (primeira troca 02/11). Em C, o UTG vs BB 25bb é exemplo do tipo de spot, não a promessa de qual spot estará aberto no dia.

## Regras aplicadas (QA)

- Zero palavra do vocabulário de cassino ou aposta. Também fora do texto do anúncio: "bet" sozinho, "$", "EV", "win rate", conforme `docs/02-paid/compliance-meta.md` §3. Só entra "c-bet", porque é termo de poker pedido no brief. O tom de referência "bet mostly for value" foi adaptado para "go for value" / "vá de value" por esse motivo.
- Sem promessa de resultado. Descreve o desvio do field e o ajuste.
- A Aura não é tracker e não lê as mãos do usuário. Em D, "seu spot" e "sua decisão" falam do spot que o usuário abre e do que ele ajusta na própria decisão, não de diagnóstico das mãos dele.
- Sem bastidor (amostra, calibração, beta). Field Exploits leva "Novo módulo" / "New module".
- Sem concorrente nominal. Em D, "solver" aparece como categoria.
- Visuais: tela ou mockup do app, grid, régua. Sem carta, ficha, dinheiro ou mesa. Sem e-mail ou conta na captura.
- Targeting: 18+. Em EN, excluir os 18 mercados proibidos pela Meta (nenhum dos 5 países-alvo está na lista). Se NL, DE ou AT reprovarem em série, tirar o país do targeting.
- Limites conferidos: headline da arte até 6 palavras, apoio da arte até 8 palavras, primary text até 125 caracteres, headline do anúncio até 40, descrição até 30.

---

## A) FIELD EXPLOITS (recurso com o nome)

Público: grinder de MTT que já estuda e quer exploit pronto, por spot.

### A / PT-BR

| Campo | Texto | Caracteres |
| --- | --- | --- |
| Headline da arte | Field Exploits: onde o field erra | 6 palavras |
| Apoio da arte | Spot a spot. E como explorar. | 6 palavras |
| Primary text | UTG vs BB, 25bb: o BB folda 53,8% contra o c-bet de 50%. GTO: 73,5%. Blefe menos, vá de value. Veja o spot completo. | 110 |
| Headline do anúncio | Onde o field erra no flop | 25 |
| Descrição | Field Exploits · Novo módulo | 28 |
| CTA | Learn More | |
| Visual | Card do spot no app (régua Field 53,8% vs faixa do GTO em verde, linha "Como explorar") com selo NOVO MÓDULO no canto. | |

### A / EN

| Campo | Texto | Caracteres |
| --- | --- | --- |
| Art headline | Where the field gets it wrong | 6 words |
| Art support line | Spot by spot, and how to exploit it. | 8 words |
| Primary text | UTG vs BB, 25bb: the BB folds 53.8% vs a 50% c-bet. GTO folds 73.5%. Bluff less, go for value. See the full spot. | 113 |
| Ad headline | Where the field gets it wrong | 29 |
| Description | Field Exploits · New module | 27 |
| CTA | Learn More | |
| Visual | Spot card in the app (field fold marker vs green GTO range bar, "How to exploit" line) with a NEW MODULE badge in the corner. | |

---

## B) MÉTODO, NÃO MAIS CONTEÚDO

Público: quem já acumulou vídeo e curso e não sabe por onde começar.

### B / PT-BR

| Campo | Texto | Caracteres |
| --- | --- | --- |
| Headline da arte | Você não precisa de mais vídeo | 6 palavras |
| Apoio da arte | Precisa saber o que estudar primeiro. | 6 palavras |
| Primary text | Mais um curso não fecha seu leak. A Aura mostra onde o field mais erra: UTG vs BB 25bb, o BB defende demais. Veja o spot. | 115 |
| Headline do anúncio | Estude o spot certo primeiro | 28 |
| Descrição | Onde o field mais erra | 22 |
| CTA | Learn More | |
| Visual | Lista de spots do field no app, com o UTG vs BB 25bb destacado e a seta Overdefend ao lado. | |

### B / EN

| Campo | Texto | Caracteres |
| --- | --- | --- |
| Art headline | You don't need more videos | 5 words |
| Art support line | You need to know what to study first. | 8 words |
| Primary text | Another course won't fix your leak. Aura shows where the field errs most: UTG vs BB 25bb, 50% c-bet. See the spot. | 118 |
| Ad headline | Study the right spot first | 26 |
| Description | Where the field errs most | 25 |
| CTA | Learn More | |
| Visual | Field spot list in the app, UTG vs BB 25bb highlighted with an Overdefend tag. | |

---

## C) ENTRADA GRÁTIS

Público: quem ainda não conhece a Aura e quer testar sem compromisso.

Checado no repo: o plano Grátis existe, sem cartão, e dá preview de cada módulo (product-truth §6 e §9; STATE.md). No Field Exploits, o Grátis vê 1 spot da semana (numeros-verificados §1). A copy diz só "grátis, sem cartão" e "1 spot por semana". Não promete módulo completo no Grátis.

### C / PT-BR

| Campo | Texto | Caracteres |
| --- | --- | --- |
| Headline da arte | Comece grátis. Sem cartão. | 4 palavras |
| Apoio da arte | Um spot do field por semana. | 6 palavras |
| Primary text | Veja onde o field erra sem cartão. UTG vs BB 25bb: o BB defende demais contra o c-bet. Crie sua conta grátis. | 103 |
| Headline do anúncio | Comece grátis, sem cartão | 25 |
| Descrição | 1 spot do field por semana | 26 |
| CTA | Sign Up | |
| Visual | Tela de cadastro simples ao lado do card do spot grátis aberto no app (sem e-mail ou conta visível). | |

### C / EN

| Campo | Texto | Caracteres |
| --- | --- | --- |
| Art headline | Start free. No card needed. | 5 words |
| Art support line | One field spot, every week. | 5 words |
| Primary text | Start free, no card. See where the field errs: UTG vs BB 25bb, the BB defends too much vs the c-bet. Try it. | 108 |
| Ad headline | Start free, no card needed | 26 |
| Description | 1 field spot every week | 23 |
| CTA | Sign Up | |
| Visual | Simple sign-up screen next to the free spot card open in the app (no email or account visible). | |

---

## D) SEU ERRO EM SEGUNDOS

Público: quem trava no tempo de estudo e quer chegar rápido à decisão.

### D / PT-BR

| Campo | Texto | Caracteres |
| --- | --- | --- |
| Headline da arte | Spot lido em segundos | 4 palavras |
| Apoio da arte | Sem horas de solver. Com ajuste pronto. | 7 palavras |
| Primary text | Horas no solver para um spot? UTG vs BB 25bb: o BB folda 13,7% abaixo da faixa do GTO. Blefe menos. Veja o spot. | 118 |
| Headline do anúncio | Leia o spot em segundos | 23 |
| Descrição | O que muda na sua decisão | 26 |
| CTA | Learn More | |
| Visual | Close no título do detalhe ("O BB defende demais contra c-bet") e na linha "Como explorar", sem mais nada em volta. | |

### D / EN

| Campo | Texto | Caracteres |
| --- | --- | --- |
| Art headline | Your spot, read in seconds | 5 words |
| Art support line | Not hours in a solver. | 5 words |
| Primary text | Hours in a solver per spot? UTG vs BB 25bb: the BB folds 13.7% below the GTO range. Bluff less. See the spot. | 120 |
| Ad headline | Read the spot in seconds | 24 |
| Description | What to change in your play | 27 |
| CTA | Learn More | |
| Visual | Close-up of the detail title ("The BB defends too much vs the c-bet") and the "How to exploit" line, nothing else around it. | |

---

## Pendências para o Rafael

1. Aprovar os 4 ângulos e os dois idiomas. Nada foi publicado nem configurado na Meta.
2. Confirmar que "solver" em D (categoria, sem marca) é aceitável.
3. Os visuais ainda não existem. Se aprovado, a fábrica de posts faz os mockups a partir do app, sem conta ou e-mail na tela.
4. Landing de destino com rodapé "ferramenta de estudo · 18+" e sem link para sala de poker (compliance-meta §3).
