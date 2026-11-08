# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 333.09
- Total actual points: 335.00
- Average predicted points: 66.62
- Average actual points: 67.00
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
- Predicted score: 69.00
- Actual score: 95.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.65 | 13.01 | 20.48 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.11 | 0.15 | 0.26 | 0.00 | 1.5 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.88 | 14.85 | 23.57 | 1.00 | 73.6 | 58.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.86 | 13.46 | 21.02 | 11.00 | 88.8 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.71 | 13.32 | 21.87 | 2.00 | 88.9 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.78 | 12.44 | 19.67 | 9.00 | 87.7 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 3.71 | 10.71 | 16.89 | 0.00 | 87.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.22 | 23.18 | 37.42 | 13.00 | 88.7 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.59 | 16.99 | 27.13 | 9.00 | 88.1 | 90.0 |
| Bench 4 | Bench | Walle Egeli | FWD | 12 | 4.5 | 0.80 | 2.93 | 5.09 | 0.00 | 14.4 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.56 | 19.04 | 30.96 | 23.00 | 89.3 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.44 | 16.50 | 26.48 | 4.00 | 88.1 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.68 | 15.38 | 24.96 | 4.00 | 84.8 | 90.0 |
| Bench 2 | Bench | Rogers | MID | 6 | 7.5 | 4.63 | 14.83 | 24.07 | 5.00 | 81.9 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.41 | 14.54 | 22.51 | 0.00 | 74.8 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 66.78
- Actual score: 54.00
- Transfer: O'Shea -> Ajayi (projected gain 6.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.95 | 11.33 | 18.54 | 3.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.00 | 0.00 | 0.07 | 0.00 | 1.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.44 | 14.95 | 23.61 | 5.00 | 88.5 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.74 | 13.73 | 21.57 | 2.00 | 88.7 | 66.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.85 | 12.96 | 20.48 | 6.00 | 89.5 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.97 | 11.30 | 18.63 | 8.00 | 78.3 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.28 | 9.22 | 14.97 | 8.00 | 58.6 | 70.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.02 | 24.76 | 39.71 | 9.00 | 87.5 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.66 | 15.86 | 25.81 | 1.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Walle Egeli | FWD | 12 | 4.5 | 0.41 | 1.52 | 2.57 | 0.00 | 7.1 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.77 | 21.73 | 36.24 | 2.00 | 88.7 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.17 | 14.84 | 23.20 | 0.00 | 84.7 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.27 | 14.72 | 23.59 | 3.00 | 87.6 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.93 | 13.94 | 22.56 | 6.00 | 75.7 | 86.0 |
| Bench 3 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 62.39
- Actual score: 75.00
- Transfer: Tzolis -> Scott (projected gain 1.32, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.09 | 12.18 | 19.59 | 14.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.17 | 0.27 | 0.40 | 0.00 | 2.4 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.59 | 13.63 | 21.50 | 6.00 | 78.2 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.76 | 11.92 | 19.46 | 1.00 | 83.9 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.72 | 11.08 | 17.55 | 1.00 | 73.6 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.67 | 11.06 | 18.56 | 6.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 3.65 | 10.52 | 16.56 | 2.00 | 86.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.78 | 22.77 | 37.24 | 9.00 | 87.9 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.92 | 17.65 | 27.95 | 12.00 | 87.7 | 90.0 |
| Bench 4 | Bench | Walle Egeli | FWD | 12 | 4.5 | 0.21 | 1.00 | 1.76 | 0.00 | 4.1 | 0.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.65 | 19.40 | 29.77 | 8.00 | 89.7 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.28 | 17.64 | 30.01 | 2.00 | 84.5 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.92 | 14.03 | 22.67 | 3.00 | 82.7 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 4.23 | 11.77 | 18.59 | 4.00 | 87.6 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 68.47
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.54) beats the best remaining Triple Captain opportunity (9.31).
- Transfer: Scott -> Groß (projected gain 2.23, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.54) beats the best remaining Triple Captain opportunity (9.31).
- Autosub: Egan replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.14 | 12.83 | 20.10 | 1.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.01 | 0.18 | 0.38 | 0.00 | 3.5 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.20 | 12.92 | 20.62 | 1.00 | 82.0 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.91 | 11.94 | 19.36 | 4.00 | 88.6 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.53 | 10.55 | 17.65 | 1.00 | 84.4 | 90.0 |
| Bench 2 | Autosub In | Egan | DEF | 11 | 4.0 | 3.31 | 9.45 | 15.72 | 1.00 | 78.4 | 77.0 |
| Bench 3 | Bench | Mendy | DEF | 11 | 4.0 | 2.15 | 6.78 | 11.40 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.54 | 24.85 | 40.36 | 6.00 | 88.2 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.83 | 12.31 | 21.20 | 0.00 | 68.1 | 0.0 |
| Bench 4 | Bench | Walle Egeli | FWD | 12 | 4.5 | 0.28 | 0.91 | 1.51 | 0.00 | 3.4 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.36 | 18.98 | 31.85 | 2.00 | 90.1 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.17 | 15.97 | 24.96 | 2.00 | 83.2 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.05 | 12.78 | 20.99 | 14.00 | 89.8 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.05 | 12.72 | 21.23 | 2.00 | 76.7 | 80.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.62 | 10.61 | 17.24 | 0.00 | 68.8 | 21.0 |

## GW6

- Train rows: 194240
- Bank: 0.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 66.45
- Actual score: 65.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.19) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Schade (projected gain 5.46, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.19) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.38 | 12.94 | 20.67 | 3.00 | 88.8 | 90.0 |
| Bench 1 | Bench Boost | Davies | GK | 14 | 4.0 | 0.00 | 0.14 | 0.34 | 0.00 | 4.1 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.71 | 13.51 | 21.38 | 9.00 | 87.6 | 81.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.28 | 10.62 | 17.82 | 6.00 | 87.4 | 90.0 |
| Bench 2 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 2.90 | 8.90 | 15.98 | 1.00 | 80.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.57 | 1.00 | 72.6 | 90.0 |
| Bench 3 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.85 | 6.38 | 12.77 | 3.00 | 42.3 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.01 | 23.74 | 38.96 | 6.00 | 87.0 | 79.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 2.91 | 9.71 | 17.34 | 12.00 | 36.5 | 71.0 |
| Bench 4 | Bench Boost | Walle Egeli | FWD | 12 | 4.5 | 0.43 | 0.94 | 1.59 | 1.00 | 4.0 | 9.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 6.88 | 18.64 | 28.52 | 6.00 | 88.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 5.98 | 17.91 | 29.98 | 1.00 | 88.6 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.49 | 15.44 | 24.28 | 9.00 | 89.7 | 83.0 |
| XI | XI | Schade | MID | 4 | 6.2 | 5.01 | 14.30 | 21.76 | 1.00 | 90.3 | 51.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.55 | 11.65 | 19.35 | 0.00 | 70.7 | 0.0 |