"""Historical normalization and training-row generation."""

from __future__ import annotations

import json
import os
from dataclasses import asdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Union

import pandas as pd

from .config import (
    EXCLUDED_WEEKS,
    POSITION_ID_TO_NAME,
    TRAINING_CUTOFF_SEASON,
    TRAINING_CUTOFF_WEEK,
    is_excluded_week,
    parse_season_start_year,
    season_is_after_cutoff,
    week_is_after_cutoff,
)
from .types import PlayerWeekLabel, PlayerWeekRow, WeekEligibility, WeekState
from . import market, news_horizon


WeekId = Union[str, Tuple[str, int]]

IDENTIFIER_COLUMNS = [
    "season",
    "week",
    "player_id",
    "player_name",
    "team_id",
    "position",
]

LABEL_COLUMNS = [
    "label_points_1gw",
    "label_points_3gw",
    "label_points_5gw",
    "label_minutes_1gw",
    "label_appearance_probability",
]

REGIME_SEASON_START = "2025-26"  # first season with Defensive Contribution points
REGIME_POSITIONS = ("DEF", "MID", "FWD")  # GK is the reference level
REGIME_FEATURES = [*(f"pos_{p}" for p in REGIME_POSITIONS), "regime_defcon", *(f"regime_x_{p}" for p in REGIME_POSITIONS)]


def regime_term_mode() -> str:
    """'' (off), 'pos' (position dummies only) or '1' (dummies + DefCon-regime crosses), from FPL_REGIME_TERM."""
    value = os.environ.get("FPL_REGIME_TERM", "0").strip().lower()
    if value in ("1", "true", "regime"):
        return "1"
    if value in ("pos", "position"):
        return "pos"
    return ""


def add_regime_columns(frame: pd.DataFrame) -> pd.DataFrame:
    """Programme item 1 (2026-10-17): position dummies and the DefCon scoring-regime crosses (see REGIME_FEATURES).

    Idempotent and a no-op unless FPL_REGIME_TERM is set; with 'pos' the regime columns are all zero so only the
    dummies carry information (the A/B that separates the position effect from the regime effect).
    """
    mode = regime_term_mode()
    if not mode or "position" not in frame.columns or "season" not in frame.columns:
        return frame
    position = frame["position"].astype(str).str.upper().replace({"GKP": "GK"})
    regime = (frame["season"].astype(str) >= REGIME_SEASON_START).astype(float)
    if mode == "pos":
        regime = regime * 0.0
    frame["regime_defcon"] = regime
    for pos in REGIME_POSITIONS:
        dummy = (position == pos).astype(float)
        frame[f"pos_{pos}"] = dummy
        frame[f"regime_x_{pos}"] = dummy * regime
    return frame


SAFE_FEATURE_COLUMNS = [
    "price_pre_deadline",
    "selected_by_percent_pre_deadline",
    "transfers_in_prev_event",
    "transfers_out_prev_event",
    "transfer_balance_prev_event",
    "home_fixture_count",
    "away_fixture_count",
    "fixture_count",
    "fixture_difficulty_mean",
    "fixture_difficulty_min",
    "team_goals_for_avg_3",
    "team_goals_against_avg_3",
    "team_goals_for_avg_5",
    "team_goals_against_avg_5",
    "opponent_goals_for_avg_3",
    "opponent_goals_against_avg_3",
    "opponent_goals_for_avg_5",
    "opponent_goals_against_avg_5",
    # F6 opponent interaction (FPL_OPPONENT_INTERACTION=1) - filtered out of
    # the active feature list when the flag is off, same pattern as F5.
    "opp_def_weakness_3",
    "form_x_opp_weakness_3",
    "xgi_x_opp_weakness_3",
    "opp_def_weakness_5",
    "form_x_opp_weakness_5",
    "xgi_x_opp_weakness_5",
    # F9 congestion / European rotation (FPL_CONGESTION_FEATS=1)
    "euro_game_within_4d",
    "euro_game_within_7d",
    "days_rest_before_fixture",
    "club_matches_last_14d",
    "euro_x_minutes_3",
    "load_x_minutes_3",
    # F13 injury history (scripts/add_injury_history_features.py writes these into a table copy;
    # used only when present in the CSV)
    "inj_absences_38",
    "inj_long_layoff_prev",
    "inj_absences_x_price",
    # F17 prior-season availability (2026-10-27, scripts/add_prior_season_features.py writes these into a table
    # copy; used only when present in the CSV). Keyed on the stable `code`: player_id is the per-season element id
    # and is re-used by a different player the next season (reports/gw9_packet_2026_10/minutes_prior_study.md).
    "prior_pl_games",
    "no_prior_pl_season",
    "prior_start_share",
    "prior_minutes_share",
    "prior_unknown",
    # F12 team attack interaction (FPL_TEAM_ATTACK_INTERACTION=1)
    "team_attack_strength_3",
    "team_attack_x_xgi_3",
    "team_attack_x_minutes_3",
    "team_attack_strength_5",
    "team_attack_x_xgi_5",
    "team_attack_x_minutes_5",
    # F10 form-vs-underlying (FPL_FORM_VS_UNDERLYING=1)
    "form_vs_underlying_3",
    "form_vs_underlying_x_minutes_3",
    "form_vs_underlying_5",
    "form_vs_underlying_x_minutes_5",
    # F8 finishing regression (FPL_FINISHING_REGRESSION=1)
    "goals_over_xg_3",
    "assists_over_xa_3",
    "involvement_over_expected_3",
    "goals_over_xg_5",
    "assists_over_xa_5",
    "involvement_over_expected_5",
    # F7 depth chart (FPL_DEPTH_CHART=1)
    "pos_minutes_share_3",
    "pos_rivals_unavailable",
    "pos_rivals_minutes_vacated_3",
    "pos_unit_size",
    "points_avg_1",
    "minutes_avg_1",
    "appearance_rate_1",
    "played_60_rate_1",
    "points_avg_3",
    "minutes_avg_3",
    "appearance_rate_3",
    "played_60_rate_3",
    "points_avg_5",
    "minutes_avg_5",
    "appearance_rate_5",
    "played_60_rate_5",
    "points_avg_8",
    "minutes_avg_8",
    "appearance_rate_8",
    "played_60_rate_8",
    "price_change_1",
    "selected_change_1",
    "home_fixture_ratio",
    "blank_gw",
    "double_gw",
    "bonus_avg_3",
    "bonus_avg_5",
    "bps_avg_3",
    "bps_avg_5",
    "influence_avg_3",
    "influence_avg_5",
    "creativity_avg_3",
    "creativity_avg_5",
    "threat_avg_3",
    "threat_avg_5",
    "ict_index_avg_3",
    "ict_index_avg_5",
    "starts_avg_3",
    "starts_avg_5",
    "expected_goals_avg_3",
    "expected_goals_avg_5",
    "expected_assists_avg_3",
    "expected_assists_avg_5",
    "expected_goal_involvements_avg_3",
    "expected_goal_involvements_avg_5",
    "expected_goals_conceded_avg_3",
    "expected_goals_conceded_avg_5",
    "defensive_contribution_avg_3",
    "defensive_contribution_avg_5",
    "defcon_hit_rate_3",
    "defcon_hit_rate_5",
    # F5 (2026-09-10, Wes-caught): clean sheets are the single biggest
    # component of defender scoring (+4) and were NEVER modelled — raw
    # merged_gw carries clean_sheets/goals_conceded but neither reached the
    # feature frame, so "Arsenal keep clean sheets" could not influence a
    # forecast. Only built when FPL_CLEAN_SHEET_FEATS=1; get_feature_columns
    # filters to columns actually present, so the un-flagged table is
    # byte-identical to before.
    "clean_sheet_rate_3",
    "clean_sheet_rate_5",
    "goals_conceded_avg_3",
    "goals_conceded_avg_5",
    "expected_data_source_available",
    "defensive_data_source_available",
    "status_flag_pre_deadline",
    "news_flag_pre_deadline",
    "chance_pre_deadline",
    # F16 (FPL_TEAM_NEWS_FEATS=1, 2026-10-21): the Guardian's pre-deadline "predicted lineups" article parsed
    # into categories (implied XI / named sub / doubtful / injured or suspended); gn_article marks the
    # team-weeks that had an article before the deadline. Columns live in the _teamnews table variant.
    "gn_article",
    "gn_xi",
    "gn_sub",
    "gn_doubtful",
    "gn_out",
    # Extracted availability facts (FPL_EXTRACT_FEATS=1, 2026-10-22, scripts/build_extract_features.py): per
    # player-week facts read by a local Gemma extractor from the Guardian/Scout prose stores (xi / bench / doubt /
    # out / return / role), any-flag, recency weight and latest-status one-hot. Columns live in the _extract table.
    "ex_n",
    "ex_xi", "ex_bench", "ex_doubt", "ex_out", "ex_return", "ex_role",
    "ex_xi_w", "ex_bench_w", "ex_doubt_w", "ex_out_w", "ex_return_w", "ex_role_w",
    "ex_last_xi", "ex_last_bench", "ex_last_doubt", "ex_last_out", "ex_last_return", "ex_last_role",
    # Programme item 1 (2026-10-17, FPL_REGIME_TERM=1|pos, add_regime_columns): position dummies (GK = reference)
    # and the Defensive-Contribution scoring regime (seasons >= 2025-26) crossed with position, so the pooled
    # 8-season ridge can carry the regime shift (DEF 2.9 -> 3.7, MID 3.75 -> 4.0, FWD 4.6 -> 4.2 points per
    # 90-minute appearance) instead of averaging the two scoring systems. Columns exist only when the flag is on.
    *REGIME_FEATURES,
    # Programme item 4 (2026-10-17, scripts/add_setpiece_features.py writes these into a table copy from the weekly
    # pre-deadline snapshots; used only when present): penalty / corner / free-kick duties
    "pen_taker",
    "pen_order_inv",
    "corner_taker",
    "fk_taker",
    "setpiece_score",
    # F15 news horizon (FPL_NEWS_HORIZON=1, news_horizon.py): gameweeks the stated return date rules out
    *news_horizon.FEATURES,
    # F14 bookmaker market (FPL_MARKET_FEATS=1, market.py): closing-odds expected goals for the
    # team and the opponent, clean-sheet and win probabilities, summed over the week's fixtures,
    # plus the crosses with the player's own level. Only present when the table was built with
    # the flag, so the un-flagged table is unchanged.
    # F19 team level (FPL_TEAM_LEVEL_FEATS=1, 2026-10-31, scripts/add_team_level_features.py): the club's and the
    # opponent's prior-season and season-to-date goal difference per game, promoted flags and the unknown-season
    # flag, so the ridge can weigh its 3/5-week form windows against a longer baseline (team streaks revert: a 5-game
    # run carries +0.09 GD/game into the next match once the prior-season level is known, see
    # reports/team_trajectory_study/README.md). Columns live in the _teamlevel table variant; dropped unless flagged.
    "tl_team_prior_gd", "tl_opp_prior_gd", "tl_team_std_gd", "tl_opp_std_gd", "tl_team_promoted", "tl_opp_promoted", "tl_unknown",
    *market.FEATURES,
]

RAW_CANONICAL_COLUMNS = [
    "season",
    "week",
    "player_id",
    "player_name",
    "code",
    "team_id",
    "position",
    "price",
    "selected_by_percent",
    "transfers_in_event",
    "transfers_out_event",
    "status",
    "news",
    "chance_of_playing",
    "opponent_team_id",
    "was_home",
    "kickoff_time",
    "fixture_difficulty",
    "minutes",
    "total_points",
    "team_h_score",
    "team_a_score",
    "goals_scored",
    "assists",
    "bonus",
    "bps",
    "influence",
    "creativity",
    "threat",
    "ict_index",
    "starts",
    "expected_goals",
    "expected_assists",
    "expected_goal_involvements",
    "expected_goals_conceded",
    "defensive_contribution",
    "clean_sheets",
    "goals_conceded",
    "expected_data_source_available",
    "defensive_data_source_available",
]


CHANCE_BY_STATUS = {"a": 1.0, "d": 0.5, "i": 0.1, "s": 0.0, "u": 0.0, "n": 0.0}


