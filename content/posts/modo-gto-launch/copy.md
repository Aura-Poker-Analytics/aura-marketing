# Modo GTO: copy de lançamento (GTO no flop, turn e river)

Status: pacote final para aprovação do Rafael; não publicado. **Versão de 15/10**, depois do retorno do Rafael sobre o aura-marketing#4 (via HUB): "sim leva" para o "por tempo limitado" e pedido de um carrossel mais apelativo, de grande lançamento: foi lançado e a inclusão no plano é temporária. Números fechados em 14/10 (antes: 08/10). Publicar só depois dos gates em Pendências (P-61, teste logado, Stripe, hospedagem das imagens do e-mail, **GATE B1** (data interna a honrar e reconciliação da landing) e **GATE A2** (frase da conta grátis)). Revisão de 15/10: o revisor deu NÃO OK ao carrossel de lançamento, e o Rafael decidiu (via HUB) que **a inclusão do GTO no Individual é a temporária**; este texto é a correção (preço = o do plano, o temporário é a inclusão; carrossel só com legenda EN).
@aurapokeranalytics: a confirmar pelo Rafael. URLs com UTM prontas na tabela abaixo.
Fonte dos números: `aura-main/_ops/golive-gto-2026-10-14/numeros-verificados-lancamento.md` (origin/main `e17fc8e`, 14/10), para a cobertura, o pré-flop e o exemplo de abertura; o exemplo CO × BB e o pré-flop seguem iguais aos de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10). Os números usados estão mapeados em "Números usados" no fim. **Nenhum marcador `[[...]]` resta no pacote.**
Peças deste pacote: Discord (também em `discord.md`), Instagram (feed, story, story da capa em PT, carrossel de 6 slides só em EN), landing e e-mail (em `email.md`).

> **Regra de texto das artes (Rafael, 08/10): "muita informação, muito texto; não pode ter tanto texto em nenhum post".** Cada arte tem no máximo UM título curto (~6 palavras) e, se precisar, UMA linha de apoio (~10 palavras). A imagem fala: barras field × GTO lado a lado, com os números. O detalhe vai para a legenda. Em toda arte só ficam o `@aurapokeranalytics` e o `18+`, pequenos. O link é o sticker/link na bio, não texto de arte. A frase do plano (GTO incluso no Individual com preço, por tempo limitado, e conta grátis) fica na legenda, no Discord, na landing e no e-mail; nas artes, o plano com o preço aparece só na capa do carrossel (apoio), no slide 5 (título, número gigante e apoio) e no story da capa PT (apoio), sempre com a moeda do idioma (EN "US$ 29/month", PT "R$ 150/mês"). O preço é o do plano Individual; o que é temporário é a inclusão do GTO, e isso é dito sem promessa de preço travado, de que quem assina agora mantém o GTO, de preço futuro ou de data. Nas artes não entram contagem de mãos nem "amostra"; nas legendas e no e-mail também ficam de fora.

## Origem das capturas e artes a refazer (por outro agente)
- **Slide 3 (turn e river):** barras renderizadas pela build, duas por spot (Second Barrel e Turn Delayed CBet, CO × BB, 30–60bb, GTO a 40bb, SRP, flop two-tone, qualquer turn), ou a captura nova do aura-novofront `35d7005` (prévia local, API de prévia, 14/10) **só se ela mostrar exatamente** 54,2% / 57,2% (50,8–63,5) e 51,7% / 44,1% (37,8–50,3) nesse recorte. Se a captura mostrar outro recorte ou outros valores, usar as barras. Os valores novos do Second Barrel vão para o `numbers.json` (chaves novas, sugestão N11), e nada numérico mora no HTML.
- **Slide 4 (pré-flop) e imagem EN do e-mail:** capturas de 08/10 do aura-novofront `429c093` (front no SHA de produção daquele dia, lendo a API local `:7060` com os snapshots do go-live, por conta de teste local, sem login em produção). Os mesmos números foram confirmados em produção em 14/10. A imagem do e-mail EN é o recorte do card de 33% do painel de Fold por tamanho de Flop CBet; a célula do CO no slide 4 tem um contorno âmbar desenhado só para destaque.
- **Slide 2, capa do story PT e imagem do e-mail PT:** barras renderizadas pela build (46,0% / 38,8% / faixa 37,1–40,4%), não são captura.
- **Capa do carrossel (slide 1):** sem número em arte além do apoio; a imagem é a do produto ou as barras do slide 2 com o gap em âmbar, a critério do designer, sem repetir o texto do slide 2.
- **Carrossel de 6 slides (versão de 15/10):** substitui o de 7. O slide 5 antigo (barras do Turn Delayed CBet) foi fundido no slide 3; o slide 6 antigo (plano) virou o slide 5 (incluso no Individual); o CTA virou o slide 6. Indicador "n / 6". Renomear/regerar `carrossel-en-01` a `-06` e apagar `carrossel-en-07.*`.
- Nenhuma peça chama as capturas de "print de produção".

