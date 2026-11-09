"""Gera o e-mail do form com 30 dias (AURA-036), PT e EN, no template v2.

Uso: python -I content/email/_template/build_form_30dias.py
Saída: content/email/form-30dias/form-{pt,en}.html. Texto de origem: content/email/form-30dias/email.md.
Plano: docs/00-strategy/form-30-dias-aura036.md. O botão leva ao form ([LINK DO FORM] até o link existir). Nada é enviado por este script.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from components import *  # noqa: E402,F403

OUT = pathlib.Path(__file__).resolve().parent.parent / "form-30dias"
# trocar pelo link real e manter o UTM: ?utm_campaign=form-30dias&utm_content=pt (en no EN)
FORM = {"pt": "[LINK DO FORM]", "en": "[LINK DO FORM]"}
SEND = "RASCUNHO · não enviar sem o sim do Rafael digitado na sessão · envio por batch, PT para BR e PT e EN para o resto"
REASON = {
    "pt": "Você recebeu este e-mail porque tem uma conta Grátis na Aura Poker Analytics.",
    "en": "You're receiving this because you have a Free account on Aura Poker Analytics.",
}
UNSUB = {"pt": BATCH_UNSUB, "en": BATCH_UNSUB.replace("Descadastrar", "Unsubscribe")}

emails = {
    "form-pt": email(
        title="30 dias de Aura, sem cartão",
        preview="Dois minutos de resposta, 30 dias do plano Individual.",
        headline="30 dias de Aura, sem cartão.",
        sub="Você se cadastrou no Grátis da Aura e não assinou. Quero saber o que travou.",
        blocks=[
            row(para("Responda um form de 2 minutos, com 3 a 4 perguntas abertas: o que esperava da Aura, o que achou difícil ou confuso, o que faltou para assinar. As respostas decidem o que eu construo a seguir."), pad="0 40px 0 40px"),
            row(para("Depois que você responder, eu libero <strong>30 dias do plano Individual</strong>, com Modo GTO e Field Exploits. Sem cartão. Ao fim, a conta volta ao Grátis e nada é cobrado. Vale para resposta de verdade: pelo menos 150 caracteres somados, umas 3 linhas."), pad="0 40px 8px 40px"),
        ],
        cta="Responder o form (30 dias do Individual)",
        cta_url=FORM["pt"],
        note=para("Dúvida? Responda este e-mail.", size=15),
        unsub=UNSUB["pt"], reason=REASON["pt"],
        draft_note=f"form 30 dias PT · 26 do país BR e PT · {SEND}",
    ),
    "form-en": email(
        lang="en",
        title="30 days of Aura, no card needed",
        preview="A 2-minute form for 30 days of the Individual plan.",
        headline="30 days of Aura, no card needed.",
        sub="You signed up for Aura Free and didn't subscribe. I want to know what got in the way.",
        blocks=[
            row(para("Fill in a 2-minute form with 3 to 4 open questions: what you expected from Aura, what felt hard or confusing, what was missing to subscribe. Your answers decide what I build next. Use your Aura account email."), pad="0 40px 0 40px"),
            row(para("Once you answer, I unlock <strong>30 days of the Individual plan</strong>, including GTO Mode and Field Exploits. No credit card. After that your account goes back to Free and you're not charged. It applies to real answers: at least 150 characters in total, about 3 lines."), pad="0 40px 8px 40px"),
        ],
        cta="Answer the form (30 days of Individual)",
        cta_url=FORM["en"],
        note=para("Questions? Just reply to this email.", size=15),
        unsub=UNSUB["en"], reason=REASON["en"],
        draft_note=f"form 30 dias EN · 6 de fora de BR e PT · {SEND}",
    ),
}
for name, html in emails.items():
    (OUT / f"{name}.html").write_text(html, encoding="utf-8")
    print("ok", name, len(html))
