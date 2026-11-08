# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 259.48
- Total actual points: 214.00
- Average predicted points: 64.87
- Average actual points: 53.50
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
- Predicted score: 72.61
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.98 | 10.78 | 17.56 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.51 | 0.61 | 1.01 | 0.00 | 12.0 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.36 | 17.21 | 27.28 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.68 | 12.38 | 19.76 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.53 | 12.12 | 19.41 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.26 | 10.50 | 16.70 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.78 | 9.17 | 15.81 | -1.00 | 84.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.83 | 18.49 | 30.51 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.79 | 14.57 | 23.70 | 2.00 | 90.0 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.38 | 10.56 | 17.21 | 2.00 | 70.9 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.68 | 22.59 | 37.98 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.26 | 20.67 | 32.32 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.71 | 17.32 | 28.70 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.26 | 16.65 | 25.84 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.85 | 14.94 | 24.53 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.70
- Actual score: 32.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.10, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.12 | 9.49 | 15.69 | 2.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.28 | 0.55 | 0.95 | 0.00 | 6.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.64 | 10.21 | 16.71 | 1.00 | 74.4 | 4.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.10 | 9.99 | 16.34 | 2.00 | 73.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.23 | 8.57 | 13.87 | 1.00 | 72.8 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.26 | 7.01 | 11.58 | 9.00 | 66.7 | 79.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.38 | 6.84 | 11.85 | 0.00 | 21.0 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.55 | 16.82 | 25.71 | 2.00 | 87.4 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.51 | 15.79 | 25.89 | 2.00 | 75.9 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.58 | 7.74 | 12.88 | 2.00 | 49.2 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.04 | 22.35 | 37.38 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.67 | 15.85 | 24.47 | 2.00 | 86.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.80 | 15.62 | 25.49 | 10.00 | 84.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.29 | 15.54 | 24.38 | 2.00 | 89.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.74 | 12.27 | 18.96 | 2.00 | 70.0 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.00
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.11) beats the best remaining Bench Boost opportunity (7.24).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 10.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.11) beats the best remaining Bench Boost opportunity (7.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.89 | 12.00 | 18.11 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 4.0 | 0.21 | 1.27 | 0.79 | 0.00 | 4.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.99 | 12.22 | 18.38 | 9.00 | 84.0 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.79 | 8.81 | 13.18 | 0.00 | 70.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.81 | 8.42 | 12.50 | 6.00 | 73.2 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 2.29 | 7.36 | 11.81 | 0.00 | 34.7 | 0.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.29 | 4.97 | 7.89 | 0.00 | 17.9 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.77 | 17.76 | 26.46 | 7.00 | 81.9 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.21 | 15.91 | 24.20 | 2.00 | 69.7 | 71.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.28 | 7.98 | 12.20 | 0.00 | 51.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.09 | 23.79 | 37.44 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.64 | 17.71 | 25.52 | 13.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.82 | 14.63 | 23.32 | 2.00 | 71.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.08 | 12.90 | 19.41 | 3.00 | 68.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.76 | 11.88 | 18.07 | 3.00 | 75.6 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.17
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.36) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 5.53, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.36) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.40 | 10.77 | 16.91 | 2.00 | 81.4 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.00 | 0.62 | 0.70 | 0.00 | 5.6 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.42 | 12.41 | 18.72 | 2.00 | 75.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.09 | 11.78 | 18.28 | 2.00 | 80.8 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.32 | 8.84 | 13.68 | -2.00 | 80.0 | 32.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.51 | 7.00 | 11.25 | 4.00 | 65.3 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.0 | 1.63 | 5.60 | 9.61 | 2.00 | 24.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.59 | 16.46 | 26.20 | 2.00 | 80.2 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.25 | 11.30 | 18.96 | 8.00 | 45.2 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.48 | 4.89 | 8.01 | 1.00 | 26.2 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.34 | 22.10 | 36.06 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.83 | 17.90 | 27.28 | 5.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.08 | 14.28 | 22.82 | 10.00 | 77.0 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.91 | 11.86 | 19.44 | 7.00 | 73.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.26 | 10.54 | 17.52 | 9.00 | 76.6 | 90.0 |