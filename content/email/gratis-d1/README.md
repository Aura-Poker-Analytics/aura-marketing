# Grátis D1: e-mail do dia seguinte ao cadastro

A Q23 da Aura simples, aprovada pelo Rafael em 04/11/2026, pede um e-mail no dia seguinte ao cadastro. O objetivo é fazer quem criou uma conta Grátis voltar no 2º dia. Meta: Aura com 35 pagantes até 31/12.

**Nada sai daqui sem o sim do Rafael digitado na sessão que envia.** Também não se cria automação no Resend sem esse sim, porque automação é envio.

## Arquivos

- `publico.sql`: quem recebe hoje, lido no AuraBusiness.
- `spot-da-semana.sql`: o número do card grátis da semana, lido no analytics prod.
- `numeros-verificados.md`: a linha lida em cada semana.
- `../_template/build_gratis_d1.py`: gera `d1-pt.html` e `d1-en.html`. O script para com erro quando o `SPOT` está fora da semana dele.
- `../previews/gratis-d1-{pt,en}-{680,390}.png`: as prévias.

## Envio (manual, com o sim do Rafael)

1. Rode `spot-da-semana.sql`. Se a linha mudou desde a última semana:
   - atualize o `SPOT` e o `SPOT_SEMANA` no build;
   - acrescente a linha no `numeros-verificados.md`;
   - passe o e-mail pelo casa:revisor.
2. Rode `publico.sql`. Tire da lista:
   - os e-mails na supressão do Resend (`list-suppressions`);
   - os contatos com `unsubscribed=true` (`get-contact`; 404 quer dizer que não é contato e pode receber);
   - os Ids que já estão em `enviados-ids.txt`.
3. Gere o HTML e tire o comentário `<!-- RASCUNHO … -->` da linha 2. Ele é nota interna e não vai ao jogador.
4. Mande em batch transacional, um e-mail por conta:
   - remetente `Aura Poker Analytics <news@news.aurapoker.com>`, reply-to `manager@aurapoker.com`;
   - cabeçalho `List-Unsubscribe` com mailto e one-click, como no envio de 30/09;
   - PT para BR, PT, AO, MZ e país nulo; EN para os demais países.
5. Grave os Ids enviados em `enviados-ids.txt`. Só Ids, nunca e-mail.

## Medição

- Abertura e clique no Resend.
- 2º login em 48 h no AuraBusiness, comparado com a coorte da onda de 30/10 a 02/11, que não recebeu e-mail.
- GA4 com `utm_campaign=gratis_d1` (`utm_content` d1-pt ou d1-en).
- Primeira leitura depois de 30 envios ou 14 dias, o que vier antes.
