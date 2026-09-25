# Meta Ads para o Modo GTO: plano e criativos

**Sessões:** overnight de 22/09/2026 (plano original) · revisão de 25/09/2026 (R$ 1.000, Modo GTO no ar) · **Branch:** `feature/meta-ads-overlay-poolvsgto` · **Status:** plano. **Nada foi criado, editado, pausado, ativado ou gasto na Meta.** A conta e o pixel foram só lidos. Em 22/09 também foram lidos o GA4, o Woo e o Postgres de analytics, só em agregados.

## Em cinco linhas (revisão de 25/09)

1. A mídia de setembro não falhou por criativo. Público de bets no BR, configuração mexida antes do gate e um funil que não passava UTM, `fbclid` nem pagamento para a Meta. Resultado: R$ 1.771 na vida da conta, ~12 cadastros, zero assinatura. A conta não gasta nada desde 15/09.
2. **Orçamento total de R$ 1.000**, num público só (identidade EN, o único recorte que já produziu), otimizando **`CompleteRegistration`**. R$ 1.000 compra de 10 a 40 cadastros no histórico da conta; **nenhum evento sai da fase de aprendizado**, e a venda nem chega perto.
3. **Fase 1 · teste, R$ 600:** 3 criativos prontos, um por conjunto, R$ 20/dia cada, 10 dias, com corte por criativo escrito antes. **Fase 2 · concentração, R$ 400:** o vencedor a R$ 40/dia por 10 dias, só se alguém ficar a ≤ R$ 60 por cadastro.
4. **Destino:** a landing do #11 em modo de lançamento → cadastro → checkout do plano GTO. A lista de espera deixa de ser destino. 🔴 **Hoje um cadastro novo não consegue comprar o GTO**: o front não pede o plano no checkout. É o A1 do brief 12, parte do go-live.
5. **Para gastar mais:** uma assinatura GTO atribuída à Meta **e** o CAC estimado com a taxa cadastro → pago medida (B4) abaixo de R$ 500. R$ 1.000 sozinho não prova o CAC.

## Os documentos

| # | Doc | O que tem |
|---|---|---|
| 01 | [linha de base](01-linha-de-base.md) | números reais de 22/09: Meta por campanha e criativo, funil GA4, UTM medida ao vivo, base e receita agregadas, o que faltou |
| 02 | [plano em fases](02-plano-em-fases.md) | **revisado em 25/09:** o que R$ 1.000 compra, evento de otimização, público, funil com o que existe e o que falta, Fases 0/1/2, cortes, os 3 criativos, o que depende do Rafael |
| 03 | [posicionamento e mensagem](03-posicionamento-e-mensagem.md) | Dunford, unicidade, promessa, "o gap", banco de provas, **nomes comerciais**, auditoria da landing e o texto da `/gto` |
| 04 | [12 reels](04-reels.md) | roteiros: gancho, storyboard, texto na tela e legenda. **Nenhum produzido**; o R6 é o primeiro a produzir |
| 05 | [10 posts e carrosséis](05-posts-carrosseis.md) | card a card, com legenda e destino |
| 06 | [stack de IA](06-stack-ia.md) | comparativo com preço, stack de ~US$ 100 e ~US$ 300, bíblia do personagem, prompts. **Fora desta rodada** |
| 07 | [compliance](07-compliance.md) | checklist por anúncio, frases proibidas e substitutas, gambling, divulgação de IA, CONAR e CDC |
| 08 | [concorrência](08-concorrencia.md) | o que a Biblioteca de Anúncios mostra e o espaço livre |
| 09 | [depoimentos](09-depoimentos.md) | 2 depoimentos reais (autorização pendente) e a fala do Rafael (versão B, aprovada, com regra de posição) |

## Orçamento por fase (25/09)

| Fase | Mídia | Passa para a próxima quando |
|---|---:|---|
| 0 · Pré-requisitos | R$ 0 | os 8 itens do `02 §3.3` com prova |
| 1 · Teste de criativo | **R$ 600** (3 × R$ 20/dia × 10 dias) | D10 com um criativo a ≤ R$ 60 por cadastro e ≥ 2 cadastros |
| 2 · Concentração | **R$ 400** (R$ 40/dia × 10 dias) | fim do orçamento; mais verba só com o `02 §6.1` |
| **Total** | **R$ 1.000** | |

Ferramentas: R$ 0 nesta rodada. Os três criativos já existem; a troca do selo é render local.

## Os três criativos desta rodada

1. **`disc02-plataforma-mda-en`** (controle): o melhor EN medido, R$ 62 por cadastro.
2. **`disc-04-pioneiro-en`**: o ângulo "isso não existia", o único que converteu no BR frio.
3. **`board01-1560-boards-en`**: o mais novo, a tela de resultado real do Postflop. Está em commits sem push de outra branch.

Os três precisam trocar o selo "500M+ audited hands" por "400K+ tournaments" (B6 da landing) antes de subir. Nenhum mostra o Modo GTO; o **R6 `um-clique-o-gap`** entra no lugar do terceiro se ficar pronto antes do D1.

## O que depende do Rafael antes do primeiro real

Lista completa em `02 §9`. Em resumo:

1. **Go-live do Modo GTO**, com o A1 do brief 12 (o checkout do GTO a partir do app).
2. **Merge do aura-landing#11** com `VITE_LAUNCH_MODO_GTO=1` e o Field vs GTO desligado (a A12b espera a HUB).
3. **Conta de anúncio:** forma de pagamento, verificação da empresa e do domínio, 2FA.
4. **Criar a campanha** do `02 §4.1`. Agente não cria nada no Meta.
5. **Sim para a leitura agregada do AuraBusiness** e autenticação do Stripe (B4), para medir o CAC.
6. A14 (real no checkout) e as autorizações dos depoimentos (B2) **não travam este teste em EN**, mas travam qualquer anúncio em PT com preço e qualquer peça com depoimento.

## Limites

- **Stripe e AuraBusiness:** não lidos em 22/09 nem em 25/09. A B4 autoriza a leitura agregada; o AuraBusiness pede o sim do Rafael na sessão.
- **Biblioteca da Meta pela API:** não devolve formato nem CTA dos anúncios.
- **Estatísticas do pixel:** a Meta guarda só 28 dias; o que está no `02 §3.2` é dos últimos 7 (18 a 25/09).
- **Sessão de teste no GA4 (22/09):** uma sessão com `utm_source=diag_claude` entrou de propósito, para medir o repasse de UTM.
