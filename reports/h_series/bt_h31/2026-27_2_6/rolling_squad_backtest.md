# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 329.60
- Total actual points: 351.00
- Average predicted points: 65.92
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
- Predicted score: 67.58
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.44 | 12.55 | 20.52 | 6.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.11 | 0.15 | 0.26 | 0.00 | 1.5 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.45 | 14.32 | 22.80 | 1.00 | 71.2 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.63 | 13.66 | 22.21 | 2.00 | 90.5 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.87 | 13.08 | 20.91 | 9.00 | 92.8 | 90.0 |
| Bench 3 | Bench | De Cuyper | DEF | 5 | 4.6 | 3.98 | 12.04 | 19.45 | 0.00 | 70.2 | 90.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 3.71 | 10.98 | 17.90 | 0.00 | 89.5 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.10 | 22.98 | 37.77 | 13.00 | 92.5 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.61 | 17.22 | 28.04 | 9.00 | 92.7 | 90.0 |
| Bench 2 | Bench | McBurnie | FWD | 11 | 5.5 | 4.05 | 10.83 | 17.22 | 1.00 | 77.4 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.55 | 18.86 | 31.41 | 23.00 | 93.2 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.39 | 16.30 | 26.72 | 4.00 | 92.2 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.65 | 15.38 | 25.55 | 4.00 | 88.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.51 | 14.69 | 24.35 | 5.00 | 84.5 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.27 | 14.10 | 22.58 | 0.00 | 75.7 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 65.70
- Actual score: 56.00
- Transfer: Mendy -> Ajayi (projected gain 4.48, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.80 | 11.33 | 18.65 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.00 | 0.00 | 0.07 | 0.00 | 1.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.40 | 15.02 | 24.28 | 5.00 | 91.4 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.85 | 13.38 | 21.36 | 6.00 | 91.9 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.21 | 12.92 | 19.93 | 4.00 | 82.9 | 76.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.96 | 11.46 | 18.82 | 8.00 | 80.1 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.74 | 7.68 | 12.35 | 3.00 | 77.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.03 | 25.25 | 40.81 | 9.00 | 93.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.61 | 15.88 | 26.30 | 1.00 | 91.5 | 90.0 |
| Bench 2 | Bench | McBurnie | FWD | 11 | 5.5 | 3.05 | 8.83 | 14.13 | 2.00 | 71.6 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.79 | 22.01 | 36.97 | 2.00 | 92.3 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.99 | 14.92 | 23.62 | 0.00 | 87.5 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.32 | 14.81 | 24.35 | 3.00 | 91.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.69 | 13.43 | 22.94 | 6.00 | 77.1 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 60.28
- Actual score: 81.00
- Transfer: Tzolis -> Scott (projected gain 4.16, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.07 | 12.49 | 20.04 | 14.00 | 92.1 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.17 | 0.27 | 0.40 | 0.00 | 2.4 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.44 | 11.57 | 18.68 | 1.00 | 81.7 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.61 | 11.05 | 18.29 | 6.00 | 83.8 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.63 | 10.85 | 17.64 | 2.00 | 88.6 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.45 | 10.29 | 16.37 | 11.00 | 65.8 | 90.0 |
| Bench 2 | Bench | O'Shea | DEF | 12 | 4.0 | 2.99 | 8.24 | 13.14 | 1.00 | 78.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.73 | 22.75 | 37.56 | 9.00 | 91.9 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.85 | 17.93 | 28.79 | 12.00 | 92.1 | 90.0 |
| Bench 3 | Bench | McBurnie | FWD | 11 | 5.5 | 2.96 | 8.56 | 13.86 | 4.00 | 72.6 | 81.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.50 | 19.38 | 30.51 | 8.00 | 92.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.19 | 17.32 | 29.97 | 2.00 | 86.5 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.91 | 13.83 | 22.99 | 3.00 | 85.6 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 4.18 | 12.39 | 20.01 | 4.00 | 92.9 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.40 -> 0.80
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 66.60
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (9.23).
- Transfer: Scott -> Groß (projected gain 2.73, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.47) beats the best remaining Triple Captain opportunity (9.23).
- Autosub: McBurnie replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.09 | 12.75 | 20.88 | 1.00 | 92.1 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.01 | 0.18 | 0.38 | 0.00 | 3.5 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.85 | 11.95 | 19.57 | 4.00 | 89.4 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.47 | 10.54 | 18.30 | 1.00 | 86.3 | 90.0 |
| Bench 4 | Bench | De Cuyper | DEF | 5 | 4.7 | 2.49 | 9.72 | 16.18 | 6.00 | 69.3 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.33 | 9.66 | 16.35 | 1.00 | 81.4 | 77.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.56 | 7.16 | 12.12 | 2.00 | 72.5 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.47 | 24.78 | 40.57 | 6.00 | 91.6 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.75 | 12.43 | 21.28 | 0.00 | 70.1 | 0.0 |
| Bench 2 | Autosub In | McBurnie | FWD | 11 | 5.5 | 3.04 | 8.68 | 13.93 | 1.00 | 69.4 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.35 | 18.97 | 32.13 | 2.00 | 92.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 4.91 | 15.89 | 25.59 | 2.00 | 85.4 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 3.99 | 12.96 | 21.26 | 14.00 | 92.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.00 | 12.38 | 21.09 | 2.00 | 78.8 | 80.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.46 | 10.27 | 17.15 | 0.00 | 70.3 | 21.0 |

## GW6

- Train rows: 194240
- Bank: 0.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 69.44
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Schade (projected gain 5.53, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.25 | 12.81 | 20.82 | 3.00 | 91.6 | 90.0 |
| Bench 1 | Bench Boost | Davies | GK | 14 | 4.0 | 0.00 | 0.14 | 0.34 | 0.00 | 4.1 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 4.84 | 13.89 | 22.27 | 15.00 | 90.5 | 67.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.13 | 10.67 | 17.89 | 6.00 | 89.3 | 90.0 |
| Bench 3 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 2.88 | 9.56 | 17.23 | 1.00 | 83.8 | 90.0 |
| Bench 2 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.57 | 1.00 | 72.6 | 90.0 |
| XI | XI | O'Shea | DEF | 12 | 4.0 | 3.24 | 8.37 | 13.23 | 11.00 | 79.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.85 | 23.59 | 39.01 | 6.00 | 91.0 | 79.0 |
| Bench 4 | Bench Boost | João Pedro | FWD | 6 | 7.6 | 2.78 | 9.56 | 16.91 | 12.00 | 37.1 | 71.0 |
| XI | XI | McBurnie | FWD | 11 | 5.5 | 3.12 | 8.82 | 13.96 | 1.00 | 71.9 | 90.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 6.83 | 19.14 | 29.53 | 6.00 | 92.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 5.95 | 17.99 | 30.70 | 1.00 | 93.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.23 | 15.45 | 24.93 | 9.00 | 91.3 | 83.0 |
| XI | XI | Schade | MID | 4 | 6.2 | 4.95 | 14.21 | 22.35 | 1.00 | 92.6 | 51.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.49 | 11.48 | 19.81 | 0.00 | 73.1 | 0.0 |