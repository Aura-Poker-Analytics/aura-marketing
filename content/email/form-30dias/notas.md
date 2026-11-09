# AURA-036: notas

**Diagnóstico:** grinder de MTT que se cadastrou no Grátis pelo anúncio SINAL01 há 1 a 11 dias e não assinou; sabe o que é a Aura e não viu motivo para pagar; a única ação é preencher o form de 2 minutos, em troca de 30 dias do Individual sem cartão.

**Números usados (fonte: brief do pedido AURA-036):**
- 2 minutos; 3 a 4 perguntas abertas; 30 dias; 150 caracteres somados; "umas 3 linhas".
- Audiência (só para envio, não vai no texto): 32 pessoas, 26 em português (país BR) e 6 EN (VE, GB, AT, DE).

**casa-lint vocab --contexto copy:** 0 erros, 0 avisos.
Não rodei `numeros`: não há numeros-verificados.md para esta peça e todos os números vêm do brief.

**Contagem:** corpo PT e EN em torno de 100 palavras com a saudação e a assinatura (uns 90 sem elas).

**Ficou de fora:** preço, cupom, urgência, prazo de liberação além de "depois que você responder, eu libero", "grátis para sempre", nome do anúncio. Sem UTM, porque o CTA vai para o form e não para a landing; a regra da casa é a landing (www.aurapoker.com), então o Rafael confirma essa exceção. Descadastro vai no rodapé do template do Resend.

**Ficha ao Rafael (recomendação):**
1. Envio aos 32 depende do seu "sim" digitado na sessão executora.
2. Dividir o envio por país: PT para os 26 do BR, EN para os 6 de fora.
3. Quem libera os 30 dias e como se confere o mínimo de 150 caracteres é decisão sua.
4. Trocar [LINK DO FORM] pelo link real antes de qualquer envio.


## Revisão do casa:revisor (09/11): OK, sem erro
Ajustes aplicados: 'umas 3 linhas'; saudação fora do fonte; a condição dos 150 caracteres sobe para o parágrafo da oferta; o e-mail pede o e-mail da conta Aura; botão 'Responder o form (30 dias do Individual)'; frase de dúvida no fonte. UTM do form: `utm_campaign=form-30dias&utm_content=pt|en` (a primeira nota dizia 'sem UTM', corrigido). Aberto: trocar `[LINK DO FORM]` (bloqueia o envio) e a exceção do CTA, com a HUB.


## 09/11: versão final
Versão com form descartada (escolha do Rafael: responder o e-mail). Assunto e primeira linha nas palavras dele: PT 'Seu feedback vale 30 dias de Aura completa, sem cartão' (54 caracteres, acima dos 50 da regra do assunto; é a frase dele) e EN 'Your feedback is worth 30 days of full Aura, no card needed' (59). Reply-to: manager@aurapoker.com. O Resend não recebe neste domínio (Receiving disabled, 0 inboxes).

## Revisor, delta de 09/11: 1 ERRO aberto, decisão do Rafael
"Aura completa" (palavras dele) não é termo da casa e pode prometer mais que o plano Individual entrega; o corpo diz "plano Individual, com Modo GTO e Field Exploits". Alternativa que o revisor propõe, só a palavra muda: PT "Seu feedback vale 30 dias do plano Individual, sem cartão" e EN "Your feedback is worth 30 days of the Individual plan, no card needed". O PR mantém a frase do Rafael; **só ele troca ou mantém**. Ajustes informativos: assunto acima de 50 caracteres (PT 54, EN 59), e os 30 dias aparecem em assunto, headline e pré-cabeçalho.
