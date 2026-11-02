# Notas: R2 EN do Grátis que não assina (02/11/2026)

**Diagnóstico de uma linha:** quem lê é um Grátis de fora do BR e de Portugal que se cadastrou e não assinou; já viu a Aura, não sabe o que mudou em 60 dias; a única ação é abrir o app pelo código ou pelo botão.

**Peças:** `r2-en-cupom.html` (com o `VOLTE50`, 80% do lote) e `r2-en-controle.html` (sem código, 20%). Geradas por `content/email/_template/build_gratis_pais.py`. Plano e fichas: `docs/00-strategy/gratis-por-pais-plano.md`.

**Números usados e fonte**
- "8 novidades", "60 dias", "20bb", "13x13", "2 entram e 2 saem": lista `NOVIDADES_60D` de `content/email/_template/components.py` (conferida como "no ar" em 02/11 no PR #60), traduzida item a item. O gerador tem um `assert` que força a lista EN a ter os mesmos 8 itens.
- "50% nos 3 primeiros meses" e "$14.50 em vez de $29": 50% de US$ 29, preço mensal do Individual em dólar (`content/email/reconquista-2026-11/sequencia.md`); a regra de 50% por 3 meses é o VOLTE50 (`_ops/email-calendario-2026-11.md`). O `R6eSQeTK` vale em BRL (7500) e em USD (1450) pelo `currency_options`, lido no Stripe live com o campo expandido (correção da HUB de 02/11: a primeira versão achava que só valia em BRL).
- "Nov 30": validade do VOLTE50 no calendário.

**Prévia no navegador:** 680 px e 390 px conferidas. No 680 apareceu o selo "NOVO" em português dentro do e-mail em inglês; corrigido com o parâmetro `badge` em `novidades()` (PT segue `NOVO`, EN usa `NEW`; os HTMLs em português não mudaram).

**Lint:** `casa_lint.py vocab --contexto copy` nos dois HTMLs: 0 erro, 0 aviso. `casa-lint-ci.py --base origin/main`: 0 erro no diff.

**Revisão:** `casa:revisor` (subagente, só leitura). Resultado no fim deste arquivo.

**Fora desta peça:** o sim do Rafael para qualquer envio, e a janela de envio (15h de Brasília para EN, hipótese a medir). Não há `[SPOT]`: o R2 usa as novidades.

## Revisão do casa:revisor (02/11): CORRIGIR, ajustes aplicados
- ERRO 1 (`[CODE]` no preheader e na caixa): resolvido; o e-mail usa o `VOLTE50`, que já vale em dólar.
- ERRO 2 (não dizia onde digitar o código): a caixa agora termina com "Enter the code at checkout."
- Ajustes aplicados: abertura com o ganho ("8 new things in Aura since you signed up."), "$14.50 ... $29" sem espaço, "Same login, nothing to set up". O comentário de rascunho (linha 2) sai antes do envio.
- Aberto: conferir no Stripe se o cupom restringe por 1.ª compra (`first_time_transaction`) para o texto "first subscription only".
