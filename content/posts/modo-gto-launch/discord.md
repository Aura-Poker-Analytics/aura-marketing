# Discord: lançamento do Modo GTO (GTO no flop, turn e river)

Status: rascunho sem marcadores abertos; não publicado. Versão de 15/10/2026 (a inclusão do GTO no Individual é a temporária, por tempo limitado; decisão do Rafael via HUB), números fechados em 14/10.
**Tamanho real (len do texto exato dos blocos abaixo, URL inclusa, `\n` = 1 caractere, emoji = 1 caractere): PT 1.108, EN 1.150. Teto de 1.200 respeitado nos dois, com folga de 92 e 50 caracteres (contando cada emoji como 2, UTF-16, ficam 1.111 e 1.153).** A contagem de 15/10 foi refeita à mão (deltas sobre a contagem linha a linha anterior), porque esta sessão não tinha Python nem shell; **recontar por regex ou `len()` antes de postar** (comando em Notas). 3 emojis funcionais: 📊 título, 🔎 convite, 👉 CTA.
**Aviso de publicação: só postar depois do teste logado do Rafael, do P-61 no ar (Modo GTO aberto ao Individual), da conferência do preço no Stripe pelo Rafael, do GATE B1 (data interna a honrar e reconciliação da landing publicada, sessão do aura-landing) e do GATE A2 (a frase da conta grátis só fica se o teste logado confirmar).** O link leva ao app e o texto promete o módulo.
Números: exemplo (a) de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10): field 46,0%, GTO 38,8% (faixa 37,1–40,4%), 5,6 pp acima do topo da faixa. A cobertura segue `aura-main/_ops/golive-gto-2026-10-14/numeros-verificados-lancamento.md` (14/10). Preço: US$ 29/mês (EN) e R$ 150/mês (PT) são o preço do plano Individual, do checkout (HUB), a conferir no Stripe. Nenhum outro número.
O CTA é "Conhecer o Modo GTO" / "See GTO Mode"; não promete o GTO de graça. A frase do plano é a decisão do Rafael via HUB (13 e 15/10): PT "O Modo GTO está incluso no plano Individual (R$ 150/mês) por tempo limitado." e EN "GTO Mode is included in the Individual plan (US$ 29/month) for a limited time.", nunca a moeda trocada; o temporário é a inclusão do GTO no Individual, não o preço; "por tempo limitado" sem data, sem preço travado, sem promessa de que quem assina agora mantém o GTO, sem preço futuro. Sem plano Modo GTO à parte, sem Top, sem desconto semestral/anual.
@aurapokeranalytics: a confirmar pelo Rafael. UTM: `utm_campaign=modo-gto-launch`, uma URL por idioma.

---

## PT

```
📊 **Modo GTO no ar**

GTO no flop, no turn e no river. No flop, a reação ao c-bet e ao raise. No turn e no river, também a frequência de aposta do agressor (second barrel, delayed c-bet, probe no turn, third barrel). Ao lado do field, o número GTO e a faixa GTO.

**Exemplo**
CO × BB em pote simples, 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado. Contra o c-bet de 33%, o field folda 46,0% e o GTO 38,8% (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa. É um spot, não a média do field.

**Como usar**
Escolha o spot, clique em Apply e veja o field e o GTO juntos. A faixa de status do app guia cada clique até ter GTO.

Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb.

🔎 Abra um spot que você joga e olhe o gap.

O Modo GTO está **incluso no plano Individual (R$ 150/mês) por tempo limitado.** A conta grátis segue com o field e a comparação com o MDF.
Ferramenta de estudo. 18+.
👉 Conhecer o Modo GTO: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt
```

## EN

```
📊 **GTO Mode is live**

GTO on the flop, turn and river. On the flop, the response to the c-bet and to the raise. On the turn and river, also the aggressor's betting frequency (second barrel, delayed c-bet, turn probe, third barrel). Next to the field, the GTO number and the GTO range.

**Example**
CO × BB single-raised pot, 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop. Facing a 33% c-bet, the field folds 46.0% and GTO 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range. This is one spot, not the field average.

**How to use it**
Pick the spot, hit Apply and see the field and GTO together. The app's status bar guides each click until GTO is there.

Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb.

🔎 Open a spot you play and look at the gap.

GTO Mode is **included in the Individual plan (US$ 29/month) for a limited time.** The free account keeps the field and the MDF comparison.
Study tool. 18+.
👉 See GTO Mode: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en
```

---

## Notas
- Sem exemplo de abertura no Discord: um exemplo só, para caber no teto. O exemplo de abertura (Turn Delayed CBet) e o Second Barrel vivem no carrossel.
- Sem "todas as ações", sem o c-bet do flop, o donk nem o probe do river como feature.
- A ressalva de torneios vanilla fica só na Metodologia do app (pedido do Rafael em 06/10); o Discord não a repete.
- A inclusão do GTO no Individual é a temporária. Sem promessa de preço travado, de que quem assina agora mantém o GTO, de preço futuro ou plano GTO à parte, e sem data. Se a data interna for combinada (GATE B1), ela entra aqui e nas demais peças ao mesmo tempo.
- Mudanças de 15/10 frente à versão de 13/10: título "Modo GTO no ar" / "GTO Mode is live" (antes "Novo na Aura: Modo GTO" / "New on Aura: GTO Mode"); a frase do plano diz "incluso no plano Individual (preço) por tempo limitado", em negrito (revisão de 15/10); no EN, "The app's status bar guides each click until GTO is there" (antes "…you, click by click, until GTO is there") para caber no teto.
- Conferência da contagem: copiar o texto de cada bloco (sem as cercas) para um arquivo sem quebra de linha final e rodar `python -c "import sys;print(len(open(sys.argv[1],encoding='utf-8').read()))" arquivo.txt`. Se o Windows gravar `\r\n`, a contagem sobe 1 por linha: normalizar para `\n`. Parcial da contagem manual (PT): título 20, parágrafo de cobertura 240, exemplo 265, uso 117, pré-flop 84, convite 43, plano 139, rodapé 26, CTA 135 (sem URL: 23 + 112).
