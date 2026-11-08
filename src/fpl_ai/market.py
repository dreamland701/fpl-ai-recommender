"""Bookmaker market features (F14, 2026-10-14).

The closing betting market is the strongest public forecast of a match: it prices team strength,
injuries, rotation and motivation as of kickoff, and it is schedule-assigned (exogenous), the one
class of signal where the attenuation audit and F6 showed the anchor was blind. Source:
football-data.co.uk per-season E0.csv files (1X2, over/under 2.5, Pinnacle and average closing lines)
built into data/market_odds/pl_match_odds.csv by scripts/build_market_odds.py, which also fits an
independent-Poisson goal model to each match so every fixture carries a market expected-goals
number for both sides.

Per fixture row (one player, one match) the features are
  mkt_team_xg   market expected goals for the player's team
  mkt_opp_xg    market expected goals for the opponent
  mkt_cs_prob   exp(-mkt_opp_xg) = market clean-sheet probability
  mkt_win_prob  market probability the player's team wins
  mkt_available 1 when the match was matched to an odds row
A player-week sums them over the week's fixtures (doubles add, blanks are 0), then the dataset
crosses them with the player's own level (minutes, xGI) the same way F6 crosses opponent weakness.
Enabled with FPL_MARKET_FEATS=1; the table without the flag is unchanged.
"""
from __future__ import annotations

import math
import os
from functools import lru_cache
from pathlib import Path
from typing import Dict, Iterable, Optional, Tuple

import numpy as np
import pandas as pd

DEFAULT_ODDS_PATH = Path("data/market_odds/pl_match_odds.csv")
DEFAULT_UPCOMING_PATH = Path("data/market_odds/upcoming_odds.csv")
BASE_FEATURES = ["mkt_team_xg", "mkt_opp_xg", "mkt_cs_prob", "mkt_win_prob", "mkt_available"]
INTERACTION_FEATURES = ["mkt_xg_x_xgi_5", "mkt_xg_x_minutes_3", "mkt_cs_x_minutes_3"]
FEATURES = BASE_FEATURES + INTERACTION_FEATURES
MAX_GOALS = 12
LEAGUE_LAMBDA = 1.4  # fallback expected goals per side when a fixture has no odds


def enabled() -> bool:
    return os.environ.get("FPL_MARKET_FEATS", "0") == "1"


def london_date(stamps: pd.Series) -> pd.Series:
    """Calendar date in London for a UTC kickoff series (football-data dates are UK local dates)."""
    utc = pd.to_datetime(stamps, errors="coerce", utc=True)
    return utc.dt.tz_convert("Europe/London").dt.strftime("%Y-%m-%d")


def devig(odds: Iterable[float]) -> Optional[Tuple[float, ...]]:
    values = [float(o) for o in odds]
    if any(not math.isfinite(v) or v <= 1.0 for v in values):
        return None
    inv = [1.0 / v for v in values]
    total = sum(inv)
    return tuple(p / total for p in inv)


def _poisson_table(lam_h: float, lam_a: float) -> np.ndarray:
    goals = np.arange(MAX_GOALS + 1)
    ph = np.exp(-lam_h) * lam_h ** goals / np.array([math.factorial(g) for g in goals])
    pa = np.exp(-lam_a) * lam_a ** goals / np.array([math.factorial(g) for g in goals])
    return np.outer(ph, pa)


def outcome_probs(lam_h: float, lam_a: float) -> Tuple[float, float, float, float]:
    table = _poisson_table(lam_h, lam_a)
    home = float(np.tril(table, -1).sum())
    draw = float(np.trace(table))
    away = float(np.triu(table, 1).sum())
    totals = np.add.outer(np.arange(MAX_GOALS + 1), np.arange(MAX_GOALS + 1))
    over = float(table[totals > 2.5].sum())
    return home, draw, away, over


