# GW7 ledger (settled 2026-10-19; scored 2026-10-21 from the public API, `entry/picks_gw7.json`, `entry/history_settled.json`)

| | |
|---|---|
| Entered move | Isak → Haaland, B.Fernandes → McGinn (−4), the packet's leading route; captain Haaland |
| GW7 points | 68 gross, 64 net of the hit; league average 59; bench 5 (Sels 2, N.Williams 3, Mitchell 0) |
| Overall rank | 3,876,191 → 3,721,584 |
| Expected (own forecasts, sheet) | 61.3 classic / 58.2 classic+SFT |

Per-player realised: Haaland 13 (captain, 26) vs Isak 9 out; McGinn 1 vs B.Fernandes 1 out; Konsa 9, Evanilson 12,
De Cuyper 6, Groß 5, Saka 3, Justin 2, João Pedro 2, Cunha 1 (6 minutes), Donnarumma 1. Cherki did not play
(0 minutes, status "a", P(appear) classic 0.95 / SFT 0.97: neither pipeline had a warning, consistent with the
article audit), auto-sub McGinn 1.

Classic vs classic+SFT XI in hindsight: the classic XI (Evanilson started, McGinn benched) is the entered team, 68.
The SFT XI (McGinn started over Evanilson) also lands on 68, but only because Cherki's absence auto-subbed
Evanilson's 12 back in; the SFT's own call, McGinn 1 over Evanilson 12, was −11 on the day. The generic shrink
moved nobody across a decision line; the one player-specific move it made was wrong.

H1 shadow read, final corpus, scored on the settled week (`h1_gw7_accuracy.md`, 667 players): RMSE classic 1.995 vs
SFT 2.028, MAE 1.113 vs 1.193, bias −0.02 vs −0.35; on the 21 decision-relevant rows (classic ≥ 4) RMSE 3.673 vs
3.643. The generic shrink cost accuracy on the week overall, as in every live week so far.
