#!/usr/bin/env python3
"""F13: injury-history features for the classic model (Wes, 2026-10-11: "Saka is not a great idea because he
could be injured and could not perform as well as his price tag").

Computed per player strictly from earlier gameweeks (a row's label_minutes_1gw is that week's outcome, so only
previous rows are read), counting only weeks his team had a fixture:
  inj_absences_38       games missed in his last 38 team games, if he normally starts when available
                        (mean minutes when playing >= 60); 0 otherwise
  inj_long_layoff_prev  1 if last season he missed 5+ team games in a row and played at least 10
  inj_absences_x_price  inj_absences_38 x price (does it matter more for premiums?)
reports/review_fixes_2026_10/injury_pattern.md measured the residual these target: about -0.1 pts/GW for
absence-prone regulars, -0.28 (not significant) for premiums with a long lay-off.

usage: add_injury_history_features.py <in.csv> <out.csv>
"""
import sys

import numpy as np
import pandas as pd

SEASON_ORDER = {s: i for i, s in enumerate(["2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22",
                                             "2022-23", "2023-24", "2024-25", "2025-26", "2026-27"])}


def main() -> None:
    src, dst = sys.argv[1], sys.argv[2]
    t = pd.read_csv(src, low_memory=False)
    t["_order"] = t["season"].map(SEASON_ORDER) * 100 + t["week"]
    # 2026-10-27: player_id is the per-season element id and is re-used by a different player the next season;
    # cross-season history must key on the stable `code` (filled within season where a row lacks it).
    t["_code"] = t.groupby(["season", "player_id"])["code"].transform(lambda s: s.ffill().bfill()).fillna(-1).astype(int)
    t = t.sort_values(["_code", "_order"]).reset_index(drop=True)
    absences = np.zeros(len(t)); layoff = np.zeros(len(t))
    for pid, idx in t.groupby("_code").indices.items():
        g = t.loc[idx]
        mins = pd.to_numeric(g["label_minutes_1gw"], errors="coerce").fillna(0.0).to_numpy()
        team_played = (pd.to_numeric(g["fixture_count"], errors="coerce").fillna(0) > 0).to_numpy()
        seasons = g["season"].to_numpy()
        history = []  # (season, minutes) for earlier weeks with a team fixture
        for j, row_idx in enumerate(idx):
            last = [m for _, m in history[-38:]]
            played = [m for m in last if m > 0]
            if played and np.mean(played) >= 60:
                absences[row_idx] = sum(1 for m in last if m == 0)
            prev = [m for s, m in history if SEASON_ORDER.get(s, -9) == SEASON_ORDER.get(seasons[j], -9) - 1]
            if prev:
                streak = best = 0
                for m in prev:
                    streak = streak + 1 if m == 0 else 0
                    best = max(best, streak)
                layoff[row_idx] = float(best >= 5 and sum(1 for m in prev if m > 0) >= 10)
            if team_played[j]:
                history.append((seasons[j], mins[j]))
    t["inj_absences_38"] = absences
    t["inj_long_layoff_prev"] = layoff
    t["inj_absences_x_price"] = absences * pd.to_numeric(t["price_pre_deadline"], errors="coerce").fillna(0.0)
    t = t.drop(columns=["_order", "_code"]).sort_values(["season", "week", "player_id"]).reset_index(drop=True)
    t.to_csv(dst, index=False)
    nz = t["inj_absences_38"] > 0
    print(f"wrote {dst}: {len(t)} rows; absences>0 on {nz.mean():.0%}, long lay-off flag on {t['inj_long_layoff_prev'].mean():.0%}")


if __name__ == "__main__":
    main()
