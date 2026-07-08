# Públicos Meta — Diagnóstico e Prognóstico

**Autor:** thread Mídia Paga · **Data:** 2026-07-08 · **Fonte:** inspeção direta do Gerenciador de Anúncios (Chrome logado, somente leitura — nada alterado)
**Para:** uso futuro do agente de mídia paga. Este doc é o inventário vivo dos públicos + o que está errado + o plano. Reler antes de montar qualquer conjunto de anúncios.

> **Nota de método:** o MCP oficial da Meta (`mcp.facebook.com/ads`) **ainda não estava conectado a esta sessão** no momento da coleta — os dados abaixo vieram da navegação no Gerenciador. Quando o MCP subir, revalidar tamanhos e capturar os **IDs numéricos** de cada público (a UI não expõe fácil; a API sim). Ver §5.

Conta: **Aura Business** `1598770224460932` (BRL) · Dataset/Pixel `1405949840871947` · IG @aurapokeranalytics (710 seguidores).

---

## 1. Inventário atual (4 públicos + 0 conversões personalizadas)

| # | Nome | Tipo | Definição | Tamanho | Criado | Usado? |
|---|---|---|---|---|---|---|
| 1 | **Aura \| Seguidores IG (Base)** | Personalizado | Engajamento IG: contas que **começaram a seguir** @aurapokeranalytics | **Abaixo de 1.000** | 29/01/2026 | ❌ 0 conjuntos |
| 2 | **Semelhante (BR, 1%) - …Seguidores IG (Base)** | Lookalike | 1% da população do Brasil, fonte = #1 | Indisponível | 29/01/2026 | ❌ |
| 3 | **Semelhante (BR, 1% to 3%) - …Seguidores IG (Base)** | Lookalike | 1–3% da população do Brasil, fonte = #1 | Indisponível | 29/01/2026 | ❌ |
| 4 | **Aura Business** | Salvo | BR · 18+ · **inclui** lookalike #2 · **E** cargo "Professional Poker Player" | Indisponível | 06/02/2026 (ed. 13/02) | ❌ |

**Conversões personalizadas:** nenhuma criada (tela inicial vazia).
**Públicos de site (pixel):** nenhum — o pixel coleta PageView mas não há custom audience de visitantes ainda.
**Retenção/idade:** só o público salvo #4 declara 18+ explicitamente.

## 2. Diagnóstico — o que está errado (prioridade decrescente)

**D1 — A semente é pequena demais (< 1.000) e frágil.** 🔴 crítico
O público #1 é a fundação de tudo (os 2 lookalikes saem dele). Meta recomenda semente de **1.000–50.000** para lookalike de qualidade; abaixo de 1.000 o sinal é ruidoso e o "semelhante" vira quase aleatório. Com 710 seguidores no IG, esse teto era esperado.

**D2 — A semente usa o critério mais estreito possível.** 🔴
#1 = quem "começou a seguir" — só seguidores. A Meta permite semente muito maior: **todos que engajaram** com o perfil/conteúdo IG (curtida, salvamento, DM, visita ao perfil) em até **365 dias**. Trocar "seguidores" por "engajadores 365d" aumenta a semente sem pagar nada e melhora D1.

**D3 — O público salvo #4 está sobre-empilhado.** 🟠
Ele cruza **lookalike ∩ cargo "Professional Poker Player" ∩ BR ∩ 18+**. Dois problemas:
- Interseccionar um lookalike (que já é uma expansão algorítmica) com um interesse rígido **anula** o lookalike e encolhe o alcance a quase nada.
- "Professional Poker Player" como cargo é um segmento minúsculo e enviesado a US — quase vazio no BR.
Resultado provável: alcance irrisório e CPM alto. Não usar como está.

**D4 — Tudo é BR-only.** 🟠
Nenhuma semente serve à fase de frio EN (F2 do plano). Uma base de <1.000 seguidores brasileiros **não pode** semear lookalike EN. A fase EN precisará de sementes próprias (pixel/registro pós-launch).

**D5 — Nada nunca rodou.** 🟡
0 uso em todos. Coerente com a conta nunca ter gasto de verdade. Sem histórico de entrega, esses públicos não têm aprendizado acumulado — começamos do zero de fato.

