# GW9 interim packet (fixed pipeline)

- **Snapshot:** 2026-10-27T15:41:24+00:00 UTC; deadline 2026-10-31T11:00:00Z.
- **Entry 6535607:** bank £1.7m, free transfers 1, chips used: 3xc. Transfers already made for GW9: none.
- **Selling prices vs the app values pasted 2026-10-04:** ['Konsa: computed 4.6 vs app 4.5', 'Groß: computed 5.8 vs app 5.7', 'Cherki: computed 7.8 vs app 7.7', 'Evanilson: computed 6.1 vs app 6.0', 'João Pedro: computed 7.7 vs app 7.6'].

## Squad and targets as the model sees them

| Player | Status | Chance | News | GW9 | GW9–13 | P(appear) | min |
|---|---|---|---|---|---|---|---|
| Donnarumma | a | -1.0 | — | 2.82 | 13.9 | 0.88 | 80 |
| Konsa | a | 100.0 | — | 3.34 | 16.2 | 0.89 | 80 |
| Justin | a | -1.0 | — | 3.24 | 15.1 | 0.90 | 81 |
| De Cuyper | a | -1.0 | — | 4.25 | 21.1 | 0.92 | 83 |
| Mitchell | a | -1.0 | — | 2.94 | 13.5 | 0.91 | 82 |
| Cunha | a | -1.0 | — | 3.34 | 17.0 | 0.68 | 61 |
| Rogers | a | -1.0 | — | 5.54 | 25.4 | 1.00 | 90 |
| Groß | a | -1.0 | — | 4.82 | 24.4 | 1.00 | 90 |
| Cherki | a | -1.0 | — | 3.78 | 19.2 | 0.55 | 49 |
| Haaland | a | 100.0 | — | 8.21 | 41.1 | 1.00 | 90 |
| Evanilson | a | -1.0 | — | 4.32 | 19.8 | 0.91 | 82 |
| Sels | a | -1.0 | — | 2.48 | 12.1 | 0.87 | 78 |
| João Pedro | i | 0.0 | Thigh injury - Unknown return date | 3.57 | 18.7 | 0.48 | 44 |
| N.Williams | d | 75.0 | Arm injury - 75% chance of playing | 2.80 | 14.2 | 0.76 | 69 |
| McGinn | a | -1.0 | — | 3.32 | 15.8 | 0.80 | 72 |
| Calafiori | d | 75.0 | Hip injury - 75% chance of playing | 3.31 | 17.6 | 0.59 | 54 |
| Gabriel | a | -1.0 | — | 5.11 | 24.8 | 1.00 | 90 |
| Timber | d | 75.0 | Hamstring injury - 75% chance of playing | 1.08 | 7.1 | 0.29 | 26 |

## Exact optimizer (GW9–13 value vs holding, net of hits)

| Route | Gain | Hit | Bank after | Captain |
|---|---|---|---|---|
| GW9-13, max 1: João Pedro → Thiago | +7.2 | 0 | 1.6 | Haaland |
| GW9-13, max 2: Sels + João Pedro → Raya + Thiago | +10.1 | 4 | 0.4 | Haaland |
| GW9-13, max 3: Cunha + João Pedro + N.Williams → Gabriel + Tavernier + Thiago | +13.2 | 8 | 0.2 | Haaland |
| GW9-13 wildcard | +33.9 | — | 0.0 | Haaland |
| GW9 only, max 1: João Pedro → Thiago | +1.7 | 0 | 1.6 | Haaland |
| GW9 only, max 2: João Pedro → Thiago | +1.7 | 0 | 1.6 | Haaland |
| GW9 only, max 3: João Pedro → Thiago | +1.7 | 0 | 1.6 | Haaland |
| GW9 only free hit | +8.0 | — | 0.0 | Haaland |

## Enumerated routes (decision sheet, GW9–13 gain vs holding, net of hits)

| Option | Gain now | If rolled | Bank after |
|---|---|---|---|
| João Pedro → Thiago | +7.2 | +5.5 | 1.6 |
| Donnarumma + João Pedro → Raya + Thiago | +10.1 | +11.0 | 0.9 |
| Cunha + João Pedro + N.Williams → Tavernier + Thiago + Gabriel | +13.2 | +12.4 | 0.2 |
| Wildcard (GW9-13) | +0.7 | — | 0.1 |
| Free Hit (GW9 only) | +1.8 | — | 0.8 |

Hold: XI Donnarumma, De Cuyper, Konsa, Justin, Rogers, Groß, Cherki, Cunha, McGinn, Haaland, Evanilson; bench Sels > Mitchell > N.Williams > João Pedro; captain Haaland, vice Rogers.

## Lineups for the leading routes (bench order = entry order, GK first)

- **hold** (bank after 1.7): XI Donnarumma, De Cuyper, Konsa, Justin, Rogers, Groß, Cherki, Cunha, McGinn, Haaland, Evanilson; bench Sels > Mitchell > N.Williams > João Pedro; C Haaland, VC Rogers; GW9 XI forecast 55.2 before hits.
- **Konsa -> Calafiori (1 FT, no hit)** (bank after 0.3): XI Donnarumma, De Cuyper, Calafiori, Justin, Rogers, Groß, Cherki, Cunha, McGinn, Haaland, Evanilson; bench Sels > Mitchell > N.Williams > João Pedro; C Haaland, VC Rogers; GW9 XI forecast 55.2 before hits.
- **João Pedro -> Thiago (GW9-13, max 1 moves, hit 0)** (bank after 1.6): XI Donnarumma, De Cuyper, Konsa, Justin, Rogers, Groß, Cherki, Cunha, Haaland, Thiago, Evanilson; bench Sels > McGinn > Mitchell > N.Williams; C Haaland, VC Rogers; GW9 XI forecast 56.5 before hits.
- **Sels + João Pedro -> Raya + Thiago (GW9-13, max 2 moves, hit 4)** (bank after 0.4): XI Raya, De Cuyper, Konsa, Justin, Rogers, Groß, Cherki, Cunha, Haaland, Thiago, Evanilson; bench Donnarumma > McGinn > Mitchell > N.Williams; C Haaland, VC Rogers; GW9 XI forecast 58.0 before hits.
- **João Pedro -> Thiago (GW9 only, max 1 moves, hit 0)** (bank after 1.6): XI Donnarumma, De Cuyper, Konsa, Justin, Rogers, Groß, Cherki, Cunha, Haaland, Thiago, Evanilson; bench Sels > McGinn > Mitchell > N.Williams; C Haaland, VC Rogers; GW9 XI forecast 56.5 before hits.

## Role-override sheet (new signings / role changes the ridge cannot see)

See [role_override_sheet.md](role_override_sheet.md).

Classic + F6 on the fixed pipeline makes the decision; the SFT arm is logged in shadow. See ../README.md for how to read the route gains and their uncertainty.
