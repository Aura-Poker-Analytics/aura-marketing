# Escada de onboarding — copies finais (v1 pra revisão do PO)

**Criado:** 2026-08-28 · Template visual: o mesmo do Lote 1/reativação (barra dourada, logo, print, CTA dourado, unsubscribe Resend)
**Remetente:** Aura Poker Analytics `<news@news.aurapoker.com>` · Reply-To `manager@aurapoker.com`
**UTM padrão:** `utm_source=email&utm_medium=email&utm_campaign=onboarding&utm_content=d00|d07|d14|d21-<mes>`

## Spot oficial do D7 (escolhido pelo PO, 28/08)

> **Flop CBet IP · SRP · BB×EP** — Reg Aggro **85,2%** (n=2.399.253) · Reg Tight **77,6%** (n=804.261) · gap **7,6 pp** · visível na UI (tela CBet IP)

---

## D0 — Boas-vindas: aprenda a FATIAR o field (revisado 28/08 por pedido do PO)

**Assunto:** `Sua conta está pronta. Aprenda a fatiar o field.`
**Preheader:** `O mesmo spot muda de cara quando você troca a fatia — buy-in, estágio, classe, posição.`

Bem-vindo à Aura.

A plataforma não te mostra "o número do spot". Mostra o número **da fatia que você escolher** — e é na comparação entre fatias que mora a informação que ninguém mais tem.

Quatro cortes pra você pensar desde o primeiro login:

♠ **Por buy-in** — o field de ≤$22 não joga como o de $109. A frequência que você decorou pode ser de um torneio que você nem joga.

♠ **Por estágio** — early profundo e bolha são jogos diferentes: as mesmas ações, outras frequências.

♠ **Por classe de jogador** — Reg Aggro e Reg Tight não apertam os mesmos botões. O painel separa um do outro, spot a spot. *(Semana que vem te mando um exemplo com números que valem a pena.)*

♠ **Por posição** — RFI de CO e de BTN são parentes distantes. Compare lado a lado.

No **preview grátis** você navega o recorte inicial de cada módulo (≤$22 · Vanilla · Early) e os principais exploit cards do Hotspot. O jeito de pensar já vem completo: **nunca leia um número sem saber de qual fatia ele veio.**

**[Abrir a Aura →]** (app, utm d00)

Bom grind.

---

## D7 — O gap entre classes (o e-mail de valor)

**Assunto:** `85,2% vs 77,6% — o mesmo cbet, dois regs diferentes`
**Preheader:** `Flop CBet IP, pote single-raised, EP contra BB. 3,2 milhões de mãos separadas por classe.`

O spot: pote single-raised, EP abre, você paga do BB. O flop vem e ele, em posição, aperta o cbet.

A pergunta que quase ninguém consegue responder com dado: **quem está apertando?**

> **Reg Aggro:** cbeta **85,2%** das vezes *(2,4M mãos)*
> **Reg Tight:** cbeta **77,6%** *(804 mil mãos)*

7,6 pontos parecem pouco — até você traduzir em range: um cbeta **praticamente tudo que chega no flop**; o outro escolhe. O mesmo bet, no mesmo spot, carrega informação diferente dependendo de quem aperta.

**Você defende o big blind igual contra os dois?**

Na Aura, o painel de classes mostra isso spot a spot — com o tamanho de amostra na tela, pra você saber o quanto confiar em cada número.

**[Ver o painel de classes →]** (app, utm d07)

*Imagem do e-mail (aprovada pelo PO 28/08): mockup oficial da fábrica — `instagram/templates/shots/mockup-cbet-classes.png` (spot, perfis e amostras conferidos contra o dado validado).*
*URL pública p/ o HTML:* `https://raw.githubusercontent.com/Aura-Poker-Analytics/aura-marketing/feature/descoberta-reels-v2/instagram/templates/shots/mockup-cbet-classes.png`
*(Trocar para `aura.poker/email/cbet-classes.png` se o Betiato subir no host de e-mail — cosmético, não bloqueia.)*

---

## D14 — O que o upgrade destrava

**Assunto:** `O preview te mostrou a porta. Isso aqui é o resto da casa.`
**Preheader:** `Board completo, todos os buy-ins, todos os filtros.`

