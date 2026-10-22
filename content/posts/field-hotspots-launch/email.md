# E-mail: lançamento do Field Hotspots

Status: rascunho; **não enviado**, nada criado no Resend. Versão de 22/10/2026. Formato curto, no padrão da versão A de `content/posts/modo-gto-launch/email-versoes-wow.md`: promessa em uma frase, um spot concreto com a ação, FOMO só com fato, botão para a landing. Sem frase que explica a interface, sem bastidor, sem "pp", "a Aura" no feminino, "field" e nunca "pool".
Números de `numeros-verificados.md` (mapa em `copy.md`); nenhum `[NUM]` resta. **Só enviar depois** do merge do Field Hotspots (aura-novofront#169), do olho logado do Rafael e, de preferência, antes da primeira troca de spots (02/11), porque o exemplo é o spot da semana de 22/10 (ver `copy.md`, Pendência 2). Envio e lista são do Rafael.

---

## PT

**Assunto, opção 1:** Field Hotspots: onde o field mais erra
**Assunto, opção 2:** UTG vs BB, 25bb: o field defende demais
**Recomendado: opção 2.** Tem spot e diagnóstico no assunto (tom de reg), e a opção 1 fica para a linha de abertura.
**Preheader:** Field Hotspots no ar. Dois spots novos toda segunda.

**Corpo (texto)**

Field Hotspots no ar
Onde o field mais se afasta do GTO, spot a spot.

Os spots pós-flop de MTT em que o field mais erra, já discriminados: posições, stack, flop, size de c-bet e a ação para explorar.

UTG vs BB, 25bb, SRP, flop A♠ 3♠ 6♥ (A-high two-tone, OESD possível). Contra o c-bet de 50%, o field folda 53,8% e o GTO folda 73,5%: 19,7% abaixo. O BB defende demais contra c-bet. Blefe menos e aposte mais por value.

O Modo GTO libera 8 spots. O Grátis vê 1. Toda segunda, 2 saem e 2 entram, e o que sai não volta igual. O reg do lado pode estar vendo.

Botão: Abrir o Field Hotspots
Sob o botão: Primeira troca de spots: segunda, 02/11. Poker é jogo de habilidade e estudo. 18+.

---

## EN

**Subject, option 1:** Field Hotspots: where the field leaks most
**Subject, option 2:** UTG vs BB, 25bb: the field overdefends
**Recommended: option 2.** Spot and diagnosis in the subject (reg-to-reg tone); option 1 becomes the opening line.

**Preheader:** Field Hotspots is live. Two new spots every Monday.

**Body (text)**

Field Hotspots is live
Where the field strays most from GTO, spot by spot.

The postflop MTT spots where the field leaks most, already itemized: positions, stack, flop, c-bet size and the action to exploit it.

UTG vs BB, 25bb, SRP, A♠ 3♠ 6♥ flop (A-high two-tone, possible OESD). Facing a 50% c-bet, the field folds 53.8% and GTO folds 73.5%: 19.7% below. The BB defends too much against the c-bet. Bluff less and bet more for value.

GTO Mode unlocks 8 spots. Free sees 1. Every Monday, 2 leave and 2 come in, and what leaves doesn't come back the same. The reg next to you might be looking.

Button: Open Field Hotspots
Under the button: First spot swap: Monday, Nov 2. Poker is a game of skill and study. 18+.

---

## Nota técnica

- **Link do CTA (botão para a landing, nunca o app/login; `www.aurapoker.com` com www):**
  - PT: https://www.aurapoker.com?utm_source=email&utm_medium=email&utm_campaign=field-hotspots-launch&utm_content=pt
  - EN: https://www.aurapoker.com?utm_source=email&utm_medium=email&utm_campaign=field-hotspots-launch&utm_content=en
- **Descadastro:** placeholder `{{{RESEND_UNSUBSCRIBE_URL}}}` no rodapé, substituído pelo Resend no envio.
  - Rodapé PT: "Você recebe este e-mail porque tem uma conta ou lista de espera da Aura. Cancelar inscrição: {{{RESEND_UNSUBSCRIBE_URL}}}. Ferramenta de estudo. 18+."
  - Footer EN: "You are receiving this email because you have an Aura account or waitlist spot. Unsubscribe: {{{RESEND_UNSUBSCRIBE_URL}}}. Study tool. 18+."
- **Imagem (opcional, 600px, mockup do produto):** o card do spot da semana (UTG vs BB, 25bb, rótulo Overdefend, barras Field × GTO com N1 e N2, caixa Como explorar), renderizado pela build com os números confirmados, no formato do idioma (PT com vírgula, EN com ponto). Sem lista de 8 spots e sem números fora do `numeros-verificados.md`. **Alt text:** PT "Card do Field Hotspots para o spot UTG vs BB a 25bb em SRP, flop A-high two-tone: fold do field contra o do GTO, rótulo Overdefend e a caixa Como explorar: blefe menos e aposte mais por value." / EN "Field Hotspots card for the UTG vs BB spot at 25bb in an SRP, A-high two-tone flop: field fold against GTO fold, an Overdefend label and the How to exploit box: bluff less and bet more for value."
- **Layout:** 600px, tabelas, estilos inline, preheader oculto, botão âmbar `#D4A418`, linha de canais (Discord, WhatsApp, YouTube) e 18+ no rodapé, igual ao e-mail do Modo GTO.
- **Botão:** "Abrir o Field Hotspots" / "Open Field Hotspots". A frase sob o botão não cita preço; só a data da primeira troca, que é fato do calendário (segunda, 02/11).
- **FOMO usado, todo verdadeiro:** 8 spots no Modo GTO contra 1 no Grátis; rotação semanal (2 entram, 2 saem; o que sai não volta igual, fato confirmado na regra `pvg-release-v1`, Pendência 3 do `copy.md`); "o reg do lado pode estar vendo" (com "pode"). Fora: contador, "só X vagas", afirmação de que outros jogadores usam a Aura.
- **Reply-to:** o e-mail não pede resposta; manter `manager@aurapoker.com` como nos anteriores. Confirmar antes do envio.
- **Não enviado.** Envio e lista são do Rafael.

---

## Build e hospedagem das imagens (22/10, fábrica de posts)

- `email-pt.html` e `email-en.html` (envio) e `.preview.html` (caminho relativo `email/`) saem de `instagram/src/build_email.py`, no padrão do Modo GTO. Assunto recomendado (opção 2) em `<title>`; preheader oculto; CTA com os UTMs da nota técnica; descadastro `{{{RESEND_UNSUBSCRIBE_URL}}}`. `numbers.json` foi preenchido em 22/10 com `numeros-verificados.md` §2 (53,8% / 73,5% / 19,7% abaixo), então o HTML e a imagem saem sem `[NUM]`, sem faixa de rascunho e sem `[DRAFT]` no `<title>`; se algum número voltar a faltar, o marcador vermelho e a faixa "RASCUNHO · NÃO ENVIAR" reaparecem.
- Imagens: `email/field-hotspots-pt.png` e `email/field-hotspots-en.png` (1200 px, card do spot renderizado pela build, sem print da tela e sem lista de 8 spots).
- **Pendência de hospedagem (aura-landing):** o HTML de envio referencia `https://www.aurapoker.com/email/field-hotspots-pt.png` e `.../field-hotspots-en.png`, o mesmo esquema do Modo GTO (`modo-gto-pt.png`, aura-landing#25). Os dois PNGs precisam ser versionados em `public/email/` do aura-landing e estar no ar, conferidos por sha256, antes de qualquer envio. Hoje essas URLs não existem. Os PNGs de `email/` já foram gerados com os números verificados.
- Antes do envio: conferir `instagram/src/numbers.json` contra o `numeros-verificados.md`, rodar `python build_email.py && python qa.py`, hospedar as imagens e só então criar o rascunho no Resend (envio e lista são do Rafael).
