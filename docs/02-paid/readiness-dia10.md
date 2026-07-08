# Prontidão dia 10/07 — Go/No-Go consolidado

**Autor:** thread Mídia Paga · **Data:** 2026-07-08 · **Launch da landing:** 10/07/2026
**Regra absoluta:** tudo sobe **PAUSADO**. Só o Rafael (PO) ativa e gasta. Este doc não altera nada — consolida e linka o que já está espalhado em:
[auditoria-meta-ads.md](auditoria-meta-ads.md) · [pixel-capi-spec.md](pixel-capi-spec.md) · [estrutura-campanhas.md](estrutura-campanhas.md) · [compliance-meta.md](compliance-meta.md) · [mcp-meta-identidade.md](mcp-meta-identidade.md) · [publicos-diagnostico.md](publicos-diagnostico.md)

**Como ler:** cada item tem status (puxado dos docs-fonte), dono, o que destrava e classificação de bloqueio. Agrupado pelas 3 categorias abaixo — a ordem de execução real está em **CAMINHO CRÍTICO** no final.

---

## 🔴 BLOQUEIA o launch da landing em si (dia 10)

Nenhum item de mídia paga bloqueia o launch da landing. O único ponto realmente 🔴 é técnico e já é responsabilidade do dev, não da conta Meta:

| Item | Status atual | Dono | O que destrava | Fonte |
|---|---|---|---|---|
| **Pixel base (browser) na landing — FASE 1 mínima** | Decisão do PO (08/07): lançar sem a integração completa pra agilizar. O mínimo pro dia 10 é só o **pixel browser + PageView** (~15 min, sem backend/CAPI/segredo). Sem ele, no cutover o `aurapoker.com` fica **cego** (o pixel do WP velho some e nada entra) e você deixa de acumular público de retargeting | Dev da landing | Adicionar o snippet `fbq` + PageView no front da SWA. CAPI/Subscribe/UTM ficam pra Fase 2 (antes do pago) — ver [handoff §6](handoff-landing-pixel-migracao.md) |

Tudo o mais abaixo (§🟠 e §🟡) é sobre a **conta de anúncios**, não sobre a landing existir e publicar no ar. A landing pode e deve subir no dia 10 mesmo que a conta Meta continue zerada — o launch não depende de ads (orgânico é o canal principal, ver [compliance-meta.md §4](compliance-meta.md)).

---

## 🟠 BLOQUEIA o 1º gasto de mídia (não o launch da landing)

Sem estes itens, a estrutura de [estrutura-campanhas.md](estrutura-campanhas.md) não pode nem subir pausada de forma útil, ou não pode ser ativada quando o Rafael decidir gastar.

| # | Item | Status atual | Dono | O que destrava |
|---|---|---|---|---|
| G3 | **Campanhas antigas armadas** | 2 campanhas ("Apresentando a Aura - 2026", "Video Preflop Youtube") com toggle **ligado** + "erro no pagamento"; 1 ("Apresentando a Aura - Engajamento") desativada. Só não rodam porque não há saldo | Rafael, no Gerenciador de Anúncios | Desativar as 3 **antes** de qualquer saldo entrar — senão elas disparam sozinhas assim que houver método de pagamento |
| G1 | **Método de pagamento na conta Aura Business** | Nenhum. Modelo pré-pago, saldo R$ 0,00. Limite diário imposto pela Meta: R$ 105,49 (sobe com histórico) | Rafael, no Gerenciador (Cobrança e pagamentos) | Sem isso, nenhuma campanha — nem a nova, pausada — pode ser ativada. **Fazer só depois de G3** (ordem de segurança) |
| G2 | **Página do Facebook no BM** | Nenhuma. Lista de Páginas vazia; Business Suite opera só com o IG | Rafael, no Gerenciador | Identidade de anúncio exigida pelo Gerenciador de Anúncios — sem Página, não dá pra configurar o "ad set" de forma completa |
| — | **Domínio da landing** | **CONFIRMADO (08/07): `aurapoker.com`** — mesmo domínio do site atual (cutover WP→Azure). Falta só o Rafael (a) aceitar o alerta "confirme o domínio" no Diagnóstico do dataset e (b) verificar `aurapoker.com` no BM | Rafael, no BM | Ações de confirmação/verificação, não mais decisão. Ver [handoff-landing-pixel-migracao.md §5](handoff-landing-pixel-migracao.md) |
| — | **Pixel/CAPI/eventos da landing** | `PageView` ok; `CompleteRegistration` e `Subscribe` (browser+server, dedup, UTM) **não implementados** — spec entregue ao dev em 04/07 | Dev da landing | Sem isso o KPI norte (conta free atribuída via UTM) nasce cego — dá pra rodar mídia sem otimização real, mas não dá pra medir CPA nem otimizar pro evento certo |
| — | **Públicos utilizáveis** | 4 públicos existentes, todos fracos/BR-only, 0 uso (ver [publicos-diagnostico.md §1-2](publicos-diagnostico.md)): semente de seguidores <1.000, lookalikes sobre semente frágil, público salvo sobre-empilhado (lookalike ∩ cargo). Faltam: engajadores IG 365d, visitantes de site (pixel novo), exclusão de convertidos | Thread Mídia Paga (criação, custo zero) | Sem público de retargeting quente minimamente saudável, a Fase RTG (primeira a subir) não tem pra quem anunciar |

