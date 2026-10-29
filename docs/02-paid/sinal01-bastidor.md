# SINAL01: bastidor da copy e das artes

Notas internas do estudo de sinal na Meta (29/10/2026). A copy está em `content/ads/sinal01/` e as artes em `content/ads/sinal01/art/` (HTML-fonte e CSS em `fonte/pt` e `fonte/en`).

Status: rascunho para aprovação do Rafael. Nada publicado. Autor: copywriter Aura. Data: 2026-10-29.

4 ângulos, cada um para um público diferente. PT-BR para Brasil. EN para UK, CA, DE, NL, AT.

## Fonte dos números

Spot escolhido em 29/10/2026. Todos os números vêm de `docs/02-paid/sinal01-spots-fortes.md` (linha 1 da tabela "Os 3 melhores") e de `content/ads/sinal01/numeros/spots_all.csv`, gerado por `content/ads/sinal01/numeros/measure_spots.py` (medição sobre o calendário do Field Exploits `tbl_field_exploit_release 20261026`). É o spot `btn_sb` (BTN abre, SB defende), pote SRP, 25bb, flop A-high rainbow desconectado, c-bet de 33%.

| Número usado | Valor | Onde aparece |
| --- | --- | --- |
| Fold do field (SB) contra o c-bet de 33% | 41,5% (EN 41.5%) | A, C, D, carrossel 2 e 3 |
| Fold do GTO nesse c-bet | 25,0% (EN 25.0%) | A, C, D, carrossel 2 e 3 |
| Faixa do GTO | 19,0 a 31,0 (centro 25,0) | régua de A, C e do carrossel |
| Desvio fora da faixa do GTO | 10,5% acima da faixa (EN 10.5% above the GTO range) | A e C |
| Direção | Overfold (o SB folda demais) | A, B, C, D, carrossel 2 |
| n | 9.937 mãos (EN 9,937 hands) | linha do spot de A e C e dos cartões 2 e 3 |

Por que este spot: ele é forte nas três faixas medidas (v5, v7/v8 e v9), com desvio fora da faixa de 10,5 nas três e centro do GTO igual (25,0) nas três. Assim o número não muda se o flop migrar da faixa 5 para a 7/8 depois do lançamento (V8-FLOP). O spot antigo cairia para 0 na v7/v8.

Nenhum outro número foi usado. Em B não há contagem de spots, para não depender de número do ranking.

Atenção ao Rafael: nenhum criativo diz "spot da semana" nem promete qual spot o Grátis abre. Em C o mockup é rotulado "Exemplo de spot" / "Example spot", sem selo de grátis, e a copy diz só "grátis, sem cartão". O BTN vs SB 25bb é exemplo do tipo de spot.

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

## Regras do estudo (duas fases, decisão do Rafael em 29/10)

Verba total R$ 800, R$ 50/dia (R$ 25 por conjunto). 5 anúncios por conjunto: os ângulos A, B, C, D e o carrossel da Aura inteira.

**Fase 1, semana 1 (~R$ 350).** Tudo rodando, sem nenhuma edição por 7 dias (orçamento, público e criativo intocados). Leituras:
- Por anúncio e país: cliques no link, sessões com mais de 30 s (GA4, `utm_content`), cadastros no `tbl_user` (`utm_content`), custo por sessão qualificada e por cadastro.
- BR: tempo mediano de sessão por clique. Em agosto era 0,1 a 0,2 s.

Regras de corte durante a fase 1 (únicas exceções ao "não mexer"):
- Anúncio que gastar R$ 60 sem nenhuma sessão de mais de 30 s: pausar.
- Anúncio reprovado pela Meta: pausar e registrar em `docs/02-paid/log-reprovacoes.md`.

Fim da fase 1 (dia 7), decisão:
- BR sai se o tempo mediano de sessão for menor que 5 s; a verba inteira vai para o EN.
- Escolher o país que respondeu melhor (custo por sessão qualificada; cadastro desempata).
- Nesse país, ficar com os 2 anúncios de menor custo por sessão qualificada (cadastro, se houver, pesa mais).
- A troca de fase vai à HUB com os números antes de qualquer mudança na conta.

**Fase 2 (~R$ 450, R$ 50/dia, ~9 dias).** Só os 2 anúncios escolhidos, no país escolhido. Objetivo: 6 a 8 cadastros e o primeiro custo por cadastro do vencedor. Escala só depois disso: se o custo por cadastro qualificado ficar em até R$ 60 por 2 semanas, propor ao Rafael cerca de R$ 2.000 no vencedor por 4 semanas.

Prova da UTM: o primeiro cadastro do estudo precisa chegar ao `tbl_user` com `utm_campaign=aura-sinal01`. Se não chegar em 3 dias com cliques, a HUB é avisada antes de seguir.
