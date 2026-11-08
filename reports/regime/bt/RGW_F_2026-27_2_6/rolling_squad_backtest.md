# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 340.65
- Total actual points: 332.00
- Average predicted points: 68.13
- Average actual points: 66.40
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
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 68.66
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.42 | 12.25 | 19.42 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.32 | 0.72 | 0.00 | 2.0 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 6.10 | 15.67 | 24.83 | 1.00 | 75.5 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.94 | 14.14 | 23.05 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | De Cuyper | DEF | 5 | 4.6 | 4.58 | 13.46 | 21.77 | 0.00 | 72.8 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.78 | 12.66 | 19.97 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Ajayi | DEF | 11 | 4.0 | 4.50 | 11.86 | 19.29 | 6.00 | 59.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.13 | 22.98 | 37.38 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.52 | 16.47 | 26.67 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 3.33 | 10.38 | 17.60 | 1.00 | 54.5 | 45.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.39 | 18.57 | 30.70 | 23.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.00 | 15.88 | 26.48 | 4.00 | 88.2 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.44 | 15.70 | 25.57 | 4.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.62 | 14.70 | 24.40 | 5.00 | 83.1 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.20 | 13.86 | 22.03 | 0.00 | 72.5 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 67.75
- Actual score: 50.00
- Transfer: Guéhi -> Calafiori (projected gain 1.86, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.85 | 11.15 | 18.03 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.21 | 0.39 | 0.00 | 1.9 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 5.71 | 15.93 | 25.28 | 5.00 | 90.0 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.75 | 13.63 | 21.46 | 4.00 | 84.4 | 76.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.87 | 13.62 | 21.65 | 2.00 | 90.0 | 66.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.95 | 13.42 | 21.13 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.75 | 10.69 | 17.24 | 8.00 | 67.0 | 70.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.04 | 24.92 | 40.16 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.50 | 15.01 | 25.03 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.07 | 7.05 | 12.03 | 2.00 | 41.5 | 65.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.76 | 21.49 | 36.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.18 | 14.94 | 23.87 | 0.00 | 85.0 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.21 | 13.89 | 22.45 | 3.00 | 88.1 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.88 | 13.42 | 22.71 | 6.00 | 76.1 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 1.75 | 6.39 | 11.29 | 5.00 | 32.9 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 63.76
- Actual score: 79.00
- Transfer: Tzolis -> Ødegaard (projected gain 3.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.19 | 12.14 | 19.39 | 14.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.07 | 0.38 | 0.73 | 0.00 | 3.5 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.90 | 14.01 | 22.17 | 6.00 | 81.9 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.89 | 12.33 | 20.09 | 1.00 | 88.6 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.91 | 11.35 | 18.09 | 1.00 | 73.3 | 58.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 3.74 | 10.84 | 17.36 | 2.00 | 86.5 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.87 | 10.78 | 17.44 | 11.00 | 67.3 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.75 | 22.66 | 37.07 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.91 | 17.29 | 27.53 | 12.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 2.59 | 7.43 | 12.46 | 12.00 | 49.4 | 62.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.66 | 19.04 | 29.91 | 8.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.16 | 17.00 | 29.19 | 2.00 | 84.6 | 90.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 4.92 | 14.34 | 23.19 | 3.00 | 81.2 | 84.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.84 | 13.10 | 21.25 | 3.00 | 83.1 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.61 | 8.47 | 14.55 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 68.09
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.50) beats the best remaining Triple Captain opportunity (9.27).
- Transfer: M.Sangaré -> Groß (projected gain 2.66, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.50) beats the best remaining Triple Captain opportunity (9.27).
- Autosub: De Cuyper replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.18 | 12.51 | 19.96 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.21 | 0.51 | 0.83 | 0.00 | 2.9 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.36 | 12.95 | 20.70 | 1.00 | 84.1 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.91 | 11.06 | 19.17 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | De Cuyper | DEF | 5 | 4.7 | 2.91 | 10.32 | 17.40 | 6.00 | 72.7 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.53 | 9.77 | 16.28 | 1.00 | 79.5 | 77.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.19 | 6.92 | 11.80 | 0.00 | 46.3 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.50 | 24.82 | 39.73 | 6.00 | 90.0 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.75 | 11.94 | 19.80 | 0.00 | 72.3 | 0.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.67 | 8.86 | 15.01 | 2.00 | 55.2 | 80.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.37 | 18.48 | 30.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 4.99 | 15.20 | 24.58 | 2.00 | 84.2 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.12 | 12.72 | 20.99 | 14.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.96 | 11.75 | 19.68 | 2.00 | 76.8 | 80.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.41 | 10.84 | 18.48 | 2.00 | 60.9 | 72.0 |

## GW6

- Train rows: 194240
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 72.40
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.29) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro -> Kostoulas (projected gain 3.59, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.29) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.43 | 12.79 | 20.52 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Palmer | GK | 12 | 4.0 | 0.38 | 0.69 | 1.03 | 0.00 | 4.1 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 5.30 | 14.63 | 23.12 | 15.00 | 90.0 | 67.0 |
| XI | XI | Calafiori | DEF | 1 | 5.8 | 4.87 | 13.68 | 22.14 | 9.00 | 90.0 | 81.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.21 | 9.61 | 17.72 | 1.00 | 86.5 | 90.0 |
| Bench 2 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.15 | 8.83 | 14.99 | 1.00 | 73.9 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.76 | 5.93 | 12.71 | 3.00 | 43.5 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.04 | 23.89 | 39.08 | 6.00 | 90.0 | 79.0 |
| XI | XI | Kostoulas | FWD | 5 | 5.6 | 4.60 | 12.39 | 19.00 | 1.00 | 84.6 | 59.0 |
| Bench 3 | Bench Boost | Emersonn | FWD | 12 | 5.5 | 3.00 | 8.71 | 14.21 | 2.00 | 58.6 | 70.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 7.07 | 18.59 | 28.96 | 6.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.05 | 17.96 | 30.17 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.24 | 14.84 | 23.88 | 9.00 | 89.3 | 83.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.71 | 11.14 | 18.92 | 1.00 | 66.8 | 89.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.54 | 11.06 | 18.58 | 0.00 | 72.2 | 0.0 |