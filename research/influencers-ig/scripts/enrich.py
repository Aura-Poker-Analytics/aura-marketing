"""Fase 2: enriquecimento via Instagram Graph API (Business Discovery).

Token: variavel META_IG_TOKEN (processo) ou registro do usuario do Windows. Nunca impresso.
Cache em disco (cache/<handle>.json): nao repete chamada. Limite ~190 chamadas/hora.
Uso: python -X utf8 -I enrich.py [--test] [--limit N]
"""
import csv, json, os, sys, time, urllib.parse, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW, CACHE = ROOT / "raw", ROOT / "cache"
CACHE.mkdir(exist_ok=True)
IG_ID = "17841468976680108"
API = "https://graph.facebook.com/v21.0"
PER_HOUR = 190
FIELDS = ("business_discovery.username({u}){{username,name,followers_count,media_count,biography,"
          "media.limit(12){{timestamp,like_count,comments_count,caption}}}}")


def token():
    t = os.environ.get("META_IG_TOKEN")
    if not t and os.name == "nt":
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment") as k:
            t = winreg.QueryValueEx(k, "META_IG_TOKEN")[0]
    if not t:
        sys.exit("META_IG_TOKEN ausente")
    return t


TOKEN = token()
calls = []  # timestamps da janela de 1h


def get(path, params):
    now = time.time()
    while calls and now - calls[0] > 3600:
        calls.pop(0)
    if len(calls) >= PER_HOUR:
        wait = 3600 - (now - calls[0]) + 1
        print(f"limite horario, aguardando {wait:.0f}s", flush=True)
        time.sleep(wait)
    calls.append(time.time())
    url = f"{API}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read())
        except Exception:
            return e.code, {"error": {"message": "http error"}}
    except Exception as e:  # nunca ecoar URL/token
        return 0, {"error": {"message": type(e).__name__}}


def norm(h):
    return h.strip().lstrip("@").lower().rstrip(".,;/")


def handles():
    seen = {}
    for f in ("brasil", "latam", "ingles"):
        for r in csv.DictReader(open(RAW / f"{f}.csv", encoding="utf-8-sig")):
            h = norm(r["handle"])
            if h and h not in seen:
                seen[h] = f
    return seen


def main():
    if "--test" in sys.argv:
        s, j = get("me/accounts", {"fields": "id,name,instagram_business_account"})
        print("me/accounts", s, json.dumps(j)[:600])
        s, j = get(IG_ID, {"fields": "username,followers_count"})
        print("ig id", s, json.dumps(j)[:300])
        return
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 10**9
    todo = [h for h in handles() if not (CACHE / f"{h}.json").exists()][:limit]
    print(f"a consultar: {len(todo)}", flush=True)
    for i, h in enumerate(todo, 1):
        s, j = get(IG_ID, {"fields": FIELDS.format(u=h)})
        err = j.get("error", {})
        if err.get("code") in (4, 17, 32, 613) or s == 429:
            print("rate limit da API, aguardando 15 min", flush=True)
            time.sleep(900)
            s, j = get(IG_ID, {"fields": FIELDS.format(u=h)})
            err = j.get("error", {})
        if err.get("code") in (190, 102):
            sys.exit("token invalido/expirado: parar")
        (CACHE / f"{h}.json").write_text(json.dumps({"status": s, "resp": j}, ensure_ascii=False), encoding="utf-8")
        print(i, h, s, err.get("code", "ok"), flush=True)
        time.sleep(1)


main()
