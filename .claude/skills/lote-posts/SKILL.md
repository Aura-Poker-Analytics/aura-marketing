---
name: lote-posts
description: Produz um lote semanal de posts/reels da Aura Poker Analytics seguindo o brand-kit, o calendário/fila de conteúdo e os anti-padrões de compliance do repo. Usar quando o Rafael pedir "lote de posts", "fábrica de posts" ou "conteúdo da semana".
---

# Lote de posts — fábrica semanal

## Ler primeiro (caminhos reais, não repetir conteúdo aqui)
- `brand/brand-kit.md` — fonte da verdade de marca: paleta, tipografia, tom de voz (PROIBIDO tom guru/get-rich).
- `docs/00-strategy/plano-marketing-launch-2.0.md` — pilares, regra de ouro dos números (§C) e checklist de compliance por post (§Compliance).
- `content/posts/README.md` e `content/reels/README.md` — biblioteca única: o que já está em `Posted/`, o que foi rejeitado em `Alterar/`, e a fila pronta.
- `docs/02-paid/calendario-organico-30d.md` — último calendário datado publicado (pode estar vencido; tratar como referência de cadência, não como fila viva).
- `instagram/templates/*.html` + `instagram/templates/deck.js` — templates de render.
- `C:\Users\Rafael\Documents\GitHub\lastro\docs\poker-i18n.json` — vocabulário/termos de poker para consistência PT/EN entre repos.
- `brand/brand.yaml` (marca da Aura; enquanto não existir, o `brand/brand-kit.md`), `voz-grinder` e `copywriting`, quando fizerem sentido para o tema.

## Entrada esperada
Tema ou feature a divulgar, quantidade de peças, idiomas (PT, EN ou ambos — o padrão do repo é bilíngue).

## Passos
1. **Checar repetição.** Ler `content/posts/README.md` (seção `Posted/`) e `content/reels/README.md` (coluna status) antes de propor ângulo ou slug — nunca reaproveitar um slug ou ângulo já publicado sem que o Rafael peça explicitamente.
2. **Gerar rascunhos de copy.** Usar `brand.yaml` (ou o `brand-kit.md`) para o tom, `voz-grinder` para texto de poker ao jogador e `copywriting` para estrutura persuasiva + o vocabulário de `poker-i18n.json` do lastro para termos técnicos consistentes entre os produtos do ecossistema. Todo número no post precisa de fonte verificada (regra de ouro, §C do plano) ou vai rotulado "ilustrativo".
3. **Salvar por peça.** Cada peça vira uma pasta em `content/posts/<slug>/` (card) ou `content/reels/reel-NN-<slug>/` (reel), com `copy.md` (PT+EN) — seguindo a convenção kebab-case já usada no repo. Não mover nada de/para `Posted/` ou `Alterar/`: essa triagem é do Rafael.
4. **Nunca renderizar vídeo frame a frame dentro da sessão.** Gerar o roteiro (`roteiro.md`) e o script de render (baseado nos `instagram/build-*.mjs` existentes); disparar o render real por Bash em **background**, com saída redirecionada a arquivo, e só relatar quando terminar.
5. **Fechar o lote.** Listar todos os arquivos criados nesta sessão e marcar explicitamente o que precisa de aprovação visual do Rafael antes de ir para `Posted/`.

## Regras fixas
- Publicação é sempre manual do Rafael — nenhum agente publica ou agenda no Meta Business Suite.
- Rodar o checklist de compliance (§Compliance do plano) em cada peça antes de listá-la como pronta.
- Modelo sugerido: Sonnet. Sessão descartável por lote — não precisa persistir entre lotes.
