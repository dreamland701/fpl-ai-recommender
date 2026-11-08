# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 262.91
- Total actual points: 227.00
- Average predicted points: 65.73
- Average actual points: 56.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 71.31
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Junior Kroupi replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.21 | 10.69 | 17.37 | 1.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 4.0 | 0.47 | 0.84 | 1.37 | 0.00 | 8.3 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.26 | 17.27 | 27.38 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.38 | 12.01 | 19.20 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.48 | 10.92 | 18.18 | 5.00 | 89.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.12 | 10.50 | 16.70 | 3.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.66 | 9.22 | 15.88 | -1.00 | 82.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.50 | 18.03 | 29.79 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.44 | 14.06 | 22.89 | 2.00 | 88.5 | 87.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.5 | 4.09 | 6.25 | 9.42 | 2.00 | 28.2 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.63 | 22.77 | 38.21 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.67 | 19.58 | 30.70 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.71 | 17.62 | 29.07 | 0.00 | 90.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.90 | 16.65 | 27.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.88 | 16.08 | 24.98 | 6.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 3.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.62
- Actual score: 41.00
- Transfer: Cole Palmer -> Mohammed Kudus (projected gain 10.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.78 | 8.09 | 13.28 | 8.00 | 78.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 4.0 | 0.19 | 0.58 | 0.98 | 0.00 | 5.4 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 5.09 | 14.55 | 23.12 | 4.00 | 90.0 | 70.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.19 | 10.30 | 16.78 | 2.00 | 74.8 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.27 | 8.69 | 14.04 | 1.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.30 | 7.09 | 11.69 | 9.00 | 67.5 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.99 | 5.98 | 10.49 | 0.00 | 12.7 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 6.31 | 16.47 | 25.16 | 2.00 | 82.2 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.41 | 15.70 | 25.72 | 2.00 | 73.7 | 78.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.59 | 5.39 | 8.77 | 2.00 | 24.2 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.15 | 22.64 | 37.77 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.97 | 17.52 | 27.23 | 10.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.49 | 15.52 | 23.95 | 2.00 | 82.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.09 | 15.10 | 23.70 | 2.00 | 85.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.74 | 12.41 | 19.12 | 2.00 | 69.6 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 3.80 -> 3.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.00
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.30) beats the best remaining Bench Boost opportunity (8.77).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 11.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.30) beats the best remaining Bench Boost opportunity (8.77).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.79 | 9.38 | 14.82 | 10.00 | 86.1 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 4.0 | 0.28 | 1.30 | 1.36 | 0.00 | 5.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.00 | 11.94 | 18.43 | 9.00 | 84.2 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.85 | 10.96 | 16.88 | 6.00 | 66.9 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.88 | 8.19 | 12.64 | 6.00 | 74.4 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.27 | 7.19 | 11.19 | 0.00 | 59.5 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.00 | 4.04 | 6.93 | 0.00 | 11.9 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.59 | 17.02 | 25.78 | 7.00 | 77.9 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.20 | 15.69 | 24.33 | 2.00 | 69.3 | 71.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 3.26 | 6.87 | 9.81 | 0.00 | 37.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.19 | 23.74 | 37.81 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.47 | 17.00 | 24.91 | 13.00 | 79.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.06 | 14.79 | 24.00 | 2.00 | 76.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.13 | 12.71 | 19.56 | 3.00 | 69.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.83 | 11.80 | 18.40 | 3.00 | 76.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 3.70 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.97
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.88) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Reinildo Mandava -> Daniel Muñoz Mejía (projected gain 3.57, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.88) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.13 | 9.48 | 15.57 | 2.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 4.0 | 0.36 | 0.99 | 1.52 | 0.00 | 7.7 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.47 | 12.47 | 18.96 | 2.00 | 75.8 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.26 | 12.13 | 19.07 | 1.00 | 81.6 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.14 | 11.86 | 18.50 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.57 | 7.08 | 11.43 | 4.00 | 66.5 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.93 | 3.14 | 5.26 | 1.00 | 7.5 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.53 | 16.25 | 25.92 | 2.00 | 78.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.51 | 11.89 | 19.97 | 8.00 | 49.9 | 66.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.27 | 4.82 | 7.10 | 0.00 | 22.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.51 | 22.43 | 36.69 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.75 | 17.66 | 26.89 | 5.00 | 80.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.29 | 14.78 | 23.50 | 10.00 | 81.1 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.01 | 12.05 | 19.76 | 7.00 | 75.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.36 | 10.73 | 17.87 | 9.00 | 78.3 | 90.0 |