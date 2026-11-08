# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 324.16
- Total actual points: 339.00
- Average predicted points: 64.83
- Average actual points: 67.80
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
- Predicted score: 66.90
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.54 | 12.89 | 20.58 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Matthews | GK | 8 | 4.0 | 0.02 | 0.22 | 0.43 | 0.00 | 5.0 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.65 | 14.79 | 23.84 | 1.00 | 74.6 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.40 | 13.46 | 22.02 | 2.00 | 89.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.61 | 12.50 | 19.90 | 9.00 | 89.7 | 90.0 |
| Bench 2 | Bench | De Cuyper | DEF | 5 | 4.6 | 3.90 | 12.01 | 19.46 | 0.00 | 70.6 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 3.61 | 10.84 | 17.50 | 0.00 | 89.2 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.01 | 22.78 | 37.51 | 13.00 | 89.7 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.45 | 16.76 | 27.22 | 9.00 | 89.4 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 3.16 | 9.84 | 17.07 | 1.00 | 55.2 | 45.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.48 | 19.15 | 31.74 | 23.00 | 90.7 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.28 | 16.28 | 26.64 | 4.00 | 89.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.70 | 15.43 | 25.70 | 4.00 | 86.6 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.52 | 14.79 | 24.50 | 5.00 | 83.7 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.25 | 14.22 | 22.49 | 0.00 | 75.6 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 64.49
- Actual score: 56.00
- Transfer: O'Shea -> Ajayi (projected gain 4.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.83 | 11.63 | 19.17 | 3.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Matthews | GK | 8 | 4.0 | 0.00 | 0.08 | 0.23 | 0.00 | 3.3 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.10 | 14.38 | 23.33 | 5.00 | 88.3 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.83 | 13.20 | 20.95 | 6.00 | 91.0 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.00 | 12.65 | 19.47 | 4.00 | 82.0 | 76.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.76 | 11.36 | 19.03 | 8.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.49 | 10.43 | 17.18 | 8.00 | 69.8 | 70.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.90 | 24.88 | 40.30 | 9.00 | 88.6 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.46 | 15.68 | 25.94 | 1.00 | 89.4 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.16 | 6.98 | 11.92 | 2.00 | 41.5 | 65.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.63 | 21.79 | 36.61 | 2.00 | 90.6 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.03 | 14.81 | 23.76 | 0.00 | 85.7 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.15 | 14.77 | 24.02 | 3.00 | 88.7 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.90 | 14.08 | 23.32 | 6.00 | 77.8 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 59.75
- Actual score: 71.00
- Transfer: Tzolis -> Scott (projected gain 1.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.99 | 12.08 | 19.67 | 14.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Matthews | GK | 8 | 4.0 | 0.18 | 0.28 | 0.41 | 0.00 | 3.4 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.52 | 11.43 | 18.87 | 1.00 | 82.6 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.48 | 10.90 | 18.59 | 6.00 | 85.8 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.58 | 10.77 | 17.77 | 1.00 | 75.8 | 58.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.47 | 10.57 | 17.16 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench | De Cuyper | DEF | 5 | 4.7 | 3.26 | 10.13 | 16.21 | 11.00 | 66.2 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.61 | 22.69 | 37.56 | 9.00 | 89.2 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.73 | 17.44 | 27.91 | 12.00 | 89.4 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.58 | 7.39 | 12.31 | 12.00 | 49.0 | 62.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.55 | 19.33 | 30.25 | 8.00 | 89.9 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.22 | 17.55 | 30.50 | 2.00 | 85.3 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.88 | 14.17 | 23.12 | 3.00 | 84.3 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 4.13 | 11.96 | 19.45 | 4.00 | 90.7 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 65.60
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.41) beats the best remaining Triple Captain opportunity (9.17).
- Transfer: Scott -> Groß (projected gain 2.97, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.41) beats the best remaining Triple Captain opportunity (9.17).
- Autosub: De Cuyper replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.10 | 12.58 | 20.34 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Matthews | GK | 8 | 4.0 | 0.05 | 0.20 | 0.28 | 0.00 | 3.1 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.76 | 11.75 | 19.79 | 4.00 | 89.7 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.27 | 9.98 | 17.40 | 1.00 | 84.3 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.12 | 9.35 | 15.96 | 1.00 | 80.4 | 77.0 |
| Bench 2 | Autosub In | De Cuyper | DEF | 5 | 4.7 | 2.29 | 9.06 | 15.77 | 6.00 | 67.9 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.15 | 6.78 | 11.40 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.41 | 24.66 | 40.22 | 6.00 | 88.5 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.54 | 11.93 | 20.55 | 0.00 | 68.8 | 0.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.61 | 8.68 | 14.41 | 2.00 | 53.2 | 80.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.30 | 19.26 | 31.92 | 2.00 | 90.6 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.00 | 16.03 | 25.70 | 2.00 | 84.4 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 3.93 | 12.92 | 21.15 | 14.00 | 92.4 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.85 | 12.57 | 21.35 | 2.00 | 77.9 | 80.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.49 | 10.25 | 17.48 | 0.00 | 69.6 | 21.0 |

## GW6

- Train rows: 194240
- Bank: 0.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 67.42
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.47) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Schade (projected gain 7.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.47) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.19 | 12.74 | 20.80 | 3.00 | 89.7 | 90.0 |
| Bench 1 | Bench Boost | Matthews | GK | 8 | 4.0 | 0.17 | 0.35 | 0.58 | 0.00 | 4.0 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 4.73 | 13.83 | 21.59 | 15.00 | 90.0 | 67.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.03 | 10.37 | 17.77 | 6.00 | 90.2 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.57 | 1.00 | 72.6 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 2.71 | 8.66 | 15.87 | 1.00 | 80.3 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.85 | 6.38 | 12.77 | 3.00 | 42.3 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.78 | 23.26 | 38.22 | 6.00 | 88.6 | 79.0 |
| Bench 3 | Bench Boost | João Pedro | FWD | 6 | 7.6 | 2.73 | 9.50 | 17.10 | 12.00 | 37.1 | 71.0 |
| Bench 2 | Bench Boost | Emersonn | FWD | 12 | 5.5 | 3.00 | 8.60 | 14.01 | 2.00 | 57.3 | 70.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 6.84 | 19.07 | 29.26 | 6.00 | 91.6 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 5.97 | 18.12 | 30.77 | 1.00 | 90.2 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.37 | 15.78 | 25.16 | 9.00 | 90.2 | 83.0 |
| XI | XI | Schade | MID | 4 | 6.2 | 4.82 | 14.03 | 22.05 | 1.00 | 90.4 | 51.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.38 | 11.47 | 19.76 | 0.00 | 71.9 | 0.0 |