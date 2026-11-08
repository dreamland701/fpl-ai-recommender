#!/usr/bin/env python3
"""How much can chip timing win at all? Exact tables + hindsight ceilings per half-season.

Wes (2026-10-11): the planner only looks 5 weeks ahead and G8's reward valued a held triple captain /
bench boost at zero, so neither could wait for a double gameweek. Before spending GPU days on a
full-half RL policy (G9), measure the room: with perfect knowledge of outcomes, what is the best any
chip timing could have scored over a half-season, versus the planner?

For every half-season in the state caches, every (wildcard week, free hit week) pair (incl. none) is
played as a closed loop with the disciplined "auto" transfer rule. Each week records what the squad
reached would have earned from triple captain (the armband holder's points) and bench boost (the
bench's points), plus the observation a policy could legitimately see that week (forecasts, priced
chip options, chips left, double/blank gameweek sizes a few weeks ahead). Wildcard and free hit change
the squad, so they need their own trajectories; triple captain and bench boost do not, so they are
additive on top. The result is an exact tabulated MDP for chip timing: a tiny numeric policy trains on
it in seconds (scripts/train_tiny_chip_policy.py), and the hindsight optimum is a brute-force max.

Outputs reports/chip_timing/<season>_h<half>.json and a summary in reports/chip_timing/ceilings.md.

usage: chip_timing_tables.py [--halves 2023-24:2,...] [--workers 18]
"""
from __future__ import annotations

import argparse
import itertools
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from dataclasses import replace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("FPL_PLANNER_DISCIPLINE", "1")
from fpl_ai.grpo_env import load_states  # noqa: E402
from fpl_ai.grpo_plan_env_v2 import CHIPS, FIRST_HALF_LAST_WEEK, MAX_HORIZON, PlanEnvV2, WeekAction, outlook_points  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402

OUT = ROOT / "reports" / os.environ.get("FPL_CHIP_TABLES_DIR", "chip_timing")
FILES = {"2020-21": ["2020-21"], "2021-22": ["2021-22"], "2022-23": ["2022-23"], "2023-24": ["2023-24"],
         "2024-25": ["2024-25"], "2025-26": ["2025-26-train", "2025-26-holdout"]}
ALL_HALVES = [f"{s}:{h}" for s in FILES for h in (1, 2)]
SCHEDULE_AHEAD = 6  # weeks of double/blank gameweek sizes shown ahead (roughly when fixtures are rearranged)
STATES = []  # set in the parent before forking


def half_states(season: str, half: int):
    states = []
    for key in FILES[season]:
        states += load_states(ROOT / "reports" / os.environ.get("FPL_STATES_DIR", "grpo_states_v2") / f"{key}.jsonl")
    return sorted((s for s in states if (s.week <= FIRST_HALF_LAST_WEEK) == (half == 1)), key=lambda s: s.week)


def projected(ids, table, key):
    """Best XI by `key` plus the captain's double: the advisor's chip pricing."""
    value = {pid: table[pid][key] for pid in ids if pid in table}
    by = {pos: sorted((pid for pid in value if table[pid]["pos"] == pos), key=lambda i: -value[i]) for pos in ("GK", "DEF", "MID", "FWD")}
    best = 0.0
    for d in range(3, 6):
        for f in range(1, 4):
            m = 10 - d - f
            if 2 <= m <= 5 and len(by["DEF"]) >= d and len(by["MID"]) >= m and len(by["FWD"]) >= f:
                xi = by["GK"][:1] + by["DEF"][:d] + by["MID"][:m] + by["FWD"][:f]
                best = max(best, sum(value[i] for i in xi) + max(value[i] for i in xi))
    return best