**D6 — Sem públicos de site nem exclusão de convertidos.** 🟡
Sem custom audience de visitantes da landing e sem audience de "já criou conta free" não dá pra (a) fazer retargeting de visitantes nem (b) **excluir quem já converteu** — desperdício garantido quando o pixel novo começar a povoar.

## 3. Prognóstico — plano de ação (ligado ao launch)

### Agora / pré-launch (custo zero, tudo é criação de público)
- **P1 — Recriar a semente como "engajadores IG 365d"** (não só seguidores). Nome sugerido: `Aura | IG Engajadores 365d`. Vira a nova base dos lookalikes. Mantém #1 antigo só como referência.
- **P2 — Não confiar em lookalike no launch.** Com semente <1.000 e BR-only, os lookalikes #2/#3 entram no máximo como **teste de baixo peso**. Prioridade de frio vai para **interesses de poker + Advantage+ broad** (ver [estrutura-campanhas.md](estrutura-campanhas.md) §2), que não dependem da semente fraca.
- **P3 — Desmontar o público salvo #4.** Para frio, usar **OU** lookalike **OU** interesse — nunca a interseção. Remover o cargo "Professional Poker Player". Se quiser um salvo de interesse, criar um limpo: BR · 18+ · interesses {Poker, Texas hold'em, PokerStars, GGPoker, WSOP}.

### Assim que o pixel novo da landing povoar (semana do launch → +7d)
- **P4 — Criar públicos de site:** `Visitantes landing 30d` e `Visitantes landing 7d` (retargeting quente do RTG, [estrutura-campanhas.md](estrutura-campanhas.md) §1).
- **P5 — Criar audience de convertidos** a partir do evento `CompleteRegistration` (180d) — usar como **exclusão** em todo frio/retargeting (não pagar por quem já tem conta).
- **P6 — (opcional) Conversão personalizada** "Conta free criada" baseada em URL (`/signup/success`) como rede de segurança se o evento `CompleteRegistration` falhar em disparar. Hoje não existe nenhuma conversão personalizada.

### Pós-launch, quando houver volume (~50–100 cadastros free)
- **P7 — Trocar a semente dos lookalikes de "seguidores IG" para "criadores de conta free".** Intenção muito maior que seguidor de IG → lookalike melhor. Este é o upgrade que resolve D1/D2 de vez. Rebuild dos lookalikes a partir daí.
- **P8 — Semente EN (D4):** quando a base de cadastros tiver massa fora do BR, criar lookalike EN próprio para a fase F2. Antes disso, F2 = interesse/broad, sem lookalike.

## 4. Como isso alimenta a estrutura de campanhas

- **RTG (quente):** engajadores IG 365d (P1) + visitantes landing 30d (P4), excluindo convertidos (P5). — pronto assim que P4 existir.
- **F1 frio BR:** interesses de poker + Advantage+ broad (P2/P3); lookalike #2 como teste secundário. Excluir convertidos.
- **F2 frio EN:** interesse/broad até ter semente EN (P8).

## 5. Quando o MCP da Meta conectar — checklist do agente

1. Listar todos os públicos com **ID numérico, tamanho estimado atualizado e status de entrega** (a UI esconde os IDs; a API não).
2. Confirmar tamanho real da semente #1 (a UI diz "<1.000" — pegar o número).
3. Validar se algum público entrou em "expirando" (custom audiences de engajamento expiram sem novo engajamento; retenção padrão 365d).
4. Cruzar com os eventos do dataset (`CompleteRegistration`/`Subscribe`) assim que a landing nova estiver instrumentada ([pixel-capi-spec.md](pixel-capi-spec.md)).
5. **Regra que não muda:** criar/editar público via MCP é permitido (não gasta); **subir ou ativar campanha, não** — segue a regra absoluta (tudo pausado, ativação só pelo Rafael).

## 6. Referência rápida

| Item | Valor |
|---|---|
| Business Manager | Aura Poker Analytics · `830069129552748` |
| Conta de anúncios | Aura Business · `1598770224460932` · BRL |
| Dataset/Pixel | Aura – Website Data Set · `1405949840871947` |
| IG | @aurapokeranalytics · `17841468976680108` · 710 seguidores |
| Públicos hoje | 4 (1 personalizado, 2 lookalike, 1 salvo) — todos BR, nenhum usado |
| Conversões personalizadas | 0 |
| IDs dos públicos | capturar via MCP (§5) — UI não expõe |
