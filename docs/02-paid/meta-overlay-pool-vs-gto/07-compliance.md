# 07 · Compliance: Meta, poker, IA e publicidade no Brasil

Atualiza `docs/02-paid/compliance-meta.md` (04/07/2026) com o que mudou: avatar de IA, a política de divulgação de IA de 2026, o ambiente de bets no Brasil e as frases do lançamento do Modo GTO. Isto não é parecer jurídico; é a regra operacional para subir anúncio.

## 1. Checklist antes de subir QUALQUER anúncio

Marque todas as linhas. Uma linha falhando, o anúncio não sobe.

**Produto e promessa**
- [ ] O texto fala de **estudo, dado, análise, decisão, spot, field, GTO**, nunca de ganhar dinheiro.
- [ ] Nenhuma das frases proibidas do §2 aparece no texto, na tela, na fala nem na legenda.
- [ ] Todo número foi conferido na tela no dia, com `n` visível no criativo, e o print de origem está guardado.
- [ ] Nada do que aparece como "no ar" está fora de produção. Na Fase 1, Modo GTO e Field vs GTO aparecem com `prévia do beta` e "em breve".
- [ ] "Grátis" quer dizer grátis: sem cartão, sem cobrança futura escondida (CDC). O texto do card Grátis bate com o que o Grátis vê (ver o achado 4 do `03 §5.1`).
- [ ] Sem nome de concorrente no texto (regra de marca). "GTO" e "solver" genéricos podem.
- [ ] Sem EV por mão, sem "GTO em qualquer spot", sem "cobre GG".

**Imagem**
- [ ] Zero fichas, cartas espalhadas em mesa de cassino, roleta, dinheiro, cifrão, luxo. A tela do produto é o visual.
- [ ] Nenhum e-mail, nome de conta ou nick visível.
- [ ] Rodapé `18+` em todo quadro.

**IA**
- [ ] Se houver o analista da Aura ou voz sintética: selo `Personagem gerado por IA` no quadro do começo ao fim **e** rótulo de IA ligado no fluxo de criação do anúncio.
- [ ] O personagem não fala como cliente, não dá depoimento, não fala de resultado.
- [ ] Nenhum rosto ou voz de jogador, coach, influencer ou pessoa real, nem "parecido com".
- [ ] B-roll gerado não imita a interface da Aura.

**Segmentação e destino**
- [ ] Idade mínima de 18 anos (a Aura usa 21+ por padrão).
- [ ] Nas campanhas EN, os 18 mercados que a Meta lista como proibidos para gambling estão excluídos, por precaução (`compliance-meta.md §2`).
- [ ] A landing de destino não tem link para sala de poker, bônus, afiliado nem "jogue aqui", e tem o rodapé "Ferramenta de estudo · 18+ · A Aura não é site de apostas e não oferece jogo".
- [ ] Audience Network desligada.

**Prova social**
- [ ] Depoimento só de pessoa real, identificada, que usou o produto e deu autorização por escrito para aquele texto. Sem isso, não tem depoimento.

## 2. Frases a evitar, e o que dizer no lugar

| Evitar | Por quê | Dizer no lugar |
|---|---|---|
| "Ganhe mais" / "ganhe dinheiro" / "aumente seus ganhos" | resultado financeiro (Meta: práticas comerciais inaceitáveis; CONAR; CDC) e sinal de gambling | "estude o spot certo" · "veja onde o field desvia" |
| "Lucro", "lucre", "renda", "bankroll subindo" | idem | "decisão", "edge" em contexto técnico, sem valor em dinheiro |
| "Aumente seu winrate / ROI em X semanas" | promessa de resultado não comprovável | "o número do field, com a amostra" |
| "Garantido", "certeza", "infalível" | promessa absoluta | "medido em 500M+ mãos" |
| "Aposte", "aposta", "bet", "banca", "odds", "palpite", "sinais", "grupo VIP" | vocabulário de bets; ativa o classificador de gambling | "spot", "linha", "decisão" |
| "Jogue agora", "cadastre-se e jogue" | parece operador de jogo | "crie a conta", "entre na lista" |
| "Bônus", "freebet", "depósito", "saque" | operador/afiliado | não se aplica à Aura |
| "O melhor solver", "melhor que [concorrente]" | a Aura não é solver; comparativo nominal | "o GTO e o field na mesma tela" |
| "EV por mão", "quanto você perde por mão" | o produto não calcula (salvo Spots do mês) | "valor em bb do spot" só no Field vs GTO, lido da tela |
| "Bilhões de mãos" | falso; o número aprovado é 500M+ | "500M+ mãos auditadas" |
| "Todas as salas", "GGPoker" | GG, Party e 888 = 0% | "7 salas" |
| "Overlay" | em MTT, overlay é o buraco do garantido; lê como torneio | "Modo GTO" (`03 §2`) |
| "Pool" em copy | regra de marca | "field" |
| "Eu uso a Aura e…" na boca do avatar | depoimento falso | o analista apresenta; não testemunha |

