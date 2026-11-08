# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 258.46
- Total actual points: 220.00
- Average predicted points: 64.61
- Average actual points: 55.00
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
- Predicted score: 70.31
- Actual score: 52.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.83 | 10.89 | 17.93 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 4.0 | 0.34 | 0.96 | 1.67 | 0.00 | 13.1 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.13 | 16.71 | 26.30 | 1.00 | 90.0 | 8.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.68 | 12.33 | 19.72 | 5.00 | 90.0 | 68.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.45 | 12.06 | 19.24 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 3.99 | 9.95 | 15.69 | 3.00 | 81.5 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.56 | 8.87 | 15.27 | -1.00 | 77.6 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.44 | 17.74 | 29.25 | 9.00 | 88.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.66 | 14.89 | 24.48 | 2.00 | 90.0 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.16 | 10.30 | 16.74 | 2.00 | 64.5 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.60 | 22.51 | 37.80 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.63 | 19.15 | 29.74 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.63 | 17.26 | 28.53 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.09 | 16.81 | 26.32 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.55 | 14.58 | 24.02 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.27
- Actual score: 37.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.39, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.14 | 9.83 | 16.31 | 2.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 4.0 | 0.48 | 1.19 | 1.88 | 0.00 | 10.4 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.39 | 13.34 | 20.95 | 6.00 | 79.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.20 | 10.17 | 16.57 | 2.00 | 75.9 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.13 | 8.17 | 13.12 | 1.00 | 67.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.23 | 6.80 | 11.19 | 9.00 | 64.4 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.79 | 5.43 | 9.58 | 0.00 | 6.4 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.46 | 16.96 | 26.05 | 2.00 | 88.9 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.33 | 15.37 | 25.12 | 2.00 | 69.6 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.47 | 7.57 | 12.58 | 2.00 | 45.3 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.11 | 22.22 | 37.04 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.72 | 16.15 | 25.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.88 | 15.65 | 25.50 | 10.00 | 86.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.19 | 15.25 | 23.96 | 2.00 | 88.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.62 | 11.90 | 18.22 | 2.00 | 64.5 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.43
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.44) beats the best remaining Bench Boost opportunity (6.75).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 10.45, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.44) beats the best remaining Bench Boost opportunity (6.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.87 | 11.91 | 18.42 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Sam Proctor | GK | 2 | 4.0 | 0.24 | 1.43 | 1.53 | 0.00 | 9.4 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.92 | 12.35 | 18.96 | 1.00 | 73.2 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.01 | 11.86 | 18.18 | 9.00 | 84.6 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.75 | 7.76 | 11.84 | 6.00 | 69.1 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.17 | 6.88 | 10.62 | 0.00 | 55.5 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.84 | 3.60 | 6.17 | 0.00 | 6.7 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.66 | 17.32 | 26.28 | 7.00 | 81.5 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.07 | 15.25 | 23.53 | 2.00 | 64.0 | 71.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.15 | 7.45 | 11.80 | 0.00 | 47.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.14 | 23.40 | 37.11 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.66 | 17.55 | 25.74 | 13.00 | 86.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.03 | 14.73 | 23.88 | 2.00 | 76.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.13 | 12.66 | 19.43 | 3.00 | 70.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.65 | 11.19 | 17.33 | 3.00 | 70.4 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.45
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.45) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Reinildo Mandava -> Micky van de Ven (projected gain 3.38, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.45) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.45 | 10.86 | 17.33 | 2.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Sam Proctor | GK | 2 | 4.0 | 0.28 | 1.12 | 1.67 | 0.00 | 10.0 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.06 | 11.86 | 18.69 | 1.00 | 86.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.12 | 11.74 | 18.17 | 2.00 | 81.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.38 | 10.49 | 17.15 | 0.00 | 63.3 | 63.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.48 | 6.85 | 10.90 | 4.00 | 62.9 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.82 | 2.85 | 4.76 | 1.00 | 3.9 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.54 | 16.38 | 26.04 | 2.00 | 80.1 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.28 | 11.19 | 18.79 | 8.00 | 42.6 | 66.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.53 | 4.91 | 8.26 | 1.00 | 25.9 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.43 | 22.07 | 35.94 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.91 | 18.24 | 27.64 | 5.00 | 87.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.26 | 14.71 | 23.30 | 10.00 | 81.2 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.98 | 11.99 | 19.50 | 7.00 | 75.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.18 | 10.19 | 16.83 | 9.00 | 71.9 | 90.0 |