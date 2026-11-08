# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 213.56
- Total actual points: 247.00
- Average predicted points: 53.39
- Average actual points: 61.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 191634
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: B.Fernandes
- Vice captain: Mendy
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 54.02
- Actual score: 91.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 11.76 | 19.21 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.09 | 8.57 | 14.13 | 10.00 | 84.7 | 90.0 |
| Vice Captain | XI | Mendy | DEF | 11 | 4.0 | 4.99 | 12.89 | 20.24 | 1.00 | 76.3 | 58.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 3.93 | 11.95 | 19.24 | 11.00 | 91.1 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.99 | 11.49 | 18.86 | 2.00 | 91.3 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.78 | 11.44 | 17.96 | 1.00 | 89.0 | 90.0 |
| Bench 4 | Bench | Murillo | DEF | 18 | 5.5 | 3.20 | 10.13 | 17.05 | 1.00 | 85.8 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.82 | 14.01 | 23.17 | 9.00 | 104.4 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 4 | 8.0 | 3.41 | 11.25 | 18.44 | 2.00 | 77.7 | 90.0 |
| Bench 3 | Bench | McBurnie | FWD | 11 | 5.5 | 3.37 | 9.55 | 15.08 | 1.00 | 80.1 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 5.14 | 14.69 | 25.10 | 23.00 | 93.4 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 4.87 | 14.16 | 23.24 | 7.00 | 92.8 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.81 | 14.04 | 23.68 | 4.00 | 100.3 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.03 | 13.48 | 22.67 | 4.00 | 90.5 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 4.45 | 13.07 | 20.99 | 0.00 | 78.2 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Szoboszlai
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 49.30
- Actual score: 37.00
- Transfer: Murillo -> De Cuyper (projected gain 3.51, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 6.0 | 3.25 | 9.95 | 16.40 | 3.00 | 86.1 | 90.0 |
| XI | XI | Tzolakis | GK | 11 | 4.5 | 3.39 | 9.62 | 15.75 | 6.00 | 89.8 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 4.16 | 11.95 | 18.02 | 4.00 | 92.7 | 76.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 3.98 | 11.95 | 18.73 | 2.00 | 91.9 | 66.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.21 | 9.57 | 15.82 | 6.00 | 81.5 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.19 | 9.36 | 14.60 | 8.00 | 73.4 | 70.0 |
| Bench 2 | Bench | Guéhi | DEF | 15 | 6.0 | 2.97 | 8.57 | 13.78 | 8.00 | 80.5 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 3.90 | 12.28 | 20.98 | 1.00 | 92.0 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 3.29 | 10.40 | 17.04 | 2.00 | 72.6 | 90.0 |
| Bench 3 | Bench | McBurnie | FWD | 11 | 5.5 | 2.39 | 7.14 | 11.64 | 2.00 | 67.8 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 5.88 | 17.93 | 30.84 | 2.00 | 98.9 | 90.0 |
| Vice Captain | XI | Szoboszlai | MID | 14 | 7.0 | 4.60 | 13.25 | 21.06 | 3.00 | 88.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.34 | 12.86 | 20.38 | 0.00 | 90.1 | 45.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 3.46 | 12.78 | 21.01 | 1.00 | 84.9 | 90.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 1.37 | 5.29 | 9.31 | 5.00 | 16.7 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 1.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Palmer
- Vice captain: João Pedro
- Effective captain: Palmer
- Chip used: triple_captain
- Predicted score: 55.82
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.54) beats the best remaining Triple Captain opportunity (6.53).
- Transfer: Tzolis -> Ødegaard (projected gain 5.33, hit 0)
- Chip used: Triple Captain on Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (5.54) beats the best remaining Triple Captain opportunity (6.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.93 | 11.37 | 18.11 | 14.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 2.68 | 8.17 | 13.15 | 2.00 | 82.3 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.10 | 11.75 | 18.59 | 6.00 | 88.0 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.13 | 9.75 | 15.99 | 6.00 | 83.1 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.35 | 9.20 | 14.94 | 11.00 | 76.2 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.02 | 8.09 | 13.46 | 8.00 | 62.8 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 2.92 | 8.03 | 12.78 | 1.00 | 51.7 | 58.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 5.32 | 14.72 | 23.85 | 12.00 | 103.2 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 7.9 | 3.01 | 8.63 | 14.61 | 1.00 | 71.1 | 90.0 |
| Bench 4 | Bench | McBurnie | FWD | 11 | 5.5 | 2.28 | 7.32 | 11.15 | 4.00 | 71.8 | 81.0 |
| Captain | Captain | Palmer | MID | 6 | 9.6 | 5.54 | 15.82 | 24.85 | 5.00 | 112.2 | 90.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 4.86 | 13.33 | 21.46 | 3.00 | 90.6 | 84.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 3.89 | 13.09 | 23.54 | 2.00 | 74.6 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.62 | 12.16 | 19.67 | 3.00 | 83.4 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.32 | 7.39 | 12.73 | 4.00 | 55.2 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.70 -> 1.50
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Raya
- Effective captain: B.Fernandes
- Chip used: bench_boost
- Predicted score: 54.42
- Actual score: 38.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.32) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Virgil -> Gvardiol (projected gain 3.18, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.32) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | Raya | GK | 1 | 6.0 | 4.01 | 12.02 | 18.61 | 1.00 | 94.8 | 90.0 |
| Bench 1 | Bench Boost | Tzolakis | GK | 11 | 4.5 | 2.75 | 8.15 | 12.93 | 6.00 | 83.7 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.00 | 12.24 | 20.32 | 1.00 | 85.4 | 90.0 |
| XI | XI | Gvardiol | DEF | 15 | 5.7 | 3.92 | 11.78 | 18.91 | 4.00 | 94.8 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 2.96 | 8.84 | 14.10 | 4.00 | 86.6 | 90.0 |
| Bench 3 | Bench Boost | De Cuyper | DEF | 5 | 4.8 | 2.52 | 8.33 | 13.70 | 6.00 | 76.1 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.38 | 4.28 | 8.44 | 0.00 | 28.4 | 0.0 |
| XI | XI | João Pedro | FWD | 6 | 7.7 | 3.13 | 11.35 | 21.93 | 0.00 | 74.9 | 0.0 |
| XI | XI | Thiago | FWD | 4 | 7.8 | 3.00 | 8.75 | 15.07 | 5.00 | 74.5 | 90.0 |
| Bench 2 | Bench Boost | McBurnie | FWD | 11 | 5.5 | 2.68 | 7.74 | 12.63 | 1.00 | 77.0 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 5.80 | 16.98 | 29.14 | 2.00 | 91.8 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.6 | 3.28 | 11.57 | 18.90 | 2.00 | 72.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.20 | 10.77 | 18.12 | 2.00 | 77.2 | 80.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.04 | 10.22 | 16.69 | 2.00 | 70.6 | 72.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 2.97 | 9.12 | 14.66 | 0.00 | 72.6 | 21.0 |