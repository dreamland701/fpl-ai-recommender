"""Does the classic model miss "injury-prone" or "just back from injury" players? (Wes, 2026-10-11:
"maybe Saka is not a great idea because he could be injured and could not perform as well as his
price tag")

From each player's week-by-week minutes (training table, all seasons, strictly before the week being
forecast) three things a manager pattern-matches on:
  - just back: games played since returning from an absence of 2+ gameweeks (1st, 2nd, 3rd game back)
  - absence-prone: gameweeks missed in the previous 38 by a player who normally starts
  - long injury last season: a run of 5+ missed gameweeks in the previous season
For the walk-forward classic forecasts in the SFT corpora (2022-23 to 2026-27 GW5), the real
surprise (actual - classic) of those players is compared with players at the same classic forecast
(0.5-point bins, same season) who show none of the patterns. Premiums (price >= 8) separately: the
"price tag" part.

usage: injury_pattern.py <out.md>
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


def main() -> None:
    t = pd.read_csv(f"{ROOT}/data/fpl_training_rows_v3_contract_f6.csv", low_memory=False,
                    usecols=["season", "week", "player_id", "code", "label_minutes_1gw", "fixture_count", "price_pre_deadline"])
    t = t[t["season"].isin(SEASONS)].copy()
    # 2026-10-27: player_id is the per-season element id (re-used by another player next season); key on code.
    t["code"] = t.groupby(["season", "player_id"])["code"].transform(lambda s: s.ffill().bfill())
    t = t[t["code"].notna()].copy(); t["code"] = t["code"].astype(int)
    code_of = {(r.season, int(r.week), int(r.player_id)): int(r.code) for r in t[["season", "week", "player_id", "code"]].itertuples(index=False)}
    price_of = {(r.season, int(r.week), int(r.player_id)): r.price_pre_deadline for r in t[["season", "week", "player_id", "price_pre_deadline"]].itertuples(index=False)}
    t["order"] = t["season"].map({s: i for i, s in enumerate(SEASONS)}) * 100 + t["week"]
    hist = defaultdict(list)  # pid -> [(order, season, week, minutes, had_fixture)]
    for r in t.sort_values("order").itertuples(index=False):
        hist[int(r.code)].append((int(r.order), r.season, int(r.week), float(r.label_minutes_1gw or 0), int(r.fixture_count or 0) > 0))

    def patterns(pid, season, week):
        rows = [h for h in hist.get(pid, []) if h[0] < SEASONS.index(season) * 100 + week and h[4]]  # weeks his team played
        mins = [h[3] for h in rows]
        out = {"back": 0, "absences38": 0, "long_last_season": False}
        if len(mins) < 6:
            return out
        # just back: count games played at the end since a 2+ gameweek absence (within the last 10 team games)
        played_run = 0
        i = len(mins) - 1
        while i >= 0 and mins[i] > 0:
            played_run += 1; i -= 1
        gap = 0
        while i >= 0 and mins[i] == 0:
            gap += 1; i -= 1
        if gap >= 2 and 1 <= played_run <= 3 and i >= 0:
            out["back"] = played_run
        # absence-prone: missed games in the last 38 team games, only for players who usually start when available
        last = mins[-38:]
        played = [m for m in last if m > 0]
        if played and np.mean(played) >= 60:
            out["absences38"] = sum(1 for m in last if m == 0)
        # long injury last season: 5+ consecutive missed team games in the previous season
        prev = SEASONS[SEASONS.index(season) - 1] if SEASONS.index(season) > 0 else None
        streak = best = 0
        for h in rows:
            if h[1] == prev:
                streak = streak + 1 if h[3] == 0 else 0
                best = max(best, streak)
        prev_played = [h[3] for h in rows if h[1] == prev and h[3] > 0]
        out["long_last_season"] = best >= 5 and len(prev_played) >= 10  # a regular who had a long lay-off
        return out

    recs = []
    for path in FILES:
        for line in open(path):
            r = json.loads(line); m = r["metadata"]
            pid, season, week = int(m["player_id"]), m["season"], int(r["week"])
            code = code_of.get((season, week, pid))
            if code is None:
                continue
            p = patterns(code, season, week)
            base = float(m["baseline_forecast"]["baseline_points_1gw"])
            price = pd.Series([price_of.get((season, week, pid))])
            recs.append({"season": season, "base": base, "actual": float(m["labels"]["points_1gw"]),
                         "minutes": float(m["labels"]["minutes_1gw"]), "price": float(price.iloc[0]) if len(price) else 0.0,
                         "papp": float(m["baseline_forecast"]["baseline_appearance_probability"]), **p})
    df = pd.DataFrame(recs)
    df["resid"] = df["actual"] - df["base"]
    df["bin"] = (df["base"] * 2).round() / 2
    clean = (df["back"] == 0) & (df["absences38"] <= 2) & (~df["long_last_season"])
    ctrl = df[clean].groupby(["season", "bin"])["resid"].mean()
    df["excess"] = df["resid"] - [ctrl.get((s, b), np.nan) for s, b in zip(df["season"], df["bin"])]
    lines = ["# Does classic miss injury-prone or just-back players?", "",
             f"{len(df)} player-weeks with walk-forward classic forecasts (2022-23 to 2026-27 GW5).", "",
             "| Pattern | Player-weeks | Classic forecast | Played | Real surprise vs similar-forecast players (pts) |", "|---|---|---|---|---|"]
    groups = [("1st game back from a 2+ GW absence", df["back"] == 1), ("2nd game back", df["back"] == 2), ("3rd game back", df["back"] == 3),
              ("Missed 6-9 of last 38 (a regular)", df["absences38"].between(6, 9)), ("Missed 10+ of last 38 (a regular)", df["absences38"] >= 10),
              ("Long lay-off last season (5+ GWs)", df["long_last_season"]),
              ("Premium (8.0+) just back (1st-3rd game)", (df["back"] > 0) & (df["price"] >= 8.0)),
              ("Premium (8.0+) with a long lay-off last season", df["long_last_season"] & (df["price"] >= 8.0)),
              ("Premium (8.0+), none of the patterns", clean & (df["price"] >= 8.0))]
    for name, sel in groups:
        g = df[sel & df["excess"].notna()]
        if len(g) < 25:
            lines.append(f"| {name} | {len(g)} | – | – | too few |"); continue
        se = g["excess"].std() / np.sqrt(len(g))
        lines.append(f"| {name} | {len(g)} | {g['base'].mean():.2f} | {(g['minutes'] > 0).mean():.0%} | {g['excess'].mean():+.2f} (± {1.96 * se:.2f}) |")
    out = "\n".join(lines) + "\n"
    open(sys.argv[1], "w").write(out)
    print(out)


if __name__ == "__main__":
    main()
