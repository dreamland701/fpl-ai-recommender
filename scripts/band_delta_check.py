#!/usr/bin/env python3
"""Mechanism check for the numeric-history block (H6, 2026-10-28): by band of the classic per-fixture minutes forecast,
the classic residual (realised - forecast) in points and minutes, and each adapter's mean delta. An adapter that has
learned the band structure tracks the residual (positive at 45-72 min, negative at 86+); H1/H5 were flat (-0.1 to -0.3
pts, ~0 min in every band). Also the "Isak pattern" rows (injury blank 3 games back, two 70+ games since, unflagged)
and corr(delta, residual) by band. usage: band_delta_check.py --examples a.jsonl [--examples b.jsonl] --pred name=path [...] --out md"""
from __future__ import annotations

import argparse
import json

import numpy as np
import pandas as pd

SE = lambda x: 2 * np.std(x, ddof=1) / np.sqrt(len(x)) if len(x) > 1 else float("nan")  # noqa: E731
BANDS = [(0, 45), (45, 60), (60, 72), (72, 80), (80, 86), (86, 91)]


def load_ex(paths):
    out = {}
    for p in paths:
        for l in open(p):
            r = json.loads(l); m = r["metadata"]; out[(m["season"], int(r["week"]), int(m["player_id"]))] = m
    return out


def load_pred(path):
    out = {}
    for l in open(path):
        r = json.loads(l); m = r["metadata"]
        try:
            out[(m["season"], int(r["week"]), int(m["player_id"]))] = json.loads(r["response"])
        except (ValueError, KeyError):
            continue
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--examples", action="append", required=True); ap.add_argument("--pred", action="append", required=True)
    ap.add_argument("--table", default="data/fpl_training_rows_v3_contract_f6.csv"); ap.add_argument("--out", required=True)
    args = ap.parse_args()
    ex = load_ex(args.examples); preds = {kv.split("=")[0]: load_pred(kv.split("=", 1)[1]) for kv in args.pred}
    seasons = sorted({k[0] for k in ex})
    t = pd.read_csv(args.table, low_memory=False, usecols=["season", "week", "player_id", "code", "fixture_count", "observed_minutes", "status_flag_pre_deadline"])
    t = t[t.season.isin(seasons)].copy(); t["code"] = t.groupby(["season", "player_id"])["code"].transform(lambda s: s.ffill().bfill()); t = t[t.code.notna()]
    f = t[t.fixture_count > 0].sort_values(["code", "season", "week"]).copy(); g = f.groupby(["code", "season"])
    for k in (1, 2, 3):
        f[f"m{k}"] = g["observed_minutes"].shift(k)
    f["flag3"] = g["status_flag_pre_deadline"].shift(3); f["gap"] = f.week - g["week"].shift(3)
    pat = f[(f.m1 >= 70) & (f.m2 >= 70) & (f.m3 == 0) & (f.flag3 == 1) & (f.gap <= 4) & (f.status_flag_pre_deadline.fillna(0) == 0)]
    patkeys = set(zip(pat.season, pat.week, pat.player_id))
    rows = []
    for k, m in ex.items():
        b = m["baseline_forecast"]; lab = m["labels"]
        rec = {"bmin": b["baseline_minutes_1gw"], "bpts": b["baseline_points_1gw"], "min": lab["minutes_1gw"], "pts": lab["points_1gw"], "isak": k in patkeys}
        for n, p in preds.items():
            rec[f"{n}_d1"] = p.get(k, {}).get("delta_points_1gw", np.nan); rec[f"{n}_dm"] = p.get(k, {}).get("delta_minutes_1gw", np.nan)
        rows.append(rec)
    d = pd.DataFrame(rows); d["res"] = d.pts - d.bpts; d["resm"] = d["min"] - d.bmin
    names = list(preds)
    lines = [f"# Band delta check ({', '.join(args.examples)}; {len(d)} rows; Isak-pattern rows {int(d.isak.sum())})", "",
             "| band (fc min) | n | classic Δpts (real−fc) | " + " | ".join(f"{n} Δpts" for n in names) + " | classic Δmin | " + " | ".join(f"{n} Δmin" for n in names) + " |",
             "|---|---|---|" + "---|" * (2 * len(names) + 1)]
    def row(label, x):
        return (f"| {label} | {len(x)} | {x.res.mean():+.2f} ± {SE(x.res):.2f} | " + " | ".join(f"{x[f'{n}_d1'].mean():+.2f}" for n in names)
                + f" | {x.resm.mean():+.1f} | " + " | ".join(f"{x[f'{n}_dm'].mean():+.1f}" for n in names) + " |")
    for lo, hi in BANDS:
        x = d[d.bmin.between(lo, hi - 0.001)]
        if len(x) >= 10:
            lines.append(row(f"{lo}-{hi}", x))
    if d.isak.sum() >= 3:
        lines.append(row("Isak pattern", d[d.isak]))
    lines += ["", "corr(adapter Δpts, classic residual) / corr(adapter Δmin, classic minutes residual):"]
    for n in names:
        lines.append(f"- {n}: pts {d[[f'{n}_d1', 'res']].corr().iloc[0, 1]:+.3f}, minutes {d[[f'{n}_dm', 'resm']].corr().iloc[0, 1]:+.3f}; "
                     f"sd of Δpts {d[f'{n}_d1'].std():.3f}, sd of Δmin {d[f'{n}_dm'].std():.2f}")
    open(args.out, "w").write("\n".join(lines) + "\n"); print("\n".join(lines))


if __name__ == "__main__":
    main()
