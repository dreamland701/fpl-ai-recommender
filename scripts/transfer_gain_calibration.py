"""Transfer-gain calibration: projected vs realised gains for the transfers the backtests considered and took.

For every candidate transfer in a bench config's windows (reports/dgw_fix/bt/<CONFIG>_<season>_<a>_<b>), the
engine's projected_gain (3GW squad-score gain net of the hit), the forecast difference in-minus-out over 1/3/5 GWs,
and the realised difference from the training table labels. Reports the calibration slope (realised on projected),
bins, hit-vs-free, applied-vs-not, and the realised value of the hits actually taken.
usage: transfer_gain_calibration.py <table.csv> <config> [<config> ...]  -> reports/transfer_calibration/<config>.csv + summary.md
"""
import glob
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path("reports/transfer_calibration"); OUT.mkdir(parents=True, exist_ok=True)


def load_labels(table):
    t = pd.read_csv(table, usecols=["season", "week", "player_id", "label_points_1gw", "label_points_3gw", "label_points_5gw", "label_minutes_1gw"], low_memory=False)
    return t.set_index(["season", "week", "player_id"])


def rows_for(config, labels):
    out = []
    pattern = f"{config}_*/rolling_squad_backtest.json" if "/" in config else f"reports/dgw_fix/bt/{config}_*/rolling_squad_backtest.json"
    for f in sorted(glob.glob(pattern)):
        d = json.load(open(f)); window = Path(f).parent.name
        for w in d["weeks"]:
            applied = {(tuple(sorted(t["players_out"])), tuple(sorted(t["players_in"]))) for t in w["transfers_applied"]}
            for rank, c in enumerate(w["candidate_transfers"]):
                key = (tuple(sorted(c["players_out"])), tuple(sorted(c["players_in"])))
                rec = {"window": window, "season": w["season"], "week": w["week"], "rank": rank, "n_transfers": len(c["players_in"]),
                       "projected_gain": c["projected_gain"], "hit_cost": c["hit_cost"], "applied": key in applied}
                ok = True
                for h in ("1gw", "3gw", "5gw"):
                    pred = real = 0.0
                    for sign, group in ((1, c["incoming_players"]), (-1, c["outgoing_players"])):
                        for p in group:
                            pred += sign * float(p[f"predicted_points_{h}"])
                            try:
                                real += sign * float(labels.loc[(w["season"], int(w["week"]), int(p["player_id"])), f"label_points_{h}"])
                            except KeyError:
                                ok = False
                    rec[f"pred_d{h}"] = pred; rec[f"real_d{h}"] = real
                rec["labels_ok"] = ok
                out.append(rec)
    return pd.DataFrame(out)


def slope(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 5 or x.std() == 0:
        return float("nan"), float("nan")
    b = np.cov(x, y, bias=True)[0, 1] / x.var(); a = y.mean() - b * x.mean()
    resid = y - (a + b * x); se = np.sqrt(resid.var(ddof=2) / (len(x) * x.var())) if len(x) > 2 else float("nan")
    return b, se


def main():
    table = sys.argv[1]; configs = sys.argv[2:]
    labels = load_labels(table)
    lines = ["# Transfer-gain calibration (projected vs realised)", "",
             "Candidates = every transfer the engine listed with a positive projected gain (top 5 per week, 3GW squad-score horizon, net of hits);",
             "applied = the one it took. Realised = label points in minus out over the same horizon (lineup effects ignored).", ""]
    for cfg in configs:
        df = rows_for(cfg, labels); df = df[df.labels_ok]
        df.to_csv(OUT / f"{Path(cfg).name}.csv", index=False)
        lines += [f"## {Path(cfg).name}: {len(df)} candidates in {df.window.nunique()} windows, {int(df.applied.sum())} applied, {int((df.applied & (df.hit_cost > 0)).sum())} hits taken", ""]
        for h in ("1gw", "3gw", "5gw"):
            b, se = slope(df[f"pred_d{h}"], df[f"real_d{h}"])
            lines.append(f"- {h}: forecast difference in−out mean {df[f'pred_d{h}'].mean():+.2f}, realised {df[f'real_d{h}'].mean():+.2f}; "
                         f"slope realised-on-forecast {b:.2f} ± {se:.2f}")
        b, se = slope(df["projected_gain"], df["real_d3gw"])
        lines.append(f"- engine projected_gain vs realised 3GW difference: slope {b:.2f} ± {se:.2f}; corr {np.corrcoef(df.projected_gain, df.real_d3gw)[0, 1]:.2f}")
        lines += ["", "| projected gain bin | n | applied | mean projected | forecast Δ3 | realised Δ3 | realised Δ1 | realised Δ5 |", "|---|---|---|---|---|---|---|---|"]
        bins = [-99, 1, 2, 3, 5, 8, 99]
        df["bin"] = pd.cut(df.projected_gain, bins)
        for b_, g in df.groupby("bin", observed=True):
            lines.append(f"| {b_} | {len(g)} | {int(g.applied.sum())} | {g.projected_gain.mean():+.2f} | {g.pred_d3gw.mean():+.2f} | {g.real_d3gw.mean():+.2f} | {g.real_d1gw.mean():+.2f} | {g.real_d5gw.mean():+.2f} |")
        lines += ["", "| subset | n | mean projected | forecast Δ3 | realised Δ3 | realised Δ3 − hit |", "|---|---|---|---|---|---|"]
        for name, g in (("applied, free", df[df.applied & (df.hit_cost == 0)]), ("applied, hit", df[df.applied & (df.hit_cost > 0)]),
                        ("not applied, free", df[~df.applied & (df.hit_cost == 0)]), ("not applied, hit", df[~df.applied & (df.hit_cost > 0)]),
                        ("rank 0 (best option)", df[df["rank"] == 0]), ("2-transfer options", df[df.n_transfers == 2])):
            if len(g):
                lines.append(f"| {name} | {len(g)} | {g.projected_gain.mean():+.2f} | {g.pred_d3gw.mean():+.2f} | {g.real_d3gw.mean():+.2f} ± {g.real_d3gw.std() / np.sqrt(len(g)):.2f} | {(g.real_d3gw - g.hit_cost).mean():+.2f} |")
        lines.append("")
    (OUT / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
