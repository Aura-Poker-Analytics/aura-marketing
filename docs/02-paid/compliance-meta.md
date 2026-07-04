# Compliance Meta Ads — Aura Poker Analytics

**Autor:** thread Mídia Paga · **Data:** 2026-07-04 · **Status:** análise pré-gasto (Fase A, custo zero)
**Decisão que este doc suporta:** podemos anunciar a Aura na Meta sem autorização prévia de "Online Gambling and Games"? Resposta curta: **sim, com argumentação sólida — mas com risco real de false-positive na revisão automática. Plano de mitigação e contingência abaixo.**

---

## 1. O que a policy diz (verificado em 04/07/2026)

Fonte: [Online Gambling and Games — Meta Transparency Center](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/gambling-games/) e [How to Apply for Permission — Business Help Center](https://www.facebook.com/business/help/4740325989340856).

- **Escopo:** produtos/serviços onde algo de **valor monetário é exigido como entrada E faz parte do prêmio** (aposta, loteria, cassino, fantasy sports, **poker** real money, torneios de skill games com prêmio).
- **Exige autorização prévia** (desde jul/2025 via portal **Autorizações e verificações** no Business Suite, não mais por e-mail): operadores de gambling online, jogos pay-to-play com prêmio monetário **e páginas de destino que promovam gambling online — incluindo sites afiliados**.
- **NÃO exige autorização:** jogos 100% free-to-play sem simulação de gambling e sem prêmio de valor monetário; cassinos físicos; streaming de poker offline; promoções de varejo com sorteio quando gambling não é o negócio principal.
- **Restrições dos autorizados:** targeting 18+ obrigatório e exclusão de 18 mercados proibidos (Azerbaijão, Bangladesh, Camboja, Egito, Hong Kong, Índia, Indonésia, Coreia, Quirguistão, Malásia, Mongólia, Mianmar, Paquistão, Filipinas, Arábia Saudita, Singapura, Taiwan, Tailândia, Vietnã).

## 2. Argumentação: por que a Aura está FORA do escopo

A Aura é **SaaS de estudo/analytics de poker** — assinatura dá acesso a estatísticas agregadas de pool. Aplicando a definição da policy:

| Critério da policy | Aura | Enquadra? |
|---|---|---|
| Entrada de valor monetário para jogar | Não há jogo. Assinatura compra acesso a software de análise | ❌ |
| Prêmio de valor monetário | Não existe prêmio de nenhum tipo | ❌ |
| Facilita apostas/jogo real money | Não processa apostas, não hospeda jogo, não deposita/saca | ❌ |
| Landing page promove gambling / afiliado | Landing vende assinatura de software; **não pode ter** link/bônus de sala de poker | ❌ (manter assim) |
| Simulação de gambling (social casino) | Exibe estatísticas e gráficos, não simula jogo | ❌ |

**Analogia de categoria:** a Aura está para o poker como um curso de análise técnica está para a bolsa — ferramenta educacional/analítica sobre uma atividade, não a atividade em si. Sites de treinamento/coaching de poker anunciam na Meta sem autorização de gambling há anos.

**Conclusão jurídico-operacional:** não é necessário pedir autorização prévia de Online Gambling and Games para BR, LatAm, EU ou US. A autorização é para quem OPERA gambling; a Aura não opera nem afilia.

### Por região (pergunta do PO)

| Região | Autorização Meta? | Observações locais |
|---|---|---|
| **BR** | Não | A regulação de apostas (Lei 14.790/2023 / SPA-MF) alcança **operadores de bets**, não software de estudo. CONAR: manter 18+ e zero promessa de ganho. |
| **LatAm** | Não | Nenhum país LatAm está na lista de 18 mercados proibidos. |
| **EU** | Não | Regras nacionais duras (IT, NL, DE, ES) miram operadores/afiliados de gambling. SaaS educacional fora do escopo. Se algum país reprovar sistematicamente, excluir do targeting é mais barato que discutir. |
| **US** | Não | Autorização por estado só para real-money gambling operators. |

**Precaução barata em campanhas EN:** excluir os 18 mercados proibidos mesmo sem obrigação — evita dar sinal "gambling-adjacent" pro classificador e não custa alcance relevante (ICP anglófono).

## 3. Risco real: false-positive da revisão automática

A revisão da Meta é automatizada na primeira camada e **classifica por sinais superficiais**: palavra "poker" no copy/landing, imagens de cartas/fichas/mesa, termos como "win rate", "$", "EV". Cenários, do mais provável ao pior:

1. **Anúncio individual reprovado** ("Online Gambling and Games") — probabilidade **alta** em algum momento. Impacto baixo se tratado certo.
2. **Reprovações em série** → queda de qualidade da conta, revisões mais lentas. Probabilidade média se ignorarmos o item 1.
3. **Restrição da conta de anúncios** ("advertising access restricted") — probabilidade baixa-média; gatilhos: muitas reprovações, apelações agressivas, conta com pouco histórico + gasto acelerando. Nossa conta tem histórico pequeno mas positivo (gasto em mar/2026, sem strikes visíveis).
4. **Restrição do Business Manager** — pior caso, raro sem reincidência.

### Mitigações de criativo/landing (checklist pré-subida de QUALQUER anúncio)

- [ ] Copy fala de **estudo, dados, análise, decisão** — nunca de ganhar dinheiro, lucro, bankroll "subindo", renda.
- [ ] Zero imagem de dinheiro, fichas empilhadas como riqueza, luxo. Gráficos e telas do produto são o visual (já é a linha do brand kit).
- [ ] 18+ configurado no targeting de TODAS as campanhas (nosso padrão, mesmo sem obrigação).
- [ ] Landing sem link para salas de poker, sem bônus, sem "jogue aqui" — e com rodapé "ferramenta de estudo · 18+".
- [ ] Palavras a evitar no texto do anúncio: aposta/bet, ganhe/win money, lucro garantido, cash out. "Poker" em si é inevitável e ok — coaching sites usam.
- [ ] Nada de comparativo nominal com concorrente (regra de brand, também reduz denúncia).

## 4. Plano de contingência

**Se um anúncio for reprovado:**
1. NÃO republicar idêntico. Pedir **revisão manual** (Account Quality → Solicitar análise) com justificativa curta: "software de análise estatística para estudo de poker; não oferece jogo, apostas nem prêmios; sem links para gambling".
2. Em paralelo, subir variação do criativo com sinal reduzido (trocar imagem/termos flagáveis).
3. Registrar em `docs/02-paid/log-reprovacoes.md` (criar na primeira ocorrência): data, campanha, criativo, motivo, resultado da apelação. Padrão de reprovação = insumo pra decidir o item abaixo.

**Se reprovações persistirem (3+ no mesmo tema):**
4. Abrir solicitação no portal **Autorizações e verificações** do Business Suite explicando o produto — mesmo entendendo que não precisamos, a autorização formal remove o atrito de uma vez. Pré-requisito prático: **verificação da empresa** (hoje pendente — ver `auditoria-meta-ads.md`), que já recomendo fazer antes do launch de qualquer forma.
5. Considerar suporte via chat do Meta Business Help (disponível para contas com gasto) anexando print da landing.

**Se a conta de anúncios for restringida:**
6. Apelar imediatamente em Account Quality com a mesma argumentação do §2 (ter este doc pronto é exatamente para isso). Não criar campanha em outra conta para "contornar" enquanto a apelação corre — circumvention é a violação que transforma restrição temporária em ban permanente do BM.
7. Enquanto durar: orgânico continua (canal principal), e o funil não para — a landing não depende de ads.

**Redutores de risco estruturais (fazer antes do 1º gasto):**
- Verificação da empresa no Business Manager (CNPJ AURA ANALYTICS LTDA já cadastrado na cobrança).
- Domínio da landing verificado no BM.
- 2FA no BM (hoje desligado) — restrição por segurança de conta é tão bloqueante quanto por policy.
- Começar gastando pouco em **retargeting quente** (menor volume de impressão → menor exposição ao classificador) e escalar devagar — coincide com a estratégia de mídia.

## 5. Resumo executivo

- **Não precisamos de autorização prévia** em nenhuma região-alvo: a Aura não se enquadra na definição (sem entrada monetária em jogo, sem prêmio, sem afiliação).
- O risco não é "estar errado", é **ser mal classificado**. Tratamento: criativos limpos (§3), apelação padronizada (§4), e autorização formal como plano B — não como pré-requisito.
- Pré-requisitos que EU recomendo antes do 1º real: verificação da empresa, domínio verificado, 2FA, campanhas antigas pausadas (detalhe na auditoria).

**Fontes:** [Meta Transparency — Online Gambling and Games](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/gambling-games/) · [Meta Business Help — Apply for Permission](https://www.facebook.com/business/help/4740325989340856) · [SBC Americas — novo fluxo de autorização (jul/2025)](https://sbcamericas.com/2025/07/10/metas-new-marketing-standards-gambling/)
