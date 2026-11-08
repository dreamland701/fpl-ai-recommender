# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 266.99
- Total actual points: 228.00
- Average predicted points: 66.75
- Average actual points: 57.00
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.16
- Actual score: 28.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.45 | 10.46 | 17.17 | 2.00 | 83.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.99 | 9.34 | 15.50 | 1.00 | 92.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.52 | 13.22 | 22.55 | 2.00 | 75.6 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.0 | 4.89 | 12.77 | 19.90 | 0.00 | 77.9 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.27 | 12.56 | 20.07 | 1.00 | 85.3 | 27.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.7 | 4.50 | 12.27 | 19.65 | 7.00 | 81.3 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 3.41 | 12.11 | 20.13 | -3.00 | 98.0 | 52.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.07 | 17.89 | 28.18 | 2.00 | 90.8 | 90.0 |
| Bench 2 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 4 | 7.0 | 3.89 | 11.33 | 17.42 | 2.00 | 74.1 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 3.79 | 9.99 | 17.74 | 2.00 | 61.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.03 | 20.44 | 34.50 | 2.00 | 92.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.64 | 17.69 | 26.94 | 7.00 | 84.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.63 | 15.67 | 26.01 | -1.00 | 80.9 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.6 | 4.47 | 14.23 | 20.56 | 2.00 | 93.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.65 | 13.15 | 20.93 | 2.00 | 87.3 | 82.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 58.16
- Actual score: 79.00
- Transfer: Pedro Porro Sauceda -> Marc Guéhi (projected gain 2.00, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.81 | 10.75 | 17.32 | 6.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.02 | 9.35 | 15.33 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 4.82 | 14.17 | 21.86 | 2.00 | 81.9 | 77.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 4.42 | 13.20 | 21.22 | 3.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.15 | 12.22 | 20.24 | 1.00 | 87.3 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.0 | 4.07 | 11.36 | 17.61 | 11.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.74 | 11.23 | 17.88 | 0.00 | 70.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.15 | 15.99 | 26.86 | 2.00 | 86.4 | 73.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 3.68 | 10.90 | 18.24 | 1.00 | 62.8 | 16.0 |
| Bench 4 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 4 | 7.0 | 3.54 | 10.47 | 16.72 | 2.00 | 72.2 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 6.13 | 18.23 | 29.18 | 18.00 | 90.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.07 | 18.10 | 30.45 | 2.00 | 83.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.16 | 15.03 | 24.97 | 3.00 | 72.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.17 | 12.68 | 19.92 | 3.00 | 74.1 | 75.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.6 | 4.08 | 12.22 | 19.94 | 10.00 | 85.7 | 90.0 |

## GW8

- Train rows: 166350
- Bank: 1.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.84
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.58) beats the best remaining Triple Captain opportunity (9.29).
- Transfer: Trevoh Chalobah -> Gabriel dos Santos Magalhães (projected gain 4.01, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (7.58) beats the best remaining Triple Captain opportunity (9.29).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.74 | 11.17 | 18.14 | 6.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.54 | 9.92 | 15.97 | 9.00 | 91.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.13 | 15.05 | 23.73 | 12.00 | 89.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.96 | 14.93 | 23.52 | 2.00 | 79.1 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.8 | 4.87 | 13.56 | 21.49 | 4.00 | 93.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.09 | 11.35 | 18.54 | 3.00 | 90.2 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | 15 | 5.0 | 3.71 | 11.13 | 17.76 | 2.00 | 85.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.46 | 13.74 | 23.71 | 2.00 | 73.7 | 90.0 |
| Bench 3 | Bench | Francisco Evanilson de Lima Barbosa | FWD | 4 | 7.0 | 3.41 | 9.87 | 16.29 | 0.00 | 70.7 | 0.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 3.21 | 9.47 | 15.86 | 1.00 | 48.7 | 30.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 7.55 | 21.03 | 33.88 | 4.00 | 103.8 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.77 | 17.36 | 29.58 | 2.00 | 79.5 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.47 | 14.85 | 24.75 | 8.00 | 78.1 | 84.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.7 | 4.31 | 12.88 | 21.60 | 1.00 | 86.5 | 45.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.8 | 4.38 | 12.28 | 20.13 | 1.00 | 75.4 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 0.00 -> 2.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Junior Kroupi
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 76.84
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.20) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Francisco Evanilson de Lima Barbosa -> Junior Kroupi (projected gain 2.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.20) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 4.10 | 11.45 | 18.47 | 6.00 | 83.5 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 3.58 | 10.32 | 16.75 | 2.00 | 93.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 6.11 | 16.59 | 26.25 | 9.00 | 92.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 5.17 | 15.12 | 24.04 | 5.00 | 96.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.9 | 4.49 | 14.00 | 22.90 | 4.00 | 92.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.20 | 12.21 | 19.91 | 3.00 | 90.3 | 90.0 |
| Bench 3 | Bench Boost | Dan Burn | DEF | 15 | 5.1 | 3.69 | 11.00 | 18.06 | 2.00 | 77.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.17 | 15.20 | 25.03 | 2.00 | 82.8 | 84.0 |
| Vice Captain | XI | Junior Kroupi | FWD | 4 | 4.5 | 6.50 | 14.76 | 21.99 | 12.00 | 119.9 | 136.0 |
| Bench 4 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.7 | 2.66 | 8.70 | 14.62 | 4.00 | 43.9 | 28.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 6.78 | 20.38 | 33.23 | 3.00 | 96.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.32 | 16.24 | 28.10 | 6.00 | 73.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.62 | 13.41 | 22.31 | 4.00 | 79.6 | 90.0 |
| XI | XI | Moisés Caicedo Corozo | MID | 7 | 5.8 | 3.88 | 12.47 | 20.56 | 2.00 | 66.2 | 90.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.8 | 3.78 | 11.95 | 19.94 | 1.00 | 63.3 | 75.0 |