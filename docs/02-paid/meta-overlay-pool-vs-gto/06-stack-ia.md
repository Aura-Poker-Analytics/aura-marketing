# 06 · Stack de IA, fluxo de produção e prompts prontos

Preços pesquisados em 22/09/2026 nas páginas oficiais, quando o fetch funcionou; o resto veio de fontes secundárias e está marcado. Câmbio de referência: R$ 5,40/US$. **Confira o preço no dia da compra.**

**Princípio:** a IA produz o apresentador, a voz e o b-roll. **Ela nunca produz a tela do produto.** Uma interface gerada por IA mostrada como se fosse a Aura seria propaganda enganosa (CDC art. 37) e quebra a regra "tela real é a estrela". A tela sai sempre de gravação real ou de mockup fiel, dito como mockup.

## 1. Comparativo

### Avatar e apresentador

| Ferramenta | Plano que serve | US$/mês | PT-BR | Avatar próprio e consentimento | Limite que pesa |
|---|---|---:|---|---|---|
| **HeyGen** (recomendado) | Creator | 29 | bom (TTS + lip-sync nativos) | avatar a partir de foto ou vídeo; pessoa real exige vídeo de consentimento dela | ~10 min de avatar premium por mês no Creator; Pro (US$ 99) dá 4K e mais minutos |
| Synthesia | Starter / Creator | 18–29 / 64–89 | bom | avatar pessoal com verificação de identidade formal | cota anual de minutos rígida |
| Creatify | Starter / Pro | 39 / 99 | foco em UGC | 3 avatares próprios no Pro | créditos expiram em 2 meses; empurra estética UGC, que não é a da marca |
| Arcads | Starter (não confirmado) | ~110 | não detalhado | clonagem só no Pro/API | sem página de preço; atores "UGC" parecem depoimento, **risco de compliance** |
| Captions (AI Twin) | Max | 24,99 | bom em legenda | só clone do próprio usuário | é clone de pessoa, não personagem |
| Hedra | Creator | 30 | depende do TTS | sem processo público de consentimento | bom lip-sync a partir de foto |
| D-ID | Lite → Advanced | 5–196 | ok | anunciante responde pela imagem | feito para agente conversacional |

### Vídeo e b-roll

| Ferramenta | Plano | US$/mês | Uso comercial | Nota |
|---|---|---:|---|---|
| **Kling** (recomendado para volume) | Standard | 10 | sim, a partir do Standard (o Free proíbe) | a entrada comercial mais barata |
| Runway Gen-4/4.5 | Standard / Pro | 12 / 28 | sim nos pagos | mais controle de câmera |
| Google Veo 3 | AI Pro / Ultra | 19,99 / 249,99 | sim nos pagos | Veo 3 Fast no Pro; o app grátis tem marca d'água |
| Luma | Plus | 30 | sim | b-roll estilizado |
| Sora | API | por segundo | — | app descontinuado em 04/2026; há relato de fim da API em 24/09 (não confirmado). **Não usar como pilar** |

### Voz PT-BR

| Ferramenta | Plano | US$/mês | Nota |
|---|---|---:|---|
| **ElevenLabs** | Starter / Creator | 6 / 22 | comercial a partir do Starter; clonagem profissional no Creator; Multilingual v2 tem PT-BR e PT-PT separados; Voice Design gera voz a partir de descrição |
| Azure / Google TTS | por caractere | — | previsível e sem ambiguidade de licença; menos natural |

### Edição, legenda e tela

| Ferramenta | Plano | US$/mês | Armadilha |
|---|---|---:|---|
| **CapCut** | Pro | ~20 | a licença comercial cobre o seu vídeo, **não a música do banco do CapCut**: não usar essa música em anúncio pago |
| Submagic | Pro | 39 (23 no anual) | legenda dinâmica; bom para o tier 2 |
| Descript | Creator | ~24–35 | edição por texto |
| Canva | Pro | 18 | capas e variações estáticas |
| **Screen Studio** | assinatura | ~9–29 (não confirmado) | gravação de tela com zoom e cursor bonitos; é a peça mais importante do stack |
| CleanShot X | Pro | ~8 | stills e GIFs |
| Rotato | anual | ~4 | mockup 3D de notebook/celular |

## 2. Recomendação

**Tier 1, ~US$ 100/mês (~R$ 540): Fases 0 e 1.**
HeyGen Creator (29) + ElevenLabs Starter (6) + Kling Standard (10) + CapCut Pro (20) + Screen Studio (~29) + CleanShot X (~8) ≈ US$ 102.

**Tier 2, ~US$ 300/mês (~R$ 1.600): Fase 2, com a cadência da F2-D (3 criativos novos por semana).**
HeyGen Pro (99) + ElevenLabs Creator (22) + Kling Pro (37) + Runway Standard (12) + Submagic Pro (39) + Screen Studio (~29) + Canva Pro (18) + Rotato (~4) + CleanShot (~8) ≈ US$ 268.

