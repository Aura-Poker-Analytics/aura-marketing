# SINAL01: bastidor da copy e das artes

Notas internas do estudo de sinal na Meta (29/10/2026). A copy está em `content/ads/sinal01/` e as artes em `content/ads/sinal01/art/` (HTML-fonte e CSS em `fonte/pt` e `fonte/en`).

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


## Pendências para o Rafael

1. Aprovar os 4 ângulos e os dois idiomas. Nada foi publicado nem configurado na Meta.
2. Confirmar que "solver" em D (categoria, sem marca) é aceitável.
3. Os visuais ainda não existem. Se aprovado, a fábrica de posts faz os mockups a partir do app, sem conta ou e-mail na tela.
4. Landing de destino com rodapé "ferramenta de estudo · 18+" e sem link para sala de poker (compliance-meta §3).

## Campanha na Meta

Campanha `120250240989100327`, conjuntos BR `120250240989470327` e EN `120250240992030327`, todos pausados, R$ 25/dia cada. Ativação só com o "pode ativar" da HUB.
