"""Official FPL squad and scoring rules shared by live play and backtests."""

from __future__ import annotations

from collections import Counter
from typing import Dict, List, Mapping, Sequence, Tuple

from .config import STARTING_XI_MAXIMUMS, STARTING_XI_MINIMUMS, STARTING_XI_SIZE

POSITION_ORDER = ("GK", "DEF", "MID", "FWD")


def is_legal_xi(position_counts: Mapping[str, int]) -> bool:
    if sum(position_counts.values()) != STARTING_XI_SIZE:
        return False
    if any(position not in STARTING_XI_MINIMUMS for position, count in position_counts.items() if count):
        return False
    return all(
        STARTING_XI_MINIMUMS[position] <= position_counts.get(position, 0) <= STARTING_XI_MAXIMUMS[position]
        for position in STARTING_XI_MINIMUMS
    )


def selling_price(purchase_price: float, current_price: float) -> float:
    """Half of any rise (rounded down to 0.1m) is kept; falls are taken in full."""
    purchase_tenths = int(round(purchase_price * 10))
    current_tenths = int(round(current_price * 10))
    if current_tenths <= purchase_tenths:
        return current_tenths / 10.0
    return (purchase_tenths + (current_tenths - purchase_tenths) // 2) / 10.0


def automatic_substitutions(
    positions: Mapping[int, str],
    starters: Sequence[int],
    bench_order: Sequence[int],
    minutes: Mapping[int, float],
) -> Tuple[List[int], List[Tuple[int, int]]]:
    """Return (players whose points count, [(starter_out, substitute_in)]).

    Each starter who did not play is replaced by the highest-priority bench
    player who played and keeps the XI legal. Unreplaced starters keep their
    slot for formation purposes and score nothing, so a bench that cannot fill
    every gap still fills the gaps it legally can.
    """

    def played(player_id: int) -> bool:
        return minutes.get(player_id, 0.0) > 0

    slot_order = sorted(
        range(len(starters)),
        key=lambda slot: (POSITION_ORDER.index(positions[starters[slot]]), slot),
    )
    lineup = list(starters)
    used: set = set()
    substitutions: List[Tuple[int, int]] = []
    for slot in slot_order:
        starter = lineup[slot]
        if played(starter):
            continue
        for substitute in bench_order:
            if substitute in used or substitute in lineup or not played(substitute):
                continue
            counts: Dict[str, int] = Counter(positions[player_id] for player_id in lineup)
            counts[positions[starter]] -= 1
            counts[positions[substitute]] += 1
            if not is_legal_xi(counts):
                continue
            lineup[slot] = substitute
            used.add(substitute)
            substitutions.append((starter, substitute))
            break
    return [player_id for player_id in lineup if played(player_id)], substitutions
