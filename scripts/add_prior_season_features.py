#!/usr/bin/env python3
"""F17: prior-season availability features (Wes, 2026-10-27, Calafiori: "rates him fairly high but the minutes he plays
are fairly low ... follows the pattern he has in the last season ... starting fresh from the new season").

The minutes/appearance heads are current-season-only by design (F2b blends QUALITY only, Wes 2026-09-01), so a
player's multi-season start record is invisible once he has an 8-week run of starts. reports/gw9_packet_2026_10/
minutes_prior_study.md measured the residual this leaves on 16,546 nailed-looking player-weeks: prior-season start
share itself is NOT predictive beyond the forecast (excess +0.03 ± 0.09 pts), but players with NO prior Premier
League season are over-forecast (excess -0.23 ± 0.09; defenders -0.35 ± 0.14; weeks 1-10 -0.38 ± 0.20).

Computed per stable player `code` (NOT player_id, which is the per-season element id and is re-used by another player
the next season) from the previous season's rows only, so nothing from the row's own season leaks:
  prior_pl_games         team games (fixture_count > 0 rows) the player was on the books for last season, capped at 38
  no_prior_pl_season     1 if he has no rows for the previous season (new signing from abroad, promoted club's
                         squad, academy graduate, or the table's first season)
  prior_start_share      starts / team games last season (0 when no prior season)
  prior_minutes_share    minutes / (90 x team games) last season (0 when no prior season)
  prior_unknown          1 for the table's first season (2019-20), where "no prior rows" means nothing; the other four
                         are 0 there so the ridge can separate "unknown" from "new to the league"

usage: add_prior_season_features.py <in.csv> <out.csv>
"""
import sys

import numpy as np
import pandas as pd

SEASONS = ["2016-17", "2017-18", "2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26", "2026-27"]


def main() -> None:
    src, dst = sys.argv[1], sys.argv[2]
    t = pd.read_csv(src, low_memory=False)
    sidx = t["season"].map({s: i for i, s in enumerate(SEASONS)})
    code = t.groupby(["season", "player_id"])["code"].transform(lambda s: s.ffill().bfill())
    played = t.loc[pd.to_numeric(t["fixture_count"], errors="coerce").fillna(0) > 0].assign(_code=code, _sidx=sidx)
    played = played[played["_code"].notna()]
    agg = played.groupby(["_code", "_sidx"]).agg(games=("week", "size"), starts=("observed_starts", "sum"),
                                                  minutes=("observed_minutes", "sum"))
    games = {k: float(v) for k, v in agg["games"].to_dict().items()}
    starts = {k: float(v) for k, v in agg["starts"].to_dict().items()}
    minutes = {k: float(v) for k, v in agg["minutes"].to_dict().items()}
    keys = list(zip(code, sidx - 1))
    first = sidx == sidx.min()
    g = np.array([games.get(k, 0.0) if pd.notna(k[0]) else 0.0 for k in keys])
    st = np.array([starts.get(k, 0.0) for k in keys]); mi = np.array([minutes.get(k, 0.0) for k in keys])
    feats = pd.DataFrame({
        "prior_pl_games": np.where(first, 0.0, np.minimum(g, 38.0)),
        "no_prior_pl_season": np.where(first, 0.0, (g == 0).astype(float)),
        "prior_start_share": np.where(first | (g == 0), 0.0, st / np.maximum(g, 1.0)),
        "prior_minutes_share": np.where(first | (g == 0), 0.0, mi / (90.0 * np.maximum(g, 1.0))),
        "prior_unknown": first.astype(float).to_numpy(),
    }, index=t.index)
    t = pd.concat([t.drop(columns=[c for c in feats.columns if c in t.columns]), feats], axis=1)
    t.to_csv(dst, index=False)
    by_season = t.groupby("season")["no_prior_pl_season"].mean().round(2).to_dict()
    print(f"wrote {dst}: {len(t)} rows; no_prior_pl_season share by season {by_season}")


if __name__ == "__main__":
    main()
