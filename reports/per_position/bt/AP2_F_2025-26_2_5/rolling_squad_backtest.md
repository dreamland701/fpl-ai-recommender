# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 262.93
- Total actual points: 219.00
- Average predicted points: 65.73
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
- Predicted score: 72.43
- Actual score: 59.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Mohammed Kudus replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 5.06 | 12.91 | 21.66 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 4.0 | 0.55 | 0.73 | 1.18 | 0.00 | 13.5 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.28 | 14.85 | 24.33 | 1.00 | 90.0 | 8.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.5 | 5.90 | 14.12 | 20.27 | 13.00 | 63.2 | 63.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 5.37 | 13.19 | 21.19 | 5.00 | 89.8 | 68.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.39 | 9.92 | 16.02 | 3.00 | 87.9 | 90.0 |
| Bench 4 | Bench | Micky van de Ven | DEF | 18 | 4.5 | 3.42 | 9.85 | 15.37 | 6.00 | 81.2 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.50 | 16.07 | 26.16 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.19 | 15.72 | 24.63 | 2.00 | 89.6 | 87.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.57 | 11.03 | 17.22 | 2.00 | 68.6 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.39 | 21.96 | 37.28 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.19 | 18.64 | 28.68 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.69 | 17.62 | 28.82 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.89 | 16.47 | 25.02 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Mohammed Kudus | MID | 18 | 6.5 | 4.43 | 15.12 | 24.73 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.14
- Actual score: 37.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.21, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 2.97 | 10.22 | 17.47 | 2.00 | 79.2 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 4.0 | 0.21 | 0.53 | 0.95 | 0.00 | 9.2 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 5.21 | 13.94 | 21.86 | 6.00 | 75.8 | 90.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.5 | 4.28 | 12.07 | 19.12 | 2.00 | 54.6 | 90.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 4.52 | 11.23 | 17.27 | 1.00 | 81.4 | 90.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 3.11 | 7.88 | 12.76 | 1.00 | 73.5 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.25 | 4.85 | 8.95 | 0.00 | 11.5 | 0.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 3.37 | 15.65 | 25.41 | 2.00 | 74.7 | 78.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 5.51 | 15.42 | 23.87 | 2.00 | 83.3 | 72.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.27 | 8.71 | 14.10 | 2.00 | 48.8 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.59 | 21.06 | 35.47 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.99 | 15.87 | 25.82 | 10.00 | 85.8 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.40 | 15.52 | 23.95 | 2.00 | 84.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.89 | 15.33 | 23.73 | 2.00 | 87.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.83 | 11.67 | 17.82 | 2.00 | 69.8 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 68.11
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (8.18).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 9.25, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (8.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.74 | 14.36 | 23.32 | 6.00 | 88.2 | 90.0 |
| Bench 1 | Bench Boost | Krisztián Hegyi | GK | 19 | 4.0 | 0.21 | 0.85 | 0.81 | 0.00 | 7.5 | 0.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.6 | 4.90 | 14.48 | 20.57 | 5.00 | 68.3 | 67.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.18 | 13.18 | 18.83 | 1.00 | 69.9 | 45.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.5 | 3.58 | 10.47 | 14.21 | 14.00 | 74.3 | 79.0 |
| Bench 2 | Bench Boost | Reinildo Mandava | DEF | 17 | 4.0 | 3.18 | 8.38 | 11.37 | 6.00 | 74.2 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.99 | 4.30 | 6.05 | 0.00 | 10.8 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.39 | 17.52 | 27.84 | 7.00 | 78.6 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 4.41 | 14.61 | 24.09 | 2.00 | 69.5 | 71.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.51 | 8.28 | 14.05 | 0.00 | 50.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.76 | 22.92 | 35.77 | 9.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.68 | 17.17 | 25.16 | 13.00 | 81.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.05 | 14.66 | 24.39 | 2.00 | 75.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.19 | 12.66 | 19.72 | 3.00 | 68.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.60 | 10.96 | 17.50 | 3.00 | 76.1 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.25
- Actual score: 43.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Daniel Ballard -> Jurriën Timber (projected gain 3.88, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.40 | 12.03 | 20.54 | 2.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Krisztián Hegyi | GK | 19 | 4.0 | 0.31 | 0.69 | 1.03 | 0.00 | 8.5 | 0.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 5.7 | 4.56 | 14.74 | 19.56 | 1.00 | 66.2 | 79.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.6 | 4.91 | 13.92 | 18.52 | 1.00 | 88.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.67 | 12.42 | 16.54 | 0.00 | 59.7 | 63.0 |
| XI | XI | Riccardo Calafiori | DEF | 1 | 5.6 | 3.53 | 12.14 | 16.58 | 2.00 | 51.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.74 | 10.15 | 12.38 | -2.00 | 80.7 | 32.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.14 | 15.31 | 28.18 | 2.00 | 78.7 | 90.0 |
| Bench 2 | Bench | Hugo Ekitiké | FWD | 12 | 8.7 | 3.03 | 10.98 | 20.75 | 8.00 | 48.4 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.57 | 4.42 | 9.10 | 1.00 | 28.6 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.97 | 20.73 | 34.45 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.64 | 15.95 | 26.17 | 5.00 | 82.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.92 | 14.05 | 23.70 | 10.00 | 80.2 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.82 | 11.01 | 19.78 | 7.00 | 74.4 | 90.0 |
| Bench 3 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 2.90 | 8.93 | 16.83 | 9.00 | 77.6 | 90.0 |