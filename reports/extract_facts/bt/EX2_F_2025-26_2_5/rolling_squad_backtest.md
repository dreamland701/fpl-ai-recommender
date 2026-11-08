# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 263.28
- Total actual points: 210.00
- Average predicted points: 65.82
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
- Predicted score: 71.72
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Junior Kroupi replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.23 | 10.78 | 17.43 | 1.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 4.0 | 0.58 | 1.06 | 1.58 | 0.00 | 10.6 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.25 | 17.32 | 27.38 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.40 | 12.08 | 19.23 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.51 | 11.00 | 18.25 | 5.00 | 89.3 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 4.15 | 10.59 | 16.77 | 3.00 | 88.1 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.68 | 9.30 | 15.94 | -1.00 | 81.9 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.48 | 18.03 | 29.77 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.44 | 14.07 | 22.86 | 2.00 | 88.3 | 87.0 |
| Bench 2 | Autosub In | Junior Kroupi | FWD | 4 | 4.5 | 4.11 | 6.29 | 9.42 | 2.00 | 27.5 | 4.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.61 | 22.79 | 38.21 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.20 | 20.33 | 33.02 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.61 | 17.47 | 28.98 | 0.00 | 90.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.88 | 16.14 | 27.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.84 | 16.03 | 24.80 | 6.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 2.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.76
- Actual score: 40.00
- Transfer: Cole Palmer -> Matheus Santos Carneiro da Cunha (projected gain 10.85, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.81 | 8.18 | 13.34 | 8.00 | 78.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 4.0 | 0.30 | 0.79 | 1.19 | 0.00 | 8.1 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.95 | 14.08 | 22.95 | 4.00 | 90.0 | 70.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.23 | 10.37 | 16.83 | 2.00 | 75.6 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.30 | 8.78 | 14.11 | 1.00 | 74.2 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.33 | 7.16 | 11.74 | 9.00 | 68.3 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.67 | 5.32 | 9.70 | 0.00 | 5.4 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.74 | 17.32 | 26.54 | 2.00 | 90.0 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.42 | 15.74 | 25.73 | 2.00 | 73.9 | 78.0 |
| Bench 2 | Bench | Junior Kroupi | FWD | 4 | 4.5 | 2.62 | 5.43 | 8.77 | 2.00 | 24.1 | 18.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.15 | 22.67 | 37.78 | 3.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.16 | 17.84 | 32.50 | 10.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.47 | 15.51 | 23.90 | 2.00 | 82.2 | 90.0 |
| XI | XI | Matheus Santos Carneiro da Cunha | MID | 14 | 8.1 | 5.63 | 15.21 | 24.10 | 1.00 | 90.0 | 30.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.77 | 12.48 | 19.16 | 2.00 | 70.3 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 2.30 -> 3.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Jack Grealish
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.87
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.95) beats the best remaining Bench Boost opportunity (7.38).
- Transfer: Matheus Santos Carneiro da Cunha -> Jack Grealish (projected gain 9.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.95) beats the best remaining Bench Boost opportunity (7.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 2.82 | 9.46 | 14.89 | 10.00 | 86.8 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 4.0 | 0.39 | 1.50 | 1.57 | 0.00 | 8.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.04 | 12.00 | 18.48 | 9.00 | 85.0 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 3.89 | 11.05 | 16.95 | 6.00 | 67.9 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.91 | 8.27 | 12.71 | 6.00 | 75.2 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.30 | 7.25 | 11.24 | 0.00 | 59.9 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.70 | 3.37 | 6.16 | 0.00 | 4.7 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.21 | 15.72 | 24.32 | 2.00 | 69.7 | 71.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 7.6 | 2.08 | 9.42 | 15.40 | 1.00 | 38.4 | 59.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.5 | 3.28 | 6.87 | 9.78 | 0.00 | 36.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.60 | 24.55 | 39.27 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.47 | 16.99 | 24.86 | 13.00 | 79.4 | 90.0 |
| Vice Captain | XI | Jack Grealish | MID | 9 | 6.8 | 5.74 | 16.75 | 24.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.96 | 14.61 | 23.88 | 2.00 | 73.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.87 | 11.87 | 18.46 | 3.00 | 77.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 3.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 66.93
- Actual score: 54.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.94) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Junior Kroupi -> João Pedro Junqueira de Jesus (projected gain 6.14, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.94) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.16 | 9.53 | 15.63 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 4.0 | 0.46 | 1.15 | 1.72 | 0.00 | 10.5 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.28 | 12.18 | 19.13 | 1.00 | 82.2 | 88.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.17 | 11.92 | 18.57 | 2.00 | 82.5 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.39 | 8.96 | 13.84 | -2.00 | 81.5 | 32.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.61 | 7.15 | 11.48 | 4.00 | 67.2 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.76 | 2.85 | 4.92 | 1.00 | 2.1 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.96 | 17.11 | 27.40 | 2.00 | 87.8 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.56 | 11.97 | 20.07 | 8.00 | 51.4 | 66.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 3.92 | 11.73 | 19.57 | 2.00 | 62.7 | 74.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.91 | 23.23 | 38.14 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.14 | 18.47 | 28.31 | 5.00 | 89.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.19 | 14.60 | 23.38 | 10.00 | 78.6 | 86.0 |
| Bench 2 | Bench | Jack Grealish | MID | 9 | 6.8 | 3.23 | 11.24 | 17.05 | 1.00 | 46.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.39 | 10.80 | 17.93 | 9.00 | 79.1 | 90.0 |