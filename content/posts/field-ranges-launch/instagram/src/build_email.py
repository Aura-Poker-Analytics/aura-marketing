"""Imagens do e-mail do Field Ranges: grade do spot de all-in, 1200 px de largura (exibida a 552 px),
sem transparencia, fundo #0b1220, rotulos das celulas apagadas realcados.
Uso: python build_email.py"""
from pathlib import Path
import numpy as np
from PIL import Image
import build as B

OUT = B.POST / "email"
OUT.mkdir(exist_ok=True)
BG_APP, BG_MAIL = np.array([2, 6, 23]), np.array([11, 18, 32])  # #020617 -> #0b1220
tmp = B.ASSETS / "_email_tmp.png"

for lang in ("pt", "en"):
    src = Image.open(B.RAW / f"{lang}-01-grade-allin.png").convert("RGB")
    # so o cartao da grade (sem titulo do spot, conforme o veto do Rafael), sem navegacao, sem cabecalho do app, sem painel de percentuais
    x0, y0, x1, y1 = [round(v * B.S) for v in (194, 682, 983, 1515)]
    src.crop((x0, y0, x1, y1)).save(tmp)
    B.lift_dim_labels(tmp, origin=(194, 682))
    a = np.asarray(Image.open(tmp).convert("RGB")).astype(int)
    m = np.abs(a - BG_APP).sum(-1) <= 6
    a[m] = BG_MAIL
    im = Image.fromarray(a.astype("uint8"))
    w = 1200
    h = round(im.height * w / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    q = im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    dst = OUT / f"field-ranges-{lang}.png"
    q.save(dst, optimize=True)
    chk = Image.open(dst)
    print(dst.name, chk.size, chk.mode, round(dst.stat().st_size / 1024), "KB")
tmp.unlink()
