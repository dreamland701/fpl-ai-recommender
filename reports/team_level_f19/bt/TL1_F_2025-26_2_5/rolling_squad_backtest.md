# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 253.28
- Total actual points: 219.00
- Average predicted points: 63.32
- Average actual points: 54.75
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
- Predicted score: 68.96
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.79 | 10.81 | 17.28 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.66 | 1.48 | 2.40 | 0.00 | 13.4 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 6.94 | 15.79 | 25.14 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.51 | 12.47 | 19.57 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.35 | 12.19 | 19.19 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 3.81 | 9.01 | 14.45 | 3.00 | 89.4 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.45 | 8.47 | 14.61 | -1.00 | 82.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.47 | 17.78 | 29.57 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.39 | 13.79 | 22.60 | 2.00 | 89.7 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 3.94 | 9.12 | 15.02 | 2.00 | 70.0 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.49 | 22.33 | 37.65 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.62 | 19.55 | 30.22 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.54 | 17.11 | 28.70 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.93 | 16.42 | 25.86 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.44 | 14.40 | 23.31 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.90
- Actual score: 32.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 9.27, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 2.90 | 9.07 | 14.96 | 2.00 | 79.2 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.28 | 0.69 | 1.45 | 0.00 | 9.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.58 | 9.93 | 16.17 | 1.00 | 76.2 | 4.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.05 | 9.73 | 15.84 | 2.00 | 74.9 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.03 | 7.86 | 12.80 | 1.00 | 74.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.26 | 6.87 | 11.46 | 9.00 | 67.7 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.67 | 5.01 | 9.05 | 0.00 | 12.4 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.14 | 16.01 | 24.77 | 2.00 | 83.4 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.49 | 15.97 | 25.94 | 2.00 | 73.9 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.33 | 7.05 | 11.82 | 2.00 | 49.6 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.18 | 22.79 | 37.78 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.72 | 16.32 | 25.03 | 2.00 | 84.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.01 | 16.11 | 26.10 | 10.00 | 85.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.97 | 14.57 | 22.96 | 2.00 | 88.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.66 | 12.12 | 18.86 | 2.00 | 69.6 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.40
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.10) beats the best remaining Bench Boost opportunity (7.36).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 6.80, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.10) beats the best remaining Bench Boost opportunity (7.36).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.67 | 11.24 | 17.60 | 6.00 | 88.0 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 4.0 | 0.26 | 1.15 | 1.38 | 0.00 | 7.5 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.94 | 13.78 | 20.78 | 5.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.90 | 11.53 | 17.97 | 9.00 | 84.4 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.67 | 7.55 | 11.53 | 6.00 | 75.3 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.16 | 6.79 | 10.71 | 0.00 | 59.7 | 90.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 1.76 | 5.65 | 9.84 | 0.00 | 26.3 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.25 | 15.71 | 24.33 | 2.00 | 68.7 | 71.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 7.6 | 2.00 | 9.35 | 15.46 | 1.00 | 34.3 | 59.0 |
| Bench 2 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.04 | 7.10 | 11.22 | 0.00 | 51.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.23 | 23.70 | 37.75 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.57 | 17.18 | 25.38 | 13.00 | 81.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.00 | 14.63 | 23.95 | 2.00 | 75.5 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.94 | 12.14 | 18.94 | 3.00 | 69.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.77 | 11.72 | 18.42 | 3.00 | 75.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.03
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: William Saliba -> Virgil van Dijk (projected gain 4.34, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.44) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.29 | 10.34 | 16.60 | 2.00 | 80.7 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.13 | 0.91 | 1.55 | 0.00 | 8.8 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.47 | 12.27 | 18.76 | 4.00 | 81.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.33 | 12.08 | 18.57 | 2.00 | 76.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.05 | 11.57 | 17.99 | 2.00 | 81.5 | 90.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 3.13 | 8.08 | 12.47 | -2.00 | 81.7 | 32.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.42 | 6.61 | 10.77 | 4.00 | 66.7 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 3.95 | 11.95 | 20.03 | 2.00 | 59.1 | 74.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.37 | 11.61 | 19.59 | 8.00 | 48.0 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.37 | 4.25 | 7.35 | 1.00 | 29.4 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.42 | 22.26 | 36.48 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.82 | 17.86 | 27.22 | 5.00 | 82.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.33 | 15.03 | 23.93 | 10.00 | 80.2 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.83 | 11.54 | 18.97 | 7.00 | 75.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.34 | 10.77 | 17.78 | 9.00 | 77.3 | 90.0 |