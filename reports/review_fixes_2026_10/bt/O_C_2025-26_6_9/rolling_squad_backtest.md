# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW5
- Simulated weeks: GW6-GW9
- Total predicted points: 272.78
- Total actual points: 247.00
- Average predicted points: 68.19
- Average actual points: 61.75
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
- Predicted score: 63.19
- Actual score: 29.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.85 | 11.48 | 18.79 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.34 | 10.35 | 17.13 | 1.00 | 98.9 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.0 | 5.27 | 13.49 | 20.98 | 0.00 | 81.7 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.65 | 13.14 | 20.73 | 2.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 4.7 | 4.32 | 13.14 | 20.89 | 7.00 | 93.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.7 | 4.66 | 12.78 | 20.49 | 7.00 | 84.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.19 | 12.74 | 21.84 | 2.00 | 74.8 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.20 | 18.29 | 28.89 | 2.00 | 95.2 | 90.0 |
| Bench 2 | Bench | Viktor Gyökeres | FWD | 1 | 9.0 | 4.36 | 13.12 | 21.98 | 2.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.93 | 9.20 | 14.23 | 2.00 | 80.0 | 79.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.25 | 18.57 | 31.72 | 2.00 | 86.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.69 | 18.18 | 27.72 | 7.00 | 86.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.33 | 15.03 | 25.01 | -1.00 | 77.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.82 | 13.95 | 22.26 | 2.00 | 92.2 | 82.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.03 | 13.50 | 22.12 | 2.00 | 80.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 60.96
- Actual score: 80.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Virgil van Dijk -> Gabriel dos Santos Magalhães (projected gain 2.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.00 | 11.41 | 18.41 | 6.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.36 | 10.37 | 17.01 | 2.00 | 96.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.04 | 14.77 | 22.82 | 2.00 | 84.8 | 77.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.13 | 14.69 | 22.71 | 9.00 | 94.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 4.55 | 13.65 | 21.97 | 3.00 | 93.3 | 90.0 |
| Bench 3 | Bench | Micky van de Ven | DEF | 18 | 4.7 | 4.16 | 12.55 | 20.95 | 2.00 | 87.7 | 90.0 |
| Bench 2 | Bench | Dan Burn | DEF | 15 | 5.0 | 4.26 | 11.93 | 18.55 | 11.00 | 84.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.45 | 16.63 | 27.87 | 2.00 | 89.9 | 73.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 4.44 | 13.08 | 21.59 | 2.00 | 65.4 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.52 | 7.88 | 13.01 | 1.00 | 68.0 | 68.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 6.28 | 18.80 | 30.08 | 18.00 | 93.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.67 | 17.12 | 28.89 | 2.00 | 78.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.22 | 15.07 | 24.92 | 3.00 | 69.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.36 | 13.10 | 20.58 | 3.00 | 76.4 | 75.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.53 | 12.90 | 20.97 | 12.00 | 76.9 | 89.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 68.51
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.98) beats the best remaining Triple Captain opportunity (8.56).
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Dan Burn -> Omar Alderete (projected gain 0.02, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.98) beats the best remaining Triple Captain opportunity (8.56).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 3.96 | 11.85 | 19.24 | 6.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.83 | 10.82 | 17.43 | 9.00 | 97.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.12 | 15.09 | 23.82 | 12.00 | 90.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.74 | 14.64 | 23.27 | 2.00 | 81.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.8 | 5.26 | 14.32 | 22.60 | 4.00 | 97.3 | 90.0 |
| Bench 2 | Bench | Micky van de Ven | DEF | 18 | 4.8 | 4.29 | 12.39 | 20.46 | 0.00 | 91.9 | 90.0 |
| Bench 3 | Bench | Omar Alderete | DEF | 17 | 4.1 | 4.17 | 11.33 | 17.38 | 6.00 | 75.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.72 | 14.59 | 25.09 | 2.00 | 78.4 | 90.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.0 | 4.31 | 13.15 | 21.47 | 2.00 | 68.0 | 90.0 |
| Bench 4 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.61 | 7.34 | 12.71 | 0.00 | 59.1 | 0.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 6.95 | 20.35 | 33.04 | 4.00 | 105.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.51 | 16.70 | 28.47 | 2.00 | 74.3 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.10 | 14.63 | 23.58 | 2.00 | 88.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.50 | 14.45 | 24.09 | 8.00 | 75.9 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.8 | 4.45 | 12.50 | 20.52 | 1.00 | 77.8 | 58.0 |

## GW9

- Train rows: 167095
- Bank: 1.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Junior Kroupi
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 80.12
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.32) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Lyle Foster -> Junior Kroupi (projected gain 3.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.32) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.7 | 4.03 | 11.69 | 18.96 | 6.00 | 86.5 | 90.0 |
| Bench 1 | Bench Boost | Martin Dúbravka | GK | 3 | 4.0 | 4.01 | 11.45 | 18.56 | 2.00 | 100.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 5.45 | 15.75 | 25.18 | 9.00 | 93.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 5.36 | 15.62 | 24.85 | 5.00 | 99.2 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.9 | 4.96 | 15.13 | 24.58 | 4.00 | 96.6 | 90.0 |
| Bench 2 | Bench Boost | Micky van de Ven | DEF | 18 | 4.8 | 4.10 | 12.18 | 19.87 | 23.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Omar Alderete | DEF | 17 | 4.1 | 3.83 | 11.33 | 18.19 | 0.00 | 79.7 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.60 | 16.30 | 26.76 | 2.00 | 89.5 | 84.0 |
| Vice Captain | XI | Junior Kroupi | FWD | 4 | 4.5 | 6.62 | 15.12 | 22.61 | 12.00 | 123.3 | 136.0 |
| XI | XI | Viktor Gyökeres | FWD | 1 | 9.1 | 4.24 | 12.34 | 20.58 | 2.00 | 66.9 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 6.87 | 20.71 | 33.78 | 3.00 | 98.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.4 | 5.07 | 15.68 | 27.10 | 6.00 | 67.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.8 | 4.91 | 14.41 | 22.75 | 3.00 | 81.3 | 77.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.31 | 12.89 | 21.47 | 4.00 | 76.0 | 90.0 |
| Bench 3 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.8 | 3.91 | 12.26 | 20.48 | 1.00 | 65.8 | 75.0 |