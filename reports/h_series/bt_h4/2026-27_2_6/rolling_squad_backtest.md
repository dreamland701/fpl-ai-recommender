# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 319.94
- Total actual points: 328.00
- Average predicted points: 63.99
- Average actual points: 65.60
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
- Predicted score: 66.45
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.60 | 12.89 | 20.49 | 6.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.23 | 0.56 | 0.00 | 2.5 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.79 | 15.12 | 24.29 | 1.00 | 75.4 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.55 | 13.60 | 22.28 | 2.00 | 90.3 | 90.0 |
| Bench 2 | Bench | De Cuyper | DEF | 5 | 4.6 | 3.99 | 12.57 | 20.19 | 0.00 | 72.4 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.41 | 11.85 | 18.73 | 9.00 | 86.0 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 3.57 | 10.62 | 17.13 | 0.00 | 88.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.00 | 23.02 | 37.40 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.31 | 16.74 | 26.65 | 9.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 3.24 | 9.99 | 17.43 | 1.00 | 57.4 | 45.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.23 | 18.54 | 30.78 | 23.00 | 89.8 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.12 | 15.99 | 25.63 | 4.00 | 85.1 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.52 | 15.16 | 25.22 | 4.00 | 85.5 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.61 | 14.87 | 24.59 | 5.00 | 83.5 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.31 | 14.47 | 22.44 | 0.00 | 76.8 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 64.05
- Actual score: 56.00
- Transfer: O'Shea -> Ajayi (projected gain 5.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.87 | 11.59 | 19.03 | 3.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.02 | 0.14 | 0.00 | 2.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.15 | 14.74 | 23.56 | 5.00 | 89.4 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.62 | 12.95 | 20.34 | 6.00 | 90.2 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.04 | 12.56 | 19.50 | 4.00 | 82.7 | 76.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.85 | 11.45 | 18.97 | 8.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.24 | 9.55 | 15.35 | 8.00 | 57.0 | 70.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.84 | 24.89 | 39.95 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.43 | 15.64 | 25.55 | 1.00 | 88.0 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.16 | 6.98 | 11.92 | 2.00 | 41.5 | 65.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.42 | 21.29 | 35.72 | 2.00 | 87.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.15 | 15.17 | 24.24 | 3.00 | 90.2 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.93 | 14.73 | 23.52 | 0.00 | 86.4 | 45.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.92 | 14.10 | 23.56 | 6.00 | 78.4 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 58.79
- Actual score: 71.00
- Transfer: M.Sangaré -> Janelt (projected gain 1.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.94 | 12.30 | 19.62 | 14.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.00 | 0.21 | 0.41 | 0.00 | 3.5 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.53 | 11.60 | 19.48 | 1.00 | 84.0 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.57 | 11.42 | 19.06 | 6.00 | 85.7 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.57 | 11.22 | 18.34 | 1.00 | 76.5 | 58.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.50 | 10.70 | 16.99 | 2.00 | 88.2 | 90.0 |
| Bench 2 | Bench | De Cuyper | DEF | 5 | 4.7 | 3.46 | 10.52 | 16.67 | 11.00 | 69.1 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.53 | 22.75 | 37.36 | 9.00 | 89.1 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.58 | 16.91 | 27.08 | 12.00 | 86.4 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 2.58 | 7.39 | 12.31 | 12.00 | 49.0 | 62.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.45 | 19.10 | 29.79 | 8.00 | 89.1 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.12 | 17.61 | 30.07 | 2.00 | 86.3 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.77 | 14.17 | 22.77 | 3.00 | 84.7 | 90.0 |
| XI | XI | Janelt | MID | 4 | 5.0 | 3.69 | 11.60 | 17.94 | 4.00 | 86.1 | 90.0 |
| Bench 3 | Bench | Tzolis | MID | 1 | 6.4 | 2.93 | 10.05 | 16.85 | 3.00 | 65.2 | 80.0 |

## GW5

- Train rows: 193573
- Bank: 0.70 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 66.49
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.38) beats the best remaining Triple Captain opportunity (9.14).
- Transfer: Emersonn -> Calvert-Lewin (projected gain 4.49, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.38) beats the best remaining Triple Captain opportunity (9.14).
- Autosub: Tzolis replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.99 | 12.47 | 20.06 | 1.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.11 | 0.33 | 0.49 | 0.00 | 3.1 | 0.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.78 | 11.95 | 19.53 | 4.00 | 90.3 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.25 | 9.92 | 16.81 | 1.00 | 83.0 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.25 | 9.65 | 15.96 | 1.00 | 82.3 | 77.0 |
| Bench 3 | Bench | De Cuyper | DEF | 5 | 4.7 | 2.40 | 9.53 | 16.27 | 6.00 | 70.6 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.15 | 6.78 | 11.40 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.38 | 24.91 | 40.60 | 6.00 | 89.5 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 4.86 | 13.15 | 20.67 | 2.00 | 82.1 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.61 | 11.81 | 20.61 | 0.00 | 71.2 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.11 | 18.64 | 31.37 | 2.00 | 89.7 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.06 | 16.14 | 25.43 | 2.00 | 85.5 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.97 | 12.76 | 21.26 | 2.00 | 79.7 | 80.0 |
| XI | XI | Janelt | MID | 4 | 5.0 | 3.47 | 10.62 | 16.71 | 3.00 | 81.3 | 90.0 |
| Bench 2 | Autosub In | Tzolis | MID | 1 | 6.4 | 2.58 | 8.82 | 15.10 | 2.00 | 64.9 | 72.0 |

## GW6

- Train rows: 194240
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 64.16
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.15) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Tzolis -> Groß (projected gain 9.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.15) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.10 | 12.63 | 20.10 | 3.00 | 88.3 | 90.0 |
| Bench 1 | Bench Boost | Palmer | GK | 12 | 4.0 | 0.32 | 0.52 | 0.82 | 0.00 | 4.4 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 4.69 | 13.62 | 21.19 | 15.00 | 88.5 | 67.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.05 | 10.63 | 17.85 | 6.00 | 89.9 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.57 | 1.00 | 72.6 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 2.58 | 8.37 | 15.37 | 1.00 | 79.7 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.85 | 6.38 | 12.77 | 3.00 | 42.3 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.68 | 23.34 | 38.31 | 6.00 | 88.1 | 79.0 |
| Bench 2 | Bench Boost | João Pedro | FWD | 6 | 7.6 | 2.54 | 9.36 | 16.96 | 12.00 | 37.5 | 71.0 |
| Bench 3 | Bench Boost | Calvert-Lewin | FWD | 13 | 6.0 | 2.43 | 9.18 | 14.93 | 2.00 | 61.9 | 90.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.9 | 6.45 | 18.26 | 27.89 | 6.00 | 84.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 5.74 | 17.73 | 29.97 | 1.00 | 90.3 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.19 | 15.35 | 24.63 | 9.00 | 89.3 | 83.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.41 | 11.92 | 19.65 | 0.00 | 73.8 | 0.0 |
| XI | XI | Janelt | MID | 4 | 5.0 | 3.38 | 10.74 | 16.98 | 3.00 | 84.0 | 90.0 |