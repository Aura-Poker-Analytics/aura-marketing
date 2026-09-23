# Meta Ads para o Modo GTO e o Field vs GTO: plano e criativos

**Sessão:** overnight de 22/09/2026 · **Branch:** `feature/meta-ads-overlay-poolvsgto` · **Status:** plano. **Nada foi criado, editado, ativado ou gasto na Meta.** A conta, o GA4, o Woo e o Postgres de analytics foram só lidos, e só em agregados.

## Em cinco linhas

1. A mídia de setembro não falhou por criativo. Público de bets no BR, configuração mexida antes do gate e um funil que não passava UTM, `fbclid` nem pagamento para a Meta. Resultado: R$ 1.771 na vida da conta, ~12 cadastros, zero assinatura.
2. **Fase 0 (R$ 0):** consertar o funil. UTM e `fbclid` da landing para o app, evento `Purchase` saindo do Stripe, página `/gto` com formulário próprio e cadastro em PT.
3. **Fase 1 (R$ 1.400, 4 semanas):** lista de espera do Modo GTO. Reabre o único recorte que já produziu (identidade EN) e prova com pelo menos uma assinatura que o funil fecha.
4. **Fase 2 (R$ 2.940 garantidos, teto de R$ 6.300; agressivo de R$ 12.600 só por gate):** lançamento no dia em que o Modo GTO responder 200 em prod. CAC-alvo de R$ 600, com corte automático em 52 cadastros sem assinatura.
5. Criativo: a tela real é a estrela. O "analista da Aura" é um personagem de IA divulgado como tal, e ele mesmo faz da divulgação o gancho.

## Os documentos

| # | Doc | O que tem |
|---|---|---|
| 01 | [linha de base](01-linha-de-base.md) | números reais: Meta por campanha e criativo, funil GA4, UTM medida ao vivo, base e receita agregadas, o que faltou |
| 02 | [plano em fases](02-plano-em-fases.md) | economia unitária, público, Fases 0/1/2 com estrutura, orçamento em 3 cenários, KPI amarrado a pagamento e critério de corte |
| 03 | [posicionamento e mensagem](03-posicionamento-e-mensagem.md) | Dunford, unicidade, promessa, "o gap", banco de provas, **nomes comerciais**, auditoria da landing e o texto da `/gto` |
| 04 | [12 reels](04-reels.md) | gancho, storyboard, texto na tela e legenda de cada um; os 3 ganchos para testar primeiro |
| 05 | [10 posts e carrosséis](05-posts-carrosseis.md) | card a card, com legenda e destino |
| 06 | [stack de IA](06-stack-ia.md) | comparativo com preço, stack de ~US$ 100 e ~US$ 300, bíblia do personagem, prompts e roteiros prontos para colar |
| 07 | [compliance](07-compliance.md) | checklist por anúncio, frases proibidas e substitutas, gambling, divulgação de IA, CONAR e CDC |
| 08 | [concorrência](08-concorrencia.md) | o que a Biblioteca de Anúncios mostra e o espaço livre |
| 09 | [depoimentos](09-depoimentos.md) | 2 depoimentos reais (autorização pendente) e 3 versões da fala do fundador (o Rafael escolhe) |

## Orçamento recomendado por fase

| Fase | Mídia | Ferramentas | Passa para a próxima quando |
|---|---:|---:|---|
| 0 · Pré-requisitos | R$ 0 | ~R$ 540/mês | 12 itens com prova (`02 §3`) |
| 1 · Pré-lançamento | **R$ 1.400** | ~R$ 540/mês | D28 com custo por cadastro ≤ R$ 60 |
| 2 · Lançamento | **R$ 2.940 → teto de R$ 6.300**; agressivo de R$ 12.600 só com CAC ≤ R$ 600 provado | ~R$ 1.600/mês | — |

## Os três ganchos para testar primeiro

1. **"Um clique. O GTO de um lado, o field do outro."** (R6). A promessa demonstrada na tela, com notícia.
2. **"Eu sou uma IA. Os 500 milhões de mãos, não."** (R5). A divulgação obrigatória vira gancho.
3. **"A Aura se recusou a me mostrar esse número."** (R8). Prova de confiança para um público cético; ninguém na categoria fala disso.

## O que depende do PO antes do primeiro real

1. **Dev da Fase 0**, itens 0.1 a 0.7: UTM e `fbclid` repassados, `fbc` no cadastro, `Purchase` via Stripe → CAPI e GA4, `/gto` com `Lead`, cadastro em PT, e-mail D0, report de coorte.
2. **Conta e BM:** criar os públicos (visitantes, vídeo, listas de cadastro e pagantes); confirmar verificação da empresa, domínio e 2FA; ligar o filtro anti-bet nos comentários.
3. **Preço:** o valor em BRL do Individual e dos planos GTO e Top (as 9 decisões de `pricing-tiers-plan.md §7`). Os reels R4 e P6 e a `/gto` da Fase 2 precisam do número.
4. **Nomes:** "Modo GTO" em vez de "overlay" (em MTT, overlay é o buraco do garantido) e "Field vs GTO" em vez de "Pool vs GTO" (regra "field, nunca pool").
5. **O personagem:** aprovar o analista da Aura, gerado do zero e sem rosto nem voz de pessoa real.
6. **Deploy para a Fase 2:** merge do #27, deploy da API (não há pipeline), migration `plan_tier`, flag `GtoOverlay:Enabled` e smoke com login real. Para a onda 2b, o Field vs GTO sair de branch.
7. **Orçamento:** aprovar o teto por fase e o gatilho de escala.
8. **Leitura para o CAC:** autenticar o Stripe numa sessão de leitura (churn e LTV) ou autorizar leitura agregada do `AuraBusiness` (grátis→pago por coorte). Sem isso, o CAC-alvo de R$ 600 é hipótese.
9. **Landing atual:** corrigir o card Grátis ("Hotspot — exploração completa" deixou de ser verdade com o #26) e o "spots que geram EV". São risco de CDC com ou sem mídia.

## Limites desta sessão

- **Stripe:** não autenticado. A receita Stripe e o churn não foram lidos.
- **Postgres de analytics de prod:** só tem tabelas de poker. Cadastro e plano ficam no `AuraBusiness`, fora da autorização.
- **Biblioteca da Meta pela API:** não devolve formato nem CTA dos anúncios.
- **Log de atividade da conta:** não liberado. A data exata da pausa da DISC02-EU não foi confirmada por ferramenta.
- **Sessão de teste no GA4:** uma sessão com `utm_source=diag_claude` entrou de propósito, para medir o repasse de UTM.
