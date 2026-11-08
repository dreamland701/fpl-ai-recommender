#!/usr/bin/env python3
"""Chip sequencing test: does a wildcard built FOR a bench boost beat the standard wildcard + bench boost?

Wes (2026-10-12): "how to sequence those chip usages ... also important". The chip-timing tables showed
a bench boost after a wildcard worth 10.6 vs 14.4 in a random week, because the standard rebuild credits
a bench player a tenth of a starter and buys the cheapest bench. Here every wildcard week w in every half
is replayed closed loop with the bench-aware rebuild (PlanEnvV2(wildcard_bench=True)); the bench boost is
then priced in week w+1 (the classic combo) or in the best later week, and compared with the standard
trajectory (wc=w, fh=None) from reports/chip_timing/<season>_h<half>.json.

Reads the same states as scripts/chip_timing_tables.py; writes reports/chip_timing/wildcard_bench_boost.md.
usage: wildcard_bench_boost.py [--halves 2023-24:2,...] [--workers 12]
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

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
os.environ.setdefault("FPL_PLANNER_DISCIPLINE", "1")
spec = importlib.util.spec_from_file_location("chip_timing_tables", ROOT / "scripts" / "chip_timing_tables.py")
ct = importlib.util.module_from_spec(spec); spec.loader.exec_module(ct)
from fpl_ai.grpo_plan_env_v2 import CHIPS, MAX_HORIZON, PlanEnvV2, WeekAction  # noqa: E402
from fpl_ai.squad_milp import optimize  # noqa: E402

OUT = ROOT / "reports" / "chip_timing"


def _variant(wc):
    """Closed loop: planner transfers every week, bench-aware wildcard at week wc, no other chip; records
    the counterfactual bench-boost value of every week (as the tables do)."""
    chips = {1: frozenset(CHIPS), 2: frozenset(CHIPS)}
    carried, recs = None, []
    for i, state in enumerate(ct.STATES):
        if carried is not None:
            state = replace(state, squad=carried["squad"], bank=carried["bank"], free_transfers=carried["free_transfers"])
        chip = "wildcard" if state.week == wc else "none"
        realized, detail, carried = PlanEnvV2([state], optimize, chips=chips, wildcard_bench=True).rollout(
            [WeekAction(transfer="auto", chip=chip)], return_state=True)
        chips = carried["chips"]
        recs.append({"week": state.week, "chip": detail[0]["chip"], "realized": realized, "bench_extra": detail[0]["bench_extra"]})
    return {"wc": wc, "weeks": recs}


def variant(wc):
    import signal

    def timed_out(signum, frame):
        raise TimeoutError
    signal.signal(signal.SIGALRM, timed_out)
    signal.alarm(ct.TRAJECTORY_TIMEOUT)
    try:
        return _variant(wc)
    except (TimeoutError, RuntimeError) as exc:
        return {"wc": wc, "failed": f"{type(exc).__name__}: {exc}"}
    finally:
        signal.alarm(0)


def score(traj, wc):
    """(total without a bench boost, bench boost the week after the wildcard, best bench boost in a later week)."""
    weeks = traj["weeks"]
    base = sum(w["realized"] for w in weeks)
    nxt = next((w["bench_extra"] for w in weeks if w["week"] == wc + 1), None)
    later = [w["bench_extra"] for w in weeks if w["week"] > wc]
    return base, nxt, (max(later) if later else None)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--halves", default=",".join(ct.ALL_HALVES))
    ap.add_argument("--workers", type=int, default=12)
    args = ap.parse_args()
    rows, per_half = [], []
    for key in args.halves.split(","):
        season, half = key.split(":"); half = int(half)
        table = json.load(open(OUT / f"{season}_h{half}.json"))
        std = {t["wc"]: t for t in table["trajectories"] if t["fh"] is None and "failed" not in t}
        ct.STATES = ct.half_states(season, half)
        weeks = [s.week for s in ct.STATES]
        wcs = [w for w in weeks[:-1] if w in std]  # a bench boost needs a week after the wildcard
        with ProcessPoolExecutor(max_workers=args.workers) as pool:
            variants = {t["wc"]: t for t in pool.map(variant, wcs, chunksize=1)}
        d_next, d_best, n = [], [], 0
        for w in wcs:
            v = variants[w]
            if "failed" in v:
                rows.append(f"| {key} | {w} | failed: {v['failed']} | | | | |")
                continue
            sb, sn, sl = score(std[w], w)
            vb, vn, vl = score(v, w)
            rows.append(f"| {key} | {w} | {sb:.0f} | {vb - sb:+.0f} | {sn:.0f} | {vn:.0f} | {sl:.0f} | {vl:.0f} | {(vb + vn) - (sb + sn):+.0f} | {(vb + vl) - (sb + sl):+.0f} |")
            d_next.append((vb + vn) - (sb + sn)); d_best.append((vb + vl) - (sb + sl)); n += 1
        best_std = max(((score(std[w], w)[0] + score(std[w], w)[2]), w) for w in wcs)
        best_var = max(((score(variants[w], w)[0] + score(variants[w], w)[2]), w) for w in wcs if "failed" not in variants[w])
        per_half.append((key, n, sum(d_next) / max(n, 1), sum(d_best) / max(n, 1), best_std, best_var))
        print(f"{key}: {n} wildcard weeks; WC+BB next week {sum(d_next) / max(n, 1):+.1f} on average; "
              f"WC+best later BB {sum(d_best) / max(n, 1):+.1f}; hindsight best standard {best_std[0]:.0f} (wc {best_std[1]}) "
              f"vs bench-aware {best_var[0]:.0f} (wc {best_var[1]})", flush=True)
    lines = ["# Wildcard built for a bench boost vs the standard wildcard", "",
             "Closed loop over each half with the planner's transfers, a wildcard at week w and no other chip; the bench boost is then",
             "priced from the counterfactual bench points in week w+1 (the classic combo) or the best later week. Standard = the",
             "chip-timing tables' trajectory (bench credited a tenth of a starter); bench-aware = PlanEnvV2(wildcard_bench=True),",
             "which also credits each bench player his second-week forecast. Deltas are bench-aware minus standard, same w.", "",
             "| half | wildcard weeks | mean Δ (WC + BB next week) | mean Δ (WC + best later BB) | hindsight best standard (w) | hindsight best bench-aware (w) |",
             "|---|---|---|---|---|---|"]
    for key, n, dn, db, bs, bv in per_half:
        lines.append(f"| {key} | {n} | {dn:+.1f} | {db:+.1f} | {bs[0]:.0f} ({bs[1]}) | {bv[0]:.0f} ({bv[1]}) |")
    tot_n = sum(p[1] for p in per_half)
    lines += ["", f"All halves: mean Δ WC+BB next week {sum(p[1] * p[2] for p in per_half) / max(tot_n, 1):+.1f}, "
              f"mean Δ WC+best later BB {sum(p[1] * p[3] for p in per_half) / max(tot_n, 1):+.1f}, "
              f"hindsight-best Δ {sum(p[5][0] - p[4][0] for p in per_half):+.0f} over {len(per_half)} halves.", "",
              "## Every wildcard week", "",
              "| half | w | standard total (no BB) | Δ total (bench-aware − standard) | std BB w+1 | aware BB w+1 | std best later BB | aware best later BB | Δ WC+BB next | Δ WC+best BB |",
              "|---|---|---|---|---|---|---|---|---|---|"] + rows
    (OUT / "wildcard_bench_boost.md").write_text("\n".join(lines) + "\n")
    print("WILDCARD BENCH BOOST DONE")


if __name__ == "__main__":
    main()
