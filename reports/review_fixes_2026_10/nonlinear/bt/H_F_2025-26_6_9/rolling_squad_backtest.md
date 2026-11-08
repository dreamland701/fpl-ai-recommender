# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 236.85
- Total actual points: 219.00
- Average predicted points: 59.21
- Average actual points: 54.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW5 are included before the first simulated week.
- League-average scores were not available for this run.

## GW6

- Train rows: 164865
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Mohammed Kudus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.28
- Actual score: 32.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 4.02 | 11.43 | 19.68 | 2.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Alisson Becker | GK | 12 | 5.5 | 3.92 | 11.38 | 17.98 | 2.00 | 85.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 4.60 | 13.19 | 17.32 | 13.00 | 85.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 5.10 | 12.74 | 16.93 | 1.00 | 84.9 | 90.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.8 | 4.30 | 12.59 | 16.12 | 2.00 | 75.3 | 69.0 |
| Bench 2 | Bench | Riccardo Calafiori | DEF | 1 | 5.7 | 3.55 | 12.36 | 17.24 | 1.00 | 77.3 | 69.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.8 | 3.98 | 12.32 | 17.49 | 2.00 | 76.5 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.8 | 5.15 | 13.62 | 18.82 | 2.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.21 | 8.04 | 14.10 | 2.00 | 79.6 | 79.0 |
| Bench 4 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 1.91 | 6.76 | 10.50 | 1.00 | 41.7 | 1.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.61 | 19.48 | 26.06 | -1.00 | 84.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 5.33 | 16.90 | 26.04 | 7.00 | 86.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 5.11 | 16.42 | 29.81 | 2.00 | 77.4 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 5.09 | 14.68 | 19.18 | 1.00 | 84.5 | 90.0 |
| Vice Captain | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.38 | 13.92 | 21.18 | 2.00 | 82.3 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.40 -> 1.20
- Free transfers: 2 -> 2
- Captain: Jurriën Timber
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Jurriën Timber
- Chip used: none
- Predicted score: 53.06
- Actual score: 89.00
- Transfer: Riccardo Calafiori -> Marcos Senesi Barón (projected gain 2.10, hit 0)
- Autosub: Joško Gvardiol replaced Kiernan Dewsbury-Hall.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 4.15 | 11.82 | 18.49 | 3.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Alisson Becker | GK | 12 | 5.5 | 2.52 | 8.62 | 14.33 | 0.00 | 68.3 | 0.0 |
| Captain | Captain | Jurriën Timber | DEF | 1 | 5.8 | 5.35 | 13.25 | 20.24 | 11.00 | 80.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.26 | 12.28 | 16.33 | 2.00 | 88.2 | 77.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.02 | 12.18 | 17.51 | 9.00 | 85.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.26 | 10.98 | 15.21 | 5.00 | 79.7 | 90.0 |
| Bench 2 | Autosub In | Joško Gvardiol | DEF | 13 | 5.8 | 3.20 | 9.30 | 16.16 | 12.00 | 68.0 | 90.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.8 | 3.01 | 11.13 | 16.95 | 1.00 | 74.5 | 16.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.68 | 8.94 | 14.47 | 1.00 | 74.1 | 68.0 |
| Bench 4 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 1.42 | 4.65 | 8.00 | 1.00 | 22.5 | 11.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 4.26 | 15.48 | 26.70 | 2.00 | 77.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.93 | 14.65 | 22.01 | 18.00 | 88.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 3.97 | 13.88 | 23.06 | 12.00 | 84.8 | 89.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.95 | 13.79 | 21.89 | 3.00 | 69.1 | 90.0 |
| XI | Bench | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 3.54 | 10.69 | 15.02 | 0.00 | 70.2 | 0.0 |

## GW8

- Train rows: 166350
- Bank: 1.20 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Mohammed Kudus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 61.72
- Actual score: 49.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.13) beats the best remaining Bench Boost opportunity (6.30).
- Transfer: Lyle Foster -> Dominic Calvert-Lewin (projected gain 5.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.13) beats the best remaining Bench Boost opportunity (6.30).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 2.60 | 10.85 | 17.56 | 2.00 | 87.1 | 90.0 |
| Bench 1 | Bench Boost | Alisson Becker | GK | 12 | 5.4 | 0.77 | 3.13 | 5.30 | 0.00 | 16.8 | 0.0 |
| XI | XI | Joško Gvardiol | DEF | 13 | 5.8 | 3.77 | 12.02 | 18.41 | 0.00 | 74.7 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.8 | 4.47 | 11.57 | 17.67 | 6.00 | 83.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 3.74 | 11.07 | 16.83 | 2.00 | 82.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 2.84 | 10.32 | 16.67 | 3.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 4.49 | 9.51 | 16.40 | 12.00 | 86.6 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.5 | 4.65 | 13.24 | 20.38 | 2.00 | 78.6 | 90.0 |
| Bench 2 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.7 | 1.59 | 6.44 | 11.77 | 1.00 | 39.9 | 30.0 |
| Bench 3 | Bench Boost | Lukas Nmecha | FWD | 11 | 5.0 | 1.41 | 5.62 | 8.76 | 1.00 | 21.9 | 24.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.4 | 7.81 | 18.94 | 33.40 | 2.00 | 84.8 | 84.0 |
| Vice Captain | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.01 | 15.28 | 23.07 | 2.00 | 86.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 4.94 | 14.98 | 22.96 | 4.00 | 86.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.50 | 10.61 | 24.90 | 8.00 | 79.3 | 84.0 |
| Bench 4 | Bench Boost | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 1.33 | 6.75 | 9.97 | 2.00 | 45.8 | 85.0 |

## GW9

- Train rows: 167095
- Bank: 0.70 -> 0.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Marcos Senesi Barón
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 62.79
- Actual score: 49.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.12) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Joško Gvardiol -> Virgil van Dijk (projected gain 2.97, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.12) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 5.5 | 3.62 | 11.26 | 19.20 | 1.00 | 87.7 | 90.0 |
| Bench 1 | Bench | Alisson Becker | GK | 12 | 5.4 | 0.81 | 3.33 | 6.40 | 0.00 | 19.0 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.9 | 4.29 | 13.11 | 20.81 | 6.00 | 80.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 3.79 | 12.24 | 17.31 | 3.00 | 86.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.5 | 4.12 | 12.17 | 18.43 | 1.00 | 86.0 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 5.00 | 12.06 | 17.02 | 5.00 | 84.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 4.89 | 11.58 | 20.67 | 9.00 | 86.0 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.5 | 4.59 | 10.13 | 18.65 | 2.00 | 73.0 | 86.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.6 | 1.80 | 6.27 | 10.20 | 4.00 | 35.4 | 28.0 |
| Bench 3 | Bench | Lukas Nmecha | FWD | 11 | 5.0 | 1.81 | 4.90 | 8.59 | 1.00 | 27.5 | 3.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.3 | 4.95 | 13.95 | 29.86 | 6.00 | 68.9 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 4 | 7.9 | 6.10 | 13.81 | 26.24 | 3.00 | 86.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 4.71 | 13.28 | 24.28 | 4.00 | 87.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.54 | 12.24 | 22.24 | 3.00 | 84.5 | 77.0 |
| Bench 2 | Bench | Kiernan Dewsbury-Hall | MID | 9 | 5.0 | 3.31 | 9.44 | 14.53 | 2.00 | 69.0 | 90.0 |