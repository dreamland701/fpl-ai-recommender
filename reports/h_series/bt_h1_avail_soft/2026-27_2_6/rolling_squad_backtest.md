# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 341.90
- Total actual points: 352.00
- Average predicted points: 68.38
- Average actual points: 70.40
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
- Predicted score: 69.86
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.59 | 12.51 | 19.99 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.23 | 0.56 | 0.00 | 2.5 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 6.10 | 15.40 | 24.49 | 1.00 | 74.6 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.76 | 13.65 | 22.21 | 2.00 | 89.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.99 | 13.04 | 20.68 | 9.00 | 89.7 | 90.0 |
| Bench 2 | Bench | De Cuyper | DEF | 5 | 4.6 | 4.15 | 12.24 | 19.52 | 0.00 | 70.6 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 3.88 | 11.08 | 17.81 | 0.00 | 89.2 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.26 | 23.07 | 37.70 | 13.00 | 89.7 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.80 | 17.30 | 28.13 | 9.00 | 89.4 | 90.0 |
| Bench 4 | Bench | McBurnie | FWD | 11 | 5.5 | 4.18 | 10.89 | 17.19 | 1.00 | 71.5 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.61 | 18.88 | 31.40 | 23.00 | 90.7 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.63 | 16.47 | 26.87 | 4.00 | 89.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.83 | 15.68 | 25.96 | 4.00 | 86.6 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.59 | 14.70 | 24.37 | 5.00 | 83.7 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.42 | 14.16 | 22.53 | 0.00 | 75.6 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 67.66
- Actual score: 56.00
- Transfer: Mendy -> Ajayi (projected gain 4.97, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.93 | 11.31 | 18.45 | 3.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.02 | 0.14 | 0.00 | 2.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.67 | 15.68 | 24.88 | 5.00 | 88.3 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 5.02 | 13.53 | 21.25 | 6.00 | 91.0 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.33 | 12.86 | 19.71 | 4.00 | 82.0 | 76.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.13 | 11.61 | 19.04 | 8.00 | 80.7 | 90.0 |
| Bench 2 | Bench | O'Shea | DEF | 12 | 4.0 | 2.74 | 7.68 | 12.35 | 3.00 | 77.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.17 | 25.29 | 40.80 | 9.00 | 88.6 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.74 | 15.92 | 26.43 | 1.00 | 89.4 | 90.0 |
| Bench 3 | Bench | McBurnie | FWD | 11 | 5.5 | 3.22 | 8.83 | 14.12 | 2.00 | 66.0 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.91 | 22.03 | 36.99 | 2.00 | 90.6 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.17 | 15.15 | 23.95 | 0.00 | 85.7 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.49 | 14.85 | 24.20 | 3.00 | 88.7 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.92 | 13.81 | 23.32 | 6.00 | 77.8 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 62.72
- Actual score: 81.00
- Transfer: Tzolis -> Scott (projected gain 2.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.20 | 12.33 | 19.80 | 14.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.21 | 0.41 | 0.00 | 3.5 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.93 | 12.32 | 19.98 | 1.00 | 82.6 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.83 | 11.37 | 18.88 | 6.00 | 85.8 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.79 | 10.93 | 17.52 | 2.00 | 87.5 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.66 | 10.58 | 16.56 | 11.00 | 66.2 | 90.0 |
| Bench 2 | Bench | O'Shea | DEF | 12 | 4.0 | 2.99 | 8.24 | 13.14 | 1.00 | 78.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.91 | 23.03 | 37.86 | 9.00 | 89.2 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.11 | 18.07 | 28.86 | 12.00 | 89.4 | 90.0 |
| Bench 3 | Bench | McBurnie | FWD | 11 | 5.5 | 2.96 | 8.56 | 13.86 | 4.00 | 72.6 | 81.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.64 | 19.39 | 30.39 | 8.00 | 89.9 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.34 | 17.54 | 30.24 | 2.00 | 85.3 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.10 | 14.01 | 22.99 | 3.00 | 84.3 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 4.30 | 12.37 | 19.93 | 4.00 | 90.7 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 68.83
- Actual score: 48.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (9.45).
- Transfer: M.Sangaré -> Groß (projected gain 2.65, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (9.45).
- Autosub: McBurnie replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.19 | 12.66 | 20.46 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.11 | 0.33 | 0.49 | 0.00 | 3.1 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.00 | 11.96 | 19.57 | 4.00 | 89.7 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.79 | 11.24 | 18.89 | 1.00 | 84.3 | 90.0 |
| Bench 3 | Bench | De Cuyper | DEF | 5 | 4.7 | 2.72 | 9.92 | 16.50 | 6.00 | 67.9 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.48 | 9.78 | 16.21 | 1.00 | 80.4 | 77.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 2.56 | 7.16 | 12.12 | 2.00 | 72.5 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.67 | 25.00 | 40.62 | 6.00 | 88.5 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 4.00 | 12.66 | 21.59 | 0.00 | 68.8 | 0.0 |
| Bench 2 | Autosub In | McBurnie | FWD | 11 | 5.5 | 3.04 | 8.68 | 13.93 | 1.00 | 69.4 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.51 | 19.05 | 32.05 | 2.00 | 90.6 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.03 | 15.94 | 25.28 | 2.00 | 84.4 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.17 | 13.14 | 21.58 | 14.00 | 92.4 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.20 | 12.60 | 21.31 | 2.00 | 77.9 | 80.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 3.46 | 10.52 | 17.66 | 2.00 | 73.6 | 90.0 |

## GW6

- Train rows: 194240
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 72.84
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.70) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: McBurnie -> Kostoulas (projected gain 3.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.70) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.40 | 12.88 | 20.80 | 3.00 | 89.7 | 90.0 |
| Bench 1 | Bench Boost | Palmer | GK | 12 | 4.0 | 0.32 | 0.52 | 0.82 | 0.00 | 4.4 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 5.15 | 14.48 | 22.67 | 15.00 | 90.0 | 67.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.38 | 10.90 | 18.23 | 6.00 | 90.2 | 90.0 |
| Bench 2 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 3.11 | 9.73 | 17.36 | 1.00 | 80.3 | 90.0 |
| Bench 3 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.57 | 1.00 | 72.6 | 90.0 |
| XI | XI | O'Shea | DEF | 12 | 4.0 | 3.24 | 8.37 | 13.23 | 11.00 | 79.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.13 | 23.97 | 39.52 | 6.00 | 88.6 | 79.0 |
| XI | XI | Kostoulas | FWD | 5 | 5.6 | 4.67 | 12.75 | 19.35 | 1.00 | 87.3 | 59.0 |
| Bench 4 | Bench Boost | João Pedro | FWD | 6 | 7.6 | 3.20 | 10.42 | 18.22 | 12.00 | 37.1 | 71.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 7.04 | 19.33 | 29.56 | 6.00 | 91.6 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.12 | 18.14 | 30.68 | 1.00 | 90.2 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.39 | 15.51 | 24.88 | 9.00 | 90.2 | 83.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.72 | 11.68 | 19.84 | 0.00 | 71.9 | 0.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 3.79 | 10.67 | 17.62 | 0.00 | 73.3 | 0.0 |