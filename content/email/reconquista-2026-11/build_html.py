"""Gera o HTML dos e-mails da reconquista 2026-11 no template de marca do Modo GTO.

Uso: python build_html.py  (escreve e1.html a e4.html nesta pasta)
O e-mail 2 só sai depois da conferência logada do Rafael (gate R4 em sequencia.md).
Envio em batch transacional do Resend: o descadastro vai no cabeçalho List-Unsubscribe
e no rodapé por resposta "sair" (batch não gera link de descadastro por contato).
"""
from pathlib import Path

HERE = Path(__file__).parent
URL = "https://www.aurapoker.com/?utm_source=email&utm_medium=email&utm_campaign=reconquista-2026-11&utm_content={c}"

PAGE = """<!DOCTYPE html>
<html lang="pt-BR" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="color-scheme" content="dark light">
  <meta name="supported-color-schemes" content="dark light">
  <meta name="x-apple-disable-message-reformatting">
  <title>{subject}</title>
</head>
<body style="margin:0; padding:0; width:100%; background-color:#070a12; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%;">
  <div style="display:none; max-height:0; overflow:hidden; mso-hide:all; font-size:1px; line-height:1px; color:#070a12; opacity:0;">{preview}</div>
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#070a12;">
    <tr>
      <td align="center" style="padding:24px 12px;">
        <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px; max-width:600px; background-color:#0b1220; border:1px solid #1e293b; border-radius:14px; overflow:hidden;">
          <tr><td bgcolor="#D4A418" style="height:3px; line-height:3px; font-size:0; background-color:#D4A418;">&nbsp;</td></tr>
          <tr>
            <td style="padding-top:26px; padding-right:34px; padding-bottom:6px; padding-left:34px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
                <td style="padding-right:10px; vertical-align:middle; width:50px;"><img src="https://www.aura.poker/email/aura-logo.png" width="40" height="32" border="0" alt="Aura" style="display:block; border:0; outline:none; text-decoration:none;"></td>
                <td style="vertical-align:middle;"><span style="font-family:Arial,Helvetica,sans-serif; font-weight:bold; font-size:20px; letter-spacing:6px; color:#e6ebf2;">AURA</span></td>
              </tr></table>
            </td>
          </tr>
          <tr>
            <td style="padding-top:14px; padding-right:34px; padding-bottom:0; padding-left:34px; font-family:Arial,Helvetica,sans-serif;">
              <h1 style="margin:0; font-size:28px; line-height:1.25; color:#e6ebf2; font-weight:bold;">{h1}</h1>
              <p style="margin:10px 0 0 0; font-size:17px; line-height:1.5; color:#D4A418; font-weight:bold;">{tagline}</p>
            </td>
          </tr>
          <tr>
            <td style="padding-top:16px; padding-right:34px; padding-bottom:4px; padding-left:34px; font-family:Arial,Helvetica,sans-serif; color:#c3ccd9; font-size:15px; line-height:1.65;">
{body}
            </td>
          </tr>
          <tr>
            <td style="padding-top:22px; padding-right:34px; padding-bottom:6px; padding-left:34px;" align="center">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>
                <td align="center" bgcolor="#D4A418" style="border-radius:10px; background-color:#D4A418;">
                  <a href="{url}" style="display:inline-block; padding-top:14px; padding-bottom:14px; padding-left:34px; padding-right:34px; font-family:Arial,Helvetica,sans-serif; font-size:16px; font-weight:bold; color:#0b1220; text-decoration:none; border-radius:10px;">{cta}</a>
                </td>
              </tr></table>
              <p style="margin:12px 0 0 0; font-family:Arial,Helvetica,sans-serif; font-size:13px; line-height:1.5; color:#9aa7ba;">{fine}</p>
            </td>
          </tr>
          <tr>
            <td style="padding-top:24px; padding-right:34px; padding-bottom:30px; padding-left:34px; border-top:1px solid #1e293b; background-color:#040711;">
              <p style="margin:0 0 6px 0; font-family:Arial,Helvetica,sans-serif; font-size:12px; line-height:1.6; color:#8a97ab;">Você recebeu este e-mail porque já foi assinante da Aura Poker Analytics.</p>
              <p style="margin:0 0 6px 0; font-family:Arial,Helvetica,sans-serif; font-size:12px; line-height:1.6; color:#8a97ab;">Não quer mais e-mails como este? Responda com "sair". Dúvidas no <a href="https://discord.gg/wYquSmUtAK" style="color:#aab6c8; text-decoration:underline;">Discord</a>.</p>
              <p style="margin:0 0 6px 0; font-family:Arial,Helvetica,sans-serif; font-size:12px; line-height:1.6; color:#8a97ab;">Fale com a gente: <a href="https://discord.gg/wYquSmUtAK" style="color:#aab6c8; text-decoration:underline;">Discord</a> · <a href="https://wa.me/554188083135" style="color:#aab6c8; text-decoration:underline;">WhatsApp</a> · <a href="https://www.youtube.com/@aurapokeranalytics" style="color:#aab6c8; text-decoration:underline;">YouTube</a></p>
              <p style="margin:12px 0 0 0; font-family:Arial,Helvetica,sans-serif; font-size:11px; letter-spacing:1px; color:#8a97ab;">AURA POKER ANALYTICS · © 2026 · 18+</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>
"""