def chance_of_playing_feature(status: pd.Series, chance: Optional[pd.Series]) -> pd.Series:
    """0-1 chance of playing: the recorded percentage when present (>= 0), else a status-letter prior
    (unknown status counts as available, like the binary flag)."""
    text = status.fillna("").astype(str).str.strip().str.lower()
    fallback = text.map(CHANCE_BY_STATUS).fillna(1.0)
    if chance is None:
        return fallback.astype(float)
    recorded = pd.to_numeric(chance, errors="coerce").fillna(-1.0)
    return (recorded / 100.0).where(recorded >= 0, fallback).clip(0.0, 1.0).astype(float)


def parse_week_id(week_id: WeekId) -> Tuple[str, int]:
    if isinstance(week_id, tuple):
        return week_id[0], int(week_id[1])
    season, week = str(week_id).split(":")
    return season, int(week)


def _normalize_price(series: pd.Series) -> pd.Series:
    numeric = pd.to_numeric(series, errors="coerce").fillna(0.0)
    return numeric.where(numeric <= 20.0, numeric / 10.0)


def _normalize_percent(series: pd.Series) -> pd.Series:
    cleaned = series.fillna(0).astype(str).str.replace("%", "", regex=False)
    return pd.to_numeric(cleaned, errors="coerce").fillna(0.0)


def _forward_rolling_sum(series: pd.Series, window: int) -> pd.Series:
    return series.iloc[::-1].rolling(window=window, min_periods=1).sum().iloc[::-1]


def _lagged_rolling_mean(grouped_series: pd.core.groupby.SeriesGroupBy, window: int) -> pd.Series:
    return grouped_series.transform(lambda series: series.shift(1).rolling(window=window, min_periods=1).mean())


def _ensure_columns(frame: pd.DataFrame, defaults: Dict[str, object]) -> pd.DataFrame:
    for column, default in defaults.items():
        if column not in frame.columns:
            frame[column] = default
    return frame


# Status value for weeks whose pre-deadline availability was never recorded.
# Treated as "not flagged" by the features and rendered as "none" in prompts,
# so it can never be mistaken for an explicit "a" (available).
STATUS_UNKNOWN = ""

# Every FPL squad holds exactly 15 players, so summing every player's
# selection count gives 15 x the number of entries (verified on the live API:
# selected_by_percent sums to 1500.0 over all players).
SQUAD_SIZE = 15.0

MULTIWEEK_LABEL_HORIZONS = {"label_points_3gw": 3, "label_points_5gw": 5, "label_points_8gw": 8}


def _team_at_fixture(frame: pd.DataFrame, fixtures: pd.DataFrame) -> Optional[pd.Series]:
    """The club a player represented in each fixture row, or None if unknowable."""
    if fixtures.empty or "fixture" not in frame.columns or "was_home" not in frame.columns:
        return None
    if not {"id", "team_h", "team_a"}.issubset(fixtures.columns):
        return None
    teams = fixtures[["id", "team_h", "team_a"]].drop_duplicates("id").set_index("id")
    fixture_id = pd.to_numeric(frame["fixture"], errors="coerce")
    home = frame["was_home"].astype(str).str.lower().isin({"true", "1", "1.0"})
    team_h = pd.to_numeric(fixture_id.map(teams["team_h"]), errors="coerce")
    team_a = pd.to_numeric(fixture_id.map(teams["team_a"]), errors="coerce")
    return team_h.where(home, team_a)


def _ownership_percent(selected: pd.Series, week: pd.Series, player_id: pd.Series) -> pd.Series:
    """Ownership as a true percentage of entries.

    Historical merged_gw files store `selected` as a COUNT of squads, while the
    live API reports a percentage. Counts are converted with the entry total
    implied by the 15-player identity. The running maximum over weeks keeps
    the denominator as-of and robust to blank weeks, where players without a
    fixture are missing from the file.
    """
    if selected.empty or float(selected.max()) <= 100.0:
        return selected
    frame = pd.DataFrame({"selected": selected, "week": week, "player_id": player_id})
    per_player_week = frame.drop_duplicates(subset=["week", "player_id"])
    entries = (per_player_week.groupby("week")["selected"].sum() / SQUAD_SIZE).sort_index().cummax()
    denominator = week.map(entries)
    percent = 100.0 * selected / denominator.where(denominator > 0)
    return percent.fillna(0.0).clip(0.0, 100.0)


def _asof_league_reference(values: pd.Series, season: pd.Series, week: pd.Series, team: pd.Series) -> pd.Series:
    """Per-(season, week) league mean of a team-level lagged statistic.

    Each team counts once (not once per player row), and only values already
    known at that week's deadline enter the mean, so later fixtures can never
    move an earlier row.
    """
    frame = pd.DataFrame(
        {"season": season.astype(str), "week": pd.to_numeric(week, errors="coerce"), "team": team, "value": values}
    )
    known = frame.loc[(pd.to_numeric(frame["team"], errors="coerce") > 0) & frame["value"].notna()]
    reference = (
        known.drop_duplicates(subset=["season", "week", "team"])
        .groupby(["season", "week"], as_index=False)["value"]
        .mean()
        .rename(columns={"value": "reference"})
    )
    merged = frame[["season", "week"]].merge(reference, on=["season", "week"], how="left")
    return pd.Series(merged["reference"].to_numpy(), index=values.index, dtype=float)


def training_rows_asof(training_frame: pd.DataFrame, season: str, week: int) -> pd.DataFrame:
    """Rows usable to fit a model that predicts `season` GW`week`.

    Rows must come from strictly earlier weeks, and multi-week labels must be
    fully settled before the cutoff: a 5GW label from GW t covers t..t+4, so
    it is masked (NaN) unless t + 4 < week. Model fitting drops NaN labels per
    head, so the 1GW and minutes heads keep those rows.
    """
    frame = training_frame
    eligible = frame["eligible_for_training"].astype(str).str.lower().isin({"true", "1", "1.0"})
    row_key = frame["season"].astype(str).map(parse_season_start_year) * 100 + pd.to_numeric(
        frame["week"], errors="coerce"
    )
    cutoff_key = parse_season_start_year(season) * 100 + int(week)
    rows = frame.loc[eligible & (row_key < cutoff_key)].copy()
    in_season = rows["season"].astype(str) == str(season)
    row_week = pd.to_numeric(rows["week"], errors="coerce")
    for column, horizon in MULTIWEEK_LABEL_HORIZONS.items():
        if column in rows.columns:
            rows[column] = pd.to_numeric(rows[column], errors="coerce")
            rows.loc[in_season & (row_week + horizon - 1 >= int(week)), column] = float("nan")
    return rows


def latest_training_cutoff(training_frame: pd.DataFrame) -> Tuple[str, int]:
    """(season, week) just after the newest eligible training row."""
    eligible = training_frame.loc[
        training_frame["eligible_for_training"].astype(str).str.lower().isin({"true", "1", "1.0"})
    ]
    keys = eligible["season"].astype(str).map(parse_season_start_year) * 100 + pd.to_numeric(
        eligible["week"], errors="coerce"
    )
    newest = eligible.loc[keys.idxmax()]
    return str(newest["season"]), int(newest["week"]) + 1


def get_week_eligibility(season: str, week: int) -> WeekEligibility:
    if is_excluded_week(season, week):
        return WeekEligibility(
            season=season,
            week=week,
            eligible_for_training=False,
            eligible_for_backtest=False,
            reason=EXCLUDED_WEEKS[(season, week)],
        )
    if season_is_after_cutoff(season) or week_is_after_cutoff(season, week):
        return WeekEligibility(
            season=season,
            week=week,
            eligible_for_training=False,
            eligible_for_backtest=False,
            reason=(
                "Excluded because it is after the configured training cutoff of "
                f"{TRAINING_CUTOFF_SEASON} GW{TRAINING_CUTOFF_WEEK}."
            ),
        )
    return WeekEligibility(
        season=season,
        week=week,
        eligible_for_training=True,
        eligible_for_backtest=True,
        reason="Eligible for v1 training and backtests.",
    )


def _load_players_lookup(season_dir: Path) -> pd.DataFrame:
    players_raw = season_dir / "players_raw.csv"
    if not players_raw.exists():
        return pd.DataFrame()
    lookup = pd.read_csv(players_raw)
    if "id" not in lookup.columns:
        return pd.DataFrame()
    rename_map = {
        "id": "player_id",
        "web_name": "player_name",
        "team": "team_id",
        "element_type": "position_id",
        "status": "status",
        "news": "news",
        "now_cost": "price",
        "selected_by_percent": "selected_by_percent",
    }
    lookup = lookup.rename(columns={k: v for k, v in rename_map.items() if k in lookup.columns})
    return lookup


def _load_fixtures_lookup(season_dir: Path) -> pd.DataFrame:
    fixtures_path = season_dir / "fixtures.csv"
    if not fixtures_path.exists():
        return pd.DataFrame()
    fixtures = pd.read_csv(fixtures_path)
    return fixtures


def _load_season_gameweeks(season_dir: Path, season: str) -> pd.DataFrame:
    merged_path = season_dir / "merged_gw.csv"
    gws_merged_path = season_dir / "gws" / "merged_gw.csv"
    if merged_path.exists():
        frame = pd.read_csv(merged_path)
    elif gws_merged_path.exists():
        frame = pd.read_csv(gws_merged_path)
    else:
        gw_dir = season_dir / "gws"
        if not gw_dir.exists():
            raise FileNotFoundError(f"Could not find merged_gw.csv or gws/ in {season_dir}")
        frames = []
        for path in sorted(gw_dir.glob("gw*.csv")):
            gameweek = int(path.stem.replace("gw", ""))
            gw_frame = pd.read_csv(path)
            if "week" not in gw_frame.columns and "round" not in gw_frame.columns and "event" not in gw_frame.columns:
                gw_frame["week"] = gameweek
            frames.append(gw_frame)
        frame = pd.concat(frames, ignore_index=True)
    frame["season"] = season
    return frame


def _merge_fixture_difficulty(frame: pd.DataFrame, fixtures: pd.DataFrame) -> pd.DataFrame:
    if fixtures.empty:
        return frame
    merged = frame.copy()
    if "fixture" in merged.columns and "id" in fixtures.columns:
        merged = merged.merge(
            fixtures[["id", "team_h_difficulty", "team_a_difficulty"]],
            left_on="fixture",
            right_on="id",
            how="left",
        )
        merged["fixture_difficulty"] = merged.apply(
            lambda row: row["team_h_difficulty"] if bool(row.get("was_home")) else row["team_a_difficulty"],
            axis=1,
        )
        return merged.drop(columns=["id"], errors="ignore")

    required = {"event", "team_h", "team_a", "team_h_difficulty", "team_a_difficulty"}
    if not required.issubset(fixtures.columns) or "team_id" not in merged.columns or "opponent_team_id" not in merged.columns:
        return merged

    fixtures_lookup = fixtures[list(required)].rename(columns={"event": "week"})
    fixtures_lookup["team_id"] = fixtures_lookup["team_h"]
    fixtures_lookup["opponent_team_id"] = fixtures_lookup["team_a"]
    fixtures_lookup["was_home"] = True
    fixtures_lookup["fixture_difficulty"] = fixtures_lookup["team_h_difficulty"]

    reverse_lookup = fixtures_lookup.copy()
    reverse_lookup["team_id"] = reverse_lookup["opponent_team_id"]
    reverse_lookup["opponent_team_id"] = fixtures_lookup["team_id"]
    reverse_lookup["was_home"] = False
    reverse_lookup["fixture_difficulty"] = reverse_lookup["team_a_difficulty"]

    lookup = pd.concat(
        [
            fixtures_lookup[["week", "team_id", "opponent_team_id", "was_home", "fixture_difficulty"]],
            reverse_lookup[["week", "team_id", "opponent_team_id", "was_home", "fixture_difficulty"]],
        ],
        ignore_index=True,
    )
    merged = merged.merge(
        lookup,
        on=["week", "team_id", "opponent_team_id", "was_home"],
        how="left",
    )
    return merged


