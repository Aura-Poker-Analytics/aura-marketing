"""Gera o e-mail do form com 30 dias (AURA-036), PT e EN, no template v2.

Uso: python -I content/email/_template/build_form_30dias.py
Saída: content/email/form-30dias/resp-{pt,en}.html (versão resposta por e-mail; a versão com form foi descartada em 09/11). Texto de origem: content/email/form-30dias/email.md.
Plano: docs/00-strategy/form-30-dias-aura036.md. O botão leva ao form ([LINK DO FORM] até o link existir). Nada é enviado por este script.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from components import *  # noqa: E402,F403

OUT = pathlib.Path(__file__).resolve().parent.parent / "form-30dias"
SEND = "RASCUNHO · não enviar sem o sim do Rafael digitado na sessão · envio por batch, PT para BR e PT e EN para o resto"
REASON = {
    "pt": "Você recebeu este e-mail porque tem uma conta Grátis na Aura Poker Analytics.",
    "en": "You're receiving this because you have a Free account on Aura Poker Analytics.",
}
UNSUB = {"pt": BATCH_UNSUB, "en": BATCH_UNSUB.replace("Descadastrar", "Unsubscribe")}

emails = {}

# ---- Versão B: responder este e-mail (sem form). O botão abre a resposta; as perguntas vão no corpo.
# Reply-to do batch: manager@aurapoker.com (o Resend não recebe neste domínio: Receiving disabled, 0 inboxes; 09/11).
REPLY = "mailto:manager@aurapoker.com?subject={s}&body=1.%0A%0A2.%0A%0A3.%0A%0A4."
emails["resp-pt"] = email(
    title="Seu feedback vale 30 dias de Aura completa, sem cartão",
    preview="Responda este e-mail em 2 minutos e eu libero 30 dias do plano Individual.",
    headline="Seu feedback vale 30 dias de Aura completa, sem cartão.",
    sub="Você se cadastrou no Grátis da Aura e não assinou. Quero saber o que travou.",
    blocks=[
        row(para("Responda este e-mail com a sua resposta a cada pergunta abaixo. Leva 2 minutos, e elas decidem o que eu construo a seguir."), pad="0 40px 0 40px"),
        row(panel(steps([
            ("O que você esperava da Aura?", "Quando se cadastrou."),
            ("O que achou difícil ou confuso?", "No uso."),
            ("O que faltou para você assinar?", "O que te fez parar."),
            ("O que você mudaria?", "Opcional."),
        ])), pad="0 40px 24px 40px"),
        row(para("Se você responder com pelo menos 150 caracteres somados (umas 3 linhas), eu libero <strong>30 dias do plano Individual</strong>, com Modo GTO e Field Exploits. Sem cartão. Ao fim, a conta volta ao Grátis e nada é cobrado. Use o mesmo e-mail da sua conta Aura."), pad="0 40px 8px 40px"),
    ],
    cta="Responder este e-mail",
    cta_url=REPLY.format(s="Minhas%20respostas%20(30%20dias%20de%20Aura)"),
    note=para("Dúvida? É só responder.", size=15),
    unsub=UNSUB["pt"], reason=REASON["pt"],
    draft_note=f"form 30 dias, versão resposta por e-mail, PT · 26 do país BR e PT · {SEND}",
)
emails["resp-en"] = email(
    lang="en",
    title="Your feedback is worth 30 days of full Aura, no card needed",
    preview="Reply in 2 minutes and I'll unlock 30 days of the Individual plan.",
    headline="Your feedback is worth 30 days of full Aura, no card needed.",
    sub="You signed up for Aura Free and didn't subscribe. I want to know what got in the way.",
    blocks=[
        row(para("Reply to this email with your answers to the questions below. It takes 2 minutes, and your answers decide what I build next."), pad="0 40px 0 40px"),
        row(panel(steps([
            ("What did you expect from Aura?", "When you signed up."),
            ("What felt hard or confusing?", "In use."),
            ("What was missing for you to subscribe?", "What made you stop."),
            ("What would you change?", "Optional."),
        ])), pad="0 40px 24px 40px"),
        row(para("If you reply with at least 150 characters in total (about 3 lines), I unlock <strong>30 days of the Individual plan</strong>, including GTO Mode and Field Exploits. No credit card. After that your account goes back to Free and you're not charged. Use the same email as your Aura account."), pad="0 40px 8px 40px"),
    ],
    cta="Reply to this email",
    cta_url=REPLY.format(s="My%20answers%20(30%20days%20of%20Aura)"),
    note=para("Questions? Just reply.", size=15),
    unsub=UNSUB["en"], reason=REASON["en"],
    draft_note=f"form 30 dias, versão resposta por e-mail, EN · 6 de fora de BR e PT · {SEND}",
)

for name, html in emails.items():
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
    print("ok", name, len(html))
