#!/usr/bin/env python3
"""Live parity check for the F16 wiring (2026-10-28), on a settled gameweek whose article the training table holds.

1. Category parity: scripts/live_team_news.py on the week's frozen snapshot + Guardian store must reproduce the
   categories scripts/build_team_news_table.py wrote for the same (season, week, player_id) keys.
2. Frame parity: CanonicalDataset.build_live_week_frame on the _teamnews table with FPL_TEAM_NEWS_LIVE_JSON set must
   carry gn_* columns identical to the training rows of that week (same player_id), and the fitted suite's forecasts
   with the live gn_* must differ from the forecasts with gn_* zeroed only where the categories differ from "no article".

usage: PYTHONPATH=src FPL_PRIOR_BLEND=1 FPL_OPPONENT_INTERACTION=1 FPL_TEAM_NEWS_FEATS=1 python scripts/team_news_live_parity.py \
         --event 7 --snapshot reports/gw7_packet_2026_10/snapshot --store reports/evidence_guardian_football_2627_gw7final.jsonl \
         --table data/fpl_training_rows_v3_contract_f6_teamnews.csv --table-feat reports/team_news_f16/gn_feat.json \
         --out reports/team_news_f16/live_parity_gw7.md
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
PY = sys.executable


class FrozenClient:
    def __init__(self, snap: Path) -> None:
        self._bootstrap = json.loads((snap / "bootstrap_static.json").read_text())
        self._fixtures = json.loads((snap / "fixtures.json").read_text())

    def bootstrap_static(self):
        return self._bootstrap

    def fixtures(self):
        return self._fixtures


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--event", type=int, required=True)
    ap.add_argument("--season", default="2026-27")
    ap.add_argument("--snapshot", required=True)
    ap.add_argument("--store", action="append", required=True)
    ap.add_argument("--table", required=True)
    ap.add_argument("--table-feat", required=True, help="gn_feat.json written by build_team_news_table.py --feat-json")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    snap = Path(args.snapshot)
    live_json = ROOT / "reports/team_news_f16" / f"gn_feat_live_gw{args.event}_paritycheck.json"
    cmd = [PY, str(ROOT / "scripts/live_team_news.py"), "--event", str(args.event), "--season", args.season,
           "--bootstrap", str(snap / "bootstrap_static.json"), "--out", str(live_json)]
    for s in args.store:
        cmd += ["--store", s]
    run = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    lines = [f"# F16 live parity, {args.season} GW{args.event}", "", "## 1. Category parity (live parser vs table builder)", "",
             "```", run.stdout.strip().splitlines()[0] if run.stdout.strip() else run.stderr.strip()[-500:], "```", ""]
    live = json.loads(live_json.read_text()) if live_json.exists() else {}
    table_feat = {k: v for k, v in json.load(open(args.table_feat)).items() if k.startswith(f"{args.season}|{args.event}|")}
    keys = set(live) | set(table_feat)
    same = sum(1 for k in keys if live.get(k) == table_feat.get(k))
    diff = [(k, table_feat.get(k), live.get(k)) for k in sorted(keys) if live.get(k) != table_feat.get(k)]
    lines += [f"live keys {len(live)}, table keys {len(table_feat)}, identical {same}/{len(keys)}; differences {len(diff)}", ""]
    if diff:
        lines += ["| key | table | live |", "|---|---|---|"] + [f"| {k} | {a} | {b} |" for k, a, b in diff[:40]] + [""]
    # 2. frame parity
    from fpl_ai.api import OfficialSnapshotService
    from fpl_ai.dataset import CanonicalDataset, training_rows_asof
    from fpl_ai.models import fit_model_suite_from_frame

    deadline = json.loads((snap / "manifest.json").read_text())["deadline_time"]
    dataset = CanonicalDataset.from_csv(args.table)
    gn = ["gn_article", "gn_xi", "gn_sub", "gn_doubtful", "gn_out"]
    feats = dataset.feature_columns
    lines += ["## 2. Frame parity", "", f"feature columns {len(feats)}, gn_* in model: {[c for c in gn if c in feats]}", ""]
    official = OfficialSnapshotService(client=FrozenClient(snap)).build_current_week_frame(deadline)
    os.environ["FPL_TEAM_NEWS_LIVE_JSON"] = str(live_json)
    live_frame = dataset.build_live_week_frame(official, history_root="data/fpl_history")
    os.environ.pop("FPL_TEAM_NEWS_LIVE_JSON")
    live_off = dataset.build_live_week_frame(official, history_root="data/fpl_history")
    rows = dataset.training_frame[(dataset.training_frame.season == args.season) & (dataset.training_frame.week == args.event)]
    m = live_frame[["player_id"] + gn].merge(rows[["player_id"] + gn], on="player_id", suffixes=("_live", "_table"))
    mism = {c: int((m[f"{c}_live"] != m[f"{c}_table"]).sum()) for c in gn}
    lines += [f"players in both frames {len(m)}; live gn_* means {live_frame[gn].mean().round(3).to_dict()}; table week means {rows[gn].mean().round(3).to_dict()}",
              f"mismatches per column: {mism}", f"gn_* in the frame without the live file: {live_off[gn].abs().sum().to_dict()} (expect all 0)", ""]
    # 3. forecast delta from the categories alone
    train = training_rows_asof(dataset.training_frame, args.season, args.event)
    suite = fit_model_suite_from_frame(train_frame=train, feature_names=feats)
    f_on = {f.player_id: f for f in suite.predict_frame(live_frame)}
    f_off = {f.player_id: f for f in suite.predict_frame(live_off)}
    cat = live_frame.set_index("player_id")
    recs = []
    for pid, f in f_on.items():
        g = f_off.get(pid)
        if g is None:
            continue
        c = "none" if cat.at[pid, "gn_article"] == 0 else ("XI" if cat.at[pid, "gn_xi"] else "sub" if cat.at[pid, "gn_sub"] else "doubtful" if cat.at[pid, "gn_doubtful"] else "out")
        recs.append({"player": f.player_name, "cat": c, "d1": f.predicted_points_1gw - g.predicted_points_1gw,
                     "dmin": f.predicted_minutes - g.predicted_minutes, "p1_on": f.predicted_points_1gw, "min_on": f.predicted_minutes})
    d = pd.DataFrame(recs)
    lines += ["## 3. Forecast movement from the live categories (classic+F6+F16 with vs without the article)", "",
              "| category | n | mean Δ GW pts | mean Δ minutes |", "|---|---|---|---|"]
    for c, g in d.groupby("cat"):
        lines.append(f"| {c} | {len(g)} | {g.d1.mean():+.3f} | {g.dmin.mean():+.1f} |")
    lines += ["", "Largest moves:", ""] + [f"- {r.player} ({r.cat}): GW {r.d1:+.2f}, minutes {r.dmin:+.1f} (now {r.p1_on:.2f} / {r.min_on:.0f})"
                                          for r in d.reindex(d.d1.abs().sort_values(ascending=False).index).head(12).itertuples()]
    Path(args.out).write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
