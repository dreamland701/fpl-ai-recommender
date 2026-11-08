# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 495.92
- Total actual points: 404.00
- Average predicted points: 70.85
- Average actual points: 57.71
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 0.50
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 86.25
- Actual score: 71.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 5.49 | 16.13 | 26.31 | 3.00 | 102.7 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.5 | 5.09 | 14.88 | 24.65 | 6.00 | 108.6 | 90.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.5 | 7.12 | 20.45 | 33.38 | 1.00 | 110.9 | 8.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.5 | 6.65 | 19.12 | 31.41 | 13.00 | 84.3 | 63.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 6.01 | 17.29 | 28.31 | 6.00 | 104.1 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.5 | 5.60 | 17.15 | 28.19 | 5.00 | 102.2 | 90.0 |
| Bench 2 | Bench | Rico Lewis | DEF | 13 | 5.0 | 5.61 | 16.38 | 26.78 | 1.00 | 82.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.5 | 6.25 | 18.62 | 30.51 | 2.00 | 96.4 | 87.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 6.01 | 17.64 | 28.51 | 15.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Richarlison de Andrade | FWD | 18 | 6.5 | 5.53 | 17.03 | 27.97 | 4.00 | 92.5 | 77.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 9.80 | 25.05 | 39.80 | 5.00 | 110.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 7.35 | 22.26 | 36.25 | 3.00 | 101.9 | 85.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.0 | 7.59 | 21.72 | 35.37 | 6.00 | 104.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 7.17 | 20.79 | 33.83 | 2.00 | 108.6 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 7.04 | 20.60 | 33.14 | 10.00 | 107.1 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 68.11
- Actual score: 40.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: William Saliba -> Jurriën Timber (projected gain 1.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.5 | 4.22 | 13.33 | 21.34 | 2.00 | 91.9 | 90.0 |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 4.46 | 13.27 | 21.33 | 6.00 | 91.3 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.5 | 5.37 | 16.75 | 27.19 | 2.00 | 66.6 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.90 | 14.84 | 23.57 | 4.00 | 86.7 | 70.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.5 | 4.88 | 14.79 | 23.45 | 2.00 | 60.1 | 90.0 |
| Bench 3 | Bench | Rico Lewis | DEF | 13 | 5.0 | 3.41 | 11.17 | 17.43 | 1.00 | 71.3 | 5.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 3.40 | 10.21 | 15.77 | 0.00 | 42.6 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 6.51 | 19.62 | 31.04 | 9.00 | 91.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.23 | 15.62 | 24.11 | 2.00 | 72.8 | 72.0 |
| Bench 2 | Bench | Richarlison de Andrade | FWD | 18 | 6.6 | 4.31 | 13.35 | 20.33 | 2.00 | 69.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.83 | 21.41 | 32.86 | 3.00 | 88.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.1 | 6.01 | 18.72 | 28.59 | 2.00 | 77.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.27 | 16.22 | 24.67 | 2.00 | 75.6 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 5.05 | 16.03 | 24.80 | 3.00 | 83.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.77 | 15.41 | 23.05 | 2.00 | 79.7 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.95
- Actual score: 66.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 1.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 4.27 | 12.77 | 20.88 | 2.00 | 87.8 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.5 | 4.00 | 11.95 | 19.71 | 6.00 | 88.3 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.6 | 4.74 | 14.02 | 22.56 | 5.00 | 68.8 | 67.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.5 | 4.96 | 13.88 | 21.66 | 5.00 | 85.7 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.70 | 13.81 | 21.39 | 6.00 | 76.3 | 90.0 |
| Bench 2 | Bench | Jurriën Timber | DEF | 1 | 5.6 | 4.22 | 12.28 | 19.10 | 8.00 | 57.6 | 90.0 |
| Bench 4 | Bench | Rico Lewis | DEF | 13 | 5.0 | 2.77 | 8.35 | 13.66 | 0.00 | 42.5 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 6.18 | 18.61 | 28.74 | 7.00 | 87.0 | 78.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 7.7 | 4.21 | 13.73 | 21.52 | 1.00 | 63.1 | 59.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.7 | 4.33 | 12.86 | 19.66 | 1.00 | 70.7 | 19.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.09 | 20.91 | 32.39 | 9.00 | 83.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.3 | 5.60 | 16.59 | 25.49 | 13.00 | 69.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.12 | 14.95 | 22.81 | 3.00 | 74.7 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.6 | 5.02 | 14.62 | 22.64 | 3.00 | 74.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.84 | 14.17 | 22.46 | 3.00 | 85.7 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 65.45
- Actual score: 50.00
- League average score: 0.00
- Transfer: Jurriën Timber -> Trevoh Chalobah (projected gain 0.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.19 | 12.56 | 20.22 | 2.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.86 | 11.85 | 19.45 | -3.00 | 85.7 | 4.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.91 | 14.56 | 23.33 | 1.00 | 86.2 | 88.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.82 | 13.92 | 21.62 | 2.00 | 80.6 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.1 | 4.50 | 13.24 | 20.52 | 8.00 | 75.0 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.7 | 4.27 | 13.10 | 21.23 | 2.00 | 60.2 | 90.0 |
| Bench 4 | Bench | Rico Lewis | DEF | 13 | 5.0 | 1.44 | 5.15 | 9.19 | 0.00 | 29.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.19 | 18.11 | 29.40 | 2.00 | 89.2 | 90.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.7 | 3.83 | 11.18 | 19.44 | 2.00 | 56.2 | 74.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.7 | 3.14 | 9.83 | 16.41 | 9.00 | 48.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.24 | 22.13 | 34.42 | 5.00 | 87.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.4 | 6.28 | 17.96 | 28.25 | 5.00 | 75.2 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.7 | 4.92 | 13.91 | 22.38 | 2.00 | 72.1 | 60.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.82 | 13.75 | 22.36 | 7.00 | 75.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.07 | 12.79 | 21.07 | 9.00 | 81.2 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.26
- Actual score: 25.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Rico Lewis -> Dan Burn (projected gain 1.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.11 | 12.21 | 19.93 | 2.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.66 | 8.28 | 14.08 | 1.00 | 51.5 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.7 | 4.61 | 14.10 | 22.14 | 1.00 | 74.7 | 69.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.73 | 13.85 | 22.10 | 1.00 | 89.3 | 27.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.0 | 5.37 | 13.67 | 21.14 | 0.00 | 79.0 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.1 | 3.60 | 12.54 | 20.79 | -3.00 | 97.4 | 52.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.12 | 12.42 | 20.44 | 2.00 | 84.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.19 | 18.27 | 29.20 | 2.00 | 97.0 | 90.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 7.6 | 4.09 | 12.21 | 19.76 | 2.00 | 64.3 | 89.0 |
| XI | XI | Richarlison de Andrade | FWD | 18 | 6.7 | 4.09 | 10.85 | 19.42 | 2.00 | 68.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.45 | 20.84 | 33.80 | 2.00 | 84.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.81 | 18.41 | 28.33 | 7.00 | 84.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.45 | 14.54 | 24.06 | 2.00 | 80.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.89 | 14.10 | 22.40 | 2.00 | 90.4 | 82.0 |
| Bench 3 | Bench | Cody Gakpo | MID | 12 | 7.7 | 3.86 | 11.08 | 20.16 | 1.00 | 61.1 | 45.0 |

## GW7

- Train rows: 165607
- Bank: 0.70 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.22
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.10) beats the best remaining Triple Captain opportunity (8.71).
- League average score: 0.00
- Transfer: Pedro Porro Sauceda -> Gabriel dos Santos Magalhães (projected gain 2.89, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.10) beats the best remaining Triple Captain opportunity (8.71).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.25 | 12.07 | 19.42 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.86 | 8.67 | 14.71 | 2.00 | 68.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 5.08 | 14.43 | 22.17 | 9.00 | 92.6 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.39 | 12.15 | 19.64 | 8.00 | 75.4 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.7 | 4.15 | 11.87 | 19.52 | 6.00 | 62.9 | 74.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.0 | 4.28 | 11.84 | 18.31 | 11.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.94 | 11.57 | 18.29 | 0.00 | 70.1 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.40 | 16.62 | 28.04 | 2.00 | 92.3 | 73.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.5 | 4.00 | 12.04 | 19.94 | 2.00 | 65.0 | 63.0 |
| Bench 3 | Bench | Richarlison de Andrade | FWD | 18 | 6.8 | 3.63 | 10.98 | 18.63 | 1.00 | 64.8 | 16.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.08 | 20.32 | 32.55 | 2.00 | 78.5 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.7 | 6.36 | 19.05 | 30.62 | 18.00 | 90.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.69 | 13.46 | 22.04 | 12.00 | 76.1 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.39 | 13.15 | 20.60 | 3.00 | 77.5 | 75.0 |
| Bench 4 | Bench | Cody Gakpo | MID | 12 | 7.6 | 3.26 | 10.40 | 18.84 | 7.00 | 55.1 | 90.0 |

## GW8

- Train rows: 166350
- Bank: 0.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 77.68
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.87) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Trevoh Chalobah -> Marc Guéhi (projected gain 2.49, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.87) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.26 | 12.62 | 20.46 | 6.00 | 87.1 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.93 | 8.67 | 14.41 | 5.00 | 71.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 5.00 | 14.61 | 22.96 | 12.00 | 89.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.8 | 5.28 | 14.29 | 22.44 | 4.00 | 95.2 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.57 | 12.95 | 20.63 | 10.00 | 82.9 | 90.0 |
| Bench 2 | Bench Boost | Dan Burn | DEF | 15 | 5.0 | 4.00 | 11.91 | 18.96 | 2.00 | 86.1 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.7 | 4.11 | 11.88 | 19.58 | 6.00 | 68.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.92 | 15.15 | 26.05 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 7.4 | 3.47 | 10.37 | 17.44 | 1.00 | 54.2 | 16.0 |
| Bench 4 | Bench Boost | Richarlison de Andrade | FWD | 18 | 6.8 | 3.42 | 10.23 | 17.15 | 1.00 | 51.3 | 30.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 7.06 | 20.52 | 33.23 | 4.00 | 102.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 7.04 | 19.92 | 32.16 | 2.00 | 74.7 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.36 | 15.29 | 24.64 | 2.00 | 87.3 | 90.0 |
| XI | XI | Cody Gakpo | MID | 12 | 7.5 | 4.68 | 13.78 | 22.68 | 7.00 | 75.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.8 | 4.50 | 12.57 | 20.62 | 1.00 | 78.2 | 58.0 |