def fit_poisson(p_home: float, p_draw: float, p_away: float, p_over: Optional[float]) -> Tuple[float, float]:
    """Expected goals per side whose independent-Poisson outcome probabilities match the market."""
    from scipy.optimize import minimize

    targets = [p_home, p_draw, p_away] + ([p_over] if p_over is not None else [])

    def loss(x):
        probs = outcome_probs(x[0], x[1])
        model = list(probs[:3]) + ([probs[3]] if p_over is not None else [])
        return sum((m - t) ** 2 for m, t in zip(model, targets))

    best = None
    for init in ((1.5, 1.1), (1.1, 1.5), (1.3, 1.3)):
        res = minimize(loss, init, method="L-BFGS-B", bounds=[(0.15, 5.0), (0.15, 5.0)])
        if best is None or res.fun < best.fun:
            best = res
    return float(best.x[0]), float(best.x[1])


@lru_cache(maxsize=4)
def load_match_odds(path: str = str(DEFAULT_ODDS_PATH)) -> pd.DataFrame:
    """Season, London date, FPL team ids, probabilities and fitted lambdas per match; empty if absent."""
    file = Path(path)
    if not file.exists():
        return pd.DataFrame(columns=["season", "date", "home_team_id", "away_team_id", "lambda_home", "lambda_away",
                                     "p_home", "p_draw", "p_away"])
    odds = pd.read_csv(file, dtype={"season": str, "date": str})
    return odds


def fixture_market_lookup(odds: pd.DataFrame) -> pd.DataFrame:
    """One row per (season, date, team_id, opponent_team_id) with the team's own market numbers."""
    if odds.empty:
        return pd.DataFrame(columns=["season", "date", "team_id", "opponent_team_id"] + BASE_FEATURES)
    home = pd.DataFrame({
        "season": odds["season"], "date": odds["date"],
        "team_id": odds["home_team_id"].astype(int), "opponent_team_id": odds["away_team_id"].astype(int),
        "mkt_team_xg": odds["lambda_home"], "mkt_opp_xg": odds["lambda_away"], "mkt_win_prob": odds["p_home"],
    })
    away = pd.DataFrame({
        "season": odds["season"], "date": odds["date"],
        "team_id": odds["away_team_id"].astype(int), "opponent_team_id": odds["home_team_id"].astype(int),
        "mkt_team_xg": odds["lambda_away"], "mkt_opp_xg": odds["lambda_home"], "mkt_win_prob": odds["p_away"],
    })
    lookup = pd.concat([home, away], ignore_index=True)
    lookup["mkt_cs_prob"] = np.exp(-lookup["mkt_opp_xg"].astype(float))
    lookup["mkt_available"] = 1.0
    return lookup.drop_duplicates(["season", "date", "team_id", "opponent_team_id"])


