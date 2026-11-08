#!/usr/bin/env python3
"""Returner-pattern calibration (2026-10-28; Wes: "Isak is fully fit, he played the last two games - is the low
P(appear) a classic-ML issue?"). The minutes/appearance heads are current-season rolling features, so an injury blank
three games ago still sits in the 3/5/8-week windows after two full games back. This measures, on the stored
walk-forward classic forecasts (SFT corpora, top-256 per week), what players with exactly that pattern actually did:
  isak      : last two fixture-weeks >= 70 min, the one before = 0 min with a pre-deadline injury/doubt flag, unflagged now
  benchblank: same, but the 0-minute week was unflagged (status 'a'): a benching, not an injury
  anyblank  : same, any 0-minute week three back
  nailed    : last three fixture-weeks all >= 70 min (control)
Forecast minutes / P(appear) / points vs realised minutes / appeared / points, with 2 s.e.
usage: returner_pattern_calibration.py <out.md>"""
from __future__ import annotations

import ast
import json
import sys

import numpy as np
import pandas as pd

ROOT = "/home/wescheng/projects/fpl/fpl"
_ns = {"ROOT": ROOT}
for node in ast.parse(open(f"{ROOT}/scripts/minutes_prior_study.py").read()).body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") in ("FILES", "SEASONS"):
        _ns[node.targets[0].id] = eval(compile(ast.Expression(node.value), "<x>", "eval"), _ns)
FILES, SEASONS = _ns["FILES"], _ns["SEASONS"]


def se2(x):
    x = np.asarray(x, dtype=float)
    return 2 * x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else float("nan")