def normalize_vaastav_history(history_root: Union[str, Path]) -> pd.DataFrame:
    """Load a vaastav-style historical repository into a canonical fixture-level frame."""

    history_root = Path(history_root)
    season_dirs = [path for path in sorted(history_root.iterdir()) if path.is_dir()]
    all_frames: List[pd.DataFrame] = []

    for season_dir in season_dirs:
        season = season_dir.name
        try:
            season_frame = _load_season_gameweeks(season_dir, season)
        except FileNotFoundError:
            # A season dir with fixtures/teams but no per-gameweek data yet —
            # e.g. the live season's schedule written for fixture-outlook
            # attachment before any matches are played. Nothing to train on.
            continue
        players_lookup = _load_players_lookup(season_dir)
        fixtures_lookup = _load_fixtures_lookup(season_dir)

        rename_map = {
            "round": "week",
            "event": "week",
            "element": "player_id",
            "id": "player_id",
            "name": "player_name",
            "team": "team_id",
            "opponent_team": "opponent_team_id",
            "value": "price",
            "selected": "selected_by_percent",
            "transfers_in": "transfers_in_event",
            "transfers_out": "transfers_out_event",
        }
        season_frame = season_frame.rename(columns={k: v for k, v in rename_map.items() if k in season_frame.columns})
        # Only a per-gameweek status column is a pre-deadline fact. Seasons
        # without one would otherwise inherit players_raw.csv's END-OF-SEASON
        # status/news, copied onto every week (a leak: a player injured in May
        # reads "injured" in August).
        has_weekly_status = "status" in season_frame.columns
        team_at_fixture = _team_at_fixture(season_frame, fixtures_lookup)

        expected_columns = {
            "expected_goals",
            "expected_assists",
            "expected_goal_involvements",
            "expected_goals_conceded",
        }
        defensive_columns = {
            "defensive_contribution",
            "clearances_blocks_interceptions",
            "recoveries",
            "tackles",
        }
        season_frame["expected_data_source_available"] = float(any(column in season_frame.columns for column in expected_columns))
        season_frame["defensive_data_source_available"] = float(any(column in season_frame.columns for column in defensive_columns))

        if not players_lookup.empty:
            merge_columns = ["player_id"]
            for column in ["player_name", "team_id", "position_id", "status", "news", "price", "selected_by_percent", "code"]:
                if column in players_lookup.columns:
                    merge_columns.append(column)
            season_frame = season_frame.merge(players_lookup[merge_columns], on="player_id", how="left", suffixes=("", "_lookup"))
            # players_raw.csv (players_lookup) carries the correct numeric
            # team_id; merged_gw.csv's own "team" column is a name STRING
            # ("Sunderland", not 17) that silently coerces to NaN -> the -1
            # default below. Without this coalesce, team_id is -1 for every
            # row (verified: 100% of rows, all seasons) -- team-conditional
            # features (team_goals_for_avg_3/5 etc.) collapse to one global
            # pool instead of per-team, and the squad optimizer's "max 3 per
            # club" constraint silently never triggers (candidate.team_id > 0
            # is never true). Prefer the lookup's numeric value when present.
            for column in ["team_id", "position_id"]:
                lookup_column = f"{column}_lookup"
                if lookup_column in season_frame.columns:
                    season_frame[column] = pd.to_numeric(season_frame[lookup_column], errors="coerce").combine_first(
                        pd.to_numeric(season_frame.get(column), errors="coerce")
                    )
                    season_frame = season_frame.drop(columns=[lookup_column])

        # players_raw.csv is an end-of-season snapshot, so its team is the
        # club a player finished with. Mid-season movers then carry their old
        # club's matches into the new club's team form. The fixture itself
        # says which side the player was on.
        if team_at_fixture is not None:
            season_frame["team_id"] = team_at_fixture.combine_first(
                pd.to_numeric(season_frame.get("team_id"), errors="coerce")
            )
        if not has_weekly_status:
            season_frame["status"] = STATUS_UNKNOWN
            season_frame["news"] = ""
            # Pre-deadline snapshots reconstructed from the data repository's commit history
            # (scripts/backfill_history_status_from_vaastav.py, 2026-10-14). Only rows with a
            # snapshot keep a real status; the rest stay unknown rather than "available".
            weekly_status_path = season_dir / "weekly_status.csv"
            if weekly_status_path.exists() and "week" in season_frame.columns and "player_id" in season_frame.columns:
                weekly = pd.read_csv(weekly_status_path, low_memory=False)
                if "chance_next" not in weekly.columns:
                    weekly["chance_next"] = -1.0
                weekly = weekly.drop_duplicates(["week", "player_id"])[["week", "player_id", "status", "news", "chance_next"]]
                weekly["week"] = pd.to_numeric(weekly["week"], errors="coerce").fillna(0).astype(int)
                weekly["player_id"] = pd.to_numeric(weekly["player_id"], errors="coerce").fillna(-1).astype(int)
                keyed = season_frame[["week", "player_id"]].copy()
                keyed["week"] = pd.to_numeric(keyed["week"], errors="coerce").fillna(0).astype(int)
                keyed["player_id"] = pd.to_numeric(keyed["player_id"], errors="coerce").fillna(-1).astype(int)
                joined = keyed.merge(weekly, on=["week", "player_id"], how="left")
                season_frame["status"] = joined["status"].fillna(STATUS_UNKNOWN).to_numpy()
                season_frame["news"] = joined["news"].fillna("").astype(str).to_numpy()
                season_frame["chance_of_playing"] = pd.to_numeric(joined["chance_next"], errors="coerce").fillna(-1.0).to_numpy()

        # chance_of_playing: FPL's 0-100 "chance of playing next round" when a pre-deadline snapshot
        # carried it; -1 = not recorded (derived from the status letter at feature time).
        if "chance_of_playing" not in season_frame.columns:
            season_frame["chance_of_playing"] = -1.0
        season_frame = _ensure_columns(
            season_frame,
            {
                "week": 0,
                "player_id": -1,
                "player_name": "",
                "code": -1,
                "team_id": -1,
                "position": "",
                "position_id": 0,
                "price": 0.0,
                "selected_by_percent": 0.0,
                "transfers_in_event": 0.0,
                "transfers_out_event": 0.0,
                "status": "a",
                "news": "",
                "opponent_team_id": -1,
                "was_home": False,
                "kickoff_time": "",
                "fixture_difficulty": 0.0,
                "minutes": 0.0,
                "total_points": 0.0,
                "team_h_score": 0.0,
                "team_a_score": 0.0,
                "goals_scored": 0.0,
                "assists": 0.0,
                "bonus": 0.0,
                "bps": 0.0,
                "influence": 0.0,
                "creativity": 0.0,
                "threat": 0.0,
                "ict_index": 0.0,
                "starts": 0.0,
                "expected_goals": 0.0,
                "expected_assists": 0.0,
                "expected_goal_involvements": 0.0,
                "expected_goals_conceded": 0.0,
                "defensive_contribution": 0.0,
                "clean_sheets": 0.0,
                "goals_conceded": 0.0,
                "expected_data_source_available": 0.0,
                "defensive_data_source_available": 0.0,
            },
        )

        if "position" not in season_frame.columns or season_frame["position"].eq("").all():
            season_frame["position"] = season_frame["position_id"].map(POSITION_ID_TO_NAME).fillna(season_frame["position"])

        season_frame["price"] = _normalize_price(season_frame["price"])
        season_frame["week"] = pd.to_numeric(season_frame["week"], errors="coerce").fillna(0).astype(int)
        season_frame["player_id"] = pd.to_numeric(season_frame["player_id"], errors="coerce").fillna(-1).astype(int)
        season_frame["selected_by_percent"] = _ownership_percent(
            _normalize_percent(season_frame["selected_by_percent"]),
            season_frame["week"],
            season_frame["player_id"],
        )
        season_frame["team_id"] = pd.to_numeric(season_frame["team_id"], errors="coerce").fillna(-1).astype(int)
        season_frame["opponent_team_id"] = pd.to_numeric(
            season_frame["opponent_team_id"], errors="coerce"
        ).fillna(-1).astype(int)
        season_frame["was_home"] = season_frame["was_home"].fillna(False).astype(bool)
        season_frame["minutes"] = pd.to_numeric(season_frame["minutes"], errors="coerce").fillna(0.0)
        season_frame["total_points"] = pd.to_numeric(season_frame["total_points"], errors="coerce").fillna(0.0)
        season_frame["transfers_in_event"] = pd.to_numeric(
            season_frame["transfers_in_event"], errors="coerce"
        ).fillna(0.0)
        season_frame["transfers_out_event"] = pd.to_numeric(
            season_frame["transfers_out_event"], errors="coerce"
        ).fillna(0.0)
        for column in [
            "bonus",
            "bps",
            "influence",
            "creativity",
            "threat",
            "ict_index",
            "starts",
            "expected_goals",
            "expected_assists",
            "expected_goal_involvements",
            "expected_goals_conceded",
            "defensive_contribution",
            "clean_sheets",
            "goals_conceded",
            "expected_data_source_available",
            "defensive_data_source_available",
        ]:
            season_frame[column] = pd.to_numeric(season_frame[column], errors="coerce").fillna(0.0)

        season_frame = _merge_fixture_difficulty(season_frame, fixtures_lookup)
        season_frame = _ensure_columns(season_frame, {column: 0.0 for column in RAW_CANONICAL_COLUMNS})
        all_frames.append(season_frame[RAW_CANONICAL_COLUMNS].copy())

    if not all_frames:
        raise FileNotFoundError(f"No season directories found under {history_root}")
    return pd.concat(all_frames, ignore_index=True).sort_values(["season", "week", "player_id"]).reset_index(drop=True)


def _load_european_fixtures(path: Path) -> Dict[Tuple[str, int], List[pd.Timestamp]]:
    """(season, fpl_team_id) -> sorted European kickoff timestamps.

    The feed names clubs in its own style, so a small alias table maps them to
    each season's FPL team table (FPL ids are season-local, hence the per-season
    rebuild). Clubs that never qualified simply have no entry and score 0 on
    every congestion feature, which is correct rather than missing.
    """
    out: Dict[Tuple[str, int], List[pd.Timestamp]] = {}
    if not path.exists():
        return out
    aliases = {"Tottenham": "Spurs", "Man United": "Man Utd"}
    history_root = Path(os.environ.get("FPL_HISTORY_ROOT", "data/fpl_history"))
    name_to_id: Dict[Tuple[str, str], int] = {}
    if history_root.exists():
        for season_dir in sorted(history_root.iterdir()):
            teams_csv = season_dir / "teams.csv"
            if not teams_csv.exists():
                continue
            frame = pd.read_csv(teams_csv)
            for row in frame.itertuples(index=False):
                try:
                    name_to_id[(season_dir.name, str(row.name))] = int(row.id)
                except (AttributeError, ValueError, TypeError):
                    continue
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
            start_year = int(record["season_start_year"])
            when = pd.to_datetime(str(record["date_utc"]).replace("Z", ""), utc=True, errors="coerce")
        except (json.JSONDecodeError, KeyError, ValueError, TypeError):
            continue
        if pd.isna(when):
            continue
        season = f"{start_year}-{str(start_year + 1)[-2:]}"
        for side in ("home", "away"):
            club = aliases.get(record.get(side), record.get(side))
            team_id = name_to_id.get((season, str(club)))
            if team_id is None:
                continue
            out.setdefault((season, team_id), []).append(when)
    for key in out:
        out[key] = sorted(out[key])
    return out


