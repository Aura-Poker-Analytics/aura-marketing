# Estratégia Criativa — Launch Aura 2.0 (v2, pivot 2026-07-06)

**Owner:** Rafael (aprova tudo) · **Autor:** Fábrica de posts · **Status:** proposta aguardando aprovação
**Substitui:** o mix de pilares do plano 1.0 **durante o arco de launch**. O plano macro (funil, KPI, conta bilíngue, compliance) segue valendo.

---

## 1. O pivot (decisão do PO, 2026-07-06)

**Fora (por ora):** posts "o pool desvia do MDF/solver" como regra (antigo P1). Sem números de solver
validados no produto, o comparativo é frágil. Volta quando o overlay solver×pool sair (roadmap P6).

**Dentro:** vender a **Aura 2.0 em si** — módulos, filtros, o que o usuário consegue responder,
prints/vídeos da ferramenta, apelo comercial direto. O produto é a estrela; o dado aparece
*dentro da UI mostrada*, não como stat solto.

## 2. Mensagem-mestra do launch

> **Solvers te mostram o equilíbrio. A Aura te mostra o adversário.**
> Aura 2.0: a estratégia real do field de MTT, medida em bilhões de mãos — filtrada por posição,
> stack, buy-in e estágio do torneio. Conta grátis, sem cartão.

Hierarquia de argumentos (usar nessa ordem):
1. **Categoria nova** — não é tracker, não é solver: é inteligência do FIELD.
2. **Escala** — bilhões de mãos de MTT real (nunca citar sites não cobertos; sem prometer GG).
3. **Acionável** — filtros que respondem perguntas de estudo reais em cliques.
4. **Grátis** — plano free permanente (Hotspot vitrine + preflop limitado), upgrade quando bater nas travas.

⚠️ Nunca prometer: win rate/ROI pessoal, "lucro garantido", cobertura de sites que não temos.

## 3. Pilares do arco de launch (substituem o mix 1.0 até 17/07)

| # | Pilar | O que é | Formato |
|---|---|---|---|
| L1 | **Reveal 2.0** | teaser + anúncio: "o mesmo jogo — novas informações" | hero card + story countdown |
| L2 | **Module tour** | 1 carrossel por módulo: PreFlop Analysis, Postflop Analysis, Hotspot | carrossel 5–7 (capa → 3-4 telas/valor → CTA) |
| L3 | **"Você consegue responder…"** | pergunta de estudo real → a tela da Aura que responde | card único com UI + pergunta |
| L4 | **Feature/filtro em destaque** | estágio de torneio, buy-in, Mystery/KO, IP/OOP, sizing %pot, amostra | spotlight card |
| L5 | **CTA free** | plano grátis permanente, sem cartão, link na bio | CTA card / slide final |

Cadência teaser (06–09/07): L1 diário (countdown D-4…D-1) + 1 L3 como aperitivo.
Launch week (10–17/07): D0 = L1 reveal + L2 Hotspot; depois alternar L2/L3/L4, fechar sempre com L5.

## 4. Sistema visual v2 ("mais capricho")

Regras de construção de TODO criativo (o que faltou na v1):

1. **Camadas, nunca fundo chapado:** base slate-950 → glow radial navy → arco da aura (o círculo
   do símbolo, gigante, cortando o quadro, stroke gold com glow) → padrão sutil de naipes/grid
   (~3% opacidade) → conteúdo.
2. **Logo de verdade, em destaque:** wordmark oficial (vetor da fonte custom) — nunca digitar
   "AURA" em Montserrat. Ícone da aura como marca d'água estrutural e como selo.
3. **Produto na imagem:** todo post L2/L3/L4 mostra UI — mock fiel da tela (recriado em HTML) ou
   print real via parâmetro. Moldura de browser/glass card com sombra profunda e borda amber sutil.
4. **Elementos de poker, sóbrios:** naipes como textura, cartas estilizadas simples quando couber
   (ex.: A♠ minimalista), fichas/badges. Nada de dinheiro/luxo (compliance).
5. **Tipografia:** títulos BOLD CAPS Montserrat 800-900 com palavra-chave em gradient amber;
   corpo sentence case slate-300. Fonte custom só via SVG oficial.
6. **Fold/call/raise** apenas com significado semântico (dentro de gráficos da UI).
7. **Rodapé padrão:** ícone + handle + 18+ (+ amostra quando houver número real).

## 5. Templates v2 (este repo, `instagram/templates/`)

| Arquivo | Pilar | Novo? |
|---|---|---|
| `launch-hero.html` | L1 reveal/countdown (feed + story) | novo |
| `carrossel-capa.html` | L2/L3 capa com UI espiando + hook | rebuild |
| `carrossel-slide.html` | L2 slide: painel de UI + título + corpo | rebuild |
| `carrossel-cta.html` | L5 fechamento free | rebuild |
| `feature-spotlight.html` | L3/L4 UI grande emoldurada + bullets | rebuild |
| `stat-card.html` | P1 (em espera até solver) — mantido e re-skinado | rebuild |

Mocks de UI embutidos (parametrizáveis): grid 13×13 de range preflop (heatmap amber), painel
postflop (barras fold/call/raise por sizing), Exploit Card do Hotspot. Todos aceitam
`screenshotSrc` para trocar por print real quando disponível.

## 6. Prints e vídeos reais
- Prints reais do beta exigem sessão logada — pendência: Rafael captura (ou fornece acesso de
  screenshot) das telas Preflop/Postflop/Hotspot em 1920×1080, tema dark, sem dados de cliente.
- Vídeo (reels de navegação na ferramenta) = fase 2 do launch; roteiro sai dos mesmos pilares L2/L3.
- Até lá, os mocks fiéis carregam o visual (rotulados como representação da UI, sem números
  inventados apresentados como dado real — usar "illustrative" quando for mock).

## 7. Compliance (inalterado)
Checklist do plano 1.0 §Compliance vale por post. Números reais só com fonte verificada na hora;
mock de UI = ilustrativo e identificável como tal.