def observe(env: PlanEnvV2, i: int) -> dict:
    """What a chip policy may see at this week: origin forecasts only, plus the schedule a few weeks out."""
    state = env.states[0]
    table = env._forecast_table(state)
    squad = env._start_squad()
    env._refresh_sell(squad, table)
    ids = [pid for pid in squad.players if pid in table]
    fc = {f.player_id: f for f in state.forecasts}
    cap, bench = [], []
    for k in range(MAX_HORIZON):
        values = sorted((outlook_points(fc[pid], k) for pid in ids), reverse=True)
        cap.append(values[0] if values else 0.0)
        bench.append(sum(values[11:15]) if len(values) >= 15 else 0.0)
    xi_now = projected(ids, table, "p1")
    fh = env._move(0, squad, "free_hit")
    wc = env._move(0, squad, "wildcard")
    fh_ids = [p for p in ids if p not in fh["out"]] + list(fh["in"])
    wc_ids = [p for p in ids if p not in wc["out"]] + list(wc["in"])
    sched = []
    for k in range(SCHEDULE_AHEAD + 1):
        if i + k < len(STATES):
            counts = [f.fixture_count for f in STATES[i + k].forecasts]
            sched.append((round(counts.count(2) / len(counts), 3), round(counts.count(0) / len(counts), 3)))
        else:
            sched.append((0.0, 0.0))
    # squad health (v2, 10-12): a wildcard's value depends on how broken the squad is, which the
    # projected rebuild gain does not capture (its trigger lost 190 pts over 12 halves)
    papp = [fc[pid].appearance_probability for pid in ids]
    return {"bank": round(squad.bank, 1), "free_transfers": squad.free_transfers,
            "squad_papp_mean": round(sum(papp) / max(1, len(papp)), 3), "squad_flagged": sum(1 for p in papp if p < 0.5),
            "squad_p1_sum": round(sum(fc[pid].predicted_points_1gw for pid in ids), 1),
            "squad_p5_sum": round(sum(fc[pid].predicted_points_5gw for pid in ids), 1),
            "cap_outlook": [round(v, 2) for v in cap], "bench_outlook": [round(v, 2) for v in bench], "xi_proj": round(xi_now, 2),
            "fh_gain_proj": round(projected(fh_ids, table, "p1") - xi_now, 2),
            "wc_gain_proj": round(projected(wc_ids, table, "p5") - projected(ids, table, "p5"), 2),
            "squad_double": sum(1 for pid in ids if fc[pid].fixture_count == 2), "squad_blank": sum(1 for pid in ids if fc[pid].fixture_count == 0),
            "league_double": [s[0] for s in sched], "league_blank": [s[1] for s in sched]}


TRAJECTORY_TIMEOUT = 900  # s; a normal trajectory takes 15-25 s. 2020-21 H2 had workers spin for 9 h on some pair.


def trajectory(args):
    """Closed loop over the half with a wildcard at week wc and a free hit at week fh (None = never)."""
    import signal

    def timed_out(signum, frame):
        raise TimeoutError
    signal.signal(signal.SIGALRM, timed_out)
    signal.alarm(TRAJECTORY_TIMEOUT)
    try:
        return _trajectory(args)
    except (TimeoutError, RuntimeError) as exc:
        return {"wc": args[0], "fh": args[1], "failed": f"{type(exc).__name__}: {exc}"}
    finally:
        signal.alarm(0)


def _trajectory(args):
    wc, fh = args
    chips = {1: frozenset(CHIPS), 2: frozenset(CHIPS)}
    carried, recs = None, []
    for i, state in enumerate(STATES):
        if carried is not None:
            state = replace(state, squad=carried["squad"], bank=carried["bank"], free_transfers=carried["free_transfers"])
        env = PlanEnvV2([state] + list(STATES[i + 1:i + MAX_HORIZON]), optimize, chips=chips)
        obs = observe(env, i)
        chip = "wildcard" if state.week == wc else "free_hit" if state.week == fh else "none"
        realized, detail, carried = PlanEnvV2([state], optimize, chips=chips).rollout([WeekAction(transfer="auto", chip=chip)], return_state=True)
        chips = carried["chips"]
        d = detail[0]
        recs.append({**obs, "week": state.week, "chip": d["chip"], "realized": realized, "captain_points": d["captain_points"],
                     "bench_extra": d["bench_extra"], "best_xi_points": d["best_xi_points"]})
    return {"wc": wc, "fh": fh, "weeks": recs}


def planner_total():
    chips = {1: frozenset(CHIPS), 2: frozenset(CHIPS)}
    carried, total, used = None, 0.0, []
    for i, state in enumerate(STATES):
        if carried is not None:
            state = replace(state, squad=carried["squad"], bank=carried["bank"], free_transfers=carried["free_transfers"])
        env = PlanEnvV2([state] + list(STATES[i + 1:i + MAX_HORIZON]), optimize, chips=chips)
        action = env.baseline_plan()[0]
        realized, detail, carried = PlanEnvV2([state], optimize, chips=chips).rollout([action], return_state=True)
        chips = carried["chips"]
        total += realized
        if detail[0]["chip"] != "none":
            used.append((state.week, detail[0]["chip"]))
    return total, used


def best_tc_bb(traj):
    """Best distinct triple-captain and bench-boost weeks on this trajectory, avoiding its WC/FH weeks."""
    free = [w for w in traj["weeks"] if w["chip"] == "none"]
    best = (0.0, None, None)
    for a, b in itertools.permutations(free, 2):
        gain = a["captain_points"] + b["bench_extra"]
        if gain > best[0]:
            best = (gain, a["week"], b["week"])
    return best