## Pendências reais
1. **P-61 no ar e ordem de publicação.** Só postar ou enviar depois do P-61 no ar (Modo GTO aberto ao Individual) e depois que a versão de 13/10 estiver em produção.
2. **Preço e inclusão temporária (Rafael confere no Stripe).** Decisões do Rafael via HUB: 13/10, "vamos anunciar como fazendo parte do plano de 29 por tempo limitado"; 15/10, "sim leva" ao "por tempo limitado" e **a inclusão do GTO no Individual é a temporária**. **US$ 29 / R$ 150 é o preço mensal normal do plano Individual, não um preço promocional:** o que é temporário é a inclusão do GTO, não o preço. A frase do plano (versão final de 15/10) é: PT "O Modo GTO está incluso no plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF." EN "GTO Mode is included in the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison." Mensagem curta (capa e legenda): PT "Modo GTO no ar. Incluso no plano Individual (R$ 150/mês) por tempo limitado." EN "GTO Mode is live. Included in the Individual plan (US$ 29/month) for a limited time." Fonte do valor (HUB): `aura-landing` `src/content/pricing.ts` e `aura-novofront` `billingPlans.ts` (US$ 29/mês no checkout em EN, R$ 150/mês no checkout em PT). **Pendente: o Rafael confere no Stripe que o checkout cobra 29 / 150 hoje.** Regras: PT sempre "plano Individual" e "R$ 150/mês" (nunca "US$ 29" nem "R$ 29" em peça PT); EN sempre "Individual plan" e "US$ 29/month" (nunca "R$ 150" em peça EN). Urgência só por "por tempo limitado" / "for a limited time": sem data de fim, sem "últimas horas", sem "só hoje". **Nenhuma peça diz** que quem assina agora mantém o preço ou o GTO, nem fala de preço futuro, plano GTO à parte ou data. As pendências da inclusão temporária são o **GATE B1** (item 8). Nenhuma peça cita o plano Modo GTO à parte, o plano Top, desconto semestral/anual ou outra promoção.
3. **Teste logado do Rafael.** Conferir em `www.aura.poker` os mesmos valores do exemplo CO × BB (46,0% / 38,8% / faixa 37,1–40,4%), do RFI do CO (31,6% / 37,0%), do exemplo de abertura (Turn Delayed CBet 51,7% / 44,1% / faixa 37,8–50,3%) e do Second Barrel do mesmo recorte (54,2% / 57,2% / faixa 50,8–63,5%, usado no slide 3 do carrossel e na legenda), antes de qualquer post ou envio.
4. **Hospedagem das imagens do e-mail (aura-landing#17).** `email/modo-gto-pt.png` e `-en.png` precisam estar em `https://www.aurapoker.com/email/` antes do envio.
5. **Cobertura: nunca vira "todas".** A tela não cobre todas as ações (por exemplo, o c-bet do flop como abertura, o donk do flop e o probe do river não são feature). Nenhuma peça usa "todas / every / all" para cobertura, nem cita o c-bet do flop, o donk ou o probe do river como feature. O texto fica nas formas abaixo.
6. **"Por tempo limitado" sem data (recomendação do revisor, CONAR/CDC).** Expressão de urgência sem data de fim pode ser questionada. Recomendação: combinar uma data de fim e honrá-la, ou tirar a expressão. O Rafael respondeu "sim leva" em 15/10: o post leva "por tempo limitado". As peças mantêm "por tempo limitado" / "for a limited time", sem data. Se uma data for combinada depois, ela entra em todas as peças ao mesmo tempo (capa do carrossel, slide 5, story da capa, legendas, Discord, landing, e-mail).
7. **Dependências de produção.** (a) aura-api#84: o turn e o river de co_btn, utg_bb@25 e outros pares ficam fora hoje até o deploy; o texto de cobertura só vale com esse deploy feito. (b) A landing de produção não pode mostrar o GTO como plano à parte (nem preço próprio); só como parte do Individual.
8. **GATE B1: inclusão temporária do GTO no Individual (nada publica antes).** O Rafael decidiu (via HUB, 15/10) que **a inclusão do GTO no Individual é a temporária**; US$ 29/mês e R$ 150/mês são o preço normal do plano. Faltam:
   - **Data de fim interna:** se há uma a honrar, mesmo sem divulgá-la (CONAR/CDC). Se a data for combinada, entra em todas as peças ao mesmo tempo.
   - **Reconciliação da landing já publicada, em sessão do aura-landing:** `docs/lancamento-modo-gto.md:101`, `v5.test.ts:319` e `356-364`, `faq.ts:162` e `182` (a FAQ diz "mantém o preço"), `pricing.ts:184-187`.
   - **Oferta em dólar para público BR:** CDC art. 31; a HUB decide (as peças PT usam R$, as EN usam US$, sem misturar moedas na mesma peça).
   Até lá, nenhuma peça promete preço travado/garantido, que quem assina agora mantém o GTO, preço futuro, plano GTO à parte ou data de fim, e nenhuma cita desconto semestral/anual.
9. **Second Barrel no slide 3.** Entra como contraste (dentro da faixa) ao lado do Turn Delayed CBet (acima do topo), do mesmo recorte largo do arquivo de 14/10. A captura `35d7005` só serve se mostrar esses valores; senão, barras da build.
10. **Linha de fonte do preço (pedido à HUB).** As peças citam o preço do Individual (US$ 29 / R$ 150 mensal) e nenhum dos dois `numeros-verificados` tem linha de fonte para ele (`golive-gto-2026-10-04` e `golive-gto-2026-10-14/numeros-verificados-lancamento.md`). A HUB deve incluir uma linha de preço (Individual US$ 29 / R$ 150 mensal) em `numeros-verificados-lancamento.md`, com a origem (`pricing.ts`, `billingPlans.ts`, checkout/Stripe); até lá, a fonte é a indicação da HUB e a conferência do Rafael no Stripe.
11. **GATE A2: frase da conta grátis.** "A conta grátis segue com o field e a comparação com o MDF" (feed PT e EN, Discord, landing, e-mail) só fica se o teste logado do Rafael confirmar, com uma conta Grátis, que ela continua vendo o field e a comparação com o MDF sem o número GTO. Se não confirmar, a frase sai de todas as peças.

## Decisões registradas
- **Cobertura (texto final, HUB 14/10).** PT: "GTO no flop, no turn e no river. No flop, a reação ao c-bet e ao raise. No turn e no river, também a frequência de aposta do agressor (second barrel, delayed c-bet, probe no turn, third barrel)." EN: "GTO on the flop, turn and river. On the flop, the response to the c-bet and to the raise. On the turn and river, also the aggressor's betting frequency (second barrel, delayed c-bet, turn probe, third barrel)." Nas legendas curtas e no e-mail, versão curta: "no flop, turn e river" e "inclusive as aberturas do agressor no turn e no river", com a lista só "second barrel, delayed c-bet e third barrel" quando houver lista (EN "on the flop, turn and river" e "including the aggressor's openings on the turn and river"; "second barrel, delayed c-bet and third barrel").
- **Capa de lançamento (15/10, substitui a "capa com duas linhas" de 08/10).** A capa do carrossel ("GTO Mode is live") e a do story PT ("Modo GTO no ar") têm só título e UMA linha de apoio, que diz o plano com o preço e "por tempo limitado" ("Included in Individual (US$ 29/month) for a limited time." / "Incluso no plano Individual (R$ 150/mês) por tempo limitado."). A capa EN leva a pílula LIVE e a do story PT a pílula NO AR: são marcas de lançamento, não selo de desconto. Sai a micro-legenda do spot; não há mais exceção à regra de uma linha. No story PT, o spot vai como rótulo do gráfico ("CO × BB · c-bet de 33% · exemplo"), que não é uma segunda linha de apoio.
- **Preço = plano; o temporário é a inclusão do GTO (decisão do Rafael via HUB, 15/10).** US$ 29 / R$ 150 é o preço normal do Individual. O preço aparece só na capa do carrossel, no slide 5 e no story da capa PT, com a moeda do idioma. Em cada arte, "limited time" / "por tempo limitado" aparece UMA vez. Nenhuma arte leva selo de oferta ou de desconto; as pílulas LIVE (carrossel) e NO AR (story PT) só marcam o lançamento. Sem data, sem "últimas horas", sem preço travado, sem promessa de que quem assina agora mantém o GTO, sem preço futuro, sem desconto semestral/anual. **Nota interna: o termo "early bird" está reservado para o lançamento do plano próprio e não aparece em nenhuma peça deste pacote.**
- **Carrossel só com legenda EN (revisão de 15/10).** A legenda PT do carrossel saiu: a PT fica no feed PT e no story, e a legenda do carrossel não mistura moedas.
- **Carrossel de 6 slides, só em EN (15/10).** 1 capa de lançamento; 2 o exemplo do c-bet de 33% (Overfold); 3 turn e river com dois spots lado a lado (Second Barrel dentro da faixa, Turn Delayed CBet acima do topo); 4 pré-flop; 5 incluso no Individual (US$ 29/month); 6 CTA. Cada slide: título curto e no máximo UMA linha de apoio; a imagem fala.
- **Slide 3 usa o Second Barrel como contraste (15/10).** O Second Barrel (54,2% / 57,2%, faixa 50,8–63,5, dentro da faixa) e o Turn Delayed CBet (51,7% / 44,1%, faixa 37,8–50,3, 1,4 pp acima do topo) vêm do mesmo recorte largo (28 classes de board; `numeros-verificados-lancamento.md`, 14/10), onde o arquivo permite o Second Barrel "só como contraste". Não usar o Probe (faixa larga) nem a célula de um board só.
- **Slide 4 mostra os números arredondados da tela.** A captura traz Field 32% / GTO 37% / −5. A fonte tem 31,6 / 37,0 / −5,4; as legendas e a landing usam os valores da fonte.
- **Stories e feed** seguem com o exemplo CO × BB (c-bet de 33%). O exemplo de abertura (Turn Delayed CBet) e o Second Barrel só vivem no carrossel (slide 3 e legenda); Discord, landing e e-mail ficam com um exemplo só.
- **Sem contagem de mãos nem amostra.** O brand-kit pede rodapé de amostra em post com número; a instrução do Rafael de 08/10 o substitui. Ficam fora a contagem de mãos do exemplo de abertura (80 mil), as 10.216 mãos do exemplo CO × BB e o número de oportunidades do pré-flop (23,8 milhões).
- **Bug do front a lembrar.** O app em PT mistura formatos no mesmo card ("46.0%" e "38,8%"). Nas peças em PT escrevemos sempre com vírgula.

## Fatos de produto aplicados
- **Dois números ao lado do field:** o número GTO e a faixa GTO. Rótulos de resultado do app que podem aparecer em legenda: "dentro da faixa GTO" e "acima da faixa GTO" (EN "inside the GTO range", "above the GTO range").
- **Fluxo:** "escolha o spot, clique em Apply e veja o field e o GTO juntos" e "a faixa de status do app guia cada clique até ter GTO" (EN "the app's status bar guides you, click by click, until GTO is there"). Sem citar as frases em inglês da tela. Nada de "GTO em breve" nem "ainda sem GTO" como feature.
- **Pré-flop:** "o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb" (pré-flop `20261007`).
- **Filtro do exemplo nas peças:** "torneios Regular" (EN "Regular tournaments") e "últimos 2 anos" (EN "last 2 years"), sem a palavra vanilla.
- **Plano e conta Grátis:** frase única da Pendência 2 (o GTO está incluso no plano Individual, com o preço do plano, por tempo limitado; o temporário é a inclusão). Vive na legenda do feed, na legenda do carrossel (só EN), no Discord, na landing (sob o CTA) e no e-mail (sob o botão); na arte, só a capa do carrossel, o slide 5 e a capa do story PT. A parte da conta grátis é o GATE A2. CTAs de texto: "Conhecer o Modo GTO" / "See GTO Mode"; nenhum diz "grátis". O slide 6 do carrossel usa "Get GTO Mode" (pedido do Rafael via HUB), que não promete gratuidade: a conta grátis segue só com o field e o MDF. O único preço citado é o do plano Individual, com a moeda nunca trocada.
- **Escopo da referência:** a ressalva de torneios vanilla fica só na Metodologia do app (pedido do Rafael em 06/10). Nenhuma peça a repete; "Regular" aparece só como filtro do spot.
- **"Spot"** é a situação ou a decisão, nunca contagem de linhas.
- **Formato dos números:** vírgula em PT (46,0%), ponto em EN (46.0%).
- **Nome em inglês:** "GTO Mode".
- **Carrossel só em EN;** a capa tem story PT-BR 1080x1920 ("Modo GTO no ar", incluso no Individual em R$). Não há story EN da capa.

## O exemplo (reação ao c-bet; exemplo (a))
Filtro da tela: Postflop · SRP · RFI CO, caller BB · stack 30.1–60bb (GTO a 40bb) · torneio Regular · flop K-high, two-tone, sem par, desconectado · reação do BB ao c-bet de 33%.
- Field folda **46,0%**; GTO folda **38,8%** (38,78 na API), faixa **37,1–40,4%** (37,13–40,43); diferença **+5,6 pp** (a tela mostra a distância ao topo da faixa; contra o centro do GTO são 7,2). Leitura: acima da faixa.

**Texto final do exemplo, PT:** "CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board."

**Final example text, EN:** "CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board."

**Exemplo de pré-flop (exemplo (b)):** RFI do CO, torneio Regular, stack 30–50bb (GTO a 40bb). Field abre **31,6%**; GTO abre **37,0%**; diferença **−5,4 pp** (o field abre de menos). PT: "No pré-flop, RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos: o field abre 31,6% e o GTO abre 37,0%." EN: "Preflop, CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years: the field opens 31.6% and GTO opens 37.0%."

## O exemplo de abertura do agressor (Turn Delayed CBet)
Spot (recorte largo): CO × BB · 30–60bb (GTO a 40bb) · SRP · flop two-tone · turn qualquer · torneios Regular · últimos 2 anos. Ação: Turn Delayed CBet (o CO aposta o turn depois do flop passado). Métrica: frequência da aposta do CO, field contra GTO. Field aposta **51,7%**; GTO aposta **44,1%**, faixa **37,8–50,3%**; **1,4 pp acima do topo da faixa**. Leitura: acima da faixa (o field aposta mais do que o GTO). Resumo para o apoio da arte: "CO × BB · two-tone · turn".

**Texto final, PT:** "CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop two-tone, qualquer turn. No turn, depois do flop passado, o CO aposta (delayed c-bet): o field aposta 51,7% e o GTO aposta 44,1% (faixa 37,8–50,3%): 1,4 pp acima do topo da faixa. Aqui o field aposta mais do que o GTO. É um spot, não a média do field. Confira no seu board."

**Final text, EN:** "CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, two-tone flop, any turn. On the turn, after the flop checks through, the CO bets (delayed c-bet): the field bets 51.7% and GTO bets 44.1% (range 37.8–50.3%): 1.4 pp above the top of the range. Here the field bets more than GTO does. This is one spot, not the field average. Check it on your board."

## URLs por peça
Regra: Discord leva ao app (`https://www.aura.poker/`); Instagram e e-mail levam à landing (`https://www.aurapoker.com/`). Parâmetros: `utm_source=<fonte>&utm_medium=<meio>&utm_campaign=modo-gto-launch&utm_content=<peça>`.

| Peça | Idioma | Destino | utm_source | utm_content | URL |
|---|---|---|---|---|---|
| Discord PT | PT | app | discord | discord-pt | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt |
| Discord EN | EN | app | discord | discord-en | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en |
| Feed (link na bio) | PT e EN | landing | instagram | feed | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=feed |
| Story (sticker de link) | PT e EN | landing | instagram | story | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=story |
| Story da capa do carrossel (sticker de link) | PT | landing | instagram | story-capa-pt | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=story-capa-pt |
| Carrossel, só EN (link na bio) | EN (legenda só EN) | landing | instagram | carrossel-en | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=carrossel-en |
| Landing (botão de CTA, para o cadastro no app) | PT e EN | app | landing | modo-gto (utm_medium=website) | https://www.aura.poker/Login?tab=signup&utm_source=landing&utm_medium=website&utm_campaign=modo-gto-launch&utm_content=modo-gto |
| E-mail PT | PT | landing | email | pt | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=pt |
| E-mail EN | EN | landing | email | en | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=modo-gto-launch&utm_content=en |

Observação: para o botão da landing mantive `utm_source=landing`, como no Field Trends. Ajustar se o Rafael preferir outro valor.

## Rodapé
- **Artes:** só `@aurapokeranalytics · 18+`, pequeno.
- **Legendas, landing e e-mail:** PT "Ferramenta de estudo. 18+." / EN "Study tool. 18+." (na landing, também "A Aura não é site de apostas e não oferece jogo.").

---

# (a) Instagram

## Texto final de cada arte (título + apoio)

Em toda arte, além do título e da linha de apoio: logo AURA, `@aurapokeranalytics · 18+` pequeno e, nos slides, o indicador "n / 6". Nas barras, o % central do GTO no rótulo e a faixa GTO como sombreado, com a faixa escrita pequena.

| Arte | Formato | Idioma | Título | Apoio (uma linha) | O que a imagem mostra |
|---|---|---|---|---|---|
| Feed | 1080x1350 | PT | Mesmo spot, dois números | CO × BB · K-high two-tone · c-bet de 33% | Barras de fold lado a lado: Field 46,0% e GTO 38,8% (faixa 37,1–40,4%) |
| Feed | 1080x1350 | EN | Same spot, two numbers | CO × BB · K-high two-tone · 33% c-bet | Fold bars side by side: Field 46.0% and GTO 38.8% (range 37.1–40.4%) |
| Story | 1080x1920 | PT | O field folda mais que o GTO? | CO × BB · K-high two-tone · c-bet de 33% | Mesmas barras (46,0% e 38,8%); sticker de link "Conhecer o Modo GTO" |
| Story | 1080x1920 | EN | Does the field fold more than GTO? | CO × BB · K-high two-tone · 33% c-bet | Same bars (46.0% and 38.8%); link sticker "See GTO Mode" |
| Story da capa do carrossel (novo, 15/10) | 1080x1920 | PT | Modo GTO no ar | Incluso no plano Individual (R$ 150/mês) por tempo limitado. | Pílula NO AR (marca de lançamento, não selo de desconto); barras de fold do exemplo (46,0% e 38,8%, faixa 37,1–40,4% sombreada) com o gap em âmbar e o rótulo do gráfico "CO × BB · c-bet de 33% · exemplo" (rótulo, não segunda linha de apoio); sticker de link "Conhecer o Modo GTO" |
| Carrossel 1 (capa de lançamento) | 1080x1350 | EN | GTO Mode is live | Included in Individual (US$ 29/month) for a limited time. | Capa de grande lançamento: logo grande, pílula LIVE (marca de lançamento, não selo de desconto) e a janela do produto com o Modo GTO (ou as barras do slide 2, sem repetir o texto dele). Sem micro-legenda do spot |
| Carrossel 2 | 1080x1350 | EN | See where the field breaks from GTO | CO × BB · K-high two-tone · 33% c-bet | As barras e os dois números: Field 46.0%, GTO 38.8% (range 37.1–40.4%), gap em âmbar |
| Carrossel 3 | 1080x1350 | EN | GTO on the turn and river | Second barrel: inside the range. Delayed c-bet: above. | Dois pares de barras de aposta lado a lado, mesmo spot (rótulo pequeno na imagem: CO × BB · two-tone flop · any turn): Second Barrel Field 54.2% e GTO 57.2% (range 50.8–63.5); Turn Delayed CBet Field 51.7% e GTO 44.1% (range 37.8–50.3), gap em âmbar só no segundo |
| Carrossel 4 | 1080x1350 | EN | Preflop: GTO and deviation | CO RFI at 40bb: the field opens less than GTO. | Captura da grade com a célula do RFI do CO destacada: na tela, Field 32%, GTO 37%, −5 (arredondado; a fonte tem 31,6 / 37,0 / −5,4) |
| Carrossel 5 | 1080x1350 | EN | GTO Mode is included in Individual | For a limited time. | O "US$ 29/month" gigante no centro, em âmbar, sobre o fundo da marca. Sem cadeado, sem selo de oferta, sem "de/por". "Limited time" uma vez só na arte |
| Carrossel 6 (CTA) | 1080x1350 | EN | Get GTO Mode | Link in bio. | Logo e fundo da marca |

Contagem de palavras (regra do Rafael): títulos de 3 a 7 palavras; apoios de 3 a 10 palavras (capa: 7; slide 2: 7 mais símbolos; slide 3: 8; slide 4: 10; slide 5: 4 mais o número gigante (título de 5 palavras); slide 6: 3).

Notas de arte:
- **Cores:** fold em teal `#015A6B`; a distância entre a barra do field e a do GTO em âmbar (o gap). Faixa GTO sombreada em volta da barra do GTO. No slide 3, as barras são de aposta (frequência de bet), não de fold: usar a cor semântica do raise (`#AD2C34`) para a aposta, mantendo o gap em âmbar e a faixa sombreada. No Second Barrel o field está dentro da faixa: sem gap.
- **Capa (slide 1 e story PT):** é o gancho. Título grande; o apoio diz o plano com o preço e "por tempo limitado", em âmbar. Sem data. O preço é o do Individual, não uma oferta: a arte não usa "de/por", risco, percentual nem outro sinal de desconto. Nenhuma arte leva selo de oferta ou de desconto; a capa EN leva a pílula LIVE e a do story PT a pílula NO AR, que só marcam o lançamento. "Limited time" / "por tempo limitado" aparece UMA vez por arte.
- **Slide 3:** barras renderizadas pela build, ou a captura `35d7005` só se mostrar exatamente esses valores (ver "Origem das capturas"). Não mostrar estado de carregamento nem aviso de "sem GTO". Sem contagem de mãos. Os números 54.2/57.2 e 51.7/44.1 e as duas faixas ficam nas barras; a faixa pequena, escrita.
- **Slide 4:** o stack da captura é 30–50bb (GTO a 40bb), torneio Regular. O número fica dentro da captura.
- **Slide 5:** título "GTO Mode is included in Individual", o "US$ 29/month" gigante e apoio "For a limited time." (sem data, sem "últimas horas", sem "preço travado", sem "quem assina agora mantém", sem preço futuro). A frase completa sobre o plano Individual e a conta grátis fica na legenda.
- **Slide 6:** "Get GTO Mode" + "Link in bio." Sem preço.
- **Story da capa PT:** o preço aparece em R$ (nunca US$); o gráfico leva o rótulo do spot "CO × BB · c-bet de 33% · exemplo" e a pílula NO AR. O sticker de link leva à landing com `utm_content=story-capa-pt`.
- **Enquete opcional no story (fora da arte):** "Qual spot você quer ver com o GTO ao lado?" com as opções "Flop" e "Turn/river" / "Which spot do you want to see with GTO next to it?" with "Flop" and "Turn/river".

## Strings para o agente das artes e do HTML (não editei `instagram/src`)
- **`build.py`:** `story-capa-pt` → título "Modo GTO<br><em>no ar</em>", apoio "Incluso no plano Individual (R$ 150/mês) por tempo limitado.", pílula NO AR, rótulo do gráfico "CO × BB · c-bet de 33% · exemplo" (no lugar do spot completo), sem segunda linha de apoio. `carrossel-en-01` → título "GTO Mode<br>is <em>live</em>", apoio "Included in Individual (US$ 29/month) for a limited time.", pílula LIVE, sem selo de oferta e sem micro-legenda. Slides 2 a 6 conforme a tabela acima; indicador "n / 6"; sem `carrossel-en-07`.
- **`numbers.json`:** novo bloco N11 para o Second Barrel (field 54.2; GTO centro 57.2, de 50.8, até 63.5; leitura: dentro da faixa, sem gap; fonte `numeros-verificados-lancamento.md`, 14/10); `N8`/`N9`/`N10` (Turn Delayed CBet: 51.7 / 44.1 / 37.8–50.3 / 1.4 acima do topo) seguem como estão. `textos_com_numero.c6_apoio_en` ("Part of the US$ 29/month plan, for a limited time.") sai; entram `c1_apoio_en` "Included in Individual (US$ 29/month) for a limited time.", `c1_apoio_pt` (story) "Incluso no plano Individual (R$ 150/mês) por tempo limitado.", `c1_rotulo_pt` (story) "CO × BB · c-bet de 33% · exemplo", `c3_apoio_en` "Second barrel: inside the range. Delayed c-bet: above.", `c4_apoio_en` "CO RFI at 40bb: the field opens less than GTO.", `c5_titulo_en` "GTO Mode is included in Individual", `c5_numero_en` "US$ 29/month" (o número gigante) e `c5_apoio_en` "For a limited time.". `email_under_pt` "O Modo GTO está incluso no plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF. Poker é jogo de habilidade e estudo. 18+." e `email_under_en` "GTO Mode is included in the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison. Poker is a game of skill and study. 18+." Preheaders do e-mail: PT "Incluso no plano Individual, por tempo limitado. O GTO no flop, turn e river, ao lado do field." EN "Included in the Individual plan, for a limited time. GTO on the flop, turn and river, next to the field."
- **`build_email.py`:** assunto e h1 PT "Modo GTO no ar" e EN "GTO Mode is live" (o HTML do e-mail já foi atualizado pelo outro agente; aqui fica o registro); preheader conforme `email.md`. O corpo do e-mail (`email_corpo_*`, `email_preflop_*`) não muda.
- **Aviso de moeda:** nenhuma string PT leva "US$" ou "R$ 29"; nenhuma string EN leva "R$".

## Legendas

### Legenda do feed
PT:
```
O GTO folda 38,8%. O field folda 46,0%. Mesmo spot.

O Modo GTO está no ar. Ao lado da frequência do field, o número GTO e a faixa GTO.

Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

Pós-flop: o GTO no flop, turn e river, inclusive as aberturas do agressor no turn e no river. Escolha o spot, clique em Apply e veja o field e o GTO juntos. A faixa de status do app guia cada clique até ter GTO.

Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

O Modo GTO está incluso no plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF.

Conhecer o Modo GTO, link na bio. Ferramenta de estudo. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```
EN:
```
GTO folds 38.8%. The field folds 46.0%. Same spot.

GTO Mode is live. Next to the field frequency, the GTO number and the GTO range.

Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Postflop: GTO on the flop, turn and river, including the aggressor's openings on the turn and river. Pick the spot, hit Apply and see the field and GTO together. The app's status bar guides you, click by click, until GTO is there.

Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

GTO Mode is included in the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison.

See GTO Mode, link in bio. Study tool. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

### Legenda do carrossel (só EN)
O carrossel é só em EN e a legenda também: não há legenda PT do carrossel nem mistura de moedas. A versão PT vive no feed PT (legenda acima) e no story da capa PT (sem legenda; se o Rafael quiser, usa a do feed PT).
```
GTO Mode is live. Included in the Individual plan.

See where the field breaks from GTO: next to the field frequency, the GTO number and the GTO range.

Postflop: GTO on the flop, turn and river. On the flop, the response to the c-bet and to the raise. On the turn and river, also the aggressor's betting frequency (second barrel, delayed c-bet, turn probe, third barrel). Pick the spot, hit Apply and see the field and GTO together. The app's status bar guides you, click by click, until GTO is there.

Response: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Opening: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, two-tone flop, any turn. On the turn, after the flop checks through, the CO bets (delayed c-bet): the field bets 51.7% and GTO bets 44.1% (range 37.8–50.3%): 1.4 pp above the top of the range. Here the field bets more than GTO does. In the same spot, the second barrel is inside the range: the field bets 54.2% and GTO 57.2% (range 50.8–63.5%). These are spots, not the field average.

Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb. CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years: the field opens 31.6% and GTO opens 37.0%.

Open a spot you play, look at the gap and pick what to study.

GTO Mode is included in the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison.

Get GTO Mode, link in bio. Save it for study. Study tool. 18+.

#poker #pokerMTT #pokerestudo #aurapoker
```

---

# (b) Landing

@aurapokeranalytics: a confirmar pelo Rafael. URL do CTA: ver a linha "Landing" da tabela "URLs por peça".

## Kicker (acima do título, com a pílula de novo)
- PT: No ar · Modo GTO
- EN: Live now · GTO Mode

## Título
- PT: O GTO e o field na mesma tela.
- EN: GTO and the field on the same screen.

## Subtítulo
- PT: Modo GTO: no flop, turn e river, o número GTO e a faixa GTO ao lado da frequência do field. Veja onde o field sai da faixa e estude esse spot.
- EN: GTO Mode: on the flop, turn and river, the GTO number and the GTO range next to the field frequency. See where the field leaves the range and study that spot.

## 3 bullets
PT:
- Pós-flop: GTO no flop, no turn e no river. No flop, a reação ao c-bet e ao raise. No turn e no river, também a frequência de aposta do agressor (second barrel, delayed c-bet, probe no turn, third barrel). Escolha o spot, clique em Apply e veja o field e o GTO juntos; a faixa de status do app guia cada clique até ter GTO.
- Pré-flop: a grade traz o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb. No RFI do CO a 30–50bb (GTO a 40bb), torneios Regular, últimos 2 anos, o field abre 31,6% e o GTO abre 37,0%.
- Exemplo: CO × BB em pote simples (SRP), 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado, contra o c-bet de 33%. O field folda 46,0% contra 38,8% do GTO (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

EN:
- Postflop: GTO on the flop, turn and river. On the flop, the response to the c-bet and to the raise. On the turn and river, also the aggressor's betting frequency (second barrel, delayed c-bet, turn probe, third barrel). Pick the spot, hit Apply and see the field and GTO together; the app's status bar guides you, click by click, until GTO is there.
- Preflop: the grid carries the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb. On the CO RFI at 30–50bb (GTO at 40bb), Regular tournaments, last 2 years, the field opens 31.6% and GTO opens 37.0%.
- Example: CO × BB single-raised pot (SRP), 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop, facing a 33% c-bet. The field folds 46.0% against GTO's 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

Nota de rodapé da seção (PT): "Um spot, não a média do field. Ferramenta de estudo · 18+. A Aura não é site de apostas e não oferece jogo."
Footnote (EN): "One spot, not the field average. Study tool · 18+. Aura is not a betting site and does not offer gambling."
(Sem números de escala no rodapé: a escala de 08/10 descrevia a cobertura antiga e não foi atualizada.)

CTA: PT "Conhecer o Modo GTO" / EN "See GTO Mode".
Frase sob o CTA, PT: "O Modo GTO está incluso no plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF." / EN: "GTO Mode is included in the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison."

## Alt text das imagens (2)
### Imagem 1: o exemplo lado a lado
- PT: "Duas barras de fold no mesmo spot do pós-flop: o field em 46,0% e o GTO em 38,8%, com a faixa GTO de 37,1 a 40,4% em volta da barra do GTO e a diferença em destaque."
- EN: "Two fold bars for the same postflop spot: the field at 46.0% and GTO at 38.8%, with the 37.1–40.4% GTO range around the GTO bar and the gap highlighted."
### Imagem 2: a grade do pré-flop
- PT: "Grade de mãos do Preflop Analysis em que as células cobertas mostram o GTO e o desvio do field, com a célula do RFI do CO em destaque."
- EN: "Preflop Analysis hand grid where the covered cells show the GTO and the field deviation, with the CO RFI cell highlighted."

Nota para o designer: as imagens só mostram os números de "Números usados". Não mostrar preço nas imagens (o preço fica só na frase do plano, sob o CTA). Não mostrar estado de carregamento nem aviso de "sem GTO".

---

# (c) Discord

Texto completo, com URLs, em `discord.md` (mesma pasta). PT e EN, abaixo de 1.200 caracteres cada, com o título "Modo GTO no ar" / "GTO Mode is live" e a inclusão por tempo limitado em negrito. Tamanho real e emojis: ver `discord.md`. **Só postar depois do teste logado, do P-61 no ar e do GATE B1.**

---

# (d) E-mail

Texto, assuntos (um deles anuncia "Modo GTO no ar" / "GTO Mode is live"), preheader com "incluso no plano Individual, por tempo limitado" e notas técnicas em `email.md`. Corpo curto, um exemplo (CO × BB) e a comparação field × GTO dele. Botão "Conhecer o Modo GTO" / "See GTO Mode"; frase do plano sob o botão. A imagem do e-mail (`email/modo-gto-pt.png` e `-en.png`) tem os mesmos números do exemplo (46,0% e 38,8%, faixa 37,1–40,4%).

---

## Números usados

| Número no texto | Valor | Fonte | Onde aparece |
|---|---|---|---|
| Preço do plano Individual (o temporário é a inclusão do GTO, não o preço) | US$ 29/mês no checkout EN (EN "US$ 29/month"); R$ 150/mês no checkout PT | `aura-landing` `pricing.ts` e `aura-novofront` `billingPlans.ts` (HUB); Rafael via HUB, 13 e 15/10. **Pendente: o Rafael confere no Stripe; regra no GATE B1** | Capa e slide 5 do carrossel (EN), story da capa PT (R$), legendas, Discord, landing, e-mail. Moeda nunca trocada |
| "Por tempo limitado" / "for a limited time" | sem data de fim | Rafael ("sim leva"), 15/10; sem data por decisão | Capa e slide 5 do carrossel, story da capa PT, legendas, Discord, landing, e-mail |
| N11: Second Barrel no recorte largo (28 classes de board) | field 54,2% (EN 54.2%) · GTO 57,2% (EN 57.2%) · faixa 50,8–63,5% (EN 50.8–63.5%) · dentro da faixa (sem gap) | `numeros-verificados-lancamento.md` (14/10), seção N7 a N10 ("Outras ações no mesmo recorte") | Slide 3 (barras, sem contagem de mãos); legenda do carrossel. Uso como contraste, não como exemplo principal |
| Diferença do exemplo (a) dentro da imagem EN do e-mail | "Overfold +5.6 pp" (a tela mostra a distância ao topo da faixa) | Exemplo (a), 08/10, confirmado em 14/10 | Imagem EN do e-mail; o texto do e-mail não cita a diferença |
| Spot do exemplo CO × BB | CO × BB · SRP · 30–60bb (GTO a 40bb) · Regular · flop K-high, two-tone, sem par, desconectado · c-bet de 33% | Exemplo (a), 08/10 | Apoio do feed; legendas, Discord, landing, e-mail |
| Field folda | 46,0% (EN 46.0%) | Exemplo (a), `potPercentage` do `actionSize` 2 | Barras (feed, stories, story da capa PT, carrossel 2); legendas, Discord, landing, e-mail |
| GTO folda e faixa | 38,8% (38,78 na API); faixa 37,1–40,4% (37,13–40,43) | Exemplo (a), `gtoFold` e `gtoBand.fold` | Barras com a faixa como sombreado; legendas, Discord, landing, e-mail |
| Diferença | +5,6 pp (acima do topo da faixa, como a tela mostra; 7,2 é contra o centro) | Exemplo (a) | Só texto: legendas, Discord, landing (o e-mail não a cita) |
| Pré-flop | RFI do CO, Regular, 30–50bb (GTO a 40bb): field abre 31,6%, GTO abre 37,0%, −5,4 pp | Exemplo (b) | Captura do slide 4; legenda do carrossel e landing (bullet 2). O −5,4 pp não é citado no texto |
| Ação da abertura | Turn Delayed CBet (o CO aposta o turn depois do flop passado) | `numeros-verificados-lancamento.md` (14/10) | Slide 3 (barra); legenda do carrossel |
| Spot da abertura e do Second Barrel | CO × BB · 30–60bb (GTO a 40bb) · SRP · flop two-tone · turn qualquer · Regular · últimos 2 anos (rótulo da arte: "CO × BB · two-tone flop · any turn") | idem | Slide 3 (rótulo); legenda do carrossel |
| Field aposta | 51,7% (EN 51.7%) | idem | Slide 3 (barra); legenda do carrossel |
| GTO aposta e faixa | 44,1%, faixa 37,8–50,3% (EN 44.1%, 37.8–50.3%) | idem | Slide 3 (barra e faixa); legenda do carrossel |
| Diferença da abertura | 1,4 pp acima do topo da faixa (EN 1.4 pp above the top of the range) | idem | Slide 3 (gap desenhado, sem número na arte); legenda do carrossel |
| Cobertura | Texto da seção "Decisões registradas" | idem | Legendas, landing, Discord, e-mail, slide 3 |

Não usados, por instrução da fonte e da HUB: a contagem de mãos do exemplo de abertura (80 mil), as 197 mil do Second Barrel, as 10.216 mãos e as 23,8 milhões de oportunidades; contagens de linhas e a escala de 08/10 (30 situações, 2.330 flops, 6.980.568 nós, 225 decisões); o Probe (faixa larga) como exemplo; o candidato SB × BB 3-bet (amostra pequena); RFI do BTN a 40bb (51%), disponível para peças de sustentação.