Na conta grátis você viu o preview de cada módulo: os principais exploit cards, o grid inicial de Preflop, uma amostra do Postflop.

O plano Individual abre o resto:

♠ **O board completo do Hotspot** — todos os exploit cards, não só o topo da lista
♠ **Todos os buy-ins e estágios** — do micro ao high, early ao FT, ICM
♠ **Todos os filtros** — classe de jogador, textura de board, sizing, tipo de torneio
♠ **Node-by-Node completo** — a árvore inteira, nó por nó

Mesmo jogo. Toda a informação.

**[Ver planos →]** (app/planos, utm d14)

---

## D21 — O cupom 75% off (SÓ pra quem não assinou; gate: deploy do checkout confirmado)

**Assunto:** `Primeira mensalidade por R$37 — até <último dia do mês>`
**Preheader:** `75% off no primeiro mês. Código <CODIGO-DO-MES> no checkout.`

Três semanas de Aura. Você já sabe o que tem aqui dentro.

Este mês, o primeiro mês do plano Individual sai por **R$37,50** (ou **US$7,25** no plano em dólar):

> ### Código: **<CODIGO-DO-MES>**
> **75% off na primeira mensalidade**
> Aplicar no checkout · válido até **<último dia do mês>**

Depois, preço normal — R$150/mês, cancela quando quiser. O código do mês que vem será outro.

**[Assinar por R$37,50 →]** (app/planos, utm d21)

*Regras do cupom (Stripe): amount_off FIXO R$112 / US$22 (≈75% da mensalidade) · duration once · max_redemptions 100 · expires fim do mês. NUNCA percent_off (75% do anual = R$971 de brecha).*

---

## Brief pra FÁBRICA — criativo frio "classes" (substituto do eixo vs-MDF)

**Nome/slug:** `disc03-classes-cbet` (PT) e `disc03-classes-cbet-en` (EN) — vira `utm_content`
**Formato:** reel 9:16, 15–20s, + capa estática dedicada. Estrutura:

1. **Frame 1 (0–2s), o gancho:** os dois números GIGANTES — `85,2% × 77,6%` — e a linha: **"O MESMO CBET. DOIS REGS DIFERENTES."**
2. **Frame 2:** o setup em uma frase: "Pote single-raised. EP cbeta IP contra o BB."
3. **Frame 3 (o coração):** painel REAL da UI — CBet IP com Reg Aggro e Reg Tight lado a lado, `n` visível (2,4M / 804k). Zoom lento, sem pressa (feedback do PO: transição lenta).
4. **Frame 4:** a pergunta: "Você defende igual contra os dois?"
5. **Frame 5 (fechamento):** "Field intelligence por classe de jogador · 500M+ mãos auditadas · grátis pra começar, sem cartão" + aurapoker.com + 18+.

**Guard-rails:** frequência é descritiva — 🚫 "leak", "erro", "vs GTO", MDF, promessa de lucro. Amostra SEMPRE visível junto do número. Jargão em inglês (cbet, IP, SRP, range). Tom reg-pra-reg.
**Specs:** playbook §3.8 (safe zones, legenda embutida, funciona sem som; considerar trilha discreta desta vez).

---

## Implementação técnica (decidida 29/08)

**HTMLs finais:** `content/email/onboarding-d00-fatiar.html` · `-d07-classes.html` · `-d14-upgrade.html` · `-d21-cupom.html` — aprovados pelo PO em 29/08.

**Mecanismo de envio: `send-batch-emails` + Topic**, NÃO broadcast/segmento. Motivo: o plano do Resend limita a 3 segmentos e os três estão ocupados pela campanha de reativação; reciclá-los exigiria remover ~194 contatos um a um ou deletar segmento (destrutivo, risco de perder registro de descadastro). Topic dá gestão de inscrição sem tocar em segmento.

- **Topic:** `Onboarding — dicas de estudo` · id `4bf404de-32ce-4064-aad6-cd6e693e155f` · default `opt_in`
- Enviar sempre com `topicId` (gestão de inscrição) e `tags` `{cohort: d00|d07|d14|d21}` pra leitura por degrau
- Descadastro visível no rodapé: `mailto:manager@aurapoker.com?subject=Descadastrar` (o `{{{RESEND_UNSUBSCRIBE_URL}}}` só funciona em broadcast)
- Lotes de até 100 e-mails por chamada; coortes atuais são de 10–20 pessoas

