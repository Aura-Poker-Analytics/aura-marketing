#!/usr/bin/env python3
"""casa-lint no CI (M5): confere o hash da cópia da casa e roda o lint de vocabulário sobre o texto ao público.

Bloqueia só o erro em linha adicionada ou alterada pelo diff (base...HEAD). Erro em linha antiga é aviso
("item de limpeza"). Sem --base (push na main, rodada manual), nada bloqueia: tudo é aviso.
Só stdlib. Uso: python scripts/casa-lint-ci.py [--base <ref>] [--so-hash]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
CASA = RAIZ / "casa"
LINT = CASA / "casa_lint.py"
BANNED = CASA / "dados" / "banned_terms.json"
LOCK = CASA / "casa.lock.json"
ESCOPO = ["content"]  # texto ao público: posts, legendas, e-mails
EXT = {".md", ".txt", ".html", ".htm", ".json", ".yaml", ".yml", ".mdx"}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def git(*args: str) -> str:
    r = subprocess.run(["git", "-C", str(RAIZ), *args], capture_output=True, text=True, encoding="utf-8")
    if r.returncode:
        sys.exit(f"git {' '.join(args)}: {r.stderr.strip()}")
    return r.stdout


def conferir_hash() -> bool:
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    ok = True
    r = subprocess.run([sys.executable, "-X", "utf8", "-I", str(LINT), "hash", "--lock", str(LOCK), str(BANNED)],
                       capture_output=True, text=True, encoding="utf-8")
    print(r.stdout + r.stderr, end="")
    ok &= r.returncode == 0
    esperado = lock["casa_lint"]["casa_lint.py"]["sha256"]
    if sha(LINT) != esperado:
        print(f"HASH casa_lint.py {sha(LINT)[:12]} != casa.lock.json {esperado[:12]}")
        ok = False
    return ok


def linhas_novas(base: str) -> dict[str, set[int]]:
    """arquivo -> números das linhas adicionadas ou alteradas em HEAD (git diff -U0)."""
    out = git("diff", "-U0", "--no-color", f"{base}...HEAD", "--", *ESCOPO)
    novas: dict[str, set[int]] = {}
    arq = None
    for ln in out.splitlines():
        if ln.startswith("+++ "):
            arq = None if ln.endswith("/dev/null") else ln[6:]
        elif ln.startswith("@@") and arq:
            m = re.search(r"\+(\d+)(?:,(\d+))?", ln)
            ini, n = int(m.group(1)), int(m.group(2) or 1)
            novas.setdefault(arq, set()).update(range(ini, ini + n))
    return novas


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", help="ref base do PR (ex.: origin/main)")
    ap.add_argument("--so-hash", action="store_true")
    a = ap.parse_args()

    if not conferir_hash():
        print("::error::dado da casa não bate com o casa.lock.json (desatualizado ou adulterado)")
        return 1
    if a.so_hash:
        return 0

    arqs = sorted(str(p.relative_to(RAIZ)).replace("\\", "/") for d in ESCOPO for p in (RAIZ / d).rglob("*")
                  if p.is_file() and p.suffix.lower() in EXT)
    r = subprocess.run([sys.executable, "-X", "utf8", "-I", str(LINT), "--dados", str(CASA / "dados"), "--json",
                        "vocab", "--contexto", "copy", *arqs], capture_output=True, text=True, encoding="utf-8", cwd=RAIZ)
    if r.returncode not in (0, 1):
        print(r.stdout + r.stderr)
        return 2
    achados = json.loads(r.stdout or "[]")
    novas = linhas_novas(a.base) if a.base else {}
    bloqueia, aviso = [], []
    for x in achados:
        if x["nivel"] == "erro" and a.base and x["linha"] in novas.get(x["arquivo"].replace("\\", "/"), set()):
            bloqueia.append(x)
        else:
            aviso.append(x)
    for x in bloqueia:
        print(f"::error file={x['arquivo']},line={x['linha']}::{x['rubrica']} {x['regra']}: \"{x['trecho']}\" -> {x['sugestao']}")
    antigos = len(aviso)
    print(f"casa-lint: {len(bloqueia)} erro(s) no diff (bloqueiam), {antigos} achado(s) antigo(s) (aviso, item de limpeza)")
    if antigos:
        por = {}
        for x in aviso:
            por[x["arquivo"]] = por.get(x["arquivo"], 0) + 1
        for f, n in sorted(por.items(), key=lambda kv: -kv[1])[:10]:
            print(f"::warning file={f}::{n} achado(s) antigo(s) do casa-lint (limpeza)")
    return 1 if bloqueia else 0


if __name__ == "__main__":
    sys.exit(main())
