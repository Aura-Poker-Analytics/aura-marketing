# Medição, Valor e Otimização — Tráfego Pago

**Autor:** thread Mídia Paga · **Data:** 2026-07-08
**Para quê:** amarrar eventos → objetivos de campanha → KPIs → regras de decisão. É a peça que fecha a estrutura de tráfego pago: os outros docs dizem *o que subir*; este diz *como ler e otimizar*.

Base: [pixel-capi-spec.md](pixel-capi-spec.md) (eventos) · [estrutura-campanhas.md](estrutura-campanhas.md) (fases/orçamento) · [publicos-build-spec.md](publicos-build-spec.md) (públicos) · oferta auditada no Stripe (§3).

---

## 1. O funil e os eventos

```
Impressão/clique (Meta)  →  PageView  →  CompleteRegistration  →  Subscribe
        │                     │              (conta free)          (assinatura paga)
     mídia paga          landing              KPI NORTE            KPI de receita
```

| Evento | Onde | Papel na otimização |
|---|---|---|
| `PageView` | browser | base de retargeting (públicos de site) + denominador de conversão |
| `CompleteRegistration` | browser + CAPI (dedup) | **evento de otimização principal** das campanhas de conversão (RTG/F1/F2) |
| `Subscribe` | CAPI (webhook Stripe) | evento de **valor**; otimização por valor/receita quando houver volume |

## 2. Hierarquia de KPI

1. **KPI norte:** **conta free atribuída via UTM** (`CompleteRegistration` casado ao UTM na AuraBusiness). É o que decide se a mídia funciona.
2. **KPI de receita:** `Subscribe` (assinatura paga) e sua taxa a partir da conta free (free→paid).
3. **Diagnóstico (não-meta):** CPM, CTR, frequência, custo por engajador (topo de funil / boost do reveal).
4. **Vaidade (ignorar como meta):** seguidores, curtidas, alcance bruto.

⚠️ **Fonte da verdade = AuraBusiness (UTM), não o Ads Manager.** O Gerenciador superconta conversão (view-through, janelas largas). O número que vale pra decisão é conta free por UTM no banco.

## 3. Valor da oferta (pra ROAS/LTV — do Stripe)

Produto único **"AURA Plano Individual"**, **USD**:

| Plano | Preço | Normalizado /mês |
|---|---|---|
| Mensal | **$29/mês** | $29 |
| Semestral | **$149/6m** | ~$24.8 |
| Anual | **$259/ano** | ~$21.6 |

- `Subscribe.value` = valor do 1º ciclo cobrado; `currency = usd`.
- **LTV proxy inicial** (até ter churn real): use o mensal como piso (~$29) e o anual como teto de intenção (~$259/ano). Refine com a taxa de retenção quando houver base.
- **Cobrança em USD** (não BRL) — impacto: (a) `Subscribe` reporta USD; (b) no BR, o preço aparece em dólar — não prometer ganho, mas a transparência de preço é decisão de copy da landing, não da mídia.

## 4. Que evento otimiza cada fase

| Fase (estrutura-campanhas.md) | Objetivo Meta | Otimiza por |
|---|---|---|
| BOOST reveal (launch-hero) | Alcance/Engajamento | — (semear público; ver [launch-hero-trafego.md](launch-hero-trafego.md)) |
| RTG (retargeting quente) | Vendas/Conversões | `CompleteRegistration` |
| F1 frio BR | Conversões | `CompleteRegistration` |
| F2 frio EN | Conversões | `CompleteRegistration` |
| (futuro) escala por valor | Conversões (value) | `Subscribe` / valor — só com volume de assinatura suficiente |

**Regra de learning:** ad set precisa de ~10 conversões do evento otimizado por semana pra sair do aprendizado. Se `CompleteRegistration` < 10/sem por 2 semanas → cair pra otimização por "cliques no link"/visitas até o volume voltar (fallback já previsto em estrutura-campanhas.md §6). Não otimizar por `Subscribe` enquanto o volume de assinatura for baixo (será, no começo).

## 5. Regras de decisão (guard-rails)

- **CPA de referência:** definir na 1ª semana de dados (custo por conta free via UTM). Antes disso, não há alvo — é calibração.
- **Kill-switch:** CPA > 3× a referência da fase por 7 dias corridos → pausar/revisar (o Rafael executa; agente só sinaliza).
- **Orçamento:** mudança > 20%/dia reseta learning → ajustar no máx. 1×/semana.
- **Teto da conta:** limite diário R$105,49 hoje (sobe com histórico) — somar BOOST + RTG não pode estourar ([auditoria-meta-ads.md](auditoria-meta-ads.md)).
- **Exclusão universal:** todo ad set de conversão exclui `Convertidos CompleteRegistration 180d` ([publicos-build-spec.md](publicos-build-spec.md) P5) — não pagar por quem já criou conta.

## 6. Ritual semanal (sexta, com o QG)

Ler, nesta ordem:
1. **AuraBusiness:** contas free por UTM (por campanha/criativo) + free→paid (`Subscribe`).
2. **Ads Manager:** gasto, CPM, CTR, frequência — só pra diagnosticar *por que* o nº 1 está como está.
3. **Decisão:** manter / trocar criativo / ajustar público / pausar — segundo os guard-rails do §5.
4. Registrar o que mudou (pra não resetar learning por capricho).

## 7. Pré-condições pra este playbook rodar

- Eventos instrumentados na landing nova ([handoff-landing-pixel-migracao.md](handoff-landing-pixel-migracao.md)) — `CompleteRegistration` deduplicado e `Subscribe` do Stripe chegando.
- UTM persistido até a conta (senão o KPI norte não fecha).
- Públicos criados ([publicos-build-spec.md](publicos-build-spec.md)).
- Pré-requisitos de conta OK ([readiness-dia10.md](readiness-dia10.md)).

Sem isso, otimização é chute. Com isso, cada real gasto vira leitura.
