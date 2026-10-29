"""Leitura apenas. Reproduz a faixa 5/7/8/9 do flop para cada linha de tbl_field_exploit_rank (flop) com o
reference_band do lastro (tag v9, via PYTHONPATH), N = 1 por linha, field de cada linha mantido."""
import csv, os, sys, json
from collections import Counter, defaultdict
import psycopg2, psycopg2.extras
from lastro.poker import gto_aggregate as ga
from lastro.poker import field_exploit as F

HC = {6: "A", 5: "K", 4: "Q", 3: "J", 2: "T", 1: "low"}
TONE = {1: "rainbow", 2: "monotone", 3: "two_tone"}
PAIRED = {1: "unpaired", 2: "paired", 3: "trips"}
CONN = {0: "disconnected", 1: "oesd", 2: "connected", 3: "straightboard"}
cid = lambda r: f"{HC[r[0]]}_{TONE[r[1]]}_{PAIRED[r[2]]}_{CONN[r[3]]}"

con = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password=os.environ["AURA_PG_PASSWORD"])
cur = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
cur.execute("set transaction read only")
cur.execute("""select * from tbl_field_exploit_rank where street='flop' and snapshot_date='20261026'""")
rank = cur.fetchall()
cur.execute("""select solver_pair, stack_bb, actionsize, boardflophighcard h, boardtone t, pairedflop p,
  board_connectedness_fl c, gto_fold, gto_call, gto_raise, gto_allin, coverage, action_path, run_id
  from tbl_gto_reference where snapshot_date='20261022'""")
ref = defaultdict(list)
for r in cur.fetchall():
    ref[(r["solver_pair"], int(r["stack_bb"]), int(r["actionsize"]), r["h"], r["t"], r["p"], r["c"])].append(r)
cur.execute("""select * from tbl_field_exploit_release where street='flop' and snapshot_date='20261026'""")
rel = defaultdict(list)
for r in cur.fetchall():
    rel[(r["solver_pair"], int(r["stack_bb"]), r["boardflophighcard"], r["boardtone"], r["pairedflop"], r["board_connectedness_fl"])].append(r)

STRONG = F.STRONG_PP; TOL = F.TOL
fl = lambda x: None if x is None else float(x)

def cell_of(rows):
    def col(k):
        vs = [float(r[k]) for r in rows if r[k] is not None]
        return F.collapse_runs(vs) if vs else None
    fold = col("gto_fold")
    if fold is None: return None
    return ga.GtoCell(fold=fold, call=col("gto_call"), raise_=col("gto_raise"), allin=col("gto_allin"), n_runs=1,
                      n_cells=1, reach_total=1.0, dispersion_pp=0.0, fused=False, provenance={})

out = []
miss = Counter()
for r in rank:
    pair, stack, size = r["solver_pair"], int(r["stack_bb"]), int(r["actionsize"])
    key = (pair, stack, size, r["boardflophighcard"], r["boardtone"], r["pairedflop"], r["board_connectedness_fl"])
    c = cid(key[3:])
    node = F.flop_reaction_node(pair, size)
    field = float(r["field_value"])
    row = dict(pair=pair, stack=stack, size=F.FLOP_SIZE_LABEL[size], cls=c, node=node, n=r["pool_n"],
               field=field * 100, is_headline=r["is_headline"], class_model=r["class_model"],
               stored_gto=float(r["gto_value"]) * 100, stored_hw=r["band_half_width_pp"], stored_dev=r["deviation_pts"],
               stored_dir=r["direction"], stored_qualifies=r["qualifies"], spot_rank=r["spot_rank"])
    rrows = ref.get(key)
    cell = cell_of(rrows) if rrows else None
    if cell is None:
        miss["no_cell"] += 1
        continue
    for v in (5, 7, 8, 9):
        if r["class_model"]:
            # célula class_model: o σ é o do modelo de classe em todas as versões (sem termo do rep, sem v9)
            hw = float(r["band_half_width_pp"]); ctr = float(r["gto_value"]); wide = False
        else:
            b = ga.reference_band([ga.ClassSlice(c, cell, 1.0)], street="flop", role="reaction", node=node,
                                  solver_pair=pair, stack_bb=stack, band_version=v)
            if isinstance(b, ga.GtoGate):
                row[f"v{v}_gate"] = str(b); row[f"v{v}_dev"] = None; row[f"v{v}_wide"] = None; continue
            hw = b.half_width_pp; ctr = b.center; wide = bool(b.wide)
        d = abs(field - ctr) * 100 - hw
        row[f"v{v}_center"] = ctr * 100; row[f"v{v}_hw"] = hw; row[f"v{v}_lo"] = ctr * 100 - hw; row[f"v{v}_hi"] = ctr * 100 + hw
        row[f"v{v}_dev"] = max(d, 0.0); row[f"v{v}_wide"] = wide
        row[f"v{v}_dir"] = "overfold" if field > ctr else "overdefend"
        row[f"v{v}_strong"] = (not wide) and d >= STRONG - TOL
    rl = rel.get((pair, stack) + key[3:])
    if rl:
        row["release"] = ";".join(f"{x['release_date']}|{'GRATIS' if x['free_week'] else 'Individual'}|{x['strength']}|{x['card_key']}" for x in rl)
    out.append(row)

fields = sorted({k for r in out for k in r}, key=lambda k: (k not in ("pair","stack","size","cls"), k))
with open(sys.argv[1], "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(out)
tot = Counter()
for r in out:
    tot["rows"] += 1
    for v in (5, 7, 8, 9):
        tot[f"strong_v{v}"] += bool(r.get(f"v{v}_strong"))
        tot[f"wide_v{v}"] += bool(r.get(f"v{v}_wide"))
        tot[f"headline_strong_v{v}"] += bool(r["is_headline"] and r.get(f"v{v}_strong"))
    tot["stored_strong_ge5"] += (abs(r["stored_dev"] or 0) >= 5 - TOL)
    tot["v5_matches_stored"] += abs((r.get("v5_dev") or 0) - abs(r["stored_dev"] or 0)) < 1e-6
    tot["center_same_5_8"] += abs(r.get("v5_center", 0) - r.get("v8_center", 1)) < 1e-9
    tot["center_same_8_9"] += abs(r.get("v8_center", 0) - r.get("v9_center", 1)) < 1e-9
    tot["v7_eq_v8"] += abs((r.get("v7_dev") or 0) - (r.get("v8_dev") or 0)) < 1e-9 and r.get("v7_wide") == r.get("v8_wide")
print(json.dumps(dict(tot), indent=1), dict(miss))
