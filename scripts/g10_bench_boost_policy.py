#!/usr/bin/env python3
"""G10: a per-decision bench-boost (and triple-captain) timing policy learned from the chip tables.

Wes (2026-10-13): capture as much as possible of the ~25 points per half that perfectly timed TC+BB earn
over the planner; focus the learning where the signal has little noise. The bound computed first:
triple captain timing is luck (the captain's forecast correlates +0.16 with his actual score week to week,
and an oracle knowing every future forecast does no better than a random week), bench boost is not
(+0.40; planner 11.0 of a hindsight 20.4). So the learnable target is the bench boost: at each week with
the chip held, play it now or wait, scored by that week's counterfactual bench points from the tables.

Stage A (`build`): replay the planner's closed-loop path per half (no chips) and record, per week, what a
policy may see (bench players' forecasts and P(play), outlook, schedule ahead, weeks left) and the
hindsight labels (bench_extra, captain_points). Stage B (`eval`): leave-one-season-out, fit a value model
for this week's bench points and a continuation model for the best later week, and score the stopping
policy closed loop (bench boost is additive, so the realised value is the chosen week's bench_extra).

usage: g10_bench_boost_policy.py build [--workers 12]; g10_bench_boost_policy.py eval
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor
from dataclasses import replace
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("FPL_PLANNER_DISCIPLINE", "1")
spec = importlib.util.spec_from_file_location("chip_timing_tables", ROOT / "scripts" / "chip_timing_tables.py")
ct = importlib.util.module_from_spec(spec); spec.loader.exec_module(ct)
from fpl_ai.grpo_plan_env_v2 import CHIPS, MAX_HORIZON, FIRST_HALF_LAST_WEEK, PlanEnvV2, WeekAction, outlook_points  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402

DATA = ROOT / "reports" / "chip_timing" / "g10_dataset.jsonl"
OUT = ROOT / "reports" / "chip_timing" / "g10_bench_boost.md"


def replay(key: str):
    season, half = key.split(":"); half = int(half)
    states = ct.half_states(season, half)
    ct.STATES = states
    chips = {1: frozenset(CHIPS), 2: frozenset(CHIPS)}
    carried, recs = None, []
    last = FIRST_HALF_LAST_WEEK if half == 1 else 38
    for i, state in enumerate(states):
        if carried is not None:
            state = replace(state, squad=carried["squad"], bank=carried["bank"], free_transfers=carried["free_transfers"])
        env = PlanEnvV2([state] + list(states[i + 1:i + MAX_HORIZON]), optimize, chips=chips)
        obs = ct.observe(env, i)
        # the lineup the planner fields this week, after its transfer: replay the week once to learn the squad,
        # then read bench/captain forecasts from the post-transfer squad
        realized, detail, carried = PlanEnvV2([state], optimize, chips=chips).rollout([WeekAction(transfer="auto")], return_state=True)
        chips = carried["chips"]
        fc = {f.player_id: f for f in state.forecasts}
        post = carried["squad"]
        table = env._forecast_table(state)
        ids = [p.player_id for p in post if p.player_id in table]
        values = {pid: table[pid]["p1"] for pid in ids}
        by = {pos: sorted((pid for pid in ids if table[pid]["pos"] == pos), key=lambda i: -values[i]) for pos in ("GK", "DEF", "MID", "FWD")}
        best = None
        for d_ in range(3, 6):
            for f_ in range(1, 4):
                m = 10 - d_ - f_
                if 2 <= m <= 5 and len(by["DEF"]) >= d_ and len(by["MID"]) >= m and len(by["FWD"]) >= f_:
                    xi = by["GK"][:1] + by["DEF"][:d_] + by["MID"][:m] + by["FWD"][:f_]
                    s = sum(values[p] for p in xi)
                    if best is None or s > best[0]:
                        best = (s, xi)
        xi = best[1]
        bench = by["GK"][1:2] + sorted((p for p in ids if p not in xi and table[p]["pos"] != "GK"), key=lambda p: -values[p])
        captain = max(xi, key=lambda p: values[p])
        second = sorted((values[p] for p in xi), reverse=True)[1] if len(xi) > 1 else 0.0
        bp = [fc[p] for p in bench]
        d = detail[0]
        recs.append({"key": key, "season": season, "half": half, "week": state.week, "weeks_left": last - state.week + 1,
                     "bench_p1": [round(f.predicted_points_1gw, 2) for f in bp], "bench_papp": [round(f.appearance_probability, 3) for f in bp],
                     "bench_fix": [f.fixture_count for f in bp], "bench_pos": [f.position for f in bp],
                     "bench_minutes": [round(f.predicted_minutes, 1) for f in bp], "bench_price": [f.price for f in bp],
                     "cap_p1": round(fc[captain].predicted_points_1gw, 2), "cap_papp": round(fc[captain].appearance_probability, 3),
                     "cap_fix": fc[captain].fixture_count, "cap_price": fc[captain].price, "cap_second_p1": round(second, 2),
                     "xi_papp_mean": round(float(np.mean([fc[p].appearance_probability for p in xi])), 3),
                     **{k: obs[k] for k in ("bank", "free_transfers", "squad_papp_mean", "squad_flagged", "cap_outlook", "bench_outlook",
                                            "league_double", "league_blank", "squad_double", "squad_blank")},
                     "bench_extra": d["bench_extra"], "captain_points": d["captain_points"], "best_xi_points": d["best_xi_points"],
                     "realized": realized})
    # hindsight continuation labels
    for t, r in enumerate(recs):
        r["bb_future_max"] = max([x["bench_extra"] for x in recs[t + 1:]], default=0.0)
        r["tc_future_max"] = max([x["captain_points"] for x in recs[t + 1:]], default=0.0)
    return recs


def build(workers: int) -> None:
    with ProcessPoolExecutor(max_workers=workers) as pool:
        out = []
        for recs in pool.map(replay, ct.ALL_HALVES, chunksize=1):
            out += recs
            print(f"{recs[0]['key']}: {len(recs)} weeks; BB hindsight {max(r['bench_extra'] for r in recs):.0f}", flush=True)
    DATA.write_text("".join(json.dumps(r) + "\n" for r in out))
    print(f"wrote {len(out)} rows -> {DATA}")


# ------------------------------------------------------------------------------------------ stage B
def feats(r: dict) -> list:
    bp, pa, fx, mn = r["bench_p1"], r["bench_papp"], r["bench_fix"], r["bench_minutes"]
    pad = lambda xs, n=4, v=0.0: (list(xs) + [v] * n)[:n]  # noqa: E731
    return ([r["weeks_left"], sum(bp), min(pa) if pa else 0, float(np.mean(pa)) if pa else 0, sum(1 for p in pa if p < 0.5),
             sum(1 for f in fx if f == 0), sum(1 for f in fx if f >= 2), sum(mn) / 90.0,
             r["bench_outlook"][0], max(r["bench_outlook"][1:]), float(np.mean(r["bench_outlook"][1:])),
             r["squad_papp_mean"], r["squad_flagged"], r["xi_papp_mean"], r["bank"], r["free_transfers"], r["squad_double"], r["squad_blank"]]
            + pad(sorted(bp, reverse=True)) + pad(sorted(pa)) + r["league_double"][:7] + r["league_blank"][:7])


def fit_ridge(X, y, lam=1.0):
    X1 = np.hstack([X, np.ones((len(X), 1))])
    mu, sd = X1[:, :-1].mean(0), X1[:, :-1].std(0) + 1e-9
    Z = X1.copy(); Z[:, :-1] = (Z[:, :-1] - mu) / sd
    w = np.linalg.solve(Z.T @ Z + lam * np.eye(Z.shape[1]), Z.T @ y)
    return lambda A: (np.hstack([(A - mu) / sd, np.ones((len(A), 1))]) @ w)


def fit_gbm(X, y):
    from sklearn.ensemble import HistGradientBoostingRegressor
    m = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_depth=3, min_samples_leaf=10, random_state=0).fit(X, y)
    return m.predict


def play_week(recs, decide):
    """First week where decide(t) says play; the chip's realised value is that week's bench_extra."""
    for t in range(len(recs)):
        if t == len(recs) - 1 or decide(t):
            return recs[t]["week"], recs[t]["bench_extra"]


def evaluate() -> None:
    rows = [json.loads(l) for l in open(DATA)]
    halves = {}
    for r in rows:
        halves.setdefault(r["key"], []).append(r)
    for k in halves:
        halves[k].sort(key=lambda r: r["week"])
    seasons = sorted({r["season"] for r in rows})
    X_all = {k: np.array([feats(r) for r in v]) for k, v in halves.items()}
    results = {}
    lines = ["# G10: bench-boost stopping policy (per-decision, leave-one-season-out)", "",
             "Each held-out half is played closed loop along the planner's path; the bench boost is additive, so a policy's value is the",
             "bench points of the week it chose. Models are fit on the other seasons only. Planner rule = the live rule (play when this",
             "week's projected bench beats the next four). Value model g = this week's bench points from observable features;",
             "continuation h = best later week's bench points from the same features + weeks left. Policy: play when g >= h (+ margin).", "",
             "| half | hindsight | planner rule | random | g>=h ridge | g>=h gbm | g>=h gbm, margin -1 | gbm value-threshold |", "|---|---|---|---|---|---|---|---|"]
    tot = {}
    for season in seasons:
        train = [r for r in rows if r["season"] != season]
        Xtr = np.array([feats(r) for r in train]); y_now = np.array([r["bench_extra"] for r in train]); y_fut = np.array([r["bb_future_max"] for r in train])
        # continuation only meaningful with weeks left >= 2
        g_r, h_r = fit_ridge(Xtr, y_now), fit_ridge(Xtr, y_fut)
        g_b, h_b = fit_gbm(Xtr, y_now), fit_gbm(Xtr, y_fut)
        for key, recs in halves.items():
            if recs[0]["season"] != season:
                continue
            X = X_all[key]
            hind = max(r["bench_extra"] for r in recs)
            rnd = float(np.mean([r["bench_extra"] for r in recs]))
            plan = play_week(recs, lambda t: recs[t]["bench_outlook"][0] >= max(recs[t]["bench_outlook"][1:]) - 1e-9)
            gr, hr, gb, hb = g_r(X), h_r(X), g_b(X), h_b(X)
            pol = {"ridge": play_week(recs, lambda t: gr[t] >= hr[t]), "gbm": play_week(recs, lambda t: gb[t] >= hb[t]),
                   "gbm_m1": play_week(recs, lambda t: gb[t] >= hb[t] - 1.0),
                   # value threshold: play when predicted bench points are in the top quartile of training weeks' predictions
                   "gbm_q": play_week(recs, lambda t: gb[t] >= np.quantile(g_b(Xtr), 0.75))}
            results[key] = {"hind": hind, "plan": plan, "rnd": rnd, **pol}
            lines.append(f"| {key} | {hind:.0f} | {plan[1]:.0f} (w{plan[0]}) | {rnd:.1f} | {pol['ridge'][1]:.0f} (w{pol['ridge'][0]}) | {pol['gbm'][1]:.0f} (w{pol['gbm'][0]}) | "
                         f"{pol['gbm_m1'][1]:.0f} (w{pol['gbm_m1'][0]}) | {pol['gbm_q'][1]:.0f} (w{pol['gbm_q'][0]}) |")
    n = len(results)
    def mean(k): return sum((v[k][1] if isinstance(v[k], tuple) else v[k]) for v in results.values()) / n
    summ = f"| **mean of {n}** | {mean('hind'):.1f} | {mean('plan'):.1f} | {mean('rnd'):.1f} | {mean('ridge'):.1f} | {mean('gbm'):.1f} | {mean('gbm_m1'):.1f} | {mean('gbm_q'):.1f} |"
    lines.append(summ)
    wins = {k: sum(1 for v in results.values() if v[k][1] > v["plan"][1]) for k in ("ridge", "gbm", "gbm_m1", "gbm_q")}
    ties = {k: sum(1 for v in results.values() if v[k][1] == v["plan"][1]) for k in wins}
    lines += ["", "Wins / ties vs the planner rule per half: " + ", ".join(f"{k} {wins[k]}/{ties[k]}" for k in wins) + ".", ""]
    # feature view: what the value model keys on (ridge, all data)
    Xa = np.array([feats(r) for r in rows]); ya = np.array([r["bench_extra"] for r in rows])
    names = ["weeks_left", "bench_p1_sum", "bench_papp_min", "bench_papp_mean", "bench_n_doubtful", "bench_n_blank", "bench_n_double", "bench_minutes/90",
             "bench_outlook0", "bench_outlook_max_later", "bench_outlook_mean_later", "squad_papp_mean", "squad_flagged", "xi_papp_mean", "bank", "ft",
             "squad_double", "squad_blank"] + [f"bench_p1_{i}" for i in range(4)] + [f"bench_papp_{i}" for i in range(4)] + [f"league_double_{i}" for i in range(7)] + [f"league_blank_{i}" for i in range(7)]
    from sklearn.model_selection import cross_val_score
    from sklearn.ensemble import HistGradientBoostingRegressor
    from sklearn.linear_model import Ridge
    groups = [r["season"] for r in rows]
    from sklearn.model_selection import GroupKFold
    cv = GroupKFold(n_splits=len(seasons))
    r2_g = cross_val_score(HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_depth=3, min_samples_leaf=10, random_state=0), Xa, ya, cv=cv, groups=groups, scoring="r2").mean()
    r2_r = cross_val_score(Ridge(alpha=1.0), (Xa - Xa.mean(0)) / (Xa.std(0) + 1e-9), ya, cv=cv, groups=groups, scoring="r2").mean()
    base_r2 = cross_val_score(Ridge(alpha=1.0), Xa[:, [8]], ya, cv=cv, groups=groups, scoring="r2").mean()
    lines += [f"Leave-one-season-out R² for this week's bench points: forecast alone {base_r2:.3f}, ridge on all features {r2_r:.3f}, gbm {r2_g:.3f}.", ""]
    corr = [(abs(np.corrcoef(Xa[:, j], ya)[0, 1]) if Xa[:, j].std() > 0 else 0, names[j], np.corrcoef(Xa[:, j], ya)[0, 1] if Xa[:, j].std() > 0 else 0) for j in range(Xa.shape[1])]
    lines += ["Strongest single correlations with this week's bench points: " + ", ".join(f"{nm} {c:+.2f}" for _, nm, c in sorted(corr, reverse=True)[:8]) + ".", ""]
    OUT.write_text("\n".join(lines) + "\n")
    print("\n".join(lines[-6:]))
    print(summ)
    print("G10 EVAL DONE")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("stage", choices=["build", "eval"])
    ap.add_argument("--workers", type=int, default=12)
    a = ap.parse_args()
    build(a.workers) if a.stage == "build" else evaluate()
