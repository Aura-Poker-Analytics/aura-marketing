# Recapturar os mockups do Field Hotspots

**Estado em 23/10 (pacote refeito):** nenhuma arte do pacote usa print da tela. O carrossel (`carrossel-v3/`), o feed, os stories, o story da capa e o e-mail são reconstruídos em HTML por `carrossel-v3/build_pacote.py`. Os recortes desta pasta ficam só como insumo para a seção da landing (sessão no aura-landing). **Pendência:** se a landing usar recorte, recapturar logado de www.aura.poker/hotspot, em EN e com device scale 2, depois do deploy do aura-novofront#186 (o texto do cadeado muda). Os recortes mobile do pago e do Grátis eram byte a byte iguais e viraram um arquivo só (`mobile-spot-sem-numeros.png`, `mobile-menu-hotspots-new.png`).

## Histórico (pacote de 22/10, substituído)

As artes usam prints da validação do aura-novofront#169 (22/10, ambiente de teste, contas de teste "P" e "F"):
`aura-novofront/_ops/validacao-prints/169/`. Quando o merge estiver no ar, recapturar de **www.aura.poker/hotspot** (pago e Grátis, 1280 e 390; e **em EN**, ver abaixo), colocar os novos prints na mesma pasta de validação (ou ajustar `RAW` em `instagram/src/make_mockups.py`) com os mesmos nomes e rodar `python make_mockups.py` e `python build.py` em `instagram/src`.

Regra: nenhum número estatístico da tela aparece nas artes. Os prints originais (COM números) ficam só em `aura-novofront/_ops/validacao-prints/169/`; `make_mockups.py` lê de lá e este repo não guarda cópia. Os recortes de `mockups/` têm os números cobertos pelo `make_mockups.py`. Números nas artes vêm só de `instagram/src/numbers.json`.

## Origem dos recortes
| Recorte (mockups/) | Print (validacao-prints/169/) | Região (px do print) |
|---|---|---|
| nav-completo.png, nav-neutro-idioma.png | paid-1280-3 | menu do topo, y 0-57, sem sino e avatar da conta de teste (neutro = sem "Painel") |
| spot-detalhe-cabecalho.png | paid-1280-3 | painel do detalhe até o rótulo Overdefend, sem a linha de números |
| como-explorar.png | paid-1280-3 | caixa Como explorar |
| lista-paga-sem-numeros.png | paid-1280-3 | coluna dos spots, números das linhas cobertos |
| lista-gratis-sem-numeros.png | free-1280-3 | 1 spot + 2 linhas trancadas, números cobertos |
| janela-capa-sem-numeros.png | paid-1280-3 | menu + lista + cabeçalho do detalhe, números cobertos |
| mobile-spot-sem-numeros.png, mobile-menu-hotspots-new.png | paid-390-3 | card do spot (linha de números coberta); barra inferior com Hotspots NEW |

Os prints `-4-field-hotspots-full` são byte a byte iguais aos `-3`; só os `-3` são usados. A 7ª linha da lista não entra no recorte (o recorte termina na 6ª).

## Qual arte usa qual
| Arte | Usa |
|---|---|
| story-capa-pt | RECORTES REAIS: nav-completo (x 420-945) + lista-paga-sem-numeros (2 primeiras linhas), ampliados 1,7x e 2,4x |
| carrossel-en-01 | RECORTE REAL: nav-neutro-idioma (2x); a lista é reconstruída em EN com os textos da tela |
| feed PT/EN, story PT/EN, carrossel 2 a 7, e-mail | nenhum print: cartas, cards de spot, barras e caixa Como explorar são reconstruídos no HTML (paleta do brand-kit; cartas com face creme e 4 cores). Parâmetros do spot (UTG vs BB, 25bb, SRP, textura, boards A♠3♠6♥, 6♠A♣7♣, 7♣A♥5♥) vêm da tela de 22/10 |
| mobile-*.png | gerados, ainda sem uso em arte |

## O que recapturar e por quê
1. **Troca de spot em 02/11:** o exemplo é o spot da semana de 22/10. Depois da troca ele pode sair da tela. Publicar antes, ou recapturar com o spot vigente e atualizar os parâmetros dos cards, `FLOPS`/`SPOTS` em `build.py`/`lib.py` e o texto do e-mail.
2. **EN:** os prints são em PT (menu "Painel", "DESVIO FORTE", "NOVO", "SPOTS LIBERADOS"). O carrossel é em EN, por isso só o menu neutro de idioma é recorte; a lista é reconstruída. Com os prints em EN (alternador PT/EN do topo), os recortes reais podem substituir as reconstruções.
3. **Resolução:** os prints são 1x (1280 e 390). Na capa em story eles são ampliados (soft). Recapturar com device scale 2 melhora a nitidez.
4. **Gráfico por size e linha de números:** ficam cobertos de propósito; não recapturar para mostrar.
5. Rótulo do spot e "NEW" no menu conferidos no ar (a tela não mostra Beta).
