"""Leitura semanal de insights por post do Instagram da Aura (agente G1 Vigia).

Só lê. Usa a Instagram Graph API com o token em META_IG_TOKEN (nunca impresso
nem gravado). Grava um CSV por semana em instagram/insights/ e imprime um
resumo curto com os posts que mais salvaram e compartilharam.

Uso:
    python scripts/ig_insights_semanal.py            # últimos 7 dias
    python scripts/ig_insights_semanal.py --dias 28  # janela maior
    python scripts/ig_insights_semanal.py --checar   # só confere token e conta
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

IG_USER_ID = "17841468976680108"  # @aurapokeranalytics
GRAPH = "https://graph.facebook.com/" + os.environ.get("META_GRAPH_VERSION", "v23.0")
SAIDA = Path(__file__).resolve().parent.parent / "instagram" / "insights"

# Métricas por tipo de mídia. Pedidas uma a uma: se a Meta recusar uma
# (descontinuada ou não suportada no tipo), a linha fica vazia nela.
METRICAS = {
    "FEED": ["reach", "views", "saved", "shares", "likes", "comments", "total_interactions", "profile_visits"],
    "REELS": ["reach", "views", "saved", "shares", "likes", "comments", "total_interactions", "ig_reels_avg_watch_time"],
    "STORY": ["reach", "views", "shares", "replies", "total_interactions", "navigation"],
}


def _token() -> str:
    tok = os.environ.get("META_IG_TOKEN", "")
    if not tok:
        sys.exit("META_IG_TOKEN não definida. Peça ao Rafael (ação INSTA-TOKEN).")
    return tok


def _get(caminho: str, **params) -> dict:
    params["access_token"] = _token()
    url = f"{GRAPH}/{caminho}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        # A mensagem de erro da Graph API não traz o token; a URL traz, então nunca a mostramos.
        try:
            msg = json.load(e).get("error", {}).get("message", "")
        except Exception:
            msg = ""
        raise RuntimeError(f"Graph API {e.code} em {caminho}: {msg}") from None


def midias_desde(desde: dt.datetime) -> list[dict]:
    campos = "id,caption,media_type,media_product_type,permalink,timestamp"
    pagina = _get(f"{IG_USER_ID}/media", fields=campos, limit=50)
    saida = []
    while True:
        for m in pagina.get("data", []):
            ts = dt.datetime.strptime(m["timestamp"], "%Y-%m-%dT%H:%M:%S%z")
            if ts < desde:
                return saida
            saida.append(m)
        prox = pagina.get("paging", {}).get("cursors", {}).get("after")
        if not prox or "next" not in pagina.get("paging", {}):
            return saida
        pagina = _get(f"{IG_USER_ID}/media", fields=campos, limit=50, after=prox)


def insights(midia: dict) -> dict:
    tipo = midia.get("media_product_type") or "FEED"
    valores = {}
    for metrica in METRICAS.get(tipo, METRICAS["FEED"]):
        try:
            dados = _get(f"{midia['id']}/insights", metric=metrica).get("data", [])
            valores[metrica] = dados[0]["values"][0]["value"] if dados else ""
        except RuntimeError:
            valores[metrica] = ""
    return valores


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=7)
    ap.add_argument("--checar", action="store_true")
    args = ap.parse_args()

    if args.checar:
        conta = _get(IG_USER_ID, fields="username,media_count")
        print(f"ok: @{conta.get('username')} com {conta.get('media_count')} mídias")
        return

    desde = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.dias)
    linhas = []
    for m in midias_desde(desde):
        linha = {
            "data": m["timestamp"][:10],
            "tipo": m.get("media_product_type") or m.get("media_type"),
            "link": m.get("permalink", ""),
            "legenda": (m.get("caption") or "").replace("\n", " ")[:80],
        }
        linha.update(insights(m))
        linhas.append(linha)

    SAIDA.mkdir(parents=True, exist_ok=True)
    arquivo = SAIDA / f"ig-insights-{dt.date.today().isoformat()}-{args.dias}d.csv"
    colunas = ["data", "tipo", "link", "legenda"] + sorted({k for l in linhas for k in l} - {"data", "tipo", "link", "legenda"})
    with arquivo.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=colunas)
        w.writeheader()
        w.writerows(linhas)

    def num(l, k):
        return l.get(k) if isinstance(l.get(k), (int, float)) else 0

    print(f"{len(linhas)} posts em {args.dias} dias -> {arquivo}")
    for l in sorted(linhas, key=lambda l: num(l, "saved") + num(l, "shares"), reverse=True)[:5]:
        print(f"  {l['data']} {l['tipo']:<6} alcance={l.get('reach', '')} salvos={l.get('saved', '')} "
              f"compart.={l.get('shares', '')}  {l['legenda'][:50]}")


if __name__ == "__main__":
    main()
