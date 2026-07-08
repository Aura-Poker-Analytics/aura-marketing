# Tráfego Pago — Launch Hero (Reveal Aura 2.0)

**Autor:** thread Mídia Paga · **Data:** 2026-07-08 · **Status:** proposta para decisão do PO (tudo pausado)
**Contexto da mudança:** decisão do PO (2026-07-08) elimina a fase de teaser/countdown — entramos direto com
posts de lançamento. O criativo em avaliação é `launch-hero` (L1, reveal "O MESMO JOGO — NOVAS INFORMAÇÕES" +
CTA "Crie sua conta grátis"), já renderizado em:

- Feed 4:5 — `instagram/output/2026-07-06-templates-v2/launch-hero.png` (1080×1350)
- Story/Reels 9:16 — `instagram/output/2026-07-06-templates-v2/launch-hero-story.png` (1080×1920)

(confirmados via Glob nesta sessão — não analisei o pixel da imagem, só a existência dos arquivos)

**Regra absoluta, vale para tudo abaixo:** qualquer objeto criado sobe **PAUSADO**. Ativação e gasto são
exclusivos do Rafael (PO). Este doc não ativa nada.

---

## 0. A tensão (por que isto não é um "sim" automático)

`estrutura-campanhas.md` §0 e §4 são explícitos: o pago **recicla vencedores do orgânico** (30–45d de
validação) e reusa **stat/feature cards** — não estreia conceito, não empurra branding. O `launch-hero` é
exatamente o oposto disso: é o criativo de marca/reveal, zero validação orgânica (ainda nem foi postado),
sem número verificado embutido (a mensagem é posicionamento, não stat).

Ao mesmo tempo, `publicos-diagnostico.md` mostra a fase RTG **faminta de público**: semente de seguidores
IG < 1.000 (D1), base 100% BR (D4), zero público de site ainda (D6 — só existe depois que a landing subir e
o pixel povoar). A RTG só vira útil quando existir "gente quente" suficiente para reciclar — e hoje quase
não existe.

**A pergunta real não é "o reveal merece verba" — é "o reveal merece verba para *qual objetivo*".** Como
reveal de marca sem validação, ele é candidato fraco a otimização por cadastro (§4 do plano macro pede
criativo validado para isso). Como *semeador de público* para a RTG faminta, ele é candidato razoável — a
única coisa que ele precisa fazer é ser visto e engajado pelo público certo, não converter.

---

## 1. Avaliação das 3 opções

### Opção 1 — Só orgânico (fiel ao plano)

O reveal roda 100% orgânico; verba paga espera o 1º stat/feature card vencer no orgânico (critério de
`estrutura-campanhas.md` §4: top saves + alcance no IG Insights).

**Prós:** disciplina total com o princípio "pago recicla, não estreia" (§0/§4). Zero risco de queimar verba
em criativo não testado. Zero exposição adicional ao classificador de policy antes do fluxo de compliance
estar rodado uma vez no orgânico.

**Custo de oportunidade real:** o launch é o único momento em que "O MESMO JOGO — NOVAS INFORMAÇÕES" tem
sentido — é um evento, não repete. Com base orgânica de 710 seguidores e alcance dependente de distribuição
orgânica do IG (que penaliza contas paradas — sem post há 60d, conforme auditoria), o reveal pode alcançar
uma fração pequena do público endereçável na única semana em que a mensagem de "lançamento" é literalmente
verdade. Esperar 30–45d de validação significa que a RTG (que já está sequenciada para abrir ~17/07, guiada
por ≥500 visitantes ou essa data) segue com semente de público paupérrima justamente na janela em que ela
mais precisa de gente para reciclar. Ou seja: escolher a Opção 1 não é "neutro" — é aceitar que a fase RTG
nasce mais fraca do que precisava, e que o momento de maior tração de marca (o lançamento em si) não teve
nenhum empurrão pago, mesmo que pequeno e não voltado a conversão.

### Opção 2 — Boost de alcance/engajamento do reveal (topo de funil) — **RECOMENDADA**

