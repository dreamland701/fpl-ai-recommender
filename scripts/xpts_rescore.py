#!/usr/bin/env python
"""Re-score decision-backtest directories on expected points (xPts) next to realised points (2026-10-17, item 6).

Reads each window's rolling_squad_backtest.json, replays the week scoring exactly as backtest.py does (realised starters
after autosubs, effective captain, bench boost = all 15, triple captain = captain twice, minus hit cost) with two
per-player-week point tables: the realised points (validated against the file's actual_score) and xPts from
data/xpts_table.csv (scripts/build_xpts_table.py).

usage:
  xpts_rescore.py --baseline reports/status_backfill/bt/ST1_F --test reports/status_backfill/bt/STN_F \
                  --test reports/transfer_calibration/bt/HT2_F ... [--label status] [--out reports/xpts]
A prefix P matches window dirs P_<season>_<a>_<b> (xargs benches) or P/<season>_<a>_<b> (H-series benches).
Writes <out>/<label>_windows.csv (per window per config: actual, xpts) and appends to <out>/summary.md.
"""
import argparse, glob, json, re
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
WIN = re.compile(r"(\d{4}-\d{2})_(\d+)_(\d+)$")


def window_dirs(prefix: str):
    out = {}
    for d in glob.glob(prefix + "_*") + glob.glob(prefix + "/*"):
        if not Path(d, "rolling_squad_backtest.json").is_file():
            continue
        m = WIN.search(Path(d).name)
        if m:
            out[m.group(0)] = d
    return out


