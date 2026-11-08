#!/usr/bin/env python3
"""NOTE (2026-10-27): the table's player_id is the per-season element id and is RE-USED by a different player the next
season (841 of 866 ids map to 2+ codes); cross-season history must key on `code`. scripts/add_injury_history_features.py
(F13) and reports/review_fixes_2026_10/injury_pattern.py keyed on player_id, so their prior-season terms were wrong.

Does the classic minutes model over-rate players who LOOK nailed now but have a rotation/injury history?
(Wes, 2026-10-27, Calafiori: 7 straight starts, forecast 90 min / P(app) 1.0 / 5.5 pts for GW8, then benched;
last season 22 starts of 38, the season before 11 of 38.)

The minutes/appearance heads are current-season-only by design (F2b blends QUALITY only, Wes 2026-09-01), so a
player's multi-season start share is invisible to them once he has an 8-week run of starts. This study measures the
residual that leaves, on the walk-forward classic forecasts stored in the SFT corpora (top-256 per week,
2022-23 .. 2026-27 GW5), bucketed by the player's PRIOR-season start share. Second question (Wes: "starting fresh
from the new season"): after the F2b ramp (6 played weeks), do players whose current-season PPG runs ahead of
their prior-season PPG regress more than the forecast expects?

usage: minutes_prior_study.py <out.md>
"""
import json
import sys
from collections import defaultdict

import numpy as np
import pandas as pd

ROOT = "/home/wescheng/projects/fpl/fpl"
FILES = [f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/train.jsonl",
         f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_thru_2526_26_eval_2526_27_38/eval.jsonl",
         f"{ROOT}/reports/llm_residual_v2_e20_contract_top256_eval_2627_2_5/eval.jsonl"]
SEASONS = ["2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27"]


def se(x):
    x = np.asarray(x, dtype=float)
    return 2 * x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else float("nan")