**Por que não Arcads nem Creatify como base:** os dois são construídos para o formato "ator falando para a câmera como cliente". Nas mãos erradas, esse formato vira depoimento falso, que é proibido aqui. O analista da Aura é um apresentador de marca, com cara de analista, e não de cliente.

## 3. O personagem: "o analista da Aura"

**Bíblia do personagem (colar no brief de qualquer ferramenta):**

- **Quem é:** o apresentador sintético da Aura. Explica dados do field. **Não é jogador, não é cliente, não é coach, não dá depoimento, não fala de resultado financeiro.**
- **Aparência:** adulto de ~30–35 anos, aparência neutra, que não lembra nenhuma pessoa real conhecida. Camiseta escura lisa ou jaqueta slate, sem logo de sala de poker. Luz de estúdio suave, fundo escuro slate-950 com um brilho âmbar discreto.
- **Voz:** PT-BR, tom de analista: calmo, seco, preciso. Ritmo médio. Nada de entusiasmo de vendedor.
- **Frases que usa:** "field", "spot", "o gap", "amostra", "c-bet", "SRP" (jargão em inglês, como a marca).
- **Frases proibidas:** "ganhe", "lucro", "dinheiro", "garantido", "eu uso e…", "meus resultados".
- **Divulgação:** selo `Personagem gerado por IA` no quadro, rótulo de IA ligado no anúncio, e a própria piada do R5 ("Eu sou uma IA").
- **Base de imagem:** gerada do zero ou avatar de estoque da ferramenta. **Nunca** o rosto ou a voz de uma pessoa real sem contrato e consentimento gravado. Se o PO quiser usar a própria imagem, é outro personagem (o fundador), com consentimento dele gravado na ferramenta, e sem o selo de personagem.

### 3.1 Prompt de imagem do personagem (HeyGen "Generate AI Avatar" ou gerador de imagem)

```
Photorealistic portrait of a fictional data analyst, 32 years old, neutral ambiguous features,
short dark hair, calm focused expression, plain dark slate crew-neck t-shirt, no logos, no jewelry.
Studio lighting, soft key light from the left, subtle warm amber rim light.
Background: very dark navy-slate (#0F172A) with a faint out-of-focus amber glow.
Medium shot from chest up, facing camera, vertical 9:16 framing, head in the upper third.
Must not resemble any real celebrity, athlete or poker player.
No playing cards, no poker chips, no casino, no money, no text.
```

### 3.2 Prompt de voz (ElevenLabs → Voice Design)

```
Brazilian Portuguese male voice, early thirties, calm and precise, like a data analyst
explaining a chart to a colleague. Neutral São Paulo accent, medium pace, low energy,
no salesman enthusiasm, clear consonants, slightly warm tone.
```

Configuração sugerida: modelo Multilingual v2, variante **pt-BR**; Stability ~0,55; Similarity ~0,75; Style 0; speaker boost ligado. Gerar três vozes, escolher uma e **nomeá-la "Analista Aura"**, para usar sempre a mesma.

## 4. Roteiros prontos para colar no HeyGen

Configuração do projeto:

- **Formato:** 9:16, 1080×1920.
- **Avatar:** "Analista Aura".
- **Voz:** a do ElevenLabs (integração) ou a voz PT-BR nativa mais próxima.
- **Fundo:** verde chapado. O fundo slate e a tela entram no CapCut.
- **Legenda:** desligada; a legenda é feita no CapCut.
- **Velocidade:** 1,0.

Use `<break time="0.4s"/>` onde houver pausa, se a voz for ElevenLabs; no HeyGen, uma quebra de linha.

**R5 · eu-sou-uma-ia**
```
Eu sou uma IA. Os quinhentos milhões de mãos, não.
<break time="0.4s"/>
Elas são de torneios de verdade, em sete salas. A Aura mede o que o field fez em cada spot.
<break time="0.3s"/>
Agora ela põe o GTO do lado. O que o solver joga, e o que o field joga, no mesmo board.
<break time="0.4s"/>
A diferença tem nome: o gap.
<break time="0.3s"/>
O Modo GTO abre em breve. A lista está no link.
```

**R9 · tres-perguntas**
```
Três perguntas que o seu solver não responde.
<break time="0.4s"/>
Um: o que o field do seu buy-in faz nesse spot. O solver não joga no seu buy-in.
<break time="0.3s"/>
Dois: se o field muda perto da bolha. O solver não sabe em que etapa você está.
<break time="0.3s"/>
Três: quanto o field sai do GTO. Essa é a nova.
<break time="0.4s"/>
As duas primeiras já estão na Aura. A terceira abre em breve. Link na bio.
```

**R10 · deixa-eu-te-mostrar** (preencher ⟨…⟩ com os números da tela gravada no D-1)
```
Deixa eu te mostrar um spot que o field joga diferente do GTO.
<break time="0.3s"/>
Pote single-raised, BTN contra BB, quarenta blinds, board pareado.
<break time="0.4s"/>
O GTO folda ⟨X⟩ por cento. O field folda ⟨Y⟩ por cento. Amostra de ⟨N⟩ mãos.
<break time="0.4s"/>
Esse gap é o que você leva para a mesa.
<break time="0.3s"/>
Modo GTO, novo na Aura. Link na bio.
```