def main() -> None:
    out = sys.argv[1]
    t = pd.read_csv(f"{ROOT}/data/fpl_training_rows_v3_contract_f6.csv", low_memory=False,
                    usecols=["season", "week", "player_id", "code", "player_name", "position", "price_pre_deadline", "fixture_count",
                             "observed_minutes", "observed_starts", "observed_points", "status_pre_deadline", "status_flag_pre_deadline"])
    t = t[t["season"].isin(SEASONS)].copy()
    t["sidx"] = t["season"].map({s: i for i, s in enumerate(SEASONS)})
    t["code"] = t.groupby(["season", "player_id"])["code"].transform(lambda s: s.ffill().bfill())
    t = t[t["code"].notna()].copy(); t["code"] = t["code"].astype(int)
    f = t[t["fixture_count"] > 0].sort_values(["code", "sidx", "week"]).copy()
    g = f.groupby(["code", "sidx"])
    for k in (1, 2, 3):
        f[f"m{k}"] = g["observed_minutes"].shift(k)
    f["flag3"] = g["status_flag_pre_deadline"].shift(3)
    f["st3"] = g["status_pre_deadline"].shift(3)
    f["gap"] = f["week"] - g["week"].shift(3)
    f["flag_now"] = f["status_flag_pre_deadline"].fillna(0)
    base = (f["m1"] >= 70) & (f["m2"] >= 70) & (f["m3"].notna()) & (f["flag_now"] == 0) & (f["gap"] <= 4)
    slices = {
        "isak (injury blank 3 back, two 70+ games since)": base & (f["m3"] == 0) & (f["flag3"] == 1),
        "benchblank (unflagged 0-min week 3 back)": base & (f["m3"] == 0) & (f["flag3"] == 0) & (f["st3"] == "a"),
        "anyblank (0-min week 3 back)": base & (f["m3"] == 0),
        "nailed (three 70+ games)": base & (f["m3"] >= 70),
    }
    fc = {}
    for path in FILES:
        for line in open(path):
            r = json.loads(line); m = r["metadata"]; b = m["baseline_forecast"]
            fc[(m["season"], int(r["week"]), int(m["player_id"]))] = (float(b["baseline_minutes_1gw"]), float(b["baseline_appearance_probability"]), float(b["baseline_points_1gw"]))
    f["key"] = list(zip(f["season"], f["week"], f["player_id"]))
    f["b_min"] = f["key"].map(lambda k: fc.get(k, (np.nan,) * 3)[0])
    f["b_app"] = f["key"].map(lambda k: fc.get(k, (np.nan,) * 3)[1])
    f["b_pts"] = f["key"].map(lambda k: fc.get(k, (np.nan,) * 3)[2])
    f["appeared"] = (f["observed_minutes"] > 0).astype(float)
    lines = ["# Returner-pattern calibration (walk-forward classic forecasts, top-256 per week)", "",
             f"Table rows with a fixture {len(f):,}; forecasts available for {f['b_min'].notna().sum():,}. Seasons {SEASONS[0]} → {SEASONS[-1]} GW8.", "",
             "## All rows with the pattern (realised only)", "",
             "| slice | n | realised min | appeared | started | points |", "|---|---|---|---|---|---|"]
    for name, mask in slices.items():
        d = f[mask]
        lines.append(f"| {name} | {len(d):,} | {d.observed_minutes.mean():.1f} ± {se2(d.observed_minutes):.1f} | {d.appeared.mean():.3f} | {d.observed_starts.mean():.3f} | {d.observed_points.mean():.2f} |")
    lines += ["", "## Rows with a stored forecast: forecast vs realised", "",
              "| slice | n | fc min → real | fc P(app) → appeared | fc pts → real pts | Δ pts (real − fc) |", "|---|---|---|---|---|---|"]
    rows = {}
    for name, mask in slices.items():
        d = f[mask & f["b_min"].notna()]
        rows[name] = d
        lines.append(f"| {name} | {len(d):,} | {d.b_min.mean():.1f} → {d.observed_minutes.mean():.1f} ± {se2(d.observed_minutes):.1f} | "
                     f"{d.b_app.mean():.3f} → {d.appeared.mean():.3f} | {d.b_pts.mean():.2f} → {d.observed_points.mean():.2f} | "
                     f"{(d.observed_points - d.b_pts).mean():+.2f} ± {se2(d.observed_points - d.b_pts):.2f} |")
    lines += ["", "## The Isak slice by cut", "", "| cut | n | fc min → real | fc P → appeared | fc pts → real | Δ pts |", "|---|---|---|---|---|---|"]
    d0 = rows["isak (injury blank 3 back, two 70+ games since)"]
    cuts = {"FWD": d0[d0.position == "FWD"], "MID": d0[d0.position == "MID"], "DEF+GK": d0[d0.position.isin(["DEF", "GK"])],
            "price ≥ 8.0": d0[d0.price_pre_deadline >= 8.0], "price < 8.0": d0[d0.price_pre_deadline < 8.0],
            "2019-22": d0[d0.sidx <= 2], "2022-25": d0[d0.sidx.between(3, 5)], "2025-27": d0[d0.sidx >= 6],
            "fc min < 70": d0[d0.b_min < 70], "fc min ≥ 70": d0[d0.b_min >= 70]}
    for name, d in cuts.items():
        if len(d) < 5:
            lines.append(f"| {name} | {len(d)} | | | | |"); continue
        lines.append(f"| {name} | {len(d):,} | {d.b_min.mean():.1f} → {d.observed_minutes.mean():.1f} ± {se2(d.observed_minutes):.1f} | "
                     f"{d.b_app.mean():.3f} → {d.appeared.mean():.3f} | {d.b_pts.mean():.2f} → {d.observed_points.mean():.2f} | {(d.observed_points - d.b_pts).mean():+.2f} ± {se2(d.observed_points - d.b_pts):.2f} |")
    # the same players one game later (4th game back) and the nailed control at the same forecast-minutes band
    nailed = rows["nailed (three 70+ games)"]
    lo, hi = d0.b_min.quantile(0.1), d0.b_min.quantile(0.9)
    nb = nailed[nailed.b_min.between(lo, hi)]
    lines += ["", f"Nailed control restricted to the Isak slice's forecast-minutes band ({lo:.0f}-{hi:.0f}): n {len(nb):,}, "
              f"fc min {nb.b_min.mean():.1f} → real {nb.observed_minutes.mean():.1f}, fc pts {nb.b_pts.mean():.2f} → {nb.observed_points.mean():.2f} ({(nb.observed_points - nb.b_pts).mean():+.2f} ± {se2(nb.observed_points - nb.b_pts):.2f}).", ""]
    ex = d0[d0.sidx >= 6].sort_values(["season", "week"])[["season", "week", "player_name", "position", "b_min", "observed_minutes", "b_pts", "observed_points"]]
    lines += ["## 2025-27 examples of the Isak slice", "", "| season | GW | player | pos | fc min | real min | fc pts | real pts |", "|---|---|---|---|---|---|---|---|"]
    lines += [f"| {r.season} | {r.week} | {r.player_name} | {r.position} | {r.b_min:.0f} | {r.observed_minutes:.0f} | {r.b_pts:.2f} | {r.observed_points:.0f} |" for r in ex.itertuples()]
    open(out, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
