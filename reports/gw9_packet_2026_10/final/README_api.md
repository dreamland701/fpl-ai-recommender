# GW9 final packet (fixed pipeline)

- **Snapshot:** 2026-10-31T09:15:01+00:00 UTC; deadline 2026-10-31T11:00:00Z.
- **Entry 6535607:** bank £1.7m, free transfers 1, chips used: 3xc. Transfers already made for GW9: none.
- **Selling prices vs the app values pasted 2026-10-04:** ['Konsa: computed 4.6 vs app 4.5', 'Cunha: computed 7.8 vs app 7.9', 'Groß: computed 5.8 vs app 5.7', 'Cherki: computed 7.8 vs app 7.7', 'Evanilson: computed 6.1 vs app 6.0', 'João Pedro: computed 7.7 vs app 7.6'].

## Squad and targets as the model sees them

| Player | Status | Chance | News | GW9 | GW9–13 | P(appear) | min |
|---|---|---|---|---|---|---|---|
| Donnarumma | a | -1.0 | — | 2.79 | 13.8 | 0.88 | 79 |
| Konsa | a | 100.0 | — | 3.50 | 16.7 | 0.91 | 82 |
| Justin | a | -1.0 | — | 3.24 | 15.1 | 0.90 | 81 |
| De Cuyper | a | -1.0 | — | 4.21 | 21.0 | 0.92 | 82 |
| Mitchell | a | -1.0 | — | 2.90 | 13.4 | 0.90 | 81 |
| Cunha | a | -1.0 | — | 3.22 | 16.6 | 0.66 | 60 |
| Rogers | a | -1.0 | — | 5.71 | 25.9 | 1.00 | 90 |
| Groß | a | -1.0 | — | 4.69 | 24.0 | 0.98 | 88 |
| Cherki | a | -1.0 | — | 3.54 | 18.4 | 0.51 | 46 |
| Haaland | a | 100.0 | — | 8.38 | 41.6 | 1.00 | 90 |
| Evanilson | a | -1.0 | — | 5.44 | 23.4 | 1.00 | 90 |
| Sels | a | -1.0 | — | 2.48 | 12.1 | 0.87 | 78 |
| João Pedro | i | 0.0 | Thigh injury - Unknown return date | 0.00 | 6.5 | 0.00 | 0 |
| N.Williams | a | 100.0 | — | 3.28 | 15.9 | 0.87 | 78 |
| McGinn | a | -1.0 | — | 3.39 | 16.1 | 0.81 | 72 |
| Calafiori | d | 75.0 | Hip injury - 75% chance of playing | 2.42 | 14.7 | 0.46 | 41 |
| Gabriel | a | -1.0 | — | 5.43 | 25.8 | 1.00 | 90 |
| Timber | d | 75.0 | Hamstring injury - 75% chance of playing | 1.08 | 7.1 | 0.29 | 26 |

## What moved since the interim packet

| Player | Status now | News now | GW9 (interim → now) | GW9–13 (interim → now) |
|---|---|---|---|---|
| Konsa | a | — | 3.34 → 3.50 | 16.2 → 16.7 |
| Rogers | a | — | 5.54 → 5.71 | 25.4 → 25.9 |
| Cherki | a | — | 3.78 → 3.54 | 19.2 → 18.4 |
| Evanilson | a | — | 4.32 → 5.44 | 19.8 → 23.4 |
| João Pedro | i | Thigh injury - Unknown return date | 3.57 → 0.00 | 18.7 → 6.5 |
| N.Williams | a | — | 2.80 → 3.28 | 14.2 → 15.9 |
| Calafiori | d | Hip injury - 75% chance of playing | 3.31 → 2.42 | 17.6 → 14.7 |
| Rogers | a | — | 5.54 → 5.71 | 25.4 → 25.9 |
| Konsa | a | — | 3.34 → 3.50 | 16.2 → 16.7 |
| João Pedro | i | Thigh injury - Unknown return date | 3.57 → 0.00 | 18.7 → 6.5 |
| N.Williams | a | — | 2.80 → 3.28 | 14.2 → 15.9 |
| Cherki | a | — | 3.78 → 3.54 | 19.2 → 18.4 |
| Gabriel | a | — | 5.11 → 5.43 | 24.8 → 25.8 |

## Exact optimizer (GW9–13 value vs holding, net of hits)

