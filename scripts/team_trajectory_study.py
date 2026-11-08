#!/usr/bin/env python3
"""Team trajectory study (2026-10-31, Wes: "should the classic model capture up-and-coming teams? Villa and Spurs are
doing well, the commentary says so; if the classic ML cannot see it that is an argument for SFT/RL").

The ridge carries team form only as lagged 3- and 5-week rolling goals for/against (own team and opponent), i.e. a
short window with no baseline: a mid-table club on a hot streak and a champion in ordinary form look alike. This study
asks whether that leaves anything on the table, using the stored walk-forward classic forecasts (E20 corpora, top-256
per week, 2022-23 -> 2026-27 GW5, plus the live F6 corpora for 2026-27 GW6-8):

  A. team-level predictability: how much of a club's last-5 goal-difference streak persists into the next game once its
     prior-season level is known (if the streak is noise, no model can monetise it);
  B. forecast residual (realised - classic forecast points) by own-team trajectory bucket: last-5 GD vs prior-season GD
     ("trend"), season-to-date vs prior ("trajectory"), last-5 alone ("form", what the model already sees), and a
     creator-style flag (last-4 points >= 8 from a club that finished 8th or lower); by position group and for regulars;
  C. the same for the OPPONENT's trajectory (facing a rising team);
  D. 2026-27 live: residual by club GW2-8, Villa and Spurs players singled out, and the as-of GW9 team features the
     production model sees.

usage: PYTHONPATH=src python3 scripts/team_trajectory_study.py [out_dir]"""
from __future__ import annotations

import ast
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
_ns: dict = {"ROOT": str(ROOT)}
for node in ast.parse((ROOT / "scripts/minutes_prior_study.py").read_text()).body:
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") in ("FILES", "SEASONS"):
        exec(compile(ast.Module(body=[node], type_ignores=[]), "x", "exec"), _ns)
FILES = list(_ns["FILES"]) + [str(ROOT / f"reports/live_gw{w}final_2627_f6_corpus_full.jsonl") for w in (6, 7, 8)]
SEASONS = sorted(s for s in _ns["SEASONS"] if s >= "2022-23")
if "2026-27" not in SEASONS:
    SEASONS.append("2026-27")
POS = {1: "GK", 2: "DEF", 3: "MID", 4: "FWD"}


def se2(x) -> float:
    x = np.asarray(x, dtype=float)
    return 2 * x.std(ddof=1) / np.sqrt(len(x)) if len(x) > 1 else float("nan")


def cell(x) -> str:
    x = np.asarray(x, dtype=float)
    return f"{x.mean():+.3f} ±{se2(x):.3f} (n {len(x):,})" if len(x) else "—"


def ols(y, X, names):
    X = np.column_stack([np.ones(len(y))] + [np.asarray(c, dtype=float) for c in X])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    dof = max(len(y) - X.shape[1], 1)
    cov = np.linalg.pinv(X.T @ X) * (resid @ resid / dof)
    se = np.sqrt(np.diag(cov))
    r2 = 1 - (resid @ resid) / ((y - y.mean()) @ (y - y.mean()))
    return {n: (b, 2 * s) for n, b, s in zip(["const"] + names, beta, se)}, r2


def team_names() -> dict:
    """(season, team_id) -> (short_name, code); the FPL team `code` is stable across seasons, ids are not."""
    out, name_to_code = {}, {}
    frames = {}
    for d in sorted((ROOT / "data/fpl_history").iterdir()):
        p = d / "teams.csv"
        if p.exists():
            frames[d.name] = pd.read_csv(p)
    for season, tm in frames.items():
        if "code" in tm.columns:
            for r in tm.itertuples(index=False):
                name_to_code[str(r.name)] = int(r.code)
    for season, tm in frames.items():
        for r in tm.itertuples(index=False):
            code = int(r.code) if "code" in tm.columns and pd.notna(r.code) else name_to_code.get(str(r.name))
            short = str(getattr(r, "short_name", r.name))
            out[(season, int(r.id))] = (short, code)
    return out


