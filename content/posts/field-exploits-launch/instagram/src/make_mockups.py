"""Field Hotspots: recortes dos prints da tela (mockups/raw -> mockups/).

Regra: nenhum numero estatistico da tela aparece nos recortes. As linhas com numero
("Field xx,x% · GTO xx,x% · xx,x% abaixo", "Fold do field ...", barras por size) sao cobertas com a cor de fundo
local ou ficam fora do enquadramento. Numeros de verdade entram nas artes pela build, via numbers.json.
Parametros do spot (25bb, SRP, UTG vs BB, textura) nao sao estatistica e ficam.

Uso: python make_mockups.py
"""
from pathlib import Path

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
POST = HERE.parents[1]
# prints originais (COM numeros) ficam no aura-novofront, fora deste repo
RAW = POST.parents[3] / "aura-novofront/_ops/validacao-prints/169"
OUT = POST / "mockups"

PAID = RAW / "paid-1280-3-field-hotspots.png"
FREE = RAW / "free-1280-3-field-hotspots.png"
PAID_M = RAW / "paid-390-3-field-hotspots.png"
FREE_M = RAW / "free-390-3-field-hotspots.png"


def cover(im, box, sample_xy):
    """Pinta box com a cor de fundo amostrada em sample_xy (pixel de fundo, fora do texto)."""
    col = im.getpixel(sample_xy)
    ImageDraw.Draw(im).rectangle(box, fill=col)


def mask_list_numbers(im, rows, x1=402, x0s=None):
    """Cobre a linha 'Field x% · GTO y% · z% abaixo' de cada linha da lista.
    x0 por linha: o rotulo Overfold e mais estreito que o Overdefend (o texto comeca mais a esquerda)."""
    for i, y in enumerate(rows):
        x0 = (x0s[i] if x0s else 124)
        cover(im, (x0, y - 14, x1, y + 14), (x1 + 3, y))


def mask_detail_numbers(im):
    """Linha 'Fold do field ... · GTO ... · ... abaixo · N mil maos' do painel de detalhe (1280)."""
    cover(im, (443, 359, 1100, 382), (1150, 370))


def main():
    paid = Image.open(PAID).convert("RGB")
    free = Image.open(FREE).convert("RGB")
    ROWS = [241 + 93 * i for i in range(7)]            # linha 3 de cada item da lista (a 7a fica fora do recorte)
    X0S = [124, 124, 124, 108, 108, 124, 108]         # linhas 4 e 5 sao Overfold (chip estreito)

    # ---- menu do topo (sem numero)
    paid.crop((0, 0, 1170, 57)).save(OUT / "nav-completo.png")      # sem sino e avatar da conta de teste
    paid.crop((490, 0, 945, 57)).save(OUT / "nav-neutro-idioma.png")      # Preflop · Postflop · Field Hotspots NEW · Trends

    # ---- cabecalho do detalhe: par, stack, 3 boards, textura, rotulo Overdefend (para antes da linha de numeros)
    paid.crop((424, 153, 1252, 362)).save(OUT / "spot-detalhe-cabecalho.png")
    # ---- caixa Como explorar (texto do produto, sem numero)
    paid.crop((445, 396, 1231, 468)).save(OUT / "como-explorar.png")

    # ---- lista de 8 spots (plano pago): cada linha sem os numeros
    lp = paid.copy()
    mask_list_numbers(lp, ROWS, x0s=X0S)
    lp.crop((28, 150, 410, 733)).save(OUT / "lista-paga-sem-numeros.png")

    # ---- lista do Gratis: 1 spot liberado + 2 linhas trancadas
    lf = free.copy()
    mask_list_numbers(lf, [241])
    lf.crop((28, 150, 410, 372)).save(OUT / "lista-gratis-sem-numeros.png")

    # ---- janela de capa: menu + lista + cabecalho do detalhe (numeros cobertos)
    hw = paid.copy()
    mask_list_numbers(hw, ROWS, x0s=X0S)
    mask_detail_numbers(hw)
    hw.crop((0, 0, 945, 358)).save(OUT / "janela-capa-sem-numeros.png")

    # ---- mobile 390
    pm = Image.open(PAID_M).convert("RGB")
    fm = Image.open(FREE_M).convert("RGB")
    for nm, im in (("pago", pm), ("gratis", fm)):
        m = im.copy()
        cover(m, (44, 520, 352, 562), (352, 535))      # 'Fold do field ... abaixo' + '· N mil maos'
        m.crop((28, 172, 362, 712)).save(OUT / f"mobile-{nm}-spot-sem-numeros.png")
        im.crop((0, 788, 390, 844)).save(OUT / f"mobile-{nm}-menu-hotspots-new.png")
    print("ok", len(list(OUT.glob("*.png"))), "recortes em", OUT)


if __name__ == "__main__":
    main()
