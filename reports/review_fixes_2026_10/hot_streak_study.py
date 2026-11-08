"""Do hot players cool off, beyond what the classic forecast already expects?

Population: regular starters (3-week minutes average >= 60) in every gameweek of
2022-23..2025-26, with the walk-forward classic forecast the SFT corpus used.
"Hot" is fixed in advance from pre-deadline form only:
  hot       last-3 points average >= 7 and at least 2.5 above the last-8 average
  very hot  last-3 points average >= 9
Reports (a) cooling against the streak and (b) the residual against the classic
forecast relative to non-hot regulars with the same forecast (0.5-point bins),
per season. (b) is what an adjustment could profit from.
"""
import json
import sys
from collections import defaultdict

import numpy as np
import pandas as pd

ROOT = "/home/wescheng/projects/fpl/fpl"


def main() -> None:
    rows = []
    for line in open(f"{ROOT}/reports/llm_player_forecast_2022_26_e20_base.jsonl"):
        r = json.loads(line); m = r["metadata"]
        rows.append((m["season"], int(m["week"]), int(m["player_id"]), m["position"],
                     float(m["baseline_forecast"]["baseline_points_1gw"]), float(m["labels"]["points_1gw"])))
    corpus = pd.DataFrame(rows, columns=["season", "week", "player_id", "pos", "classic", "actual"])
    table = pd.read_csv(f"{ROOT}/data/fpl_training_rows_v3_contract_f6.csv", low_memory=False,
                        usecols=["season", "week", "player_id", "points_avg_3", "points_avg_8", "minutes_avg_3", "fixture_count"])
    df = corpus.merge(table, on=["season", "week", "player_id"], how="inner")
    df = df.loc[(df["minutes_avg_3"] >= 60) & (df["fixture_count"] == 1)].copy()
    df["resid"] = df["actual"] - df["classic"]
    df["hot"] = (df["points_avg_3"] >= 7) & (df["points_avg_3"] - df["points_avg_8"] >= 2.5)
    df["very_hot"] = df["points_avg_3"] >= 9
    df["bin"] = (df["classic"] * 2).round() / 2
    controls = df.loc[~df["hot"] & ~df["very_hot"]].groupby(["season", "bin"])["resid"].mean()
    df["expected_resid"] = [controls.get((s, b), np.nan) for s, b in zip(df["season"], df["bin"])]
    df["excess"] = df["resid"] - df["expected_resid"]
    print(f"regular-starter player-weeks: {len(df)} (2022-23..2025-26)")
    for flag in ("hot", "very_hot"):
        sub = df.loc[df[flag] & df["excess"].notna()]
        se = sub["excess"].std() / np.sqrt(len(sub))
        print(f"\n{flag}: n {len(sub)} player-weeks")
        print(f"  streak (last-3 avg) {sub['points_avg_3'].mean():.2f} -> classic forecast {sub['classic'].mean():.2f} "
              f"-> actual next week {sub['actual'].mean():.2f}")
        print(f"  vs classic, beyond similar-forecast regulars: {sub['excess'].mean():+.2f} points (se {se:.2f}, t {sub['excess'].mean() / se:+.2f})")
        for season, g in sub.groupby("season"):
            s = g["excess"].std() / np.sqrt(len(g))
            print(f"    {season}: {g['excess'].mean():+.2f} (se {s:.2f}, n {len(g)})")


if __name__ == "__main__":
    main()