def main() -> None:
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "reports/team_trajectory_study"
    out_dir.mkdir(parents=True, exist_ok=True)
    cols = ["season", "week", "player_id", "player_name", "team_id", "position", "primary_opponent_team_id", "fixture_count",
            "home_fixture_count", "goals_for", "goals_against", "team_goals_for_avg_5", "team_goals_against_avg_5",
            "label_points_1gw", "observed_minutes"]
    t = pd.read_csv(ROOT / "data/fpl_training_rows_v3_contract_f6.csv", low_memory=False, usecols=cols)
    t = t[t["season"].isin(SEASONS)].copy()
    if pd.api.types.is_numeric_dtype(t["position"]):
        t["position"] = t["position"].map(POS)
    names = team_names()
    t["club"] = [names.get((s, int(x)), ("?", None))[0] for s, x in zip(t["season"], t["team_id"])]

    # ---- team-week table -------------------------------------------------------------------------------------------
    tw = (t.groupby(["season", "team_id", "week"], as_index=False)
            .agg(gf=("goals_for", "first"), ga=("goals_against", "first"), nfix=("fixture_count", "first")))
    tw = tw[tw["gf"].notna() & (tw["nfix"] > 0)].copy()
    tw["code"] = [names.get((s, int(x)), ("?", None))[1] for s, x in zip(tw["season"], tw["team_id"])]
    tw["gd"] = tw["gf"] - tw["ga"]
    tw["pts"] = np.where(tw["gd"] > 0, 3, np.where(tw["gd"] == 0, 1, 0)) * tw["nfix"].clip(lower=1)  # DGW approximated
    tw = tw.sort_values(["season", "team_id", "week"])
    g = tw.groupby(["season", "team_id"], sort=False)
    for c in ("gd", "nfix", "pts", "gf", "ga"):
        tw[f"cum_{c}"] = g[c].cumsum() - tw[c]
    tw["games_before"] = tw["cum_nfix"]
    tw["std_gd_pg"] = tw["cum_gd"] / tw["cum_nfix"].replace(0, np.nan)
    tw["std_ppg"] = tw["cum_pts"] / tw["cum_nfix"].replace(0, np.nan)
    for w in (4, 5):
        tw[f"l{w}_gd"] = g["gd"].transform(lambda s: s.shift(1).rolling(w, min_periods=w).sum())
        tw[f"l{w}_n"] = g["nfix"].transform(lambda s: s.shift(1).rolling(w, min_periods=w).sum())
        tw[f"l{w}_pts"] = g["pts"].transform(lambda s: s.shift(1).rolling(w, min_periods=w).sum())
        tw[f"l{w}_gd_pg"] = tw[f"l{w}_gd"] / tw[f"l{w}_n"]
    tw["l5_gf_pg"] = g["gf"].transform(lambda s: s.shift(1).rolling(5, min_periods=5).sum()) / tw["l5_n"]
    tw["l5_ga_pg"] = g["ga"].transform(lambda s: s.shift(1).rolling(5, min_periods=5).sum()) / tw["l5_n"]
    # prior-season level by club code
    season_tot = tw.groupby(["season", "code"], as_index=False).agg(gd=("gd", "sum"), n=("nfix", "sum"), pts=("pts", "sum"))
    season_tot["gd_pg"] = season_tot["gd"] / season_tot["n"]
    season_tot["ppg"] = season_tot["pts"] / season_tot["n"]
    season_tot["rank"] = season_tot.groupby("season")["pts"].rank(ascending=False, method="min")
    prev = {s: f"{int(s[:4]) - 1}-{str(int(s[:4]))[2:]}" for s in tw["season"].unique()}
    prior = {(r.season, r.code): (r.gd_pg, r.ppg, r.rank) for r in season_tot.itertuples(index=False)}
    pr = [prior.get((prev[s], c), (np.nan, np.nan, np.nan)) for s, c in zip(tw["season"], tw["code"])]
    tw["prior_gd_pg"] = [x[0] for x in pr]
    tw["prior_ppg"] = [x[1] for x in pr]
    tw["prior_rank"] = [x[2] for x in pr]
    tw["promoted"] = tw["prior_gd_pg"].isna()
    tw["trend5"] = tw["l5_gd_pg"] - tw["prior_gd_pg"]            # last-5 streak vs the club's prior-season level
    tw["traj"] = tw["std_gd_pg"].where(tw["games_before"] >= 5) - tw["prior_gd_pg"]  # season-to-date vs prior
    tw["rising"] = (tw["l4_pts"] >= 8) & (tw["prior_rank"] >= 8)
    tw["falling"] = (tw["l4_pts"] <= 3) & (tw["prior_rank"] <= 6)
    tw["gd_pg_this"] = tw["gd"] / tw["nfix"]

    L = ["# Team trajectory study: does the classic model miss up-and-coming (or fading) teams?", "",
         f"Seasons {SEASONS[0]} → {SEASONS[-1]}. Team form in the ridge = lagged 3/5-week rolling goals for/against (own and opponent), "
         "no longer baseline. Here: trend5 = last-5 GD/game − the club's prior-season GD/game; traj = season-to-date GD/game "
         "(≥5 games) − prior; form5 = last-5 GD/game alone; rising = last-4 points ≥ 8 from a club that finished 8th or lower "
         "(falling = ≤ 3 points from a top-6 club). Promoted clubs have no prior and are excluded from trend/traj. ± = 2 s.e.", ""]

    # ---- A. does the streak persist? --------------------------------------------------------------------------------
    a = tw[tw["l5_gd_pg"].notna() & tw["prior_gd_pg"].notna() & tw["gd_pg_this"].notna()].copy()
    L += ["## A. Team level: does a 5-game streak carry into the next game once the club's level is known?", "",
          f"Team-weeks with a prior season and 5 previous games: {len(a):,}. OLS of this week's GD/game on the lagged measures.", "",
          "| model | coefficients (± 2 s.e.) | R² |", "|---|---|---|"]
    for nm, X, names_ in [("prior only", [a["prior_gd_pg"]], ["prior"]),
                          ("form5 only", [a["l5_gd_pg"]], ["form5"]),
                          ("prior + form5", [a["prior_gd_pg"], a["l5_gd_pg"]], ["prior", "form5"]),
                          ("prior + season-to-date + form5", [a["prior_gd_pg"], a["std_gd_pg"].fillna(a["prior_gd_pg"]), a["l5_gd_pg"]], ["prior", "std", "form5"])]:
        co, r2 = ols(a["gd_pg_this"].to_numpy(float), X, names_)
        L.append(f"| {nm} | " + ", ".join(f"{k} {v[0]:+.3f} ±{v[1]:.3f}" for k, v in co.items() if k != "const") + f" | {r2:.3f} |")
    for lab, m in (("rising", a["rising"]), ("falling", a["falling"])):
        sub, rest = a[m], a[~m & ~a["promoted"]]
        L.append(f"\n{lab} team-weeks {len(sub):,}: next-game GD/game {sub['gd_pg_this'].mean():+.2f} ±{se2(sub['gd_pg_this']):.2f} "
                 f"(their last-5 {sub['l5_gd_pg'].mean():+.2f}, prior-season {sub['prior_gd_pg'].mean():+.2f}); other clubs with a prior {rest['gd_pg_this'].mean():+.2f}.")
    L.append("")

    # ---- B/C. forecast residuals ------------------------------------------------------------------------------------
    fc = {}
    for path in FILES:
        for line in open(path):
            r = json.loads(line); m = r["metadata"]; b = m["baseline_forecast"]
            fc[(m["season"], int(m["week"]), int(m["player_id"]))] = (float(b["baseline_points_1gw"]), float(b["baseline_minutes_1gw"]),
                                                                       float(b["baseline_appearance_probability"]))
    key = list(zip(t["season"], t["week"].astype(int), t["player_id"].astype(int)))
    t["b_pts"] = [fc.get(k, (np.nan,) * 3)[0] for k in key]
    t["b_min"] = [fc.get(k, (np.nan,) * 3)[1] for k in key]
    t["pts"] = pd.to_numeric(t["label_points_1gw"], errors="coerce")
    t["res"] = t["pts"] - t["b_pts"]
    f = t[t["b_pts"].notna() & t["pts"].notna() & (t["fixture_count"] == 1)].copy()
    tcols = ["season", "team_id", "week", "trend5", "traj", "l5_gd_pg", "l5_gf_pg", "l5_ga_pg", "prior_gd_pg", "rising", "falling", "promoted", "games_before"]
    f = f.merge(tw[tcols], on=["season", "team_id", "week"], how="left")
    opp = tw[tcols].rename(columns={c: f"opp_{c}" for c in tcols if c not in ("season", "week")}).rename(columns={"opp_team_id": "primary_opponent_team_id"})
    f["primary_opponent_team_id"] = pd.to_numeric(f["primary_opponent_team_id"], errors="coerce")
    f = f.merge(opp, on=["season", "primary_opponent_team_id", "week"], how="left")
    f["grp"] = np.where(f["position"].isin(["GK", "DEF"]), "GK/DEF", "MID/FWD")
    f["regular"] = f["b_min"] >= 60
    # team-week quintile edges (so player counts do not dominate the bucket edges)
    def buckets(col, src):
        edges = src[col].dropna().quantile([0.2, 0.4, 0.6, 0.8]).to_numpy()
        return pd.cut(f[col], [-np.inf, *edges, np.inf], labels=["Q1 lowest", "Q2", "Q3", "Q4", "Q5 highest"])
    tw_valid = tw[tw["trend5"].notna()]
    for col in ("trend5", "traj", "l5_gd_pg", "opp_trend5", "opp_l5_gd_pg"):
        src_col = col.replace("opp_", "")
        f[f"b_{col}"] = buckets(col, tw_valid.rename(columns={src_col: col}) if col.startswith("opp_") else tw_valid)

    L += ["## B. Forecast residual (realised − classic points) by the player's OWN team trajectory", "",
          f"Player-weeks with a stored walk-forward forecast and a single fixture: {len(f):,}; with a team trend (club has a prior season, 5 games played): {f['trend5'].notna().sum():,}. "
          "Residual +0.10 on a bucket = the model under-forecasts those players by a tenth of a point per week.", ""]
    for col, title in (("b_trend5", "trend5 = last-5 GD vs prior-season level (what the model lacks)"),
                       ("b_traj", "traj = season-to-date GD vs prior-season level"),
                       ("b_l5_gd_pg", "form5 = last-5 GD alone (what the model already carries)")):
        L += [f"### {title}", "", "| bucket | all | GK/DEF | MID/FWD | regulars (forecast ≥ 60 min) | mean trend | mean forecast | mean realised |", "|---|---|---|---|---|---|---|---|"]
        raw = col[2:]
        for b_ in ["Q1 lowest", "Q2", "Q3", "Q4", "Q5 highest"]:
            s = f[f[col] == b_]
            if not len(s):
                continue
            L.append(f"| {b_} | {cell(s['res'])} | {cell(s[s['grp'] == 'GK/DEF']['res'])} | {cell(s[s['grp'] == 'MID/FWD']['res'])} | "
                     f"{cell(s[s['regular']]['res'])} | {s[raw].mean():+.2f} | {s['b_pts'].mean():.2f} | {s['pts'].mean():.2f} |")
        L.append("")
    L += ["### Creator-style flags", "", "| flag | all | GK/DEF | MID/FWD | regulars | n team-weeks |", "|---|---|---|---|---|---|"]
    for lab, m in (("rising (last-4 ≥ 8 pts, finished ≥ 8th)", f["rising"] == True), ("falling (last-4 ≤ 3 pts, finished top 6)", f["falling"] == True),  # noqa: E712
                   ("promoted club", f["promoted"] == True), ("everyone else", (f["rising"] == False) & (f["falling"] == False) & (f["promoted"] == False))):  # noqa: E712
        s = f[m]
        L.append(f"| {lab} | {cell(s['res'])} | {cell(s[s['grp'] == 'GK/DEF']['res'])} | {cell(s[s['grp'] == 'MID/FWD']['res'])} | {cell(s[s['regular']]['res'])} | "
                 f"{s[['season', 'team_id', 'week']].drop_duplicates().shape[0]:,} |")
    L.append("")
    # regression of the residual on the team terms
    r = f[f["trend5"].notna() & f["opp_trend5"].notna()].copy()
    L += ["### Regression of the residual on team terms (all rows with trends, position dummies included)", "",
          "| term | coefficient ± 2 s.e. | reading |", "|---|---|---|"]
    co, r2 = ols(r["res"].to_numpy(float),
                 [r["trend5"], r["prior_gd_pg"], r["opp_trend5"], r["opp_prior_gd_pg"], (r["grp"] == "MID/FWD").astype(float), r["b_pts"]],
                 ["own trend5", "own prior level", "opp trend5", "opp prior level", "MID/FWD", "forecast"])
    notes = {"own trend5": "points/week left per 1.0 GD/game of own streak over the prior level",
             "own prior level": "points/week left per 1.0 GD/game of prior-season level",
             "opp trend5": "same for the opponent's streak", "opp prior level": "same for the opponent's level",
             "MID/FWD": "position offset", "forecast": "per forecast point (the generic shrink/stretch)"}
    for k, v in co.items():
        if k != "const":
            L.append(f"| {k} | {v[0]:+.3f} ±{v[1]:.3f} | {notes[k]} |")
    L.append(f"\nR² {r2:.4f} on {len(r):,} rows. Scale: a club one full goal per game above its prior level over 5 games is a very strong streak (Villa GW4-8 2026-27 ≈ +0.6 vs prior ≈ −0.4).\n")
    # by season stability for the top trend bucket
    L += ["### Top trend5 bucket by season (stability)", "", "| season | residual, Q5 | residual, Q1 | n Q5 |", "|---|---|---|---|"]
    for s_ in SEASONS:
        q5 = f[(f["season"] == s_) & (f["b_trend5"] == "Q5 highest")]; q1 = f[(f["season"] == s_) & (f["b_trend5"] == "Q1 lowest")]
        if len(q5):
            L.append(f"| {s_} | {cell(q5['res'])} | {cell(q1['res'])} | {len(q5):,} |")
    L.append("")
    L += ["## C. Residual by the OPPONENT's trajectory (facing a rising or fading team)", "",
          "| bucket | all | GK/DEF | MID/FWD | regulars |", "|---|---|---|---|---|"]
    for b_ in ["Q1 lowest", "Q2", "Q3", "Q4", "Q5 highest"]:
        s = f[f["b_opp_trend5"] == b_]
        if len(s):
            L.append(f"| opp trend5 {b_} | {cell(s['res'])} | {cell(s[s['grp'] == 'GK/DEF']['res'])} | {cell(s[s['grp'] == 'MID/FWD']['res'])} | {cell(s[s['regular']]['res'])} |")
    L.append("")

    # ---- D. 2026-27 live -----------------------------------------------------------------------------------------------
    live = f[f["season"] == "2026-27"].copy()
    L += ["## D. 2026-27 so far (GW2-5 from the E20 live eval corpus, GW6-8 from the final-packet F6 corpora)", "",
          f"Rows {len(live):,}. Per club: residual of all forecast players and of regulars; the 'sum' is the points the model left on that club's players over the weeks covered.", "",
          "| club | n | residual all | residual regulars | sum, regulars | GW8 last-5 GF/GA per game | trend5 at GW8 |", "|---|---|---|---|---|---|---|"]
    tw8 = tw[(tw["season"] == "2026-27") & (tw["week"] == 8)].set_index("team_id")
    rows = []
    for club, s in live.groupby("club"):
        tid = int(s["team_id"].iloc[0]); reg = s[s["regular"]]
        w8 = tw8.loc[tid] if tid in tw8.index else None
        rows.append((reg["res"].sum() if len(reg) else 0.0, club, len(s), cell(s["res"]), cell(reg["res"]), f"{reg['res'].sum():+.1f}" if len(reg) else "—",
                     f"{w8['l5_gf_pg']:.2f} / {w8['l5_ga_pg']:.2f}" if w8 is not None and pd.notna(w8["l5_gf_pg"]) else "—",
                     f"{w8['trend5']:+.2f}" if w8 is not None and pd.notna(w8["trend5"]) else "promoted/—"))
    for r_ in sorted(rows, reverse=True):
        L.append(f"| {r_[1]} | {r_[2]} | {r_[3]} | {r_[4]} | {r_[5]} | {r_[6]} | {r_[7]} |")
    L.append("")
    for club in ("AVL", "TOT"):
        s = live[(live["club"] == club) & (live["b_min"] >= 30)]
        if not len(s):
            continue
        L += [f"### {club} players (forecast ≥ 30 min), GW2-8", "", "| player | pos | weeks | forecast/wk | realised/wk | residual/wk | sum |", "|---|---|---|---|---|---|---|"]
        agg = s.groupby(["player_name", "position"]).agg(n=("res", "size"), fcst=("b_pts", "mean"), real=("pts", "mean"), res=("res", "mean"), tot=("res", "sum")).reset_index()
        for r_ in agg.sort_values("tot", ascending=False).itertuples(index=False):
            L.append(f"| {r_.player_name} | {r_.position} | {r_.n} | {r_.fcst:.2f} | {r_.real:.2f} | {r_.res:+.2f} | {r_.tot:+.1f} |")
        L.append("")
    # what the model sees going into GW9: lagged last-5 features by club
    L += ["### As-of GW9 team form the production features carry (last 5 weeks, GW4-8, per game) vs prior-season level", "",
          "| club | last-5 GF | last-5 GA | last-5 GD | prior-season GD/game | trend5 | last-4 pts | flag |", "|---|---|---|---|---|---|---|---|"]
    tw9 = tw[(tw["season"] == "2026-27") & (tw["week"] == 8)].copy()
    # shift: the GW9 as-of window is weeks 4-8, i.e. this week's (8) values included -> recompute directly
    s26 = tw[tw["season"] == "2026-27"]
    for tid, grp_ in s26.groupby("team_id"):
        last5 = grp_[grp_["week"].between(4, 8)]; last4 = grp_[grp_["week"].between(5, 8)]
        if len(last5) < 5:
            continue
        pri = grp_["prior_gd_pg"].iloc[0]; rank = grp_["prior_rank"].iloc[0]
        gd5 = last5["gd"].sum() / last5["nfix"].sum()
        trend = gd5 - pri if pd.notna(pri) else np.nan
        flag = "rising" if (last4["pts"].sum() >= 8 and pd.notna(rank) and rank >= 8) else ("falling" if (last4["pts"].sum() <= 3 and pd.notna(rank) and rank <= 6) else "")
        L.append(f"| {names.get(('2026-27', int(tid)), ('?',))[0]} | {last5['gf'].sum() / last5['nfix'].sum():.2f} | {last5['ga'].sum() / last5['nfix'].sum():.2f} | {gd5:+.2f} | "
                 f"{pri:+.2f} | {trend:+.2f} | {int(last4['pts'].sum())} | {flag} |" if pd.notna(pri) else
                 f"| {names.get(('2026-27', int(tid)), ('?',))[0]} | {last5['gf'].sum() / last5['nfix'].sum():.2f} | {last5['ga'].sum() / last5['nfix'].sum():.2f} | {gd5:+.2f} | promoted | — | {int(last4['pts'].sum())} | |")
    L.append("")
    (out_dir / "README.md").write_text("\n".join(L))
    f.to_parquet(out_dir / "rows.parquet") if hasattr(f, "to_parquet") else None
    print("\n".join(L))
    print(f"\nwrote {out_dir / 'README.md'}")


if __name__ == "__main__":
    main()
