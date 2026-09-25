# STATE.md — aura-marketing

Atualizado em: 2026-09-25 · por: sessão **aura-marketing · plano Meta Ads · R$ 1.000 com Modo GTO** · branch de trabalho: `feature/meta-ads-overlay-poolvsgto` ([PR #1](https://github.com/Aura-Poker-Analytics/aura-marketing/pull/1), draft)

Regras: menos de 150 linhas. Aponta para docs, não os repete. Toda sessão de tarefa atualiza este arquivo antes de fechar. "Em andamento" tem no máximo dois itens. Primeiro STATE.md do repo, criado nesta sessão.

## 1. Implementado
- Brand kit e vocabulário ("field, nunca pool"; "Modo GTO", nunca "overlay", em público) · `brand/brand-kit.md`, `docs/02-paid/meta-overlay-pool-vs-gto/07-compliance.md`
- Pipeline de criativos por HTML → `.mp4`/`.png` (`instagram/build-*.mjs`, `instagram/templates/`), re-renderizável localmente sem custo
- Criativos pagos renderizados, PT e EN: DISC-01 a DISC-04, DISC02 plataforma, DISC03 classes de c-bet, PAID01 v1–v3 · `content/paid/`. Todos com o selo "500M+" gravado (ver §3)
- Plano de Meta Ads revisado para **R$ 1.000 com o Modo GTO no ar** (25/09): Fase 1 R$ 600 (3 criativos × R$ 20/dia × 10 dias), Fase 2 R$ 400 só com gate, otimização por `CompleteRegistration`, público identidade EN · `docs/02-paid/meta-overlay-pool-vs-gto/02-plano-em-fases.md` · PR #1, sem merge
- Mídia paga: **parada desde 15/09** (conferido no MCP da Meta em 25/09: último gasto em 15/09, R$ 9,53). Vida da conta: R$ 1.771, ~12 cadastros, 0 assinaturas · `01-linha-de-base.md`

## 2. Em andamento (máx. 2)
- **Meta Ads · R$ 1.000 com Modo GTO** · branch `feature/meta-ads-overlay-poolvsgto` · onde parou: plano revisado e commitado no PR #1; nada criado na Meta · próximo passo: re-renderizar os 3 criativos escolhidos trocando "500M+ audited hands" por "400K+ tournaments" (item 0.6), depois esperar o §9 do doc 02 · doc: `docs/02-paid/meta-overlay-pool-vs-gto/02-plano-em-fases.md`
- **BOARD01 (seleção de board) e descoberta v2** · branch `feature/descoberta-reels-v2` (checkout `aura-main/aura-marketing`), **pushada em 25/09** até `dd5f7ec` (5 commits, fast-forward, sem rebase) · onde parou: BOARD01 EN renderizado (24,2 s), PT não feito; `PLAYBOOK-midia-paga-do-zero.md §8.6` escrito · próximo passo: PR ou merge dessa branch, para o T3 do plano de R$ 1.000 chegar à `main`

## 3. Bloqueado ou na mão do PO
- **Ligar os R$ 1.000** · bloqueado por: go-live do Modo GTO **com o A1 do brief 12**. Medido em 25/09 na `main` do `aura-novofront`: `CreateCheckoutSessionRequest` não tem plano, então **um cadastro novo só consegue comprar o Individual**, embora a API aceite `planId: gto` · desde: 2026-09-25
- Merge do aura-landing#11 com `VITE_LAUNCH_MODO_GTO=1` e `VITE_LAUNCH_FIELD_VS_GTO` desligada (a flag do Top publica "spots novos todo mês", A12b) · bloqueado por: ok do PO · desde: 2026-09-24
- Conta de anúncio `1598770224460932`: forma de pagamento, verificação da empresa e do domínio, 2FA; criar a campanha do `02 §4.1` · bloqueado por: Rafael (o MCP da Meta é só leitura) · desde: 2026-09-25
- Medir o CAC: leitura agregada do AuraBusiness (pede o sim do Rafael na sessão) e do Stripe (autenticar) · autorizado pela B4, ainda não feito · desde: 2026-09-24
- 🔴 **"500M+ mãos" gravado em todos os criativos prontos e nos 12 roteiros**, e o PO tirou o número da landing (sem proveniência; B6 = "Mais de 400 mil torneios" + `/metodologia`) · resolvido por: re-render (item 0.6), sem decisão pendente · desde: 2026-09-23
- A14 (real no checkout ≠ landing): não trava o teste EN, trava anúncio em PT com preço · bloqueado por: Rafael no Stripe · desde: 2026-09-25
- Depoimentos (B2): texto final por escrito do Paulo "Galator" e do braga (sem [GTOW]) · não travam esta rodada · bloqueado por: autores · desde: 2026-09-24

## 4. Contratos que este repo FORNECE
| Contrato | Consumidor | Formato e onde está documentado | Versão ou data |
| --- | --- | --- | --- |
| Convenção de UTM da mídia paga (`utm_source=meta`, `utm_medium=paid_social`, `utm_campaign=gto-r1000`, `utm_content=<slug do criativo>`) | relatório de coorte no AuraBusiness (B4), GA4 | `02-plano-em-fases.md §3.1` · não tinha linha; registrado nesta sessão | 25/09 |

## 5. Contratos que este repo CONSOME
| Contrato | Fornecedor | Como consome (tabela, pacote, arquivo) | Risco atual |
| --- | --- | --- | --- |
| Repasse de `utm_*`/`fbclid`/`fbp`/`lang` da landing ao app | aura-landing (`src/lib/appUrl.ts`, #11) | URL do CTA | só existe no #11, sem merge; o app trava o primeiro toque (`aura_attribution_v1`) |
| UTM e `fbc`/`fbp` gravados no cadastro | aura-novofront + aura_api (`TblUser.cs:108-122`) | colunas `Utm*` do `tbl_user`, lidas em agregado | leitura pede o sim do Rafael |
| Eventos Meta: `CompleteRegistration` (pixel + CAPI, `reg_<id>`), `Subscribe` (CAPI, `sub_<id>`) | aura_api `MetaCapiService.cs`, pixel `1405949840871947` | otimização e medição no Gerenciador | `Subscribe` com `currency` fixa em `"usd"` e valor por mapa de price id: conferir os price ids do GTO; `InitiateCheckout` não existe |
| Preços e nomes dos planos (GTO US$ 49/249/439, R$ 250/1.245/—) | HUB (A13, A16), aura-landing `pricing.ts` | só internamente; real fora do criativo até a A14 | anual em real em disputa (A16) |
| Alegações públicas ("400K+ tournaments", `/metodologia`) | aura-landing#11 (B6) | selo dos criativos | depende do merge do #11 |

## 6. Próxima sessão
Re-render dos 3 criativos do `02 §8` com o selo "400K+ tournaments · 7 rooms" (depois do push da `feature/descoberta-reels-v2`) · sessão única neste worktree · Sonnet médio (é troca de string e render) · começa por `docs/02-paid/meta-overlay-pool-vs-gto/02-plano-em-fases.md §8.2`. A medição do D10/D30 é outra sessão (Opus médio, leitura agregada com o sim do Rafael).

## Mapa de leitura
- Regras de engenharia: AGENTS.md
- Plano de Meta Ads e linha de base: `docs/02-paid/meta-overlay-pool-vs-gto/00-LEIA-ME.md`
- Playbook de mídia paga: `docs/02-paid/PLAYBOOK-midia-paga-do-zero.md` (a §8.6 na branch `feature/descoberta-reels-v2`)
- Mapa do ecossistema e contratos: `../ECOSYSTEM.md`
