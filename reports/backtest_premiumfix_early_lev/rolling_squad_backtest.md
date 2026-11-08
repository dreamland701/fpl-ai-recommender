# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 454.92
- Total actual points: 409.00
- Average predicted points: 64.99
- Average actual points: 58.43
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 78.36
- Actual score: 57.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 5.35 | 15.68 | 25.70 | 3.00 | 102.7 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.5 | 4.95 | 14.43 | 24.04 | 6.00 | 108.6 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.5 | 7.17 | 20.57 | 33.63 | 1.00 | 110.9 | 8.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.5 | 6.51 | 18.66 | 30.81 | 13.00 | 84.3 | 63.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 5.87 | 16.83 | 27.70 | 6.00 | 104.1 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.5 | 5.47 | 16.69 | 27.59 | 5.00 | 102.2 | 90.0 |
| Bench 2 | Bench | Rayan Aït-Nouri | DEF | 13 | 6.0 | 5.65 | 16.46 | 27.10 | 1.00 | 100.9 | 22.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.5 | 5.85 | 17.29 | 28.54 | 9.00 | 80.1 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.5 | 5.67 | 16.84 | 28.01 | 2.00 | 96.4 | 87.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.42 | 15.86 | 26.01 | 15.00 | 81.8 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.61 | 22.55 | 37.30 | 5.00 | 110.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 6.76 | 20.48 | 33.75 | 3.00 | 101.9 | 85.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 7.03 | 20.33 | 33.22 | 2.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.0 | 7.00 | 19.94 | 32.87 | 6.00 | 104.5 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 5.92 | 17.79 | 28.91 | 2.00 | 94.1 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: João Pedro Junqueira de Jesus
- Vice captain: Mohamed Salah
- Effective captain: João Pedro Junqueira de Jesus
- Chip used: none
- Predicted score: 60.59
- Actual score: 45.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: William Saliba -> Jurriën Timber (projected gain 1.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.5 | 4.07 | 12.94 | 20.78 | 2.00 | 91.9 | 90.0 |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 4.32 | 12.87 | 20.77 | 6.00 | 91.3 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.5 | 5.22 | 16.35 | 26.63 | 2.00 | 66.6 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.75 | 14.44 | 23.01 | 4.00 | 86.7 | 70.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.5 | 4.73 | 14.39 | 22.90 | 2.00 | 60.1 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 3.43 | 10.27 | 15.92 | 0.00 | 42.6 | 0.0 |
| Bench 4 | Bench | Rayan Aït-Nouri | DEF | 13 | 6.0 | 3.15 | 10.04 | 15.56 | 0.00 | 47.5 | 90.0 |
| Captain | Captain | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.95 | 18.04 | 29.10 | 9.00 | 91.6 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.68 | 14.03 | 22.17 | 2.00 | 72.8 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.26 | 13.59 | 21.31 | 2.00 | 66.7 | 78.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.94 | 18.91 | 30.36 | 3.00 | 88.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.1 | 5.45 | 17.14 | 26.66 | 2.00 | 77.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.63 | 15.02 | 22.50 | 2.00 | 79.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.72 | 14.64 | 22.73 | 2.00 | 75.6 | 90.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 5.0 | 4.18 | 11.40 | 17.43 | 3.00 | 72.8 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.67
- Actual score: 72.00
- League average score: 0.00
- Transfer: Rayan Aït-Nouri -> Daniel Muñoz Mejía (projected gain 2.95, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 4.13 | 12.43 | 20.33 | 2.00 | 87.8 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 5.5 | 3.86 | 11.61 | 19.16 | 6.00 | 88.3 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.6 | 4.60 | 13.68 | 22.02 | 5.00 | 68.8 | 67.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.5 | 4.82 | 13.54 | 21.12 | 5.00 | 85.7 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.56 | 13.47 | 20.85 | 6.00 | 76.3 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.6 | 4.07 | 11.94 | 18.55 | 8.00 | 57.6 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.27 | 7.14 | 11.88 | 0.00 | 29.8 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.70 | 17.57 | 27.32 | 7.00 | 87.0 | 78.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 7.7 | 3.73 | 12.69 | 20.10 | 1.00 | 63.1 | 59.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 4.06 | 12.26 | 19.39 | 2.00 | 59.6 | 71.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.13 | 18.41 | 29.89 | 9.00 | 83.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.3 | 5.12 | 15.55 | 24.06 | 13.00 | 69.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.64 | 13.91 | 21.38 | 3.00 | 74.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.70 | 13.83 | 21.91 | 3.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Anton Stach | MID | 11 | 5.0 | 3.78 | 10.61 | 16.36 | 1.00 | 72.2 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.53
- Actual score: 42.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Daniel Ballard -> Micky van de Ven (projected gain 2.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.06 | 12.21 | 19.68 | 2.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.74 | 11.50 | 18.91 | -3.00 | 85.7 | 4.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.79 | 14.22 | 22.79 | 1.00 | 86.2 | 88.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 4.45 | 13.63 | 22.17 | 1.00 | 87.1 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.69 | 13.57 | 21.08 | 2.00 | 80.6 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.7 | 4.14 | 12.75 | 20.69 | 2.00 | 60.2 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.7 | 4.26 | 12.03 | 18.96 | 1.00 | 68.2 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.78 | 17.60 | 28.43 | 2.00 | 89.2 | 90.0 |
| Bench 2 | Bench | Hugo Ekitiké | FWD | 12 | 8.8 | 3.59 | 11.28 | 18.20 | 8.00 | 52.4 | 66.0 |
| Bench 4 | Bench | Chris Wood | FWD | 16 | 7.7 | 3.43 | 10.67 | 18.48 | 2.00 | 56.2 | 74.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.56 | 19.63 | 31.92 | 5.00 | 87.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 7.4 | 5.87 | 17.45 | 27.28 | 5.00 | 75.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.41 | 13.24 | 21.39 | 7.00 | 75.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.95 | 12.44 | 20.54 | 9.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.50 | 9.57 | 15.06 | 15.00 | 69.7 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 1.00 -> 2.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.74
- Actual score: 32.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: Jurriën Timber -> Marc Guéhi (projected gain 1.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.96 | 11.79 | 19.33 | 2.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.51 | 7.87 | 13.48 | 1.00 | 51.5 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.7 | 4.46 | 13.69 | 21.54 | 1.00 | 74.7 | 69.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.82 | 13.64 | 21.57 | 2.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.58 | 13.44 | 21.50 | 1.00 | 89.3 | 27.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 4.38 | 13.27 | 21.07 | 7.00 | 90.4 | 90.0 |
| Bench 2 | Bench | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 3.97 | 12.01 | 19.84 | 2.00 | 84.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.06 | 17.97 | 28.45 | 2.00 | 97.0 | 90.0 |
| Bench 3 | Bench | Chris Wood | FWD | 16 | 7.6 | 3.95 | 11.92 | 19.00 | 2.00 | 64.3 | 89.0 |
| Bench 4 | Bench | Hugo Ekitiké | FWD | 12 | 8.8 | 3.70 | 11.73 | 18.47 | 0.00 | 60.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.19 | 18.34 | 31.30 | 2.00 | 84.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.68 | 18.12 | 27.58 | 7.00 | 84.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.31 | 14.25 | 23.31 | 2.00 | 80.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.74 | 13.69 | 21.80 | 2.00 | 90.4 | 82.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.37 | 11.69 | 17.64 | 2.00 | 78.7 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 2.00 -> 1.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 64.58
- Actual score: 103.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.29) beats the best remaining Triple Captain opportunity (7.42).
- League average score: 0.00
- Transfer: Riccardo Calafiori -> Gabriel dos Santos Magalhães (projected gain 2.56, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.29) beats the best remaining Triple Captain opportunity (7.42).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.08 | 11.62 | 18.76 | 6.00 | 84.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.76 | 8.41 | 14.34 | 2.00 | 68.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.1 | 4.91 | 13.99 | 21.50 | 9.00 | 92.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.7 | 4.48 | 13.35 | 21.40 | 3.00 | 89.5 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.18 | 12.55 | 20.94 | 2.00 | 86.4 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.21 | 11.70 | 18.98 | 8.00 | 75.4 | 90.0 |
| Bench 2 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.6 | 3.58 | 10.72 | 18.46 | 7.00 | 59.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.30 | 16.22 | 27.20 | 2.00 | 92.3 | 73.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.5 | 3.90 | 11.64 | 19.09 | 2.00 | 65.0 | 63.0 |
| Bench 4 | Bench | Hugo Ekitiké | FWD | 12 | 8.7 | 1.87 | 6.53 | 11.82 | 1.00 | 22.1 | 16.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 6.26 | 18.66 | 29.77 | 18.00 | 90.2 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.92 | 17.82 | 30.05 | 2.00 | 78.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 4.59 | 13.06 | 21.20 | 12.00 | 76.1 | 89.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.22 | 12.70 | 19.93 | 3.00 | 77.5 | 75.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.26 | 9.46 | 14.38 | 2.00 | 73.2 | 66.0 |

## GW8

- Train rows: 166350
- Bank: 1.60 -> 2.30
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 72.44
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.68) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Pedro Porro Sauceda -> Marcos Senesi Barón (projected gain 1.70, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.68) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.6 | 4.08 | 12.18 | 19.77 | 6.00 | 87.1 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.82 | 8.36 | 13.96 | 5.00 | 71.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.2 | 4.82 | 14.18 | 22.28 | 12.00 | 89.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 4.8 | 5.16 | 13.97 | 21.98 | 4.00 | 95.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.42 | 13.66 | 21.63 | 2.00 | 79.7 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.39 | 12.51 | 19.94 | 10.00 | 82.9 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.8 | 4.23 | 12.23 | 20.19 | 0.00 | 90.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.73 | 14.60 | 25.11 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 7.4 | 3.27 | 9.82 | 16.50 | 1.00 | 54.2 | 16.0 |
| Bench 4 | Bench Boost | Hugo Ekitiké | FWD | 12 | 8.7 | 2.56 | 7.90 | 13.65 | 1.00 | 33.2 | 28.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 6.87 | 19.97 | 32.30 | 4.00 | 102.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.76 | 17.42 | 29.66 | 2.00 | 74.7 | 84.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.7 | 5.16 | 14.74 | 23.71 | 2.00 | 87.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.8 | 4.32 | 12.13 | 19.93 | 1.00 | 78.2 | 58.0 |
| Bench 3 | Bench Boost | Anton Stach | MID | 11 | 5.0 | 2.98 | 8.21 | 13.01 | 2.00 | 66.9 | 72.0 |