Tese: usar o reveal para semear o público quente que a RTG vai reciclar — sem otimizar por cadastro. Isso
não viola §0/§4 no sentido de "reciclar vencedor para vender", porque o objetivo aqui **não é venda, é
alcance/engajamento** — uma categoria de mídia diferente da fase de conversão (RTG/F1/F2). É reconciliável
com o princípio geral se o objetivo Meta escolhido for `Awareness`/`Engagement` (ou `Traffic` sem otimizar
para landing), nunca `Conversions`.

Ver plano operacional completo na §2.

**Por que não é a Opção 3:** o reveal não tem stat verificado, não foi validado, e a mensagem é
posicionamento — não pede ação de "criar conta agora" com a mesma urgência que um stat card ("o pool foldou
X% aqui — e você?"). Otimizar `CompleteRegistration` num criativo de marca gasta o orçamento de aprendizado
do algoritmo (que precisa de sinal de conversão) num criativo que não foi desenhado para arrancar esse
sinal.

### Opção 3 — Direto para conversão (CompleteRegistration) no reveal

**Por que não fazer isso agora:** o algoritmo de Conversions precisa de volume de sinal (`CompleteRegistration`)
para sair do learning — com público pequeno e um criativo de marca (não um gancho de stat/dor), a taxa de
conversão esperada é a mais baixa do catálogo de criativos possíveis. Gastar o "learning budget" logo no
primeiro objeto pago do histórico da conta é o pior lugar para queimar isso. Além disso, fura o princípio
§0/§4 diretamente: reciclar vencedor é precisamente o mecanismo que a estrutura de campanhas usa para
garantir que o dinheiro de conversão vai atrás de criativo que já provou tração — o reveal não passou por
esse filtro.

**Quando reconsiderar:** se, na prática, o reveal viralizar no orgânico (alcance/saves muito acima da
média da conta) nos primeiros 2-3 dias — nesse caso ele "se qualifica" como vencedor validado rápido e pode
entrar na fila de reciclagem antecipada. Mas isso é decisão a posteriori, não a proposta deste doc.

---

## 2. Plano operacional (Opção 2 — recomendada)

| Parâmetro | Definição |
|---|---|
| **Objetivo Meta** | Reconhecimento de marca / Engajamento (Awareness ou Engagement) — **nunca Conversões**. Se o Gerenciador só oferecer "Tráfego", usar sem otimizar para evento de conversão (otimizar por LinkClick, não por CompleteRegistration) |
| **Não otimizar por** | Cadastro/CompleteRegistration — isso é papel da RTG, não deste boost |
| **Público** | Ver tabela de públicos abaixo — prioridade: engajadores IG (P1 de `publicos-diagnostico.md`, criar se ainda não existir) + broad BR 18+ leve por interesse. Não usar o público salvo #4 (`Aura Business`) — está sobre-empilhado (D3) e não usar lookalikes ainda (D1: semente <1.000, ruidosa) |
| **Posicionamentos** | Feed IG + Stories/Reels IG, manual. **Sem Audience Network / FB right column** — sem Página FB ativa e o criativo é 100% IG-nativo (mesma regra da RTG, §1 de `estrutura-campanhas.md`) |
| **Formatos** | 1080×1350 (feed) já renderizado; 1080×1920 (story/reels) já renderizado. Sem variação de movimento ainda — considerar versão com zoom leve se este boost validar bem (nota de `estrutura-campanhas.md` §4: movimento rende CPM melhor em stories) |
| **Duração** | Curta e concentrada: 3–5 dias corridos cobrindo o lançamento (janela 10–14/07). Reveal é evento, não campanha contínua — depois disso a verba de topo de funil cede lugar à RTG |
| **UTM** | Ver §4 |

### Público — opções concretas

| Público | Fonte | Tamanho estimado | Uso aqui |
|---|---|---|---|
| Engajadores IG 365d | Criar agora (P1 de `publicos-diagnostico.md` — ainda não existe, só o "seguidores" antigo) | Maior que o público #1 atual (<1.000), mas ainda pequeno — confirmar tamanho no Gerenciador antes de subir | Prioridade 1 — é público que já demonstrou afinidade, barato de alcançar, e vira insumo de lookalike melhor depois (P7) |
| Broad BR 18+ leve (Advantage+ audience, sem interesse) | Novo — deixar o algoritmo achar quem engaja | Grande (BR 18+ irrestrito) | Prioridade 2 — usar só se o orçamento permitir 2º ad set; serve para não depender só da base minúscula de engajadores |
| Interesses poker BR (Poker, Texas Hold'em, PokerStars, GGPoker, WSOP) | Novo, limpo (sem cruzar com cargo — lição de D3) | Confirmar (tipicamente 1–5M no Gerenciador) | Prioridade 3, opcional — mais alinhado a "achar gente de poker" que a broad, mas broad geralmente ganha em custo (nota de §2 de `estrutura-campanhas.md`) |
| Lookalike (#2/#3 existentes) | Existente | Indisponível/não confiável (D1) | **Não usar neste boost** — semente fraca, risco de desperdiçar verba num público ruidoso |
| Público salvo "Aura Business" (#4) | Existente | Indisponível, provavelmente irrisório | **Não usar** — está sobre-empilhado (D3), precisa ser desmontado primeiro (P3) |

### Orçamento — opções para decisão do Rafael (formato §5 de `estrutura-campanhas.md`)

Premissas: CPM IG BR R$15–30 (mesma referência da RTG); público de engajadores pequeno satura rápido;
objetivo aqui é alcance/frequência controlada, não volume de cliques. Números são ordem de grandeza, não
promessa.

| Opção | R$/dia | R$/total (3–5 dias) | O que compra | Leitura |
|---|---|---|---|---|
| A 💡 | **20** | ~60–100 | ~1–1.5k impressões/dia no público de engajadores; frequência controlada sem saturar em 1 dia | **Recomendada.** Público de engajadores é pequeno — mais verba vira frequência alta rápido, não mais alcance útil |
| B | 35 | ~105–175 | Alcance um pouco maior + abre espaço para o 2º ad set (broad BR leve) rodar em paralelo | Se quiser testar broad BR junto do público de engajadores desde o dia 1 |
| C | 60 | ~180–300 | Satura o público de engajadores em ~1–2 dias; força a migrar cedo para broad | Não recomendo — é orçamento de F1 (frio), não de um boost de topo de funil de 3–5 dias |

**Guard-rail:** este boost usa o mesmo teto de guard-rail geral do §5 (`estrutura-campanhas.md`) — não é
orçamento adicional "livre", é a primeira fatia do orçamento de mídia paga do launch. Se o Rafael aprovar
RTG e este boost na mesma semana, o total combinado deve ser avaliado contra o limite diário da conta
(R$105,49/dia hoje, conforme `auditoria-meta-ads.md`).

### Como medir se "semear público" valeu

Não usar CPA/cadastro como métrica de sucesso deste boost — não é o objetivo. Métricas corretas:

- **Custo por engajador retido**: gasto total ÷ (curtidas + comentários + compartilhamentos + saves +
  novos seguidores durante o período). Objetivo: comparar contra o custo orgânico equivalente (proxy: se
  fosse caro alcançar essa quantidade de engajamento organicamente, o boost valeu).
- **Tamanho do público quente gerado**: variação no tamanho do público "Engajadores IG 365d" (P1) antes vs.
  depois do boost — é o público que a RTG recicla. Sucesso = crescimento mensurável (dobrar a base de <1.000
  já é significativo).
- **Frequência**: não deixar passar de ~4–5 no período — sinal de saturação, não motivo para aumentar
  orçamento.
- **NÃO contar como sucesso:** CompleteRegistration gerado incidentalmente (é bônus, não meta — pode até
  acontecer via link na bio/CTA do card, mas não é o KPI deste objeto).

Revisão: no fim da janela (dia 14 ou 15/07), registrar os números acima e decidir se o padrão se repete em
próximos posts de reveal/marca (module tour L2, por exemplo).

---

## 3. Status dos pré-requisitos (§7 de `estrutura-campanhas.md`)

Puxado de `auditoria-meta-ads.md` (auditoria de 2026-07-04) — não inventei nenhum status novo.

| Pré-requisito | Status em 04/07 | Bloqueia subir pausado? | Bloqueia ativar (gasto)? |
|---|---|---|---|
| Método de pagamento na conta | ❌ Nenhum, saldo R$0,00 | Não | **Sim** — sem saldo, nada roda mesmo se ativado |
| Domínio confirmado no dataset | ❌ Pendente (alerta desde 04/06) | Não | Sim — mensuração nasce capenga sem isso |
| Eventos da landing validados (pixel-capi-spec.md §6) | ⚠️ Pendência do dev — não há confirmação de que rodou | Não | Sim — sem `CompleteRegistration` validado, não dá pra saber se este boost (ou qualquer coisa) gerou público que depois converteu |
| Campanhas antigas com erro desativadas | ⚠️ 3 campanhas "erro no pagamento" ainda ligadas (G3) | Não diretamente, mas **fazer antes de adicionar pagamento** (ordem seguida na auditoria: desativar → só então método de pagamento) | Sim, indiretamente — risco de reativação acidental ao entrar saldo |

**Conclusão de status:** nenhum destes bloqueia **subir o objeto pausado** (que é o único passo que este doc
propõe agora). Todos os quatro bloqueiam **ativar/gastar** — coerente com o estado já mapeado na auditoria.
**O que destrava:** os itens 1–5 do checklist "pronto pro dia 10" em `auditoria-meta-ads.md` §3, sob
responsabilidade do Rafael no Business Manager, mais o item 7 (dev da landing rodar o checklist de aceite
do pixel/CAPI). Nenhuma ação nova aqui — apenas reforçando que continuam pendentes conforme a última
auditoria. **Recomendo reconfirmar esses status no Gerenciador antes de ativar** — a auditoria é de 04/07 e
pode estar defasada; marcar "confirmar" para qualquer coisa que não foi checada de novo nesta sessão.

---

## 4. UTM proposto

Coerente com o naming de `estrutura-campanhas.md` §0 (`AURA_<FASE>_<GEO>_<OBJETIVO>`) e com a convenção de
`pixel-capi-spec.md` §4.

| Param | Valor proposto |
|---|---|
| `utm_source` | `meta` |
| `utm_medium` | `paid_social` |
| `utm_campaign` | `launch20_reveal` |
| `utm_content` | por formato/ad: `hero_feed_1350` / `hero_story_1920` (e variante com movimento, se criada: `hero_story_1920_motion`) |

Nome de campanha no Gerenciador (mesma convenção): `AURA_BOOST_BR_ALCANCE` (fase "BOOST" nova, para deixar
explícito no naming que não é RTG nem F1 — é o objeto de topo de funil do reveal). Ad set:
`ig_engajadores365d_launch` / `broad_br18_launch`. Ad: `l1_launchhero_feed` / `l1_launchhero_story`.

---

## 5. Ajustes de criativo/copy para a versão PAGA (vs. o post orgânico)

O post orgânico já foi desenhado dentro do brand kit e do `compliance-meta.md`. Para a versão **paga**,
reforçar por dois motivos: (a) mídia paga expõe o criativo à revisão automática da Meta, que "classifica
por sinais superficiais" (`compliance-meta.md` §3); (b) o texto de acompanhamento do anúncio (o campo de
"texto principal" no Gerenciador, além do próprio card) é superfície nova que o post orgânico não tinha.

**Releitura de risco do reveal especificamente:** o card em si (`launch-hero.html`) usa a copy
`"Field intelligence for MTT grinders — the pool's real strategy, measured across billions of hands"` +
CTA `"Crie sua conta grátis"` — sem menção a dinheiro, sem "win rate", sem "$". Isso já está alinhado ao
argumento "SaaS de estudo" do `compliance-meta.md` §2. O termo "poker"/"MTT" aparece mas é esperado e aceito
(coaching sites anunciam assim há anos, conforme o próprio doc). **Avaliação: risco baixo no card, mas o
texto de acompanhamento do anúncio (campo separado no Gerenciador) precisa do mesmo cuidado** — é ali que
erros de redator costumam vazar linguagem de "ganhe"/"lucre".

**Ajustes recomendados para a peça PAGA (não mudar o post orgânico):**

- [ ] Texto de acompanhamento do anúncio usa vocabulário de "estudo/dados/decisão" — nunca "ganhe", "lucre",
      "suba de banca". Sugestão de texto: *"A Aura 2.0 chegou: estatísticas reais do field de MTT, filtradas
      por posição, stack e estágio — pra estudar o adversário, não decorar o equilíbrio. Conta grátis, sem
      cartão."*
- [ ] Não adicionar imagem/elemento extra de dinheiro, fichas como riqueza ou luxo além do que já existe no
      card (o card já é limpo — não adicionar no nível do anúncio).
- [ ] Manter "18+" visível no card (já está, canto inferior conforme o HTML) — reforçar também no targeting
      (idade mínima 18 configurada no ad set, não só visual).
- [ ] Evitar no texto do anúncio: aposta/bet, "win money", "lucro garantido", "cash out", promessas de
      renda. "Poker"/"MTT"/"pool" seguem permitidos.
- [ ] Não usar comparação nominal com concorrente (regra de marca + reduz denúncia, `compliance-meta.md` §3).
- [ ] Link de destino: landing sem afiliação/link de sala de poker (já é a regra da landing, `compliance-meta.md`
      §2 — apenas reconfirmar que a versão no ar em 10/07 mantém isso).
- [ ] Rodar este checklist por anúncio antes de subir, mesmo pausado (facilita a revisão do Rafael).

Nenhuma reescrita do card em si é necessária — a mudança fica no texto de acompanhamento do anúncio (que
não existe no post orgânico) e na configuração de targeting (18+ explícito).

---

## 6. Checklist de compliance específico deste anúncio

- [ ] Objetivo configurado = Alcance/Engajamento (ou Tráfego sem otimizar para conversão) — nunca Conversões
- [ ] Idade mínima 18 configurada no ad set (targeting), além do selo visual no card
- [ ] Texto de acompanhamento revisado contra a lista de termos proibidos (§5 acima)
- [ ] Sem imagem/elemento de dinheiro/luxo além do card já aprovado
- [ ] Sem comparativo nominal com concorrente
- [ ] Link de destino = landing oficial, sem afiliação de sala de poker, com rodapé "ferramenta de estudo · 18+"
- [ ] Posicionamentos manuais = Feed IG + Stories/Reels IG apenas (Audience Network desmarcado)
- [ ] UTM completo e correto em toda URL de anúncio (§4)
- [ ] Público não usa o salvo #4 nem lookalike (D3/D1 de `publicos-diagnostico.md`)
- [ ] Objeto criado **PAUSADO** — nenhuma ativação sem o Rafael
- [ ] Pré-requisitos de gasto (§3 deste doc) reconfirmados no Gerenciador antes de qualquer ativação
- [ ] Se reprovado por "Online Gambling and Games": seguir o plano de contingência de `compliance-meta.md` §4
      (não republicar idêntico; pedir revisão manual com a justificativa padrão; registrar em
      `log-reprovacoes.md`)

---

## 7. Resumo da recomendação

**Opção 2 — boost de alcance/engajamento do reveal, sem otimizar por cadastro.** Sobe pausado, orçamento
R$20–35/dia por 3–5 dias (opções A/B acima), público de engajadores IG 365d (criar) + broad BR 18+ leve,
feed + stories/reels, UTM `launch20_reveal`. Métrica de sucesso é custo por engajador retido e crescimento
do público quente — não cadastro. Ativação e gasto ficam 100% com o Rafael, condicionados a reconfirmar os
pré-requisitos do §3 (pagamento, domínio, eventos da landing, campanhas antigas) no Gerenciador antes de
qualquer real sair.
