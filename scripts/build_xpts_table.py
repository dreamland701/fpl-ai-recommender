#!/usr/bin/env python
"""Build data/xpts_table.csv: per (season, week, player_id) the realised FPL points and the expected points (xPts).

xPts (2026-10-17, programme item 6) replaces the four luck-dominated scoring components with their expectation from the
FPL match stats and keeps everything else as realised (appearance, bonus, saves, cards, own goals, penalties, DefCon):

    xpts = total_points
           - [ G*goal(pos) + A*3 + CS*cs(pos) - floor(GC/2)*[GK/DEF] ]                 (realised)
           + [ xG*goal(pos) + xA*3 + P(CS)*cs(pos) - E[floor(GC/2)]*[GK/DEF] ]          (expected)

    P(CS) = exp(-xGC) when the player played >= 60 minutes in that fixture, else 0; E[floor(GC/2)] under Poisson(xGC)
    for players with minutes > 0. Computed per fixture (data/fpl_history/<season>/merged_gw.csv), summed per gameweek.

usage: build_xpts_table.py [--seasons 2022-23 2023-24 ...] [--out data/xpts_table.csv]
"""
import argparse, math
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
GOAL = {"GK": 6, "GKP": 6, "DEF": 6, "MID": 5, "FWD": 4}
CS = {"GK": 4, "GKP": 4, "DEF": 4, "MID": 1, "FWD": 0}


def expected_floor_half(lam: np.ndarray, kmax: int = 20) -> np.ndarray:
    """E[floor(K/2)] for K ~ Poisson(lam)."""
    lam = np.clip(np.asarray(lam, dtype=float), 0.0, None)
    out = np.zeros_like(lam)
    for k in range(2, kmax + 1):
        out += (k // 2) * np.exp(-lam) * lam ** k / math.factorial(k)
    return out


def load_season(season: str) -> pd.DataFrame:
    f = ROOT / "data/fpl_history" / season / "merged_gw.csv"
    df = pd.read_csv(f, low_memory=False)
    gw_col = next(c for c in ("GW", "round", "event") if c in df.columns)
    id_col = next(c for c in ("element", "player_id", "id") if c in df.columns)
    if "position" not in df.columns and "position_id" in df.columns:  # live-season files carry position_id
        df["position"] = pd.to_numeric(df["position_id"], errors="coerce").map({1: "GK", 2: "DEF", 3: "MID", 4: "FWD"})
    pos = df["position"].astype(str).str.upper().str.strip().replace({"GKP": "GK"})
    need = ["minutes", "total_points", "goals_scored", "assists", "clean_sheets", "goals_conceded",
            "expected_goals", "expected_assists", "expected_goals_conceded"]
    for c in need:
        df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0)
    m = df["minutes"].to_numpy(float)
    g = pos.map(GOAL).fillna(0).to_numpy(float); cs = pos.map(CS).fillna(0).to_numpy(float)
    gkdef = pos.isin(["GK", "DEF"]).to_numpy()
    played = m > 0
    realised = (df["goals_scored"] * g + df["assists"] * 3 + df["clean_sheets"] * cs
                - np.floor(df["goals_conceded"] / 2) * gkdef)
    xgc = df["expected_goals_conceded"].to_numpy(float)
    p_cs = np.where(m >= 60, np.exp(-xgc), 0.0)
    expected = (df["expected_goals"] * g + df["expected_assists"] * 3 + p_cs * cs
                - expected_floor_half(xgc) * gkdef * played)
    out = pd.DataFrame({
        "season": season, "week": df[gw_col].astype(int), "player_id": df[id_col].astype(int), "position": pos,
        "fixtures": 1, "minutes": m, "actual_points": df["total_points"].astype(float),
        "xpts": (df["total_points"] - realised + expected).astype(float),
        "x_goal_pts": df["expected_goals"] * g, "x_assist_pts": df["expected_assists"] * 3.0,
        "x_cs_pts": p_cs * cs, "x_gc_pts": -expected_floor_half(xgc) * gkdef * played,
        "r_goal_pts": df["goals_scored"] * g, "r_assist_pts": df["assists"] * 3.0, "r_cs_pts": df["clean_sheets"] * cs,
        "r_gc_pts": -np.floor(df["goals_conceded"] / 2) * gkdef,
    })
    agg = {c: "sum" for c in out.columns if c not in ("season", "week", "player_id", "position")}
    agg["position"] = "first"
    return out.groupby(["season", "week", "player_id"], as_index=False).agg(agg)


def calibrate_components(table: pd.DataFrame) -> pd.DataFrame:
    """League-level calibration of the expected components, per season and position (2026-10-17 finding):
    FPL assists run 1.3-2.1x the xA-based expectation (penalties won, rebounds, own-goal assists are assists but
    not xA) and clean sheets realise at only 0.7-0.8x exp(-xGC); goals and goals-conceded are ~1.0. Each expected
    component is scaled by the season-position ratio of realised to expected points so the metric is unbiased by
    component. The ratio is league-wide, so it favours no configuration; it only removes a common bias."""
    table = table.copy()
    for comp in ("goal", "assist", "cs", "gc"):
        r, x = f"r_{comp}_pts", f"x_{comp}_pts"
        tot = table.groupby(["season", "position"])[[r, x]].sum()
        ratio = (tot[r] / tot[x].where(tot[x].abs() > 1e-9)).fillna(1.0).clip(0.25, 4.0)
        table[f"cal_{comp}"] = ratio.reindex(pd.MultiIndex.from_frame(table[["season", "position"]])).to_numpy()
        table[x] = table[x] * table[f"cal_{comp}"]
    table["xpts"] = (table.actual_points - (table.r_goal_pts + table.r_assist_pts + table.r_cs_pts + table.r_gc_pts)
                     + (table.x_goal_pts + table.x_assist_pts + table.x_cs_pts + table.x_gc_pts))
    return table