**R12 · as-maos-que-o-field-nao-beta**
```
Essas são as mãos que o field deveria betar aqui. E não beta.
<break time="0.4s"/>
Quanto mais acesa, maior a diferença entre o GTO e o field.
<break time="0.3s"/>
No feed, cada spot vem com as mãos que mudam, em ordem.
<break time="0.3s"/>
E com o valor em bb de explorar.
<break time="0.4s"/>
Field vs GTO, no plano Top. Link na bio.
```

**Versões EN (F1-A, F2-B):** traduzir mantendo o jargão. Na EN, "field" continua "field" e "Modo GTO" vira "GTO Mode". A voz EN precisa de uma segunda voz no ElevenLabs; não usar a PT-BR falando inglês.

## 5. Prompts de b-roll (Kling, Runway ou Veo)

O b-roll só entra **entre** telas reais, como transição ou fundo do apresentador, até 3 s por uso. Todos em 9:16, 5 s, sem texto (texto gerado por IA sai torto; o texto entra no CapCut).

**B1 · linhas de dado (fundo do analista)**
```
Slow dolly-in over a dark navy-slate surface (#0F172A). Thin glowing amber lines draw
themselves left to right, forming two smooth line charts that run parallel and then separate,
leaving a bright amber gap between them. Shallow depth of field, subtle film grain,
cinematic, minimal, no text, no numbers, no playing cards, no chips, no casino. Vertical 9:16.
```

**B2 · grade 13×13 (abertura do R12)**
```
Top-down view of a 13 by 13 grid of dark slate squares on a near-black background.
Squares light up one by one in warm amber with varying intensity, like a heatmap loading.
Smooth, calm, precise motion. No text, no letters, no cards, no chips. Vertical 9:16, 5 seconds.
```

**B3 · transição "field"**
```
Abstract visualization of a large crowd represented as thousands of tiny amber dots on a dark
navy background, drifting slowly and then aligning into a clean horizontal band.
Elegant, data-driven, minimal. No faces, no text, no poker imagery. Vertical 9:16, 5 seconds.
```

**Negativos para qualquer b-roll:** `playing cards, poker chips, casino, roulette, money, coins, dollar signs, luxury, slot machine, dice, text, watermark`.

## 6. Captura da tela real (Screen Studio): checklist

1. Conta de gravação dedicada (grátis e paga), via `dev-login-{paid,free}.html` locais ou login real do PO. **Nunca** conta de cliente.
2. Janela em 1440×900, zoom do navegador em 110%, modo escuro.
3. Esconder menu de conta, e-mail, sino de notificações e qualquer nome de usuário.
4. Um movimento por take: um filtro, um clique, um zoom. Cursor grande, clique com destaque, zoom automático do Screen Studio ligado.
5. Exportar em 4K e recortar para 9:16 no CapCut. A tela ocupa ao menos 60% da altura útil.
6. Para cada número mostrado, tirar um print com `n` visível e guardar ao lado do projeto, como prova de origem do número.
7. Fase 1: tela do Modo GTO ou do Field vs GTO sempre com o selo `prévia do beta`.

## 7. Montagem (CapCut), padrão da marca

- **Legenda:** Montserrat Bold 64–72 px, branca, palavra-chave em âmbar `#FBBF24`, no máximo 2 linhas, centralizada entre 30% e 65% da altura.
- **Rodapé fixo:** `500M+ mãos auditadas · 7 salas · 18+` em Montserrat 28 px, slate-300.
- **Selo de IA:** `Personagem gerado por IA`, Montserrat 26 px, fundo slate-800 a 80%, canto superior esquerdo abaixo dos 250 px, durante o reel inteiro.
- **Áudio:** voz a −14 LUFS. Sem música do banco do CapCut em anúncio pago. Se houver trilha, que seja de biblioteca com licença de anúncio (Artlist, Epidemic ou similar), baixa e sem letra.
- **Exportação:** 1080×1920, 30 fps, H.264, ~12 Mbps. Capa 1080×1920 com o gancho escrito.

## 8. Fluxo de produção de um reel

| Passo | Ferramenta | Tempo |
|---|---|---|
| 1. Escolher o spot e conferir `n` na tela | Aura | 10 min |
| 2. Gravar a tela | Screen Studio | 15 min |
| 3. Gerar a fala do analista (se houver) | ElevenLabs → HeyGen | 10 min + renderização |
| 4. Gerar 1–2 b-rolls (se houver) | Kling | 10 min + renderização |
| 5. Montar, legendar, selo, rodapé | CapCut | 30–40 min |
| 6. Revisão: `07-compliance.md` §1, linha por linha | humano | 10 min |
| 7. Versão EN (texto e voz) | CapCut + ElevenLabs | 20 min |

Cerca de **1h30 por reel PT com analista**, e 1h sem. Os doze da Fase 1 e da Fase 2 cabem em ~2 semanas de meio período.
