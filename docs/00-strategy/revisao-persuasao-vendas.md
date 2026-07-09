# Revisão de Persuasão & Vendas — Aura 2.0

**Data:** 2026-07-09 · **Autor:** Fábrica de posts (revisão de especialista solicitada pelo PO)
**Escopo:** todo o aura-marketing (estratégia, programa IG, paid, landing copy) cruzado com o produto
documentado em `aura-context` e a landing em `aura-landing`. Fontes citadas por arquivo.
**Como ler:** §1 é o ranking do que fazer. §2–§9 detalham. Nada aqui viola o compliance vigente
(sem promessa de lucro, sem termos de gambling, sem concorrente nominal, número só verificado).

---

## 1. Sumário executivo — as 10 jogadas, por impacto

| # | Jogada | Impacto | Esforço | Quem |
|---|---|---|---|---|
| 1 | **Consertar integridade de claims** (7 sites / 500M vs bilhões / depoimentos) | 🔴 crítico — confiança é a base de toda persuasão | baixo | Fábrica + dev landing |
| 2 | **Destravar o checkout** (UpgradeModal é `#TODO`) ou ponte concierge | 🔴 crítico — hoje não há como COMPRAR | médio | Dev (fora deste repo; cobrar) |
| 3 | **Reenquadrar o free: "Hotspot completo grátis"** como headline da oferta | alto | baixo | Fábrica + landing |
| 4 | **Ancorar o anual: "menos que um buy-in de $22 por mês"** | alto | baixo | Landing/pricing copy |
| 5 | **Win-back da base morta** (157 contas travadas + ~23 churned Woo) | alto | médio | Precisa de e-mail (gap) |
| 6 | **Comment-to-DM funnel no IG** ("comenta FIELD") | alto | baixo | Rafael opera / ManyChat |
| 7 | **Prova social real** (Discord, marcos de uso, case do leak report) | alto | médio | Fábrica + Rafael |
| 8 | **Rebalancear copy IG: outcome > feature** + save/share prompts | médio | baixo | Fábrica (deck.js) |
| 9 | **Nurture mínimo de 4 e-mails** (free→paid não pode ser 100% mudo) | médio | médio | Precisa de e-mail (gap) |
| 10 | **Bio do IG + destaque fixado** como mini-landing | médio | trivial | Fábrica escreve, Rafael aplica |

---

## 2. Integridade de claims — consertar ANTES de amplificar

Persuasão se apoia em credibilidade. Hoje há três rachaduras que um prospect atento (e o ICP é
grinder analítico — o público MAIS atento que existe) encontra em 2 cliques:

**2.1 "7 sites cobertos" no hero da landing** (`aura-landing/src/content/siteContent.ts:357`).
O próprio doc de produto proíbe: o lake é ~89% família PokerStars e **GG/Party/888 = 0 mãos**
(`aura-context/docs/01-product/landing-positioning.md:9`; parsers prontos ≠ dado carregado,
ADR-010). Um usuário de GG assina, filtra, não acha o field dele, e vira detrator no Discord.
→ **Trocar por claim verdadeiro e ainda forte:** "Milhões de torneios da maior sala do mundo"
ou "+500M mãos auditadas · novas redes a cada trimestre" (cobertura como roadmap, não fato).
Mesma correção vale pro anúncio do Discord se for reaproveitado em post.

**2.2 "Bilhões" (IG) vs "+500M" (landing).** As legendas do programa dizem "bilhões de mãos";
o hero da landing diz "+500M mãos auditadas". O clique sai do post e cai numa página que
contradiz o post — dissonância que custa conversão. → **Regra do número-herói: UM número,
verificado no banco, usado EM TODO LUGAR** (bio, arte, legenda, landing, ads). Ação: puxar o
total real na fonte (regra de ouro) e padronizar. Se o verificado for ~500M, "meio bilhão de
mãos" é honesto e soa grande; "bilhões" sem lastro é passivo de confiança.

**2.3 Depoimentos da landing** (Lucas M., Ana P., "Rafael C. — Head Coach de Stable").
⚠️ Se não forem pessoas reais com autorização, é o risco nº 1 da página: depoimento inventado é
violação de CDC/puffery e, pior, o nicho é pequeno — alguém vai perguntar "quem é Lucas M.?".
→ **Confirmar autenticidade com o PO.** Se não forem reais: remover já e substituir por prova
real (§6). Uma landing sem depoimento é neutra; uma landing com depoimento falso desarma tudo.

**2.4 Higiene interna:** o plano cita "710 users"; a reconciliação de billing de 09/07 mostra
**229 contas** em `AuraBusiness.tbl_user` e **0 assinantes Stripe reais** (~8 pagantes legados
Woo). Nenhum desses números vai pra público, mas as decisões de funil (tamanho de retargeting,
metas) devem usar os reais.

## 3. O funil tem um buraco no caixa

