# Auditoria Meta Business — estado atual vs. pronto pro dia 10/07

**Autor:** thread Mídia Paga · **Auditado em:** 2026-07-04, via Business Suite logado (somente leitura — nada foi alterado)
**Veredito:** a fundação existe e é melhor que o esperado (BM próprio, conta com histórico, pixel ativo). Faltam **5 ações manuais do Rafael**, nenhuma bloqueia o launch da landing em si — mas 3 bloqueiam o primeiro real de mídia.

---

## 1. O que existe (inventário)

| Ativo | Status | Detalhe |
|---|---|---|
| **Business Manager** | ✅ Existe | "Aura Poker Analytics", ID `830069129552748`. Rafael único admin (acesso total, inclusive finanças) |
| **Conta de anúncios principal** | ✅ Ativa | "Aura Business", ID `1598770224460932`, BRL, propriedade do BM. **Com histórico de gasto** (mar/2026, pré-pago, valores pequenos — bom: conta não é "virgem", reduz atrito de conta nova) |
| **Conta de anúncios secundária** | ⚠️ **CORRIGIDO 2026-07-12** | ID `1210943484403967`, sem nome — mas **NÃO ociosa**: tem o **pixel `1405949840871947` + dataset + Instagram conectados** (provável auto-criada pelo "Turbinar" do IG). O pixel estava aqui, não na Aura Business. **Decisão: oficial = Aura Business `1598770224460932`;** conectar o pixel nela e abandonar/renomear esta. Ver [publicos-build-spec.md §0](publicos-build-spec.md) |
| **Instagram** | ✅ Conectado | @aurapokeranalytics (ID 17841468976680108), propriedade do BM, 710 seguidores. Sem post há 60d (teaser 06/07 resolve) |
| **Página do Facebook** | ❌ **Nenhuma no BM** | Lista de Páginas vazia. A home do Business Suite opera só com o IG. Ver gap G2 |
| **Pixel/Dataset** | ✅ Existe e recebe | "Aura – Website Data Set", ID `1405949840871947`, browser pixel em `aurapoker.com`. PageView ativo (últimas 5h!), InitiateCheckout/AddToCart parados há 9d (site antigo). **Sem CAPI** |
| **Método de pagamento** | ❌ Nenhum | Modelo pré-pago, saldo **R$ 0,00**. Limite diário imposto pela Meta: R$ 105,49 (sobe com histórico) |
| **Campanhas antigas** | ⚠️ 3 na conta | "Apresentando a Aura - 2026" e "Video Preflop Youtube": **toggle LIGADO + "Erro no pagamento"** (não rodam só porque não há saldo). "Apresentando a Aura - Engajamento": desativada |
| **Domínios verificados** | ❌ Nenhum | E o Diagnóstico do dataset pede confirmação do domínio `aurapoker.com` (alerta desde 04/06) |
| **Verificação da empresa** | ❌ Não iniciada | Central de Segurança: "Qualificada para verificação" — botão disponível. Dados fiscais já cadastrados na cobrança (AURA ANALYTICS LTDA, CNPJ 55.998.551/0001-88, Curitiba) |
| **Segurança do BM** | ⚠️ Frágil | 2FA: "Ninguém" obrigado. Admin único, sem contato de recuperação ("faltam informações de contato") |

## 2. Gaps e plano de fechamento

### Bloqueiam o 1º gasto (não o launch da landing)

- **G1 — Método de pagamento ausente.** Ação Rafael (Cobrança e pagamentos → Adicionar forma de pagamento). ⚠️ **FAZER O G3 ANTES** — no modelo pré-pago o risco é menor (sem saldo, nada roda), mas a ordem segura é: desativar campanhas antigas → só então adicionar pagamento/fundos.
- **G2 — Sem Página do Facebook no BM.** Anúncio via Gerenciador precisa de identidade (Página). Confirmar se existe Página fora do BM (a home do Business Suite referencia asset `808012409059298` — pode ser uma Página antiga vinculada ao IG); se existir, adicionar ao portfólio; senão, criar Página mínima "Aura Poker Analytics" (logo, categoria Software, link) só como identidade de anúncio. 15 min.
- **G3 — Campanhas antigas armadas.** Duas campanhas com toggle ligado seguradas apenas pelo "erro no pagamento". Ação Rafael no Gerenciador: **desativar as 3** antes de qualquer saldo entrar. (Não mexi em nada — regra da thread: leitura apenas.)

### Bloqueiam a mensuração (idealmente prontos ATÉ 10/07)

- **G4 — CAPI + eventos novos na landing.** Spec pronta pro dev em [pixel-capi-spec.md](pixel-capi-spec.md) — repassar HOJE. Sem isso o KPI norte (conta free via UTM) nasce cego.
- **G5 — Domínio.** (a) Aceitar o alerta do Diagnóstico do dataset (allowlist `aurapoker.com`); (b) verificar domínio no BM (Adequação e segurança → Domínios → meta-tag ou DNS TXT). Confirmar antes qual é o domínio final da landing.

### Higiene (essa semana, 20 min, reduz risco de bloqueio)

- **G6 — Verificação da empresa.** Central de Segurança → Iniciar verificação (CNPJ já está lá). É também o pré-requisito do plano B de compliance ([compliance-meta.md](compliance-meta.md) §4).
- **G7 — 2FA obrigatório + contato de recuperação + (opcional) 2º admin de confiança.** BM com admin único sem 2FA é o modo mais comum de perder tudo — e restrição por segurança bloqueia ads igual restrição por policy.

## 3. Checklist "pronto pro dia 10" (ordem sugerida)

**Rafael, no Business Manager (~40 min total):**
1. [ ] Desativar as 3 campanhas antigas (G3)
2. [ ] Ativar 2FA + completar informações de contato (G7)
3. [ ] Iniciar verificação da empresa (G6)
4. [ ] Confirmar/criar Página FB e adicionar ao BM (G2)
5. [ ] Confirmar domínio no Diagnóstico do dataset + verificar domínio no BM (G5)
6. [ ] (Só quando decidir ativar mídia — pós-launch:) adicionar forma de pagamento/fundos (G1)

**Dev da landing (antes de 10/07):**
7. [ ] Implementar [pixel-capi-spec.md](pixel-capi-spec.md) e rodar o checklist de aceite (§6)

**Thread Mídia Paga (Fase B, só com GO + orçamento):**
8. [ ] Subir estrutura de [estrutura-campanhas.md](estrutura-campanhas.md) — tudo pausado — pra revisão e ativação do Rafael
