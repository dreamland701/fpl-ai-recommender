# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 334.18
- Total actual points: 315.00
- Average predicted points: 66.84
- Average actual points: 63.00
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
- Predicted score: 68.82
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.43 | 12.31 | 19.60 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.08 | 0.07 | 0.14 | 0.00 | 1.3 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 6.17 | 15.88 | 25.15 | 1.00 | 74.7 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.80 | 13.62 | 22.12 | 2.00 | 88.8 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.86 | 12.90 | 20.38 | 9.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.0 | 4.43 | 11.59 | 18.78 | 6.00 | 56.8 | 90.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 3.87 | 11.08 | 17.84 | 0.00 | 86.7 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.07 | 22.71 | 36.86 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.66 | 16.92 | 27.45 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Gonzalo | FWD | 10 | 6.0 | 4.06 | 11.50 | 18.65 | 2.00 | 87.5 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.36 | 18.48 | 30.53 | 23.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.13 | 16.32 | 27.23 | 4.00 | 89.6 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.54 | 16.04 | 26.16 | 4.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.56 | 14.49 | 24.03 | 5.00 | 82.7 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.21 | 13.90 | 22.09 | 0.00 | 73.3 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 67.73
- Actual score: 53.00
- Transfer: Gonzalo -> Wissa (projected gain 4.13, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.85 | 11.19 | 18.15 | 3.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.00 | 0.00 | 0.01 | 0.00 | 1.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 5.69 | 15.82 | 25.11 | 5.00 | 90.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 5.00 | 13.59 | 21.42 | 6.00 | 90.0 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.12 | 11.51 | 18.82 | 8.00 | 78.6 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.78 | 10.77 | 17.35 | 8.00 | 66.2 | 70.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.80 | 7.70 | 12.28 | 3.00 | 77.7 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.99 | 24.65 | 39.64 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.62 | 15.38 | 25.65 | 1.00 | 90.0 | 90.0 |
| XI | XI | Wissa | FWD | 17 | 6.1 | 5.32 | 14.17 | 21.75 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.70 | 21.24 | 35.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.29 | 15.32 | 24.53 | 0.00 | 86.7 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.30 | 14.22 | 23.03 | 3.00 | 89.2 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.87 | 13.38 | 22.66 | 6.00 | 76.3 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 1.79 | 6.53 | 11.54 | 5.00 | 33.8 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 61.92
- Actual score: 71.00
- Transfer: Tzolis -> Scott (projected gain 3.95, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.21 | 12.30 | 19.67 | 14.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.15 | 0.21 | 0.30 | 0.00 | 2.5 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.84 | 12.18 | 19.88 | 1.00 | 87.4 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.91 | 11.34 | 18.06 | 1.00 | 72.8 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.84 | 11.27 | 18.60 | 6.00 | 83.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.76 | 10.90 | 17.46 | 2.00 | 86.0 | 90.0 |
| Bench 2 | Bench | O'Shea | DEF | 12 | 4.0 | 3.08 | 8.38 | 13.29 | 1.00 | 78.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.66 | 22.29 | 36.35 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.06 | 17.75 | 28.33 | 12.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Wissa | FWD | 17 | 6.1 | 2.88 | 8.61 | 14.30 | 2.00 | 57.6 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.70 | 19.16 | 30.14 | 8.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.10 | 16.77 | 28.77 | 2.00 | 83.5 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.94 | 13.43 | 21.83 | 3.00 | 84.0 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 4.25 | 12.33 | 19.95 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.70 | 8.77 | 15.05 | 4.00 | 42.4 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 68.89
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.43) beats the best remaining Triple Captain opportunity (9.18).
- Transfer: Wissa -> Calvert-Lewin (projected gain 2.90, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.43) beats the best remaining Triple Captain opportunity (9.18).
- Autosub: Scott replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.21 | 12.70 | 20.32 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.00 | 0.11 | 0.28 | 0.00 | 3.2 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.99 | 12.00 | 19.45 | 4.00 | 88.3 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.88 | 11.00 | 19.10 | 1.00 | 90.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.55 | 9.82 | 16.37 | 1.00 | 79.2 | 77.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.69 | 7.25 | 12.36 | 2.00 | 73.2 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.16 | 6.81 | 11.60 | 0.00 | 46.0 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.43 | 24.51 | 39.13 | 6.00 | 90.0 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 5.07 | 13.15 | 20.56 | 2.00 | 80.4 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.90 | 12.44 | 20.64 | 0.00 | 73.2 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.32 | 18.30 | 30.37 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.02 | 15.30 | 24.76 | 2.00 | 84.5 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.03 | 12.02 | 20.14 | 2.00 | 77.7 | 80.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.63 | 10.47 | 17.38 | 0.00 | 68.2 | 21.0 |
| Bench 2 | Autosub In | Scott | MID | 3 | 6.1 | 3.42 | 10.27 | 17.52 | 2.00 | 73.3 | 90.0 |

## GW6

- Train rows: 194240
- Bank: 0.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 66.83
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.60) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Groß (projected gain 9.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.60) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.47 | 12.99 | 20.94 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Davies | GK | 14 | 4.0 | 0.00 | 0.09 | 0.22 | 0.00 | 3.7 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.37 | 10.91 | 18.06 | 6.00 | 88.1 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.18 | 9.50 | 17.62 | 1.00 | 85.7 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.16 | 8.82 | 14.97 | 1.00 | 73.5 | 90.0 |
| XI | XI | O'Shea | DEF | 12 | 4.0 | 3.29 | 8.40 | 13.26 | 11.00 | 79.3 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.75 | 5.90 | 12.75 | 3.00 | 43.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.96 | 23.57 | 38.46 | 6.00 | 90.0 | 79.0 |
| Bench 2 | Bench Boost | João Pedro | FWD | 6 | 7.6 | 3.14 | 10.09 | 17.31 | 12.00 | 42.1 | 71.0 |
| Bench 3 | Bench Boost | Calvert-Lewin | FWD | 13 | 6.0 | 2.71 | 9.31 | 15.23 | 2.00 | 60.3 | 90.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.9 | 7.18 | 18.96 | 29.59 | 6.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 5.97 | 17.69 | 29.69 | 1.00 | 89.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.29 | 14.98 | 24.13 | 9.00 | 89.6 | 83.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.62 | 11.36 | 19.09 | 0.00 | 73.0 | 0.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 3.78 | 10.64 | 17.44 | 0.00 | 75.1 | 0.0 |