## 3. Por que a Aura não pede a autorização de gambling (e o risco que sobra)

A política da Meta de *Online Gambling and Games* cita **"poker"** nominalmente entre os exemplos, mas define o escopo como produto ou serviço em que *algo de valor monetário é exigido como entrada e faz parte do prêmio*. A Aura não tem entrada, prêmio, aposta, depósito nem saque: é SaaS de análise de mãos já jogadas. Está fora do escopo, e não pede autorização (`compliance-meta.md §2`; política relida em 22/09 em transparency.meta.com).

**O risco não é estar errado, é ser mal classificado.** A palavra "poker" dispara revisão automática. No Brasil, o ambiente endureceu: a AGU notificou a Meta em 08/2025 para derrubar anúncios de bets não licenciadas, e a Portaria SPA/MF 1.207/2024 regula a publicidade dos operadores. A Aura não é operador, e essas regras não se aplicam a ela diretamente, mas o classificador fica mais sensível a tudo que parecer bet. Um detalhe medido: a Meta classifica a conta como "Publishing / Online Only Publications", não como software, o que reforça que o texto do anúncio tem que deixar claro que é ferramenta de estudo.

**Não existe caso público** de anunciante de software de estudo de poker rejeitado ou aprovado por esse motivo. GTOWizard, Upswing, os Geckos e o Drivehud anunciam há meses (`08-concorrencia.md`), o que sugere que o caminho está aberto, mas não garante nada.

## 4. Divulgação de IA

- **Meta:** o rótulo "AI info" é obrigatório em anúncios de tema social, eleitoral e político com pessoa ou voz realista criada ou alterada. Fontes secundárias convergentes dizem que em 03/2026 a exigência se estendeu a anúncios comerciais em que a IA gera ou altera substancialmente o sujeito visual. A página oficial não foi confirmada nesta pesquisa. **Regra da Aura: ligar a divulgação sempre que houver o analista ou voz sintética, com ou sem detecção automática (C2PA).** Ajuste de cor, corte ou sugestão de texto por IA não precisa de rótulo.
- **CONAR:** o Guia de Publicidade por Influenciadores Digitais de 2026 (vigente desde 01/06/2026) tem seção de IA. As regras do Código valem para conteúdo gerado por IA como para qualquer outro, e anunciante, agência e criador respondem juntos. O uso de IA não pode induzir o consumidor a erro.
- **Na prática:** o selo no quadro, o rótulo no anúncio, a frase "apresentador gerado por IA" na legenda dos reels com o analista, e o R5, que faz da divulgação o gancho.

## 5. Se um anúncio for reprovado

Segue o `compliance-meta.md §4` sem mudança:

1. Não republicar idêntico.
2. Pedir revisão com a justificativa padrão: "software de análise estatística para estudo de poker; não oferece jogo, apostas nem prêmios; sem links para gambling".
3. Em paralelo, subir uma variação com menos sinal (menos "poker" no texto, nenhuma carta na imagem).
4. Registrar em `docs/02-paid/log-reprovacoes.md`.

Com 3 reprovações no mesmo tema, pedir a autorização formal pelo portal *Autorizações e verificações*, com a verificação da empresa como pré-requisito (Fase 0, item 0.9). **Nunca** abrir outra conta para contornar: é o que transforma restrição em banimento do BM.

## 6. Fontes

- Meta, *Online Gambling and Games*: https://transparency.meta.com/policies/ad-standards/restricted-goods-services/gambling-games/
- Meta, *About Meta's Online Gambling and Games policy*: https://www.facebook.com/business/help/345214789920228
- Meta, *Unacceptable business practices*: https://transparency.meta.com/policies/ad-standards/fraud-scams/unacceptable-business-practices/
- Meta, *Personal attributes*: https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/
- Lei 14.790/2023; Portaria SPA/MF 1.207/2024; AGU × Meta (igamingtoday.com, 08/2025)
- CONAR, Guia de Influenciadores 2026 (resumos em migalhas.com.br, cesconbarrieu.com.br, tozzinifreire.com.br)
- CDC, arts. 30, 31 e 37
