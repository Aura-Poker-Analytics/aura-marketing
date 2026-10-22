# Field Hotspots: copy de lançamento

Status: **não publicado**; rascunho para aprovação do Rafael. Versão de 22/10/2026. Branch `feature/launch-field-hotspots`, sem commit.
@aurapokeranalytics: a confirmar pelo Rafael.
Peças deste pacote: landing e artes (este arquivo), Discord (`discord.md`), Instagram (`instagram.md`) e e-mail (`email.md`).
Telas de referência: `aura-novofront/_ops/validacao-prints/169/paid-1280-3-field-hotspots.png` (com o Modo GTO, 8 spots) e `free-1280-3-field-hotspots.png` (Grátis, 1 spot e 7 trancados).

**Números:** todos vêm de `content/posts/field-hotspots-launch/numeros-verificados.md` (22/10/2026). Nenhum marcador `[NUM]` resta no pacote; cada número está mapeado à linha da fonte em "Números usados", no fim. PT com vírgula, EN com ponto; desvio em %, nunca "pp".

## Mensagem central
- PT: Os hotspots de desvio forte do field, discriminados e a um clique: onde ele se afasta do GTO, em qual size de c-bet, e o que fazer com isso.
- EN: The field's strong-deviation hotspots, itemized and one click away: where it strays from GTO, at which c-bet size, and what to do about it.

Estrutura de toda peça: **um spot concreto** (UTG vs BB, 25bb, SRP, flop A-high two-tone com OESD possível, Overdefend), **a ação** ("O BB defende demais contra c-bet. Blefe menos e aposte mais por value.", texto da própria caixa "Como explorar") e **um CTA**.

## Como a direção do Rafael foi aplicada (FOMO sem mentira)
Direção dele: "Tem que ter um apelo que damos os maiores hotspots do field discriminados e facilmente acessiveis. podemos usar fearmongering tambem pois se é muito privilegio ter essa informação.. gerar FOMO".
- **FOMO que é fato do produto:** a rotação semanal (toda segunda, 2 spots entram e 2 saem; o que sai não volta na mesma forma), o Grátis vê 1 dos 8, e os hotspots vêm do field real de MTT. "Facilmente acessíveis" = item próprio no menu do topo, com selo NEW.
- **Medo no tom de grinder, sempre com "pode":** "O reg do lado pode estar vendo." / "Quem não sabe onde o field erra pode estar deixando fichas na mesa." Nenhuma frase afirma que alguém usa a ferramenta.
- **Fora, por regra:** contador, "só X vagas", prazo inventado, afirmação de que outros jogadores usam a Aura, promessa de ganho, número sem fonte, "Pool vs GTO", a palavra "ponte" e texto de bastidor.
- **Cuidado com a data:** "a primeira troca é na segunda, 02/11" é a única data nas peças, e é fato do calendário.

