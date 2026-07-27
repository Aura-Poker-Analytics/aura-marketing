# Calendário orgânico — 30 dias (26/07 → 24/08)

**Montado em 2026-07-25.** Pronto pra agendar no **Meta Business Suite → Planejador**.
⚠️ **Não é possível agendar via MCP** — o servidor conectado é o de *anúncios*, não de publicação de conteúdo. Agendamento é manual (~20 min pro mês inteiro).

## Links com UTM (copiar e colar)

**Bio (fixo, trocar uma vez só):**
```
https://www.aurapoker.com/?utm_source=instagram&utm_medium=bio&utm_campaign=organico
```

**Story (um por peça — o `utm_content` diz qual story gerou o clique):**
```
https://www.aurapoker.com/?utm_source=instagram&utm_medium=story&utm_campaign=organico&utm_content=SLUG
```
Trocar `SLUG` pelo nome da pasta da peça (ex.: `cbet-reaction`). Isso aparece no `tbl_user` e me deixa dizer qual story converteu.

> **Sempre `www.`** — sem isso o redirect da GoDaddy come os UTMs.

---

## Semanas 1–2 — conteúdo PRONTO (arte + copy)

| Data | Peça | Ângulo | Story + link |
|---|---|---|---|
| **26/07** | `cbet-reaction` | postflop real · veia leak *(o ângulo de maior alcance no histórico)* | ✅ `utm_content=cbet-reaction` |
| **29/07** | `escala-500m` | prova/escala | ✅ `utm_content=escala-500m` |
| **31/07** | `reg-vs-fish` | perfil de vilão | ✅ `utm_content=reg-vs-fish` |
| **02/08** | `textura-muda-o-field` | leak/textura | ✅ `utm_content=textura-muda-o-field` |
| **05/08** | `size-mais-usado` | postflop | ✅ `utm_content=size-mais-usado` |
| **07/08** | `postflop-sizings` | postflop | ✅ `utm_content=postflop-sizings` |

**Ordem não é aleatória:** abre com `cbet-reaction` porque a veia leak/Hotspot foi a de maior alcance no histórico (440), e intercala postflop com outros ângulos pra não repetir tema em sequência.

## Semanas 3–4 — precisa de render

| Data | Peça | Estado |
|---|---|---|
| **09/08** | `carrossel-tour-modulos` | 🟡 em `To do/` — conceito+copy, falta render |
| **12/08** | `reel-04-bubble` | 🟡 roteiro pronto, falta produzir *(prioridade — reel é o formato de maior alcance)* |
| **14/08** | `carrossel-ler-exploit-card` | 🟡 em `To do/` — falta render |
| **17/08** | `cta-preview-board` | 🟡 em `To do/` — falta render |
| **20/08** | ⬜ **GAP** | sem peça |
| **23/08** | ⬜ **GAP** | sem peça |

## ⚠️ O gap de conteúdo

**Pronto pra agendar hoje: 6 peças (~2 semanas).** Depois disso depende de produção:
- 3 peças em `To do/` precisam de render
- `reel-04-bubble` precisa ser produzido
- **Faltam ~2 peças** pra fechar os 30 dias

Duas saídas: pedir à fábrica um lote pequeno de reposição, **ou** esticar a cadência pra 1 post a cada 3 dias nas semanas 3–4 (aceitável — o feed nesse período serve mais como prova de vida do que como aquisição).

## Stories (2–3×/semana)

Não precisam ser peça nova. O mais eficiente:
1. **Story do post do dia** — republica o card com o sticker de link *(é o motor de clique: 11 cliques num story vs. o feed inteiro do mês)*
2. **Story avulso** no meio da semana — bastidor, print de tela, número solto do produto
3. Sempre com **sticker de link + UTM** da tabela acima

## Como conferir se funcionou

Roda no `tbl_user` a qualquer momento (eu faço):
```sql
SELECT utm_medium, utm_content, COUNT(*)
FROM tbl_user WHERE utm_campaign='organico'
GROUP BY 1,2 ORDER BY 3 DESC;
```
Isso mostra **qual story/peça gerou cadastro** — não só clique.

## Nota de sobreposição com o pago
A campanha `AURA-DISC01` roda em paralelo, mas **não conflita**: o pago é topo de funil (conceito, 4 ganchos de descoberta) e o orgânico é meio de funil (feature/tour, pra quem já entende). Medição separada por `utm_medium` (`paid` vs `bio`/`story`).
