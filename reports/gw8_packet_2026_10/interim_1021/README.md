# GW8 final packet (fixed pipeline)

- **Snapshot:** 2026-10-22T01:17:11+00:00 UTC; deadline 2026-10-23T17:30:00Z.
- **Entry 6535607:** bank £0.2m, free transfers 1, chips used: none. Transfers already made for GW8: none.
- **Selling prices vs the 10-04 app values:** ['Groß: computed 5.8 vs app 5.7', 'João Pedro: computed 7.7 vs app 7.6', 'Cherki: computed 7.8 vs app 7.7'].

## What moved since 2026-10-04

| Player | Status now | News now | GW8 (10-04 → now) | GW8–12 (10-04 → now) |
|---|---|---|---|---|
| Donnarumma | a | — | nan → 2.77 | nan → 14.3 |
| Konsa | a | — | nan → 3.25 | nan → 14.2 |
| Justin | a | — | nan → 3.57 | nan → 15.5 |
| De Cuyper | a | — | nan → 4.11 | nan → 20.6 |
| Cunha | a | — | nan → 3.31 | nan → 16.8 |
| Saka | d | Thigh injury - 50% chance of playing | nan → 4.57 | nan → 22.6 |
| McGinn | a | — | nan → 2.78 | nan → 14.7 |
| Groß | a | — | nan → 4.41 | nan → 23.9 |
| Haaland | a | — | nan → 8.34 | nan → 40.8 |
| João Pedro | a | — | nan → 5.63 | nan → 25.4 |
| Evanilson | a | — | nan → 3.76 | nan → 18.0 |
| Sels | a | — | nan → 2.63 | nan → 12.3 |
| Cherki | a | — | nan → 3.35 | nan → 17.7 |
| N.Williams | a | — | nan → 3.37 | nan → 15.3 |
| Mitchell | a | — | nan → 3.46 | nan → 14.9 |
| Haaland | a | — | nan → 8.34 | nan → 40.8 |
| De Cuyper | a | — | nan → 4.11 | nan → 20.6 |
| E.Le Fée | a | — | nan → 3.39 | nan → 17.1 |
| Xhaka | a | — | nan → 3.50 | nan → 16.1 |
| Rogers | a | — | nan → 5.93 | nan → 26.0 |
| Hall | a | — | nan → 3.88 | nan → 18.0 |

## Options (GW8–12 gain vs holding, net of hits; route scorer from the 10-04 packet)

| Option | Gain now | If rolled to GW8 | Bank after |
|---|---|---|---|
| Cunha → Rogers | +9.2 | +6.6 | 0.1 |
| Cunha + Cherki → Rogers + Mbeumo | +10.2 | +10.8 | 0.1 |
| Donnarumma + Cunha + N.Williams → Verbruggen + Rogers + Calafiori | +11.3 | +10.4 | -0.0 |
| Wildcard (GW8-12) | +5.9 | — | 0.2 |
| Free Hit (GW8 only) | +3.8 | — | 0.2 |

Hold: XI Donnarumma, De Cuyper, Justin, Mitchell, N.Williams, Saka, Groß, Cherki, Haaland, João Pedro, Evanilson; bench Sels > Cunha > Konsa > McGinn; captain Haaland, vice João Pedro.

## Lineups for the leading routes (bench order = entry order, GK first)

- **hold** (bank after 0.2): XI Donnarumma, De Cuyper, Justin, Mitchell, N.Williams, Saka, Groß, Cherki, Haaland, João Pedro, Evanilson; bench Sels > Cunha > Konsa > McGinn; C Haaland, VC João Pedro; GW8 XI forecast 55.7 before hits.

## E20 holdout (2025-26 GW27–38, fixed pipeline)

- base decode FAILED (scoring skipped)
- scoring FAILED
- MAE:
- availability AUC among likely starters (promotion-rule metric): classic 0.549 vs E20 0.727 (n=2439)
- GW27-30: E20 225  classic+F6 266  -41
- GW31-34: E20 216  classic+F6 229  -13
- GW35-38: E20 263  classic+F6 258  +5
- TOTAL: E20 704  classic+F6 753  -49  windows won 1/3 (adapter noise sd ~24/window)

Classic + F6 on the fixed pipeline makes the decision; adapters are logged in shadow. See ../README.md for how to read the route gains and their uncertainty.
