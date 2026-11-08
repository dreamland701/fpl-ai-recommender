# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 342.49
- Total actual points: 351.00
- Average predicted points: 68.50
- Average actual points: 70.20
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
- Predicted score: 70.07
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.59 | 12.51 | 19.99 | 6.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Cairns | GK | 13 | 4.0 | 0.15 | 0.26 | 0.48 | 0.00 | 3.0 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 6.06 | 15.37 | 24.46 | 1.00 | 73.5 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.76 | 13.65 | 22.21 | 2.00 | 87.9 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.99 | 13.04 | 20.68 | 9.00 | 90.0 | 90.0 |
| Bench 3 | Bench | De Cuyper | DEF | 5 | 4.6 | 4.25 | 12.35 | 19.62 | 0.00 | 68.1 | 90.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 3.88 | 11.08 | 17.81 | 0.00 | 87.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.26 | 23.07 | 37.70 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.80 | 17.30 | 28.13 | 9.00 | 90.0 | 90.0 |
| Bench 2 | Bench | McBurnie | FWD | 11 | 5.5 | 4.26 | 10.96 | 17.26 | 1.00 | 74.9 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.61 | 18.88 | 31.40 | 23.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.63 | 16.47 | 26.87 | 4.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.86 | 15.71 | 25.99 | 4.00 | 85.2 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.65 | 14.76 | 24.43 | 5.00 | 82.0 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.59 | 14.30 | 22.67 | 0.00 | 72.9 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 67.79
- Actual score: 56.00
- Transfer: Mendy -> Ajayi (projected gain 4.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.87 | 11.26 | 18.39 | 3.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Cairns | GK | 13 | 4.0 | 0.00 | 0.00 | 0.15 | 0.00 | 3.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.67 | 15.68 | 24.88 | 5.00 | 90.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 5.02 | 13.53 | 21.25 | 6.00 | 90.0 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.36 | 12.90 | 19.74 | 4.00 | 80.3 | 76.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.17 | 11.64 | 19.07 | 8.00 | 77.7 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.73 | 7.67 | 12.35 | 3.00 | 77.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.17 | 25.29 | 40.80 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.74 | 15.92 | 26.43 | 1.00 | 88.7 | 90.0 |
| Bench 2 | Bench | McBurnie | FWD | 11 | 5.5 | 3.30 | 8.91 | 14.19 | 2.00 | 69.3 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.91 | 22.03 | 36.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.20 | 15.18 | 23.98 | 0.00 | 84.6 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.49 | 14.85 | 24.20 | 3.00 | 88.7 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.00 | 13.91 | 23.42 | 6.00 | 75.4 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 1.91 | 6.66 | 11.94 | 5.00 | 34.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 62.89
- Actual score: 81.00
- Transfer: Tzolis -> Scott (projected gain 2.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.20 | 12.33 | 19.80 | 14.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Cairns | GK | 13 | 4.0 | 0.10 | 0.28 | 0.47 | 0.00 | 3.7 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.88 | 12.27 | 19.93 | 1.00 | 83.2 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.83 | 11.37 | 18.88 | 6.00 | 82.9 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.79 | 10.93 | 17.52 | 2.00 | 86.1 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.80 | 10.71 | 16.68 | 11.00 | 63.7 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.99 | 8.24 | 13.14 | 1.00 | 78.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.91 | 23.03 | 37.86 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.11 | 18.07 | 28.86 | 12.00 | 90.0 | 90.0 |
| Bench 2 | Bench | McBurnie | FWD | 11 | 5.5 | 3.02 | 8.61 | 13.91 | 4.00 | 72.6 | 81.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.64 | 19.39 | 30.39 | 8.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.39 | 17.59 | 30.28 | 2.00 | 83.8 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.14 | 14.05 | 23.03 | 3.00 | 83.2 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 4.30 | 12.37 | 19.93 | 4.00 | 90.0 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.61 | 8.80 | 14.97 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 69.48
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (9.45).
- Transfer: Scott -> Groß (projected gain 2.53, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.67) beats the best remaining Triple Captain opportunity (9.45).
- Autosub: McBurnie replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.19 | 12.66 | 20.46 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Cairns | GK | 13 | 4.0 | 0.15 | 0.32 | 0.45 | 0.00 | 2.4 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.00 | 11.96 | 19.57 | 4.00 | 87.3 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.79 | 11.24 | 18.89 | 1.00 | 86.2 | 90.0 |
| Bench 3 | Bench | De Cuyper | DEF | 5 | 4.7 | 2.77 | 9.99 | 16.56 | 6.00 | 67.5 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.51 | 9.80 | 16.23 | 1.00 | 78.3 | 77.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 2.57 | 7.17 | 12.13 | 2.00 | 72.5 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.67 | 25.00 | 40.62 | 6.00 | 90.0 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 4.12 | 12.80 | 21.72 | 0.00 | 68.4 | 0.0 |
| Bench 2 | Autosub In | McBurnie | FWD | 11 | 5.5 | 3.13 | 8.76 | 14.01 | 1.00 | 69.4 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.51 | 19.05 | 32.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.09 | 16.00 | 25.34 | 2.00 | 82.5 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.17 | 13.14 | 21.58 | 14.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.30 | 12.69 | 21.41 | 2.00 | 76.4 | 80.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.80 | 10.66 | 17.59 | 0.00 | 67.3 | 21.0 |

## GW6

- Train rows: 194240
- Bank: 0.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 72.26
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.17) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Schade (projected gain 5.60, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.17) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.40 | 12.88 | 20.80 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Cairns | GK | 13 | 4.0 | 0.00 | 0.08 | 0.24 | 0.00 | 3.5 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 5.15 | 14.48 | 22.67 | 15.00 | 90.0 | 67.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.38 | 10.90 | 18.23 | 6.00 | 87.5 | 90.0 |
| Bench 3 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 3.07 | 9.69 | 17.32 | 1.00 | 82.6 | 90.0 |
| Bench 2 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.09 | 8.76 | 14.60 | 1.00 | 72.6 | 90.0 |
| XI | XI | O'Shea | DEF | 12 | 4.0 | 3.23 | 8.36 | 13.23 | 11.00 | 79.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.13 | 23.97 | 39.52 | 6.00 | 90.0 | 79.0 |
| Bench 4 | Bench Boost | João Pedro | FWD | 6 | 7.6 | 3.00 | 10.20 | 17.99 | 12.00 | 38.4 | 71.0 |
| XI | XI | McBurnie | FWD | 11 | 5.5 | 3.20 | 8.90 | 14.04 | 1.00 | 71.9 | 90.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 7.04 | 19.33 | 29.56 | 6.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.12 | 18.14 | 30.68 | 1.00 | 89.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.39 | 15.51 | 24.88 | 9.00 | 88.9 | 83.0 |
| XI | XI | Schade | MID | 4 | 6.2 | 5.10 | 14.32 | 22.38 | 1.00 | 90.0 | 51.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.83 | 11.80 | 19.96 | 0.00 | 71.4 | 0.0 |