## ✅ LOTE INAUGURAL ENVIADO — 29/08

Base: 34 cadastros pós-relançamento (≥20/07), fornecida pelo PO. **26 e-mails enviados**, 8 excluídos.

| Degrau | Enviados | Quem |
|---|---|---|
| **D0** (≤3d) | 2 | j.r_scp, carritossur |
| **D7** (4–17d) | 8 | fjose1610, lucasrrigos, pedrosavassi11, tiagotigela, plininmaker1, josesergiosilva86, pokerfranco89, pedroalmm1 |
| **D14** (≥18d) | 16 | belicon.coach, lucasandim, rodrigo--sr, maekilee090, screenbeat, thiagobteles@outlook, tmt031414, jaymemendes, pedrohkaled, gracianogustavo26, mtavernari, mhcsandrs, mitpoker1, gasparini.luu, luiza.gasparini, hailonhkennerly |

**Exclusões (8) e motivo:**
- **Pagantes** (`active && !trial`): eliseucanuto, dalhe.gto, **gdr0896** ⚠️ e valdogamito (assinante que cancelou — alvo de win-back, não de onboarding)
- **🇬🇧🇩🇪 Cadastros internacionais da campanha EU** (copy está em PT): `jandug@hotmail.co.uk` (15/08), `chris_f_12@hotmail.co.uk` (18/08), `philipp.zeckai@googlemail.com` (18/08) — **PENDENTE: versão EN da escada.** São exatamente os leads que custaram ~R$40 cada; ficar sem nurture desperdiça a aquisição.
- **Descartável:** `sydney.moore63@mx-mailsrv.com` (domínio de e-mail temporário)

**⚠️ Achado: possível 6º assinante desconhecido.** `gdr0896@gmail.com` (cadastro 19/08) está com `active=true, trial=false` — conta paga ativa — mas **não existe na Stripe live** e não tinha `crypto_last_payment_ref` na consulta de 23/08. Ou é acesso concedido manualmente, ou um pagamento fora dos dois rails. Vale o PO conferir.

**Próximos degraus (relógio individual, envio semanal manual):** quem recebeu D0 hoje → D7 em ~05/09; quem recebeu D7 → D14 em ~05/09; quem recebeu D14 → **D21 em ~19/09, condicionado aos gates do cupom**.

**Histórico do bloqueio (resolvido):** o MCP `postgres-azure-business` está fora do ar e é a ÚNICA fonte da lista de cadastros pós-relançamento (Stripe só tem pagantes; Resend só tem a lista do trial antigo; GA4/Meta não têm PII). Tentado e falhou: consulta via `Azure_MCP_Server__postgres` com auth MicrosoftEntra (401 — usuário `manager@aurapoker.com` sem permissão no servidor `aura-production`/`Aura-resource-group`); a via `PostgreSQL` exigiria manipular a senha em texto claro. **Desbloqueio: reiniciar o servidor MCP do Postgres.**

**Query do lote inaugural (rodar assim que o banco voltar):**
```sql
SELECT LOWER(TRIM(email)) AS email, create_date::date AS dia,
       (CURRENT_DATE - create_date::date) AS idade, active, trial
FROM tbl_user
WHERE create_date >= '2026-07-20' AND email LIKE '%@%.%'
ORDER BY create_date DESC;
```
Regras de corte: excluir assinantes ativos (Stripe: therunner.poker@, eliseucanuto@, dalhe.gto@, gremistaak@, valdogamito@), internos (`rafreis%`, `tiago.betiato%`) e descartáveis. Degrau por idade: ≤3d → D0 · 4–17d → **D7** (mais forte, ninguém viu) · ≥18d → D14 · D21 só após o gate.

## Operação da escada

- **Lote inaugural (após aprovação do PO):** aplicar o degrau correto pra cada cadastro existente pela idade da conta (cadastros de jul/ago: começam no D14; novos: D0)
- Envio semanal manual via Resend (batch) até validar taxas → depois Resend Automations
- **Gates antes do primeiro D21:** deploy da aura-api confirmado (campo de cupom no checkout + metadata UTM) + criação do cupom do mês na Stripe
