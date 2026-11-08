#!/usr/bin/env python3
"""Is the SFT more accurate than classic? Week-by-week accuracy ledger: classic vs SFT as written vs SFT average.

For each player-week with a known outcome, the 1-week points forecast of
  classic           the baseline in the prompt
  SFT as written    classic + the greedy delta the adapter wrote
  SFT average       classic + the mean of the adapter's own distribution (scripts/expectation_decode.py)
is scored against the actual points: RMSE (what expected-points decisions care about), MAE, bias
(forecast minus actual), and how often the SFT version lands closer than classic. Also split by
whether the prompt had any text evidence, and for decision-relevant players (classic >= 4 points).

usage: track_sft_accuracy.py --set LABEL EXAMPLES GREEDY EXPECTED [--set ...] [--labels-csv TABLE] --out-md OUT.md
EXAMPLES rows carry metadata.labels.points_1gw when built after the week settled; otherwise the
actual points are joined from --labels-csv (data/fpl_training_rows_v3_contract_f6.csv after the weekly
ingest; label_points_1gw on a week-w row is the points scored in week w) by season/week/player_id.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.llm_adjust import parse_delta_response  # noqa: E402


def load_preds(path):
    out = {}
    for line in open(path):
        if line.strip():
            p = json.loads(line)
            out[(str(p["season"]), int(p["week"]), int(p["metadata"]["player_id"]))] = parse_delta_response(p["response"]) or {}
    return out


def metrics(base, written, average, actual):
    e_c, e_w, e_a = base - actual, written - actual, average - actual
    r = lambda e: float(np.sqrt(np.mean(e ** 2)))  # noqa: E731
    return {"n": int(len(actual)),
            "rmse": (r(e_c), r(e_w), r(e_a)),
            "mae": (float(np.mean(np.abs(e_c))), float(np.mean(np.abs(e_w))), float(np.mean(np.abs(e_a)))),
            "bias": (float(np.mean(e_c)), float(np.mean(e_w)), float(np.mean(e_a))),
            "closer": (float(np.mean(np.abs(e_w) < np.abs(e_c))), float(np.mean(np.abs(e_a) < np.abs(e_c))))}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", nargs=4, action="append", metavar=("LABEL", "EXAMPLES", "GREEDY", "EXPECTED"), required=True)
    ap.add_argument("--labels-csv")
    ap.add_argument("--out-md", required=True)
    args = ap.parse_args()
    actual_lookup = {}
    if args.labels_csv:
        import pandas as pd
        t = pd.read_csv(args.labels_csv, usecols=["season", "week", "player_id", "label_points_1gw"], low_memory=False)
        t = t[["season", "week", "player_id", "label_points_1gw"]]  # itertuples follows frame order, not usecols order
        actual_lookup = {(str(s), int(w), int(p)): float(y) for s, w, p, y in t.itertuples(index=False) if y == y}

    lines = ["# SFT accuracy ledger: classic vs SFT as written vs SFT average", "",
             "1-week points forecasts scored against actual points. RMSE is the one that matters for expected-points decisions; "
             "bias is forecast minus actual (negative = under-forecast). \"Closer\" = share of player-weeks where that SFT version "
             "lands nearer the actual than classic.", ""]
    head = ("| Set | Player-weeks | RMSE classic / written / average | MAE classic / written / average | "
            "Bias classic / written / average | Closer than classic: written / average |")
    for label, ex_path, g_path, e_path in args.set:
        greedy, expected = load_preds(g_path), load_preds(e_path)
        rows = []
        for line in open(ex_path):
            r = json.loads(line); m = r["metadata"]
            key = (str(r["season"]), int(r["week"]), int(m["player_id"]))
            y = (m.get("labels") or {}).get("points_1gw")
            if y is None:
                y = actual_lookup.get(key)
            if y is None or key not in greedy or key not in expected:
                continue
            b = float(m["baseline_forecast"]["baseline_points_1gw"])
            evid = "No timestamp-safe text evidence is available" not in r["prompt"]
            rows.append((int(r["week"]), b, b + greedy[key].get("delta_points_1gw", 0.0), b + expected[key].get("delta_points_1gw", 0.0), float(y), evid))
        if not rows:
            lines += [f"## {label}", "", "No settled outcomes yet.", ""]
            continue
        week, base, wr, av, act, evid = map(np.array, zip(*rows))
        groups = [("All", np.ones_like(act, dtype=bool))] + [(f"GW{w}", week == w) for w in sorted(set(week.tolist()))] + [
            ("With text evidence", evid.astype(bool)), ("No text evidence", ~evid.astype(bool)),
            ("Classic forecast >= 4 (decision-relevant)", base >= 4)]
        lines += [f"## {label}", "", head, "|---|---|---|---|---|---|"]
        for name, sel in groups:
            if sel.sum() < 20:
                continue
            m = metrics(base[sel], wr[sel], av[sel], act[sel])
            f3 = lambda t, d=3: " / ".join(f"{x:.{d}f}" for x in t)  # noqa: E731
            lines.append(f"| {name} | {m['n']} | {f3(m['rmse'])} | {f3(m['mae'])} | {' / '.join(f'{x:+.2f}' for x in m['bias'])} | "
                         f"{m['closer'][0]:.0%} / {m['closer'][1]:.0%} |")
        lines.append("")
    Path(args.out_md).write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
