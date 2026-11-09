---
name: diagnostico-midia-paga
description: Diagnóstico diário/semanal das campanhas pagas da Aura a partir das métricas e do playbook de mídia paga, sem tocar nas campanhas. Usar quando o Rafael perguntar "como está o tráfego pago", pedir "diagnóstico de campanha" ou "vale reativar".
---

# Diagnóstico de mídia paga

## Ler primeiro (caminhos reais, não repetir conteúdo aqui)
- `docs/02-paid/PLAYBOOK-midia-paga-do-zero.md` — §4 (gates de saúde, não performance) e §8 (anti-padrões documentados, `8.1`–`8.6`; `8.6` é o caso mais caro, campanha DISC02-EU).
- `docs/02-paid/analise-campanhas-historicas.md` e `docs/02-paid/auditoria-meta-ads.md` — histórico de gasto/CTR/CPC/CPM já auditado, conta `1598770224460932` ("Aura Business").
- CSVs na raiz do repo (`Jun-25-2026_Jul-22-2026_*.csv`) — **atenção:** são exports de Insights do Instagram (orgânico: alcance, curtidas, visitas ao perfil), não gasto/CPA de campanha paga. Ver `content/README.md` ("Fora de pasta"), que já sinaliza isso e sugere mover para `docs/02-paid/insights/` — não movido ainda.
- Para números de gasto/CPA/CPM reais de campanha, puxar ao vivo via Meta Marketing API (skill `meta-ads-doctor` já instalada neste repo, usa as tools `mcp__f3ba1470...ads_*`), não confiar em CSV local desatualizado.
- `.claude/skills/meta-ads-doctor/references/statistical-thresholds.md` — necessário para não declarar vencedor/perdedor com amostra insuficiente (ver corolário estatístico do §8.6 do playbook).

## Passos
1. **Ler as métricas do período** pedido (dia/semana): puxar via Meta Marketing API (meta-ads-doctor) o que estiver ativo ou pausado na janela, e cruzar com o histórico já auditado nos docs acima.
2. **Comparar com os gates do playbook** (§4): CPM na faixa esperada, frequência, CTR, conversões vs. orçamento gasto — nunca julgar performance antes do gate de ~50% do orçamento definido para a campanha.
3. **Verificar contra cada anti-padrão do §8** antes de recomendar qualquer mudança — em especial `8.6` (não mexer em configuração sem janela limpa) e `8.3` (CPM barato pode ser sinal ruim, não bom). Citar o anti-padrão pelo número quando ele se aplicar.
4. **Saída em tabela** de até 10 linhas: `campanha | gasto | resultado | gate | recomendação`.
5. **Nunca criar, pausar ou editar campanha nesta sessão.** Apenas recomendar — o Rafael executa ou aprova explicitamente no Gerenciador de Anúncios antes de qualquer ação.

## Contexto fixo
A mídia paga foi **pausada em 15/09/2026** após R$ 1.500 gastos sem gerar assinante — qualquer recomendação de reativação precisa justificar o que mudaria desta vez (ver §8.6 do playbook: reativar sem gate definido antes de olhar o resultado é o próprio anti-padrão que já custou caro aqui).

## Regras fixas
- Modelo: Sonnet. Candidata a rotina agendada (diária ou semanal).
- Nada em produção, billing ou gasto sem aprovação explícita do Rafael naquele turno.
