"""Score a week's shadow-adapter read against the settled live points, without waiting for the table rebuild.

Inputs: a reghead prediction file (one JSON per player with metadata.baseline_forecast and a response holding the
deltas) and the FPL live endpoint dump for the week. Reports classic vs classic+SFT on 1GW points (RMSE, MAE, bias,
decision-relevant rows = classic >= 4) and on P(appear) (Brier, AUC against minutes > 0), plus the biggest misses.

Usage: python3 scripts/score_shadow_week.py --pred reports/h_series/h5_gw9final_pred.jsonl \
         --live reports/gw9_packet_2026_10/entry/live_gw9.json --label "H5 final read, GW9" --out <md>
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def auc(scores, labels):
    pos = [s for s, l in zip(scores, labels) if l]
    neg = [s for s, l in zip(scores, labels) if not l]
    if not pos or not neg:
        return float("nan")
    wins = 0.0
    for p in pos:
        for n in neg:
            wins += 1.0 if p > n else 0.5 if p == n else 0.0
    return wins / (len(pos) * len(neg))


def stats(pred, actual):
    n = len(pred)
    err = [p - a for p, a in zip(pred, actual)]
    return {"n": n, "rmse": math.sqrt(sum(e * e for e in err) / n), "mae": sum(abs(e) for e in err) / n, "bias": sum(err) / n}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pred", required=True)
    ap.add_argument("--live", required=True)
    ap.add_argument("--label", default="shadow read")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    live = {e["id"]: e["stats"] for e in json.load(open(a.live))["elements"]}
    rows = []
    for line in open(a.pred):
        r = json.loads(line); m = r["metadata"]; b = m["baseline_forecast"]; d = json.loads(r["response"])
        st = live.get(m["player_id"])
        if st is None:
            continue
        c1 = b["baseline_points_1gw"]; s1 = c1 + d.get("delta_points_1gw", 0.0)
        cp = b.get("baseline_appearance_probability", 0.0); sp = min(1.0, max(0.0, cp + d.get("delta_appearance_probability", 0.0)))
        rows.append({"name": m.get("player_name"), "pos": m.get("position"), "c1": c1, "s1": s1, "cp": cp, "sp": sp,
                     "actual": st["total_points"], "played": st["minutes"] > 0, "minutes": st["minutes"]})
    out = [f"# {a.label}: shadow accuracy vs settled points ({len(rows)} players)", ""]
    allc = stats([r["c1"] for r in rows], [r["actual"] for r in rows]); alls = stats([r["s1"] for r in rows], [r["actual"] for r in rows])
    dec = [r for r in rows if r["c1"] >= 4]
    decc = stats([r["c1"] for r in dec], [r["actual"] for r in dec]) if dec else None
    decs = stats([r["s1"] for r in dec], [r["actual"] for r in dec]) if dec else None
    closer = sum(abs(r["s1"] - r["actual"]) < abs(r["c1"] - r["actual"]) for r in dec) / len(dec) if dec else float("nan")
    out += ["| Set | n | RMSE classic | RMSE SFT | MAE classic | MAE SFT | bias classic | bias SFT |", "|---|---|---|---|---|---|---|---|",
            f"| all | {allc['n']} | {allc['rmse']:.3f} | {alls['rmse']:.3f} | {allc['mae']:.3f} | {alls['mae']:.3f} | {allc['bias']:+.2f} | {alls['bias']:+.2f} |"]
    if dec:
        out.append(f"| classic >= 4 | {decc['n']} | {decc['rmse']:.3f} | {decs['rmse']:.3f} | {decc['mae']:.3f} | {decs['mae']:.3f} | {decc['bias']:+.2f} | {decs['bias']:+.2f} |")
        out.append(f"\nSFT closer than classic on {closer:.0%} of the classic >= 4 rows.")
    played = [r["played"] for r in rows]
    bc = sum((r["cp"] - r["played"]) ** 2 for r in rows) / len(rows); bs = sum((r["sp"] - r["played"]) ** 2 for r in rows) / len(rows)
    unc = [r for r in rows if 0.15 <= r["cp"] <= 0.9]
    out += ["", "| P(appear) | n | Brier classic | Brier SFT | AUC classic | AUC SFT |", "|---|---|---|---|---|---|",
            f"| all | {len(rows)} | {bc:.4f} | {bs:.4f} | {auc([r['cp'] for r in rows], played):.3f} | {auc([r['sp'] for r in rows], played):.3f} |"]
    if unc:
        out.append(f"| classic P in [0.15, 0.9] | {len(unc)} | {sum((r['cp'] - r['played']) ** 2 for r in unc) / len(unc):.4f} | {sum((r['sp'] - r['played']) ** 2 for r in unc) / len(unc):.4f} | "
                   f"{auc([r['cp'] for r in unc], [r['played'] for r in unc]):.3f} | {auc([r['sp'] for r in unc], [r['played'] for r in unc]):.3f} |")
    dnp = [r for r in rows if not r["played"] and r["cp"] >= 0.5]
    out += ["", f"Forecast starters (classic P >= 0.5) who did not play: {len(dnp)}: " + ", ".join(f"{r['name']} (P {r['cp']:.2f} -> {r['sp']:.2f})" for r in sorted(dnp, key=lambda r: -r['cp'])[:12])]
    out += ["", "## Biggest misses (actual - classic)", "", "| Player | Pos | Min | Actual | Classic | SFT |", "|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: -abs(r["actual"] - r["c1"]))[:10]:
        out.append(f"| {r['name']} | {r['pos']} | {r['minutes']} | {r['actual']} | {r['c1']:.2f} | {r['s1']:.2f} |")
    out += ["", "## Largest SFT-vs-classic disagreements on points", "", "| Player | Pos | Min | Actual | Classic | SFT | SFT closer? |", "|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: -abs(r["s1"] - r["c1"]))[:10]:
        out.append(f"| {r['name']} | {r['pos']} | {r['minutes']} | {r['actual']} | {r['c1']:.2f} | {r['s1']:.2f} | {'yes' if abs(r['s1'] - r['actual']) < abs(r['c1'] - r['actual']) else 'no'} |")
    text = "\n".join(out)
    print(text)
    if a.out:
        Path(a.out).write_text(text + "\n")


if __name__ == "__main__":
    main()
