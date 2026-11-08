# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 262.75
- Total actual points: 227.00
- Average predicted points: 65.69
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
- Predicted score: 71.36
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Junior Kroupi replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.23 | 10.77 | 17.42 | 1.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 4.0 | 0.32 | 0.61 | 1.09 | 0.00 | 3.0 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.26 | 17.32 | 27.41 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.40 | 12.08 | 19.24 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.50 | 10.98 | 18.21 | 5.00 | 89.3 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.15 | 10.58 | 16.76 | 3.00 | 88.2 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.67 | 9.28 | 15.91 | -1.00 | 82.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.49 | 18.04 | 29.79 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.44 | 14.08 | 22.89 | 2.00 | 88.5 | 87.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.5 | 4.10 | 6.27 | 9.40 | 2.00 | 27.6 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.62 | 22.79 | 38.19 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.65 | 19.59 | 30.70 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.63 | 17.48 | 28.97 | 0.00 | 90.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.00 | 16.96 | 28.15 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.87 | 16.09 | 24.96 | 6.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 3.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.64
- Actual score: 41.00
- Transfer: Cole Palmer -> Mohammed Kudus (projected gain 10.80, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.81 | 8.17 | 13.33 | 8.00 | 78.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 5.17 | 14.78 | 23.34 | 4.00 | 90.0 | 70.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.22 | 10.36 | 16.82 | 2.00 | 75.5 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.29 | 8.77 | 14.10 | 1.00 | 74.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.32 | 7.16 | 11.74 | 9.00 | 68.2 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.67 | 5.30 | 9.66 | 0.00 | 5.2 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 6.32 | 16.52 | 25.18 | 2.00 | 82.4 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.42 | 15.74 | 25.74 | 2.00 | 73.9 | 78.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.61 | 5.41 | 8.74 | 2.00 | 24.0 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.14 | 22.66 | 37.76 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.80 | 17.06 | 27.01 | 10.00 | 87.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.47 | 15.53 | 23.93 | 2.00 | 82.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 5.09 | 15.14 | 23.72 | 2.00 | 86.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.77 | 12.49 | 19.17 | 2.00 | 70.3 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 3.80 -> 3.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.58
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.74) beats the best remaining Bench Boost opportunity (8.11).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 11.14, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.74) beats the best remaining Bench Boost opportunity (8.11).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.82 | 9.45 | 14.87 | 10.00 | 86.8 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.03 | 12.01 | 18.47 | 9.00 | 84.9 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.89 | 11.05 | 16.95 | 6.00 | 68.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.90 | 8.26 | 12.69 | 6.00 | 75.2 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.29 | 7.25 | 11.23 | 0.00 | 59.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.69 | 3.35 | 6.12 | 0.00 | 4.6 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.61 | 17.08 | 25.81 | 7.00 | 78.7 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.22 | 15.74 | 24.36 | 2.00 | 69.8 | 71.0 |
| Bench 2 | Bench Boost | Junior Kroupi | FWD | 4 | 4.5 | 3.27 | 6.86 | 9.76 | 0.00 | 36.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.19 | 23.76 | 37.81 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.47 | 17.02 | 24.92 | 13.00 | 79.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.96 | 14.63 | 23.89 | 2.00 | 73.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.16 | 12.78 | 19.61 | 3.00 | 70.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.87 | 11.88 | 18.45 | 3.00 | 77.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 3.70 -> 2.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.17
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.89) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Reinildo Mandava -> Daniel Muñoz Mejía (projected gain 3.58, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.89) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.16 | 9.53 | 15.62 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 4.0 | 0.00 | 0.45 | 0.88 | 0.00 | 3.3 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.50 | 12.51 | 19.01 | 2.00 | 76.5 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.29 | 12.17 | 19.12 | 1.00 | 82.3 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.18 | 11.90 | 18.55 | 2.00 | 82.5 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.61 | 7.13 | 11.48 | 4.00 | 67.3 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.76 | 2.86 | 4.92 | 1.00 | 2.2 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.57 | 16.29 | 25.96 | 2.00 | 79.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.57 | 11.97 | 20.05 | 8.00 | 51.3 | 66.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.20 | 4.73 | 6.97 | 0.00 | 20.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.51 | 22.43 | 36.69 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.75 | 17.66 | 26.89 | 5.00 | 81.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.20 | 14.59 | 23.39 | 10.00 | 78.8 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.6 | 4.04 | 12.09 | 19.80 | 7.00 | 76.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.39 | 10.78 | 17.93 | 9.00 | 79.2 | 90.0 |