def _build_team_form(frame: pd.DataFrame) -> pd.DataFrame:
    team_fixture_rows = frame[
        [
            "season",
            "week",
            "team_id",
            "opponent_team_id",
            "was_home",
            "kickoff_time",
            "team_h_score",
            "team_a_score",
        ]
    ].drop_duplicates()
    team_fixture_rows["goals_for"] = team_fixture_rows.apply(
        lambda row: row["team_h_score"] if bool(row["was_home"]) else row["team_a_score"],
        axis=1,
    )
    team_fixture_rows["goals_against"] = team_fixture_rows.apply(
        lambda row: row["team_a_score"] if bool(row["was_home"]) else row["team_h_score"],
        axis=1,
    )
    team_week = (
        team_fixture_rows.groupby(["season", "team_id", "week"], as_index=False)[["goals_for", "goals_against"]]
        .sum()
        .sort_values(["season", "team_id", "week"])
    )
    grouped = team_week.groupby(["season", "team_id"], sort=False)
    team_week["team_goals_for_avg_3"] = _lagged_rolling_mean(grouped["goals_for"], 3)
    team_week["team_goals_against_avg_3"] = _lagged_rolling_mean(grouped["goals_against"], 3)
    team_week["team_goals_for_avg_5"] = _lagged_rolling_mean(grouped["goals_for"], 5)
    team_week["team_goals_against_avg_5"] = _lagged_rolling_mean(grouped["goals_against"], 5)

    # F2c (FPL_PRIOR_BLEND=1): blend early-season TEAM attack/defense form
    # toward the club's prior-season per-week rates, keyed by club NAME via
    # each season's teams.csv (FPL team_ids are season-local). The player-
    # level blend (F2b) left team features on raw 2-game windows — which is
    # how GW3 2026-27 rated Hull's defense (2 CS vs a promoted side and a
    # shambolic United) above Man City's (0 CS vs two real opponents).
    # Promoted clubs have no prior row -> w=1 (pure current, no fabricated
    # pedigree). Opponent_* features derive from this same table downstream,
    # so the blend propagates automatically.
    # REJECTED 2026-09-04 (three-window backtest: net −11 vs F2b-only —
    # team form is less sticky than player quality). Kept behind its OWN
    # flag so FPL_PRIOR_BLEND=1 rebuilds reproduce the ADOPTED F2b-only
    # table; enable only for re-testing.
    if os.environ.get("FPL_PRIOR_BLEND_TEAM", "0") == "1":
        history_root = Path(os.environ.get("FPL_HISTORY_ROOT", "data/fpl_history"))
        id_to_name: Dict[Tuple[str, int], str] = {}
        for season_dir in history_root.iterdir() if history_root.exists() else []:
            teams_csv = season_dir / "teams.csv"
            if not teams_csv.exists():
                continue
            teams = pd.read_csv(teams_csv)
            if "id" in teams.columns and "name" in teams.columns:
                for row in teams.itertuples(index=False):
                    id_to_name[(season_dir.name, int(row.id))] = str(row.name)
        names = pd.Series(
            [id_to_name.get((s, int(t))) for s, t in zip(team_week["season"], team_week["team_id"])],
            index=team_week.index,
        )
        season_rates = (
            team_week.assign(club=names)
            .dropna(subset=["club"])
            .groupby(["club", "season"], sort=False)[["goals_for", "goals_against"]]
            .mean()
        )
        prior_gf, prior_ga = [], []
        for club, season in zip(names, team_week["season"]):
            key = (club, f"{parse_season_start_year(season) - 1}-{str(parse_season_start_year(season))[2:]}")
            if club is not None and key in season_rates.index:
                row = season_rates.loc[key]
                prior_gf.append(float(row["goals_for"]))
                prior_ga.append(float(row["goals_against"]))
            else:
                prior_gf.append(float("nan"))
                prior_ga.append(float("nan"))
        prior_gf = pd.Series(prior_gf, index=team_week.index)
        prior_ga = pd.Series(prior_ga, index=team_week.index)
        weeks_before = grouped.cumcount()
        blend_w = (weeks_before / 6.0).clip(0.0, 1.0).where(prior_gf.notna(), 1.0)
        for column, prior in (
            ("team_goals_for_avg_3", prior_gf), ("team_goals_for_avg_5", prior_gf),
            ("team_goals_against_avg_3", prior_ga), ("team_goals_against_avg_5", prior_ga),
        ):
            team_week[column] = blend_w * team_week[column].fillna(0.0) + (1.0 - blend_w) * prior.fillna(0.0)
    return team_week


def _expand_blank_weeks(player_week: pd.DataFrame) -> pd.DataFrame:
    expanded: List[pd.DataFrame] = []
    static_columns = ["player_name", "team_id", "position"]
    carry_columns = ["price", "selected_by_percent", "status", "news"]
    fill_zero_columns = [
        "transfers_in_event",
        "transfers_out_event",
        "home_fixture_count",
        "away_fixture_count",
        "fixture_count",
        "fixture_difficulty_mean",
        "fixture_difficulty_min",
        "observed_points",
        "observed_minutes",
        "observed_appearances",
        "observed_played_60",
        "observed_bonus",
        "observed_bps",
        "observed_influence",
        "observed_creativity",
        "observed_threat",
        "observed_ict_index",
        "observed_starts",
        "observed_expected_goals",
        "observed_expected_assists",
        "observed_expected_goal_involvements",
        "observed_expected_goals_conceded",
        "observed_defensive_contribution",
        "observed_clean_sheets",
        "observed_goals_conceded",
        "expected_data_source_available",
        "defensive_data_source_available",
    ]

    for (season, player_id), group in player_week.groupby(["season", "player_id"], sort=False):
        group = group.sort_values("week")
        first_week = int(group["week"].min())
        last_week = int(group["week"].max())
        weeks = pd.DataFrame({"week": range(first_week, last_week + 1)})
        reindexed = weeks.merge(group, on="week", how="left")
        reindexed["season"] = season
        reindexed["player_id"] = player_id

        for column in static_columns:
            reindexed[column] = reindexed[column].ffill().bfill()
        for column in carry_columns:
            reindexed[column] = reindexed[column].ffill().fillna(0 if column in {"price", "selected_by_percent"} else "")
        reindexed["status"] = reindexed["status"].replace(0, "a").fillna("a")
        reindexed["primary_opponent_team_id"] = reindexed["primary_opponent_team_id"].fillna(-1).astype(int)
        reindexed["kickoff_time"] = reindexed["kickoff_time"].fillna("")
        for column in fill_zero_columns:
            reindexed[column] = pd.to_numeric(reindexed[column], errors="coerce").fillna(0.0)
        expanded.append(reindexed)

    return pd.concat(expanded, ignore_index=True).sort_values(["season", "player_id", "week"]).reset_index(drop=True)