| Route | Gain | Hit | Bank after | Captain |
|---|---|---|---|---|
| GW9-13, max 1: João Pedro → N.Jackson | +12.5 | 0 | 2.5 | Haaland |
| GW9-13, max 2: João Pedro + McGinn → N.Jackson + Tavernier | +17.2 | 4 | 1.4 | Haaland |
| GW9-13, max 3: Mitchell + Cunha + João Pedro → Gabriel + N.Jackson + Tavernier | +23.3 | 8 | 0.3 | Haaland |
| GW9-13 wildcard | +45.9 | — | 0.1 | Haaland |
| GW9 only, max 1: João Pedro → N.Jackson | +3.8 | 0 | 2.5 | Haaland |
| GW9 only, max 2: João Pedro → N.Jackson | +3.8 | 0 | 2.5 | Haaland |
| GW9 only, max 3: João Pedro → N.Jackson | +3.8 | 0 | 2.5 | Haaland |
| GW9 only free hit | +12.2 | — | -0.0 | Haaland |

## Enumerated routes (decision sheet, GW9–13 gain vs holding, net of hits)

| Option | Gain now | If rolled | Bank after |
|---|---|---|---|
| João Pedro → N.Jackson | +12.5 | +8.8 | 2.5 |
| João Pedro + McGinn → N.Jackson + Tavernier | +17.2 | +14.9 | 1.4 |
| Mitchell + Cunha + João Pedro → Gabriel + Tavernier + N.Jackson | +23.3 | +18.8 | 0.3 |
| Wildcard (GW9-13) | +12.9 | — | 0.1 |
| Free Hit (GW9 only) | +7.2 | — | 0.2 |

Hold: XI Donnarumma, De Cuyper, Konsa, N.Williams, Justin, Rogers, Groß, Cherki, McGinn, Haaland, Evanilson; bench Sels > Cunha > Mitchell > João Pedro; captain Haaland, vice Rogers.

## Lineups for the leading routes (bench order = entry order, GK first)

- **hold** (bank after 1.7): XI Donnarumma, De Cuyper, Konsa, N.Williams, Justin, Rogers, Groß, Cherki, McGinn, Haaland, Evanilson; bench Sels > Cunha > Mitchell > João Pedro; C Haaland, VC Rogers; GW9 XI forecast 56.6 before hits.
- **Konsa -> Calafiori (1 FT, no hit)** (bank after 0.4): XI Donnarumma, De Cuyper, N.Williams, Justin, Rogers, Groß, Cherki, McGinn, Cunha, Haaland, Evanilson; bench Sels > Mitchell > Calafiori > João Pedro; C Haaland, VC Rogers; GW9 XI forecast 56.3 before hits.
- **João Pedro -> N.Jackson (GW9-13, max 1 moves, hit 0)** (bank after 2.5): XI Donnarumma, De Cuyper, Konsa, N.Williams, Rogers, Groß, Cherki, McGinn, Haaland, N.Jackson, Evanilson; bench Sels > Justin > Cunha > Mitchell; C Haaland, VC N.Jackson; GW9 XI forecast 60.0 before hits.
- **João Pedro + McGinn -> N.Jackson + Tavernier (GW9-13, max 2 moves, hit 4)** (bank after 1.4): XI Donnarumma, De Cuyper, Konsa, N.Williams, Tavernier, Rogers, Groß, Cherki, Haaland, N.Jackson, Evanilson; bench Sels > Justin > Cunha > Mitchell; C Haaland, VC N.Jackson; GW9 XI forecast 62.5 before hits.
- **João Pedro -> N.Jackson (GW9 only, max 1 moves, hit 0)** (bank after 2.5): XI Donnarumma, De Cuyper, Konsa, N.Williams, Rogers, Groß, Cherki, McGinn, Haaland, N.Jackson, Evanilson; bench Sels > Justin > Cunha > Mitchell; C Haaland, VC N.Jackson; GW9 XI forecast 60.0 before hits.

## Role-override sheet (new signings / role changes the ridge cannot see)

See [role_override_sheet.md](role_override_sheet.md).

## Classic vs classic + SFT (H5), with the text behind each move

See [side_by_side_h5.md](side_by_side_h5.md).

Classic + F6 on the fixed pipeline makes the decision; the SFT arm is logged in shadow. See ../README.md for how to read the route gains and their uncertainty.
