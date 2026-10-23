# STATE.md — aura-marketing

Atualizado em: 2026-10-23 · por: sessão `aura-marketing · followup cadastrados e Grátis · plano` (branch `feat/followup-cadastrados-gratis`) e, antes, sessão `aura-marketing · lançamento Field Hotspots · pacote` (branch `feature/launch-field-hotspots`) e, antes, `aura-marketing · Modo GTO pacote` (branch `feature/launch-modo-gto`) e, antes, `aura · Field Ranges · pacote de lançamento`

Regras: menos de 150 linhas. Aponta para docs, não os repete. Toda sessão de tarefa atualiza este arquivo antes de fechar. "Em andamento" tem no máximo dois itens.

## 1. Implementado
- Pacote de lançamento do Field Ranges (Beta), sem publicar: Discord PT/EN, Instagram (feed, story, carrossel de 6) PT/EN, mockups e texto da landing em `content/posts/field-ranges-launch/` (revisão de marca em 4 rodadas, OK com ressalvas na final; HUB aprovou o pacote em 3acf1ae).

## 2. Em andamento (máx. 2)
- **Pacote Field Exploits (ex-Field Hotspots; 22–23/10, P-82)** · branch `feature/launch-field-exploits` · onde parou: o Rafael renomeou o módulo para Field Exploits em 23/10; pacote aprovado (aura-marketing#9, mesclado em `1d049be`) refeito com o nome novo em `content/posts/field-exploits-launch/` (UTM `field-exploits-launch`), mesma narrativa e visual; item de Novidades no #10 · próximo passo: a tela do app mostrar Field Exploits, deploy de aura-api#122/aura-novofront#186, landing no ar, olho logado, publicar antes de 02/11; postar e enviar são do Rafael
- **Pacote Modo GTO (versão 15/10)** · branch `feature/launch-modo-gto` · onde parou: [PR #4](https://github.com/Aura-Poker-Analytics/aura-marketing/pull/4) com OK formal do revisor, nada publicado; carrossel de lançamento (7 slides EN, com o slide Field vs GTO, "GTO Mode is live", incluso no Individual por tempo limitado), story da capa PT, feed, e-mail PT/EN e textos em `content/posts/modo-gto-launch/` · próximo passo: gates do Rafael/HUB (P-61 conferido logado, Stripe 29/150, teste logado, hospedagem das imagens do e-mail no aura-landing#17, reconciliação da landing em sessão própria, data interna do "tempo limitado", oferta em dólar para o público BR) e depois postar/enviar · sessão pode ser arquivada
- **Pacote Field Ranges** · branch `feature/launch-field-ranges` · onde parou: PR #2 aberto (3acf1ae), nada publicado, pacote fechado do lado da sessão · próximo passo: merge do PR #2 e postagens são do Rafael; a landing lê os mockups deste worktree (não remover até o merge); só o @aurapokeranalytics a confirmar · doc: `content/posts/field-ranges-launch/copy.md`

## 3. Bloqueado ou na mão do PO
- **Followup de cadastrados e Grátis (23/10)** · branch `feat/followup-cadastrados-gratis` · plano em `docs/00-strategy/followup-cadastrados-gratis.md` (diagnóstico com a consulta de cada número, 4 segmentos por uso de módulo, sequências de ativação, upgrade e reativação, teste A/B no R1) e rascunhos A1, U1 e R1 em `content/email/followup-*.html`; nada enviado, nenhuma automação criada · bloqueado por: decisões R1–R6 do Rafael (§9 do doc: tracking no Resend, envio dos lotes, CTA da ativação, sem desconto, segmento Grátis, assinatura); contagens do AuraBusiness sem ferramenta de leitura (SQL pronto na §1.4); sessão no aura_api para os marcos `first_analysis_at` e `last_gate_hit_at` (fase 2) · desde: 2026-10-23
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
