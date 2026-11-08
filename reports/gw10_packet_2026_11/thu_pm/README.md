# GW10 final packet (fixed pipeline)

- **Snapshot:** 2026-11-05T23:09:42+00:00 UTC; deadline 2026-11-06T18:30:00Z.
- **Entry 6535607:** bank £0.3m, free transfers 1, chips used: 3xc. Transfers already made for GW10: none.
- **Selling prices vs the app values pasted 2026-10-04:** ['Konsa: computed 4.6 vs app 4.5', 'N.Williams: computed 4.9 vs app 5.0', 'Groß: computed 5.8 vs app 5.7', 'Cherki: computed 7.8 vs app 7.7', 'Evanilson: computed 6.2 vs app 6.0', 'Cunha: computed 7.8 vs app 7.9'].

## Squad and targets as the model sees them

| Player | Status | Chance | News | GW10 | GW10–14 | P(appear) | min |
|---|---|---|---|---|---|---|---|
| Donnarumma | a | -1.0 | — | 3.03 | 14.0 | 0.88 | 79 |
| Konsa | d | 75.0 | Knee injury - 75% chance of playing | 3.75 | 16.3 | 0.81 | 73 |
| N.Williams | a | 100.0 | — | 3.30 | 15.9 | 0.89 | 80 |
| De Cuyper | a | -1.0 | — | 5.06 | 22.9 | 0.98 | 88 |
| McGinn | a | -1.0 | — | 3.36 | 16.0 | 0.82 | 74 |
| Groß | a | -1.0 | — | 5.34 | 24.9 | 1.00 | 90 |
| Rogers | a | -1.0 | — | 6.37 | 27.3 | 1.00 | 90 |
| Cherki | a | -1.0 | — | 3.43 | 17.6 | 0.46 | 41 |
| Haaland | a | 100.0 | — | 8.80 | 41.1 | 1.00 | 90 |
| Evanilson | a | -1.0 | — | 4.44 | 20.1 | 0.76 | 68 |
| Isak | a | 100.0 | — | 4.78 | 21.9 | 0.76 | 68 |
| Sels | a | -1.0 | — | 2.42 | 11.9 | 0.84 | 76 |
| Cunha | a | -1.0 | — | 3.55 | 17.1 | 0.68 | 61 |
| Justin | a | -1.0 | — | 3.18 | 15.0 | 0.90 | 80 |
| Mitchell | a | -1.0 | — | 3.00 | 13.8 | 0.91 | 82 |
| Rice | a | 100.0 | — | 4.88 | 22.1 | 0.97 | 88 |
| Raya | a | -1.0 | — | 4.87 | 21.7 | 1.00 | 90 |
| Gabriel | a | -1.0 | — | 5.49 | 24.8 | 1.00 | 90 |
| Calafiori | a | 100.0 | — | 5.27 | 23.0 | 1.00 | 90 |
| Verbruggen | a | -1.0 | — | 3.60 | 17.1 | 1.00 | 90 |
| Mbeumo | a | -1.0 | — | 4.43 | 21.2 | 0.94 | 85 |
| Thiago | a | -1.0 | — | 4.06 | 21.4 | 1.00 | 90 |
| Tavernier | a | -1.0 | — | 4.22 | 19.4 | 0.72 | 64 |
| N.Jackson | a | -1.0 | — | 3.21 | 16.0 | 0.54 | 48 |
| Rayan | a | -1.0 | — | 4.26 | 18.2 | 0.87 | 78 |
| Van Hecke | a | 100.0 | — | 4.01 | 19.2 | 0.91 | 82 |
| Saka | i | 0.0 | Thigh injury - Unknown return date | 2.35 | 13.5 | 0.28 | 26 |

## What moved since the interim packet

| Player | Status now | News now | GW10 (interim → now) | GW10–14 (interim → now) |
|---|---|---|---|---|
| Konsa | d | Knee injury - 75% chance of playing | 4.24 → 3.75 | 18.1 → 16.3 |

## Exact optimizer (GW10–14 value vs holding, net of hits)

| Route | Gain | Hit | Bank after | Captain |
|---|---|---|---|---|
| GW10-14, max 1: Cunha → Rice | +4.9 | 0 | 0.7 | Haaland |
| GW10-14, max 2: Donnarumma + Cunha → Raya + Rice | +8.7 | 4 | -0.0 | Haaland |
| GW10-14, max 3: Donnarumma + Cunha → Raya + Rice | +8.7 | 4 | -0.0 | Haaland |
| GW10-14 wildcard | +30.9 | — | -0.0 | Haaland |
| GW10 only, max 1: Cherki → Rice | +1.4 | 0 | 0.7 | Haaland |
| GW10 only, max 2: Cherki → Rice | +1.4 | 0 | 0.7 | Haaland |
| GW10 only, max 3: Cherki → Rice | +1.4 | 0 | 0.7 | Haaland |
| GW10 only free hit | +7.9 | — | -0.0 | Haaland |

## Enumerated routes (decision sheet, GW10–14 gain vs holding, net of hits)

| Option | Gain now | If rolled | Bank after |
|---|---|---|---|
| Cunha → Rice | +4.9 | +3.6 | 0.7 |
| Donnarumma + Cunha → Raya + Rice | +8.7 | +9.5 | 0.0 |
| Donnarumma + N.Williams + Cunha → Raya + Calafiori + Rayan | +7.8 | +7.6 | 0.1 |
| Wildcard (GW10-14) | +0.9 | — | 0.4 |
| Free Hit (GW10 only) | +1.6 | — | 0.8 |

Hold: XI Donnarumma, De Cuyper, Konsa, N.Williams, Rogers, Groß, Cunha, Cherki, Haaland, Isak, Evanilson; bench Sels > McGinn > Justin > Mitchell; captain Haaland, vice Rogers.

## Lineups for the leading routes (bench order = entry order, GK first)

- **hold** (bank after 0.3): XI Donnarumma, De Cuyper, Konsa, N.Williams, Rogers, Groß, Cunha, Cherki, Haaland, Isak, Evanilson; bench Sels > McGinn > Justin > Mitchell; C Haaland, VC Rogers; GW10 XI forecast 60.7 before hits.
- **Cunha -> Rice (GW10-14, max 1 moves, hit 0)** (bank after 0.7): XI Donnarumma, De Cuyper, Konsa, N.Williams, Rogers, Groß, Rice, Cherki, Haaland, Isak, Evanilson; bench Sels > McGinn > Justin > Mitchell; C Haaland, VC Rogers; GW10 XI forecast 62.0 before hits.
- **Donnarumma + Cunha -> Raya + Rice (GW10-14, max 2 moves, hit 4)** (bank after 0.0): XI Raya, De Cuyper, Konsa, N.Williams, Rogers, Groß, Rice, Cherki, Haaland, Isak, Evanilson; bench Sels > McGinn > Justin > Mitchell; C Haaland, VC Rogers; GW10 XI forecast 63.8 before hits.
- **Cherki -> Rice (GW10 only, max 1 moves, hit 0)** (bank after 0.7): XI Donnarumma, De Cuyper, Konsa, N.Williams, Rogers, Groß, Rice, Cunha, Haaland, Isak, Evanilson; bench Sels > McGinn > Justin > Mitchell; C Haaland, VC Rogers; GW10 XI forecast 62.1 before hits.

## Role-override sheet (new signings / role changes the ridge cannot see)

See [role_override_sheet.md](role_override_sheet.md).

Classic + F6 on the fixed pipeline makes the decision; the SFT arm is logged in shadow. See ../README.md for how to read the route gains and their uncertainty.
