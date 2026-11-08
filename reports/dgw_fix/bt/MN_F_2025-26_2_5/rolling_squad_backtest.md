# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 263.08
- Total actual points: 211.00
- Average predicted points: 65.77
- Average actual points: 52.75
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
- Captain: Tijjani Reijnders
- Vice captain: Antoine Semenyo
- Effective captain: Tijjani Reijnders
- Chip used: none
- Predicted score: 74.72
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.14 | 10.78 | 17.56 | 6.00 | 112.3 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.49 | 0.61 | 1.01 | 0.00 | 12.0 | 0.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.26 | 17.21 | 27.28 | 1.00 | 100.2 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.83 | 12.38 | 19.76 | 6.00 | 112.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.72 | 12.12 | 19.41 | 6.00 | 115.3 | 90.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.27 | 10.50 | 16.70 | 3.00 | 89.3 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.76 | 9.17 | 15.81 | -1.00 | 84.1 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 6.23 | 18.49 | 30.51 | 9.00 | 105.4 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.15 | 14.57 | 23.70 | 2.00 | 103.7 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.29 | 10.56 | 17.21 | 2.00 | 69.0 | 62.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 7.50 | 22.59 | 37.98 | 5.00 | 116.6 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 7.92 | 20.67 | 32.32 | 2.00 | 153.8 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.33 | 17.32 | 28.70 | 0.00 | 95.4 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.70 | 16.65 | 25.84 | 6.00 | 130.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.03 | 14.94 | 24.53 | 3.00 | 105.6 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.06
- Actual score: 32.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.12, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.07 | 9.49 | 15.69 | 2.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.30 | 0.55 | 0.95 | 0.00 | 6.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.62 | 10.21 | 16.71 | 1.00 | 73.9 | 4.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.06 | 9.99 | 16.34 | 2.00 | 72.3 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.21 | 8.57 | 13.87 | 1.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.21 | 7.01 | 11.58 | 9.00 | 65.3 | 79.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.23 | 6.84 | 11.85 | 0.00 | 17.4 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.92 | 16.82 | 25.71 | 2.00 | 92.9 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.77 | 15.79 | 25.89 | 2.00 | 80.2 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.54 | 7.74 | 12.88 | 2.00 | 48.6 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.97 | 22.35 | 37.38 | 3.00 | 106.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.18 | 15.85 | 24.47 | 2.00 | 94.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.89 | 15.62 | 25.49 | 10.00 | 85.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.59 | 15.54 | 24.38 | 2.00 | 95.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 12.27 | 18.96 | 2.00 | 69.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.40
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.88) beats the best remaining Bench Boost opportunity (6.98).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 9.89, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.88) beats the best remaining Bench Boost opportunity (6.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.97 | 12.00 | 18.11 | 6.00 | 92.1 | 90.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 4.0 | 0.22 | 1.27 | 0.79 | 0.00 | 4.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.05 | 12.22 | 18.38 | 9.00 | 85.2 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.77 | 8.81 | 13.18 | 0.00 | 69.1 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.81 | 8.42 | 12.50 | 6.00 | 72.9 | 90.0 |
| Bench 3 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 2.12 | 7.36 | 11.81 | 0.00 | 31.9 | 0.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.25 | 4.97 | 7.89 | 0.00 | 17.2 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.94 | 17.76 | 26.46 | 7.00 | 85.8 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.34 | 15.91 | 24.20 | 2.00 | 71.7 | 71.0 |
| Bench 2 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.26 | 7.98 | 12.20 | 0.00 | 51.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.04 | 23.79 | 37.44 | 9.00 | 104.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 6.13 | 17.71 | 25.52 | 13.00 | 90.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.77 | 14.63 | 23.32 | 2.00 | 70.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.02 | 12.90 | 19.41 | 3.00 | 66.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.66 | 11.88 | 18.07 | 3.00 | 73.5 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.90
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 5.53, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.29) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.39 | 10.77 | 16.91 | 2.00 | 81.6 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.00 | 0.62 | 0.70 | 0.00 | 5.8 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.41 | 12.41 | 18.72 | 2.00 | 73.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.09 | 11.78 | 18.28 | 2.00 | 81.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.29 | 8.84 | 13.68 | -2.00 | 78.8 | 32.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.46 | 7.00 | 11.25 | 4.00 | 63.7 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.0 | 1.60 | 5.60 | 9.61 | 2.00 | 23.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.55 | 16.46 | 26.20 | 2.00 | 80.9 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.07 | 11.30 | 18.96 | 8.00 | 42.1 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.46 | 4.89 | 8.01 | 1.00 | 26.4 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.26 | 22.10 | 36.06 | 5.00 | 99.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.25 | 17.90 | 27.28 | 5.00 | 88.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.00 | 14.28 | 22.82 | 10.00 | 75.7 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.87 | 11.86 | 19.44 | 7.00 | 72.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.19 | 10.54 | 17.52 | 9.00 | 74.9 | 90.0 |