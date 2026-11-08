# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 262.96
- Total actual points: 227.00
- Average predicted points: 65.74
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
- Predicted score: 71.24
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Junior Kroupi replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.23 | 10.76 | 17.41 | 1.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 4.0 | 0.58 | 1.06 | 1.58 | 0.00 | 10.8 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.26 | 17.31 | 27.39 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.40 | 12.08 | 19.24 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.50 | 10.98 | 18.22 | 5.00 | 89.3 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.15 | 10.58 | 16.75 | 3.00 | 88.1 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.67 | 9.28 | 15.91 | -1.00 | 81.9 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.49 | 18.05 | 29.81 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.44 | 14.09 | 22.90 | 2.00 | 88.5 | 87.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.5 | 4.10 | 6.27 | 9.40 | 2.00 | 27.5 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.62 | 22.79 | 38.20 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.64 | 19.59 | 30.70 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.62 | 17.48 | 28.98 | 0.00 | 90.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.90 | 16.71 | 27.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.87 | 16.10 | 24.96 | 6.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 3.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.61
- Actual score: 41.00
- Transfer: Cole Palmer -> Mohammed Kudus (projected gain 10.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.81 | 8.17 | 13.32 | 8.00 | 78.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 4.0 | 0.30 | 0.79 | 1.19 | 0.00 | 8.2 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 5.10 | 14.60 | 23.15 | 4.00 | 90.0 | 70.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.22 | 10.36 | 16.81 | 2.00 | 75.4 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.29 | 8.77 | 14.09 | 1.00 | 74.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.32 | 7.16 | 11.74 | 9.00 | 68.2 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.66 | 5.29 | 9.65 | 0.00 | 5.2 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 6.32 | 16.52 | 25.17 | 2.00 | 82.3 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.42 | 15.74 | 25.74 | 2.00 | 73.9 | 78.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.60 | 5.41 | 8.74 | 2.00 | 24.0 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.14 | 22.66 | 37.76 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.85 | 17.30 | 27.02 | 10.00 | 88.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.48 | 15.53 | 23.93 | 2.00 | 82.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.10 | 15.14 | 23.72 | 2.00 | 85.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.76 | 12.48 | 19.15 | 2.00 | 70.2 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 3.80 -> 3.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.96
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.12) beats the best remaining Bench Boost opportunity (8.58).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 11.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.12) beats the best remaining Bench Boost opportunity (8.58).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.82 | 9.44 | 14.87 | 10.00 | 86.7 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 4.0 | 0.39 | 1.50 | 1.57 | 0.00 | 8.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.03 | 12.00 | 18.47 | 9.00 | 84.9 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.88 | 11.04 | 16.94 | 6.00 | 67.9 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.91 | 8.25 | 12.69 | 6.00 | 75.2 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.29 | 7.24 | 11.23 | 0.00 | 59.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.69 | 3.34 | 6.11 | 0.00 | 4.6 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.61 | 17.07 | 25.80 | 7.00 | 78.7 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.22 | 15.73 | 24.35 | 2.00 | 69.7 | 71.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 3.27 | 6.86 | 9.76 | 0.00 | 36.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.19 | 23.76 | 37.80 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.48 | 17.01 | 24.91 | 13.00 | 79.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.96 | 14.62 | 23.89 | 2.00 | 73.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.16 | 12.77 | 19.60 | 3.00 | 70.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.87 | 11.87 | 18.44 | 3.00 | 77.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 3.70 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.15
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.88) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Reinildo Mandava -> Daniel Muñoz Mejía (projected gain 3.57, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.88) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.16 | 9.53 | 15.61 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 4.0 | 0.46 | 1.17 | 1.73 | 0.00 | 10.6 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.49 | 12.50 | 19.00 | 2.00 | 76.4 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.29 | 12.17 | 19.12 | 1.00 | 82.3 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.18 | 11.90 | 18.55 | 2.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.61 | 7.13 | 11.48 | 4.00 | 67.3 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.76 | 2.85 | 4.91 | 1.00 | 2.2 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.57 | 16.30 | 25.95 | 2.00 | 79.7 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.57 | 11.97 | 20.04 | 8.00 | 51.3 | 66.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.20 | 4.73 | 6.97 | 0.00 | 20.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.51 | 22.43 | 36.68 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.75 | 17.66 | 26.88 | 5.00 | 80.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.20 | 14.60 | 23.39 | 10.00 | 78.8 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.04 | 12.09 | 19.79 | 7.00 | 76.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.39 | 10.78 | 17.92 | 9.00 | 79.2 | 90.0 |