P = '              <p style="margin:0 0 14px 0;">{}</p>'
LI = '              <p style="margin:0 0 10px 0; padding-left:14px; border-left:3px solid #D4A418;">{}</p>'
SIGN = '              <p style="margin:18px 0 4px 0;">Rafael<br><span style="color:#9aa7ba;">Fundador da Aura</span></p>'
FINE = "O código VOLTA vale até 16/11, uma vez, no primeiro mês do plano Individual. O Modo GTO está incluso no plano Individual por tempo limitado. Poker é jogo de habilidade e estudo. 18+."

EMAILS = {
    "e1": dict(
        subject="Desde que você saiu, a Aura ganhou o GTO",
        preview="O Field Exploits mostra spots em que o field se afasta forte do GTO. Para quem já assinou, 80% de desconto no primeiro mês até 16/11.",
        h1="A Aura ganhou o GTO",
        tagline="O field e o GTO lado a lado, spot a spot.",
        body=[
            P.format("Você já foi assinante da Aura. Escrevo porque o produto que você conheceu mudou bastante."),
            P.format("Hoje a Aura mostra o GTO ao lado do field:"),
            LI.format("<strong style=\"color:#e6ebf2;\">Modo GTO:</strong> o número e a faixa GTO ao lado do que o field faz, no flop, turn e river."),
            LI.format("<strong style=\"color:#e6ebf2;\">Field Ranges:</strong> o range que o field abre e defende, mão a mão, comparado ao GTO."),
            LI.format("<strong style=\"color:#e6ebf2;\">Field Exploits:</strong> 8 spots em que o field se afasta forte do GTO, em pares e stacks diferentes, cada um com o exploit pronto para usar. Toda segunda entram 2 novos."),
            P.format("Para quem já assinou, o primeiro mês do plano Individual mensal sai com <strong style=\"color:#e6ebf2;\">80% de desconto</strong>, de R$ 150 por R$ 30, com o código <strong style=\"color:#D4A418;\">VOLTA</strong> no checkout. Vale até 16/11."),
            SIGN,
        ],
        cta="Ver a nova Aura", content="e1",
    ),
    "e2": dict(
        subject="Um spot em que o field erra contra o GTO esta semana",
        preview="Um dos 8 spots do Field Exploits, com o número do field, o do GTO e o exploit.",
        h1="Um spot desta semana",
        tagline="O field folda 53,8%. O GTO folda 73,5%.",
        body=[
            P.format("Um dos 8 spots do Field Exploits desta semana:"),
            LI.format("<strong style=\"color:#e6ebf2;\">UTG contra BB, 25bb, pote simples (SRP), flop A-high two-tone, sem par, com OESD possível. O UTG dá c-bet de 50%.</strong>"),
            P.format("O field folda <strong style=\"color:#e6ebf2;\">53,8%</strong>. O GTO folda <strong style=\"color:#e6ebf2;\">73,5%</strong> (faixa 67,5–79,5%)."),
            P.format("<strong style=\"color:#D4A418;\">Como explorar:</strong> o BB defende demais contra c-bet. Blefe menos e aposte mais por value."),
            P.format("É um spot, não a média do field. Os outros 7 estão no app."),
            P.format("O código <strong style=\"color:#D4A418;\">VOLTA</strong> vale até 16/11: o primeiro mês do Individual mensal sai por R$ 30."),
            SIGN,
        ],
        cta="Ver os 8 spots", content="e2",
    ),
    "e3": dict(
        subject="2 spots novos hoje, e uma pergunta rápida",
        preview="O Field Exploits ganhou spots novos. E eu queria saber o que te fez sair.",
        h1="2 spots novos hoje",
        tagline="E uma pergunta rápida.",
        body=[
            P.format("Hoje entraram 2 spots novos no Field Exploits."),
            P.format("Também queria te perguntar uma coisa: o que te fez cancelar a Aura? Pode ser uma linha só, respondendo este e-mail. Eu leio todas, e isso decide o que a gente constrói a seguir."),
            P.format("Se quiser voltar, o código <strong style=\"color:#D4A418;\">VOLTA</strong> vale até domingo, 16/11."),
            SIGN,
        ],
        cta="Ver os spots novos", content="e3",
    ),
    "e4": dict(
        subject="O código VOLTA vence hoje",
        preview="80% de desconto no primeiro mês do Individual, até 23:59 de hoje.",
        h1="O código VOLTA vence hoje",
        tagline="Até 23:59, no horário de Brasília.",
        body=[
            P.format("Último lembrete: o código <strong style=\"color:#D4A418;\">VOLTA</strong> vence hoje às 23:59. Com ele, o primeiro mês do plano Individual mensal sai por R$ 30 em vez de R$ 150."),
            P.format("Desde 26/10, o Field Exploits recebeu 6 spots novos, cada um com o exploit."),
            P.format("Depois disto, não mando mais nada sobre essa oferta."),
            SIGN,
        ],
        cta="Voltar para a Aura", content="e4",
    ),
}

for name, e in EMAILS.items():
    html = PAGE.format(subject=e["subject"], preview=e["preview"], h1=e["h1"], tagline=e["tagline"],
                       body="\n".join(e["body"]), url=URL.format(c=e["content"]), cta=e["cta"], fine=FINE)
    (HERE / f"{name}.html").write_text(html, encoding="utf-8")
    print(name, len(html))
