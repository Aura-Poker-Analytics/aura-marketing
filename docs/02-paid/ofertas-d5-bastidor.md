# Ofertas D5: notas de bastidor (não é texto ao público)

Peças: `content/emails/ofertas-d5/{volta-paradas,anual-fe}.md` e `en/`. Nada enviado nem publicado. Sem commit.

## Fontes dos números
- Exemplo BTN vs SB 25bb, flop A-high rainbow, c-bet 33%: field folda 41,5%, GTO 25,0% (9.937 mãos). Fonte: `docs/02-paid/sinal01-spots-fortes.md` linha 1 e `content/ads/sinal01/numeros/`. É o mesmo spot dos anúncios SINAL01, escolhido por continuar desvio forte nas faixas 5, 7/8 e 9.
- Preços (R$ 75, R$ 150, R$ 1.295, R$ 995, US$ 199, US$ 259, cerca de R$ 83 por mês) e prazos (30/11, 01/12): vêm do brief do pedido, sem `numeros-verificados.md` próprio. Conferir contra o Stripe antes de enviar. R$ 995 / 12 = R$ 82,92.

## Decidido pela HUB (29/10)
- Quem está nas assinaturas paradas recebe só a oferta A e sai da lista do anual (B).
- Saudação sem nome: "Olá," no PT e "Hi," no EN. Os assuntos que começam com {{primeiro_nome}} só vão para quem tem nome; sem nome, usar o assunto sem nome da mesma lista.
- EN da volta fica "half price": o cupom é 50% também em USD (US$ 14,50 no mensal).
- O código fica como placeholder até o cupom existir no Stripe (ficha MKT-D5-EXEC, com o Rafael).
- Assunto 2 do anual EN: "about US$ 17 a month" no lugar de "R$ 83", porque a lista EN paga em dólar.

## Dúvidas abertas
1. O código {{CODIGO_VOLTA}} vale só no 1º mês; no anual direto (R$ 1.295) a copy não promete desconto.
2. A frase "Modo GTO incluso no plano Individual por tempo limitado" está também no e-mail do anual. Fica como o Rafael decidiu (LANDING-GTO-TEMPO A); se ele quiser evitar a leitura de "garantido por 12 meses", troca por "Field Exploits no plano Individual".
3. Os links com `utm_source=landing` e `utm_source=instagram` (banner e story) seguem o pedido; confirmar que o GA4 aceita esses valores.

## Recomendações
- Volta: assunto 1 (pessoal) como principal; assunto 3 (oferta direta) como variante B.
- Anual: assunto 1 (preço e prazo claros).

## Lint
`casa-lint-ci.py` e `casa_lint.py vocab` NÃO foram executados: esta sessão não tinha shell. Conferência manual por busca nos padrões de `banned_terms.json` (Beta, plano GTO, pool, overlay, bastidor, pp/pts, "o Aura", ponto decimal no PT): 0 achados nos arquivos PT; no EN só o ponto decimal, que é correto em `en/`. Rodar o lint antes de commitar.
