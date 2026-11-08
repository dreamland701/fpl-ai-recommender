# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 326.49
- Total actual points: 325.00
- Average predicted points: 65.30
- Average actual points: 65.00
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
- Predicted score: 67.32
- Actual score: 90.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.69 | 12.68 | 19.95 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Steele | GK | 5 | 4.0 | 0.00 | 0.08 | 0.32 | 0.00 | 0.3 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.91 | 14.74 | 23.47 | 1.00 | 73.6 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.61 | 13.19 | 21.27 | 2.00 | 87.0 | 90.0 |
| Bench 3 | Bench | De Cuyper | DEF | 5 | 4.6 | 4.19 | 12.20 | 19.56 | 0.00 | 71.3 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.69 | 11.82 | 19.03 | 9.00 | 88.7 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 4.60 | 11.02 | 18.24 | 6.00 | 63.3 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.75 | 21.68 | 35.41 | 13.00 | 87.7 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.53 | 16.10 | 26.14 | 9.00 | 86.7 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 3.33 | 9.01 | 15.37 | 1.00 | 56.3 | 45.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.38 | 17.97 | 29.72 | 23.00 | 89.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.38 | 15.81 | 25.45 | 4.00 | 87.7 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.66 | 15.37 | 25.21 | 4.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Rogers | MID | 6 | 7.5 | 4.47 | 14.75 | 24.18 | 5.00 | 81.6 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.39 | 13.95 | 21.74 | 0.00 | 71.7 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 64.95
- Actual score: 50.00
- Transfer: Guéhi -> Calafiori (projected gain 1.57, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.98 | 11.47 | 18.67 | 3.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Steele | GK | 5 | 4.0 | 0.25 | 0.43 | 0.64 | 0.00 | 1.2 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.64 | 12.83 | 20.79 | 2.00 | 86.9 | 66.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.32 | 12.51 | 19.29 | 4.00 | 82.4 | 76.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.74 | 12.34 | 19.46 | 6.00 | 88.6 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 4.65 | 11.98 | 18.28 | 5.00 | 83.4 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.18 | 9.00 | 14.73 | 8.00 | 57.2 | 70.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.62 | 23.81 | 38.45 | 9.00 | 86.7 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.54 | 15.37 | 25.33 | 1.00 | 86.4 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.16 | 6.98 | 11.92 | 2.00 | 41.5 | 65.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.63 | 21.00 | 35.16 | 2.00 | 89.7 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.02 | 14.90 | 23.45 | 0.00 | 83.4 | 45.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.96 | 14.59 | 23.88 | 6.00 | 77.7 | 86.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.24 | 14.43 | 23.14 | 3.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.2 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 62.04
- Actual score: 80.00
- Transfer: Tzolis -> Ødegaard (projected gain 5.11, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.10 | 12.04 | 19.04 | 14.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Steele | GK | 5 | 4.0 | 0.21 | 0.42 | 0.65 | 0.00 | 1.3 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.68 | 13.51 | 21.28 | 6.00 | 78.8 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.72 | 11.23 | 17.70 | 1.00 | 73.9 | 58.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.71 | 10.57 | 16.71 | 11.00 | 67.5 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.60 | 10.56 | 17.01 | 2.00 | 86.8 | 90.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.1 | 3.24 | 9.33 | 14.55 | 1.00 | 72.3 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.45 | 21.94 | 36.02 | 9.00 | 86.8 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.84 | 17.02 | 27.06 | 12.00 | 86.6 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 2.58 | 7.39 | 12.31 | 12.00 | 49.0 | 62.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.43 | 19.67 | 30.21 | 8.00 | 89.6 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.21 | 17.27 | 29.76 | 2.00 | 83.6 | 90.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 4.88 | 14.43 | 22.76 | 3.00 | 80.8 | 84.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.95 | 13.51 | 21.62 | 3.00 | 82.8 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 66.21
- Actual score: 36.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.23) beats the best remaining Triple Captain opportunity (8.97).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.23) beats the best remaining Triple Captain opportunity (8.97).
- Autosub: De Cuyper replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 12.69 | 20.34 | 1.00 | 91.2 | 90.0 |
| Bench 1 | Bench | Steele | GK | 5 | 4.0 | 0.05 | 0.27 | 0.41 | 0.00 | 1.3 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.32 | 12.87 | 20.60 | 1.00 | 82.8 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.49 | 9.73 | 16.30 | 1.00 | 80.4 | 77.0 |
| Bench 2 | Autosub In | De Cuyper | DEF | 5 | 4.7 | 2.77 | 9.31 | 15.85 | 6.00 | 70.3 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.05 | 8.47 | 13.34 | 1.00 | 72.3 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.15 | 6.78 | 11.40 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.23 | 24.15 | 39.25 | 6.00 | 87.9 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.85 | 12.17 | 20.93 | 0.00 | 69.1 | 0.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.61 | 8.68 | 14.41 | 2.00 | 53.2 | 80.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.27 | 18.46 | 31.01 | 2.00 | 89.1 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.00 | 16.38 | 25.60 | 2.00 | 84.6 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.21 | 12.76 | 21.39 | 2.00 | 77.7 | 80.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.60 | 11.83 | 19.26 | 2.00 | 63.1 | 72.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.58 | 10.37 | 17.34 | 0.00 | 68.2 | 21.0 |

## GW6

- Train rows: 194240
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 65.97
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.99) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Emersonn -> Kostoulas (projected gain 3.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.99) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.29 | 12.56 | 20.21 | 3.00 | 90.5 | 90.0 |
| Bench 1 | Bench Boost | Steele | GK | 5 | 4.0 | 0.02 | 0.26 | 0.49 | 0.00 | 1.7 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 4.90 | 13.15 | 20.69 | 15.00 | 89.2 | 67.0 |
| XI | XI | Calafiori | DEF | 1 | 5.8 | 4.60 | 12.45 | 19.84 | 9.00 | 85.2 | 81.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.56 | 1.00 | 72.6 | 90.0 |
| Bench 2 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 2.55 | 7.32 | 11.82 | 1.00 | 70.9 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.96 | 6.56 | 12.77 | 3.00 | 41.2 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.59 | 22.78 | 37.71 | 6.00 | 87.9 | 79.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 3.94 | 12.37 | 22.71 | 12.00 | 56.0 | 71.0 |
| XI | XI | Kostoulas | FWD | 5 | 5.6 | 4.45 | 12.04 | 17.99 | 1.00 | 83.1 | 59.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 11.9 | 5.84 | 17.31 | 29.34 | 1.00 | 87.7 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.23 | 15.97 | 25.01 | 9.00 | 87.2 | 83.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.86 | 11.77 | 19.30 | 1.00 | 68.3 | 89.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.64 | 11.53 | 19.26 | 0.00 | 72.6 | 0.0 |
| Bench 3 | Bench Boost | M.Sangaré | MID | 4 | 5.6 | 2.46 | 7.62 | 13.41 | 1.00 | 39.6 | 38.0 |