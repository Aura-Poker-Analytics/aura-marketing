# SINAL01 carrossel: bastidor da copy

Notas internas do carrossel "a Aura inteira" (29/10/2026). Copy em `content/ads/sinal01/carrossel/` (PT) e `.../carrossel/en/` (EN). Status: rascunho para aprovação do Rafael. Nada publicado nem configurado na Meta.

## Fontes

| O que | Fonte |
| --- | --- |
| Lista de módulos no ar | `aura-main/STATE.md` (Modo GTO com faixa v8 no turn e river, Field Exploits com flop, turn e river, Node-by-Node no ar desde 29/07) e `aura-landing/src/content/siteContent.ts` (PLATFORM_MODULES) |
| O que o Grátis vê | `aura-landing/src/content/pricing.ts` (FREE_PLAN e INDIVIDUAL_PLAN). O rodapé do cartão 9 não cita o Field Exploits no Grátis |
| 41,5% / 25,0% (BTN vs SB, 25bb, flop A-high rainbow, c-bet de 33%; faixa do GTO 19,0 a 31,0; 9.937 mãos) | `docs/02-paid/sinal01-spots-fortes.md` (linha 1) e `content/ads/sinal01/numeros/` (`spots_all.csv` e o script de medição `measure_spots.py`). Spot escolhido por ser forte nas faixas 5, 7/8 e 9: desvio fora da faixa de 10,5 nas três, centro do GTO igual (25,0). |
| 6,9 mi+ pontos de decisão GTO | `content/posts/field-exploits-launch/numeros-verificados.md` §1 e Q7 (6.991.627, arredondado para baixo; consulta Q7) |
| 90 situações pré-flop | `content/posts/field-ranges-launch/numeros-verificados.md` §2 |
| Marca, compliance | `brand/brand-kit.md`, `docs/02-paid/compliance-meta.md` |

Nenhum outro número foi usado. Não usei "Mais de 400 mil torneios" (a landing atual não traz a frase em `src`), nem "114 stats" do Field Trends (aparece na landing, mas não achei um `numeros-verificados.md` do Field Trends no repo), nem "8 spots" (o carrossel não precisa).

## Regras aplicadas

- Zero "bet" sozinho, "aposta", "ganhe", "lucro", "banca", "dinheiro", "EV", "$". Só "c-bet". O ajuste do cartão 2 é "C-bet mais vezes, inclusive sem mão", sem "aposte".
- Sem promessa de resultado. O benefício é de estudo: onde o field erra e como explorar.
- Sem bastidor: nada de amostra, calibração, beta ou "500M+". Field Exploits leva o selo NOVO MÓDULO / NEW MODULE.
- Modo GTO sempre como parte do plano Individual. Não há "plano GTO".
- Sem concorrente nominal. "Solver" aparece como categoria (como na H1 da landing e na tagline de marca).
- Field Trends: "variação normal", nunca "ruído".
- Visuais: telas do app, grade, gráfico. Sem carta, ficha, mesa, dinheiro, e-mail ou conta.
- O spot BTN vs SB 25bb c-bet de 33% (41,5% x 25,0%) é de uma classe de flop só: "flop A-high rainbow" (EN "A-high rainbow flop"). Toda citação do spot leva a classe, e os cartões 2 e 3 levam o n (9.937 mãos; EN 9,937 hands).
- Primary text até 125 caracteres, contagem conferida por script: A PT 116, A EN 103, B PT 117, B EN 110 (carrossel, após a troca de spot).
- Cartões 6 e 7 levam o selo "Exemplo ilustrativo" / "Illustrative example" (grade e gráfico são ilustrativos). Cartão 8: "Donk 33%" no lugar de "Bet".
- Targeting: 18+. Em EN, excluir os 18 mercados proibidos pela Meta (nenhum dos 5 países-alvo está na lista).

## Em dúvida, para o Rafael

1. `product-truth-aura.md` (09/07) está velho: diz "NÃO é solver / sem GTO" e traz "500M+". Segui STATE.md e a landing. Vale atualizar o gabarito.
2. A landing de destino precisa estar com as flags de lançamento ligadas (`VITE_LAUNCH_MODO_GTO` e `VITE_LAUNCH_FIELD_EXPLOITS`). `pricing.ts` ainda mostra o Modo GTO como "Em breve" e a lista de módulos o mostra como no ar. Se o clique cair numa página que não mostra o Modo GTO, o anúncio e a landing se contradizem. Conferir o build de produção antes de ativar.
3. Hotspot Analysis ficou fora: a landing o marca como "em breve". Se for para anunciar, é outra decisão.
4. Node-by-Node: a landing o lista só no Individual. Não afirmei o que o Grátis vê dele, e o rodapé do cartão 9 omite o módulo. Confirmar se o Grátis tem prévia.
5. Cartão 6: o dado "o field só paga com AA em 13% das vezes" existe e é verificado, mas é estimativa do field. Preferi o "90 situações". Se quiser a mão no cartão, entra com o texto de estimativa.
6. Cartão 2: nenhum cartão diz "spot da semana" nem promete qual spot o Grátis abre. O BTN vs SB 25bb é o exemplo.
7. Selo NOVO MÓDULO só no Field Exploits. Field Trends e Field Ranges também tiveram lançamento recente; a landing ainda chama o Trends de "Novo módulo". Decidir se leva selo.
8. Para escalar: sugiro testar a capa 1 contra a 2 (conceito contra mão) com o mesmo restante do carrossel, e o primary text A contra o B.
9. "Cadastre-se" (Sign Up) como botão fica coerente com o anúncio C do sinal01. "Saiba mais" é a alternativa se a conversão de cadastro vier fraca.
