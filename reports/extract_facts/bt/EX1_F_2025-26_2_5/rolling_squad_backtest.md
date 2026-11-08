# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 263.66
- Total actual points: 210.00
- Average predicted points: 65.92
- Average actual points: 52.50
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
- Predicted score: 71.79
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Junior Kroupi replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.21 | 10.71 | 17.39 | 1.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 4.0 | 0.26 | 1.08 | 2.01 | 0.00 | 11.8 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.25 | 17.28 | 27.37 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.39 | 12.02 | 19.19 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.49 | 10.94 | 18.22 | 5.00 | 89.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.13 | 10.51 | 16.72 | 3.00 | 87.9 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.67 | 9.24 | 15.91 | -1.00 | 82.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.49 | 18.00 | 29.75 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.43 | 14.03 | 22.85 | 2.00 | 88.3 | 87.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.5 | 4.11 | 6.27 | 9.44 | 2.00 | 28.3 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.63 | 22.77 | 38.22 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.22 | 20.29 | 32.99 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.70 | 17.61 | 29.07 | 0.00 | 90.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.88 | 16.08 | 27.84 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.84 | 16.02 | 24.82 | 6.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 2.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.99
- Actual score: 40.00
- Transfer: Cole Palmer -> Matheus Santos Carneiro da Cunha (projected gain 11.06, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.78 | 8.11 | 13.30 | 8.00 | 78.4 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 4.0 | 0.50 | 1.40 | 2.35 | 0.00 | 8.0 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.93 | 14.02 | 22.90 | 4.00 | 90.0 | 70.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.20 | 10.31 | 16.81 | 2.00 | 75.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.28 | 8.70 | 14.06 | 1.00 | 73.6 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.31 | 7.09 | 11.70 | 9.00 | 67.6 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.99 | 6.01 | 10.53 | 0.00 | 12.9 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.76 | 17.32 | 26.56 | 2.00 | 90.0 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.41 | 15.70 | 25.71 | 2.00 | 73.7 | 78.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.61 | 5.42 | 8.79 | 2.00 | 24.4 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.15 | 22.65 | 37.79 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.34 | 18.22 | 32.87 | 10.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.49 | 15.51 | 23.92 | 2.00 | 82.5 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 5.75 | 15.42 | 24.26 | 1.00 | 90.0 | 30.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.74 | 12.42 | 19.14 | 2.00 | 69.7 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 2.30 -> 3.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Jack Grealish
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.05
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.17) beats the best remaining Bench Boost opportunity (7.60).
- Transfer: Matheus Santos Carneiro da Cunha -> Jack Grealish (projected gain 9.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.17) beats the best remaining Bench Boost opportunity (7.60).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.80 | 9.41 | 14.85 | 10.00 | 86.2 | 90.0 |
| Bench 1 | Bench Boost | Antonín Kinský | GK | 18 | 4.0 | 0.37 | 1.89 | 2.39 | 0.00 | 8.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.02 | 11.95 | 18.44 | 9.00 | 84.3 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.85 | 10.97 | 16.88 | 6.00 | 66.8 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.89 | 8.21 | 12.66 | 6.00 | 74.4 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.28 | 7.20 | 11.21 | 0.00 | 59.6 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.01 | 4.07 | 6.97 | 0.00 | 12.0 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.19 | 15.68 | 24.29 | 2.00 | 69.2 | 71.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 7.6 | 2.02 | 9.34 | 15.34 | 1.00 | 37.0 | 59.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.28 | 6.89 | 9.83 | 0.00 | 37.2 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.63 | 24.59 | 39.31 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.47 | 16.98 | 24.86 | 13.00 | 79.3 | 90.0 |
| Vice Captain | XI | Jack Grealish | MID | 9 | 6.8 | 5.73 | 16.70 | 24.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.05 | 14.78 | 23.98 | 2.00 | 75.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.84 | 11.81 | 18.42 | 3.00 | 76.9 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 3.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.84
- Actual score: 54.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.96) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Junior Kroupi -> João Pedro Junqueira de Jesus (projected gain 6.21, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.96) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.14 | 9.49 | 15.59 | 2.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Antonín Kinský | GK | 18 | 4.0 | 0.29 | 1.45 | 2.38 | 0.00 | 9.5 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.26 | 12.15 | 19.08 | 1.00 | 81.5 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.14 | 11.88 | 18.53 | 2.00 | 81.7 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.37 | 8.92 | 13.79 | -2.00 | 80.8 | 32.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.58 | 7.11 | 11.43 | 4.00 | 66.4 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.93 | 3.15 | 5.27 | 1.00 | 7.4 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.95 | 17.11 | 27.41 | 2.00 | 87.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.51 | 11.90 | 20.00 | 8.00 | 50.0 | 66.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 3.85 | 11.63 | 19.47 | 2.00 | 61.0 | 74.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.94 | 23.28 | 38.19 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.17 | 18.52 | 28.36 | 5.00 | 89.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.28 | 14.78 | 23.49 | 10.00 | 80.8 | 86.0 |
| Bench 2 | Bench | Jack Grealish | MID | 9 | 6.8 | 3.19 | 11.18 | 17.01 | 1.00 | 45.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.36 | 10.75 | 17.89 | 9.00 | 78.3 | 90.0 |