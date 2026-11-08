"""Exact squad optimizer (transfers or wildcard) for the route-scorer objective.

maximise  sum v_i*s_i + sum v_i*c_i + 0.1 * sum_outfield v_i*(x_i - s_i) - HIT*h
  x_i = in the 15, s_i = in the XI, c_i = captain
subject to the squad shape (2 GK, 5 DEF, 5 MID, 3 FWD), a legal XI (1 GK,
3-5 DEF, 2-5 MID, 1-3 FWD), at most 3 per club, and the selling-price budget:
kept players cost their selling price, new ones their current price, against
bank + the selling value of the current squad. Without a wildcard, transfers
beyond the free ones cost HIT points each (h >= transfers - free).

It replaces two shortcuts in the existing tools: the transfer search that only
sells the six weakest players (review item P2) and a draft that ignores the
captain. New signings with status u/i/s/n are excluded; owned players can stay.
"""
from __future__ import annotations

from typing import Dict, Iterable, Mapping, Optional

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp

HIT = 4
SQUAD = {"GK": 2, "DEF": 5, "MID": 5, "FWD": 3}
XI_BOUNDS = {"GK": (1, 1), "DEF": (3, 5), "MID": (2, 5), "FWD": (1, 3)}
UNAVAILABLE = {"u", "i", "s", "n"}


def optimize(
    F: Mapping[int, dict],
    value: Mapping[int, float],
    current_sell: Mapping[int, float],
    bank: float,
    free_transfers: int = 1,
    wildcard: bool = False,
    max_transfers: Optional[int] = None,
    forced_in: Iterable[int] = (),
    forced_out: Iterable[int] = (),
    bench_value: Optional[Mapping[int, float]] = None,
) -> Dict[str, object]:
    """`bench_value[pid]` replaces the default bench credit (a tenth of an outfield player's value,
    nothing for the second keeper): a wildcard played to set up a bench boost values all fifteen."""
    ids = [pid for pid, r in F.items() if pid in current_sell or r["status"] not in UNAVAILABLE]
    n = len(ids)
    v = np.array([float(value[pid]) for pid in ids])
    outfield = np.array([F[pid]["pos"] != "GK" for pid in ids], dtype=float)
    bench = 0.1 * v * outfield if bench_value is None else np.array([float(bench_value[pid]) for pid in ids])
    cost = np.array([float(current_sell[pid]) if pid in current_sell else float(F[pid]["price"]) for pid in ids])
    new = np.array([pid not in current_sell for pid in ids], dtype=float)
    # variables: x (n), s (n), c (n), h (1)
    size = 3 * n + 1
    objective = np.zeros(size)
    objective[:n] = -bench
    objective[n:2 * n] = -(v - bench)
    objective[2 * n:3 * n] = -v
    objective[-1] = 0.0 if wildcard else HIT
    rows, lower, upper = [], [], []

    def add(coefs, lo, hi):
        rows.append(coefs)
        lower.append(lo)
        upper.append(hi)

    def block(part, mask):
        row = np.zeros(size)
        row[part * n:(part + 1) * n] = mask
        return row

    for pos, count in SQUAD.items():
        mask = np.array([F[pid]["pos"] == pos for pid in ids], dtype=float)
        add(block(0, mask), count, count)
        lo, hi = XI_BOUNDS[pos]
        add(block(1, mask), lo, hi)
    add(block(1, np.ones(n)), 11, 11)
    add(block(2, np.ones(n)), 1, 1)
    for i in range(n):
        row = np.zeros(size); row[n + i] = 1; row[i] = -1
        add(row, -np.inf, 0)          # s_i <= x_i
        row = np.zeros(size); row[2 * n + i] = 1; row[n + i] = -1
        add(row, -np.inf, 0)          # c_i <= s_i
    # at most three per club; a squad that already holds more (two of its players joined the same club in a
    # transfer window: Guehi and Semenyo, 2025-26 week 23) may keep them, as FPL allows, but not add to them
    held = {}
    for pid in current_sell:
        if pid in F:
            held[F[pid]["team_id"]] = held.get(F[pid]["team_id"], 0) + 1
    for team in {F[pid]["team_id"] for pid in ids}:
        mask = np.array([F[pid]["team_id"] == team for pid in ids], dtype=float)
        add(block(0, mask), 0, max(3, held.get(team, 0)))
    budget = bank + sum(current_sell.values())
    add(block(0, cost), -np.inf, budget + 1e-6)
    if not wildcard:
        row = block(0, new); row[-1] = -1
        add(row, -np.inf, free_transfers)  # transfers - h <= free
    if max_transfers is not None:
        add(block(0, new), 0, max_transfers)
    lo_bounds = np.zeros(size)
    hi_bounds = np.ones(size)
    hi_bounds[-1] = 15
    index = {pid: i for i, pid in enumerate(ids)}
    for pid in forced_in:
        lo_bounds[index[pid]] = 1
    for pid in forced_out:
        if pid in index:
            hi_bounds[index[pid]] = 0
    integrality = np.ones(size)
    result = milp(objective, constraints=LinearConstraint(np.array(rows), lower, upper),
                  integrality=integrality, bounds=Bounds(lo_bounds, hi_bounds),
                  options={"time_limit": 120})
    if result.x is None:
        raise RuntimeError(f"optimizer failed: {result.message}")
    x = result.x
    squad = [ids[i] for i in range(n) if x[i] > 0.5]
    xi = [ids[i] for i in range(n) if x[n + i] > 0.5]
    captain = next(ids[i] for i in range(n) if x[2 * n + i] > 0.5)
    hits = 0 if wildcard else int(round(x[-1]))
    spent = sum(cost[index[pid]] for pid in squad)
    return {
        "squad": squad, "xi": xi, "captain": captain,
        "out": [pid for pid in current_sell if pid not in squad],
        "in": [pid for pid in squad if pid not in current_sell],
        "score": float(-result.fun) + (0 if wildcard else HIT * hits),
        "hits": hits, "net": float(-result.fun), "bank_after": round(budget - spent, 1),
    }
