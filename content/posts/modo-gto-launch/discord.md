# Discord: lançamento do Modo GTO

Status: rascunho com números fechados; não publicado.
**Tamanho real (len do texto exato dos blocos abaixo, URL inclusa, em caracteres Unicode como o `len` do Python): PT 1.029, EN 1.066. Teto de 1.200 respeitado nos dois.** Recontar se qualquer palavra mudar. 3 emojis funcionais: 📊 título, 🔎 convite, 👉 CTA.
**Aviso de publicação: só postar depois do passo 6 do roteiro de go-live (teste logado do Rafael) e depois do P-61 no ar (Modo GTO aberto ao Individual).** O link leva ao app e o texto promete o módulo.
Números: todos de `aura-main/_ops/golive-gto-2026-10-04/numeros-verificados.md` (08/10), exemplo (a): field 46,0%, GTO 38,8% (faixa 37,1–40,4%), 5,6 pp acima do topo da faixa. Nenhum outro número.
O CTA é "Conhecer o Modo GTO" / "See GTO Mode"; não promete o GTO de graça. A frase do plano é a da HUB de 08/10 ("incluído no plano Individual por tempo limitado") e depende da publicação do P-61. Sem preço, sem o plano Modo GTO como produto à venda, sem "prévia", sem Beta.
@aurapokeranalytics: a confirmar pelo Rafael. UTM: `utm_campaign=modo-gto-launch`, uma URL por idioma.

---

## PT

```
📊 **Novo na Aura: Modo GTO**

Ao lado do número do field, o número GTO e a faixa GTO, onde há referência. Onde o field sai da faixa, está o spot para estudar.

**Exemplo de spot**
CO × BB em pote simples, 30–60bb (GTO a 40bb), torneios Regular, últimos 2 anos, flop K-high two-tone, sem par, desconectado. Contra o c-bet de 33%, o field folda 46,0% e o GTO folda 38,8% (faixa 37,1–40,4%): 5,6 pp acima do topo da faixa.
Aqui o field folda mais do que o GTO. É um spot, não a média do field. Confira no seu board.

**O que você vê**
- Pós-flop: SRP e 3-bet, flop e turn, inclusive a reação a raise no flop do SRP
- Pré-flop: o GTO e o desvio nas células cobertas, inclusive o RFI de CO e BTN a 40bb

🔎 Abra um spot que você joga e olhe o gap.

O Modo GTO está incluído no plano Individual por tempo limitado. A conta grátis segue com o field e a comparação com o MDF.
Ferramenta de estudo. 18+.
👉 Conhecer o Modo GTO: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-pt
```

## EN

```
📊 **New on Aura: GTO Mode**

Next to the field number, the GTO number and the GTO range, where a reference exists. Where the field leaves the range, that is the spot to study.

**Example spot**
CO × BB single-raised pot, 30–60bb (GTO at 40bb), Regular tournaments, last 2 years, K-high two-tone, unpaired, disconnected flop. Facing a 33% c-bet, the field folds 46.0% and GTO folds 38.8% (range 37.1–40.4%): 5.6 pp above the top of the range.
Here the field folds more than GTO does. This is one spot, not the field average. Check it on your board.

**What you see**
- Postflop: SRP and 3-bet, flop and turn, including the response to a raise on the SRP flop
- Preflop: the GTO and the deviation in the covered cells, including the CO and BTN RFI at 40bb

🔎 Open a spot you play and look at the gap.

GTO Mode is included in the Individual plan for a limited time. The free account keeps the field and the MDF comparison.
Study tool. 18+.
👉 See GTO Mode: https://www.aura.poker/?utm_source=discord&utm_medium=social&utm_campaign=modo-gto-launch&utm_content=discord-en
```

---

## Notas
- A reação a raise é dita só como "no flop do SRP". Nos 3-bets BB vs CO, SB vs BTN e BTN vs CO a 40/60bb ela ainda não tem GTO; não generalizar.
- A ressalva de torneios vanilla fica só na Metodologia do app (pedido do Rafael em 06/10); o Discord não a repete.
- Conferência da contagem, para quem quiser refazer: copiar o texto de cada bloco (sem as cercas ```) para um arquivo sem quebra de linha final e rodar `python -c "import sys;print(len(open(sys.argv[1],encoding='utf-8').read()))" arquivo.txt`. A contagem acima foi feita por regex âncorada no arquivo inteiro (`\A(?s:.){N}\z`), porque esta sessão não tinha Python. O resultado é PT 1.029 e EN 1.066.