def main() -> None:
    out = sys.argv[1]
    t = pd.read_csv(f"{ROOT}/data/fpl_training_rows_v3_contract_f6.csv", low_memory=False,
                    usecols=["season", "week", "player_id", "code", "player_name", "position", "price_pre_deadline", "fixture_count",
                             "observed_points", "observed_minutes", "observed_starts", "minutes_avg_3", "starts_avg_3",
                             "appearance_rate_3", "status_flag_pre_deadline"])
    t = t[t["season"].isin(SEASONS)].copy()
    t["sidx"] = t["season"].map({s: i for i, s in enumerate(SEASONS)})
    # player_id is the per-season FPL element id (re-used by a DIFFERENT player next season); code is the stable id.
    # Some rows carry code NaN: fill within (season, player_id).
    t["code"] = t.groupby(["season", "player_id"])["code"].transform(lambda s: s.ffill().bfill())
    t = t[t["code"].notna()].copy(); t["code"] = t["code"].astype(int)
    # per (player, season): team games (weeks with a fixture), starts, minutes, points
    played = t[t["fixture_count"] > 0]
    agg = played.groupby(["code", "sidx"]).agg(games=("week", "size"), starts=("observed_starts", "sum"),
                                                     minutes=("observed_minutes", "sum"), points=("observed_points", "sum"))
    season_stats = {k: v for k, v in agg.to_dict("index").items()}
    # current-season running totals strictly before the row's week
    t = t.sort_values(["code", "sidx", "week"])
    g = t.groupby(["code", "sidx"])
    had = (t["fixture_count"] > 0).astype(float)
    t["cur_games"] = g[["fixture_count"]].transform(lambda s: (s > 0).astype(float).cumsum().shift(1).fillna(0))["fixture_count"]
    t["cur_starts"] = g["observed_starts"].transform(lambda s: s.cumsum().shift(1).fillna(0))
    t["cur_apps"] = g["observed_minutes"].transform(lambda s: (s > 0).astype(float).cumsum().shift(1).fillna(0))
    t["cur_points"] = g["observed_points"].transform(lambda s: s.cumsum().shift(1).fillna(0))
    rowinfo = t.set_index(["season", "week", "player_id"])

    recs = []
    for path in FILES:
        for line in open(path):
            r = json.loads(line); m = r["metadata"]
            pid, season, week = int(m["player_id"]), m["season"], int(r["week"])
            try:
                row = rowinfo.loc[(season, week, pid)]
            except KeyError:
                continue
            if isinstance(row, pd.DataFrame):
                row = row.iloc[0]
            sidx = SEASONS.index(season)
            code = int(row["code"])
            prev = season_stats.get((code, sidx - 1)); prev2 = season_stats.get((code, sidx - 2))
            b = m["baseline_forecast"]; lab = m["labels"]
            recs.append({
                "season": season, "week": week, "pid": pid, "name": m["player_name"], "pos": row["position"],
                "price": float(row["price_pre_deadline"] or 0),
                "b_min": float(b["baseline_minutes_1gw"]), "b_app": float(b["baseline_appearance_probability"]),
                "b_pts": float(b["baseline_points_1gw"]), "min": float(lab["minutes_1gw"]), "pts": float(lab["points_1gw"]),
                "fixtures": int(row["fixture_count"] or 0),
                "min3": float(row["minutes_avg_3"] or 0), "starts3": float(row["starts_avg_3"] or 0),
                "flag": float(row["status_flag_pre_deadline"] or 0),
                "prev_games": prev["games"] if prev else np.nan,
                "prev_share": (prev["starts"] / prev["games"]) if prev and prev["games"] >= 10 else np.nan,
                "prev_min_share": (prev["minutes"] / (90 * prev["games"])) if prev and prev["games"] >= 10 else np.nan,
                "prev_ppg": (prev["points"] / prev["games"]) if prev and prev["games"] >= 10 else np.nan,
                "prev2_share": (prev2["starts"] / prev2["games"]) if prev2 and prev2["games"] >= 10 else np.nan,
                "cur_games": float(row["cur_games"]), "cur_starts": float(row["cur_starts"]), "cur_apps": float(row["cur_apps"]),
                "cur_ppg": (float(row["cur_points"]) / float(row["cur_games"])) if row["cur_games"] >= 1 else np.nan,
            })
    d = pd.DataFrame(recs)
    d = d[d["fixtures"] == 1]  # single-fixture weeks only: minutes residuals are per 90
    d["res_min"] = d["min"] - d["b_min"]; d["res_pts"] = d["pts"] - d["b_pts"]
    d["played"] = (d["min"] > 0).astype(float); d["started"] = (d["min"] >= 60).astype(float)
    d["bin"] = (d["b_pts"] * 2).round() / 2
    ctrl = d.groupby(["season", "bin"])["res_pts"].mean()
    d["excess"] = d["res_pts"] - np.array([ctrl.get((s_, b_), np.nan) for s_, b_ in zip(d["season"], d["bin"])])
    mctrl = d.groupby(["season", "bin"])["res_min"].mean()
    d["excess_min"] = d["res_min"] - np.array([mctrl.get((s_, b_), np.nan) for s_, b_ in zip(d["season"], d["bin"])])
    lines = [f"# Minutes-prior study (rotation history vs a current run of starts)\n",
             f"{len(d)} single-fixture player-weeks with walk-forward classic forecasts (top-256 per week, 2022-23 to 2026-27 GW5).",
             "Residual = actual minus the classic forecast. Excess = residual minus the mean residual of all rows in the same",
             "(season, 0.5-point forecast bin), i.e. the surprise beyond what players at the same forecast delivered. ± is 2 standard errors.\n"]

    def table(sub, title, key, bins, labels):
        lines.append(f"## {title}\n")
        lines.append(f"| {key} | n | forecast min | actual min | residual min | excess min | P(played) fc / act | P(60+) | forecast pts | actual pts | residual pts | excess pts |")
        lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
        for lo, hi, lab in zip(bins[:-1], bins[1:], labels):
            s = sub[(sub[key] >= lo) & (sub[key] < hi)]
            if len(s) < 20:
                continue
            lines.append(f"| {lab} | {len(s)} | {s.b_min.mean():.1f} | {s['min'].mean():.1f} | {s.res_min.mean():+.1f} (± {se(s.res_min):.1f}) | "
                         f"{s.excess_min.mean():+.1f} (± {se(s.excess_min.dropna()):.1f}) | "
                         f"{s.b_app.mean():.2f} / {s.played.mean():.2f} | {s.started.mean():.2f} | {s.b_pts.mean():.2f} | {s.pts.mean():.2f} | "
                         f"{s.res_pts.mean():+.2f} (± {se(s.res_pts):.2f}) | {s.excess.mean():+.2f} (± {se(s.excess.dropna()):.2f}) |")
        s = sub[sub[key].isna()]
        if len(s) >= 30:
            lines.append(f"| no prior season | {len(s)} | {s.b_min.mean():.1f} | {s['min'].mean():.1f} | {s.res_min.mean():+.1f} (± {se(s.res_min):.1f}) | "
                         f"{s.excess_min.mean():+.1f} (± {se(s.excess_min.dropna()):.1f}) | "
                         f"{s.b_app.mean():.2f} / {s.played.mean():.2f} | {s.started.mean():.2f} | {s.b_pts.mean():.2f} | {s.pts.mean():.2f} | "
                         f"{s.res_pts.mean():+.2f} (± {se(s.res_pts):.2f}) | {s.excess.mean():+.2f} (± {se(s.excess.dropna()):.2f}) |")
        lines.append("")

    nailed = d[(d.min3 >= 75) & (d.starts3 >= 0.99) & (d.flag == 0)]
    bins = [0, 0.4, 0.6, 0.8, 1.01]; labels = ["< 40%", "40-60%", "60-80%", "80%+"]
    table(nailed, f"A. Looks nailed now (3-week minutes >= 75, started all 3, no flag; n {len(nailed)}), by PRIOR-season start share",
          "prev_share", bins, labels)
    table(nailed[nailed.pos == "DEF"], "A2. Same, defenders only", "prev_share", bins, labels)
    table(nailed[nailed.week <= 10], "A3. Same, weeks 1-10 of the season only", "prev_share", bins, labels)
    table(nailed[nailed.week >= 11], "A4. Same, weeks 11+ only", "prev_share", bins, labels)
    two = nailed[(nailed.prev_share < 0.6) & (nailed.prev2_share < 0.6)]
    lines.append(f"**Calafiori profile** (nailed now, prior TWO seasons both under 60% starts): n {len(two)}, forecast {two.b_min.mean():.1f} min / "
                 f"{two.b_pts.mean():.2f} pts, actual {two['min'].mean():.1f} min / {two.pts.mean():.2f} pts, residual {two.res_min.mean():+.1f} min "
                 f"(± {se(two.res_min):.1f}) / {two.res_pts.mean():+.2f} pts (± {se(two.res_pts):.2f}), excess {two.excess.mean():+.2f} pts (± {se(two.excess.dropna()):.2f}); P(played) {two.played.mean():.2f}, P(60+) {two.started.mean():.2f}.\n"
                 if len(two) else "")
    # everyone (not just nailed), to see whether the effect is specific to the nailed-looking rows
    table(d[d.flag == 0], "B. All unflagged rows, by prior-season start share", "prev_share", bins, labels)
    # fresh-season question
    fresh = d[(d.week >= 7) & (d.week <= 14) & (d.cur_apps >= 5) & d.prev_ppg.notna()]
    fresh = fresh.assign(gap=fresh.cur_ppg - fresh.prev_ppg)
    table(fresh, f"C. Weeks 7-14 after the prior blend has faded, by (current-season PPG minus prior-season PPG) (n {len(fresh)})",
          "gap", [-99, -1.0, 0.0, 1.0, 2.0, 99], ["below -1", "-1 to 0", "0 to +1", "+1 to +2", "above +2"])
    table(fresh[fresh.pos == "DEF"], "C2. Same, defenders only", "gap", [-99, -1.0, 0.0, 1.0, 2.0, 99],
          ["below -1", "-1 to 0", "0 to +1", "+1 to +2", "above +2"])
    # correlation check: does prev_share add anything to b_min for the nailed rows? partial via OLS
    s = nailed.dropna(subset=["prev_share"])
    if len(s) > 100:
        X = np.column_stack([np.ones(len(s)), s.b_min, s.prev_share, s.price])
        beta = np.linalg.lstsq(X, s["min"], rcond=None)[0]
        resid = s["min"] - X @ beta
        cov = np.linalg.inv(X.T @ X) * (resid @ resid) / (len(s) - X.shape[1])
        lines.append(f"**OLS on nailed rows:** actual minutes = {beta[0]:.1f} + {beta[1]:.3f} x forecast + {beta[2]:.1f} x prior start share "
                     f"(± {2*np.sqrt(cov[2,2]):.1f}) + {beta[3]:.2f} x price; n {len(s)}.\n")
        X = np.column_stack([np.ones(len(s)), s.b_pts, s.prev_share, s.price])
        beta = np.linalg.lstsq(X, s["pts"], rcond=None)[0]
        resid = s["pts"] - X @ beta
        cov = np.linalg.inv(X.T @ X) * (resid @ resid) / (len(s) - X.shape[1])
        lines.append(f"**OLS on nailed rows (points):** actual = {beta[0]:.2f} + {beta[1]:.3f} x forecast + {beta[2]:.2f} x prior start share "
                     f"(± {2*np.sqrt(cov[2,2]):.2f}) + {beta[3]:.3f} x price.\n")
    cal = d[(d.name.str.contains("Calafiori"))].sort_values(["season", "week"])
    if len(cal):
        lines.append("## Calafiori rows in the corpus\n")
        lines.append("| season | week | forecast min | actual | forecast pts | actual | prior share |")
        lines.append("|---|---|---|---|---|---|---|")
        for r in cal.itertuples():
            lines.append(f"| {r.season} | {r.week} | {r.b_min:.0f} | {r.min:.0f} | {r.b_pts:.2f} | {r.pts:.0f} | {r.prev_share if pd.notna(r.prev_share) else float('nan'):.2f} |")
    open(out, "w").write("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
