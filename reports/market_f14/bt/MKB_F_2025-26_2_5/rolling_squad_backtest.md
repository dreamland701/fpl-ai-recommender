# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 257.13
- Total actual points: 214.00
- Average predicted points: 64.28
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
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 72.00
- Actual score: 53.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 4.08 | 11.00 | 17.86 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Kjell Scherpen | GK | 6 | 4.0 | 0.43 | 0.55 | 0.94 | 0.00 | 10.1 | 0.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.20 | 16.75 | 26.62 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.74 | 12.52 | 19.93 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 4.60 | 12.29 | 19.64 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.04 | 9.87 | 15.82 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.77 | 9.11 | 15.72 | -1.00 | 84.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.77 | 18.33 | 30.30 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.72 | 14.36 | 23.41 | 2.00 | 90.0 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.18 | 10.00 | 16.41 | 2.00 | 71.3 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.50 | 22.14 | 37.35 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 7.19 | 20.49 | 32.06 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.69 | 17.29 | 28.64 | 0.00 | 90.0 | 0.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.22 | 16.49 | 25.58 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.78 | 14.72 | 24.22 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.00
- Actual score: 32.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.27, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.05 | 9.32 | 15.48 | 2.00 | 80.8 | 90.0 |
| Bench 1 | Bench | Kjell Scherpen | GK | 6 | 4.0 | 0.10 | 0.28 | 0.56 | 0.00 | 6.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.0 | 3.55 | 10.03 | 16.46 | 1.00 | 74.5 | 4.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.02 | 9.78 | 16.06 | 2.00 | 73.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.15 | 8.37 | 13.60 | 1.00 | 72.9 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.32 | 7.16 | 11.81 | 9.00 | 66.5 | 79.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.33 | 6.70 | 11.65 | 0.00 | 21.1 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.45 | 16.53 | 25.26 | 2.00 | 87.5 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.51 | 15.80 | 25.90 | 2.00 | 75.7 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.53 | 7.57 | 12.65 | 2.00 | 49.3 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.92 | 22.05 | 36.94 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.69 | 15.93 | 24.61 | 2.00 | 86.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.80 | 15.62 | 25.48 | 10.00 | 84.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.17 | 15.21 | 23.91 | 2.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.76 | 12.35 | 19.08 | 2.00 | 70.1 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.53
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.80) beats the best remaining Bench Boost opportunity (6.89).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 10.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.80) beats the best remaining Bench Boost opportunity (6.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.93 | 12.08 | 18.20 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Kjell Scherpen | GK | 6 | 4.0 | 0.00 | 1.13 | 0.67 | 0.00 | 4.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.02 | 12.27 | 18.42 | 9.00 | 83.9 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.84 | 8.94 | 13.38 | 0.00 | 69.9 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.74 | 8.22 | 12.23 | 6.00 | 73.4 | 90.0 |
| Bench 2 | Bench Boost | William Saliba | DEF | 1 | 6.0 | 2.33 | 7.45 | 11.91 | 0.00 | 34.6 | 0.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 1.22 | 4.78 | 7.63 | 0.00 | 18.1 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.72 | 17.63 | 26.26 | 7.00 | 82.1 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.25 | 16.01 | 24.34 | 2.00 | 69.6 | 71.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.21 | 7.80 | 11.95 | 0.00 | 51.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.03 | 23.64 | 37.20 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.59 | 17.60 | 25.37 | 13.00 | 83.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.81 | 14.66 | 23.38 | 2.00 | 71.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.04 | 12.79 | 19.25 | 3.00 | 68.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.76 | 11.90 | 18.09 | 3.00 | 75.7 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 63.60
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.29) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 5.36, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.29) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.37 | 10.70 | 16.80 | 2.00 | 81.4 | 90.0 |
| Bench 1 | Bench | Kjell Scherpen | GK | 6 | 4.0 | 0.23 | 0.81 | 0.82 | 0.00 | 5.2 | 0.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.40 | 12.33 | 18.62 | 2.00 | 75.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.05 | 11.68 | 18.14 | 2.00 | 80.8 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.23 | 8.59 | 13.32 | -2.00 | 80.3 | 32.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.56 | 7.11 | 11.37 | 4.00 | 65.1 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 6.0 | 1.60 | 5.52 | 9.48 | 2.00 | 24.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.52 | 16.33 | 26.01 | 2.00 | 80.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.28 | 11.37 | 19.01 | 8.00 | 45.0 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.39 | 4.65 | 7.67 | 1.00 | 26.5 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.26 | 21.91 | 35.74 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.78 | 17.80 | 27.11 | 5.00 | 83.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.05 | 14.23 | 22.78 | 10.00 | 77.2 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.84 | 11.71 | 19.20 | 7.00 | 73.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.29 | 10.64 | 17.65 | 9.00 | 76.3 | 90.0 |