- O fluxo de upgrade in-app termina num **placeholder `#TODO-checkout`**
  (`aura-landing/.../UpgradeModal.tsx`, spec de gating Inc 5). Assinantes Stripe reais: **0**.
- Tradução de vendas: todo o marketing empurra tráfego para uma compra **que não pode ser
  concluída self-serve**. Cada dia de conteúdo antes disso constrói audiência, não receita.
- **Ação imediata (ponte, custo zero):** enquanto o checkout não liga, o botão de upgrade e a
  seção de planos apontam para um canal concierge ("Assine pelo Discord/WhatsApp — resposta em
  minutos"). Vender manualmente 10 assinaturas > mostrar um modal quebrado. Bônus: as conversas
  de venda manuais são pesquisa de objeções de graça.
- **Cobrar do dev** a ligação Stripe (a camada `getTier()` já existe como seam — spec
  trial-gating Inc 4/5). É o item de maior ROI de todo o ecossistema de marketing.

## 4. Oferta: o free está mal contado e o anual está mal ancorado

**4.1 O ativo escondido: Hotspot é COMPLETO no free** (destravado por decisão do PO em 26/06).
A copy atual vende o free como "recorte limitado" (preflop ≤$22, Vanilla, Early) — enquadramento
de restrição. Inverter para enquadramento de entrega:

> ❌ "Plano grátis com recursos essenciais"
> ✅ **"Veja os leaks do field de graça. O módulo Hotspot inteiro — de graça, pra sempre, sem cartão."**

O free deixa de ser "amostra" e vira **um produto com nome e resultado** ("descubra o spot mais
explorável do seu limite em 2 minutos"). O paywall então fica natural: o free mostra QUE o leak
existe; o pago mostra COMO atacar (todas as texturas, sizings, buy-ins) — framing que o próprio
roadmap de produto recomenda (`91-roadmap-produto.md §2.3`).

**4.2 Âncora de preço para o ICP.** Anual $259 ≈ **$21,6/mês** — menos que UM buy-in de $22,
exatamente o limite que o free tier cobre e o field que o cliente joga. A âncora se escreve
sozinha e é compliant (compara com custo, não promete ganho):

> "O plano anual custa menos que um buy-in de $22 por mês."

Usar na seção de planos, no FAQ e no slide de CTA de carrosséis quando falarmos de upgrade.
Complementos: badge "Mais popular" já existe no anual (bom); adicionar **reversão de risco
explícita** ("cancele quando quiser, sem multa") — hoje não aparece em lugar nenhum.

**4.3 Urgência honesta de launch (sem desconto):** "preço de founding member — quem assina no
launch trava $29/mês para sempre; o preço sobe com os próximos módulos (EV, overlay de solver)".
Urgência real (o roadmap de features existe), sem queimar margem nem parecer liquidação.

## 5. Copy do IG — de catálogo de features para máquina de desejo

O programa atual (13 posts) é sólido em consistência e compliance, mas 8 de 13 posts são
**feature-forward** ("o módulo mostra X"). Feature informa; resultado persuade. Ajustes:

**5.1 Rebalancear pilares.** O formato mais persuasivo do lote é o L3 ("Você consegue responder
isso?") — abre um loop de curiosidade, posiciona o produto como resposta e desafia o ego de
estudo do grinder. Hoje são só 2 de 13. → Nas semanas 3–4 (e na sustentação), subir L3 para
~40% do mix. Banco de perguntas pronto no material de produto: bolha/ICM (A2), bounty (A3),
game selection ("qual buy-in é mais explorável?", A4), meta-shift ("o field de 2026 folda menos
que o de 2024?", A1).

**5.2 Toda legenda ganha 2 linhas que faltam:**
- **Save-bait:** "Salva pra revisar antes da próxima session." (save é o sinal que o algoritmo
  mais premia; nosso conteúdo é literalmente material de estudo — pedir save é natural)
- **Pergunta-isca de comentário:** "Qual spot você quer ver o field errando? Comenta aí." —
  comentário alimenta alcance e vira pauta de conteúdo.

**5.3 Comment-to-DM funnel (a alavanca nº 1 de conversão orgânica no IG hoje):**
"Comenta **FIELD** que eu te mando o link da conta grátis no DM." DM > link na bio (menos
fricção, conversa 1:1, pode perguntar o limite que a pessoa joga). Operável manualmente com o
volume atual; ManyChat quando escalar. Requer só padronizar a frase nos posts L5/CTA.

**5.4 CTA por estágio do funil, não one-size:** posts de alcance frio (L3/L4) fecham com
"segue + salva"; posts quentes (L2/L5) fecham com conta grátis; após o marco de prova social,
CTA com social proof embutido ("junte-se aos X grinders").

**5.5 Reels de captura de tela (15–30s) são a prioridade nº 1 pós-lote estático.** Distribuição
fria no IG de 2026 é vídeo. Um screen-record navegando o Hotspot com voice-over PT ("isso aqui
é o field foldando demais no turn — de graça no app") supera qualquer card estático em alcance.
Roteiro = os mesmos L2/L3 já escritos. Sem produção: tela real + legenda automática.

**5.6 Perfil como landing:** fixar 3 posts (o que é a Aura / tour Hotspot / CTA free),
destaques "Módulos · Grátis · FAQ", e bio nova:

> **AURA · Field Intelligence para MTT**
> O que o field REALMENTE faz — +500M mãos [número-herói verificado]
> Hotspot grátis, sem cartão ↓
> aurapoker.com/?utm_source=instagram&utm_medium=organic&utm_campaign=bio

(link direto com UTM, sem linktree — cada clique a menos é conversão a mais).

## 6. Prova social — construir a real, nunca inventar

Hoje: zero depoimentos verificáveis, zero case, comunidade Discord existe mas não aparece no
marketing. Plano de 30 dias, tudo verificável:

1. **Colher no Discord do launch** (o anúncio 2.0 já gerou reação): pedir permissão para
   printar/citar 3–5 mensagens reais. Formato IG: card de quote com o template atual.
2. **Marcos de uso como prova:** quando cruzar marcos reais ("primeiros 100 cadastros da 2.0",
   "X análises rodadas na semana 1" — instrumentação de growth analytics dá isso), postar como
   celebração. Número real + momentum = prova.
3. **Case do leak report concierge** (já em beta): 1 jogador, "encontramos 3 leaks de preflop
   no field dele em 20 minutos" — processo e descoberta, nunca resultado financeiro (compliance).
4. **"Sessão de estudo com a Aura" (pilar P5 do plano)** vira live/reel com um coach convidado —
   prova social emprestada + conteúdo + alcance do convidado.
5. **Substituir os depoimentos da landing** pelos itens 1–3 assim que existirem (ver §2.3).

## 7. Win-back e nurture — o dinheiro que já está na casa

- **157 contas históricas travadas + ~23 churned do Woo + ~8 pagantes legados** (reconciliação
  09/07). São pessoas que JÁ levantaram a mão. Campanha de 2 e-mails: "A Aura que você conheceu
  não existe mais — a 2.0 é outra ferramenta [3 bullets do que mudou]. Sua conta já existe;
  entra de graça." Custo ~zero, provável melhor CPA de todo o launch.
- **Nurture mínimo viável (4 e-mails)** para novos cadastros free: D0 boas-vindas + "roda teu
  primeiro Hotspot em 2 min"; D2 how-to de um módulo; D5 o que o pago destrava (âncora do
  buy-in); D12 case/prova + founding price. Product-led sem NENHUM toque é deixar o churn de
  ativação correr solto.
- **Gap de infraestrutura:** não há ferramenta de e-mail documentada em lugar nenhum. Decisão
  pro PO: Resend/Loops/Brevo etc. — qualquer uma serve; o que importa é existir o canal.

## 8. Landing — ajustes de conversão além dos claims

1. Hero: headline atual descreve a categoria ("Field Intelligence para…"); testar variante
   orientada a resultado: **"Descubra onde o field erra — antes de sentar na mesa."**
2. Seção de planos: liderar com o free reenquadrado (§4.1), âncora do buy-in (§4.2), reversão
   de risco, e **preço em BRL ao lado do USD** (público 100% BR; USD adiciona fricção mental —
   mesmo que a cobrança seja USD, mostrar "~R$ XXX" contextualiza).
3. FAQ: adicionar as 3 objeções que faltam — "Isso é permitido pelas salas?" (é estudo
   populacional anonimizado, não HUD em tempo real), "Serve pro meu limite?" (buy-ins de $0 a
   $1k+), "E se eu não gostar?" (cancela quando quiser).
4. CTA final já é bom ("vantagem real") — repetir a reversão de risco embaixo do botão.

## 9. Métricas de persuasão (fechar o loop)

- Instrumentar (spec de growth analytics já existe): `paywall_shown → upgrade_clicked →
  subscribe` é O funil de vendas; sem ele, otimizamos copy no escuro.
- Ativação = 1ª análise rodada (não o cadastro). Todo o nurture aponta pra isso.
- Revisão semanal (ritual do QG): saves/post, DMs iniciados, cadastros por utm_content,
  paywall CTR. Matar/duplicar criativos por esses números, não por likes.

---

## Anexo — o que já está bom (não mexer)

- Posicionamento de categoria (solver mostra o equilíbrio / Aura mostra o adversário) — é o
  ativo estratégico nº 1, e a seção "A Diferença" da landing executa bem o triângulo
  solver/tracker/Aura sem citar marcas.
- Compliance discipline (18+, sem promessa de lucro, números ilustrativos rotulados).
- Free permanente sem cartão como redutor de fricção do CTA.
- Sistema visual v2 e o pipeline deck.js (velocidade de produção é vantagem competitiva).
- Arte EN + legenda PT-first (opcionalidade de mercado sem custo).
