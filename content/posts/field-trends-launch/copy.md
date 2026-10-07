# Field Trends: copy de lançamento

Status: rascunho para aprovação do Rafael. Não publicado, sem commit.
@aurapokeranalytics: a confirmar pelo Rafael. URLs com UTM prontas na tabela abaixo.
Fonte única dos números: `aura-main/_ops/field-trends-launch/numeros-verificados.md` (versão de 07/10, que apareceu durante a escrita e substituiu os marcadores `XX` do primeiro rascunho). Cada número usado está mapeado no bloco "Números usados" no fim. **Nenhum `XX` restou no pacote.**
Peças deste pacote: Discord (também em `discord.md`), Instagram (feed, story, carrossel), landing e e-mail (em `email.md`, `email-pt.html`, `email-en.html` e os `*.preview.html`).

## Pendências de produto (conferir antes de aprovar)
1. **Filtros.** O briefing cita filtros por buy-in, stack e posição. O STATE do produto de 06/10 lista posição como fora dos filtros desta versão do Field Trends (entram buy-in, stack, etapa, perfil, Regular/KO). Por isso o texto diz só **"buy-in e stack"**. Se posição entrou, trocar nas linhas: Discord PT/EN ("Filtros por buy-in e stack"), carrossel slide 5, landing bullet 3 e e-mail (frase sob o botão).
2. **O que o plano Grátis vê (B2).** Pelo STATE e pelo roteiro de release (§6), o Grátis só vê um teaser (IP Flop CBet com buy-in até US$ 22), e qualquer filtro abre o paywall. Os cards "o que mudou", Regs e fish, filtros e a lista completa são dos planos pagos. O botão pedido pelo Rafael segue "Acesse grátis" / "Get free access", e perto dele (Discord, legendas do feed e do carrossel, landing, e-mail) está a frase: PT "A conta grátis abre uma prévia do Field Trends; as variações significativas, os filtros e a lista completa de stats são dos planos pagos." / EN "The free account opens a Field Trends preview; the significant changes, filters and the full stat list are on paid plans." Nenhuma peça promete ao Grátis o painel de mudanças do field. Se o Rafael decidir abrir mais coisa no Grátis, ajustar essas frases. Slide 6 e story já seguem essa leitura: o slide 6 diz "abra o Field Trends" e o story diz "Veja uma stat de graça.".
3. **Só publicar depois do smoke logado do Rafael (estado real em 07/10, conforme `aura-main/_ops/field-trends-launch/roteiro-release.md` §8).** O roteiro registra como **já executados em 07/10**: promote do banco na Azure (`--verify` ok, GRANT ao papel read-only), publish da API (`deploy-4d370aa.zip`, app setting `FieldTrends__ExcludedQuarters__0=20251`), smoke anônimo (401 nas 4 rotas do Field Trends e nas demais conferidas) e a flag do front (#86 mesclado, `792e1b8`, bundle `index-BdNKbc3s.js` com `isFieldTrendsEnabled` verdadeiro). **Falta o smoke logado com conta paga, que o roteiro deixa com o Rafael** (o smoke com conta Grátis, previsto no §6, não consta como executado no §8). Nenhuma peça deste pacote deve sair antes desse smoke. Datas e ordem são do Rafael.
4. **2T26 em curso.** A fonte exige citar sempre "até o 2T26 (em curso)". Todo número com 2T26 leva a marca no texto. Se a publicação cair depois do fechamento do trimestre e os números forem relidos, reescrever sem "em curso".
5. **Os números do exemplo são do field inteiro, não de um spot.** Fold to IP Flop CBet (43,62% para 44,99%) é a média do field no flop, todas as posições. Por isso o exemplo diz "você dá c-bet IP no flop", sem BTN contra BB, sem textura de board e sem stack. Não acrescentar spot específico sem número do spot.
6. **`product-truth-aura.md`** não existe neste worktree nem no `aura-context`. Li `AGENTS.md`, `brand-kit.md`, o plano de marketing, os números verificados e o roteiro de release. Se o arquivo existir em outro lugar, vale uma conferência rápida das frases de produto.
7. **Stats citadas.** c-bet, fold to c-bet, donk e probe aparecem na fonte (IP Flop CBet, Fold to IP Flop CBet, Fold to OOP Flop Donk Bet, OOP Probe Bet), então a lista do briefing está coberta.

## Regra de leitura do exemplo (A1)
O exemplo é do field inteiro, não de um spot: nenhuma peça afirma que o exploit continua valendo nem que o c-bet de bluff ganha fold equity sem o qualificador "em média, no field inteiro" e o convite "confira no seu spot". Frase longa (legendas, Discord, landing, e-mail): PT "No field inteiro, o fold to c-bet IP subiu 1,36 pp, então em média o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot." / EN "Across the whole field, the IP fold to c-bet rose 1.36 pp, so on average the IP bluff c-bet has a little more fold equity. Check it in your own spot." Versão curta (slide 5): PT "Em média, o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot." / EN "On average, the IP bluff c-bet has a little more fold equity. Check it in your own spot."
Regra do 2T26 (A4): todo número do 2T26 em texto leva "(2T26 em curso)" / "(2Q26 in progress)", inclusive o 41,84% do call e a soma de 75,7 milhões de mãos.

## URLs por peça
Regra: Discord leva ao app (`https://www.aura.poker/`); Instagram e e-mail levam à landing (`https://www.aurapoker.com/`). Parâmetros: `utm_source=<fonte>&utm_medium=<meio>&utm_campaign=field-trends-launch&utm_content=<peça>`.

| Peça | Destino | utm_source | utm_content | URL |
|---|---|---|---|---|
| Discord PT | app | discord | discord-pt | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-trends-launch&utm_content=discord-pt |
| Discord EN | app | discord | discord-en | https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-trends-launch&utm_content=discord-en |
| Feed (link na bio) | landing | instagram | feed | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-trends-launch&utm_content=feed |
| Story (sticker de link) | landing | instagram | story | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-trends-launch&utm_content=story |
| Carrossel (link na bio) | landing | instagram | carrossel | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-trends-launch&utm_content=carrossel |
| Landing (botão de CTA, para o cadastro no app) | app | landing | (sem utm_content; utm_medium=website) | https://www.aura.poker/Login?tab=signup&utm_source=landing&utm_medium=website&utm_campaign=field-trends-launch |
| E-mail PT | landing | email | pt | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=field-trends-launch&utm_content=pt |
| E-mail EN | landing | email | en | https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=field-trends-launch&utm_content=en |

Observação: para o botão da landing mantive `utm_source=landing`, como no Field Ranges. Ajustar se o Rafael preferir outro valor.

## Rodapé padrão (um só)
- PT: "Dados: Aura · 11 trimestres, até o 2T26 (em curso) · 18+"
- EN: "Data: Aura · 11 quarters, through 2Q26 (in progress) · 18+"

Regra: o rodapé usa só o número de trimestres. O 75,7 milhões de mãos é do c-bet IP no flop, não do módulo inteiro, então só aparece colado a esse stat ("só o c-bet IP no flop soma 75,7 milhões de mãos") e nunca como base do módulo. Nenhuma arte atribui esse número a outra stat.

---

# (a) Instagram

## Legenda do feed (1080x1350)

Texto na arte (PT), idêntico ao `instagram/feed-pt.png` (fonte: `instagram/src/build.py`):
- Selo (pílula âmbar) + kicker: NOVO MÓDULO · FIELD TRENDS
- Título: O FIELD MUDOU. O SEU EXPLOIT AINDA VALE?
- Spot, uma vez só: Field contra c-bet IP no flop
- Stat: Fold to c-bet IP: 43,62% → 44,99%
- Período, pequeno: 2T25 → 2T26 (em curso)
- Diagrama da faixa, só com os rótulos: +1,36 pp e ± 0,77 pp
- CTA (âmbar): Já na Aura · conta grátis, link na bio
- Rodapé: @aurapokeranalytics · Dados: Aura · 11 trimestres, até o 2T26 (em curso) · 18+

Texto na arte (EN), idêntico ao `instagram/feed-en.png`:
- Seal (amber pill) + kicker: NEW MODULE · FIELD TRENDS
- Title: THE FIELD CHANGED. DOES YOUR EXPLOIT STILL HOLD?
- Spot, once: Field vs IP flop c-bet
- Stat: Fold to c-bet IP: 43.62% → 44.99%
- Period, small: 2Q25 → 2Q26 (in progress)
- Band diagram, labels only: +1.36 pp and ± 0.77 pp
- CTA (amber): Now on Aura · free account, link in bio
- Footer: @aurapokeranalytics · Data: Aura · 11 quarters, through 2Q26 (in progress) · 18+

Nota de arte: selo "NOVO MÓDULO" / "NEW MODULE" (nunca "Beta"). A leitura do exemplo (variação acima da faixa, "mudança real, e pequena", fold equity) fica só na legenda, não na arte. Números: 43,62%, 44,99%, +1,36, ± 0,77 (seção 4 da fonte).

Legenda PT:
```
Novo módulo na Aura: Field Trends.

O field mudou. O seu exploit ainda vale?

São 114 stats do pós-flop, trimestre a trimestre, e o Field Trends destaca só as mudanças significativas do último ano: 23 das 114. Cada stat traz a faixa de variação normal do próprio field, então você separa o que mudou de verdade do que é oscilação.

Exemplo: o fold to c-bet IP no flop foi de 43,62% (2T25) para 44,99% (2T26 em curso), acima da faixa de variação normal da stat (± 0,77 pp). A mudança é real, e pequena. No mesmo período, o call do field caiu de 42,99% para 41,84% (2T26 em curso).

No field inteiro, o fold to c-bet IP subiu 1,36 pp, então em média o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot.

Acesse grátis, link na bio. A conta grátis abre uma prévia do Field Trends; as variações significativas, os filtros e a lista completa de stats são dos planos pagos.

Dados: Aura, 11 trimestres, até o 2T26 (em curso). 18+.

#poker #pokerMTT #pokerestudo #pokerstrategy #aurapoker
```

Legenda EN:
```
New module on Aura: Field Trends.

The field changed. Does your exploit still hold?

That is 114 postflop stats, quarter by quarter, and Field Trends highlights only the significant changes of the past year: 23 of the 114. Each stat carries the normal variation band of its own field, so you can tell what really changed from what is just drift.

Example: the IP flop fold to c-bet went from 43.62% (2Q25) to 44.99% (2Q26 in progress), above the stat's normal variation band (± 0.77 pp). The change is real, and small. Over the same period, the field's call dropped from 42.99% to 41.84% (2Q26 in progress).

Across the whole field, the IP fold to c-bet rose 1.36 pp, so on average the IP bluff c-bet has a little more fold equity. Check it in your own spot.

Get free access, link in bio. The free account opens a Field Trends preview; the significant changes, filters and the full stat list are on paid plans.

Data: Aura, 11 quarters, through 2Q26 (in progress). 18+.

#poker #MTT #pokerstrategy #pokerstudy #aurapoker
```

## Story (1080x1920)

Nota ao designer (Instagram e landing): sem selo de fase nem convite a feedback; o kicker é só "FIELD TRENDS".

Texto na arte (PT), idêntico ao `instagram/story-pt.png` (fonte: `instagram/src/build.py`):
- Topo: logo; pílula NOVO MÓDULO + FIELD TRENDS
- Centro: "Fold to c-bet IP no flop:" / 43,62% → 44,99% / "Mudança real ou variação normal?" / "(2T25 → 2T26, em curso)"
- Diagrama da faixa, só com os rótulos: +1,36 pp e ± 0,77 pp
- Base: "Veja uma stat de graça." / botão "Conta grátis" / rodapé "Dados: Aura · 11 trimestres, até o 2T26 (em curso) · 18+" / selo 18+

Texto na arte (EN), idêntico ao `instagram/story-en.png`:
- Top: logo; NEW MODULE pill + FIELD TRENDS
- Center: "IP flop fold to c-bet:" / 43.62% → 44.99% / "Real change or normal variation?" / "(2Q25 → 2Q26, in progress)"
- Band diagram, labels only: +1.36 pp and ± 0.77 pp
- Bottom: "See one stat for free." / button "Free account" / footer "Data: Aura · 11 quarters, through 2Q26 (in progress) · 18+" / 18+ badge

Nota de arte: a arte não traz frase de veredito, só a pergunta. O Grátis só abre uma prévia, por isso o convite é "uma stat de graça". Nenhum número novo.

Instrução ao designer (fora do texto da arte): o botão de CTA é o sticker de link do Instagram, com o texto "Conta grátis" / "Free account". Sticker de enquete opcional: "O seu c-bet IP ainda vale?" / "Does your IP c-bet still hold?" com opções "Confiro a stat" / "Vou revisar" e "I will check the stat" / "I will review it".

## Carrossel (6 slides, 1080x1350)

Texto idêntico ao das artes finais (`instagram/carrossel-*.png`; fonte: `instagram/src/build.py`). Títulos em caixa alta, corpo em sentence case. Rodapé padrão em todos os slides (@aurapokeranalytics · "Dados: Aura · 11 trimestres, até o 2T26 (em curso) · 18+" / "Data: Aura · 11 quarters, through 2Q26 (in progress) · 18+", selo 18+) e indicador "n / 6" no topo. Os cards dos slides 1, 3, 4 e 5 são capturas do app (imagem), não texto de arte.

### Slide 1: gancho
- PT: pílula NOVO MÓDULO + FIELD TRENDS / título "O FIELD MUDOU. E O SEU EXPLOIT?" / sub "Acompanhe o field, trimestre a trimestre." / 2 cards do app / legenda "Variação em 1 ano (2T26 em curso)"
- EN: NEW MODULE pill + FIELD TRENDS / title "THE FIELD CHANGED. WHAT ABOUT YOUR EXPLOIT?" / sub "Follow the field, quarter by quarter." / 2 app cards / caption "Change over 1 year (2Q26 in progress)"
- Número: nenhum no corpo (só o rodapé).

### Slide 2: stat por stat
- PT: título "STAT POR STAT" / corpo "114 stats do pós-flop: c-bet, fold to c-bet, donk, probe e mais, trimestre a trimestre." / destaque "Só o c-bet IP no flop soma 75,7 milhões de mãos (a soma inclui o 2T26, em curso)."
- EN: title "STAT BY STAT" / body "114 postflop stats: c-bet, fold to c-bet, donk, probe and more, quarter by quarter." / highlight "The IP flop c-bet alone adds up to 75.7 million hands (the sum includes 2Q26, in progress)."
- Arte: linha do tempo trimestral de uma stat, na paleta do app. Números: 114 (seção 3), 75,7 milhões (seção 1).

### Slide 3: só o que mudou
- PT: título "SÓ O QUE MUDOU DE VERDADE" / 5 cards do app / legenda "Variação em 1 ano (2T26 em curso)" / corpo "No último ano, 23 das 114 stats tiveram variação significativa." / destaque "Menos stat para olhar, mais tempo de estudo."
- EN: title "ONLY WHAT REALLY CHANGED" / 5 app cards / caption "Change over 1 year (2Q26 in progress)" / body "Over the past year, 23 of the 114 stats had a significant change." / highlight "Fewer stats to scan, more time to study."
- Números: 23 e 114 (seções 6 e 3).

### Slide 4: a faixa de variação normal
- PT: título "REAL OU VARIAÇÃO NORMAL?" / corpo "Cada stat traz a faixa de variação normal do próprio field. Dentro da faixa, é oscilação. Fora, o field mudou." / destaque "Fold to c-bet IP: +1,36 pp. Faixa: ± 0,77 pp. Mudança real." / período "2T25 → 2T26 (em curso)" / legenda do gráfico "Gráfico: C-bet no flop (IP) %, com a sua faixa de variação normal"
- EN: title "REAL OR NORMAL VARIATION?" / body "Every stat carries the normal variation band of its own field. Inside the band, it is drift. Outside, the field changed." / highlight "IP fold to c-bet: +1.36 pp. Band: ± 0.77 pp. A real change." / period "2Q25 → 2Q26 (in progress)" / chart caption "Chart: IP flop c-bet %, with its normal variation band"
- Arte: gráfico do **C-bet no flop (IP) %** com a faixa de variação normal sombreada, só para ilustrar a faixa (não é a série do Fold, e nenhum número do destaque é lido no gráfico). A legenda curta fica sob o gráfico. O destaque (Fold to c-bet IP: +1,36 pp, faixa ± 0,77) fica colado ao card real do Fold to IP Flop CBet (o mesmo do slide 5), com "2T25 → 2T26 (em curso)". No e-mail, a mesma legenda vai sob o gráfico. Números: 43,62%, 44,99%, +1,36, ± 0,77 (seção 4); nenhum número novo.

### Slide 5: o que fazer com isso
- PT: título "O QUE FAZER COM ISSO" / 2 cards do app / legenda dos cards "Variação em 1 ano (2T26 em curso)" / corpo "O fold to c-bet IP foi de 43,62% para 44,99% (2T26 em curso), e o call caiu de 42,99% para 41,84% (2T26 em curso). O field folda um pouco mais e paga um pouco menos." / destaque "Em média, o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot."
- EN: title "WHAT TO DO WITH IT" / 2 app cards / card caption "Change over 1 year (2Q26 in progress)" / body "IP fold to c-bet went from 43.62% to 44.99% (2Q26 in progress), and the call dropped from 42.99% to 41.84% (2Q26 in progress). The field folds a little more and calls a little less." / highlight "On average, the IP bluff c-bet has a little more fold equity. Check it in your own spot."
- Microtexto: "Filtre por buy-in e stack (planos pagos) e confira no field do seu jogo." / "Filter by buy-in and stack (paid plans) and check the field you actually play."
- Números: 43,62%, 44,99%, 42,99%, 41,84% (seções 4 e 5).

### Slide 6: CTA
- PT: pílula NOVO MÓDULO + FIELD TRENDS / título "ABRA O FIELD TRENDS" / corpo "Crie sua conta grátis e abra o Field Trends." / botão "Link na bio" / "18+"
- EN: NEW MODULE pill + FIELD TRENDS / title "OPEN FIELD TRENDS" / body "Create your free account and open Field Trends." / button "Link in bio" / "18+"
- Número: nenhum no corpo.

**Nota de arte do carrossel, slides 1 e 6.** Pílula âmbar "NOVO MÓDULO" / "NEW MODULE" + FIELD TRENDS acima do título nos slides 1 e 6 (nunca "Beta"). Os slides 2 a 5 levam só o kicker FIELD TRENDS. Nenhum número novo.

### Legenda do carrossel
PT:
```
Novo módulo na Aura: Field Trends.

O field mudou. O seu exploit ainda vale?

O Field Trends mostra 114 stats do pós-flop trimestre a trimestre e destaca só as mudanças significativas do último ano: 23 das 114. Cada stat traz a faixa de variação normal do próprio field. Dentro dela é oscilação, fora dela o field mudou.

Exemplo: o fold to c-bet IP no flop foi de 43,62% (2T25) para 44,99% (2T26 em curso), fora da faixa de ± 0,77 pp, e o call caiu de 42,99% para 41,84% (2T26 em curso). Mudança real, e pequena. No field inteiro, o fold to c-bet IP subiu 1,36 pp, então em média o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot.

Filtros por buy-in e stack nos planos pagos. Salve para estudar.

Acesse grátis, link na bio. A conta grátis abre uma prévia do Field Trends; as variações significativas, os filtros e a lista completa de stats são dos planos pagos.

Dados: Aura, 11 trimestres, até o 2T26 (em curso). 18+.

#poker #pokerMTT #pokerestudo #pokerstrategy #aurapoker
```
EN:
```
New module on Aura: Field Trends.

The field changed. Does your exploit still hold?

Field Trends shows 114 postflop stats quarter by quarter and highlights only the significant changes of the past year: 23 of the 114. Each stat carries the normal variation band of its own field. Inside it, drift; outside it, the field changed.

Example: the IP flop fold to c-bet went from 43.62% (2Q25) to 44.99% (2Q26 in progress), outside the ± 0.77 pp band, and the call dropped from 42.99% to 41.84% (2Q26 in progress). A real change, and a small one. Across the whole field, the IP fold to c-bet rose 1.36 pp, so on average the IP bluff c-bet has a little more fold equity. Check it in your own spot.

Buy-in and stack filters on paid plans. Save it for study.

Get free access, link in bio. The free account opens a Field Trends preview; the significant changes, filters and the full stat list are on paid plans.

Data: Aura, 11 quarters, through 2Q26 (in progress). 18+.

#poker #MTT #pokerstrategy #pokerstudy #aurapoker
```

---

# (b) Landing

@aurapokeranalytics: a confirmar pelo Rafael. URL do CTA: ver a linha "Landing" da tabela "URLs por peça" no topo.

## Anúncio (kicker acima do título, com a pílula de novo módulo)
- PT: Novo módulo na Aura: Field Trends
- EN: New module on Aura: Field Trends

## Título
- PT: O field mudou. O seu exploit ainda vale?
- EN: The field changed. Does your exploit still hold?

## Subtítulo
- PT: Field Trends: 114 stats do field de MTT no pós-flop, trimestre a trimestre, com as mudanças significativas do último ano em destaque e a faixa de variação normal de cada stat para você separar mudança real de oscilação.
- EN: Field Trends: 114 MTT field stats on the postflop, quarter by quarter, with the significant changes of the past year highlighted and each stat's normal variation band, so you can tell a real change from drift.

## 3 bullets
PT:
- Stat por stat: 30 ações e 84 reações (c-bet, fold to c-bet, donk, probe e mais), em 11 trimestres. Só o c-bet IP no flop soma 75,7 milhões de mãos (a soma inclui o 2T26, em curso).
- Real ou variação normal: no último ano, 23 das 114 stats tiveram variação significativa. Exemplo: o fold to c-bet IP foi de 43,62% (2T25) para 44,99% (2T26 em curso), acima da faixa de ± 0,77 pp. Mudança real, e pequena. No field inteiro, o fold to c-bet IP subiu 1,36 pp, então em média o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot.
- Confira onde você joga: filtros por buy-in e stack (planos pagos).

EN:
- Stat by stat: 30 actions and 84 reactions (c-bet, fold to c-bet, donk, probe and more), over 11 quarters. The IP flop c-bet alone adds up to 75.7 million hands (the sum includes 2Q26, in progress).
- Real or normal variation: over the past year, 23 of the 114 stats had a significant change. Example: the IP fold to c-bet went from 43.62% (2Q25) to 44.99% (2Q26 in progress), above the ± 0.77 pp band. A real change, and a small one. Across the whole field, the IP fold to c-bet rose 1.36 pp, so on average the IP bluff c-bet has a little more fold equity. Check it in your own spot.
- Check where you play: buy-in and stack filters (paid plans).

Nota de rodapé da seção (PT): "Field inteiro, 2T25 a 2T26 (o 2T26 está em curso). Cada stat tem a sua própria faixa de variação normal. Filtros e lista completa de stats nos planos pagos. Dados: Aura, 11 trimestres."
Footnote (EN): "Whole field, 2Q25 to 2Q26 (2Q26 is in progress). Each stat has its own normal variation band. Filters and the full stat list on paid plans. Data: Aura, 11 quarters."
Frase sob o CTA (B2), PT: "A conta grátis abre uma prévia do Field Trends; as variações significativas, os filtros e a lista completa de stats são dos planos pagos." / EN: "The free account opens a Field Trends preview; the significant changes, filters and the full stat list are on paid plans." A nota de rodapé acima já repete a ideia ("Filtros e lista completa de stats nos planos pagos"); manter as duas.
CTA: PT "Criar conta grátis" / EN "Create free account". (Botão não alterado nesta rodada; se o Rafael quiser o mesmo "Acesse grátis" / "Get free access" do e-mail, trocar aqui.)
Números usados na landing: 114, 30, 84 (seção 3), 11 e 75,7 milhões (seções 1 e 2), 23 (seção 6), 43,62%, 44,99%, +1,36, ± 0,77 (seção 4). Ficam só no texto, nunca atribuídos a uma imagem.

## Alt text das imagens (2)

### Imagem 1: o que mudou no field
- PT: "Painel do Field Trends com as stats do field que mudaram de forma significativa no último ano, cada uma com a variação trimestre a trimestre."
- EN: "Field Trends panel with the field stats that changed significantly over the past year, each showing its quarter-by-quarter movement."

### Imagem 2: uma stat com a faixa de variação normal
- PT: "Gráfico trimestral de uma stat do field com a faixa de variação normal em volta da linha, mostrando se a mudança sai da faixa."
- EN: "Quarterly chart of a field stat with the normal variation band around the line, showing whether the change leaves the band."

### Imagem 3 (filtros): FICA FORA
Não há mockup de filtros, então o alt text da imagem 3 foi removido. O bullet 3 ("filtros por buy-in e stack (planos pagos)") segue só como texto. Se um mockup de filtros existir no futuro, escrever o alt text na hora.

- Nota para o designer: as imagens não mostram percentuais além dos que estão em `numeros-verificados.md`. Não atribuir a nenhuma imagem os números do texto. Não mostrar número de pré-flop nem de filtro por buy-in (a fonte manda não citar).

---

# (c) Discord

Texto completo, com URLs, em `discord.md` (mesma pasta). PT e EN, abaixo de 1.200 caracteres cada (estimativa manual, cerca de 1.160 PT e 1.170 EN), 3 emojis funcionais (📈 título, 🔎 convite, 👉 CTA), abre com o anúncio de novo módulo, sem selo de fase e sem pedido de feedback. Mantida igual ao `discord.md`. **Só postar depois do smoke logado com conta paga:** banco, API e flag já foram executados em 07/10 pelo `roteiro-release.md`; falta o smoke logado do Rafael.

**PT**
```
📈 **Novo módulo na Aura: Field Trends**

O field mudou, e o seu exploit ainda vale? Das 114 stats do pós-flop, 23 tiveram variação significativa no último ano, trimestre a trimestre.

**Exemplo de spot**
Você dá c-bet IP no flop. O field folda 43,62% (2T25) e 44,99% (2T26 em curso), acima da faixa de variação normal (± 0,77 pp). Mudança real, e pequena. O call caiu de 42,99% para 41,84% (2T26 em curso).
No field inteiro, o fold to c-bet IP subiu 1,36 pp, então em média o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot.

**O que você vê**
- As mudanças significativas do último ano
- A faixa de variação normal de cada stat
- Filtros por buy-in e stack

**Base:** 75,7 mi de mãos só no c-bet IP no flop, em 11 trimestres (3T23 a 2T26, sem o 1T25). A soma inclui o 2T26, em curso.

🔎 Veja no Field Trends se o field mudou nas stats que você explora.

A conta grátis abre uma prévia do Field Trends; as variações significativas, os filtros e a lista completa de stats são dos planos pagos.
👉 Acesse grátis: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-trends-launch&utm_content=discord-pt
```

**EN**
```
📈 **New module on Aura: Field Trends**

The field changed, does your exploit still hold? Of the 114 postflop stats, 23 had a significant change over the past year, quarter by quarter.

**Example spot**
You c-bet IP on the flop. The field folds 43.62% (2Q25) and 44.99% (2Q26 in progress), above the normal variation band (± 0.77 pp). A real change, and a small one. The call dropped from 42.99% to 41.84% (2Q26 in progress).
Across the whole field, the IP fold to c-bet rose 1.36 pp, so on average the IP bluff c-bet has a little more fold equity. Check it in your own spot.

**What you see**
- The significant changes of the past year
- The normal variation band of every stat
- Buy-in and stack filters

**Data:** 75.7M hands on the IP flop c-bet alone, over 11 quarters (3Q23 to 2Q26, excluding 1Q25). The sum includes 2Q26, still in progress.

🔎 See in Field Trends whether the field changed in the stats you exploit.

The free account opens a Field Trends preview; the significant changes, filters and the full stat list are on paid plans.
👉 Get free access: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=field-trends-launch&utm_content=discord-en
```

---

# (d) E-mail

Texto, assuntos, preheader e notas técnicas em `email.md`. HTML em `email-pt.html` e `email-en.html`; abrir do disco pelos `email-pt.preview.html` e `email-en.preview.html`. Assunto recomendado: a 1 ("Novo módulo na Aura: Field Trends" / "New module on Aura: Field Trends"); a 2 ("O field mudou. O seu exploit ainda vale?" / "The field changed. Does your exploit still hold?") fica como alternativa. O corpo abre com o anúncio e só depois traz a pergunta. A frase sob o botão diz que a conta grátis abre uma prévia.

---

## Pendências de número

**Nenhuma.** O `numeros-verificados.md` chegou durante a escrita e todos os `XX` foram trocados por número com fonte. Não sobrou marcador. O que segue em aberto é de produto, não de número (ver "Pendências de produto" no topo): filtro de posição, o que o Grátis vê e a aba no ar antes de publicar.

## Números usados (todos de `numeros-verificados.md`, versão de 07/10)

| Número no texto | Seção da fonte | Onde aparece |
|---|---|---|
| 114 stats (30 ações e 84 reações) | §3 | Discord, feed (legenda), carrossel slides 2 e 3 e legenda, landing (subtítulo, bullets 1 e 2), e-mail |
| 23 das 114 com variação significativa em 1 ano | §6 | Discord, feed (legenda), carrossel slide 3 e legenda, landing bullet 2, e-mail |
| 75,7 milhões de mãos (c-bet IP no flop, 11 trimestres, 3T23 a 2T26, sem o 1T25; a soma inclui o 2T26 em curso, e o texto diz isso) | §1 e §2 | Discord (Base), carrossel slide 2, landing bullet 1 |
| 11 trimestres (3T23 a 2T26, em curso) | §2 | rodapé padrão (todas as artes), Discord, landing (nota), e-mail (linha "Dados") |
| Fold to IP Flop CBet 43,62% (2T25) para 44,99% (2T26), +1,36 pp, faixa ± 0,77 | §4 | Discord, feed (arte e legenda), story, carrossel slides 4 e 5 e legenda, landing bullet 2, e-mail |
| Call vs IP Flop CBet 42,99% para 41,84% | §5 | Discord, feed (legenda), carrossel slide 5 e legenda |

Não usados, por instrução da fonte: qualquer número de pré-flop, de filtro por buy-in e o 78,9% do Grátis. As outras mudanças reais da fonte (donk, probe, delayed c-bet) ficaram de fora para não pesar o texto; podem entrar em peças de sustentação.
