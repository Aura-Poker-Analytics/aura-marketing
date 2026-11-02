# Rotina semanal de ativação da Meta (prepara, não envia)

**Criada em 02/11/2026** · **Pedido:** ROTINA-ATIVACAO, resposta do Rafael "A" (via HUB) · **Tarefa agendada:** `ativacao-meta-semanal`, segunda 07:00 (horário local), no app, com o MCP `postgres-azure-business` só em SELECT e o do Resend só para conferir rascunhos.
**Meta que move:** Aura, cadastros novos ≥ 10 por semana viram pagantes (35 em 31/12).

## O que a rotina faz toda segunda

1. Lê o último `content/email/ativacao-meta/lote-*.csv` (só ids) e monta o lote novo: cadastros com `utm_source` em `meta` ou `instagram` que ainda não estão em nenhum lote, sem superusuário, sem `@aurapoker.com`, sem Stripe nem assinatura.
2. Define o idioma pelo país, no dia: PT só para BR e PT; EN para o resto; país vazio em PT (regra do Rafael de 02/11).
3. Define o passo de cada id: A1 para quem não recebeu nada; A2 para quem está há 3 dias do A1; A3 há 6 dias; sempre com no mínimo 3 dias desde o último envio (`_ops/email-calendario-2026-11.md`). A2 e A3 só valem para quem não fez análise: o GA4 não lista por pessoa, então a rotina marca "conferir no GA4 na véspera".
4. Grava `lote-<data>.csv` (id, cadastro, país, idioma, passo; nunca e-mail) e um cartão curto, e abre um PR de conteúdo.
5. Confere no Resend que os rascunhos de A1, A2 e A3 em PT e EN existem e continuam em rascunho. Não cria rascunho novo se já existe.
6. Manda o cartão à HUB: tamanho do lote por idioma e passo, assuntos, ids dos rascunhos e a pergunta "posso enviar?".

## O que ela não faz sozinha

Enviar (broadcast, batch ou e-mail avulso); criar contato ou segmento no Resend; criar cupom ou promotion code; escrever no AuraBusiness; pôr e-mail, nome ou nick em arquivo, git ou mensagem; ligar automação. Cada envio é um "sim" do Rafael digitado na sessão que envia (MKT-D4).

## Guardrails

- Lote com mais de 40 pessoas: para e avisa (anomalia).
- Quem está em público de maior prioridade (ex-pagante, assinatura parada no Woo, Grátis do R2) não entra: a rotina não tem e-mail, então o cruzamento é feito pela sessão que envia, no dia, com a lista de ids.
- Cada execução registra quantos ids leu e quantos entraram.
- O app precisa estar aberto às 07:00; se estiver fechado, a tarefa roda na próxima abertura.

## Onde está o texto da tarefa

`C:\Users\Rafael\.claude\scheduled-tasks\ativacao-meta-semanal\SKILL.md`. Mudar horário ou regra é pelo `update_scheduled_task`; a regra de idioma, o mínimo de 3 dias e o calendário valem sobre este arquivo quando mudarem.

## Fase 2 (depois da ficha de LGPD)

Container Apps Job no repo `growth-ops`, com o mesmo contrato. Só entra quando a HUB abrir a frente; o envio continua com o "sim" do Rafael.
