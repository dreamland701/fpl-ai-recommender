#!/usr/bin/env python3
"""Congestion residual study (2026-10-29, Wes's Justin v N.Williams question: Bournemouth and Brentford both played
Carabao Cup ties on the Wednesday before GW9). Domestic cup schedules are not on disk, so this uses the European
fixture file (UCL/UEL/UECL 2022-) as the midweek-game proxy: a Thursday Europa tie before a Sunday PL game is a harder
version of a Wednesday cup tie before Saturday. For every table row from 2022-23 on, flag whether the player's OWN team
and the OPPONENT played in Europe within 4 days before the PL kickoff (and within 3 days after it), then measure what
the stored walk-forward classic forecast (E20 corpora, top-256 per week) missed: realised minus forecast points and
minutes by group and position, plus the raw clean-sheet and goals-conceded rates for every defender and keeper who
played 60+, controlled by the opponent's attacking-form quartile and restricted to European-club opponents (same clubs,
with and without a midweek game). If the opponent-congestion residual is ~0, an opponent's midweek game is not an
opportunity for the model. F9 (own-team congestion as ridge features) was measured null in September.
usage: PYTHONPATH=src python3 scripts/congestion_residual_study.py [out.md]"""
from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from fpl_ai.dataset import _load_european_fixtures  # noqa: E402

_ns: dict = {"ROOT": str(ROOT)}
for node in ast.parse((ROOT / "scripts/minutes_prior_study.py").read_text()).body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") in ("FILES", "SEASONS"):
        exec(compile(ast.Module(body=[node], type_ignores=[]), "x", "exec"), _ns)
FILES = _ns["FILES"]
SEASONS = [s for s in _ns["SEASONS"] if s >= "2022-23"]
BEFORE_DAYS, AFTER_DAYS = 4.0, 3.0


def se2(x) -> float:
    x = np.asarray(x, dtype=float)
    return 2 * x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else float("nan")


