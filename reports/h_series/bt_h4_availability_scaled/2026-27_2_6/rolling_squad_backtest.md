# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 349.06
- Total actual points: 327.00
- Average predicted points: 69.81
- Average actual points: 65.40
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
- Vice captain: Mendy
- Effective captain: Haaland
- Chip used: none
- Predicted score: 74.22
- Actual score: 91.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.68 | 12.75 | 20.37 | 6.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Dubravka | GK | 19 | 4.0 | 0.88 | 2.25 | 3.84 | 0.00 | 11.7 | 0.0 |
| Vice Captain | XI | Mendy | DEF | 11 | 4.0 | 6.98 | 17.62 | 28.03 | 1.00 | 75.4 | 58.0 |
| XI | XI | O'Reilly | DEF | 15 | 6.5 | 5.56 | 15.73 | 25.77 | 2.00 | 63.9 | 88.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 5.18 | 15.28 | 24.37 | 0.00 | 72.4 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.85 | 12.67 | 20.10 | 9.00 | 86.0 | 90.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 3.91 | 11.19 | 17.98 | 0.00 | 88.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.22 | 22.95 | 37.51 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.70 | 17.02 | 27.67 | 9.00 | 87.1 | 90.0 |
| Bench 2 | Bench | Emersonn | FWD | 12 | 5.5 | 4.63 | 14.06 | 23.74 | 1.00 | 57.4 | 45.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 6.56 | 18.73 | 31.14 | 23.00 | 89.8 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 6.80 | 18.42 | 30.11 | 11.00 | 71.3 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 6.49 | 16.94 | 26.96 | 0.00 | 76.8 | 45.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.99 | 16.17 | 26.77 | 4.00 | 85.5 | 90.0 |
| Bench 3 | Bench | Slater | MID | 11 | 4.5 | 4.29 | 11.41 | 18.33 | 2.00 | 88.0 | 90.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 68.81
- Actual score: 47.00
- Transfer: Mendy -> Ajayi (projected gain 7.75, hit 0)
- Autosub: O'Shea replaced O'Reilly.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.13 | 11.90 | 19.40 | 3.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Dubravka | GK | 19 | 4.0 | 0.91 | 2.55 | 4.26 | 0.00 | 12.9 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.57 | 15.41 | 24.44 | 5.00 | 89.4 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.68 | 13.92 | 21.33 | 4.00 | 82.7 | 76.0 |
| XI | Bench | O'Reilly | DEF | 15 | 6.5 | 4.88 | 13.43 | 22.07 | 0.00 | 68.0 | 0.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.95 | 13.33 | 20.93 | 6.00 | 90.2 | 90.0 |
| Bench 2 | Autosub In | O'Shea | DEF | 12 | 4.0 | 2.74 | 7.68 | 12.35 | 3.00 | 77.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.11 | 25.12 | 40.53 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.78 | 16.03 | 26.60 | 1.00 | 88.0 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.16 | 6.98 | 11.92 | 2.00 | 41.5 | 65.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.78 | 21.61 | 36.29 | 2.00 | 87.1 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 5.63 | 16.32 | 26.88 | 2.00 | 78.8 | 89.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.39 | 15.81 | 24.99 | 0.00 | 86.4 | 45.0 |
| XI | XI | Slater | MID | 11 | 4.5 | 3.79 | 10.36 | 16.51 | 3.00 | 84.8 | 90.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: João Pedro
- Effective captain: Haaland
- Chip used: none
- Predicted score: 62.21
- Actual score: 75.00
- Transfer: Emersonn -> Barry (projected gain 4.89, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 12.11 | 19.43 | 14.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Dubravka | GK | 19 | 4.0 | 0.90 | 2.57 | 4.14 | 0.00 | 11.8 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 4.95 | 14.31 | 22.39 | 11.00 | 69.1 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 4.07 | 12.77 | 20.71 | 1.00 | 84.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.91 | 11.29 | 18.10 | 2.00 | 88.2 | 90.0 |
| Bench 2 | Bench | O'Shea | DEF | 12 | 4.0 | 2.99 | 8.24 | 13.14 | 1.00 | 78.4 | 90.0 |
| Bench 4 | Bench | O'Reilly | DEF | 15 | 6.4 | 0.83 | 3.67 | 7.28 | 1.00 | 10.2 | 8.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.85 | 22.84 | 37.55 | 9.00 | 89.1 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 6.01 | 17.78 | 28.39 | 12.00 | 86.4 | 90.0 |
| XI | XI | Barry | FWD | 9 | 5.6 | 4.59 | 13.10 | 20.98 | 2.00 | 65.6 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.65 | 18.53 | 31.94 | 2.00 | 86.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 5.60 | 16.81 | 27.79 | 8.00 | 76.5 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.4 | 4.23 | 13.06 | 22.26 | 3.00 | 65.2 | 80.0 |
| XI | XI | Slater | MID | 11 | 4.5 | 3.38 | 9.79 | 15.74 | 2.00 | 83.7 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.00 -> 1.80
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 72.98
- Actual score: 40.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (9.38).
- Transfer: O'Reilly -> Bogle (projected gain 1.19, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (9.38).
- Autosub: Slater replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.13 | 12.47 | 20.15 | 1.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Dubravka | GK | 19 | 4.0 | 0.88 | 2.45 | 4.02 | 0.00 | 10.5 | 0.0 |
| XI | XI | Bogle | DEF | 13 | 4.6 | 5.14 | 13.30 | 20.72 | 5.00 | 73.7 | 66.0 |
| Bench 3 | Bench | De Cuyper | DEF | 5 | 4.7 | 3.33 | 12.16 | 20.22 | 6.00 | 70.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.87 | 10.88 | 18.04 | 1.00 | 82.3 | 77.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.62 | 10.73 | 18.03 | 1.00 | 83.0 | 90.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 2.56 | 7.16 | 12.12 | 2.00 | 72.5 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.61 | 24.82 | 40.33 | 6.00 | 89.5 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 4.90 | 15.54 | 26.48 | 0.00 | 71.2 | 0.0 |
| XI | XI | Barry | FWD | 9 | 5.6 | 5.17 | 13.82 | 21.35 | 6.00 | 64.6 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.44 | 18.85 | 31.71 | 2.00 | 89.7 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 5.51 | 17.02 | 27.86 | 2.00 | 85.2 | 80.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.57 | 13.20 | 21.91 | 0.00 | 71.2 | 21.0 |
| XI | XI | Tzolis | MID | 1 | 6.4 | 3.80 | 12.29 | 20.90 | 2.00 | 64.9 | 72.0 |
| Bench 2 | Autosub In | Slater | MID | 11 | 4.5 | 3.53 | 9.87 | 15.62 | 2.00 | 82.4 | 77.0 |

## GW6

- Train rows: 194240
- Bank: 1.80 -> 2.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 70.84
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.54) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Tzolis -> Groß (projected gain 10.50, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.54) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.33 | 12.68 | 20.48 | 3.00 | 88.3 | 90.0 |
| Bench 1 | Bench Boost | Dubravka | GK | 19 | 4.0 | 0.70 | 2.38 | 4.09 | 0.00 | 12.1 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 5.06 | 14.21 | 22.25 | 15.00 | 88.5 | 67.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.03 | 9.48 | 16.91 | 1.00 | 79.7 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.57 | 1.00 | 72.6 | 90.0 |
| Bench 3 | Bench Boost | Bogle | DEF | 13 | 4.6 | 2.47 | 8.48 | 14.37 | 1.00 | 54.5 | 85.0 |
| XI | XI | O'Shea | DEF | 12 | 4.0 | 3.24 | 8.37 | 13.23 | 11.00 | 79.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.06 | 23.75 | 39.16 | 6.00 | 88.1 | 79.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.23 | 13.76 | 24.07 | 12.00 | 37.5 | 71.0 |
| XI | XI | Barry | FWD | 9 | 5.6 | 4.45 | 13.48 | 21.36 | 6.00 | 70.8 | 85.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.9 | 6.77 | 18.59 | 28.44 | 6.00 | 84.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.09 | 18.04 | 30.52 | 1.00 | 90.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 5.94 | 17.80 | 29.06 | 2.00 | 85.3 | 90.0 |
| Bench 2 | Bench Boost | Slater | MID | 11 | 4.5 | 2.91 | 8.17 | 13.35 | 2.00 | 72.3 | 74.0 |
| Bench 4 | Bench Boost | M.Sangaré | MID | 4 | 5.6 | 2.46 | 7.62 | 13.41 | 1.00 | 39.6 | 38.0 |