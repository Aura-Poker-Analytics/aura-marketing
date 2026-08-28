# Plano: onboarding free→pago com escada de oferta

**Criado:** 2026-08-27 · **Substitui** a proposta de sequência D0/D7/D14 simples
**Contexto:** 4 cadastros pagos + ~40 orgânicos parados entre o cadastro e a assinatura sem nenhum toque. Eliseu (único assinante de coorte comparável) levou 22 dias. O cupom entra como degrau final da escada, não como abertura.

## A escada (por cadastro, relógio individual)

| Dia | E-mail | Objetivo | Oferta |
|---|---|---|---|
| **D0** | Boas-vindas: "por onde começar" — 3 passos no produto (Hotspot → Preflop → Node-by-Node) | ativação | nenhuma |
| **D7** | **Tendências por classe de jogador** (eixo aprovado pelo PO 27/08): o gap Reg vs Fish num spot real e a decisão que muda ao saber a classe. ~~Caso K♦9♥5♠ vs MDF~~ rejeitado — fraco e encosta no limite do gabarito (MDF descritivo). Formato = fórmula do criativo vencedor de fev/26 (12,85% CTR: "Regs e Fishes jogam esse spot com 20% de diferença"). ⛔ Depende de números REAIS do painel de classes (PO fornece print ou extração validada) | valor/conteúdo | nenhuma |
| **D14** | "O que o upgrade destrava": board completo, todos os buy-ins, filtros | consideração | nenhuma |
| **D21** | **Só pra quem não assinou:** cupom de 50% na primeira mensalidade | conversão | `code` do mês, expira dia último do mês |

**Por que o cupom só no D21:** oferta cedo demais ancora o produto como "coisa que se compra com desconto" e canibaliza quem pagaria cheio. Três e-mails de valor primeiro; desconto como último empurrão pra quem demonstrou interesse (abriu/entrou) e não converteu.

## Desenho do cupom (lições do AURAVOLTOU aplicadas)

- **Valor fixo, nunca %**: R$75 off BRL / US$15 off USD (≈50% da mensalidade), `duration: once` — no anual desconta só isso, sem brecha de ano grátis (produto único com todos os prices, `applies_to` não separa)
- **Código mensal rotativo** (ex.: `STACKSET` em setembro): resolve o problema de expiração individual sem automação por usuário; expira no fim do mês → urgência verdadeira
- **max_redemptions**: 100/mês
- ⛔ **Gate:** confirmar que o deploy da aura-api pós-PR #18/#20 aconteceu (campo de cupom visível no checkout + metadata com UTM). Testar com assinatura-teste antes do primeiro envio D21.

## Operação

- **Fase 1 (manual, já):** lotes semanais — toda leitura de campanha, eu puxo do `tbl_user` quem cruzou D0/D7/D14/D21 na semana e disparo o e-mail correspondente via Resend (batch, mesmo template da marca)
- **Fase 2 (automação):** Resend Automations (trigger contato novo + delays) quando a Fase 1 validar copy e taxas — meta: >40% abertura, >5% clique no D14, resgate >10% no D21
- **Medição:** UTM `utm_campaign=onboarding&utm_content=d00|d07|d14|d21-<mês>` + resgates do cupom na Stripe + assinatura com metadata UTM (PR #20)

## Auditoria dos paid ads vs skill `meta-ads` (kostja94/marketing-skills, 27/08)

| Critério da skill | Nosso estado | Ação |
|---|---|---|
| 1 objetivo por campanha; sem campanhas duplicadas | ✅ ok (Leads EU · Engagement ATIV) | — |
| **Excluir clientes existentes e convertidos recentes** | ❌ **falhava** — nenhum conjunto excluía cadastrados | ✅ **corrigido 27/08**: Convertidos 180d + Trial Antigo excluídos de EU e ATIV01 |
| **3–5 criativos por conjunto** | ❌ 1 criativo por conjunto — sem teste, fadiga sem plano B | 🎯 próxima ação do PO: subir `disc-02-exploit-en.mp4` (já renderizado em `content/paid/AURA-DESCOBERTA/`) como 2º anúncio da EU |
| Frequência < 3 | ✅ EU 1,3–1,6 · ⚠️ ATIV01 ~2x acumulada no público de 10k | manter vigilância; fim de vida natural da ATIV01 ~30/08 |
| 50 conversões/semana pra sair do learning | ❌ impossível no nosso volume (2–3/semana) | trade-off consciente da receita "conversão desde o D1" — documentado no playbook §3.1-B |
| Vídeo: hook 0–3s → problema → solução → CTA | 🟡 hook ok (pergunta no frame 1); estrutura ~ok em 26s | crítica do PO ao card ATIV vale pro próximo criativo FRIO (clareza de "o que é") |
| Pixel + CAPI server-side | ✅ forte — dedup validado, Subscribe exercitado, valores em implantação | — |
| Broad/Advantage+ como default | ❌ desvio deliberado — cerca manual pós-diagnóstico bets | manter; re-testar broad só fora do BR |
| Landing mobile rápida | ✅ auditada (DOM 280ms) | — |
| Exclusão de convertidos no retargeting (7–14d) | n/a por ora (sem retargeting ativo) | aplicar quando pools de site atingirem mínimo |

**Estado das campanhas em 27/08:** EU de volta a R$15/dia (escala pra R$22 falhou o gate — 4 dias, R$91, 0 cadastros; teto do canal mapeado em ~R$15–18) · ATIV01 R$10/dia (⚠️ pausada pela API na edição de exclusões — PO precisa religar) · CPA de referência: R$40–50/cadastro · Checkpoint de conversão da coorte paga: **15/09**.
