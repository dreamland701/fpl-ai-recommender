# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 338.45
- Total actual points: 315.00
- Average predicted points: 67.69
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
- Predicted score: 69.86
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.59 | 12.51 | 19.99 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.11 | 0.15 | 0.26 | 0.00 | 1.5 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 6.10 | 15.40 | 24.49 | 1.00 | 73.1 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.76 | 13.65 | 22.21 | 2.00 | 87.9 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.99 | 13.04 | 20.68 | 9.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.0 | 4.39 | 11.16 | 18.25 | 6.00 | 53.5 | 90.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 3.88 | 11.08 | 17.81 | 0.00 | 87.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.26 | 23.07 | 37.70 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.80 | 17.30 | 28.13 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Gonzalo | FWD | 10 | 6.0 | 4.12 | 11.73 | 18.97 | 2.00 | 87.3 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.61 | 18.88 | 31.40 | 23.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.63 | 16.47 | 26.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.83 | 15.68 | 25.96 | 4.00 | 86.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.59 | 14.70 | 24.37 | 5.00 | 80.7 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.42 | 14.16 | 22.53 | 0.00 | 72.1 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 68.52
- Actual score: 53.00
- Transfer: Gonzalo -> Wissa (projected gain 4.00, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.93 | 11.31 | 18.45 | 3.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.00 | 0.00 | 0.07 | 0.00 | 1.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 5.67 | 15.68 | 24.88 | 5.00 | 90.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 5.02 | 13.53 | 21.25 | 6.00 | 90.0 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.13 | 11.61 | 19.04 | 8.00 | 77.8 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.84 | 10.72 | 17.19 | 8.00 | 66.5 | 70.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.74 | 7.68 | 12.35 | 3.00 | 79.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.17 | 25.29 | 40.80 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.74 | 15.92 | 26.43 | 1.00 | 88.7 | 90.0 |
| XI | XI | Wissa | FWD | 17 | 6.1 | 5.19 | 14.23 | 21.53 | 1.00 | 90.0 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.91 | 22.03 | 36.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.17 | 15.15 | 23.95 | 0.00 | 85.9 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.49 | 14.85 | 24.20 | 3.00 | 88.7 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.92 | 13.81 | 23.32 | 6.00 | 75.7 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 33.0 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 62.94
- Actual score: 71.00
- Transfer: Tzolis -> Scott (projected gain 2.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.20 | 12.33 | 19.80 | 14.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.17 | 0.27 | 0.40 | 0.00 | 2.4 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.93 | 12.32 | 19.98 | 1.00 | 81.8 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.83 | 11.37 | 18.88 | 6.00 | 82.1 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.88 | 11.17 | 17.79 | 1.00 | 71.9 | 58.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.79 | 10.93 | 17.52 | 2.00 | 86.1 | 90.0 |
| Bench 2 | Bench | O'Shea | DEF | 12 | 4.0 | 2.99 | 8.24 | 13.14 | 1.00 | 79.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.91 | 23.03 | 37.86 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.11 | 18.07 | 28.86 | 12.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Wissa | FWD | 17 | 6.1 | 2.89 | 9.15 | 14.46 | 2.00 | 54.7 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.64 | 19.39 | 30.39 | 8.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.34 | 17.54 | 30.24 | 2.00 | 84.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.10 | 14.01 | 22.99 | 3.00 | 82.1 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 4.30 | 12.37 | 19.93 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 43.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 69.88
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (9.45).
- Transfer: Wissa -> Calvert-Lewin (projected gain 2.90, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (9.45).
- Autosub: Scott replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.19 | 12.66 | 20.46 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.01 | 0.18 | 0.38 | 0.00 | 3.5 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.00 | 11.96 | 19.57 | 4.00 | 87.3 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.79 | 11.24 | 18.89 | 1.00 | 86.2 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.48 | 9.78 | 16.21 | 1.00 | 77.7 | 77.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.56 | 7.16 | 12.12 | 2.00 | 74.0 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.15 | 6.78 | 11.40 | 0.00 | 46.1 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.67 | 25.00 | 40.62 | 6.00 | 90.0 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 5.05 | 13.40 | 20.85 | 2.00 | 77.7 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 4.00 | 12.66 | 21.59 | 0.00 | 66.6 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.51 | 19.05 | 32.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.03 | 15.94 | 25.28 | 2.00 | 81.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.20 | 12.60 | 21.31 | 2.00 | 74.3 | 80.0 |
| Bench 2 | Autosub In | Scott | MID | 3 | 6.1 | 3.46 | 10.52 | 17.66 | 2.00 | 72.1 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.64 | 10.49 | 17.42 | 0.00 | 69.5 | 21.0 |

## GW6

- Train rows: 194240
- Bank: 0.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 67.24
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.60) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Groß (projected gain 10.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.60) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.40 | 12.88 | 20.80 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Davies | GK | 14 | 4.0 | 0.00 | 0.14 | 0.34 | 0.00 | 4.1 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.38 | 10.90 | 18.23 | 6.00 | 87.5 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.11 | 9.73 | 17.36 | 1.00 | 81.7 | 90.0 |
| Bench 2 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.57 | 1.00 | 72.0 | 90.0 |
| XI | XI | O'Shea | DEF | 12 | 4.0 | 3.24 | 8.37 | 13.23 | 11.00 | 80.0 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.85 | 6.38 | 12.77 | 3.00 | 46.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.13 | 23.97 | 39.52 | 6.00 | 90.0 | 79.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 3.20 | 10.42 | 18.22 | 12.00 | 37.7 | 71.0 |
| Bench 3 | Bench Boost | Calvert-Lewin | FWD | 13 | 6.0 | 2.69 | 9.47 | 15.35 | 2.00 | 56.2 | 90.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.9 | 7.04 | 19.33 | 29.56 | 6.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.12 | 18.14 | 30.68 | 1.00 | 89.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.39 | 15.51 | 24.88 | 9.00 | 88.9 | 83.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.72 | 11.68 | 19.84 | 0.00 | 71.5 | 0.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 3.79 | 10.67 | 17.62 | 0.00 | 73.8 | 0.0 |