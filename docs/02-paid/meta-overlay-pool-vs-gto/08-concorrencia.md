# 08 · Concorrência na Biblioteca de Anúncios da Meta (22/09/2026)

Fonte: `ads_library_search` (25 chamadas, só leitura). **Limite da ferramenta:** ela devolve página, título do link e datas de criação. Não devolve formato, corpo, CTA, destino nem se há rosto ou avatar. A longevidade abaixo foi inferida pela primeira e pela última criação do mesmo título. Para ver o criativo, é preciso abrir o `ad_snapshot_url` de cada um no navegador. Os títulos em inglês estão reproduzidos como apareceram.

## 1. Quem anuncia

| Anunciante | Mercado | O que vende no gancho | Longevidade observada |
|---|---|---|---|
| **GTOWizard** | global (inclusive BR) | capacidade nova do solver: "Solve Any Cash Spot You Want", "Preflop ICM Solving Is Live", "The PLO Upgrade Is Live" | troca o gancho a cada 3–7 dias, com presença contínua de ~5 semanas |
| **UpswingPoker** | US, também BR | história de mão e conteúdo: "The Fold That Shouldn't Be Possible"; promoções sazonais | anunciante desde pelo menos 03/2025 |
| **GTO Gecko / PLO Gecko** | Noruega | velocidade: "Master the game within weeks!", "Increase your winrate in weeks!" | ~88 dias no mesmo gancho |
| **Custom Poker Trainer AI** | US | "Increase your win-rate in weeks" | ~6 semanas |
| **Raise Your Edge** | US | comunidade: "Join The Biggest Poker Community" | ~2 meses |
| **Poker Academy** | Polônia | estudo: "Give recurring spots a proper study session" (4 ganchos em paralelo, teste ativo) | recente |
| **River** | Noruega | "See what each decision cost" | recente (19/09) |
| **Drivehud** | US | tracker: "Track. Analyze. Review. Improve." | ~6 semanas |
| **reglifepoker** (BR) | BR | "Você não precisa de mais um curso. Você precisa de um sistema." | **~163 dias, o mais longevo do levantamento** |
| PolarizePoker, Stars/Raptors/Forza Poker Team, Exploit Poker Team | BR/PT | recrutamento de staking | alto volume, não é estudo |

Sem presença detectável: PokerSnowie, Hand2Note, PokerTracker, Hold'em Manager, pokercode, DeepSolver, PokerCoaching, Chip Leader Coaching, Odin, Simple GTO Trainer, GTO+/Postflop+, Run It Once. A busca não distingue "não anuncia" de "anuncia com outro nome de página".

## 2. Padrões da categoria (skill competitor-branding)

- **Três promessas dominam:** velocidade de melhoria ("in weeks"), capacidade do solver ("now live") e comunidade/sistema. Todas falam do jogador ou da ferramenta, **nenhuma fala do field**.
- **"Winrate in weeks" é a promessa mais usada e a que a Aura não pode usar.** É promessa de resultado (`07-compliance.md §2`) e não é o que o produto entrega. Deixar para eles.
- **GTOWizard trata cada feature nova como notícia** e troca o gancho em dias. É o padrão Ogilvy de "injetar novidade", e é o que a F2-D copia no ritmo, não no tom.
- **Upswing vende com mão real contada como história.** É o formato editorial que a Ogilvy diz que vence o formato de anúncio. O R10 é a versão Aura disso: um spot real, contado, com o número do field.
- **No BR, o volume de "poker" pago é staking e bet.** Estudo em português é pouco disputado: só o reglifepoker sustenta anúncio. O gancho dele ("sistema, não mais um curso") fala com a mesma dor do arquétipo C (`02 §2`).

## 3. O espaço livre para a Aura

1. **Dado do field como gancho.** Nenhum anunciante com sinal forte usa "o que o field de verdade faz" com prova de volume.
2. **O GTO *e* o field na mesma tela.** O GTOWizard vende o equilíbrio; ninguém vende a distância entre o equilíbrio e a população. É o "gap" do `03 §2`.
3. **Honestidade de amostra.** Ninguém fala de `n`, intervalo de confiança ou de recusar um número. O R8 e o P9 ocupam isso sozinhos.
4. **Português técnico.** GTOWizard roda no BR sem uma linha em PT (`product-marketing.md §5`). Um anúncio em PT com jargão em inglês é, hoje, quase exclusivo.

## 4. Para abrir à mão (5 minutos, antes da rodada 1)

Abrir o `ad_snapshot_url` dos anúncios de maior longevidade (reglifepoker, GTO Gecko, GTOWizard "Solve Any Cash Spot", Upswing "The Fold That Shouldn't Be Possible") e anotar: formato, se há rosto, se a tela do produto aparece e em que segundo, e o CTA. Os ids estão no relatório bruto do agente; a busca se refaz em `ads_library_search` com o nome da página.
