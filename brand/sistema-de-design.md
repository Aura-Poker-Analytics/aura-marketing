# Sistema de design da Aura (artes fora dos templates)

Artifact (Design System): https://claude.ai/artifact/2LCAHgMazd7SbeEXe3qZr9
Criado em 03/11/2026 (DESIGN-CASA item 2). Privado ao dono até ser compartilhado pelo menu Compartilhar.

## Para que serve

Para toda arte da Aura que não sai de um template de `instagram/templates/`: post de feed (1080×1350), story (1080×1920), slide de carrossel, peça avulsa. Os agentes `casa:fabrica-posts` e `casa:ui` leem o artifact antes de montar a arte.

Como um agente lê: Artifact `read` na URL acima com `path: "project/README.md"` (regras), depois `project/tokens.json` (valores) e `project/components/bundle.css` (classes `au-*`). Logos: Artifact `read` com o id do asset listado no README dos Logos.

## Regras de uso

1. Arte de template segue o template. Arte nova usa o sistema inteiro. Nunca misturar os dois dialetos (template: Montserrat 900, gradiente amber, pílulas; sistema: Barlow Condensed, navy e gold, cantos de 2px, números em mono).
2. Tema `navy` é o padrão; `paper` só quando a peça pede fundo claro. No paper, `gold` só preenche; texto dourado é `gold-2`.
3. Título em CAIXA ALTA, uma linha em destaque (`.g` gold ou `.o` vazado). Pouco texto: título, uma lede, um CTA.
4. Número só com fonte verificada e `SourceNote` na arte. Field grande, GTO ao lado, diferença em "%" (nunca "pontos", "pts", "pp").
5. "a Aura" (feminino), sem "Beta", sem "plano GTO", termos de poker em EN dentro do PT. Carrossel em EN; legenda leva o PT.
6. Lockup no topo de toda arte, 18+ sempre. Logo gold sobre navy, navy sobre paper ou gold, branco só sobre navy.
7. Toda arte é vista no navegador (e a 390 px) antes de ir à HUB.

## De onde vem cada token

Fontes: **BK** = `brand/brand-kit.md`; **TPL** = `instagram/templates/*.html`; **L** = CSS da landing no ar (www.aurapoker.com, `index-BTiddCs-.css`, bloco `.v5` e `:root`, lido em 03/11/2026).

| Token | Navy | Paper | Fonte |
| --- | --- | --- | --- |
| navy | #0F1526 | #0F1526 | BK Primária; L `--navy` |
| gold | #D4A418 | #D4A418 | BK Destaque; L `--gold`; fill dos SVGs |
| gold-2 | #E8BC3A | #7A5C05 | L `--gold2`; L `#gratis .chan` |
| paper | #F3EEDF | #F3EEDF | L `--paper` |
| ground | = navy | = paper | alias |
| ground-deep | #0A0F1C | #FFFFFF | L `--ink`; BK White |
| surface | #141B30 | #FFFFFF | L `--navy2`; BK White |
| line | #222C46 | #C7C7C7 | L `--line`; BK Dark gray |
| line-strong | #36446A | = navy | L `--line2`; borda do ticket da L |
| ink | #F5F6F8 | = navy | L `--fg`; L `#gratis` |
| ink-soft | #B9BFCC | #223559 | L `.v5 --fg2`; BK gradiente 02 |
| ink-dim | #8A93A6 | #2F435C | L `.v5 --fg3`; BK gradiente 03 |
| on-gold | = navy | = navy | L `.cta` |
| fold / call / raise | #015A6B / #348A5D / #AD2C34 | iguais | BK cores semânticas; L `--action-*` |
| fold-text | #6FD0E2 | #015A6B | L `.duel .a .v`; BK |
| call-text | #46AD74 | #348A5D (3,9:1, só 24px bold) | L `--action-call-text`; BK |
| raise-text | #E06B74 | #AD2C34 | L `--action-raise-text`; BK |
| chart-field | #E8BC3A | #8A6806 | L `--chart-field`; L `#gratis h2 .g` |
| chart-gto | #7A9BBF | #2F435C | L `--chart-gto`/`--steel`; BK gradiente 03 |
| gto-stripe | #C9D6E6 | #C6D3E4 | L `.duel .b .bar`; BK gradiente 05 |
| amber-300/400/600, slate-950 | #FCD34D / #FBBF24 / #D97706, #020617 | iguais | TPL `--amber3/--amber/--amber6/--bg` (só templates) |

| Tipo | Valor | Fonte |
| --- | --- | --- |
| display (títulos, CTA) | Barlow Condensed 800/900 | L `--cond`, h1/h2 e `.cta`; arquivos woff2 da L `/fonts/v5/` |
| sans (lede, corpo) | Montserrat variável | L `--sans`; TPL `fonts/Montserrat-Variable-latin.woff2` |
| mono (números, kicker, rodapé) | IBM Plex Mono 400/600 | L `--mono`, `.duel .v`, `.chan`, `.fine`; woff2 da L |
| display-hook / display-title | 124px .94 / 88px .98 | linha e tracking de L `#final h2` e `h1.big`; 124px = máximo de L `#dist h2`; 88px ≈ máximo de L `.s-fr h2` |
| display-cta | 34px 800 .03em | L `.cta` (peso, tracking) |
| lede / body | 33px 500 1.5 / 26px | TPL `.sub` da capa / legenda |
| num-xl / num-l | 128px / 72px 600 -.04em | L `.duel .a .v` / `.b .v` (máximos) |
| kicker / label / fine | 24px .16em / 22px .14em / 18px .04em | L `.chan`, `.duel .k`, `.fine` (tracking); TPL (tamanhos) |

| Espaço e forma | Valor | Fonte |
| --- | --- | --- |
| space-art-margin | 84px | TPL `--pad` |
| space-art-top | 56px | TPL solver-vs-field `body` padding |
| space-block / space-item / space-tight | 36 / 16 / 8px | TPL capa `.sub` e `.swipe`; solver-vs-field `.bullets` e `.col .sub` |
| radius-sharp | 2px | L `--card-radius`, `.cta`, `.chip` |
| radius-card / radius-pill | 16px / 999px | TPL `.bchip` / kicker e swipe (só templates) |
| shadow-field-glow | 0 26px 70px rgba(217,119,6,.16) | TPL `.col.field` |
| zonas seguras do story | 220px topo, 260px base | escolha deste sistema (não há fonte no disco) |

Logos: `aura-symbol-*` e `aura-wordmark-*` usam os paths `ICON_PATHS` e `AURA_LETTERS` dos templates; `aura-lockup-*` junta os dois; `logo-icon.svg` e `logo-slogan.svg` são cópia de `brand/`.

## O que não tem fonte e foi decidido aqui

- Zonas seguras do story (220/260 px), passo de 72px da grade de fundo, o arco `au-arc` (eco do arco do símbolo) e o tamanho 52px do lockup no topo.
- Números dos exemplos: os do duel publicado na landing (SB contra 3-bet do BB, 30 a 50bb: field 52,5%, GTO 39,2%; 96,4 mi de mãos, 1,4 bi de decisões). A landing escreve a diferença como "+13,3 pontos", o que fere a regra R1 da casa; o sistema usa "+13,3%".
