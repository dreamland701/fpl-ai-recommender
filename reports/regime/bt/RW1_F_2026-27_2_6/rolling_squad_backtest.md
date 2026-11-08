# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 333.85
- Total actual points: 329.00
- Average predicted points: 66.77
- Average actual points: 65.80
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 67.45
- Actual score: 91.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.33 | 12.20 | 19.31 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Button | GK | 12 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.97 | 15.61 | 24.49 | 1.00 | 75.1 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.83 | 13.69 | 22.27 | 2.00 | 89.2 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.68 | 12.61 | 19.77 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 3.85 | 11.04 | 17.76 | 0.00 | 85.7 | 90.0 |
| Bench 4 | Bench | Thomas | DEF | 7 | 4.0 | 3.40 | 9.23 | 14.81 | 8.00 | 82.5 | 77.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.96 | 22.34 | 36.11 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.65 | 16.68 | 26.98 | 9.00 | 90.0 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 4.50 | 13.67 | 22.47 | 2.00 | 73.0 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.21 | 18.03 | 29.62 | 23.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.29 | 16.37 | 27.55 | 4.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.52 | 15.74 | 25.65 | 4.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.55 | 14.27 | 23.58 | 5.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Slater | MID | 11 | 4.5 | 4.23 | 11.10 | 17.77 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 192260
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 66.16
- Actual score: 54.00
- Transfer: Mendy -> Ajayi (projected gain 5.10, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.89 | 11.18 | 18.08 | 3.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Button | GK | 12 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.61 | 15.60 | 24.73 | 5.00 | 90.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.93 | 13.43 | 21.19 | 6.00 | 90.0 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.11 | 11.46 | 18.72 | 8.00 | 79.5 | 90.0 |
| Bench 4 | Bench | Thomas | DEF | 7 | 4.0 | 2.72 | 8.91 | 14.78 | 4.00 | 77.1 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.82 | 7.65 | 12.17 | 3.00 | 77.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.96 | 24.09 | 38.72 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.64 | 15.06 | 25.18 | 1.00 | 90.0 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 4.08 | 12.08 | 19.75 | 2.00 | 66.9 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.60 | 20.60 | 34.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.30 | 15.23 | 24.67 | 0.00 | 87.5 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.21 | 13.80 | 22.24 | 3.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.87 | 13.07 | 22.19 | 6.00 | 76.7 | 86.0 |
| Bench 2 | Bench | Slater | MID | 11 | 4.5 | 3.67 | 9.70 | 15.59 | 3.00 | 83.8 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 60.88
- Actual score: 71.00
- Transfer: M.Sangaré -> Janelt (projected gain 0.70, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.26 | 12.48 | 19.83 | 14.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Button | GK | 12 | 4.0 | 0.00 | 0.03 | 0.12 | 0.00 | 3.5 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.75 | 11.96 | 19.63 | 1.00 | 89.4 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.85 | 11.24 | 18.50 | 6.00 | 84.4 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.71 | 10.82 | 17.27 | 2.00 | 86.0 | 90.0 |
| Bench 2 | Bench | Thomas | DEF | 7 | 4.0 | 3.52 | 10.12 | 16.16 | 0.00 | 80.4 | 90.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 3.13 | 8.47 | 13.40 | 1.00 | 78.7 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.62 | 21.88 | 35.40 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.06 | 17.72 | 28.10 | 12.00 | 90.0 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 7.9 | 3.83 | 10.80 | 17.97 | 1.00 | 66.6 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.61 | 18.99 | 30.00 | 8.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 4.99 | 16.21 | 27.66 | 2.00 | 84.9 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.88 | 13.16 | 21.17 | 3.00 | 85.6 | 90.0 |
| XI | XI | Janelt | MID | 4 | 5.0 | 3.71 | 10.76 | 17.76 | 4.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Slater | MID | 11 | 4.5 | 3.25 | 9.07 | 14.64 | 2.00 | 82.1 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.80 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 68.04
- Actual score: 52.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.36) beats the best remaining Triple Captain opportunity (9.11).
- Transfer: Janelt -> Groß (projected gain 2.61, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.36) beats the best remaining Triple Captain opportunity (9.11).
- Autosub: Slater replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.28 | 12.95 | 20.42 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Button | GK | 12 | 4.0 | 0.06 | 0.09 | 0.16 | 0.00 | 2.5 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.03 | 12.15 | 19.48 | 4.00 | 89.9 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.98 | 10.79 | 19.20 | 1.00 | 90.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.61 | 9.87 | 16.49 | 1.00 | 80.4 | 77.0 |
| Bench 3 | Bench | Thomas | DEF | 7 | 4.0 | 3.15 | 8.69 | 14.09 | 9.00 | 75.5 | 90.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 2.78 | 7.28 | 12.60 | 2.00 | 73.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.36 | 24.36 | 38.04 | 6.00 | 90.0 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 4.04 | 12.65 | 20.09 | 0.00 | 78.9 | 0.0 |
| XI | XI | Thiago | FWD | 4 | 7.8 | 3.70 | 10.45 | 17.33 | 5.00 | 70.7 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.18 | 17.81 | 29.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 4.98 | 14.79 | 24.56 | 2.00 | 84.9 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.13 | 12.69 | 21.07 | 14.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.03 | 11.91 | 19.63 | 2.00 | 80.1 | 80.0 |
| Bench 2 | Autosub In | Slater | MID | 11 | 4.5 | 3.29 | 9.02 | 14.39 | 2.00 | 79.9 | 77.0 |

## GW6

- Train rows: 194240
- Bank: 0.10 -> 2.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 71.33
- Actual score: 61.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.69) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro -> Kostoulas (projected gain 2.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.69) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.55 | 13.16 | 21.32 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Button | GK | 12 | 4.0 | 0.21 | 0.26 | 0.35 | 0.00 | 3.4 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.38 | 10.91 | 17.88 | 6.00 | 89.0 | 90.0 |
| XI | XI | Thomas | DEF | 7 | 4.0 | 3.67 | 10.33 | 16.44 | 4.00 | 84.5 | 90.0 |
| Bench 2 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 3.29 | 9.50 | 17.93 | 1.00 | 88.1 | 90.0 |
| Bench 3 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.23 | 8.90 | 15.39 | 1.00 | 74.6 | 90.0 |
| XI | XI | O'Shea | DEF | 12 | 4.0 | 3.35 | 8.48 | 13.40 | 11.00 | 79.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.94 | 23.51 | 37.85 | 6.00 | 90.0 | 79.0 |
| XI | XI | Kostoulas | FWD | 5 | 5.6 | 4.59 | 12.40 | 19.03 | 1.00 | 83.8 | 59.0 |
| XI | XI | Thiago | FWD | 4 | 7.8 | 4.21 | 11.69 | 18.77 | 4.00 | 77.2 | 90.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 7.11 | 18.31 | 29.32 | 6.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 5.94 | 17.54 | 29.14 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.31 | 14.82 | 23.90 | 9.00 | 90.0 | 83.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.64 | 11.40 | 18.93 | 0.00 | 75.9 | 0.0 |
| Bench 4 | Bench Boost | Slater | MID | 11 | 4.5 | 2.97 | 8.11 | 13.48 | 2.00 | 73.3 | 74.0 |