def attach_fixture_market(raw: pd.DataFrame, odds: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    """Add the base market columns to fixture-level rows (season, team_id, opponent_team_id, kickoff_time).

    Unmatched fixtures get the league-average fallback with mkt_available = 0, so a missing odds row
    never zeroes a player's expected output.
    """
    frame = raw.copy()
    if odds is None:
        odds = load_match_odds(os.environ.get("FPL_MARKET_ODDS", str(DEFAULT_ODDS_PATH)))
    lookup = fixture_market_lookup(odds)
    frame["_mkt_date"] = london_date(frame["kickoff_time"])
    frame["_mkt_team"] = pd.to_numeric(frame["team_id"], errors="coerce").fillna(-1).astype(int)
    frame["_mkt_opp"] = pd.to_numeric(frame["opponent_team_id"], errors="coerce").fillna(-1).astype(int)
    merged = frame.merge(
        lookup.rename(columns={"date": "_mkt_date", "team_id": "_mkt_team", "opponent_team_id": "_mkt_opp"}),
        on=["season", "_mkt_date", "_mkt_team", "_mkt_opp"], how="left",
    )
    merged["mkt_available"] = merged["mkt_available"].fillna(0.0)
    merged["mkt_team_xg"] = merged["mkt_team_xg"].fillna(LEAGUE_LAMBDA)
    merged["mkt_opp_xg"] = merged["mkt_opp_xg"].fillna(LEAGUE_LAMBDA)
    merged["mkt_cs_prob"] = merged["mkt_cs_prob"].fillna(math.exp(-LEAGUE_LAMBDA))
    fallback_win = outcome_probs(LEAGUE_LAMBDA, LEAGUE_LAMBDA)[0]
    merged["mkt_win_prob"] = merged["mkt_win_prob"].fillna(fallback_win)
    return merged.drop(columns=["_mkt_date", "_mkt_team", "_mkt_opp"])


def add_interactions(frame: pd.DataFrame) -> pd.DataFrame:
    """Cross the week's market numbers with the player's own level (same shape as F6)."""
    xgi = pd.to_numeric(frame.get("expected_goal_involvements_avg_5"), errors="coerce").fillna(0.0)
    minutes = pd.to_numeric(frame.get("minutes_avg_3"), errors="coerce").fillna(0.0) / 90.0
    team_xg = pd.to_numeric(frame["mkt_team_xg"], errors="coerce").fillna(0.0)
    cs = pd.to_numeric(frame["mkt_cs_prob"], errors="coerce").fillna(0.0)
    frame["mkt_xg_x_xgi_5"] = team_xg * xgi
    frame["mkt_xg_x_minutes_3"] = team_xg * minutes
    frame["mkt_cs_x_minutes_3"] = cs * minutes
    return frame


def team_week_market(season: str, fixtures: pd.DataFrame, upcoming: Optional[pd.DataFrame] = None,
                     history: Optional[pd.DataFrame] = None) -> Dict[int, Dict[str, float]]:
    """Live: per-team base market sums for one gameweek.

    `fixtures` has team_h, team_a, kickoff_time (the FPL fixture list for the event). `upcoming` is
    the odds file for not-yet-played matches (same columns as pl_match_odds.csv). A fixture without
    an upcoming row falls back to the season's own history of fitted lambdas for both clubs (attack
    = mean of own lambdas, defence = mean of opponents' lambdas), then to the league average.
    """
    if upcoming is None:
        upcoming = load_match_odds(os.environ.get("FPL_MARKET_UPCOMING", str(DEFAULT_UPCOMING_PATH)))
    if history is None:
        history = load_match_odds(os.environ.get("FPL_MARKET_ODDS", str(DEFAULT_ODDS_PATH)))
    lookup = fixture_market_lookup(upcoming[upcoming["season"].astype(str) == str(season)] if not upcoming.empty else upcoming)
    keyed = {(r.date, int(r.team_id), int(r.opponent_team_id)): r for r in lookup.itertuples(index=False)}
    attack: Dict[int, list] = {}
    defence: Dict[int, list] = {}
    if not history.empty:
        for r in history[history["season"].astype(str) == str(season)].itertuples(index=False):
            attack.setdefault(int(r.home_team_id), []).append(float(r.lambda_home))
            attack.setdefault(int(r.away_team_id), []).append(float(r.lambda_away))
            defence.setdefault(int(r.home_team_id), []).append(float(r.lambda_away))
            defence.setdefault(int(r.away_team_id), []).append(float(r.lambda_home))
    out: Dict[int, Dict[str, float]] = {}
    dates = london_date(fixtures["kickoff_time"]) if "kickoff_time" in fixtures.columns else pd.Series([""] * len(fixtures))
    for (_, fixture), date in zip(fixtures.iterrows(), dates):
        home, away = int(fixture["team_h"]), int(fixture["team_a"])
        for team, opp in ((home, away), (away, home)):
            row = keyed.get((date, team, opp))
            if row is not None:
                team_xg, opp_xg, win, avail = float(row.mkt_team_xg), float(row.mkt_opp_xg), float(row.mkt_win_prob), 1.0
            else:
                own_att = float(np.mean(attack[team])) if attack.get(team) else LEAGUE_LAMBDA
                own_def = float(np.mean(defence[team])) if defence.get(team) else LEAGUE_LAMBDA
                opp_att = float(np.mean(attack[opp])) if attack.get(opp) else LEAGUE_LAMBDA
                opp_def = float(np.mean(defence[opp])) if defence.get(opp) else LEAGUE_LAMBDA
                team_xg = (own_att + opp_def) / 2.0
                opp_xg = (opp_att + own_def) / 2.0
                win = outcome_probs(team_xg, opp_xg)[0]
                avail = 0.0
            acc = out.setdefault(team, {k: 0.0 for k in BASE_FEATURES})
            acc["mkt_team_xg"] += team_xg
            acc["mkt_opp_xg"] += opp_xg
            acc["mkt_cs_prob"] += math.exp(-opp_xg)
            acc["mkt_win_prob"] += win
            acc["mkt_available"] = max(acc["mkt_available"], avail)
    return out
