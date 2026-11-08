# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 333.48
- Total actual points: 325.00
- Average predicted points: 66.70
- Average actual points: 65.00
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
- Predicted score: 68.97
- Actual score: 98.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.65 | 13.00 | 20.48 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.11 | 0.15 | 0.26 | 0.00 | 1.6 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.77 | 14.91 | 23.49 | 1.00 | 73.0 | 58.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.89 | 13.60 | 21.64 | 11.00 | 89.4 | 90.0 |
| Bench 3 | Bench | Guéhi | DEF | 15 | 6.0 | 4.61 | 13.59 | 21.98 | 2.00 | 89.2 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.77 | 12.81 | 20.06 | 9.00 | 91.5 | 90.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.0 | 4.63 | 11.43 | 18.69 | 6.00 | 62.8 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.18 | 22.87 | 37.24 | 13.00 | 89.2 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.69 | 17.17 | 27.58 | 9.00 | 90.5 | 90.0 |
| Bench 4 | Bench | Walle Egeli | FWD | 12 | 4.5 | 0.80 | 2.93 | 5.09 | 0.00 | 14.5 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.51 | 18.90 | 31.38 | 23.00 | 91.6 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.51 | 16.57 | 26.52 | 4.00 | 89.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.71 | 15.42 | 25.75 | 4.00 | 86.2 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.71 | 14.85 | 24.34 | 5.00 | 83.3 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.39 | 14.47 | 22.51 | 0.00 | 73.7 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 1.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 66.81
- Actual score: 50.00
- Transfer: Guéhi -> De Cuyper (projected gain 1.16, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.97 | 11.46 | 18.68 | 3.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.00 | 0.00 | 0.07 | 0.00 | 1.0 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.73 | 13.79 | 21.49 | 2.00 | 88.4 | 66.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 5.01 | 13.36 | 20.54 | 5.00 | 88.4 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.86 | 13.24 | 20.72 | 6.00 | 91.1 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 4.22 | 12.84 | 19.41 | 4.00 | 81.7 | 76.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.18 | 8.82 | 14.66 | 8.00 | 57.3 | 70.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.08 | 25.02 | 40.29 | 9.00 | 88.9 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.67 | 15.75 | 25.93 | 1.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Walle Egeli | FWD | 12 | 4.5 | 0.41 | 1.52 | 2.57 | 0.00 | 7.1 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.83 | 22.12 | 36.88 | 2.00 | 91.7 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.05 | 14.97 | 23.66 | 0.00 | 85.3 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.31 | 14.93 | 23.76 | 3.00 | 88.9 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.01 | 13.98 | 23.20 | 6.00 | 77.3 | 86.0 |
| Bench 3 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.2 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 1.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 62.75
- Actual score: 80.00
- Transfer: Tzolis -> Ødegaard (projected gain 4.67, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.29 | 12.84 | 20.53 | 14.00 | 90.4 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.17 | 0.27 | 0.40 | 0.00 | 2.4 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.63 | 13.82 | 21.82 | 6.00 | 78.4 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.69 | 11.09 | 17.27 | 1.00 | 73.1 | 58.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.61 | 10.85 | 17.42 | 2.00 | 86.7 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.54 | 10.67 | 16.65 | 11.00 | 65.2 | 90.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.1 | 3.29 | 9.82 | 15.18 | 1.00 | 72.7 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.81 | 23.02 | 37.31 | 9.00 | 88.3 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.86 | 18.03 | 28.16 | 12.00 | 88.3 | 90.0 |
| Bench 4 | Bench | Walle Egeli | FWD | 12 | 4.5 | 0.21 | 1.00 | 1.76 | 0.00 | 4.1 | 0.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.68 | 19.74 | 30.18 | 8.00 | 91.3 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.25 | 17.57 | 30.34 | 2.00 | 84.8 | 90.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 4.77 | 14.45 | 23.29 | 3.00 | 80.4 | 84.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.82 | 13.99 | 22.56 | 3.00 | 82.8 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 1.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 68.68
- Actual score: 34.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (9.48).
- Transfer: De Cuyper -> Gvardiol (projected gain 3.93, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.70) beats the best remaining Triple Captain opportunity (9.48).
- Autosub: Ajayi replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.20 | 12.89 | 20.52 | 1.00 | 90.6 | 90.0 |
| Bench 1 | Bench | Davies | GK | 14 | 4.0 | 0.01 | 0.18 | 0.38 | 0.00 | 3.5 | 0.0 |
| XI | XI | Gvardiol | DEF | 15 | 5.7 | 4.42 | 12.88 | 20.47 | 4.00 | 91.5 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.15 | 12.85 | 20.69 | 1.00 | 81.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.37 | 9.49 | 15.99 | 1.00 | 80.1 | 77.0 |
| Bench 2 | Autosub In | Ajayi | DEF | 11 | 4.1 | 3.25 | 9.03 | 14.68 | 1.00 | 76.2 | 90.0 |
| Bench 3 | Bench | Mendy | DEF | 11 | 4.0 | 2.15 | 6.78 | 11.40 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.70 | 24.82 | 40.52 | 6.00 | 89.0 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.77 | 12.12 | 20.75 | 0.00 | 67.9 | 0.0 |
| Bench 4 | Bench | Walle Egeli | FWD | 12 | 4.5 | 0.28 | 0.91 | 1.51 | 0.00 | 3.4 | 0.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.40 | 19.03 | 31.86 | 2.00 | 91.4 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.17 | 16.10 | 25.40 | 2.00 | 85.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.12 | 12.76 | 21.32 | 2.00 | 77.1 | 80.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.40 | 11.52 | 19.11 | 2.00 | 60.8 | 72.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.58 | 10.38 | 17.36 | 0.00 | 68.4 | 21.0 |

## GW6

- Train rows: 194240
- Bank: 0.30 -> -0.00
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 66.28
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Groß (projected gain 11.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.47 | 13.10 | 21.29 | 3.00 | 90.4 | 90.0 |
| Bench 1 | Bench Boost | Davies | GK | 14 | 4.0 | 0.00 | 0.14 | 0.34 | 0.00 | 4.2 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.71 | 13.45 | 21.55 | 9.00 | 87.7 | 81.0 |
| XI | XI | Gvardiol | DEF | 15 | 5.7 | 3.44 | 11.17 | 18.67 | 4.00 | 86.4 | 24.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.56 | 1.00 | 72.6 | 90.0 |
| Bench 2 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 2.68 | 7.79 | 12.75 | 1.00 | 72.3 | 90.0 |
| Bench 3 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.96 | 6.56 | 12.77 | 3.00 | 41.2 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.07 | 23.68 | 38.87 | 6.00 | 88.2 | 79.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 3.58 | 11.79 | 21.80 | 12.00 | 52.7 | 71.0 |
| Bench 4 | Bench Boost | Walle Egeli | FWD | 12 | 4.5 | 0.43 | 0.94 | 1.60 | 1.00 | 4.0 | 9.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.9 | 7.06 | 19.20 | 29.33 | 6.00 | 91.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 5.99 | 17.78 | 30.39 | 1.00 | 90.2 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.52 | 15.95 | 25.14 | 9.00 | 90.8 | 83.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.63 | 11.67 | 19.78 | 0.00 | 71.0 | 0.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.61 | 11.52 | 19.56 | 1.00 | 65.4 | 89.0 |