def build_training_frame(raw_history: pd.DataFrame) -> pd.DataFrame:
    """Convert fixture-level history into a pre-deadline player-week training frame."""

    raw = _ensure_columns(
        raw_history.copy(),
        {
            "code": -1,
            "chance_of_playing": -1.0,
            "goals_scored": 0.0,
            "assists": 0.0,
            "bonus": 0.0,
            "bps": 0.0,
            "influence": 0.0,
            "creativity": 0.0,
            "threat": 0.0,
            "ict_index": 0.0,
            "starts": 0.0,
            "expected_goals": 0.0,
            "expected_assists": 0.0,
            "expected_goal_involvements": 0.0,
            "expected_goals_conceded": 0.0,
            "defensive_contribution": 0.0,
            "clean_sheets": 0.0,
            "goals_conceded": 0.0,
            "expected_data_source_available": 0.0,
            "defensive_data_source_available": 0.0,
        },
    )
    raw["minutes"] = pd.to_numeric(raw["minutes"], errors="coerce").fillna(0.0)
    raw["total_points"] = pd.to_numeric(raw["total_points"], errors="coerce").fillna(0.0)
    raw["price"] = _normalize_price(raw["price"])
    raw["selected_by_percent"] = _normalize_percent(raw["selected_by_percent"])
    raw["fixture_difficulty"] = pd.to_numeric(raw["fixture_difficulty"], errors="coerce").fillna(0.0)
    raw["appearance"] = (raw["minutes"] > 0).astype(float)
    # DefCon BONUS is a THRESHOLD rule (+2 pts iff the per-match count
    # reaches 10 for DEF / 12 for MID+FWD, since 2025-26) — a linear model
    # on average counts can't express it (avg-10-steady and avg-10-spiky
    # earn very different bonus income). Precompute the nonlinearity as a
    # per-match hit indicator; the lagged rolling mean below becomes a
    # hit-RATE whose payoff is ~2x rate, which ridge can learn directly.
    # Pre-2025-26 rows have defensive_contribution == 0 -> rate 0, paired
    # with the existing defensive_data_source_available era flag (same
    # convention as the other era-gated features).
    defcon_threshold = raw["position"].map({"DEF": 10.0, "MID": 12.0, "FWD": 12.0}).fillna(9999.0)
    raw["defcon_hit"] = (
        (pd.to_numeric(raw["defensive_contribution"], errors="coerce").fillna(0.0) >= defcon_threshold)
        & (raw["minutes"] > 0)
    ).astype(float)
    raw["played_60"] = (raw["minutes"] >= 60).astype(float)
    for column in [
        "goals_scored",
        "assists",
        "bonus",
        "bps",
        "influence",
        "creativity",
        "threat",
        "ict_index",
        "starts",
        "expected_goals",
        "expected_assists",
        "expected_goal_involvements",
        "expected_goals_conceded",
        "defensive_contribution",
        "clean_sheets",
        "goals_conceded",
        "expected_data_source_available",
        "defensive_data_source_available",
    ]:
        raw[column] = pd.to_numeric(raw[column], errors="coerce").fillna(0.0)

    team_form = _build_team_form(raw)

    # F14 (FPL_MARKET_FEATS=1): closing-odds market numbers per fixture row, before the week
    # aggregation so a double gameweek adds both matches and a blank week carries zeros.
    if market.enabled():
        raw = market.attach_fixture_market(raw)

    player_week = (
        raw.groupby(["season", "week", "player_id"], as_index=False)
        .agg(
            player_name=("player_name", "first"),
            code=("code", "first"),
            team_id=("team_id", "first"),
            position=("position", "first"),
            price=("price", "first"),
            selected_by_percent=("selected_by_percent", "first"),
            transfers_in_event=("transfers_in_event", "first"),
            transfers_out_event=("transfers_out_event", "first"),
            status=("status", "first"),
            news=("news", "first"),
            chance_of_playing=("chance_of_playing", "first"),
            primary_opponent_team_id=("opponent_team_id", "first"),
            kickoff_time=("kickoff_time", "min"),
            home_fixture_count=("was_home", "sum"),
            fixture_count=("player_id", "size"),
            fixture_difficulty_mean=("fixture_difficulty", "mean"),
            fixture_difficulty_min=("fixture_difficulty", "min"),
            observed_points=("total_points", "sum"),
            observed_minutes=("minutes", "sum"),
            observed_appearances=("appearance", "sum"),
            observed_played_60=("played_60", "sum"),
            observed_bonus=("bonus", "sum"),
            observed_bps=("bps", "sum"),
            observed_influence=("influence", "sum"),
            observed_creativity=("creativity", "sum"),
            observed_threat=("threat", "sum"),
            observed_ict_index=("ict_index", "sum"),
            observed_starts=("starts", "sum"),
            observed_goals=("goals_scored", "sum"),
            observed_assists=("assists", "sum"),
            observed_expected_goals=("expected_goals", "sum"),
            observed_expected_assists=("expected_assists", "sum"),
            observed_expected_goal_involvements=("expected_goal_involvements", "sum"),
            observed_expected_goals_conceded=("expected_goals_conceded", "sum"),
            observed_defensive_contribution=("defensive_contribution", "sum"),
            observed_clean_sheets=("clean_sheets", "sum"),
            observed_goals_conceded=("goals_conceded", "sum"),
            observed_defcon_hits=("defcon_hit", "sum"),
            expected_data_source_available=("expected_data_source_available", "max"),
            defensive_data_source_available=("defensive_data_source_available", "max"),
        )
        .sort_values(["season", "player_id", "week"])
    )
    player_week["away_fixture_count"] = player_week["fixture_count"] - player_week["home_fixture_count"]
    player_week = _expand_blank_weeks(player_week)

    if market.enabled():
        week_market = raw.groupby(["season", "week", "player_id"], as_index=False).agg(
            mkt_team_xg=("mkt_team_xg", "sum"),
            mkt_opp_xg=("mkt_opp_xg", "sum"),
            mkt_cs_prob=("mkt_cs_prob", "sum"),
            mkt_win_prob=("mkt_win_prob", "sum"),
            mkt_available=("mkt_available", "max"),
        )
        player_week = player_week.merge(week_market, on=["season", "week", "player_id"], how="left")
        for column in market.BASE_FEATURES:
            player_week[column] = pd.to_numeric(player_week[column], errors="coerce").fillna(0.0)

    player_week = player_week.merge(
        team_form,
        on=["season", "team_id", "week"],
        how="left",
    )
    opponent_form = team_form.rename(
        columns={
            "team_id": "primary_opponent_team_id",
            "team_goals_for_avg_3": "opponent_goals_for_avg_3",
            "team_goals_against_avg_3": "opponent_goals_against_avg_3",
            "team_goals_for_avg_5": "opponent_goals_for_avg_5",
            "team_goals_against_avg_5": "opponent_goals_against_avg_5",
        }
    )
    player_week = player_week.merge(
        opponent_form[
            [
                "season",
                "primary_opponent_team_id",
                "week",
                "opponent_goals_for_avg_3",
                "opponent_goals_against_avg_3",
                "opponent_goals_for_avg_5",
                "opponent_goals_against_avg_5",
            ]
        ],
        on=["season", "primary_opponent_team_id", "week"],
        how="left",
    )

    grouped = player_week.groupby(["season", "player_id"], sort=False)
    for window in [1, 3, 5, 8]:
        player_week[f"points_avg_{window}"] = _lagged_rolling_mean(grouped["observed_points"], window)
        player_week[f"minutes_avg_{window}"] = _lagged_rolling_mean(grouped["observed_minutes"], window)
        player_week[f"appearance_rate_{window}"] = _lagged_rolling_mean(grouped["observed_appearances"], window)
        player_week[f"played_60_rate_{window}"] = _lagged_rolling_mean(grouped["observed_played_60"], window)
    for window in [3, 5]:
        if os.environ.get("FPL_CLEAN_SHEET_FEATS", "0") == "1":
            player_week[f"clean_sheet_rate_{window}"] = _lagged_rolling_mean(grouped["observed_clean_sheets"], window)
            player_week[f"goals_conceded_avg_{window}"] = _lagged_rolling_mean(grouped["observed_goals_conceded"], window)
        player_week[f"bonus_avg_{window}"] = _lagged_rolling_mean(grouped["observed_bonus"], window)
        player_week[f"bps_avg_{window}"] = _lagged_rolling_mean(grouped["observed_bps"], window)
        player_week[f"influence_avg_{window}"] = _lagged_rolling_mean(grouped["observed_influence"], window)
        player_week[f"creativity_avg_{window}"] = _lagged_rolling_mean(grouped["observed_creativity"], window)
        player_week[f"threat_avg_{window}"] = _lagged_rolling_mean(grouped["observed_threat"], window)
        player_week[f"ict_index_avg_{window}"] = _lagged_rolling_mean(grouped["observed_ict_index"], window)
        player_week[f"starts_avg_{window}"] = _lagged_rolling_mean(grouped["observed_starts"], window)
        player_week[f"expected_goals_avg_{window}"] = _lagged_rolling_mean(
            grouped["observed_expected_goals"], window
        )
        player_week[f"expected_assists_avg_{window}"] = _lagged_rolling_mean(
            grouped["observed_expected_assists"], window
        )
        player_week[f"expected_goal_involvements_avg_{window}"] = _lagged_rolling_mean(
            grouped["observed_expected_goal_involvements"], window
        )
        player_week[f"expected_goals_conceded_avg_{window}"] = _lagged_rolling_mean(
            grouped["observed_expected_goals_conceded"], window
        )
        player_week[f"defensive_contribution_avg_{window}"] = _lagged_rolling_mean(
            grouped["observed_defensive_contribution"], window
        )
        player_week[f"defcon_hit_rate_{window}"] = _lagged_rolling_mean(
            grouped["observed_defcon_hits"], window
        )

    # F2b (FPL_PRIOR_BLEND=1): shrink early-season POINTS form toward the
    # player's prior-season per-week rate. One-game windows made GW2 2026-27
    # forecasts rank five one-week wonders above every premium (De Cuyper
    # £4.6 #1 DEF, Gabriel #29) and annihilate anyone who missed GW1.
    # Wes's constraint (2026-09-01): blend QUALITY ONLY — availability
    # features (appearance_rate/minutes/played_60) stay purely
    # current-season so genuinely injured players (Saliba/Timber) remain
    # floored via the unblended minutes model and official flags, and
    # re-rank instantly on return. w ramps over 6 played weeks, so
    # mid-season rows are untouched; players with no prior PL season keep
    # pure current form (no fabricated priors — deflates promoted-team
    # mirages by NOT inventing a pedigree, and leaves cold starts to the
    # walk-forward loop).
    if os.environ.get("FPL_PRIOR_BLEND", "0") == "1":
        season_mean = (
            player_week.groupby(["code", "season"], sort=False)["observed_points"]
            .mean()
            .rename("season_mean_points")
            .reset_index()
        )
        season_mean["season_year"] = season_mean["season"].map(parse_season_start_year)
        prior_lookup = {
            (row.code, row.season_year + 1): row.season_mean_points
            for row in season_mean.itertuples(index=False)
        }
        season_years = player_week["season"].map(parse_season_start_year)
        prior_rate = pd.Series(
            [prior_lookup.get((c, y)) for c, y in zip(player_week["code"], season_years)],
            index=player_week.index, dtype=float,
        )
        played_before = grouped["observed_appearances"].transform(
            lambda s: s.shift(1).fillna(0.0).cumsum()
        )
        blend_w = (played_before / 6.0).clip(0.0, 1.0).where(prior_rate.notna(), 1.0)
        for window in [1, 3, 5, 8]:
            column = f"points_avg_{window}"
            player_week[column] = blend_w * player_week[column].fillna(0.0) + (
                1.0 - blend_w
            ) * prior_rate.fillna(0.0)

    # A round's `value`/`selected` are the price and ownership at that round's
    # deadline, i.e. what the live builder reads from the current snapshot.
    # Lagging them a round would train on week-old market state while live
    # serves current state, and leaves blank-week players on stale ownership.
    player_week["price_pre_deadline"] = player_week["price"]
    player_week["selected_by_percent_pre_deadline"] = player_week["selected_by_percent"]
    player_week["transfers_in_prev_event"] = grouped["transfers_in_event"].shift(1)
    player_week["transfers_out_prev_event"] = grouped["transfers_out_event"].shift(1)
    player_week["transfer_balance_prev_event"] = (
        player_week["transfers_in_prev_event"] - player_week["transfers_out_prev_event"]
    )
    # The status/news stored on a round are the pre-deadline snapshot for that
    # round (the live-season backfill writes them that way; earlier seasons
    # are STATUS_UNKNOWN), so they describe this row and must not be shifted.
    player_week["status_pre_deadline"] = player_week["status"]
    player_week["news_pre_deadline"] = player_week["news"]
    player_week["price_change_1"] = (player_week["price"] - grouped["price"].shift(1)).fillna(0.0)
    player_week["selected_change_1"] = (
        player_week["selected_by_percent"] - grouped["selected_by_percent"].shift(1)
    ).fillna(0.0)
    player_week["home_fixture_ratio"] = player_week.apply(
        lambda row: 0.0 if row["fixture_count"] == 0 else row["home_fixture_count"] / row["fixture_count"],
        axis=1,
    )
    player_week["blank_gw"] = (player_week["fixture_count"] == 0).astype(float)
    player_week["double_gw"] = (player_week["fixture_count"] > 1).astype(float)
    status_text = player_week["status_pre_deadline"].fillna("a").astype(str).str.strip().str.lower()
    player_week["status_flag_pre_deadline"] = (~status_text.isin({"a", STATUS_UNKNOWN, "nan"})).astype(float)
    player_week["news_flag_pre_deadline"] = (
        player_week["news_pre_deadline"].fillna("").astype(str).str.len().gt(0).astype(float)
    )
    # FPL_CHANCE_FEAT=1 (2026-10-14): the official chance-of-playing percentage as a 0-1 feature, the
    # graded version of the binary status flag ("d" at 75% is not "i" at 0%); status letter fallback
    # when the snapshot did not record a percentage.
    if os.environ.get("FPL_CHANCE_FEAT", "0") == "1":
        player_week["chance_pre_deadline"] = chance_of_playing_feature(
            player_week["status_pre_deadline"], player_week.get("chance_of_playing")
        )
    # F15 (FPL_NEWS_HORIZON=1): "Expected back 11 Jan" / "Suspended until 04 Dec" -> how many of the next
    # 3 / 5 gameweeks are missed, for the multi-week heads that drive transfers.
    if os.environ.get("FPL_NEWS_HORIZON", "0") == "1":
        player_week = news_horizon.add_news_horizon(player_week)

    # F6 (FPL_OPPONENT_INTERACTION=1): price the opponent as an INTERACTION,
    # not an additive term. Diagnosed 2026-09-18 from the Evanilson-v-Liverpool
    # case Wes raised: the anchor gave opponent_goals_against_avg_3 a
    # standardized coefficient of +0.0041 (top feature: 0.4843) and
    # opponent_goals_against_avg_5 -0.0163 (WRONG SIGN), while leaning on the
    # subjective FDR integer (fixture_difficulty_mean, -0.4598). Measured on
    # 56,122 rows, real 1GW points swing 25-34% between the toughest and
    # leakiest opponent quartile; the forecast swung ~2%. A purely additive
    # term cannot express the effect because it is MULTIPLICATIVE: a 5-point
    # forward loses far more against Liverpool than a 2-point defender does.
    # So cross opponent weakness with the player's own attacking level.
    if os.environ.get("FPL_OPPONENT_INTERACTION", "0") == "1":
        for window in (3, 5):
            against = pd.to_numeric(
                player_week[f"opponent_goals_against_avg_{window}"], errors="coerce"
            )
            # Center on the league reference known at this deadline, so the
            # term is a deviation from a typical opponent without using any
            # later fixture (a full-season mean would leak the future).
            league_mean = _asof_league_reference(
                against, player_week["season"], player_week["week"], player_week["primary_opponent_team_id"]
            )
            weakness = (against - league_mean).fillna(0.0)
            player_week[f"opp_def_weakness_{window}"] = weakness
            player_week[f"form_x_opp_weakness_{window}"] = (
                pd.to_numeric(player_week[f"points_avg_{window}"], errors="coerce").fillna(0.0)
                * weakness
            )
            player_week[f"xgi_x_opp_weakness_{window}"] = (
                pd.to_numeric(
                    player_week[f"expected_goal_involvements_avg_{window}"], errors="coerce"
                ).fillna(0.0)
                * weakness
            )

    # F14 (FPL_MARKET_FEATS=1): cross the week's market expected goals / clean-sheet probability
    # with the player's own level, the multiplicative shape F6 showed the ridge needs.
    if market.enabled():
        player_week = market.add_interactions(player_week)

    # F9 (FPL_CONGESTION_FEATS=1): fixture congestion / European rotation.
    #
    # Diagnosed 2026-09-21. The anchor over-predicts £9.5m+ players by 1.094
    # pts/GW, in 6/6 windows across three seasons. The cause is isolated and
    # narrow: conditional on PLAYING 60+ the premium forecast is exact (bias
    # +0.010); the entire error sits in the 26.7% of weeks they don't play
    # (bias -4.119). Premiums start at 73.3% vs 72.5% for everyone else — the
    # SAME rate — but the forecast being lost is twice as large, so where the
    # two errors cancel for ordinary players they don't for premiums.
    #
    # And the anchor had 90 features and not one about rest, congestion or
    # European football, despite european_fixtures.jsonl sitting on disk and
    # already being rendered into the LLM prompts. Big clubs rotate after a
    # Thursday or midweek European tie, which is exactly when premiums sit.
    # This is a CAPTAINCY defect: we captain from that band and the multiplier
    # doubles the error.
    if os.environ.get("FPL_CONGESTION_FEATS", "0") == "1":
        euro_by_team = _load_european_fixtures(
            Path(os.environ.get("FPL_EURO_FIXTURES", "data/competition_fixtures/european_fixtures.jsonl"))
        )
        kickoff = pd.to_datetime(player_week["kickoff_time"], errors="coerce", utc=True)

        # Club's own PL match dates, to measure rest between league games.
        club_dates: Dict[Tuple[str, int], List[pd.Timestamp]] = {}
        for (season_key, team_key), group in player_week.groupby(["season", "team_id"], sort=False):
            stamps = pd.to_datetime(group["kickoff_time"], errors="coerce", utc=True).dropna().unique()
            club_dates[(str(season_key), int(team_key))] = sorted(pd.to_datetime(list(stamps)))

        euro_4d, euro_7d, rest_days, load_14d = [], [], [], []
        for season_key, team_key, when in zip(player_week["season"], player_week["team_id"], kickoff):
            key = (str(season_key), int(team_key) if pd.notna(team_key) else -1)
            if pd.isna(when):
                euro_4d.append(0.0); euro_7d.append(0.0); rest_days.append(7.0); load_14d.append(1.0)
                continue
            euro = euro_by_team.get(key, [])
            league = club_dates.get(key, [])
            prior_euro = [d for d in euro if d < when]
            all_prior = [d for d in league + euro if d < when]
            gap_euro = (when - prior_euro[-1]).total_seconds() / 86400.0 if prior_euro else 99.0
            euro_4d.append(1.0 if gap_euro <= 4.0 else 0.0)
            euro_7d.append(1.0 if gap_euro <= 7.0 else 0.0)
            rest_days.append(
                min((when - all_prior[-1]).total_seconds() / 86400.0, 21.0) if all_prior else 7.0
            )
            window_start = when - pd.Timedelta(days=14)
            load_14d.append(float(sum(1 for d in all_prior if d >= window_start)))

        player_week["euro_game_within_4d"] = euro_4d
        player_week["euro_game_within_7d"] = euro_7d
        player_week["days_rest_before_fixture"] = rest_days
        player_week["club_matches_last_14d"] = load_14d
        # The damage is multiplicative: congestion costs a nailed-on starter
        # far more expected points than a fringe player, so cross it with the
        # player's own recent workload (the F6 lesson).
        minutes_3 = pd.to_numeric(player_week["minutes_avg_3"], errors="coerce").fillna(0.0)
        player_week["euro_x_minutes_3"] = player_week["euro_game_within_4d"] * minutes_3
        player_week["load_x_minutes_3"] = player_week["club_matches_last_14d"] * minutes_3

    # F12 (FPL_TEAM_ATTACK_INTERACTION=1): the player's own team's attacking form.
    #
    # The only signal to survive BOTH halves of the 2026-09-23 attenuation
    # audit: the model carries ~0.44-0.45 of the real effect of
    # `team_goals_for_avg_5` on next-week points, in the marginal estimate AND
    # with player quality controlled out. (Most other rows of that audit are
    # artifacts — within-player slopes on autoregressive form features are
    # mechanically negative, so the audit only licenses conclusions about
    # signals the schedule assigns, not ones the player generates.)
    #
    # Same shape as F6: cross team attacking form with the player's own output,
    # because a team scoring freely is worth more to someone who plays and
    # attacks than to a fringe defender.
    if os.environ.get("FPL_TEAM_ATTACK_INTERACTION", "0") == "1":
        for window in (3, 5):
            team_attack = pd.to_numeric(player_week[f"team_goals_for_avg_{window}"], errors="coerce")
            league_attack = _asof_league_reference(
                team_attack, player_week["season"], player_week["week"], player_week["team_id"]
            )
            centred = (team_attack - league_attack).fillna(0.0)
            player_week[f"team_attack_strength_{window}"] = centred
            player_week[f"team_attack_x_xgi_{window}"] = centred * pd.to_numeric(
                player_week[f"expected_goal_involvements_avg_{window}"], errors="coerce"
            ).fillna(0.0)
            player_week[f"team_attack_x_minutes_{window}"] = centred * pd.to_numeric(
                player_week[f"minutes_avg_{window}"], errors="coerce"
            ).fillna(0.0)

    # F10 (FPL_FORM_VS_UNDERLYING=1): is the player's form running ahead of,
    # or behind, his underlying numbers?
    #
    # From the Brobbey case (GW5 2026-27): xGI/90 0.69, the best in his peer
    # group, but points of 2/2/2/1 — so the anchor, which tracks POINTS,
    # forecast him 2.19 the week he returned 17 on 2.39 xGI. Generalized over
    # three seasons the anchor over-rates players whose points outrun their
    # underlying and under-rates the reverse: bias −0.182 in the hot quintile
    # vs +0.121 in the due quintile, spread +0.228 pts/GW, positive in 5/6
    # windows.
    #
    # This is the RANK form of the idea that died as F8. F8 used a raw
    # goals-minus-xG difference and measured NULL; the difference is dominated
    # by scale, whereas the percentile gap is comparable across players. Ranks
    # are computed WITHIN each season-week so they never peek across time.
    if os.environ.get("FPL_FORM_VS_UNDERLYING", "0") == "1":
        for window in (3, 5):
            points = pd.to_numeric(player_week[f"points_avg_{window}"], errors="coerce")
            underlying = pd.to_numeric(
                player_week[f"expected_goal_involvements_avg_{window}"], errors="coerce"
            )
            grouped_week = [player_week["season"], player_week["week"]]
            points_rank = points.groupby(grouped_week).rank(pct=True)
            underlying_rank = underlying.groupby(grouped_week).rank(pct=True)
            gap = (underlying_rank - points_rank).fillna(0.0)
            player_week[f"form_vs_underlying_{window}"] = gap
            # Multiplicative, per the F6 lesson: being "due" is worth more to a
            # player who plays than to a fringe one.
            player_week[f"form_vs_underlying_x_minutes_{window}"] = gap * pd.to_numeric(
                player_week[f"minutes_avg_{window}"], errors="coerce"
            ).fillna(0.0)

    # F8 (FPL_FINISHING_REGRESSION=1): finishing luck, as a REGRESSION term.
    # From Wes's Calafiori/Mitchell challenge (2026-09-18): "his prediction is
    # high because in the past two weeks he scored a lot." Correct in
    # principle — form features are built on ACTUAL points, which embed
    # finishing that does not persist. Mitchell is the clean case: 4 goals in
    # 203 career appearances (0.020/app), then 2 in one match, which alone
    # carried his points_avg_3 to 4.49.
    #
    # goals - xG over a window is the standard estimator of that luck. It
    # should earn a NEGATIVE coefficient: having out-scored your chances
    # predicts giving it back, so it discounts exactly the players whose
    # recent points are least repeatable.
    if os.environ.get("FPL_FINISHING_REGRESSION", "0") == "1":
        for window in (3, 5):
            goals = _lagged_rolling_mean(grouped["observed_goals"], window)
            assists = _lagged_rolling_mean(grouped["observed_assists"], window)
            xg = pd.to_numeric(player_week[f"expected_goals_avg_{window}"], errors="coerce")
            xa = pd.to_numeric(player_week[f"expected_assists_avg_{window}"], errors="coerce")
            # xG/xA only exist from 2022-23; older rows read 0.0, which would
            # otherwise fabricate huge "overperformance" for every scorer.
            has_xg = pd.to_numeric(
                player_week["expected_data_source_available"], errors="coerce"
            ).fillna(0.0) > 0
            player_week[f"goals_over_xg_{window}"] = (
                (goals - xg).where(has_xg, 0.0).fillna(0.0)
            )
            player_week[f"assists_over_xa_{window}"] = (
                (assists - xa).where(has_xg, 0.0).fillna(0.0)
            )
            player_week[f"involvement_over_expected_{window}"] = (
                player_week[f"goals_over_xg_{window}"]
                + player_week[f"assists_over_xa_{window}"]
            )

    # F7 (FPL_DEPTH_CHART=1): positional depth-chart context. Diagnosed
    # 2026-09-18 from the Konsa case Wes raised: Konsa carried P(app) 0.74 as
    # a cold-start artifact while Saliba sat at status="i", chance 0, "Back
    # injury - Unknown return date". Nothing in the player's OWN history can
    # express "the man ahead of me is out" — and the text channel cannot
    # either, because evidence windows are mention-centered, so an article
    # about Saliba attaches to Saliba's prompt, never Konsa's. The signal is
    # already structured in the official feed; it just was never joined.
    # NOTE: this is why the four earlier regex team-context attempts failed —
    # they tried to recover from prose something that ships as a status field.
    if os.environ.get("FPL_DEPTH_CHART", "0") == "1":
        unit = [player_week["season"], player_week["week"], player_week["team_id"], player_week["position"]]
        minutes3 = pd.to_numeric(player_week["minutes_avg_3"], errors="coerce").fillna(0.0)
        unavailable = player_week["status_flag_pre_deadline"].fillna(0.0)

        unit_minutes = minutes3.groupby(unit).transform("sum")
        # Share of his team's minutes at his own position: ~1.0 for a nailed
        # starter in a thin unit, low for a squad player behind two others.
        player_week["pos_minutes_share_3"] = (
            minutes3 / unit_minutes.where(unit_minutes > 0)
        ).fillna(0.0)
        # How many same-position team-mates are flagged out, and how many
        # minutes those absences vacate. Saliba out => Konsa's rivals_out
        # rises and vacated_minutes jumps, which is the promotion signal.
        player_week["pos_rivals_unavailable"] = (
            unavailable.groupby(unit).transform("sum") - unavailable
        ).clip(lower=0.0)
        player_week["pos_rivals_minutes_vacated_3"] = (
            (minutes3 * unavailable).groupby(unit).transform("sum") - minutes3 * unavailable
        ).clip(lower=0.0)
        player_week["pos_unit_size"] = (
            pd.Series(1.0, index=player_week.index).groupby(unit).transform("sum")
        )

    for column in [
        "team_goals_for_avg_3",
        "team_goals_against_avg_3",
        "team_goals_for_avg_5",
        "team_goals_against_avg_5",
        "opponent_goals_for_avg_3",
        "opponent_goals_against_avg_3",
        "opponent_goals_for_avg_5",
        "opponent_goals_against_avg_5",
        "bonus_avg_3",
        "bonus_avg_5",
        "bps_avg_3",
        "bps_avg_5",
        "influence_avg_3",
        "influence_avg_5",
        "creativity_avg_3",
        "creativity_avg_5",
        "threat_avg_3",
        "threat_avg_5",
        "ict_index_avg_3",
        "ict_index_avg_5",
        "starts_avg_3",
        "starts_avg_5",
        "expected_goals_avg_3",
        "expected_goals_avg_5",
        "expected_assists_avg_3",
        "expected_assists_avg_5",
        "expected_goal_involvements_avg_3",
        "expected_goal_involvements_avg_5",
        "expected_goals_conceded_avg_3",
        "expected_goals_conceded_avg_5",
        "defensive_contribution_avg_3",
        "defensive_contribution_avg_5",
        "defcon_hit_rate_3",
        "defcon_hit_rate_5",
        "expected_data_source_available",
        "defensive_data_source_available",
    ]:
        player_week[column] = pd.to_numeric(player_week[column], errors="coerce").fillna(0.0)

    player_week["label_points_1gw"] = player_week["observed_points"]
    player_week["label_minutes_1gw"] = player_week["observed_minutes"]
    player_week["label_appearance_probability"] = (player_week["observed_minutes"] > 0).astype(float)
    # Multi-week labels are forward sums, which TRUNCATE at each season's
    # end: the last ~4 weeks of every season carry artificially tiny
    # 3GW/5GW labels (league mean label_points_5gw decays 5.10 -> 1.05
    # over weeks 34-38; e.g. Gabriel's week-38 "5gw" label was 1 despite a
    # 26-point real 5-week run into it). That's ~13% of rows teaching
    # "high features -> tiny multi-week target", which attenuates the
    # 3GW/5GW regression heads — measured: corr(real last-season PPG,
    # baseline_5gw/5) was 0.20 vs 0.43 for the 1GW head, deflating elite
    # players ~2x. Fix (Wes chose keep-all-rows over dropping the tail,
    # 2026-08-21): scale each partial-horizon sum up to its full-horizon
    # RATE-EQUIVALENT using the actual number of rows in the forward
    # window, so week-37's 2-week sum becomes a 5-week-rate label rather
    # than a lie. Tail rows get noisier labels (fewer weeks extrapolated),
    # which regression tolerates; biased labels it does not.
    ones = pd.Series(1.0, index=player_week.index)
    weeks_in_3gw_window = grouped["observed_points"].transform(lambda series: _forward_rolling_sum(ones.loc[series.index], 3))
    weeks_in_5gw_window = grouped["observed_points"].transform(lambda series: _forward_rolling_sum(ones.loc[series.index], 5))
    raw_3gw = grouped["observed_points"].transform(lambda series: _forward_rolling_sum(series, 3))
    raw_5gw = grouped["observed_points"].transform(lambda series: _forward_rolling_sum(series, 5))
    player_week["label_points_3gw"] = raw_3gw * (3.0 / weeks_in_3gw_window.clip(lower=1.0))
    player_week["label_points_5gw"] = raw_5gw * (5.0 / weeks_in_5gw_window.clip(lower=1.0))
    # Fixtures in the same forward windows, scaled the same way (2026-10-13, double-gameweek pricing):
    # the schedule is published ahead, so these are pre-deadline multipliers for per-fixture horizon
    # heads (FPL_PER_FIXTURE=1): label_points_3gw / fixtures_next_3 is points per fixture, and the
    # forecast multiplies back by the fixtures actually ahead. All singles = 3.0 / 5.0.
    fixture_counts = pd.to_numeric(player_week["fixture_count"], errors="coerce").fillna(0.0)
    fixtures_in_3 = grouped["observed_points"].transform(lambda series: _forward_rolling_sum(fixture_counts.loc[series.index], 3))
    fixtures_in_5 = grouped["observed_points"].transform(lambda series: _forward_rolling_sum(fixture_counts.loc[series.index], 5))
    player_week["fixtures_next_3"] = fixtures_in_3 * (3.0 / weeks_in_3gw_window.clip(lower=1.0))
    player_week["fixtures_next_5"] = fixtures_in_5 * (5.0 / weeks_in_5gw_window.clip(lower=1.0))
    # 8GW horizon (Wes-approved assessment, 2026-08-21 option-3 scope):
    # same rate-normalized construction so season-tail truncation cannot
    # attenuate the long head the way it did the pre-fix 5GW labels.
    weeks_in_8gw_window = grouped["observed_points"].transform(
        lambda series: _forward_rolling_sum(ones.loc[series.index], 8)
    )
    raw_8gw = grouped["observed_points"].transform(lambda series: _forward_rolling_sum(series, 8))
    player_week["label_points_8gw"] = raw_8gw * (8.0 / weeks_in_8gw_window.clip(lower=1.0))

    eligibilities = player_week.apply(
        lambda row: asdict(get_week_eligibility(str(row["season"]), int(row["week"]))),
        axis=1,
        result_type="expand",
    )
    player_week["eligible_for_training"] = eligibilities["eligible_for_training"]
    player_week["eligible_for_backtest"] = eligibilities["eligible_for_backtest"]
    player_week["eligibility_reason"] = eligibilities["reason"]

    numeric_columns = [
        column
        for column in player_week.columns
        if column not in {"season", "player_name", "position", "status", "news", "kickoff_time", "eligibility_reason"}
    ]
    for column in numeric_columns:
        if player_week[column].dtype == object:
            converted = pd.to_numeric(player_week[column], errors="coerce")
            if converted.notna().any():
                player_week[column] = converted.fillna(0.0)

    player_week = add_regime_columns(player_week)  # item 1 (FPL_REGIME_TERM), no-op when off

    for column in SAFE_FEATURE_COLUMNS:
        # Flag-gated features (e.g. the F5 clean-sheet set) are absent unless
        # their env var is set; get_feature_columns already filters to what
        # exists, so simply skip missing columns here.
        if column not in player_week.columns:
            continue
        player_week[column] = pd.to_numeric(player_week[column], errors="coerce").fillna(0.0)
    return player_week.sort_values(["season", "week", "player_id"]).reset_index(drop=True)


