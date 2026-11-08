# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 334.79
- Total actual points: 316.00
- Average predicted points: 66.96
- Average actual points: 63.20
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
- Predicted score: 69.62
- Actual score: 90.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.55 | 12.50 | 19.88 | 6.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Dubravka | GK | 19 | 4.0 | 0.89 | 2.25 | 3.84 | 0.00 | 11.7 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 6.05 | 15.39 | 24.33 | 1.00 | 74.2 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.75 | 13.69 | 22.09 | 2.00 | 88.4 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.96 | 13.02 | 20.56 | 9.00 | 90.8 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 4.85 | 12.35 | 20.02 | 6.00 | 65.1 | 90.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 3.82 | 11.04 | 17.76 | 0.00 | 89.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.24 | 23.09 | 37.55 | 13.00 | 90.8 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.75 | 17.31 | 28.03 | 9.00 | 90.8 | 90.0 |
| Bench 3 | Bench | Gonzalo | FWD | 10 | 6.0 | 4.11 | 11.77 | 18.85 | 2.00 | 88.0 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.52 | 18.78 | 31.30 | 23.00 | 91.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.58 | 16.42 | 26.77 | 4.00 | 90.5 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.75 | 15.62 | 25.94 | 4.00 | 86.5 | 90.0 |
| Bench 2 | Bench | Rogers | MID | 6 | 7.5 | 4.55 | 14.70 | 24.23 | 5.00 | 82.9 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.38 | 14.11 | 22.40 | 0.00 | 73.7 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 67.69
- Actual score: 53.00
- Transfer: Gonzalo -> Wissa (projected gain 3.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.90 | 11.37 | 18.33 | 3.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Dubravka | GK | 19 | 4.0 | 0.91 | 2.55 | 4.26 | 0.00 | 12.9 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 5.22 | 13.97 | 21.67 | 5.00 | 90.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.96 | 13.45 | 21.08 | 6.00 | 91.1 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.36 | 11.05 | 18.21 | 8.00 | 81.1 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.82 | 10.78 | 17.13 | 8.00 | 67.3 | 70.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.74 | 7.68 | 12.35 | 3.00 | 77.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.13 | 25.25 | 40.77 | 9.00 | 90.6 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.70 | 15.87 | 26.26 | 1.00 | 89.4 | 90.0 |
| XI | XI | Wissa | FWD | 17 | 6.1 | 5.11 | 14.22 | 21.46 | 1.00 | 90.5 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.81 | 21.91 | 36.88 | 2.00 | 91.1 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.09 | 15.08 | 23.87 | 0.00 | 86.0 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.45 | 14.83 | 24.11 | 3.00 | 89.3 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.84 | 13.76 | 23.15 | 6.00 | 76.5 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.2 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 61.91
- Actual score: 71.00
- Transfer: Tzolis -> Scott (projected gain 2.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.19 | 12.50 | 19.79 | 14.00 | 90.5 | 90.0 |
| Bench 1 | Bench | Dubravka | GK | 19 | 4.0 | 0.90 | 2.57 | 4.14 | 0.00 | 11.8 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.73 | 11.33 | 18.74 | 6.00 | 83.2 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.81 | 11.21 | 17.58 | 1.00 | 72.3 | 58.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.77 | 10.92 | 17.42 | 2.00 | 86.8 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.56 | 10.68 | 16.76 | 1.00 | 76.0 | 90.0 |
| Bench 2 | Bench | O'Shea | DEF | 12 | 4.0 | 2.99 | 8.24 | 13.14 | 1.00 | 78.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.83 | 22.98 | 37.74 | 9.00 | 90.7 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.06 | 18.02 | 28.70 | 12.00 | 90.8 | 90.0 |
| Bench 3 | Bench | Wissa | FWD | 17 | 6.1 | 2.82 | 9.12 | 14.35 | 2.00 | 57.2 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.57 | 19.33 | 30.29 | 8.00 | 90.6 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.26 | 17.49 | 30.28 | 2.00 | 85.2 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.04 | 14.11 | 22.93 | 3.00 | 83.6 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 4.25 | 12.33 | 19.81 | 4.00 | 90.7 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 68.74
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.60) beats the best remaining Triple Captain opportunity (9.37).
- Transfer: Wissa -> Calvert-Lewin (projected gain 2.91, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.60) beats the best remaining Triple Captain opportunity (9.37).
- Autosub: Scott replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.15 | 12.68 | 20.42 | 1.00 | 90.8 | 90.0 |
| Bench 1 | Bench | Dubravka | GK | 19 | 4.0 | 0.88 | 2.45 | 4.02 | 0.00 | 10.5 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.91 | 11.94 | 19.42 | 4.00 | 87.8 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.43 | 9.94 | 15.71 | 1.00 | 78.3 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.44 | 9.75 | 16.07 | 1.00 | 79.2 | 77.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.56 | 7.16 | 12.12 | 2.00 | 72.5 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.15 | 6.78 | 11.40 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.60 | 24.96 | 40.41 | 6.00 | 90.5 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 5.00 | 13.39 | 20.71 | 2.00 | 80.5 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.91 | 12.69 | 21.45 | 0.00 | 68.6 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.42 | 18.94 | 32.01 | 2.00 | 91.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 4.98 | 15.91 | 25.19 | 2.00 | 83.2 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.14 | 12.66 | 21.16 | 2.00 | 76.8 | 80.0 |
| Bench 2 | Autosub In | Scott | MID | 3 | 6.1 | 3.41 | 10.50 | 17.53 | 2.00 | 73.1 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.55 | 10.43 | 17.43 | 0.00 | 68.7 | 21.0 |

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
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Groß (projected gain 10.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.31 | 12.87 | 20.61 | 3.00 | 89.9 | 90.0 |
| Bench 1 | Bench Boost | Dubravka | GK | 19 | 4.0 | 0.70 | 2.38 | 4.09 | 0.00 | 12.2 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.28 | 10.97 | 18.08 | 6.00 | 87.7 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.56 | 1.00 | 72.6 | 90.0 |
| Bench 2 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 2.85 | 8.70 | 14.21 | 1.00 | 75.3 | 90.0 |
| XI | XI | O'Shea | DEF | 12 | 4.0 | 3.23 | 8.37 | 13.23 | 11.00 | 79.4 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.96 | 6.56 | 12.77 | 3.00 | 41.2 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.01 | 23.88 | 39.31 | 6.00 | 90.2 | 79.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 3.89 | 12.69 | 22.89 | 12.00 | 56.7 | 71.0 |
| Bench 3 | Bench Boost | Calvert-Lewin | FWD | 13 | 6.0 | 2.57 | 9.37 | 15.15 | 2.00 | 58.6 | 90.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.9 | 6.95 | 19.26 | 29.44 | 6.00 | 91.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.03 | 18.06 | 30.65 | 1.00 | 91.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.31 | 15.45 | 24.67 | 9.00 | 89.2 | 83.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.64 | 11.64 | 19.74 | 0.00 | 72.5 | 0.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 3.02 | 9.18 | 14.53 | 0.00 | 63.5 | 0.0 |