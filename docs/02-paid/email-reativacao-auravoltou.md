# E-mail de reativação — conta grátis, sem cartão

**Criado:** 2026-08-12 · **Revisado:** 2026-08-13 — cupom REMOVIDO por decisão do PO; ênfase em conta grátis sem cartão
**Público:** 194 leads do trial antigo (tbl_user ago/25–jun/26, lista limpa, excluídos os 5 que já receberam o e-mail de lançamento em 30/07)
**Canal:** Resend, envio em lotes via batch (mesmo mecanismo do Lote 1)

> Histórico: a v1 deste doc oferecia o cupom AURAVOLTOU (1 mês grátis). O cupom foi **deletado da Stripe em 13/08** (0 resgates) — não mencionar em nenhuma comunicação. O PR [aura-api#18](https://github.com/Aura-Poker-Analytics/aura-api/pull/18) (campo de cupom no checkout) deixou de ser bloqueio deste e-mail, mas segue útil pra campanhas futuras.

## ✅ ENVIADO/AGENDADO em 14/08 (aprovação do PO na mesma data)

| Lote | Qtde | Broadcast | Status |
|---|---|---|---|
| 2 (recentes) | 50 | `497de556-4eeb-45e3-8979-7efb91c063ee` | **enviado 14/08 ~00h40 BRT** |
| 3 | 80 | `012b226c-7136-4c01-bf4a-76e9ca1a6f59` | agendado **16/08 10h BRT** |
| 4 | 64 | `4bb0f119-4261-48ad-846e-6608d82568a4` | agendado **18/08 10h BRT** |

Vigilância: checar bounce/spam do Lote 2 em 15/08; se anormal, **cancelar os agendados** (`cancel-broadcast`). Nota de infra: plano do Resend limita a 3 segmentos — Lotes 3/4 reutilizam os segmentos "Nova Aura NbN — Lote 1" (esvaziado dos 9 quentes antes) e "General" (estava vazio). Os nomes dos segmentos não batem com o conteúdo atual; fica o aviso pra quem olhar o painel.

## Arte

**HTML pronto:** [`content/email/reativacao-conta-gratis.html`](../../content/email/reativacao-conta-gratis.html) — adaptação do template de marca do Lote 1 (barra dourada, logo `aura.poker/email/aura-logo.png`, print do Node-by-Node hospedado, botão dourado, rodapé Discord/WhatsApp/YouTube, unsubscribe nativo do Resend via `{{{RESEND_UNSUBSCRIBE_URL}}}`).

## Copy (PT-BR)

**Remetente:** Aura Poker Analytics `<news@news.aurapoker.com>` · **Reply-To:** `manager@aurapoker.com` (idêntico ao Lote 1)
**Assunto:** `Reconstruímos a Aura. Seu login continua o mesmo.` (escolha final do PO, 14/08)
**Preheader:** `Hotspot, Postflop e Node-by-Node reconstruídos. Preview grátis de tudo, sem cartão.`
> Assunto v1 rejeitado pelo PO ("A Aura que você testou não existe mais" — podia soar como encerramento do app). O H1 interno mantém a frase, onde o contexto desfaz a ambiguidade.
**CTA principal:** `Ver a nova Aura` → `https://www.aura.poker/login?utm_source=email&utm_medium=email&utm_campaign=reativacao-2026-08&utm_content=conta-gratis`

---

Você criou uma conta na Aura quando ela ainda era outra coisa.

De lá pra cá, a gente reconstruiu a plataforma inteira:

**🎯 Hotspot** — os spots onde o field mais erra, ranqueados por desvio, com selo de confiança por amostra.

**📊 Preflop & Postflop** — RFI, 3bet, defesa por street: o que a população realmente faz, por posição, stack e estágio.

**🌳 Node-by-Node** — navegue a árvore de decisão inteira, nó por nó, com tamanho de amostra em cada um.

Tudo medido em **500M+ mãos auditadas de 7 salas**. Não é solver, não é tracker — é o que o field inteiro faz.

**Sua conta continua valendo — mesmo login de antes.** E o plano grátis dá acesso de verdade: **preview de todos os módulos, sem cadastrar cartão, sem pegadinha.** Entra, olha, e decide se faz sentido pro teu jogo.

**[Ver a nova Aura →]** `https://www.aura.poker/?utm_source=email&utm_medium=email&utm_campaign=reativacao-2026-08&utm_content=conta-gratis`

Bom grind,
Equipe Aura

*Você recebeu este e-mail porque criou uma conta na Aura. Se não quiser mais receber novidades, responda com "sair".*

---

## Medição

- **Aberturas/cliques:** Resend (tracking ligado 12/08; Lote 1 não tem esse dado)
- **Sessões:** GA4 `utm_campaign=reativacao-2026-08`
- **Reativação real:** logins dos e-mails da lista (conferir `tbl_user`/telemetria pós-envio)
- ⚠️ UTM em `tbl_user` não registra (first-touch de cadastro; usuários já existem)

## Notas

- Excluídos do envio (Lote 1, 30/07): lucasmineiro7@, mateusbocchixxe@gmail, gansildo@, galatur.ph@, gremistaak@
- Excluídos da lista-mãe: 12 descartáveis/fakes, contas internas (PO/Betiato), duplicatas → 199 limpos p/ Meta, 194 p/ e-mail
- Claim "preview de todos os módulos" segue o gabarito: grátis = preview, NUNCA "Hotspot completo grátis"
- Mesma lista de 199 subida na Meta como `Aura | Trial Antigo (lista de clientes)` (id `120249091809570327`) em 13/08