def get_feature_columns(training_frame: pd.DataFrame) -> List[str]:
    columns = [column for column in SAFE_FEATURE_COLUMNS if column in training_frame.columns]
    # F16: the team-news categories only when asked for, so the same table serves as the exact control.
    if os.environ.get("FPL_TEAM_NEWS_FEATS", "0") != "1":
        columns = [column for column in columns if not column.startswith("gn_")]
    # Extracted availability facts (2026-10-22) only when asked for, same reason.
    if os.environ.get("FPL_EXTRACT_FEATS", "0") != "1":
        columns = [column for column in columns if not column.startswith("ex_")]
    # F19 (2026-10-31): team-level baselines only when asked for, so the _teamlevel table doubles as its own control.
    if os.environ.get("FPL_TEAM_LEVEL_FEATS", "0") != "1":
        columns = [column for column in columns if not column.startswith("tl_")]
    # F14 ablation: FPL_MARKET_BASE_ONLY=1 drops the market crosses and keeps the base numbers.
    if os.environ.get("FPL_MARKET_BASE_ONLY", "0") == "1":
        columns = [column for column in columns if column not in market.INTERACTION_FEATURES]
    # F14 ablation: FPL_MARKET_REPLACE_FDR=1 lets the market stand in for the subjective FPL
    # difficulty rating (the anchor's main fixture term before F6) instead of sitting beside it.
    if os.environ.get("FPL_MARKET_REPLACE_FDR", "0") == "1":
        columns = [column for column in columns if column not in ("fixture_difficulty_mean", "fixture_difficulty_min")]
    return columns