def ceilings(trajs, planner):
    base = next(t for t in trajs if t["wc"] is None and t["fh"] is None)
    no_chips = sum(w["realized"] for w in base["weeks"])
    tcbb = best_tc_bb(base)
    best = None
    for t in trajs:
        total = sum(w["realized"] for w in t["weeks"])
        g, tc, bb = best_tc_bb(t)
        if best is None or total + g > best["total"]:
            best = {"total": total + g, "wc": t["wc"], "fh": t["fh"], "tc": tc, "bb": bb}
    captain_hindsight = sum(w["best_xi_points"] - w["captain_points"] for w in base["weeks"])
    return {"planner": planner[0], "planner_chips": planner[1], "no_chips": no_chips,
            "hindsight_tc_bb_only": no_chips + tcbb[0], "hindsight_tc_bb_weeks": tcbb[1:],
            "hindsight_all_chips": best["total"], "hindsight_chip_weeks": {k: best[k] for k in ("wc", "fh", "tc", "bb")},
            "perfect_captain_extra": captain_hindsight}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--halves", default=",".join(ALL_HALVES))
    ap.add_argument("--workers", type=int, default=18)
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    summary = {}
    for item in args.halves.split(","):
        season, half = item.split(":"); half = int(half)
        STATES[:] = half_states(season, half)
        weeks = [s.week for s in STATES]
        pairs = [(wc, fh) for wc in [None] + weeks for fh in [None] + weeks if wc is None or fh is None or wc != fh]
        t0 = time.time()
        with ProcessPoolExecutor(args.workers) as pool:
            trajs = list(pool.map(trajectory, pairs, chunksize=1))
        failed = [t for t in trajs if "failed" in t]
        for t in failed:
            print(f"  FAILED wc={t['wc']} fh={t['fh']}: {t['failed']}", flush=True)
        trajs = [t for t in trajs if "failed" not in t]
        planner = planner_total()
        c = ceilings(trajs, planner)
        summary[item] = c
        json.dump({"season": season, "half": half, "weeks": weeks, "trajectories": trajs, "ceilings": c, "failed": failed},
                  open(OUT / f"{season}_h{half}.json", "w"))
        print(f"{item}: {len(pairs)} trajectories in {time.time() - t0:.0f}s | planner {c['planner']:.0f} (chips {c['planner_chips']}) | "
              f"no chips {c['no_chips']:.0f} | hindsight TC+BB only {c['hindsight_tc_bb_only']:.0f} | hindsight all chips "
              f"{c['hindsight_all_chips']:.0f} {c['hindsight_chip_weeks']} | perfect captain +{c['perfect_captain_extra']:.0f}", flush=True)
    # the summary covers every half built so far (halves run one invocation each after the 2020-21 H2 stall)
    summary = {f"{d['season']}:{d['half']}": d["ceilings"] for d in (json.load(open(f)) for f in sorted(OUT.glob("*_h*.json")))}
    lines = ["# Chip timing: how much is there to win?", "",
             "Closed loop per half-season with the disciplined auto transfer. Hindsight = chip weeks chosen knowing the outcomes "
             "(an upper bound no policy reaches). TC+BB only = wildcard and free hit never played. Perfect captain = the best "
             "XI player captained every week (reported for scale; not a chip decision).", "",
             "| Half | Planner | No chips | Hindsight TC+BB only | Hindsight all 4 chips | Ceiling − planner | Perfect captain |",
             "|---|---|---|---|---|---|---|"]
    for item, c in summary.items():
        lines.append(f"| {item} | {c['planner']:.0f} | {c['no_chips']:.0f} | {c['hindsight_tc_bb_only']:.0f} | {c['hindsight_all_chips']:.0f} "
                     f"| +{c['hindsight_all_chips'] - c['planner']:.0f} | +{c['perfect_captain_extra']:.0f} |")
    if len(summary) > 1:
        tot = {k: sum(c[k] for c in summary.values()) for k in ("planner", "no_chips", "hindsight_tc_bb_only", "hindsight_all_chips", "perfect_captain_extra")}
        lines.append(f"| **total** | {tot['planner']:.0f} | {tot['no_chips']:.0f} | {tot['hindsight_tc_bb_only']:.0f} | {tot['hindsight_all_chips']:.0f} "
                     f"| +{tot['hindsight_all_chips'] - tot['planner']:.0f} | +{tot['perfect_captain_extra']:.0f} |")
    (OUT / "ceilings.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