def cell(x) -> str:
    x = np.asarray(x, dtype=float)
    return f"{x.mean():+.2f} ±{se2(x):.2f} (n {len(x):,})" if len(x) else "—"


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "reports/gw9_packet_2026_10/congestion_residual_study.md"
    cols = ["season", "week", "player_id", "team_id", "position", "primary_opponent_team_id", "kickoff_time", "fixture_count",
            "home_fixture_count", "observed_minutes", "observed_clean_sheets", "observed_goals_conceded", "label_points_1gw",
            "opponent_goals_for_avg_5"]
    t = pd.read_csv(ROOT / "data/fpl_training_rows_v3_contract_f6.csv", low_memory=False, usecols=cols)
    t = t[t["season"].isin(SEASONS) & (pd.to_numeric(t["fixture_count"], errors="coerce") == 1)].copy()
    t["kick"] = pd.to_datetime(t["kickoff_time"], errors="coerce", utc=True)
    t = t[t["kick"].notna() & t["primary_opponent_team_id"].notna()].copy()
    t["opp"] = t["primary_opponent_team_id"].astype(int)
    if pd.api.types.is_numeric_dtype(t["position"]):
        t["position"] = t["position"].map({1: "GK", 2: "DEF", 3: "MID", 4: "FWD"})
    euro = _load_european_fixtures(ROOT / "data/competition_fixtures/european_fixtures.jsonl")
    euro_clubs = {k for k in euro}

    def gaps(season: str, team: int, when: pd.Timestamp) -> tuple[float, float]:
        dates = euro.get((season, team), [])
        before = [d for d in dates if d < when]
        after = [d for d in dates if d > when]
        gb = (when - before[-1]).total_seconds() / 86400.0 if before else 99.0
        ga = (after[0] - when).total_seconds() / 86400.0 if after else 99.0
        return gb, ga

    combos = t[["season", "team_id", "kick"]].drop_duplicates()
    own = {(s, int(tm), k): gaps(s, int(tm), k) for s, tm, k in combos.itertuples(index=False)}
    combos_o = t[["season", "opp", "kick"]].drop_duplicates()
    opp = {(s, int(tm), k): gaps(s, int(tm), k) for s, tm, k in combos_o.itertuples(index=False)}
    t["own_gb"] = [own[(s, int(tm), k)][0] for s, tm, k in zip(t["season"], t["team_id"], t["kick"])]
    t["own_ga"] = [own[(s, int(tm), k)][1] for s, tm, k in zip(t["season"], t["team_id"], t["kick"])]
    t["opp_gb"] = [opp[(s, int(tm), k)][0] for s, tm, k in zip(t["season"], t["opp"], t["kick"])]
    t["opp_ga"] = [opp[(s, int(tm), k)][1] for s, tm, k in zip(t["season"], t["opp"], t["kick"])]
    t["own_before"] = t["own_gb"] <= BEFORE_DAYS
    t["opp_before"] = t["opp_gb"] <= BEFORE_DAYS
    t["own_after"] = t["own_ga"] <= AFTER_DAYS
    t["opp_after"] = t["opp_ga"] <= AFTER_DAYS
    t["own_euro_club"] = [(s, int(tm)) in euro_clubs for s, tm in zip(t["season"], t["team_id"])]
    t["opp_euro_club"] = [(s, int(tm)) in euro_clubs for s, tm in zip(t["season"], t["opp"])]

    fc = {}
    for path in FILES:
        for line in open(path):
            r = json.loads(line); m = r["metadata"]; b = m["baseline_forecast"]
            fc[(m["season"], int(r["week"]), int(m["player_id"]))] = (float(b["baseline_points_1gw"]), float(b["baseline_minutes_1gw"]),
                                                                       float(b["baseline_appearance_probability"]))
    key = list(zip(t["season"], t["week"].astype(int), t["player_id"].astype(int)))
    t["b_pts"] = [fc.get(k, (np.nan,) * 3)[0] for k in key]
    t["b_min"] = [fc.get(k, (np.nan,) * 3)[1] for k in key]
    t["b_app"] = [fc.get(k, (np.nan,) * 3)[2] for k in key]
    t["pts"] = pd.to_numeric(t["label_points_1gw"], errors="coerce")
    t["mins"] = pd.to_numeric(t["observed_minutes"], errors="coerce")
    t["res_pts"] = t["pts"] - t["b_pts"]
    t["res_min"] = t["mins"] - t["b_min"]
    t["res_app"] = (t["mins"] > 0).astype(float) - t["b_app"]
    f = t[t["b_pts"].notna() & t["pts"].notna()].copy()

    L = ["# Congestion residual study: does a midweek game (own team or opponent) leave anything in the forecast?", "",
         f"Rows {len(t):,} (single-fixture weeks, {SEASONS[0]} → {SEASONS[-1]}); with a stored walk-forward classic forecast {len(f):,} (top-256/week). "
         f"Midweek proxy = UCL/UEL/UECL game within {BEFORE_DAYS:.0f} days before the PL kickoff ('before') or {AFTER_DAYS:.0f} days after ('after'). "
         "Residual = realised − forecast (points, minutes, appearance). ± = 2 s.e.", "",
         f"Share of rows: own team played in Europe before {t['own_before'].mean():.1%}, opponent did {t['opp_before'].mean():.1%}, "
         f"both {(t['own_before'] & t['opp_before']).mean():.1%}; opponent is a European club that season {t['opp_euro_club'].mean():.1%}.", "",
         "## A. Forecast residual by who played in Europe in the 4 days before", "",
         "| own team played | opponent played | Δ points | Δ minutes | Δ appearance |", "|---|---|---|---|---|"]
    for ob in (False, True):
        for pb in (False, True):
            g = f[(f["own_before"] == ob) & (f["opp_before"] == pb)]
            L.append(f"| {'yes' if ob else 'no'} | {'yes' if pb else 'no'} | {cell(g['res_pts'])} | {cell(g['res_min'])} | {cell(g['res_app'])} |")
    L += ["", "## B. Forecast residual by who plays in Europe in the 3 days after (resting ahead of a tie)", "",
          "| own team plays after | opponent plays after | Δ points | Δ minutes | Δ appearance |", "|---|---|---|---|---|"]
    for oa in (False, True):
        for pa in (False, True):
            g = f[(f["own_after"] == oa) & (f["opp_after"] == pa)]
            L.append(f"| {'yes' if oa else 'no'} | {'yes' if pa else 'no'} | {cell(g['res_pts'])} | {cell(g['res_min'])} | {cell(g['res_app'])} |")
    L += ["", "## C. Opponent played in Europe before, by position (forecast rows; European-club opponents only, so the same clubs with and without a midweek game)", "",
          "| position | opponent played | Δ points | Δ minutes | realised pts | n |", "|---|---|---|---|---|---|"]
    fe = f[f["opp_euro_club"]]
    for pos in ("GK", "DEF", "MID", "FWD"):
        for pb in (False, True):
            g = fe[(fe["position"] == pos) & (fe["opp_before"] == pb)]
            if len(g):
                L.append(f"| {pos} | {'yes' if pb else 'no'} | {cell(g['res_pts'])} | {cell(g['res_min'])} | {g['pts'].mean():.2f} | {len(g):,} |")
    L += ["", "## D. Own team played in Europe before, by position (forecast rows; European clubs only)", "",
          "| position | own team played | Δ points | Δ minutes | Δ appearance | n |", "|---|---|---|---|---|---|"]
    fo = f[f["own_euro_club"]]
    for pos in ("GK", "DEF", "MID", "FWD"):
        for ob in (False, True):
            g = fo[(fo["position"] == pos) & (fo["own_before"] == ob)]
            if len(g):
                L.append(f"| {pos} | {'yes' if ob else 'no'} | {cell(g['res_pts'])} | {cell(g['res_min'])} | {cell(g['res_app'])} | {len(g):,} |")
    # raw defensive outcomes, all rows, DEF/GK who played 60+
    d = t[t["position"].isin(["GK", "DEF"]) & (t["mins"] >= 60) & t["opp_euro_club"]].copy()
    d["cs"] = pd.to_numeric(d["observed_clean_sheets"], errors="coerce")
    d["gc"] = pd.to_numeric(d["observed_goals_conceded"], errors="coerce")
    d["opp_att_q"] = d.groupby("season")["opponent_goals_for_avg_5"].transform(lambda s: pd.qcut(s.rank(method="first"), 4, labels=["q1 weakest", "q2", "q3", "q4 strongest"]))
    L += ["", "## E. Raw defensive outcomes for GK/DEF who played 60+, European-club opponents only (all rows, no forecast needed)", "",
          "| opponent attack form | opponent played in Europe before | clean-sheet rate | goals conceded | points | n |", "|---|---|---|---|---|---|"]
    for q in ["all", "q1 weakest", "q2", "q3", "q4 strongest"]:
        for pb in (False, True):
            g = d if q == "all" else d[d["opp_att_q"] == q]
            g = g[g["opp_before"] == pb]
            if len(g):
                L.append(f"| {q} | {'yes' if pb else 'no'} | {g['cs'].mean():.3f} ±{se2(g['cs']):.3f} | {g['gc'].mean():.2f} ±{se2(g['gc']):.2f} | {g['pts'].mean():.2f} ±{se2(g['pts']):.2f} | {len(g):,} |")
    L += ["", "## F. Same, opponent plays in Europe in the 3 days after", "", "| opponent plays after | clean-sheet rate | goals conceded | points | n |", "|---|---|---|---|---|"]
    for pa in (False, True):
        g = d[d["opp_after"] == pa]
        L.append(f"| {'yes' if pa else 'no'} | {g['cs'].mean():.3f} ±{se2(g['cs']):.3f} | {g['gc'].mean():.2f} ±{se2(g['gc']):.2f} | {g['pts'].mean():.2f} ±{se2(g['pts']):.2f} | {len(g):,} |")
    # own-team: do the European club's own GK/DEF concede more after a midweek tie?
    o = t[t["position"].isin(["GK", "DEF"]) & (t["mins"] >= 60) & t["own_euro_club"]].copy()
    o["cs"] = pd.to_numeric(o["observed_clean_sheets"], errors="coerce"); o["gc"] = pd.to_numeric(o["observed_goals_conceded"], errors="coerce")
    L += ["", "## G. Own team played in Europe before: that club's GK/DEF who played 60+ (all rows)", "", "| own team played before | clean-sheet rate | goals conceded | points | n |", "|---|---|---|---|---|"]
    for ob in (False, True):
        g = o[o["own_before"] == ob]
        L.append(f"| {'yes' if ob else 'no'} | {g['cs'].mean():.3f} ±{se2(g['cs']):.3f} | {g['gc'].mean():.2f} ±{se2(g['gc']):.2f} | {g['pts'].mean():.2f} ±{se2(g['pts']):.2f} | {len(g):,} |")
    # gap-days detail: Thursday→Sunday (3 days) vs Tuesday/Wednesday→Saturday (3-4 days) for the opponent
    L += ["", "## H. Opponent's rest before the match (days since its European game), forecast rows, DEF/GK", "", "| opponent rest | Δ points | realised pts | n |", "|---|---|---|---|"]
    fd = f[f["position"].isin(["GK", "DEF"]) & f["opp_euro_club"]]
    for lo, hi, lab in ((0, 2.5, "≤ 2.5 days"), (2.5, 3.5, "3 days (Thu → Sun)"), (3.5, 4.5, "4 days (Wed → Sun / Tue → Sat)"), (4.5, 8, "5-7 days"), (8, 1000, "no game that week")):
        g = fd[(fd["opp_gb"] > lo) & (fd["opp_gb"] <= hi)]
        if len(g):
            L.append(f"| {lab} | {cell(g['res_pts'])} | {g['pts'].mean():.2f} | {len(g):,} |")
    out.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
