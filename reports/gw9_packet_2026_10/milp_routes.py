#!/usr/bin/env python3
"""Exact transfer optimizer (fpl_ai.squad_milp.optimize) on a packet's forecasts: value = GW9-13 (p5) or GW9 only
(p1), captain doubled, 0.1 x bench, hits -4, at most 0..3 transfers, plus the exact wildcard / free-hit rebuilds.
Writes <PACKET_DIR>/milp_transfers.json.  usage: PACKET_DIR=reports/gw9_packet_2026_10/final python3 milp_routes.py"""
import json, os, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.squad_milp import optimize  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))
from decide import zero_if_out  # noqa: E402  (2026-10-27: out/suspended players carry 0, as in the decision sheet)

P = Path(os.environ.get("PACKET_DIR", Path(__file__).resolve().parent / "final"))
F = {}
for l in open(P / "forecasts_new_pipeline.jsonl"):
    r = zero_if_out(json.loads(l)); F[int(r["player_id"])] = r
print("zeroed:", ", ".join(r["name"] for r in F.values() if r.get("zeroed")) or "none")
state = json.loads((P / "entry_state.json").read_text())
sell = {int(s["player_id"]): float(s["selling_price"]) for s in state["squad"]}
name = {pid: r["name"] for pid, r in F.items()}
out = {}
for label, key, chip in (("GW9-13", "p5", "wildcard"), ("GW9 only", "p1", "free_hit")):
    value = {pid: float(r[key]) for pid, r in F.items()}
    kw = dict(bank=float(state["bank"]), free_transfers=int(state["free_transfers"]))
    hold = optimize(F, value, sell, max_transfers=0, **kw)
    print(f"{label} hold: value {hold['net']:.1f}; XI {', '.join(name[p] for p in hold['xi'])}; C {name[hold['captain']]}")
    for k in (1, 2, 3):
        res = optimize(F, value, sell, max_transfers=k, **kw)
        o = [name[p] for p in sell if p not in res["squad"]]; i = [name[p] for p in res["in"]]
        out[f"{label}_max{k}"] = {"net_gain": round(res["net"] - hold["net"], 2), "out": o, "in": i, "itb": res["bank_after"],
                                  "hit": 4 * int(res["hits"]), "xi": [name[p] for p in res["xi"]], "captain": name[res["captain"]]}
        print(f"  max {k}: {res['net'] - hold['net']:+5.1f} OUT {'+'.join(o) or '-'} IN {'+'.join(i) or '-'} itb {res['bank_after']} hit {4 * int(res['hits'])} | C {name[res['captain']]}")
    wc = optimize(F, value, sell, wildcard=True, **kw)
    out[f"{label}_{chip}"] = {"net_gain": round(wc["net"] - hold["net"], 2), "squad": [name[p] for p in wc["squad"]], "itb": wc["bank_after"], "captain": name[wc["captain"]]}
    print(f"  {chip}: {wc['net'] - hold['net']:+5.1f} itb {wc['bank_after']} | {', '.join(name[p] for p in wc['squad'])}")
(P / "milp_transfers.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print("wrote", P / "milp_transfers.json")
