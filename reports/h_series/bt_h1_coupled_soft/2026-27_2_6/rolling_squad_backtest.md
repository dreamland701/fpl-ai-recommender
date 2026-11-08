# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 337.55
- Total actual points: 339.00
- Average predicted points: 67.51
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
- Predicted score: 69.63
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.59 | 12.51 | 19.99 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.23 | 0.56 | 0.00 | 2.5 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.78 | 15.13 | 24.23 | 1.00 | 73.5 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.74 | 13.64 | 22.19 | 2.00 | 87.9 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.99 | 13.04 | 20.68 | 9.00 | 90.0 | 90.0 |
| Bench 2 | Bench | De Cuyper | DEF | 5 | 4.6 | 4.06 | 12.16 | 19.45 | 0.00 | 68.1 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 3.86 | 11.07 | 17.80 | 0.00 | 87.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.26 | 23.07 | 37.70 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.80 | 17.30 | 28.13 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 3.15 | 9.88 | 16.79 | 1.00 | 52.8 | 45.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.61 | 18.88 | 31.40 | 23.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.63 | 16.47 | 26.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.83 | 15.68 | 25.96 | 4.00 | 85.2 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.61 | 14.73 | 24.39 | 5.00 | 82.0 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.51 | 14.24 | 22.60 | 0.00 | 72.9 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 67.60
- Actual score: 56.00
- Transfer: O'Shea -> Ajayi (projected gain 5.19, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.90 | 11.29 | 18.43 | 3.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.02 | 0.14 | 0.00 | 2.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.67 | 15.68 | 24.88 | 5.00 | 90.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 5.02 | 13.53 | 21.25 | 6.00 | 90.0 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.31 | 12.84 | 19.69 | 4.00 | 80.3 | 76.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.07 | 11.55 | 18.98 | 8.00 | 77.7 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.72 | 10.61 | 17.08 | 8.00 | 66.6 | 70.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.17 | 25.29 | 40.80 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.75 | 15.93 | 26.43 | 1.00 | 88.7 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.16 | 6.98 | 11.92 | 2.00 | 41.5 | 65.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.91 | 22.03 | 36.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.16 | 15.14 | 23.94 | 0.00 | 84.6 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.49 | 14.85 | 24.20 | 3.00 | 88.7 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.97 | 13.87 | 23.38 | 6.00 | 75.4 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 62.53
- Actual score: 71.00
- Transfer: Tzolis -> Scott (projected gain 1.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.20 | 12.33 | 19.80 | 14.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.21 | 0.41 | 0.00 | 3.5 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.64 | 12.02 | 19.69 | 1.00 | 83.2 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.77 | 11.31 | 18.82 | 6.00 | 82.9 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.78 | 11.06 | 17.69 | 1.00 | 72.2 | 58.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.77 | 10.92 | 17.51 | 2.00 | 86.1 | 90.0 |
| Bench 2 | Bench | De Cuyper | DEF | 5 | 4.7 | 3.54 | 10.46 | 16.45 | 11.00 | 63.7 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.91 | 23.03 | 37.86 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.11 | 18.07 | 28.86 | 12.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.58 | 7.39 | 12.31 | 12.00 | 49.0 | 62.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.64 | 19.39 | 30.39 | 8.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.38 | 17.59 | 30.28 | 2.00 | 83.8 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.12 | 14.03 | 23.01 | 3.00 | 83.2 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 4.30 | 12.37 | 19.93 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 68.48
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (9.45).
- Transfer: Scott -> Groß (projected gain 2.83, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (9.45).
- Autosub: De Cuyper replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.19 | 12.66 | 20.46 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.11 | 0.33 | 0.49 | 0.00 | 3.1 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.00 | 11.96 | 19.57 | 4.00 | 87.3 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.62 | 11.08 | 18.72 | 1.00 | 86.2 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.44 | 9.73 | 16.16 | 1.00 | 78.3 | 77.0 |
| Bench 2 | Autosub In | De Cuyper | DEF | 5 | 4.7 | 2.25 | 9.36 | 15.93 | 6.00 | 67.5 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.15 | 6.78 | 11.40 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.67 | 25.00 | 40.62 | 6.00 | 90.0 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.61 | 12.26 | 21.17 | 0.00 | 68.4 | 0.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.61 | 8.68 | 14.41 | 2.00 | 53.2 | 80.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.51 | 19.05 | 32.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.07 | 15.99 | 25.32 | 2.00 | 82.5 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.17 | 13.14 | 21.58 | 14.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.23 | 12.62 | 21.34 | 2.00 | 76.4 | 80.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.65 | 10.50 | 17.43 | 0.00 | 67.3 | 21.0 |

## GW6

- Train rows: 194240
- Bank: 0.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 69.31
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.88) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Schade (projected gain 7.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.88) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.40 | 12.88 | 20.80 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Palmer | GK | 12 | 4.0 | 0.32 | 0.52 | 0.82 | 0.00 | 4.4 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 5.15 | 14.48 | 22.67 | 15.00 | 90.0 | 67.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.36 | 10.89 | 18.22 | 6.00 | 87.5 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 2.79 | 9.39 | 17.00 | 1.00 | 82.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.57 | 1.00 | 72.6 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.85 | 6.38 | 12.77 | 3.00 | 42.3 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.13 | 23.97 | 39.52 | 6.00 | 90.0 | 79.0 |
| Bench 3 | Bench Boost | João Pedro | FWD | 6 | 7.6 | 1.91 | 9.02 | 16.75 | 12.00 | 38.4 | 71.0 |
| Bench 2 | Bench Boost | Emersonn | FWD | 12 | 5.5 | 3.00 | 8.60 | 14.01 | 2.00 | 57.3 | 70.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 7.04 | 19.33 | 29.56 | 6.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.09 | 18.11 | 30.65 | 1.00 | 89.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.38 | 15.50 | 24.87 | 9.00 | 88.9 | 83.0 |
| XI | XI | Schade | MID | 4 | 6.2 | 5.10 | 14.32 | 22.38 | 1.00 | 90.0 | 51.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.59 | 11.56 | 19.70 | 0.00 | 71.4 | 0.0 |