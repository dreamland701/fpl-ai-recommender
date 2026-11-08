# GW9 final packet (fixed pipeline)

- **Snapshot:** 2026-10-28T22:35:01+00:00 UTC; deadline 2026-10-31T11:00:00Z.
- **Entry 6535607:** bank £1.7m, free transfers 1, chips used: 3xc. Transfers already made for GW9: none.
- **Selling prices vs the app values pasted 2026-10-04:** ['Konsa: computed 4.6 vs app 4.5', 'Cunha: computed 7.8 vs app 7.9', 'Groß: computed 5.8 vs app 5.7', 'Cherki: computed 7.8 vs app 7.7', 'Evanilson: computed 6.1 vs app 6.0', 'João Pedro: computed 7.7 vs app 7.6'].

## Squad and targets as the model sees them

| Player | Status | Chance | News | GW9 | GW9–13 | P(appear) | min |
|---|---|---|---|---|---|---|---|
| Donnarumma | a | -1.0 | — | 2.82 | 13.9 | 0.88 | 80 |
| Konsa | a | 100.0 | — | 3.37 | 16.3 | 0.89 | 80 |
| Justin | a | -1.0 | — | 3.24 | 15.1 | 0.90 | 81 |
| De Cuyper | a | -1.0 | — | 4.25 | 21.1 | 0.92 | 83 |
| Mitchell | a | -1.0 | — | 2.94 | 13.5 | 0.91 | 82 |
| Cunha | a | -1.0 | — | 3.27 | 16.8 | 0.67 | 60 |
| Rogers | a | -1.0 | — | 5.55 | 25.4 | 1.00 | 90 |
| Groß | a | -1.0 | — | 4.81 | 24.4 | 1.00 | 90 |
| Cherki | a | -1.0 | — | 3.73 | 19.0 | 0.54 | 49 |
| Haaland | a | 100.0 | — | 8.28 | 41.2 | 1.00 | 90 |
| Evanilson | a | -1.0 | — | 4.56 | 20.6 | 0.95 | 86 |
| Sels | a | -1.0 | — | 2.48 | 12.1 | 0.87 | 78 |
| João Pedro | i | 0.0 | Thigh injury - Unknown return date | 2.46 | 15.1 | 0.32 | 28 |
| N.Williams | d | 75.0 | Arm injury - 75% chance of playing | 2.80 | 14.2 | 0.76 | 69 |
| McGinn | a | -1.0 | — | 3.34 | 15.9 | 0.80 | 72 |
| Calafiori | d | 75.0 | Hip injury - 75% chance of playing | 3.15 | 17.1 | 0.57 | 51 |
| Gabriel | a | -1.0 | — | 5.17 | 25.0 | 1.00 | 90 |
| Timber | d | 75.0 | Hamstring injury - 75% chance of playing | 1.08 | 7.1 | 0.29 | 26 |

## What moved since the interim packet

| Player | Status now | News now | GW9 (interim → now) | GW9–13 (interim → now) |
|---|---|---|---|---|
| Evanilson | a | — | 4.32 → 4.56 | 19.8 → 20.6 |
| João Pedro | i | Thigh injury - Unknown return date | 3.57 → 2.46 | 18.7 → 15.1 |
| Calafiori | d | Hip injury - 75% chance of playing | 3.31 → 3.15 | 17.6 → 17.1 |
| João Pedro | i | Thigh injury - Unknown return date | 3.57 → 2.46 | 18.7 → 15.1 |

## Exact optimizer (GW9–13 value vs holding, net of hits)

| Route | Gain | Hit | Bank after | Captain |
|---|---|---|---|---|
| GW9-13, max 1: João Pedro → Thiago | +7.2 | 0 | 1.6 | Haaland |
| GW9-13, max 2: Cunha + N.Williams → Gabriel + Tavernier | +11.2 | 4 | 0.2 | Haaland |
| GW9-13, max 3: Cunha + João Pedro + N.Williams → Gabriel + Tavernier + Thiago | +14.4 | 8 | 0.1 | Haaland |
| GW9-13 wildcard | +35.8 | — | -0.0 | Haaland |
| GW9 only, max 1: João Pedro → N.Jackson | +2.1 | 0 | 2.6 | Haaland |
| GW9 only, max 2: João Pedro → N.Jackson | +2.1 | 0 | 2.6 | Haaland |
| GW9 only, max 3: João Pedro → N.Jackson | +2.1 | 0 | 2.6 | Haaland |
| GW9 only free hit | +8.9 | — | -0.0 | Haaland |

## Enumerated routes (decision sheet, GW9–13 gain vs holding, net of hits)

| Option | Gain now | If rolled | Bank after |
|---|---|---|---|
| João Pedro → Thiago | +7.2 | +5.5 | 1.6 |
| Cunha + N.Williams → Tavernier + Gabriel | +11.2 | +11.7 | 0.2 |
| Cunha + João Pedro + N.Williams → Tavernier + Thiago + Gabriel | +14.4 | +13.2 | 0.1 |
| Wildcard (GW9-13) | +2.5 | — | 0.6 |
| Free Hit (GW9 only) | +2.7 | — | 0.7 |

Hold: XI Donnarumma, De Cuyper, Konsa, Justin, Rogers, Groß, Cherki, McGinn, Cunha, Haaland, Evanilson; bench Sels > Mitchell > N.Williams > João Pedro; captain Haaland, vice Rogers.

## Lineups for the leading routes (bench order = entry order, GK first)

- **hold** (bank after 1.7): XI Donnarumma, De Cuyper, Konsa, Justin, Rogers, Groß, Cherki, McGinn, Cunha, Haaland, Evanilson; bench Sels > Mitchell > N.Williams > João Pedro; C Haaland, VC Rogers; GW9 XI forecast 55.5 before hits.
- **Konsa -> Calafiori (1 FT, no hit)** (bank after 0.3): XI Donnarumma, De Cuyper, Justin, Calafiori, Rogers, Groß, Cherki, McGinn, Cunha, Haaland, Evanilson; bench Sels > Mitchell > N.Williams > João Pedro; C Haaland, VC Rogers; GW9 XI forecast 55.3 before hits.
- **João Pedro -> Thiago (GW9-13, max 1 moves, hit 0)** (bank after 1.6): XI Donnarumma, De Cuyper, Konsa, Justin, Rogers, Groß, Cherki, McGinn, Haaland, Thiago, Evanilson; bench Sels > Cunha > Mitchell > N.Williams; C Haaland, VC Rogers; GW9 XI forecast 56.9 before hits.
- **Cunha + N.Williams -> Gabriel + Tavernier (GW9-13, max 2 moves, hit 4)** (bank after 0.2): XI Donnarumma, Gabriel, De Cuyper, Konsa, Rogers, Groß, Tavernier, Cherki, McGinn, Haaland, Evanilson; bench Sels > Justin > Mitchell > João Pedro; C Haaland, VC Rogers; GW9 XI forecast 59.0 before hits.
- **João Pedro -> N.Jackson (GW9 only, max 1 moves, hit 0)** (bank after 2.6): XI Donnarumma, De Cuyper, Konsa, Justin, Rogers, Groß, Cherki, McGinn, Haaland, N.Jackson, Evanilson; bench Sels > Cunha > Mitchell > N.Williams; C Haaland, VC Rogers; GW9 XI forecast 57.3 before hits.

## Role-override sheet (new signings / role changes the ridge cannot see)

See [role_override_sheet.md](role_override_sheet.md).

Classic + F6 on the fixed pipeline makes the decision; the SFT arm is logged in shadow. See ../README.md for how to read the route gains and their uncertainty.
