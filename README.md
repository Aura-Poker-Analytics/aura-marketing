# aura-marketing

Repositório de **marketing e marca** do Aura Poker Analytics.

Centraliza materiais de comunicação, identidade visual, assets exportáveis e conteúdo de campanha — separado do app (`aura-novofront`) e da landing (`aura-landing`).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `brand/` | Manual de marca, logos, fontes, paleta, templates oficiais |
| `assets/` | Imagens, banners, exports para redes e anúncios |
| `content/` | Copy, briefs, roteiros e materiais textuais de campanha |

## Relação com outros repos

- **`aura-landing`** — site público; consome assets versionados aqui quando aplicável.
- **`aura-novofront`** — app do produto; não compartilha autenticação nem deploy com este repo.
- **`aura-context`** — documentação técnica e de produto; marketing de marca fica aqui.

## Convenções

- Preferir formatos editáveis (`.svg`, `.fig`, source files) junto com exports finais (`.png`, `.pdf`).
- Nomear arquivos em kebab-case: `logo-icon-dark.svg`, `hero-banner-launch.png`.
- Não commitar credenciais, tokens de ads ou dados de clientes.
