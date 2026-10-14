# Discord: lançamento do Modo GTO (GTO no flop, turn e river)

Status: rascunho sem marcadores abertos; não publicado. Versão de 13/10/2026, números fechados em 14/10.
**Tamanho real (len do texto exato dos blocos abaixo, URL inclusa, em caracteres Unicode): PT 1.110, EN 1.156. Teto de 1.200 respeitado nos dois.** Recontar se qualquer palavra mudar. 3 emojis funcionais: 📊 título, 🔎 convite, 👉 CTA.
**Aviso de publicação: só postar depois do teste logado do Rafael, do P-61 no ar (Modo GTO aberto ao Individual) e da conferência do preço no Stripe pelo Rafael.** O link leva ao app e o texto promete o módulo.
Números: exemplo (a) de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10): field 46,0%, GTO 38,8% (faixa 37,1–40,4%), 5,6 pp acima do topo da faixa. A cobertura segue `aura-main/_ops/golive-gto-2026-10-14/numeros-verificados-lancamento.md` (14/10). Nenhum outro número.
O CTA é "Conhecer o Modo GTO" / "See GTO Mode"; não promete o GTO de graça. A frase do plano é a decisão do Rafael via HUB (13/10): PT cita "plano Individual (R$ 150/mês)", EN cita "Individual plan (US$ 29/month)", nunca a moeda trocada; "por tempo limitado" sem data. Sem plano Modo GTO à parte, sem Top, sem desconto semestral/anual.
@aurapokeranalytics: a confirmar pelo Rafael. UTM: `utm_campaign=modo-gto-launch`, uma URL por idioma.

---

## PT

```
📊 **Novo na Aura: Modo GTO**

GTO no flop, no turn e no river. No flop, a reação ao c-bet e ao raise. No turn e no river, também a frequência de aposta do agressor (second barrel, delayed c-bet, probe no turn, third barrel). Ao lado do field, o número GTO e a faixa GTO.

**Exemplo**
CO × BB em pote simples, 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado. Contra o c-bet de 33%, o field folda 46,0% e o GTO 38,8% (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. É um spot, não a média do field.

**Como usar**
Escolha o spot, clique em Apply e veja o field e o GTO juntos. A faixa de status do app guia cada clique até ter GTO.

Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

🔎 Abra um spot que você joga e olhe o gap.

O Modo GTO faz parte do plano Individual (R$ 150/mês) por tempo limitado. A conta grátis segue com o field e a comparação com o MDF.
Ferramenta de estudo. 18+.
👉 Conhecer o Modo GTO: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt
```

## EN

```
📊 **New on Aura: GTO Mode**

GTO on the flop, turn and river. On the flop, the response to the c-bet and to the raise. On the turn and river, also the aggressor's betting frequency (second barrel, delayed c-bet, turn probe, third barrel). Next to the field, the GTO number and the GTO range.

**Example**
CO × BB single-raised pot, 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop. Facing a 33% c-bet, the field folds 46.0% and GTO 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. This is one spot, not the field average.

**How to use it**
Pick the spot, hit Apply and see the field and GTO together. The app's status bar guides you, click by click, until GTO is there.

Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

🔎 Open a spot you play and look at the gap.

GTO Mode is part of the Individual plan (US$ 29/month) for a limited time. The free account keeps the field and the MDF comparison.
Study tool. 18+.
👉 See GTO Mode: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en
```

---

## Notas
- Sem exemplo de abertura no Discord: um exemplo só, para caber no teto. O exemplo de abertura (Turn Delayed CBet) vive no carrossel.
- Sem "todas as ações", sem o c-bet do flop, o donk nem o probe do river como feature.
- A ressalva de torneios vanilla fica só na Metodologia do app (pedido do Rafael em 06/10); o Discord não a repete.
- Conferência da contagem, para quem quiser refazer: copiar o texto de cada bloco (sem as cercas) para um arquivo sem quebra de linha final e rodar `python -c "import sys;print(len(open(sys.argv[1],encoding='utf-8').read()))" arquivo.txt`. A contagem acima foi feita por regex no arquivo (`📊 \*\*Novo na Aura: Modo GTO\*\*.{0,N}\n` e a cerca de fechamento, em modo multilinha e dotall, bisseção de N até o menor que casa: 1.082 depois da 1.ª linha de 28 caracteres no PT; 1.129 depois da 1.ª linha de 27 no EN), porque esta sessão não tinha Python. `\n` conta 1 caractere.
