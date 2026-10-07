# E-mail: lançamento do Field Trends

Status: rascunho para aprovação do Rafael. Não enviado.
Números usados (todos de `aura-main/_ops/field-trends-launch/numeros-verificados.md`, versão de 07/10): 114 stats (§3), 23 das 114 com variação significativa em 1 ano (§6), Fold to IP Flop CBet 43,62% (2T25) para 44,99% (2T26 em curso), +1,36 pp, faixa ± 0,77 (§4), 11 trimestres até o 2T26 (§2). Sem pré-flop, sem filtro por buy-in, sem selo de fase nem pedido de feedback.
HTML pronto: `email-pt.html` e `email-en.html` (mesma pasta). Para abrir do disco: `email-pt.preview.html` e `email-en.preview.html`.

---

## PT

**Assunto (2 opções)**
1. Novo módulo na Aura: Field Trends
2. O field mudou. O seu exploit ainda vale?

**Recomendado: a 1** (mudou em 07/10, pedido do Rafael: tudo com apelo de anúncio de novo módulo). O assunto anuncia o módulo pelo nome; a pergunta "o field mudou" abre o corpo logo depois. A 2 fica como alternativa se o Rafael preferir abrir pela pergunta. (O `<title>` do HTML usa a 1.)

**Preheader:** Novo módulo na Aura: Field Trends. Acompanhe, trimestre a trimestre, como o field muda.

**Corpo (texto)**

Novo módulo na Aura: Field Trends
Acompanhe como o field muda, trimestre a trimestre.

O field mudou, e o seu exploit ainda vale? O Field Trends mostra 114 stats do pós-flop trimestre a trimestre (c-bet, fold to c-bet, donk, probe e mais) e destaca só o que mudou de verdade: no último ano, 23 das 114 tiveram variação significativa.

Cada stat traz a faixa de variação normal do próprio field. Se a mudança passa da faixa, o field mudou. Dentro da faixa, é variação normal.

Exemplo: o fold to c-bet IP no flop foi de 43,62% (2T25) para 44,99% (2T26 em curso), acima da faixa de ± 0,77 pp. Mudança real, e pequena. No field inteiro, o fold to c-bet IP subiu 1,36 pp, então em média o c-bet de bluff IP tem um pouco mais de fold equity. Confira no seu spot.

Dados: Aura · 11 trimestres, até o 2T26 (em curso)

Botão: Acesse grátis
Sob o botão: A conta grátis abre uma prévia do Field Trends; as variações significativas, os filtros e a lista completa de stats são dos planos pagos. Poker é jogo de habilidade e estudo. 18+.

---

## EN

**Subject (2 options)**
1. New module on Aura: Field Trends
2. The field changed. Does your exploit still hold?

**Recommended: 1** (changed on Oct 7, Rafael's request: everything with a new-module announcement appeal). The subject announces the module by name; the "the field changed" question opens the body right after. Option 2 stays as the alternative if Rafael prefers to open with the question. (The HTML `<title>` uses 1.)

**Preheader:** New module on Aura: Field Trends. Follow, quarter by quarter, how the field changes.

**Body (text)**

New module on Aura: Field Trends
Follow how the field changes, quarter by quarter.

The field changed, does your exploit still hold? Field Trends shows 114 postflop stats quarter by quarter (c-bet, fold to c-bet, donk, probe and more) and highlights only what really changed: over the past year, 23 of the 114 had a significant change.

Each stat carries the normal variation band of its own field. If the move passes the band, the field changed. Inside the band, it is normal variation.

Example: the IP flop fold to c-bet went from 43.62% (2Q25) to 44.99% (2Q26 in progress), above the ± 0.77 pp band. A real change, and a small one. Across the whole field, the IP fold to c-bet rose 1.36 pp, so on average the IP bluff c-bet has a little more fold equity. Check it in your own spot.

Data: Aura · 11 quarters, through 2Q26 (in progress)

Button: Get free access
Under the button: The free account opens a Field Trends preview; the significant changes, filters and the full stat list are on paid plans. Poker is a game of skill and study. 18+.

---

## Nota técnica

- **Imagem:** mockup do Field Trends (`email/field-trends-pt.png` e `-en.png`), logo abaixo do texto e antes do botão. **Os PNGs já existem** em `email/` desta pasta, com 1200x1152 px; o HTML os exibe a 552 px com `width="552" height="530"` (1152 x 552 / 1200 = 530) e `height:auto` no estilo, nos dois HTML de cada idioma (`email-pt.html`, `email-en.html` e os `*.preview.html`). Se a fábrica gerar de novo com outra proporção, ajustar o `height` nos 4 arquivos. Hospedar em `https://www.aurapoker.com/email/` antes do envio. O mockup mostra, no máximo, números de `numeros-verificados.md` (o Fold to IP Flop CBet, 43,62% para 44,99%, é o que o texto cita), sem selo de fase. Os `*.preview.html` usam o caminho relativo `email/` para abrir do disco.
- **Logo:** `https://www.aura.poker/email/aura-logo.png` (já hospedado).
- **Link do CTA (sempre a landing, nunca o app/login; `www.aurapoker.com` com www):**
  - PT: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=field-trends-launch&utm_content=pt
  - EN: https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=field-trends-launch&utm_content=en
  - Só o logo continua hospedado em `https://www.aura.poker/email/` (padrão dos e-mails existentes); não é link de destino.
- **Descadastro:** placeholder `{{{RESEND_UNSUBSCRIBE_URL}}}` no rodapé, substituído pelo Resend no envio.
- **Layout:** 600px, tabelas, estilos inline, preheader oculto, botão âmbar `#D4A418`, linha de canais (Discord, WhatsApp, YouTube) e 18+ no rodapé, igual ao e-mail do Field Ranges.
- **2T26 em curso:** a fonte exige a marca "(em curso)" em todo número com 2T26; ela está no exemplo ("44,99% (2T26 em curso)") e na linha "Dados".
- **Aviso de lançamento (estado real, conforme `aura-main/_ops/field-trends-launch/roteiro-release.md` §8, 07/10):** banco (promote na Azure, `--verify` ok), API (publish `deploy-4d370aa.zip` e app setting `FieldTrends__ExcludedQuarters__0`) e flag (#86 mesclado, `792e1b8`, bundle `index-BdNKbc3s.js` com `isFieldTrendsEnabled` verdadeiro) **já foram executados em 07/10**, e o smoke anônimo deu 401 nas rotas esperadas. **Falta o smoke logado com conta paga, que o roteiro deixa com o Rafael.** O §8 também não registra o smoke com conta Grátis (previsto no §6). Enviar só depois do smoke do Rafael; o botão leva à landing, mas o texto promete o módulo.
- **Frase sob o botão (B2):** diz a verdade sobre o Grátis, que abre só uma prévia (IP Flop CBet com buy-in até US$ 22); as variações significativas, os filtros e a lista completa são dos planos pagos. O botão segue "Acesse grátis", pedido do Rafael.
- **Sem a frase "o exploit segue de pé" (A1):** a leitura do exemplo é a do field inteiro ("em média ... Confira no seu spot"), não promessa sobre o exploit do leitor.
- **Reply-to:** o e-mail não pede resposta, mas o remetente continua sendo o do padrão anterior (`manager@aurapoker.com` como reply-to). Confirmar antes do envio.
- **Não enviado.** Envio e lista são do Rafael.