def score_file(path: str, table: dict):
    d = json.load(open(path))
    rows = []
    for w in d["weeks"]:
        key = (w["season"], int(w["week"]))
        squad_ids = [p["player_id"] for p in w["squad"]]
        hit = sum(float(t.get("hit_cost", 0.0)) for t in w.get("transfers_applied", []))
        chip = w.get("chip_used", "none")
        base_ids = squad_ids if chip == "bench_boost" else list(w["realized_starters"])
        cap = w["effective_captain_id"]
        file_actual = {p["player_id"]: float(p.get("actual_points_1gw", 0.0)) for p in w["squad"]}

        def total(getter):
            s = sum(getter(pid) for pid in base_ids) + getter(cap) - hit
            if chip == "triple_captain":
                s += getter(cap)
            return s

        actual = total(lambda pid: file_actual.get(pid, 0.0))
        miss = sum(1 for pid in base_ids if (key[0], key[1], pid) not in table)
        xp = total(lambda pid: table.get((key[0], key[1], pid), (file_actual.get(pid, 0.0), file_actual.get(pid, 0.0)))[1])
        tab_actual = total(lambda pid: table.get((key[0], key[1], pid), (file_actual.get(pid, 0.0), 0.0, 0.0))[0])
        xs = total(lambda pid: table.get((key[0], key[1], pid), (file_actual.get(pid, 0.0), file_actual.get(pid, 0.0), file_actual.get(pid, 0.0)))[2])
        rows.append({"season": w["season"], "week": int(w["week"]), "chip": chip, "hit": hit, "file_actual": float(w["actual_score"]),
                     "actual": actual, "table_actual": tab_actual, "xpts": xp, "xpts_skill": xs, "missing": miss})
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", default=str(ROOT / "data/xpts_table.csv"))
    ap.add_argument("--baseline", required=True)
    ap.add_argument("--test", action="append", default=[])
    ap.add_argument("--label", default="bench")
    ap.add_argument("--out", default=str(ROOT / "reports/xpts"))
    a = ap.parse_args()
    t = pd.read_csv(a.table)
    has_skill = "xpts_skill" in t.columns
    table = {(r.season, int(r.week), int(r.player_id)): (float(r.actual_points), float(r.xpts), float(r.xpts_skill) if has_skill else float(r.xpts)) for r in t.itertuples()}
    cfgs = {"BASE:" + Path(a.baseline).name: window_dirs(a.baseline)}
    for p in a.test:
        cfgs[Path(p).name] = window_dirs(p)
    base_name = next(iter(cfgs))
    base_windows = set(cfgs[base_name])
    recs = []
    for cfg, wins in cfgs.items():
        for wkey, d in wins.items():
            if wkey not in base_windows:
                continue
            rows = score_file(str(Path(d, "rolling_squad_backtest.json")), table)
            for r in rows:
                r.update({"config": cfg, "window": wkey}); recs.append(r)
    weekly = pd.DataFrame(recs)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    weekly.to_csv(out / f"{a.label}_weeks.csv", index=False)
    bad = (weekly.file_actual - weekly.actual).abs() > 0.01
    tab_bad = (weekly.table_actual - weekly.actual).abs() > 0.01
    win = weekly.groupby(["config", "window"], as_index=False).agg(actual=("actual", "sum"), xpts=("xpts", "sum"), xpts_skill=("xpts_skill", "sum"), weeks=("week", "size"), missing=("missing", "sum"))
    win.to_csv(out / f"{a.label}_windows.csv", index=False)
    base = win[win.config == base_name].set_index("window")
    lines = [f"\n## {a.label}: baseline {base_name[5:]} ({len(base)} windows; replay mismatches {int(bad.sum())}/{len(weekly)} weeks, "
             f"table-vs-file actual mismatches {int(tab_bad.sum())}, missing player-weeks {int(weekly.missing.sum())})\n",
             "| config | windows | actual total | xPts total | luck (actual−xPts) | Δactual vs base | sd/window | t | Δxpts vs base | sd/window | t | corr(Δactual, Δxpts) | Δxpts+skill | t |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    pooled_a, pooled_x = [], []
    for cfg, g in win.groupby("config", sort=False):
        g = g.set_index("window")
        luck = g.actual.sum() - g.xpts.sum()
        if cfg == base_name:
            lines.append(f"| {cfg[5:]} (base) | {len(g)} | {g.actual.sum():.0f} | {g.xpts.sum():.0f} | {luck:+.0f} | | | | | | | | | |")
            continue
        common = [w for w in g.index if w in base.index]
        da = (g.loc[common, "actual"] - base.loc[common, "actual"]).to_numpy(); dx = (g.loc[common, "xpts"] - base.loc[common, "xpts"]).to_numpy()
        n = len(common)
        sa = da.std(ddof=1) if n > 1 else float("nan"); sx = dx.std(ddof=1) if n > 1 else float("nan")
        ta = da.sum() / (sa * np.sqrt(n)) if n > 1 and sa > 0 else float("nan"); tx = dx.sum() / (sx * np.sqrt(n)) if n > 1 and sx > 0 else float("nan")
        corr = np.corrcoef(da, dx)[0, 1] if n > 2 else float("nan")
        pooled_a.extend(da.tolist()); pooled_x.extend(dx.tolist())
        ds_ = (g.loc[common, "xpts_skill"] - base.loc[common, "xpts_skill"]).to_numpy()
        ss = ds_.std(ddof=1) if n > 1 else float("nan"); ts = ds_.sum() / (ss * np.sqrt(n)) if n > 1 and ss > 0 else float("nan")
        lines.append(f"| {cfg} | {n} | {g.loc[common, 'actual'].sum():.0f} | {g.loc[common, 'xpts'].sum():.0f} | {luck:+.0f} | {da.sum():+.0f} | {sa:.1f} | {ta:+.2f} | {dx.sum():+.0f} | {sx:.1f} | {tx:+.2f} | {corr:.2f} | {ds_.sum():+.0f} | {ts:+.2f} |")
    if pooled_a:
        pa, px = np.array(pooled_a), np.array(pooled_x)
        lines.append(f"\nPooled per-window config-minus-base diffs over {len(pa)} window pairs: sd actual {pa.std(ddof=1):.1f}, sd xPts {px.std(ddof=1):.1f} "
                     f"(ratio {px.std(ddof=1) / pa.std(ddof=1):.2f}), corr {np.corrcoef(pa, px)[0, 1]:.2f}; mean |diff| actual {np.abs(pa).mean():.1f} xPts {np.abs(px).mean():.1f}.")
    with open(out / "summary.md", "a") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
