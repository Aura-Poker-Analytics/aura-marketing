# Discord: lançamento do Modo GTO ("GTO em todas as ações")

Status: rascunho com marcadores pendentes; não publicado. Versão de 13/10/2026.
**Tamanho real (len do texto exato dos blocos abaixo, URL e marcadores inclusos, em caracteres Unicode): PT 1.101, EN 1.116. Sem os dois marcadores (46 caracteres): PT 1.055, EN 1.070. Teto de 1.200 respeitado nos dois.** Recontar se qualquer palavra mudar. 3 emojis funcionais: 📊 título, 🔎 convite, 👉 CTA.
**Aviso de publicação: só postar depois do teste logado do Rafael, do P-61 no ar (Modo GTO aberto ao Individual), da confirmação do preço no checkout pela HUB e da confirmação dos marcadores.** O link leva ao app e o texto promete o módulo.
Marcadores a tirar antes de postar: `[[CONFIRMAR-COBERTURA]]` (cobertura "em todas as ações do pós-flop", pendente da HUB) e `[[CONFIRMAR-PREFLOP]]` (pré-flop, confirmar se mudou).
Números: de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10), exemplo (a): field 46,0%, GTO 38,8% (faixa 37,1–40,4%), 5,6 pp acima do topo da faixa. A HUB deve reconfirmá-los no snapshot de produção de 13/10. Nenhum outro número.
O CTA é "Conhecer o Modo GTO" / "See GTO Mode"; não promete o GTO de graça. A frase do plano é a decisão do Rafael via HUB (13/10): PT cita "plano Individual (R$ 150/mês)", EN cita "Individual plan (US$ 29/month)", nunca a moeda trocada; "por tempo limitado" sem data. Depende do P-61 no ar e da HUB confirmar que o checkout cobra 29 / 150 hoje. Sem plano Modo GTO à parte, sem Top, sem desconto semestral/anual.
@aurapokeranalytics: a confirmar pelo Rafael. UTM: `utm_campaign=modo-gto-launch`, uma URL por idioma.

---

## PT

```
📊 **Novo na Aura: Modo GTO**

[[CONFIRMAR-COBERTURA]] O GTO em todas as ações do pós-flop: flop, turn e river, inclusive as aberturas do agressor (c-bet, second barrel, probe). Cada ação mostra o número GTO e a faixa GTO ao lado do field.

**Exemplo**
CO × BB em pote simples, 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado. Contra o c-bet de 33%, o field folda 46,0% e o GTO 38,8% (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. É um spot, não a média do field.

**Como usar**
Escolha o spot, clique em Apply e veja o field e o GTO juntos. A cada clique, o app mostra o que falta para ver o GTO.

[[CONFIRMAR-PREFLOP]] Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

🔎 Abra um spot que você joga e olhe o gap.

O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF.
Ferramenta de estudo. 18+.
👉 Conhecer o Modo GTO: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt
```

## EN

```
📊 **New on Aura: GTO Mode**

[[CONFIRMAR-COBERTURA]] GTO in every postflop action: flop, turn and river, including the aggressor's openings (c-bet, second barrel, probe). Each action shows the GTO number and the GTO range next to the field.

**Example**
CO × BB single-raised pot, 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop. Facing a 33% c-bet, the field folds 46.0% and GTO 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. This is one spot, not the field average.

**How to use it**
Pick the spot, hit Apply and see the field and GTO together. At every click, the app shows what is missing to see GTO.

[[CONFIRMAR-PREFLOP]] Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

🔎 Open a spot you play and look at the gap.

GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison.
Study tool. 18+.
👉 See GTO Mode: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en
```

---

## Notas
- Sem exemplo de abertura (N7 a N10) no Discord: um exemplo só, para caber no teto. O exemplo de abertura vive no carrossel.
- Sem as frases que limitavam a cobertura ("SRP e 3-bet", "flop e turn", reação a raise só no flop do SRP).
- A ressalva de torneios vanilla fica só na Metodologia do app (pedido do Rafael em 06/10); o Discord não a repete.
- Conferência da contagem, para quem quiser refazer: copiar o texto de cada bloco (sem as cercas ```) para um arquivo sem quebra de linha final e rodar `python -c "import sys;print(len(open(sys.argv[1],encoding='utf-8').read()))" arquivo.txt`. A contagem acima foi feita por regex no arquivo (`📊 \*\*Novo na Aura: Modo GTO\*\*.{0,N}\n```` em modo multilinha e dotall, bisseção de N até o menor que casa: 1.073 depois da 1.ª linha de 28 caracteres no PT; 1.089 depois da 1.ª linha de 27 no EN), porque esta sessão não tinha Python. `\n` conta 1 caractere.
