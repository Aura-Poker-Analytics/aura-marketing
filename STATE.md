# STATE.md — aura-marketing

Atualizado em: 2026-10-23 · por: sessão `aura-marketing · followup cadastrados e Grátis · plano` (branch `feat/followup-cadastrados-gratis`) e, antes, sessão `aura-marketing · lançamento Field Hotspots · pacote` (branch `feature/launch-field-hotspots`) e, antes, `aura-marketing · Modo GTO pacote` (branch `feature/launch-modo-gto`) e, antes, `aura · Field Ranges · pacote de lançamento`

Regras: menos de 150 linhas. Aponta para docs, não os repete. Toda sessão de tarefa atualiza este arquivo antes de fechar. "Em andamento" tem no máximo dois itens.

## 1. Implementado
- Pacote de lançamento do Field Ranges (Beta), sem publicar: Discord PT/EN, Instagram (feed, story, carrossel de 6) PT/EN, mockups e texto da landing em `content/posts/field-ranges-launch/` (revisão de marca em 4 rodadas, OK com ressalvas na final; HUB aprovou o pacote em 3acf1ae).

## 2. Em andamento (máx. 2)
- **M2c do time de agentes (27/10)** · branch `claude/m2c-casa-termos` · tirou "rodapé de amostra" do brand-kit e do plano 2.0, trocou `brand-voice` por `brand.yaml` + `voz-grinder` + `copywriting` na `lote-posts` (agora versionada), "plano GTO" já estava limpo na main. Fica: diff dos agentes `aura-*` com a HUB; `brand.yaml` ainda não existe. Arquivar a sessão depois do merge. PR 2 (claude/m2c-vocab-legado): "pool" vira "field" no brand-kit e no plano 2.0, "bilhões" e "amostra de milhões" saem, beta.aura.poker marcado como URL interna. O checkout principal fica sem `.claude/skills/lote-posts` (backup em `_ops/backup-lote-posts-20261027`) até voltar para a main.
- **Pacote Field Exploits (frente A1, 25/10)** · branch `feature/field-exploits-a1-ar` · onde parou: pacote conferido contra a tela no ar (aura-novofront main `6b2ef8d`: nome Field Exploits, rota `/exploits`, herói "13,7% abaixo da faixa do GTO", lista sem selo de força, cadeado "+7 spots liberados no plano Individual"); números já atualizados na main (13,7 / 5,7 / 10,8 fora da faixa; 45,1% no 33%); pendências do rename, do Individual e da decisão permanente fechadas; Novidades com corpo B e link `/exploits`; FE-PUB-V2 (card agrupado por stack) ainda não saiu · próximo passo: "pode postar" e "pode enviar" do Rafael (o e-mail exige o sim digitado por ele nesta sessão), antes de 02/11; landing (aura-landing#27) no ar antes do post
- **Pacote Modo GTO (versão 15/10)** · branch `feature/launch-modo-gto` · onde parou: [PR #4](https://github.com/Aura-Poker-Analytics/aura-marketing/pull/4) com OK formal do revisor, nada publicado; carrossel de lançamento (7 slides EN, com o slide Field vs GTO, "GTO Mode is live", incluso no Individual por tempo limitado), story da capa PT, feed, e-mail PT/EN e textos em `content/posts/modo-gto-launch/` · próximo passo: gates do Rafael/HUB (P-61 conferido logado, Stripe 29/150, teste logado, hospedagem das imagens do e-mail no aura-landing#17, reconciliação da landing em sessão própria, data interna do "tempo limitado", oferta em dólar para o público BR) e depois postar/enviar · sessão pode ser arquivada
- **Pacote Field Ranges** · branch `feature/launch-field-ranges` · onde parou: PR #2 aberto (3acf1ae), nada publicado, pacote fechado do lado da sessão · próximo passo: merge do PR #2 e postagens são do Rafael; a landing lê os mockups deste worktree (não remover até o merge); só o @aurapokeranalytics a confirmar · doc: `content/posts/field-ranges-launch/copy.md`

## 3. Bloqueado ou na mão do PO
- **Followup de cadastrados e Grátis (28/10)** · plano em `docs/00-strategy/followup-cadastrados-gratis.md` (§14 é o estado da execução) · R1 enviado em 28/10 a 185 (broadcast `f185d44e`, segmento `65da31a5`, variante A, tracking ligado) · próximo: R2 com cupom `Ph7y2HU9` em 02/11 para quem não logar em 5 dias (assunto B do §6), leitura do R1 em 04/11 · o R2 é e-mail a usuário: precisa do "sim" do Rafael · desde: 2026-10-23
- **Varredura de influencers IG MTT** · branch `feat/influencers-ig-mtt` (`research/influencers-ig/`, PR #5 rascunho) · descoberta feita (218 @ únicos: BR 50, LatAm 100 linhas, EN 157); fase 2 **bloqueada**: o token novo é válido (`me/accounts` acha a conta 17841468976680108, escopos instagram_basic, pages_show_list, pages_read_engagement ok), mas o Business Discovery volta erro 10 "Application does not have permission" — o app Aura Insights não tem o recurso **Instagram Public Content Access** (App Review → Permissions and Features; exige revisão e, em geral, verificação do negócio) · bloqueado por: Rafael pedir o recurso no App Review; depois `python -X utf8 -I scripts/enrich.py` e `scripts/build.py` · desde: 2026-10-08
- Publicação: quem posta é o Rafael; URLs com UTM já definidas (tabela no `copy.md`), falta confirmar o @ do perfil · desde: 2026-10-06
- Números: só `numeros-verificados.md` (lake congelado desde 20/08, estimativa do field); o Field Ranges só vai ao ar com o merge e o promote do Rafael no aura-main · desde: 2026-10-06

## 4. Contratos que este repo FORNECE
| Contrato | Consumidor | Formato e onde está documentado | Versão ou data |
| --- | --- | --- | --- |
| Mockups do Field Ranges (PT/EN) | aura-landing | `content/posts/field-ranges-launch/mockups/*.png` + alt text na seção Landing do `copy.md` | 06/10 |

## 5. Contratos que este repo CONSOME
| Contrato | Fornecedor | Como consome (tabela, pacote, arquivo) | Risco atual |
| --- | --- | --- | --- |
| Números verificados do Field Ranges | aura-main | cópia de `_ops/field-ranges-launch/numeros-verificados.md` | números mudam se as folhas forem refeitas |
| Telas do app | aura-novofront (#69 `bcc593f`) | capturas de http://localhost:5302 em `mockups/raw/` | a UI pode mudar antes do lançamento |

## 6. Próxima sessão
Landing: copiar os mockups e a seção Landing para o aura-landing (sessão no aura-landing, Sonnet médio, `aura-landing-dev`), depois do ok do Rafael.

## Mapa de leitura
- Regras: AGENTS.md · Estratégia: docs/00-strategy/ · Marca: brand/brand-kit.md
