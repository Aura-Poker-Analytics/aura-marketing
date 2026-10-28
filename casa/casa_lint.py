#!/usr/bin/env python3
"""casa-lint: gates de texto da casa (plano do time de agentes §2.3, rubrica R1 a R7).

Subcomandos:
  vocab     termos proibidos do dado semanal (R1, R2, R4, R6) e formato de número PT (R6)
  numeros   todo número existe no numeros-verificados (R7) com o mesmo arredondamento (R3)
  exemplos  mão de exemplo única por seção e que mostra o desvio (R5)
  hash      a cópia do dado bate com o .sha256 e com o casa.lock.json
  agentes   todo agente da casa pré-carrega a casa-conhecimento primeiro e traz a frase de reserva

Saída: uma linha por achado, "<arquivo>:<linha>: <rubrica> <regra> <nivel>: <trecho> -> <sugestão>".
Código de saída: 0 sem erro, 1 com erro, 2 uso errado ou dado ausente. Aviso não muda o código.
Só stdlib: roda no validador, no CI dos repos e no hook sem instalar nada.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass, asdict
from decimal import Decimal, InvalidOperation
from pathlib import Path

TEXT_EXT = {".md", ".txt", ".html", ".htm", ".json", ".yaml", ".yml", ".tsx", ".ts", ".jsx", ".js", ".mdx", ".csv"}


@dataclass
class Achado:
    arquivo: str
    linha: int
    rubrica: str
    regra: str
    nivel: str
    trecho: str
    sugestao: str = ""

    def __str__(self) -> str:
        s = f"{self.arquivo}:{self.linha}: {self.rubrica} {self.regra} {self.nivel}: \"{self.trecho}\""
        return s + (f" -> {self.sugestao}" if self.sugestao else "")


# ---------- dados ----------

def achar_dados(arg: str | None) -> Path:
    """--dados, depois CASA_DADOS, depois o repo (plugins/casa/bin -> dados), depois ao lado do executável."""
    here = Path(__file__).resolve().parent
    for c in (arg, os.environ.get("CASA_DADOS"), here.parents[2] / "dados" if len(here.parents) > 2 else None, here / "dados"):
        if c and (Path(c) / "banned_terms.json").is_file():
            return Path(c)
    sys.exit("casa-lint: dado não achado (use --dados ou CASA_DADOS com banned_terms.json)")


def carregar(dados: Path, nome: str) -> dict:
    return json.loads((dados / nome).read_text(encoding="utf-8"))


# ---------- leitura de texto ----------

def idioma_de(path: str, forcado: str) -> str:
    if forcado != "auto":
        return forcado
    p = path.replace("\\", "/").lower()
    if re.search(r"(^|/)en(/|$)|[._-]en\.(?:json|md|ts|tsx)$|/en-us/", p):
        return "en"
    return "pt"


def blocos(path: str, texto: str):
    """(linha, texto) a lintar. JSON: só os valores string, com a linha onde aparecem."""
    if path.endswith(".json"):
        try:
            dado = json.loads(texto)
        except json.JSONDecodeError:
            dado = None
        if dado is not None:
            linhas = texto.splitlines()
            for s in _strings(dado):
                yield _linha_de(linhas, s), s
            return
    for i, ln in enumerate(texto.splitlines(), 1):
        yield i, ln


def _strings(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from _strings(v)
    elif isinstance(x, list):
        for v in x:
            yield from _strings(v)


def _linha_de(linhas: list[str], s: str) -> int:
    alvo = json.dumps(s, ensure_ascii=False)[1:-1][:40]
    for i, ln in enumerate(linhas, 1):
        if alvo and alvo in ln:
            return i
    return 0


def arquivos(paths: list[str]):
    for p in paths:
        if p == "-":
            yield "<stdin>", sys.stdin.read()
            continue
        pp = Path(p)
        if pp.is_dir():
            for f in sorted(pp.rglob("*")):
                if f.is_file() and f.suffix.lower() in TEXT_EXT and "node_modules" not in f.parts:
                    yield str(f), f.read_text(encoding="utf-8", errors="replace")
        elif pp.is_file():
            yield str(pp), pp.read_text(encoding="utf-8", errors="replace")
        else:
            sys.exit(f"casa-lint: não achei {p}")


# ---------- vocab ----------

def compilar_regras(banned: dict, contexto: str):
    regras = []
    for r in banned["regras"]:
        ctx = r.get("contextos", ["*"])
        if "*" not in ctx and contexto not in ctx:
            continue
        flags = 0 if r.get("maiusculas") else re.IGNORECASE
        for p in r.get("padroes", []):
            regras.append((r, re.compile(p, flags)))
    return regras


DEC_PONTO_PT = re.compile(r"(?<![\w.,§])\d+\.\d{1,2}(?=\s*(?:%|bb\b))")
MILHAR_SEM_PONTO = re.compile(r"(?<![\w.,/#-])\d{5,}(?![\w.,])|(?<=n = )\d{4}(?![\d.,])")


def lint_vocab(paths, dados, contexto, idioma):
    regras = compilar_regras(carregar(dados, "banned_terms.json"), contexto)
    achados = []
    for path, texto in arquivos(paths):
        lang = idioma_de(path, idioma)
        for linha, s in blocos(path, texto):
            for r, rx in regras:
                langs = r.get("idiomas", ["*"])
                if "*" not in langs and lang not in langs:
                    continue
                if any(re.search(e, path.replace("\\", "/")) for e in r.get("excecoes_caminho", [])):
                    continue
                for m in rx.finditer(s):
                    achados.append(Achado(path, linha, r["rubrica"], r["id"], r.get("nivel", "erro"), m.group(0), r.get("sugestao", "")))
            if lang == "pt":
                for m in DEC_PONTO_PT.finditer(s):
                    achados.append(Achado(path, linha, "R6", "NUM-DEC", "erro", m.group(0), "vírgula decimal no PT (contract/vocab-v1 number_format): 73,8%"))
                for m in MILHAR_SEM_PONTO.finditer(s):
                    achados.append(Achado(path, linha, "R6", "NUM-MIL", "erro", m.group(0), "ponto no milhar no PT: 1.098"))
    return achados


# ---------- números ----------

UNIDADE = {
    "%": "%", "bb": "bb",
    "mi": "M", "mi+": "M", "milhão": "M", "milhões": "M", "M": "M", "million": "M", "millions": "M",
    "bilhão": "B", "bilhões": "B", "billion": "B", "billions": "B", "bi": "B",
    "mil": "K", "k": "K", "K": "K",
}
NUM = re.compile(
    r"(?<![\w.,])(\d[\d.,]*\d|\d)(\+?)\s*(%|bb\b|mi\+?(?![\w])|milh(?:ão|ões)\b|bilh(?:ão|ões)\b|bi\b|mil\b|million(?:s)?\b|billion(?:s)?\b|[kKM](?![\w]))?"
)


@dataclass
class Numero:
    valor: Decimal
    casas: int
    unidade: str
    escrita: str


def parse_num(tok: str, lang: str) -> tuple[Decimal, int] | None:
    t = tok
    if lang == "pt":
        if re.fullmatch(r"\d{1,3}(?:\.\d{3})+(?:,\d+)?", t) or re.fullmatch(r"\d+(?:,\d+)?", t):
            t = t.replace(".", "").replace(",", ".")
        elif re.fullmatch(r"\d+\.\d{1,2}", t):  # ponto decimal no PT: o R6 acusa; aqui vale o valor
            pass
        else:
            return None
    else:
        if re.fullmatch(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?", t) or re.fullmatch(r"\d+(?:\.\d+)?", t):
            t = t.replace(",", "")
        elif re.fullmatch(r"\d+,\d{1,2}", t):
            t = t.replace(",", ".")
        else:
            return None
    try:
        v = Decimal(t)
    except InvalidOperation:
        return None
    casas = -v.as_tuple().exponent if v.as_tuple().exponent < 0 else 0
    return v, casas


def numeros_no_texto(s: str, lang: str, ev: dict):
    ign_antes = re.compile(ev["numeros"]["ignorar_antes"], re.IGNORECASE)
    ign_num = [re.compile(p) for p in ev["numeros"]["ignorar_numero"]]
    for m in NUM.finditer(s):
        tok, unid = m.group(1), (m.group(3) or "")
        p = parse_num(tok, lang)
        if not p:
            continue
        if any(rx.fullmatch(tok) for rx in ign_num):
            continue
        if unid in ("%",) and ign_antes.search(s[: m.start()][-30:]):
            continue
        u = UNIDADE.get(unid, unid)
        if not u and len(re.sub(r"\D", "", tok)) < 4:
            continue  # número pequeno sem unidade (frase, ordinal) não é evidência
        yield Numero(p[0], p[1], u, m.group(0).strip()), m


def carregar_verificados(path: str) -> list[Numero]:
    txt = Path(path).read_text(encoding="utf-8")
    out: list[Numero] = []
    if path.endswith(".json"):
        d = json.loads(txt)
        itens = d.get("numeros", d) if isinstance(d, dict) else d
        for it in itens:
            lang = it.get("idioma", "pt")
            p = parse_num(str(it["valor"]), lang)
            if p:
                out.append(Numero(p[0], p[1], UNIDADE.get(it.get("unidade", ""), it.get("unidade", "")), str(it["valor"])))
        return out
    # markdown: coluna "Valor" de toda tabela
    col = None
    for ln in txt.splitlines():
        if not ln.strip().startswith("|"):
            col = None
            continue
        cels = [c.strip() for c in ln.strip().strip("|").split("|")]
        if col is None:
            idx = [i for i, c in enumerate(cels) if re.fullmatch(r"\**valor\**", c, re.IGNORECASE)]
            col = idx[0] if idx else -1
            continue
        if col < 0 or col >= len(cels) or re.fullmatch(r"[-: ]+", cels[col]):
            continue
        cel = cels[col].replace("*", "")
        for n, _ in numeros_no_texto(cel, "pt", {"numeros": {"ignorar_antes": r"(?!)", "ignorar_numero": []}}):
            out.append(n)
    return out


def _arred(v: Decimal, casas: int) -> Decimal:
    return v.quantize(Decimal(1).scaleb(-casas)) if casas else v.quantize(Decimal(1))


def lint_numeros(paths, dados, verificados, idioma):
    ev = carregar(dados, "evidence.json")
    ver = carregar_verificados(verificados)
    achados = []
    for path, texto in arquivos(paths):
        lang = idioma_de(path, idioma)
        for linha, s in blocos(path, texto):
            for n, m in numeros_no_texto(s, lang, ev):
                mesmos = [v for v in ver if v.unidade == n.unidade]
                if any(v.valor == n.valor and v.casas == n.casas for v in mesmos):
                    continue
                perto = [v for v in mesmos if v.casas != n.casas and (_arred(v.valor, n.casas) == n.valor or _arred(n.valor, v.casas) == v.valor)]
                if perto:
                    achados.append(Achado(path, linha, "R3", "P8", "erro", n.escrita, f"o verificado é {perto[0].escrita}: mesmo número, mesmo arredondamento"))
                else:
                    achados.append(Achado(path, linha, "R7", "P8", "erro", n.escrita, f"número fora do {Path(verificados).name}"))
    return achados


# ---------- exemplos ----------

def lint_exemplos(path):
    d = json.loads(Path(path).read_text(encoding="utf-8"))
    achados = []
    for sec in d.get("secoes", []):
        vistos = set()
        sinal = sec.get("sinal", "+")
        for mao in sec.get("maos", []):
            mid = mao.get("id")
            if mid in vistos:
                achados.append(Achado(path, 0, "R5", "P5", "erro", f"{sec.get('id')}/{mid}", "mão de exemplo repetida na seção"))
            vistos.add(mid)
            ev = mao.get("ev_perdido")
            fr = mao.get("freq_desvio")
            mostra = (ev is not None and ev > 0) or (fr is not None and fr != 0 and (fr > 0) == (sinal == "+"))
            if not mostra:
                achados.append(Achado(path, 0, "R5", "P5", "erro", f"{sec.get('id')}/{mid}", "a mão não mostra o desvio (EV perdido ≤ 0 e frequência sem o sinal do leak)"))
    return achados


# ---------- agentes ----------

# Frase de reserva: o `skills:` do frontmatter só vale quando o agente é chamado como subagente (Task).
# Rodando como thread principal (`claude --agent`), a skill não vem; a frase manda o agente carregá-la.
RESERVA = "chame a ferramenta Skill com casa:casa-conhecimento"
CASA = {"casa-conhecimento", "casa:casa-conhecimento"}


def frontmatter(texto: str) -> tuple[dict, str]:
    """Frontmatter YAML simples (chave: valor, listas inline ou em linhas "- x"), sem depender do PyYAML."""
    if not texto.startswith("---"):
        return {}, texto
    fim = texto.find("\n---", 3)
    if fim < 0:
        return {}, texto
    campos: dict = {}
    chave = None
    for ln in texto[3:fim].splitlines():
        if re.match(r"^\s+-\s+", ln) and chave:
            campos.setdefault(chave, []).append(ln.split("-", 1)[1].strip().strip("\"'"))
        elif ":" in ln and not ln.startswith(" "):
            chave, v = ln.split(":", 1)
            chave, v = chave.strip(), v.strip()
            if v.startswith("["):
                campos[chave] = [x.strip().strip("\"'") for x in v.strip("[]").split(",") if x.strip()]
            elif v:
                campos[chave] = v
    return campos, texto[fim + 4:]


def lint_agentes(paths):
    achados = []
    for path, texto in arquivos(paths):
        if not path.endswith(".md") or Path(path).name.startswith("sonda-"):
            continue  # as sondas da M4 testam a pré-carga e ficam de fora de propósito
        fm, corpo = frontmatter(texto)
        skills = fm.get("skills") or []
        if isinstance(skills, str):
            skills = [skills]
        if not skills or skills[0] not in CASA:
            achados.append(Achado(path, 1, "CASA", "A1", "erro", ", ".join(skills) or "sem skills:",
                                  "a casa-conhecimento vem primeiro no skills: (plano §2.2)"))
        if RESERVA not in corpo:
            achados.append(Achado(path, 1, "CASA", "A2", "erro", "sem frase de reserva",
                                  f"incluir no corpo: \"Se a casa-conhecimento não estiver no seu contexto, {RESERVA} antes de qualquer outra coisa.\""))
    return achados


# ---------- hash ----------

def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


def lint_hash(copia: str, lock: str | None):
    c = Path(copia)
    achados = []
    side = Path(copia + ".sha256")
    atual = sha256(c)
    if not side.is_file():
        achados.append(Achado(copia, 0, "HASH", "sha256", "erro", side.name, "falta o .sha256 ao lado da cópia"))
    elif side.read_text(encoding="utf-8").split()[0] != atual:
        achados.append(Achado(copia, 0, "HASH", "sha256", "erro", atual[:12], "a cópia não bate com o .sha256"))
    if lock:
        lk = json.loads(Path(lock).read_text(encoding="utf-8"))
        esperado = lk.get("dados", {}).get(c.name, {}).get("sha256")
        if esperado != atual:
            achados.append(Achado(copia, 0, "HASH", "lock", "erro", atual[:12], f"não bate com o casa.lock.json ({(esperado or 'ausente')[:12]})"))
    return achados


# ---------- main ----------

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="casa-lint", description=__doc__.splitlines()[0])
    ap.add_argument("--json", action="store_true", help="saída em JSON")
    ap.add_argument("--dados", help="pasta com banned_terms.json e evidence.json")
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("vocab")
    v.add_argument("--contexto", default="copy", choices=["mao", "paragrafo", "tela", "copy", "lancamento"])
    v.add_argument("--idioma", default="auto", choices=["auto", "pt", "en"])
    v.add_argument("paths", nargs="+")
    n = sub.add_parser("numeros")
    n.add_argument("--verificados", required=True)
    n.add_argument("--idioma", default="auto", choices=["auto", "pt", "en"])
    n.add_argument("paths", nargs="+")
    e = sub.add_parser("exemplos")
    e.add_argument("path")
    g = sub.add_parser("agentes")
    g.add_argument("paths", nargs="+")
    h = sub.add_parser("hash")
    h.add_argument("copia")
    h.add_argument("--lock")
    a = ap.parse_args(argv)

    if a.cmd == "vocab":
        achados = lint_vocab(a.paths, achar_dados(a.dados), a.contexto, a.idioma)
    elif a.cmd == "numeros":
        achados = lint_numeros(a.paths, achar_dados(a.dados), a.verificados, a.idioma)
    elif a.cmd == "exemplos":
        achados = lint_exemplos(a.path)
    elif a.cmd == "agentes":
        achados = lint_agentes(a.paths)
    else:
        achados = lint_hash(a.copia, a.lock)

    if a.json:
        print(json.dumps([asdict(x) for x in achados], ensure_ascii=False, indent=1))
    else:
        for x in achados:
            print(x)
        erros = sum(1 for x in achados if x.nivel == "erro")
        print(f"casa-lint {a.cmd}: {erros} erro(s), {len(achados) - erros} aviso(s)", file=sys.stderr)
    return 1 if any(x.nivel == "erro" for x in achados) else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stdin.reconfigure(encoding="utf-8")
    sys.exit(main())
