"""Lê o banned_terms.json copiado (casa/dados) para os QAs de render. Só stdlib.

achados(texto) -> lista de "R1 P1: trecho" para o texto visível de uma peça. Os QAs mantêm as listas
locais (BANNED) como extra do repo e somam estes achados como AVISO, sem derrubar o render.
"""
import re
import sys
from pathlib import Path

CASA = Path(__file__).resolve().parent
sys.path.insert(0, str(CASA))
import casa_lint  # noqa: E402

_REGRAS = casa_lint.compilar_regras(casa_lint.carregar(CASA / "dados", "banned_terms.json"), "copy")


def achados(texto: str, idioma: str = "pt") -> list[str]:
    out = []
    for r, rx in _REGRAS:
        langs = r.get("idiomas", ["*"])
        if "*" not in langs and idioma not in langs:
            continue
        for m in rx.finditer(texto):
            out.append(f"{r['rubrica']} {r['id']}: {m.group(0)!r}")
    return sorted(set(out))
