# aura-marketing

Repositório de **marketing e marca** do Aura Poker Analytics.

Centraliza estratégia, identidade visual, templates e conteúdo de campanha — separado do app (`aura-novofront`) e da landing (`aura-landing`).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `docs/00-strategy/` | Plano de marketing, posicionamento, ICP |
| `docs/01-instagram/` | Estratégia IG, calendário, pilares, hashtags |
| `docs/02-paid/` | Estratégia de tráfego pago (fase 2) |
| `docs/03-analytics/` | KPIs, reviews semanais de métricas |
| `brand/` | **brand-kit.md** (fonte da verdade de marca), logos, fontes |
| `instagram/templates/` | Templates HTML parametrizáveis (render → screenshot) |
| `instagram/copy/` | Legendas versionadas (PT+EN) |
| `instagram/output/` | Artes finais por lote: `AAAA-MM-DD-slug/` |
| `assets/` | Exports compartilhados (logos, paleta, fontes) |
| `content/` | Briefs e materiais textuais multi-canal |

## Operação

- **QG estratégico** (thread de marketing): estratégia, calendário, aprovações — ver `docs/00-strategy/plano-marketing-launch-2.0.md`.
- **Fábrica de posts** (sessão dedicada neste repo): produz lotes via Workflow (dado verificado → copy → render → QA compliance).
- **Rafael (PO)** aprova post a post e publica/agenda no Meta Business Suite. **Nenhum agente publica nada.**
- Regra de ouro: todo número em post é puxado na hora de fonte verificada (ver plano, §Regra de ouro).

## Convenções

- Preferir formatos editáveis (`.svg`, `.html` source) junto com exports finais (`.png`, `.pdf`).
- Nomear arquivos em kebab-case: `logo-icon-dark.svg`, `2026-07-06-pool-overfold-btn/`.
- Não commitar credenciais, tokens de ads ou dados de clientes.