def _attach_live_team_news(live_frame: pd.DataFrame, path: str) -> pd.DataFrame:
    """F16 live (2026-10-28): the Guardian predicted-lineups categories for the week being forecast, as written by
    scripts/live_team_news.py (keys "season|week|player_id" -> XI | sub | doubtful | injured | suspended), mapped onto
    the gn_* columns exactly as scripts/build_team_news_table.py does for training rows. A missing file, an empty
    file (no article yet) or a player whose team the article did not cover is the "no article" state (gn_article 0),
    which is what 30% of training team-weeks carry, so the forecast degrades to the no-news model, never to garbage."""
    import json as _json
    from pathlib import Path as _Path

    try:
        feat = _json.loads(_Path(path).read_text())
    except (OSError, ValueError):
        feat = {}
    season = str(live_frame["season"].mode().iloc[0])
    week = int(pd.to_numeric(live_frame["week"], errors="coerce").mode().iloc[0])
    ids = pd.to_numeric(live_frame["player_id"], errors="coerce")
    cat = ids.map(lambda p: None if pd.isna(p) else feat.get(f"{season}|{week}|{int(p)}"))
    live_frame = live_frame.copy()
    live_frame["gn_article"] = cat.notna().astype(float)
    live_frame["gn_xi"] = (cat == "XI").astype(float)
    live_frame["gn_sub"] = (cat == "sub").astype(float)
    live_frame["gn_doubtful"] = (cat == "doubtful").astype(float)
    live_frame["gn_out"] = ((cat == "injured") | (cat == "suspended")).astype(float)
    counts = cat.value_counts().to_dict()
    print(f"live frame: team-news categories for {int(cat.notna().sum())}/{len(live_frame)} players "
          f"({season} week {week}) from {path}: {counts}")
    return live_frame