## Pendências antes de publicar
1. **`numeros-verificados.md`: FECHADA (22/10).** Os `[NUM]` foram trocados pelos valores do arquivo. Se a sessão dona do módulo alterar o arquivo, refazer as peças.
2. **O exemplo é o "spot da semana" de 22/10.** Depois da troca de 02/11 ele pode sair da tela (a regra é que o spot que sai não volta na mesma forma). Publicar antes de 02/11, ou trocar o exemplo (spot, números e arte) pelo spot da semana vigente. Enquanto o exemplo estiver na tela, o texto diz "exemplo desta semana".
3. **FECHADA (22/10): "o que sai na segunda não volta igual" é fato.** Regra `pvg-release-v1` (`aura-main/_ops/pool-vs-gto-v1/exploit-2026-10-19.md:34`): sempre 8 liberados; toda segunda entram 2 e saem os 2 mais antigos; mesma janela para todos; o spot que sai some para todos. O calendário tem 688 spots, cada um uma vez. A frase aparece nos stories, Discord, e-mail, legendas e landing.
4. **Ordem de publicação:** só depois do merge e do "pode publicar" do Field Hotspots (aura-novofront#169, flag, item NEW no menu) e do olho logado do Rafael (com o Modo GTO vê 8 spots; no Grátis vê 1 e os outros 7 trancados).
5. **Discord leva à landing** (`aurapoker.com`), como pediu a tarefa. O Modo GTO levava o Discord ao app; se o Rafael preferir o app, é só trocar o destino da linha "Discord" da tabela.
6. **Rótulo Beta:** a tela não mostra Beta, só NEW, então nenhuma peça diz Beta. O Discord tem um convite de feedback sem a palavra. Se o Rafael quiser o selo Beta, entra só no Discord.
7. **Botão da landing:** a URL abre o cadastro no app como no Modo GTO. Se o Field Hotspots tiver rota própria, trocar para ela (mantendo os UTMs).
8. **Capturas de tela nas artes:** as telas de 22/10 mostram números (fold, GTO, diferença, mil mãos, faixa). Só entram na arte se o `numeros-verificados.md` os cobrir; senão usar o mockup renderizado com os valores confirmados, ou borrar.
9. **Preço e plano:** nenhuma peça cita preço. O trancado da tela diz "+7 spots liberados no Modo GTO", e as peças usam "Modo GTO" assim. Conferir se há texto do plano a acrescentar ("incluso no Individual") ou se isso fica fora.
10. **"Deixando fichas na mesa": decisão do Rafael.** A frase "Quem não sabe onde o field erra pode estar deixando fichas na mesa" (legendas do feed, PT e EN) é a direção de fearmongering que ele pediu. O brand-kit veta promessa de lucro; a frase não promete ganho (diz "pode estar deixando"), mas o revisor de marca deve saber que ela fica por decisão dele.
11. **Fechada (22/10, HUB): os 8 liberados não são os 8 maiores desvios** (posições 4, 7, 9, 16, 18, 20, 24 e 49 de 1.049, pela regra de liberação). Todas as peças trocaram "os maiores" / "mais se afasta" por "desvio forte" (5% ou mais fora da faixa do GTO).

## Regras de texto das artes (padrão Rafael, 08/10)
Cada arte tem **um título curto (até ~6 palavras) e no máximo uma linha de apoio (até ~10 palavras)**. A imagem fala. Em toda arte, só ficam o logo, `@aurapokeranalytics · 18+` pequeno e, nos slides, o indicador "n / 7". Título em caixa alta bold, apoio em sentence case. O link é o sticker ou o link na bio, não texto de arte. Cores semânticas: fold `#015A6B`, call `#348A5D`, raise `#AD2C34`; a diferença field × GTO em âmbar. Nenhuma arte mostra contagem de mãos nem preço.

## URLs por peça
Regra: Instagram, e-mail e Discord levam à landing (`https://www.aurapoker.com/`); o botão da landing leva ao cadastro no app. Parâmetros: `utm_source=<fonte>&utm_medium=<meio>&utm_campaign=field-hotspots-launch&utm_content=<peça>`.

| Peça | Idioma | Destino | utm_source | utm_content | URL |
|---|---|---|---|---|---|
| Discord PT | PT | landing | discord | discord-pt | https://www.aurapoker.com/?utm_source=discord&utm_medium=social&utm_campaign=field-hotspots-launch&utm_content=discord-pt |
| Discord EN | EN | landing | discord | discord-en | https://www.aurapoker.com/?utm_source=discord&utm_medium=social&utm_campaign=field-hotspots-launch&utm_content=discord-en |
| Feed PT (link na bio) | PT | landing | instagram | feed-pt | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-hotspots-launch&utm_content=feed-pt |
| Feed EN (link na bio) | EN | landing | instagram | feed-en | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-hotspots-launch&utm_content=feed-en |
| Story PT (sticker de link) | PT | landing | instagram | story-pt | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-hotspots-launch&utm_content=story-pt |
| Story EN (sticker de link) | EN | landing | instagram | story-en | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-hotspots-launch&utm_content=story-en |
| Story da capa PT (sticker de link) | PT | landing | instagram | story-capa-pt | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-hotspots-launch&utm_content=story-capa-pt |
| Carrossel EN (link na bio) | EN (arte) · legenda PT + EN | landing | instagram | carrossel-en | https://www.aurapoker.com/?utm_source=instagram&utm_medium=social&utm_campaign=field-hotspots-launch&utm_content=carrossel-en |
| Landing (botão de CTA, para o cadastro no app) | PT e EN | app | landing | field-hotspots (utm_medium=website) | https://www.aura.poker/Login?tab=signup&utm_source=landing&utm_medium=website&utm_campaign=field-hotspots-launch&utm_content=field-hotspots |
| E-mail PT | PT | landing | email | pt | https://www.aurapoker.com?utm_source=email&utm_medium=email&utm_campaign=field-hotspots-launch&utm_content=pt |
| E-mail EN | EN | landing | email | en | https://www.aurapoker.com?utm_source=email&utm_medium=email&utm_campaign=field-hotspots-launch&utm_content=en |

Observação: feed e story têm uma URL por idioma (no Modo GTO era uma só), para medir PT e EN separados. O `utm_source=landing` do botão segue o padrão do Modo GTO.

## Rodapé
- **Artes:** só `@aurapokeranalytics · 18+`, pequeno.
- **Legendas, landing e e-mail:** PT "Ferramenta de estudo. 18+." / EN "Study tool. 18+." (na landing, também "A Aura não é site de apostas e não oferece jogo.").

---

# (a) Landing

## Kicker (com a pílula de novo)
- PT: Novo · Field Hotspots
- EN: New · Field Hotspots

## Título
- PT: 8 spots de desvio forte do field, spot a spot.
- EN: 8 strong field deviations from GTO, spot by spot.

## Subtítulo
- PT: O Field Hotspots lista os spots pós-flop em que o field real de MTT tem desvio forte do GTO, já discriminados: posições, stack, flop, size de c-bet e a ação para explorar. Item próprio no menu do topo.
- EN: Field Hotspots lists the postflop spots where the real MTT field deviates strongly from GTO, already itemized: positions, stack, flop, c-bet size and the action to exploit it. Its own item in the top menu.

## 3 bullets
PT:
- **Cada spot, discriminado.** Par de posições, stack, tipo de pote e textura do flop com boards de exemplo. Rótulo Overfold (o field folda mais que o GTO) ou Overdefend (defende mais), com a frequência do field, a do GTO e a diferença. Exemplo desta semana: UTG vs BB, 25bb, SRP, flop A-high two-tone com OESD possível. Contra o c-bet de 50%, o BB folda 53,8% contra 73,5% do GTO, 19,7% abaixo: overdefend.
- **Como explorar, por size.** Abas Fold, Call e Raise com o detalhe de c-bet 33%, 50% e 65%, e uma caixa com a ação. Neste spot: o BB defende demais contra c-bet. Blefe menos e aposte mais por value.
- **Spots novos toda segunda.** O Modo GTO libera 8 spots; o Grátis vê 1, o spot da semana. Toda segunda, 2 spots entram e 2 saem, e o que sai não volta na mesma forma. A primeira troca é em 02/11. O reg do lado pode estar vendo a lista inteira.

EN:
- **Every spot, itemized.** Position pair, stack, pot type and flop texture with example boards. An Overfold (the field folds more than GTO) or Overdefend (defends more) label, with the field frequency, the GTO frequency and the gap. This week's example: UTG vs BB, 25bb, SRP, A-high two-tone flop with a possible OESD. Facing a 50% c-bet, the BB folds 53.8% vs 73.5% for GTO, 19.7% below: overdefend.
- **How to exploit it, by size.** Fold, Call and Raise tabs with the detail for 33%, 50% and 65% c-bets, and a box with the action. In this spot: the BB defends too much against the c-bet. Bluff less and bet more for value.
- **New spots every Monday.** GTO Mode unlocks 8 spots; Free sees 1, the spot of the week. Every Monday, 2 spots come in and 2 go out, and what goes out doesn't come back in the same form. The first swap is on Nov 2. The reg next to you might be looking at the whole list.

Nota de rodapé (PT): "Um spot, não a média do field. Ferramenta de estudo · 18+. A Aura não é site de apostas e não oferece jogo."
Footnote (EN): "One spot, not the field average. Study tool · 18+. Aura is not a betting site and does not offer gambling."

CTA: PT "Abrir o Field Hotspots" / EN "Open Field Hotspots".
Frase sob o CTA, PT: "O Grátis vê o spot da semana. O Modo GTO libera os outros 7." / EN: "Free sees the spot of the week. GTO Mode unlocks the other 7."

## Alt text das imagens (2)
### Imagem 1: o Field Hotspots com o Modo GTO
- PT: "Tela do Field Hotspots com o Modo GTO: à esquerda, a lista de 8 spots liberados, cada um com par de posições, stack, tipo de pote, textura do flop e rótulo Overfold ou Overdefend; à direita, o spot UTG vs BB a 25bb com três boards de exemplo, o fold do field contra o do GTO, as abas Fold, Call e Raise por size de c-bet e a caixa Como explorar."
- EN: "Field Hotspots screen with GTO Mode: on the left, the list of 8 unlocked spots, each with position pair, stack, pot type, flop texture and an Overfold or Overdefend label; on the right, the UTG vs BB 25bb spot with three example boards, the field fold against the GTO fold, the Fold, Call and Raise tabs by c-bet size and the How to exploit box."

### Imagem 2: o Field Hotspots no Grátis
- PT: "Tela do Field Hotspots no plano Grátis: o spot da semana liberado à esquerda, abaixo dele um cadeado com '+7 spots liberados no Modo GTO' e a data dos próximos spots, e o detalhe por size de c-bet desfocado."
- EN: "Field Hotspots screen on the Free plan: the spot of the week unlocked on the left, below it a lock with '+7 spots unlocked in GTO Mode' and the date of the next spots, and the c-bet size detail blurred."

Nota para o designer: as imagens só mostram números que estiverem em `numeros-verificados.md` (ver Pendência 8). Não mostrar preço, e-mail, conta ou nick. O alt text acima não cita números de propósito.

---

# (b) Textos das artes

Cada arte: **um título (até ~6 palavras) e uma linha de apoio (até ~10 palavras)**. Rótulos pequenos dentro do gráfico (par de posições, stack, flop) não contam como segunda linha de apoio.

| Arte | Formato | Idioma | Título | Apoio (uma linha) | O que a imagem mostra |
|---|---|---|---|---|---|
| Feed | 1080x1350 | PT | Você sabe onde o field erra? | Field Hotspots: spots novos toda segunda. | Barras de fold lado a lado, Field 53,8% e GTO 73,5% (c-bet de 50%), com a diferença em âmbar e o rótulo OVERDEFEND; rótulo pequeno "UTG vs BB · 25bb · A-high two-tone" |
| Feed | 1080x1350 | EN | Know where the field leaks? | Field Hotspots: new spots every Monday. | Mesmas barras (Field 53.8%, GTO 73.5%, 50% c-bet), gap em âmbar, rótulo OVERDEFEND; rótulo "UTG vs BB · 25bb · A-high two-tone" |
| Story | 1080x1920 | PT | O BB defende demais aqui | Field Hotspots: o que sai na segunda não volta igual. | As mesmas barras com a diferença 19,7% abaixo em âmbar (EN 19.7% below); o flop A♠ 3♠ 6♥; sticker de link "Abrir o Field Hotspots" |
| Story | 1080x1920 | EN | The BB overdefends here | Field Hotspots: what leaves on Monday doesn't come back the same. | Mesma imagem do story PT; sticker de link "Open Field Hotspots" |
| Story da capa | 1080x1920 | PT | Field Hotspots no ar | 8 spots de desvio forte do field. | Pílula NOVO; a barra do menu do topo com o item Field Hotspots e o selo NEW em destaque, e a lista de spots com os rótulos Overfold e Overdefend (sem números, ou só os confirmados); sticker de link "Abrir o Field Hotspots" |
| Carrossel 1 (capa) | 1080x1350 | EN | Field Hotspots is live | 8 strong field deviations from GTO, spot by spot. | Pílula NEW; janela do produto com a lista de spots e o item Field Hotspots NEW no menu do topo |
| Carrossel 2 (o que é) | 1080x1350 | EN | Postflop spots. Field vs GTO. | Position pair, stack, pot type, flop texture. | Lista de 3 a 4 cards de spot (par de posições, stack, SRP, textura, rótulo Overfold/Overdefend), sem números |
| Carrossel 3 (um spot) | 1080x1350 | EN | One spot, fully broken down | UTG vs BB · 25bb · SRP · A-high two-tone flop | O spot da semana: os 3 boards de exemplo (A♠ 3♠ 6♥, 6♠ A♣ 7♣, 7♣ A♥ 5♥), o rótulo OVERDEFEND, no c-bet de 50%, field 53,8% contra GTO 73,5%, a diferença 19,7% abaixo, e as abas Fold, Call, Raise com os 3 sizes (barras de fold, field × GTO: 33% 45,1% × 52,5%; 50% 53,8% × 73,5%; 65% 59,4% × 76,3%; EN com ponto) |
| Carrossel 4 (como explorar) | 1080x1350 | EN | How to exploit it | BB overdefends. Bluff less, bet more for value. | A caixa "Como explorar" em âmbar, com o texto da tela (EN exato: "The BB defends too much against the c-bet. Bluff less and bet more for value."; PT: "O BB defende demais contra c-bet. Blefe menos e aposte mais por value."), sobre o flop A♠ 3♠ 6♥ e o rótulo OVERDEFEND. Sem mãos exemplificadas |
| Carrossel 5 (Grátis 1 × pago 8) | 1080x1350 | EN | Free sees 1. GTO Mode sees 8. | The other 7 spots stay locked. | A lista com 1 spot liberado ("spot of the week") e as duas linhas da tela do Grátis ("+7 spots unlocked in GTO Mode" e "Next spots: Mon, Nov 2") |
| Carrossel 6 (rotação) | 1080x1350 | EN | Spots leave every Monday | 2 out, 2 in. First swap: Nov 2. | Linha do tempo semanal: 8 slots, 2 saindo e 2 entrando; data "Nov 2" em âmbar. Sem contador regressivo |
| Carrossel 7 (CTA) | 1080x1350 | EN | See this week's hotspots | Link in bio. | Logo e fundo da marca |

Contagem de palavras: títulos de 3 a 6 palavras; apoios de 3 a 10 palavras (story da capa: 10; carrossel 1: 8; carrossel 3: 8 mais símbolos).

Notas de arte:
- **Gancho FOMO nas artes:** feed e carrossel 5 e 6 carregam o FOMO verdadeiro (1 de 8, rotação). Nenhuma arte leva contador, "últimas vagas" ou data de fim; a única data é "Nov 2" (primeira troca).
- **Cores:** fold em teal `#015A6B` (as barras do slide 3 e do feed são de fold); diferença em âmbar. O rótulo Overdefend usa o laranja da tela e o Overfold, o azul, como na tela.
- **Story da capa:** é o gancho de lançamento; a pílula NOVO só marca o lançamento.
- **Carrossel 4:** só o texto da caixa "Como explorar", como o produto o escreve; nenhuma mão nem recomendação extra.
- **Carrossel 5:** reproduzir a lógica da tela do Grátis (1 spot da semana liberado, e as linhas "+7" e "Next spots"). Sem preço.
- **Enquete opcional no story (fora da arte):** "Seu BB defende demais contra c-bet?" com "Sim" e "Depende" / "Does your BB overdefend against c-bets?" with "Yes" and "Depends".

---

# (c) Discord
Texto completo, com URLs, em `discord.md` (mesma pasta). PT e EN, abaixo de 1.200 caracteres cada, com no máximo 3 emojis funcionais.

# (d) Instagram
Legendas do feed (PT e EN), do carrossel (bilíngue) e dos stories (sticker de link) em `instagram.md`.

# (e) E-mail
Assuntos, preheader e corpo PT e EN em `email.md`.

---

## Números usados

Contagens que são **fatos do produto** (podem ser escritas): 8 spots liberados com o Modo GTO; 1 spot da semana no Grátis (e +7 trancados); 2 spots entram e 2 saem toda segunda; primeira troca na segunda 02/11 (EN "Nov 2"); sizes de c-bet 33%, 50% e 65%; stack 25bb e o par UTG vs BB do spot da semana (parâmetros da tela de 22/10, não estatísticas).

Fonte: `numeros-verificados.md` (mesma pasta). "§1" é a tabela "O que está no ar"; "§2" é a tabela do exemplo "UTG vs BB, 25bb, SRP" (as linhas são os c-bets de 33%, 50% e 65%). Spot: UTG vs BB, 25bb, SRP, flop A-high two-tone unpaired com OESD possível, overdefend.

| Número no texto | Valor (PT · EN) | Linha da fonte | Onde aparece |
|---|---|---|---|
| Fold do field, c-bet de 50% | 53,8% · 53.8% | §2, linha "50% do pote", coluna "Fold do field" (Q5: `bet_50` 0,538) | Landing (bullet 1), artes (feed, carrossel 3), `discord.md`, `instagram.md`, `email.md` |
| Fold do GTO, c-bet de 50% | 73,5% · 73.5% | §2, linha "50% do pote", coluna "Fold do GTO" (Q5: `bet_50` 0,735) | Idem |
| Desvio, c-bet de 50% | 19,7% abaixo · 19.7% below | §2, linha "50% do pote", coluna "Desvio" (e "Linha da tela") | Landing, artes (story, carrossel 3), `discord.md` (só o fold e o GTO), `instagram.md`, `email.md` |
| Fold do field × GTO, c-bet de 33% | 45,1% × 52,5% · 45.1% × 52.5% | §2, linha "33% do pote" (Q5: `bet_33` 0,451 / 0,525) | Só na arte do carrossel 3 |
| Desvio, c-bet de 33% | 7,4% abaixo · 7.4% below | §2, linha "33% do pote" | Só na arte do carrossel 3 |
| Fold do field × GTO, c-bet de 65% | 59,4% × 76,3% · 59.4% × 76.3% | §2, linha "65% do pote" (Q5: `bet_65` 0,594 / 0,763) | Só na arte do carrossel 3 |
| Desvio, c-bet de 65% | 16,9% abaixo · 16.9% below | §2, linha "65% do pote" | Só na arte do carrossel 3 |
| "Como explorar" (PT e EN exatos) | "O BB defende demais contra c-bet. Blefe menos e aposte mais por value." · "The BB defends too much against the c-bet. Bluff less and bet more for value." | §2, "Como explorar (texto que a tela mostra)" | Carrossel 4 (caixa), legendas, landing, e-mail |
| 8 spots liberados / 1 no Grátis | 8 · 1 | §1, linhas "Spots liberados hoje" e "Spots no Grátis" (Q3: 8 e 1) | Todas as peças |
| 2 entram e 2 saem toda segunda | 2 · 2 | §1, linhas "Entram por semana" e "Saem por semana" (Q4) | Todas as peças |
| Primeira troca | segunda 02/11 (EN Nov 2) | §1, linha "Primeira troca" | Todas as peças |
| Sizes de c-bet | 33%, 50%, 65% | §2 (colunas "c-bet") | Landing, artes, legendas, Discord |
| Boards de exemplo | A♠3♠6♥, 6♠A♣7♣, 7♣A♥5♥ | §2, última linha (exemplos da classe, não o spot inteiro) | Artes (carrossel 3, story) |

Não usados de propósito: faixas do GTO (50,9–54,2; 67,5–79,5; 70,3–82,3) e "13,7% fora da faixa"; mãos por spot (15.674 na c-bet de 50%, na tela "15,7 mil mãos"; 41.087; 3.276; 182.372 nos 8 spots); escala (21.333.719 mãos do field, "mais de 21 milhões de mãos do field"; 1.049 spots, "mais de 1.000 spots de flop ranqueados"); 688 spots do catálogo; permanência de 4 semanas; preço e qualquer percentual de ganho. Nenhuma peça promete "688 spots" nem data final (fonte, §1, "Cuidados"). PT com vírgula, EN com ponto; desvio em %, nunca "pp".

## Condições do revisor de marca (parecer final OK COM RESSALVAS, 22/10)
- **D: outros spots nas artes.** O carrossel 1 e 2 e o story da capa mostram, sem números, os rótulos de outros spots da janela de 22/10 (BTN vs BB 40bb, BTN vs SB 40bb, UTG vs BB 40bb), lidos da tela. Eles não estão no `numeros-verificados.md` e saem a partir de 02/11 (o lote de abertura sai 2 por semana). Publicar antes de 02/11; depois disso, trocar esses cards.
- Decisões do Rafael: "fichas na mesa" (Pendência 10), rodapé de amostra do brand-kit × regra sem bastidor.
- Discord recontado com `len()`: PT 902, EN 897 caracteres (teto 1.200).
