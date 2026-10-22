# Plano de marketing da Aura (nov/2026): como as skills serão usadas

**Criado em:** 22/10/2026 · **Sessão:** `aura · plano de marketing · grill-me` · **Estado:** fase 0 (entrevista) em andamento

Este documento é o roteiro de método: em que ordem cada skill entra, o que lê, o que entrega e onde grava. O plano de marketing em si sai das fases 0 a 3 e vai para `plano-marketing-2026-11.md`, nesta mesma pasta.

## Ponto de partida

- A Aura está no ar há meses, com app e landing muito melhorados desde o último esforço de aquisição.
- Nunca passou de ~20 usuários pagantes.
- Mídia paga sempre sofreu para achar o público. O único sinal bom lembrado: um impulsionamento antigo pelo próprio Instagram, com interesse "Esportes", que trouxe dezenas de seguidores grinders de MTT.
- Ativos: tokens da Meta e do Instagram, Meta Ads MCP (conta Aura Business), GA4 configurado, base de leads no AuraBusiness, Resend, acervo de docs de mídia paga em `docs/02-paid/` (branch `feature/descoberta-reels-v2`).

## Regras que valem para todas as fases

1. **Medir antes de gastar.** Nenhuma verba nova antes de a fase 1 dizer onde o funil perde gente e se o rastreio é confiável.
2. **Um gargalo por vez.** Cada ciclo ataca o maior vazamento medido, com uma hipótese e um número para conferir.
3. **Fica com o Rafael:** gasto em anúncio, e-mail para a base, publicação de post, mudança de preço e de marca. As skills preparam e recomendam; ninguém publica nem envia.
4. **Todo número tem fonte e data** (regra de ouro do repo). Nada de número vindo de chat.
5. **Termos de poker em inglês** no texto em PT; "a Aura", no feminino.

## Fases e skills

| Fase | Pergunta que responde | Skills | Lê | Entrega |
| --- | --- | --- | --- | --- |
| 0. Entrevista | O que queremos, para quem, com que limites? | `grill-me` / `grilling` | Respostas do Rafael + inventário do acervo + números atuais | `docs/00-strategy/entendimento-compartilhado-2026-11.md` |
| 1. Diagnóstico | Onde o funil perde gente? O rastreio é confiável? | `analytics`, `analytics-tracking` (repo), `traffic-analysis` (repo) | GA4, AuraBusiness (só leitura, agregado), pixel/CAPI, Resend | `docs/03-analytics/diagnostico-funil-2026-11.md` |
| 2. Consertar a medição | O que falta para medir visita → cadastro → trial → assinatura? | `analytics`, `meta-ads` (repo), `docs/02-paid/pixel-capi-spec.md` | Resultado da fase 1 | Spec de eventos para o `aura-novofront`/`aura-landing` (sessão própria lá) |
| 3. Conversão | Por que quem chega não assina? | `cro`, `page-cro`, `signup`, `onboarding`, `copywriting` | Funil da fase 1, landing, app, `_strategy/AURA-UX-BLUEPRINT.md` | Lista priorizada de mudanças na landing e no app, cada uma com hipótese e número |
| 4. Base de leads | Como reativar quem já se cadastrou? | `emails`, `churn-prevention` | Base de leads (segmentos), histórico do Resend, `escada-onboarding-emails.md` | Sequências de e-mail (rascunho) + fluxo de cancelamento |
| 5. Experimentos | A mudança funcionou? | `ab-testing` | Mudanças das fases 3 e 4 | Plano de teste por hipótese, com tamanho de amostra e critério |
| 6. Aquisição | Onde comprar atenção, e quanto? | `paid-ads-strategy`, `meta-ads-doctor`, `diagnostico-midia-paga`, `ads` (repo) | Funil consertado, histórico de campanhas, `analise-campanhas-historicas.md` | Plano de mídia com verba, público, criativo e critério de corte |
| 7. Conteúdo | O que publicar no Instagram e no Discord? | `lote-posts` (repo), agentes `aura-copywriter`, `aura-fabrica-posts`, `aura-revisor-marca` | Pilares do plano, brand-kit | Calendário e lotes de posts |

As fases 3 e 4 podem correr em paralelo depois da fase 1. A fase 6 só começa depois das fases 2 e 3, porque anúncio sobre um funil que não converte e não mede só repete o histórico.

## Como cada fase fecha

- Documento da fase gravado na pasta indicada, com fonte e data de cada número.
- Decisões do Rafael anotadas no próprio documento, com a frase dele.
- Commit neste repo; o que pede código vira sessão no repo certo (`aura-novofront`, `aura-landing`, `aura_api`), nunca editado daqui.

## Fase 0: entrevista (em andamento)

Usa a skill `grilling`: rodadas de perguntas numeradas, cada uma com uma resposta recomendada, até não sobrar decisão em aberto. Os fatos (números, histórico, o que já foi decidido) são levantados por subagentes e não perguntados ao Rafael.

O registro das rodadas fica em `entendimento-compartilhado-2026-11.md`.