---

## 🟡 HIGIENE / risco (não bloqueia, mas fazer antes reduz risco de reprovação/bloqueio de conta)

| # | Item | Status atual | Dono | O que destrava |
|---|---|---|---|---|
| G6 | **Verificação da empresa** | Qualificada para verificação (CNPJ AURA ANALYTICS LTDA já cadastrado na cobrança), **não iniciada** | Rafael, no Business Manager (Central de Segurança) | Reduz risco de restrição por segurança; é também pré-requisito do plano B de compliance (pedido formal de autorização, se necessário — [compliance-meta.md §4](compliance-meta.md)) |
| G7 | **2FA do BM + contato de recuperação** | 2FA "Ninguém" obrigado; admin único (Rafael); sem contato de recuperação | Rafael, no Business Manager | BM com admin único sem 2FA é o jeito mais comum de perder tudo — restrição por segurança bloqueia ads igual restrição por policy |
| — | **MCP oficial da Meta** | Parado. Conectou com o login errado (perfil FB `61584288455982`, que só enxerga uma conta vazia); tentativa de corrigir via convite pro perfil pessoal terminou com esse perfil desabilitado. Causa-raiz: negócio é Instagram-first, BM não tem perfil de Facebook admin nem Página — Facebook Login do connector não tem o que conectar | Rafael (ação de OAuth/permissão — agente não faz) | Não bloqueia nada operacional — é conveniência (API em vez de Chrome). Dados continuam vindo 100% via Chrome logado. Caminho de correção completo em [mcp-meta-identidade.md](mcp-meta-identidade.md) — decisão já tomada: **parado até depois do launch** |

---

## CAMINHO CRÍTICO

Ordem mínima para chegar no dia 10 com a **landing no ar medindo cadastros** (KPI norte = conta free via UTM), separando o imprescindível do que pode vir depois.

### Imprescindível ATÉ 10/07

1. **Dev coloca a FASE 1 mínima do pixel** (browser + PageView) na landing nova — ~15 min, sem backend. Só pra não deixar `aurapoker.com` cego no cutover e começar a acumular público. A integração completa (CAPI/Subscribe/UTM) é **Fase 2, antes do 1º real de mídia paga**, não pré-requisito do dia 10 ([handoff §6](handoff-landing-pixel-migracao.md)).
2. **Domínio confirmado (08/07): `aurapoker.com`** — mesmo domínio do site atual (cutover WP→Azure). O dev instrumenta o pixel/CAPI em `aurapoker.com`; no repoint, o WP para de disparar nesse domínio.
3. **Rafael aceita o alerta do Diagnóstico do dataset** (`aurapoker.com`) e **verifica o domínio no BM** (Adequação e segurança → Domínios) — poucos minutos.

Com 1–3 feitos: a landing sobe no dia 10 já contando cadastro free atribuído por UTM, mesmo com a conta de anúncios zerada. **O launch não depende de ads.**

### Pode vir logo depois (antes do 1º real gasto, sem pressa do dia 10)

4. **Rafael desativa as 3 campanhas antigas (G3)** — fazer ANTES do item 5, sempre.
5. **Rafael ativa 2FA + completa contato de recuperação (G7)** — 10 min, faz a qualquer momento.
6. **Rafael inicia verificação da empresa (G6)** — CNPJ já está cadastrado, é clicar em "iniciar".
7. **Rafael confirma/cria Página do Facebook e adiciona ao BM (G2)** — identidade de anúncio.
8. **Rafael verifica o domínio no BM** (Adequação e segurança → Domínios) — depois do item 2/3 acima.
9. **Thread Mídia Paga recria públicos de retargeting** (engajadores IG 365d, e assim que o pixel novo povoar: visitantes de site + exclusão de convertidos) — custo zero, ver [publicos-diagnostico.md §3](publicos-diagnostico.md).
10. **Thread Mídia Paga sobe a estrutura de [estrutura-campanhas.md](estrutura-campanhas.md) — Fase RTG — pausada** para revisão do Rafael.
11. **Rafael adiciona forma de pagamento/fundos (G1)** — só quando decidir ativar mídia de verdade. Último passo, de propósito: sem saldo, nada roda por engano.
12. Ativação da Fase RTG é 100% decisão e ação do Rafael no Gerenciador — guia sugerido: ≥500 visitantes na landing OU 17/07, o que vier primeiro ([estrutura-campanhas.md §1](estrutura-campanhas.md)).

**MCP da Meta:** fora do caminho crítico — fica parado até depois do launch, conforme decisão em [mcp-meta-identidade.md](mcp-meta-identidade.md). Não afeta nenhum item acima.
