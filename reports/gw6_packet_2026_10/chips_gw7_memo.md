# Chips for GW7? (2026-10-06)

## Verdict

**No chip in GW7.**

- Do the plan: GW6 Bijol → De Cuyper; GW7 Bruno + Isak → Haaland + Xhaka (−4).
- Decide on the Triple Captain at the GW7 deadline, once you've seen Haaland's GW6.
- Keep the Wildcard for a real structural problem, and play it no later than about GW14–16. Then Bench Boost the week after.
- Keep the Free Hit for a crisis week.

All four first-half chips expire after GW19 (deadline 1 January 2027).

## What the numbers say

**Exact optimizer** (`squad_milp.py`). It maximises the route score (best legal XI + captain doubled + 0.1 × outfield bench) under every squad rule. Results below are GW7–10 gains against keeping the post-GW6 squad, from `chips_gw7.py`:

| Option | Gain | Transfers |
|---|---|---|
| Best single transfer | +3.8 | Cunha → Rogers |
| **Best two transfers = the plan** | **+7.9** | Bruno + Isak → Haaland + Xhaka (−4) |
| Best three transfers | +10.1 | Cunha + Isak + João Pedro → Kusi-Asare + Slater + Haaland (−8) |
| Best of any number | +10.7 | four transfers (−12) |
| Wildcard | +36.4 | keeps De Cuyper, Groß, Bruno; adds Haaland as captain; 4 non-playing bench fodder |
| Wildcard with every new signing likely to play (P ≥ 0.6) | +35.1 | 12 changes |

The optimizer independently picks your planned move as the best two-transfer move. The old decision layer could never find it, because it only sells the six weakest players.

**History says projected Wildcard gains don't turn into points** (`reports/review_fixes_2026_10/run_chip_replay.sh`, 21 windows, fixed pipeline):

- When the backtest played a Wildcard on a projected gain of at least 12 points, it fired 14 times.
- Projected gain averaged +16.8; realised averaged **−0.7** over the remaining weeks (spread ±21 per window).
- The Free Hit fired 5 times: +5.4 a time, which is noise.
- Caveat: backtest squads are freshly drafted every four weeks, so their Wildcards chase noise more than yours would. Your squad has real holes, but the plan already fixes the two biggest.

**Why the GW7 Wildcard's +27 edge over the plan shouldn't be trusted:** it comes from replacing a dozen players with the model's favourites, each 1–3 points better over four weeks. That is exactly where the replay shows no realised skill. It would also spend the Wildcard on problems that are partly temporary: João Pedro back later in October, Konsa a dead leg, Isak minor.

## The other chips

- **No blank or double gameweeks are scheduled in GW6–19.** That removes the usual reasons for Free Hit and Bench Boost.
- **Triple Captain:** City's easiest first-half home games (fixture rating 2) are GW7 Ipswich, GW11 Fulham, GW16 Hull and GW19 Spurs. They are worth roughly the same in expectation.
  - If Haaland plays a normal 90 at Anfield and City's press conference is clean, GW7 against Ipswich is a good use.
  - If not, hold it for GW11 or GW16.
- **Bench Boost:** best the week after a Wildcard built with a playing bench (the P ≥ 0.6 squad above is that kind). Without doubles, that pairing is the strongest use.
- **Free Hit:** keep it for a week with three or more absentees. Otherwise burn it on a strong one-week team by GW19.

## What E20 and the rest of this round add

- **E20** confirms the adapter can read availability (holdout AUC 0.55 → 0.73) but doesn't pick better squads (−49 over three windows). Nothing in it changes these picks.
- **New and useful:**
  - the exact optimizer (fixes the review's "candidate pruning" gap)
  - the chip calibration above
  - the City post-break rotation finding
