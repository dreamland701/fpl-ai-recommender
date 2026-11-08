#!/usr/bin/env python3
"""F19 team-level baselines (2026-10-31, Wes: "should the classic model capture up-and-coming teams such as Villa and
Spurs? If not, that is an argument for SFT/RL").

The ridge sees team form only through lagged 3/5-week goals for/against (own team and opponent), with no longer baseline,
so a mid-table club on a hot run and a champion in ordinary form look alike. reports/team_trajectory_study/README.md
measured what that leaves on the stored walk-forward forecasts: a 5-game streak carries only +0.09 ±0.11 GD/game into the
next match once the club's prior-season level is known (the level carries +0.55); players of clubs running BELOW their
level are under-forecast (+0.13 to +0.27 pts/week, i.e. the model follows streaks that revert); the residual regression
puts −0.09 ±0.08 pts/week per GD/game on the own club's prior-season level and −0.12 ±0.08 on the opponent's. These
columns hand the ridge the longer baselines so it can weigh the short windows against them. Walk-forward safe: prior-
season values use the previous season's rows only; season-to-date values use earlier weeks of the same season only.

Columns (tl_ prefix, used only with FPL_TEAM_LEVEL_FEATS=1, see dataset.get_feature_columns):
  tl_team_prior_gd   club's prior-season goal difference per game (promoted clubs get the fixed constant -1.0)
  tl_opp_prior_gd    the same for the week's primary opponent (0 in blank weeks)
  tl_team_std_gd     club's season-to-date GD per game before this week (the prior value until a game is played)
  tl_opp_std_gd      the same for the opponent
  tl_team_promoted   1 when the club has no prior-season rows in a season whose club codes are known
  tl_opp_promoted    the same for the opponent
  tl_unknown         1 for seasons without a club-code map (data/fpl_history/<season>/teams.csv missing): every other
                     tl_ column is 0 there, so the ridge can separate "unknown" from a real zero

Club identity across seasons = the FPL team `code` (season-local team_ids are re-used); 2026-27's teams.csv has no code
column and is mapped by club name. Per-fixture DGW rows keep the primary opponent's values for both fixtures.
usage: add_team_level_features.py <in.csv> <out.csv>
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROMOTED_PRIOR_GD = -1.0
NEW = ["tl_team_prior_gd", "tl_opp_prior_gd", "tl_team_std_gd", "tl_opp_std_gd", "tl_team_promoted", "tl_opp_promoted", "tl_unknown"]


def club_codes() -> dict:
    """(season, team_id) -> club code; seasons without a teams.csv are absent (-> tl_unknown)."""
    frames, name_to_code, out = {}, {}, {}
    for d in sorted((ROOT / "data/fpl_history").iterdir()):
        p = d / "teams.csv"
        if p.exists() and p.stat().st_size > 0:
            try:
                frames[d.name] = pd.read_csv(p)
            except Exception:  # noqa: BLE001
                pass
    for tm in frames.values():
        if {"code", "name"} <= set(tm.columns):
            for r in tm.itertuples(index=False):
                name_to_code[str(r.name)] = int(r.code)
    for season, tm in frames.items():
        if "id" not in tm.columns:
            continue
        for r in tm.itertuples(index=False):
            code = int(r.code) if "code" in tm.columns and pd.notna(getattr(r, "code", np.nan)) else name_to_code.get(str(getattr(r, "name", "")))
            if code is not None:
                out[(season, int(r.id))] = code
    return out


def prev_season(season: str) -> str:
    y = int(season[:4])
    return f"{y - 1}-{str(y)[2:]}"


def main() -> None:
    src, dst = sys.argv[1], sys.argv[2]
    t = pd.read_csv(src, low_memory=False)
    for c in NEW:
        if c in t.columns:
            t = t.drop(columns=[c])
    codes = club_codes()
    known_seasons = {s for s, _ in codes}
    tw = (t.groupby(["season", "team_id", "week"], as_index=False)
            .agg(gf=("goals_for", "first"), ga=("goals_against", "first"), nfix=("fixture_count", "first")))
    tw["nfix"] = pd.to_numeric(tw["nfix"], errors="coerce").fillna(0)
    tw = tw[tw["gf"].notna() & tw["ga"].notna() & (tw["nfix"] > 0)].copy()
    tw["code"] = [codes.get((s, int(x))) for s, x in zip(tw["season"], tw["team_id"])]
    tw["gd"] = tw["gf"].astype(float) - tw["ga"].astype(float)
    tw = tw.sort_values(["season", "team_id", "week"])
    g = tw.groupby(["season", "team_id"], sort=False)
    tw["cum_gd"] = g["gd"].cumsum() - tw["gd"]
    tw["cum_n"] = g["nfix"].cumsum() - tw["nfix"]
    season_tot = tw[tw["code"].notna()].groupby(["season", "code"]).agg(gd=("gd", "sum"), n=("nfix", "sum"))
    season_gd_pg = {k: float(v.gd / v.n) for k, v in season_tot.iterrows() if v.n > 0}
    # prior-season level per (season, team_id)
    prior, promoted = {}, {}
    for (season, tid), code in {(s, int(x)): c for s, x, c in zip(tw["season"], tw["team_id"], tw["code"])}.items():
        if season not in known_seasons or code is None:
            continue
        ps = prev_season(season)
        if ps not in known_seasons:
            continue  # the previous season's clubs are unknown: cannot tell promoted from unmapped
        val = season_gd_pg.get((ps, code))
        prior[(season, tid)] = val
        promoted[(season, tid)] = val is None
    # prior for promoted clubs: a FIXED constant, not estimated from the table (an estimate would use the promoted
    # clubs' own realised seasons, including the current one). Promoted clubs' first-season GD/game has averaged about
    # -1.0 over 2016-2026 (the 2023-26 cohorts here: -1.0), so -1.0 it is; the tl_*_promoted flag lets the ridge adjust.
    promoted_fill = PROMOTED_PRIOR_GD
    print(f"club codes for seasons {sorted(known_seasons)}; prior-season levels for {len(prior):,} club-seasons, "
          f"{sum(promoted.values())} promoted; promoted fill = {promoted_fill:+.3f} GD/game")
    tw["prior_gd"] = [prior.get((s, int(x)), np.nan) for s, x in zip(tw["season"], tw["team_id"])]
    is_prom = np.array([bool(promoted.get((s, int(x)), False)) for s, x in zip(tw["season"], tw["team_id"])])
    tw["prior_gd"] = np.where(tw["prior_gd"].isna().to_numpy() & is_prom, promoted_fill, tw["prior_gd"])
    tw["std_gd"] = np.where(tw["cum_n"] > 0, tw["cum_gd"] / tw["cum_n"].replace(0, np.nan), tw["prior_gd"])
    tw["is_promoted"] = [float(bool(promoted.get((s, int(x)), False))) for s, x in zip(tw["season"], tw["team_id"])]
    team_level = {(s, int(x), int(w)): (p, sd, pr) for s, x, w, p, sd, pr in
                  zip(tw["season"], tw["team_id"], tw["week"], tw["prior_gd"], tw["std_gd"], tw["is_promoted"])}
    # a club's level is also needed in its blank weeks (no team-week row): carry the latest known value
    latest = {}
    for (s, x, w), v in sorted(team_level.items()):
        latest[(s, x)] = v
    has_prior = {(s, x) for (s, x) in prior}

    def team_vals(season, tid, week):
        v = team_level.get((season, tid, week))
        if v is None:
            # blank week: use the most recent earlier team-week of the same club
            cands = [(w, val) for (s, x, w), val in team_level.items() if s == season and x == tid and w < week]
            v = max(cands)[1] if cands else (prior.get((season, tid), np.nan), prior.get((season, tid), np.nan), float(bool(promoted.get((season, tid), False))))
        return v

    seasons = t["season"].astype(str).to_numpy()
    tids = pd.to_numeric(t["team_id"], errors="coerce").to_numpy()
    weeks = pd.to_numeric(t["week"], errors="coerce").to_numpy()
    opps = pd.to_numeric(t["primary_opponent_team_id"], errors="coerce").to_numpy()
    cols = {c: np.zeros(len(t)) for c in NEW}
    cache = {}
    for i in range(len(t)):
        s, tid, w = seasons[i], tids[i], weeks[i]
        if s not in known_seasons or prev_season(s) not in known_seasons or np.isnan(tid) or np.isnan(w):
            cols["tl_unknown"][i] = 1.0
            continue
        key = (s, int(tid), int(w))
        if key not in cache:
            cache[key] = team_vals(s, int(tid), int(w))
        p, sd, pr = cache[key]
        cols["tl_team_prior_gd"][i] = 0.0 if pd.isna(p) else p
        cols["tl_team_std_gd"][i] = 0.0 if pd.isna(sd) else sd
        cols["tl_team_promoted"][i] = pr
        if not np.isnan(opps[i]):
            okey = (s, int(opps[i]), int(w))
            if okey not in cache:
                cache[okey] = team_vals(s, int(opps[i]), int(w))
            op, osd, opr = cache[okey]
            cols["tl_opp_prior_gd"][i] = 0.0 if pd.isna(op) else op
            cols["tl_opp_std_gd"][i] = 0.0 if pd.isna(osd) else osd
            cols["tl_opp_promoted"][i] = opr
    t = pd.concat([t, pd.DataFrame(cols, index=t.index)], axis=1)
    t.to_csv(dst, index=False)
    known = t[t["tl_unknown"] == 0]
    print(f"wrote {dst}: {len(t):,} rows; unknown-season rows {int(t['tl_unknown'].sum()):,}; "
          f"known rows {len(known):,}: team prior gd mean {known['tl_team_prior_gd'].mean():+.3f} sd {known['tl_team_prior_gd'].std():.3f}, "
          f"std gd sd {known['tl_team_std_gd'].std():.3f}, promoted share {known['tl_team_promoted'].mean():.3f}, "
          f"opp prior sd {known['tl_opp_prior_gd'].std():.3f}")
    chk = known[(known["season"] == "2026-27") & (known["week"] == 8)].groupby("team_id")[["tl_team_prior_gd", "tl_team_std_gd", "tl_team_promoted"]].first()
    print("2026-27 GW8 sample (team_id: prior, season-to-date, promoted):")
    print(chk.round(3).to_string())


if __name__ == "__main__":
    main()