def add_finishing_skill(table: pd.DataFrame, shrink_games: float = 30.0, window_seasons: int = 3) -> pd.DataFrame:
    """xpts_skill = xpts + a shrunken, walk-forward estimate of the player's own finishing/assisting over-performance.

    skill_rate (points per 90) = sum over PRIOR player-weeks (this season to date + the previous `window_seasons - 1`
    seasons) of (realised - expected goal and assist points) / (prior 90s + shrink_games). Team-level components
    (clean sheets, goals conceded) are never adjusted. Players are keyed by the persistent FPL `code` from
    players_raw.csv (falls back to the season element id when unmapped).
    """
    codes = {}
    for season in sorted(table.season.unique()):
        f = ROOT / "data/fpl_history" / season / "players_raw.csv"
        if f.is_file():
            pr = pd.read_csv(f, usecols=lambda c: c in ("id", "code"))
            codes.update({(season, int(i)): int(c) for i, c in zip(pr["id"], pr["code"])})
    table = table.copy()
    table["code"] = [codes.get((s, int(p)), -int(p)) for s, p in zip(table.season, table.player_id)]
    table["over"] = (table.r_goal_pts - table.x_goal_pts) + (table.r_assist_pts - table.x_assist_pts)
    table["g90"] = table.minutes / 90.0
    seasons = sorted(table.season.unique()); sidx = {s: i for i, s in enumerate(seasons)}
    table["sidx"] = table.season.map(sidx)
    table = table.sort_values(["code", "sidx", "week"]).reset_index(drop=True)
    g = table.groupby("code", sort=False)
    excl_over = g["over"].cumsum() - table["over"]; excl_g90 = g["g90"].cumsum() - table["g90"]
    season_tot = table.groupby(["code", "sidx"], as_index=False)[["over", "g90"]].sum().sort_values(["code", "sidx"])
    season_tot["cum_over"] = season_tot.groupby("code")["over"].cumsum(); season_tot["cum_g90"] = season_tot.groupby("code")["g90"].cumsum()
    older = {(c, i): (o, m) for c, i, o, m in zip(season_tot.code, season_tot.sidx, season_tot.cum_over, season_tot.cum_g90)}
    # subtract everything older than the window: cumulative totals through season (sidx - window_seasons)
    drop = [older.get((c, i - window_seasons), (0.0, 0.0)) for c, i in zip(table.code, table.sidx)]
    drop_over = np.array([d[0] for d in drop]); drop_g90 = np.array([d[1] for d in drop])
    # seasons older than the window but with the cumulative key missing (gaps) are handled by the nearest older key
    prior_over = excl_over.to_numpy() - drop_over; prior_g90 = excl_g90.to_numpy() - drop_g90
    table["skill_rate"] = prior_over / (prior_g90 + shrink_games)
    table["xpts_skill"] = table.xpts + table.skill_rate * table.g90
    return table.drop(columns=["over", "g90", "sidx"]).sort_values(["season", "week", "player_id"]).reset_index(drop=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seasons", nargs="*", default=["2022-23", "2023-24", "2024-25", "2025-26", "2026-27"])
    ap.add_argument("--out", default=str(ROOT / "data/xpts_table.csv"))
    ap.add_argument("--skill-shrink", type=float, default=30.0, help="shrinkage in 90-minute games for the finishing-skill rate")
    a = ap.parse_args()
    frames = []
    for s in a.seasons:
        try:
            t = load_season(s)
        except Exception as e:  # noqa: BLE001
            print(f"{s}: skipped ({e})"); continue
        print(f"{s}: {len(t)} player-weeks, weeks {t.week.min()}-{t.week.max()}, mean actual {t.actual_points.mean():.3f} "
              f"xpts {t.xpts.mean():.3f}, corr {np.corrcoef(t.actual_points, t.xpts)[0, 1]:.3f}, "
              f"sd actual {t.actual_points.std():.3f} xpts {t.xpts.std():.3f}")
        frames.append(t)
    table = pd.concat(frames, ignore_index=True)
    table = calibrate_components(table)
    table = add_finishing_skill(table, shrink_games=a.skill_shrink)
    top = table[table.season == table.season.max()].groupby("code").agg(skill=("skill_rate", "last"), mins=("minutes", "sum")).query("mins > 900").sort_values("skill")
    print("skill_rate (pts/90) extremes in the latest season:", top.tail(5).skill.round(2).to_dict(), top.head(3).skill.round(2).to_dict())
    print(f"xpts_skill vs actual: corr {np.corrcoef(table.actual_points, table.xpts_skill)[0, 1]:.3f}, mean {table.xpts_skill.mean():.3f} (xpts {table.xpts.mean():.3f}, actual {table.actual_points.mean():.3f})")
    table.to_csv(a.out, index=False)
    print(f"wrote {a.out}: {len(table)} rows")


if __name__ == "__main__":
    main()
