# GW8 ledger (settled 2026-10-25; scored 2026-10-26 09:15 PDT from the public API: `entry/picks_gw8.json`, `entry/history_settled.json`, `entry/live_gw8.json`, `entry/transfers_settled.json`)

| | |
|---|---|
| Entered move | Saka → Rogers (free; sold 9.5, bought 8.0, bank 1.7), the packet's recommendation. Captain Haaland on the **Triple Captain** chip (the recommendation said no chip; the G8 chip line had priced TC +8.4 this week as the best of the next four). Vice João Pedro. |
| GW8 points | **55** with the chip (47 at a plain captain); league average 45; bench 16 (Sels 2, N.Williams 8, McGinn 6; João Pedro 0 after the auto-sub) |
| Overall rank | 3,721,584 → 3,147,238; season total 486 |
| Expected (own forecasts, final Saka-out sheet) | entered XI 57.7 plain / 66.1 with TC; classic standard 57.9; Konsa-nailed 57.9; classic+SFT 54.1 (its own forecasts) |

Entered XI (3-4-3 after the override): Donnarumma 1; Konsa 14 (goal, clean sheet, 2 bonus), Justin 6, De Cuyper 1, Mitchell 1;
Cunha 1 (45 min), Rogers 1 (90 min, booked), Groß 0 (90 min); Haaland 8 ×3 = 24 (goal, 2 bonus in the 2-1 defeat at
Villa), João Pedro 0 minutes, Evanilson 6 (goal). Bench as entered: Sels 2 > Cherki 0 > N.Williams 8 > McGinn 6.
Auto-sub: João Pedro out, Cherki in (45 min, booked, 0). Saka 0 minutes (out, "unknown return date"), sold.

João Pedro did not play at Chelsea v Spurs (0-2): status "a", no news and no Guardian mention at the Friday snapshot;
P(appear) classic 0.91 / SFT 0.97; neither pipeline had a warning. The feed now carries "unspecified injury, 75%".
Same shape as Cherki in GW7: an unflagged absence the day of the game, which no pre-deadline reader can see.

## Judgment calls

| Call | Verdict | Numbers |
|---|---|---|
| Transfer Saka → Rogers (free) | RIGHT in direction, 0 on the day | Saka 0 minutes (would have sat on the bench anyway); Rogers 1 vs Cunha 1, who would have started in a hold |
| Not taking Konsa + Saka → Calafiori + Rogers (−4) | RIGHT | Calafiori 1 (22 min, now d/75% hip) vs Konsa 14: the double would have been −17 net this week |
| Captain Haaland | RIGHT | 8 raw, second in the squad behind Konsa 14; most-captained player league-wide; forecast 8.44 |
| Triple Captain on Haaland (Wes's call; sheet said no chip) | PAR, +8 | 24 vs 16; projected +8.4. Face-value realisation, but it spends the chip on an ordinary week; chip-timing study says TC timing is luck (oracle 6.4 vs random 7.0) |
| Konsa over N.Williams (Wes's nailed call, role sheet +0.2) | RIGHT, +6 | Konsa 14 vs N.Williams 8; both played 83+ |
| Cunha over Cherki (Wes's call; SFT agreed, classic order was Cherki) | NEUTRAL, +1 | Cunha 1 vs Cherki 0, both 45 minutes |
| Bench order Cherki > N.Williams > McGinn | −8 | João Pedro's slot went to Cherki 0; N.Williams 8 was a legal sub (5-3-2). The model's own order (Cherki 3.49 > N.Williams 3.35) would have done the same |
| João Pedro started, 0 minutes | MISS | no warning in the feed, the Guardian store, or either forecast; P(appear) 0.91 / 0.97 |

Scorecard: TC +8 (par), Konsa +6, Cunha +1, transfer 0, bench order −8, João Pedro −5.7 vs forecast. Net of the chip
the week was 47 against an average of 45; with it 55, +10.

## Classic vs classic+SFT XI in hindsight (realised points, auto-subs applied, plain captain unless stated)

| XI | Expected (classic forecasts) | Realised | Auto-sub |
|---|---|---|---|
| Wes entered, TC Haaland | 66.1 | **55** | Cherki 0 for João Pedro |
| Wes entered, plain captain | 57.7 | 47 | Cherki 0 |
| Classic standard sheet (N.Williams, Cherki in; bench Konsa first) | 57.9 | 54 | Konsa 14 for João Pedro |
| Classic, Konsa nailed (override sheet; bench N.Williams first) | 57.9 | 54 | N.Williams 8 |
| Classic + SFT H1, Wednesday read (Cunha in; bench Cherki first) | 57.7 (54.1 own) | 41 | Cherki 0 |
| Hold Saka, classic (Cunha starts, Saka benched) | 55.1 | 54 | Konsa 14 |
| MILP wildcard squad (+48.0 projected GW8-12), forecast XI | 66.5 | 39 | Thomas for João Pedro |
| Free Hit squad (+11.9 projected), forecast XI | 66.6 | 32 | Thomas |

The SFT XI's one player-specific call, Cunha over Cherki, was +1 on the day. Its 13-point gap to the classic sheet is the
auto-sub path (Cherki 0 vs Konsa 14 into João Pedro's slot), which follows from where each sheet placed Konsa and
Cherki, not from a forecast the adapter changed; the generic shrink again moved nobody across a decision line. The
wildcard and Free Hit squads, projected +48 over five weeks and +12 for the week, scored 39 and 32 against the hold's 54:
Palmer −1, Mbeumo 2, Rogers 1, Calafiori 1, João Pedro 0 (chip-calibration note holds: WC projections do not realise).

## H1 shadow accuracy (`h1_gw8_accuracy.md`; interim corpus of 2026-10-21, the final read never ran: GPU on the 31B backfill)

668 players: RMSE classic 2.107 vs SFT 2.136, MAE 1.172 vs 1.249, bias −0.06 vs −0.40; on the 19 decision-relevant
rows (classic ≥ 4, below the tracker's 20-row floor so computed by hand) RMSE 4.567 vs 4.495, SFT closer on 74%: the
constant shrink helped on a week where the top forecasts under-delivered (Rogers 1, João Pedro 0, Palmer −1, B.Fernandes 0;
Gabriel 17 the exception). Same profile as every live week: a little worse overall, a little better on the ≥ 4 rows, no
player-specific information.

## Carried forward to GW9

- Free move candidate Konsa → Calafiori is now doubtful on both ends: Konsa 14 and five+ straight starts; Calafiori 22
  minutes and a hip flag (d/75%). Re-check on the GW9 sheet after the Monday ingest.
- Chips left: Bench Boost, Free Hit, Wildcard (TC used GW8).
- N.Williams now d/75% (arm). João Pedro d/75%.
- Open fixes before the GW9 packet: decide step must zero forecasts for status i/s with chance 0 (Saka needed a hand-built
  scenario twice); the chip-line tag mismatch in `run_gw8_final_refresh.sh`.
