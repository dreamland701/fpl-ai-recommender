#!/usr/bin/env python3
"""Exact transfer routes that MUST bring in a named player (Wes, 2026-10-28: "ideally I can get Isak back - should I
couple it with another move from midfield, defence or keeper to enable that?"). Same engine and conventions as
milp_routes.py (fpl_ai.squad_milp.optimize: captain doubled, 0.1 x bench, hits -4, out/suspended players zeroed),
value = GW10-14 (p5) and GW10 only (p1); for 1, 2 and 3 transfers with the forced player in, plus the plain
OUT -> IN single swap when FORCE_OUT is given. usage: PACKET_DIR=<dir> FORCE_IN=Isak [FORCE_OUT="João Pedro"] python3 forced_routes.py
Writes <PACKET_DIR>/forced_routes.json."""
import json, os, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.squad_milp import optimize  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))
from decide import zero_if_out  # noqa: E402

P = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent))
F = {}
for l in open(P / "forecasts_new_pipeline.jsonl"):
    r = zero_if_out(json.loads(l)); F[int(r["player_id"])] = r
state = json.loads((P / "entry_state.json").read_text())
sell = {int(s["player_id"]): float(s["selling_price"]) for s in state["squad"]}
name = {pid: r["name"] for pid, r in F.items()}


def resolve(label: str) -> int:
    hits = [pid for pid, n in name.items() if n.lower() == label.lower()]
    if len(hits) != 1:
        raise SystemExit(f"{label!r}: {len(hits)} matches {[name[p] for p in hits]}")
    return hits[0]


force_in = [resolve(x.strip()) for x in os.environ.get("FORCE_IN", "Isak").split(",") if x.strip()]
force_out = [resolve(x.strip()) for x in os.environ.get("FORCE_OUT", "").split(",") if x.strip()]
for pid in force_in:
    r = F[pid]
    print(f"forced in: {r['name']} ({r['pos']}, {r['price']}, {r['status']}/{r['chance']}) GW10 {r['p1']:.2f} GW10-14 {r['p5']:.2f} mins {r['mins']} P(app) {r['papp']}")
print("bank", state["bank"], "free transfers", state["free_transfers"], "| sells:", ", ".join(f"{name[p]} {v}" for p, v in sell.items()))
out = {}
for label, key in (("GW10-14", "p5"), ("GW10 only", "p1")):
    value = {pid: float(r[key]) for pid, r in F.items()}
    kw = dict(bank=float(state["bank"]), free_transfers=int(state["free_transfers"]))
    hold = optimize(F, value, sell, max_transfers=0, **kw)
    print(f"{label} hold: value {hold['net']:.1f}; XI {', '.join(name[p] for p in hold['xi'])}; C {name[hold['captain']]}")
    routes = [(f"forced max{k}", dict(max_transfers=k, forced_in=force_in)) for k in (1, 2, 3)]
    if force_out:
        routes.insert(0, ("plain swap", dict(max_transfers=len(force_in), forced_in=force_in, forced_out=force_out)))
    for tag, extra in routes:
        try:
            res = optimize(F, value, sell, **kw, **extra)
        except Exception as e:  # infeasible (e.g. cannot afford with one move)
            print(f"  {tag}: infeasible ({e})"); out[f"{label}_{tag}"] = {"infeasible": str(e)}; continue
        o = [name[p] for p in sell if p not in res["squad"]]; i = [name[p] for p in res["in"]]
        out[f"{label}_{tag}"] = {"net_gain": round(res["net"] - hold["net"], 2), "out": o, "in": i, "itb": res["bank_after"],
                                 "hit": 4 * int(res["hits"]), "xi": [name[p] for p in res["xi"]], "captain": name[res["captain"]],
                                 "bench": [name[p] for p in res["squad"] if p not in res["xi"]]}
        print(f"  {tag}: {res['net'] - hold['net']:+5.1f} OUT {'+'.join(o) or '-'} IN {'+'.join(i) or '-'} itb {res['bank_after']} hit {4 * int(res['hits'])} | C {name[res['captain']]}")
        print(f"       XI {', '.join(name[p] for p in res['xi'])} | bench {', '.join(name[p] for p in res['squad'] if p not in res['xi'])}")
(P / "forced_routes.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print("wrote", P / "forced_routes.json")
