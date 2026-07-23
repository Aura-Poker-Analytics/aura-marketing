# Reels — TODOS num lugar só

Antes os roteiros de reel estavam espalhados (`lote-final/reels/` + `acervo-30d/acv-*-reel-*`). Agora ficam **todos aqui**, um por pasta, com PT+EN no mesmo `roteiro.md`.

| id | tema | status | uso | ângulos |
|---|---|---|---|---|
| reel-01-launch | Aura 2.0 no ar | ✅ PRODUZIDO (4 MP4: PT/EN × 4:5/9:16) | org+paid-br / paid-intl | escala, tour |
| reel-02-tour | tour em 20s | 🟡 roteiro | org+paid-br / paid-intl | tour de módulo |
| reel-03-exploit-card | como ler um exploit card | 🟡 roteiro | org+paid-br / paid-intl | postflop, educativo |
| reel-04-bubble | field da bolha (ICM) | 🟡 roteiro | org+paid-br / paid-intl | leak/padrão, mito×real |
| reel-05-caso-uso | grinder ESTUDA um spot | 🟡 roteiro (corrigido) | org+paid-br / paid-intl | caso de uso |

**Convenções**
- Naming estável `reel-NN-slug` (o slug vira `utm_content` se for pro pago).
- Cada `roteiro.md`: tabela cena-a-cena PT+EN, legenda PT, caption EN, procedência dos números.
- Reels novos: gravar tela do app OU montar dos prints em `assets/screenshots/`. Render dos que usam template: pipeline `instagram/` + `deck.js`.
- Sem áudio nos MP4 — trilha entra no editor do IG (biblioteca licenciada).
- MDF sempre descritivo (nunca "abaixo do MDF = leak") — `docs/00-strategy/pesquisa-mdf-limites.md` §10.

**Deletado:** `acv-17-reel-mito-mdf` (era redundante com o card `acv-10-mito-mdf`). O ângulo mito×MDF vive no card; se quiser versão reel, parte do reel-03/reel-05.