class CanonicalDataset:
    """High-level accessors around a canonical training frame."""

    def __init__(self, training_frame: pd.DataFrame):
        self.training_frame = add_regime_columns(training_frame.copy())  # item 1 (FPL_REGIME_TERM), no-op when off
        self.feature_columns = get_feature_columns(self.training_frame)

    @classmethod
    def from_history_root(cls, history_root: Union[str, Path]) -> "CanonicalDataset":
        raw_history = normalize_vaastav_history(history_root)
        training_frame = build_training_frame(raw_history)
        return cls(training_frame)

    def to_csv(self, output_path: Union[str, Path]) -> None:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        self.training_frame.to_csv(output_path, index=False)

    @classmethod
    def from_csv(cls, training_csv: Union[str, Path]) -> "CanonicalDataset":
        frame = pd.read_csv(training_csv, low_memory=False)
        # 2021-22 GW37 labels 80 goalkeepers "GKP" (source quirk): no legal XI that week (found 2026-10-10).
        if "position" in frame.columns:
            frame["position"] = frame["position"].replace({"GKP": "GK"})
        return cls(frame)

    def week_frame(self, week_id: WeekId) -> pd.DataFrame:
        season, week = parse_week_id(week_id)
        mask = (self.training_frame["season"] == season) & (self.training_frame["week"] == week)
        return self.training_frame.loc[mask].copy().reset_index(drop=True)

    def build_player_rows(self, week_id: WeekId) -> List[PlayerWeekRow]:
        week_frame = self.week_frame(week_id)
        rows = []
        for record in week_frame.to_dict(orient="records"):
            feature_values = {column: float(record.get(column, 0.0) or 0.0) for column in self.feature_columns}
            rows.append(
                PlayerWeekRow(
                    season=str(record["season"]),
                    week=int(record["week"]),
                    player_id=int(record["player_id"]),
                    player_name=str(record["player_name"]),
                    team_id=int(record["team_id"]),
                    position=str(record["position"]),
                    features=feature_values,
                )
            )
        return rows

    def build_labels(self, week_id: WeekId, horizons: Sequence[int] = (1, 3, 5)) -> List[PlayerWeekLabel]:
        del horizons  # The dataclass exposes fixed v1 horizons.
        week_frame = self.week_frame(week_id)
        labels = []
        for record in week_frame.to_dict(orient="records"):
            labels.append(
                PlayerWeekLabel(
                    season=str(record["season"]),
                    week=int(record["week"]),
                    player_id=int(record["player_id"]),
                    next_gw_points=float(record["label_points_1gw"]),
                    next_3gw_points=float(record["label_points_3gw"]),
                    next_5gw_points=float(record["label_points_5gw"]),
                    next_gw_minutes=float(record["label_minutes_1gw"]),
                    next_gw_appearance_probability=float(record["label_appearance_probability"]),
                )
            )
        return labels

    def get_week_eligibility(self, week_id: WeekId) -> WeekEligibility:
        season, week = parse_week_id(week_id)
        return get_week_eligibility(season, week)

    def build_week_state(self, week_id: WeekId) -> WeekState:
        season, week = parse_week_id(week_id)
        week_frame = self.week_frame(week_id)
        eligibility = self.get_week_eligibility(week_id)
        kickoff_values = week_frame["kickoff_time"].dropna().astype(str)
        first_kickoff = kickoff_values.min() if not kickoff_values.empty else ""
        kickoff_ts = pd.to_datetime(first_kickoff, utc=True, errors="coerce") if first_kickoff else None
        deadline_ts = ""
        if kickoff_ts is not None and not pd.isna(kickoff_ts):
            deadline_ts = (kickoff_ts - pd.Timedelta(minutes=90)).isoformat()
        notes = [eligibility.reason]
        if (week_frame["blank_gw"] > 0).any():
            notes.append("Contains players with blank gameweeks.")
        if (week_frame["double_gw"] > 0).any():
            notes.append("Contains players with double gameweeks.")
        return WeekState(
            season=season,
            week=week,
            deadline_ts=deadline_ts,
            eligible=eligibility,
            fixture_count=int(week_frame["fixture_count"].sum()),
            player_count=int(len(week_frame)),
            notes=notes,
            source_timestamps={"historical_training_frame": deadline_ts or "unknown"},
        )

    def _build_next_week_form_features(
        self, history_root: Union[str, Path], live_season: str, next_week: int
    ) -> Optional[pd.DataFrame]:
        """Walk-forward form features for the live week, by construction.

        Once the live season has played weeks in the history, the tail(1)
        join below goes stale: a GW k row's own lagged features describe the
        state BEFORE week k (for GW1 rows that is the season-boundary cold
        start — near-zero rollings), not the state after it. The correct
        live features are exactly what a training-table row for week k+1
        would carry, so build one: append a synthetic week-(k+1) row per
        player (identity + real next-week fixture, match stats blank — they
        are only ever consumed through shift(1)) to the live season's raw
        rows and run the ordinary feature pipeline over that slice
        (features are season-scoped, so other seasons are not needed).
        """
        raw = normalize_vaastav_history(history_root)
        current = raw.loc[raw["season"] == live_season].copy()
        if current.empty:
            return None
        synthetic = current.sort_values("week").groupby("code", as_index=False).tail(1).copy()
        identity_columns = {
            "season", "week", "player_id", "code", "player_name", "team_id",
            "position", "price", "selected_by_percent", "status", "news",
            "kickoff_time", "defensive_data_source_available",
            "expected_data_source_available",
        }
        for column in synthetic.columns:
            if column in identity_columns:
                continue
            if pd.api.types.is_numeric_dtype(synthetic[column]):
                synthetic[column] = float("nan")
            else:
                synthetic[column] = ""
        synthetic["week"] = next_week

        fixtures_path = Path(history_root) / live_season / "fixtures.csv"
        if fixtures_path.exists():
            fixtures = pd.read_csv(fixtures_path)
            fixtures = fixtures.loc[pd.to_numeric(fixtures["event"], errors="coerce") == next_week]
            opponent_map: Dict[int, Tuple[int, bool, float]] = {}
            for row in fixtures.itertuples():
                opponent_map[int(row.team_h)] = (int(row.team_a), True, float(row.team_h_difficulty))
                opponent_map[int(row.team_a)] = (int(row.team_h), False, float(row.team_a_difficulty))
            synthetic["opponent_team_id"] = synthetic["team_id"].map(
                lambda team_id: opponent_map.get(int(team_id), (-1, True, float("nan")))[0]
            )
            synthetic["was_home"] = synthetic["team_id"].map(
                lambda team_id: opponent_map.get(int(team_id), (-1, True, float("nan")))[1]
            )
            synthetic["fixture_difficulty"] = synthetic["team_id"].map(
                lambda team_id: opponent_map.get(int(team_id), (-1, True, float("nan")))[2]
            )

        # The previous season must be present too: the F2b prior blend looks up
        # each player's prior-season rate, and without it the live features
        # silently differ from the table the model was fitted on. Rolling
        # features are season-scoped, so nothing else changes.
        start_year = parse_season_start_year(live_season)
        previous_season = f"{start_year - 1}-{str(start_year)[2:]}"
        previous = raw.loc[raw["season"] == previous_season]
        combined = pd.concat([previous, current, synthetic], ignore_index=True)
        built = build_training_frame(combined)
        return built.loc[(built["season"].astype(str) == live_season) & (built["week"] == next_week)].copy()

    # Feature columns whose live values come from the official snapshot (or
    # the raw _hist columns) inside build_live_week_frame itself — the
    # walk-forward override below must not touch them.
    _LIVE_OWNED_FEATURES = {
        "price_pre_deadline", "selected_by_percent_pre_deadline",
        "transfers_in_prev_event", "transfers_out_prev_event",
        "transfer_balance_prev_event", "primary_opponent_team_id",
        "home_fixture_count", "away_fixture_count", "fixture_count",
        "fixture_difficulty_mean", "fixture_difficulty_min",
        "price_change_1", "selected_change_1", "home_fixture_ratio",
        "blank_gw", "double_gw", "status_flag_pre_deadline",
        "news_flag_pre_deadline", "fixtures_next_3", "fixtures_next_5", "chance_pre_deadline",
        *news_horizon.FEATURES,
        # F14 base market numbers come from the live fixture odds (api.py); the crosses are
        # recomputed at the end of build_live_week_frame from the walk-forward form.
        *market.BASE_FEATURES,
    }

    def build_live_week_frame(
        self,
        official_week_frame: pd.DataFrame,
        history_root: Union[str, Path, None] = None,
    ) -> pd.DataFrame:
        if official_week_frame.empty:
            return official_week_frame.copy()

        # FPL's numeric player_id ("element") is NOT stable across a season
        # boundary -- it gets reassigned (found 2026-08-12 building a live
        # GW1 2026-27 squad: live id 411 was "Haaland", but in the 2025-26
        # training data id 411 belonged to a different real player,
        # "Nico O'Reilly"; Haaland's own 2025-26 history lived under id
        # 430). "code" is FPL's genuinely stable per-person identifier and
        # is present on both the live snapshot and the historical frame
        # once normalize_vaastav_history has run. Prefer it; fall back to
        # player_id (old behavior) only when code isn't available on both
        # sides -- e.g. hand-built synthetic frames in tests that model a
        # single season's own mid-season live update, where player_id
        # continuity is a valid assumption.
        has_code = "code" in official_week_frame.columns and "code" in self.training_frame.columns
        join_key = "code" if has_code and (official_week_frame["code"] > 0).any() else "player_id"

        history = (
            self.training_frame.sort_values(["season", "week"])
            .groupby(join_key, as_index=False)
            .tail(1)
            .rename(columns={column: f"{column}_hist" for column in self.training_frame.columns if column != join_key})
        )
        live_frame = official_week_frame.copy().merge(history, on=join_key, how="left")

        for column in ["season", "week", "player_name", "team_id", "position"]:
            historical = f"{column}_hist"
            if column not in live_frame.columns:
                live_frame[column] = live_frame.get(historical, "")
            else:
                live_frame[column] = live_frame[column].fillna(live_frame.get(historical))

        current_numeric_overrides = ["price", "selected_by_percent", "fixture_count", "fixture_difficulty_mean", "home_fixture_count", "away_fixture_count"]
        for column in current_numeric_overrides:
            historical = f"{column}_hist"
            if column in live_frame.columns:
                live_frame[column] = pd.to_numeric(live_frame[column], errors="coerce").fillna(
                    pd.to_numeric(live_frame.get(historical), errors="coerce").fillna(0.0)
                )
            else:
                live_frame[column] = pd.to_numeric(live_frame.get(historical), errors="coerce").fillna(0.0)

        # Batch changes are within-season (a season's first round has change 0),
        # so a last row from an earlier season, or no row at all, is no change.
        last_row_season = live_frame.get("season_hist", pd.Series("", index=live_frame.index))
        same_season = last_row_season.astype(str).eq(live_frame["season"].astype(str))
        previous_price = pd.to_numeric(live_frame.get("price_hist"), errors="coerce").where(same_season)
        previous_selected = pd.to_numeric(live_frame.get("selected_by_percent_hist"), errors="coerce").where(same_season)
        live_frame["price_pre_deadline"] = live_frame["price"]
        live_frame["selected_by_percent_pre_deadline"] = live_frame["selected_by_percent"]
        live_frame["price_change_1"] = (live_frame["price_pre_deadline"] - previous_price).fillna(0.0)
        live_frame["selected_change_1"] = (live_frame["selected_by_percent_pre_deadline"] - previous_selected).fillna(0.0)
        live_frame["transfers_in_prev_event"] = pd.to_numeric(
            live_frame.get("transfers_in_event_hist"), errors="coerce"
        ).fillna(pd.to_numeric(live_frame.get("transfers_in_prev_event_hist"), errors="coerce").fillna(0.0))
        live_frame["transfers_out_prev_event"] = pd.to_numeric(
            live_frame.get("transfers_out_event_hist"), errors="coerce"
        ).fillna(pd.to_numeric(live_frame.get("transfers_out_prev_event_hist"), errors="coerce").fillna(0.0))
        live_frame["transfer_balance_prev_event"] = (
            live_frame["transfers_in_prev_event"] - live_frame["transfers_out_prev_event"]
        )
        live_frame["fixture_difficulty_min"] = live_frame["fixture_difficulty_mean"]
        live_frame["blank_gw"] = (live_frame["fixture_count"] == 0).astype(float)
        live_frame["double_gw"] = (live_frame["fixture_count"] > 1).astype(float)
        # Forward fixture counts come from the live fixture list (api.py); a snapshot without them
        # assumes single fixtures every week rather than inheriting a historical row's schedule.
        for column, default in (("fixtures_next_3", 3.0), ("fixtures_next_5", 5.0)):
            if column in live_frame.columns:
                live_frame[column] = pd.to_numeric(live_frame[column], errors="coerce").fillna(default)
            else:
                live_frame[column] = default
        live_frame["home_fixture_ratio"] = live_frame.apply(
            lambda row: 0.0 if row["fixture_count"] == 0 else row["home_fixture_count"] / row["fixture_count"],
            axis=1,
        )
        if "status" not in live_frame.columns:
            live_frame["status"] = "a"
        live_frame["status"] = live_frame["status"].fillna("a")
        if "news" not in live_frame.columns:
            live_frame["news"] = ""
        live_frame["news"] = live_frame["news"].fillna("")
        live_frame["status_flag_pre_deadline"] = live_frame["status"].astype(str).str.lower().ne("a").astype(float)
        live_frame["news_flag_pre_deadline"] = live_frame["news"].astype(str).str.len().gt(0).astype(float)
        if "chance_pre_deadline" in self.training_frame.columns:
            live_frame["chance_pre_deadline"] = chance_of_playing_feature(live_frame["status"], live_frame.get("chance_of_playing"))
        if "primary_opponent_team_id" not in live_frame.columns:
            live_frame["primary_opponent_team_id"] = -1

        live_frame["eligible_for_training"] = False
        live_frame["eligible_for_backtest"] = False
        live_frame["eligibility_reason"] = "Live official snapshot."
        if "kickoff_time" not in live_frame.columns:
            live_frame["kickoff_time"] = ""
        live_frame["kickoff_time"] = live_frame["kickoff_time"].fillna("")

        for label_column in LABEL_COLUMNS:
            live_frame[label_column] = 0.0
        for feature_column in SAFE_FEATURE_COLUMNS:
            historical = f"{feature_column}_hist"
            if feature_column not in live_frame.columns:
                if historical not in live_frame.columns:
                    # Flag-gated feature (F5 clean-sheet set) absent from both
                    # the live snapshot and the training join: leave it out so
                    # get_feature_columns keeps live and train consistent.
                    continue
                live_frame[feature_column] = pd.to_numeric(live_frame[historical], errors="coerce").fillna(0.0)
            else:
                live_frame[feature_column] = pd.to_numeric(live_frame[feature_column], errors="coerce").fillna(
                    pd.to_numeric(live_frame.get(historical), errors="coerce").fillna(0.0)
                )
        for column in self.training_frame.columns:
            if column not in live_frame.columns:
                if pd.api.types.is_numeric_dtype(self.training_frame[column]):
                    live_frame[column] = 0.0
                else:
                    live_frame[column] = ""

        # Walk-forward form override (see _build_next_week_form_features):
        # once the live season has completed weeks, recompute the rolling
        # form/team features through the real pipeline instead of carrying
        # the stale lagged features of each player's last played row.
        if history_root is not None and "code" in live_frame.columns:
            live_season = str(live_frame["season"].mode().iloc[0])
            next_week = int(pd.to_numeric(live_frame["week"], errors="coerce").mode().iloc[0])
            synthetic = self._build_next_week_form_features(history_root, live_season, next_week)
            if synthetic is not None and not synthetic.empty and "code" in synthetic.columns:
                form_columns = [
                    column
                    for column in SAFE_FEATURE_COLUMNS
                    if column in synthetic.columns
                    and column in live_frame.columns
                    and column not in self._LIVE_OWNED_FEATURES
                ]
                form = synthetic.set_index("code")[form_columns]
                overridden = 0
                codes = pd.to_numeric(live_frame["code"], errors="coerce")
                for index, code in codes.items():
                    if pd.isna(code) or int(code) not in form.index:
                        continue
                    values = form.loc[int(code)]
                    for column in form_columns:
                        value = values[column]
                        if pd.notna(value):
                            live_frame.at[index, column] = float(value)
                    overridden += 1
                print(
                    f"live frame: walk-forward form for {overridden}/{len(live_frame)} players "
                    f"({live_season} thru week {next_week - 1}); rest use last-row fallback"
                )
        if market.enabled() and all(column in live_frame.columns for column in market.BASE_FEATURES):
            live_frame = market.add_interactions(live_frame)
        # F16 live (2026-10-28): attach this week's Guardian lineup categories when the training table carries the
        # gn_* columns (the _teamnews variant) and FPL_TEAM_NEWS_LIVE_JSON names the live categories file.
        live_team_news = os.environ.get("FPL_TEAM_NEWS_LIVE_JSON")
        if live_team_news and "gn_article" in self.training_frame.columns:
            live_frame = _attach_live_team_news(live_frame, live_team_news)
        return live_frame[self.training_frame.columns].copy()
