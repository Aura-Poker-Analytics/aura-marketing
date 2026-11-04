"""Gera o e-mail P1 do ciclo de vida: pagante do plano Individual sem login há 14 dias (WF-A1-CICLO b, 04/11/2026).

Uso: python -I content/email/_template/build_pagante.py
Saída: content/email/pagante-p1-sem-login.html

Sem oferta (é pagante). O gancho é um spot que entrou no Field Exploits na segunda (releaseDate 2026-11-02),
lido logado com a conta dos agentes em 04/11 (tela /exploits, print em content/email/previews/p1-fonte-exploits-0411.png).
Cadência: no máximo 1 e-mail por pessoa por semana somando todos os fluxos; envio só com o sim do Rafael.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from components import *  # noqa: E402,F403

OUT = pathlib.Path(__file__).resolve().parent.parent

# regime e tipo (FE 1.2 via HUB, 04/11): GTO chipEV; field mistura Regular, KO e Mystery (ficha FE-REGIME)
# números: tela /exploits em 04/11, BTN vs BB river delayed c-bet SRP, 60bb (snapshot 20261102, referência 20261022)
p1 = email(
    title="Spot novo no seu Field Exploits: o BTN dá delayed c-bet de menos no river",
    preview="Field 27,7%, GTO 50,1%. Entrou na segunda e já está no seu Field Exploits.",
    headline="O BTN dá delayed c&#8209;bet de menos no river.",  # hífen que não quebra: "c-" sozinho no fim da linha
    sub="Esse spot entrou no seu Field Exploits na segunda:",
    blocks=[
        row(gto_card(
            spot="BTN vs BB, single raised pot, 60 big blinds",
            context="Flop 9-high ou menor, two-tone, sem par, com OESD possível, qualquer turn e river. GTO chipEV · field de todos os tipos de torneio (Regular, KO e Mystery).",
            field="27,7", gto="50,1", band="faixa GTO de 43,1% a 57,1%",
            verdict="<strong>Too passive:</strong> o field fica abaixo da faixa do GTO (27,7% contra 43,1% a 57,1%). Quando ele aposta, folde mais as mãos marginais.",
            label="Field Exploits · novo nesta semana",
        ), pad="0 40px 24px 40px"),
        row(para("Entram spots novos toda segunda. Hoje são 8 liberados no seu plano.", size=14, color=INK3, mb=8)),
    ],
    cta="Ver os spots da semana",
    cta_url=LANDING.format(c="pagante-inativo", k="p1-exploits"),
    note=para("Se algo travou, responda com uma linha.", size=15),
    unsub=BROADCAST_UNSUB,
    reason="Você recebeu este e-mail porque assina o plano Individual da Aura Poker Analytics.",
    draft_note="RASCUNHO P1 · pagante do Individual sem login há 14 dias · sem oferta · 1 e-mail por pessoa por semana somando os fluxos · não enviar sem o sim do Rafael · _ops/email-calendario-2026-11.md",
)

(OUT / "pagante-p1-sem-login.html").write_text(p1, encoding="utf-8")
print("pagante-p1-sem-login.html", len(p1))
