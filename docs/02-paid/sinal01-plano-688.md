# SINAL01: plano para R$ 688

Pedido do Rafael em 30/10, repassado pela HUB: "temos 688 reais na conta da meta ads. Refaça o plano com os 5 criativos pra esse montante e vamos colocar no ar." Substitui o orçamento de R$ 800 do `sinal01-bastidor.md`; as regras de corte e o objetivo ficam como lá.

## Objetivo
Medir qual ângulo traz cadastro (A Field Exploits, B método, C grátis, D segundos, carrossel da Aura inteira) e em qual país.

## Estrutura e dinheiro
- Campanha `120250240989100327`, otimização por cadastro (CompleteRegistration do pixel 1405949840871947), público aberto Advantage+.
- Trava: `spend_cap` de R$ 688 na campanha, conferido por leitura em 30/10, com R$ 0 gastos.
- Conjunto BR `120250240989470327` (PT) e conjunto EN `120250240992030327` (UK, CA, DE, NL, AT), com 5 anúncios cada.

| Fase | Duração | BR | EN | Total |
| --- | --- | --- | --- | --- |
| 1 · sinal | 7 dias | R$ 25/dia | R$ 25/dia | R$ 350 |
| 2 · concentrar | ~7 dias | os 2 melhores anúncios do país que respondeu melhor, ~R$ 48/dia | | ~R$ 338 |

A troca da fase 1 para a 2 vai à HUB com os números antes de qualquer mudança.

## Regras de corte (por anúncio)
- Pausar o anúncio que gastar R$ 35 sem nenhum cadastro e com CTR de link abaixo de 0,6%.
- Pausar o anúncio que gastar R$ 60 sem nenhuma sessão de mais de 30 s no GA4 (utm_content do anúncio).
- O conjunto BR sai se a sessão mediana dele no GA4 ficar abaixo de 5 s depois de R$ 100 gastos.
- Nada é cortado antes de R$ 35 por anúncio: abaixo disso a Meta ainda está aprendendo.

## Sucesso
- Principal: custo por cadastro. A meta é ≤ R$ 60 por cadastro qualificado, ou seja, com sessão de mais de 30 s ou 1 módulo aberto no app.
- Leitura por ângulo: cadastros e custo por cadastro de A, B, C, D e carrossel, em BR × EN.
- Escala em dezembro só se o melhor ângulo ficar ≤ R$ 60 por cadastro qualificado.

## Anúncios (todos começam juntos)
- BR: A `120250256109470327` · B `120250256086060327` · C `120250256086390327` · D `120250256109810327` · Carrossel `120250256090350327`
- EN: A `120250256110910327` · B `120250256088250327` · C `120250256088460327` · D `120250256111040327` · Carousel `120250255898570327`
- UTM: `utm_source=meta&utm_medium=paid&utm_campaign=aura-sinal01&utm_content=<a|b|c|d|carrossel>-<br|en>`, destino www.aurapoker.com/?lang=pt|en.

## Troca de criativos (01/11)
Frase final trocada por "C-bet muito mais!" / "C-bet way more!" depois da reprovação do Carrossel BR v3 por "imprimir" (PR #54). Os antigos só saem quando o substituto está ACTIVE.

| Anúncio | Novo | Estado em 01/11 | Antigo |
| --- | --- | --- | --- |
| C EN | `120250282314060327` (v3) | ACTIVE | `120250256088460327` arquivado em 01/11 |
| Carousel EN | `120250282314910327` (v2, ainda com a frase antiga no slide 2) | ACTIVE | `120250255898570327` arquivado em 01/11 |
| A BR, D BR, A EN, D EN | v3 `120250282311830327`, `…312010327`, `…313030327`, `…313620327` (frase antiga) | PENDING_REVIEW | seguem no ar |
| Carrossel BR | v3 `120250282312370327` | DISAPPROVED ("imprimir") | segue no ar |

Próximo: com as 6 artes novas subidas pelo cartão, criar A e D BR/EN, Carrossel BR e Carousel EN v3, ativar e arquivar os v3 e os antigos assim que os novos estiverem ACTIVE.

### v4 no ar (03/11)
Artes v4 subidas pelo cartão; anúncios criados e ativados, em revisão (IN_PROCESS) na leitura de 03/11:
A BR v4 `120250314164020327` · D BR v4 `120250314167510327` · Carrossel BR v4 `120250314169870327` · A EN v4 `120250314172140327` · D EN v4 `120250314173660327` · Carousel EN v3 `120250314174950327`.
Carrossel BR v3 (reprovado) arquivado em 03/11. Quando cada v4 ficar ACTIVE, saem o v3 e o antigo correspondentes (A/D BR e EN, Carrossel BR antigo, Carousel EN v2).
