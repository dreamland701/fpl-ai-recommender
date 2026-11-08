# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 257.98
- Total actual points: 220.00
- Average predicted points: 64.50
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
- Predicted score: 70.10
- Actual score: 52.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.71 | 10.53 | 17.25 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 4.0 | 0.36 | 0.94 | 1.59 | 0.00 | 12.5 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.22 | 17.04 | 26.93 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.43 | 12.14 | 19.43 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.60 | 12.06 | 19.22 | 5.00 | 90.0 | 68.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.06 | 10.25 | 16.27 | 3.00 | 85.3 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.61 | 9.01 | 15.52 | -1.00 | 79.9 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.52 | 17.96 | 29.66 | 9.00 | 90.0 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.53 | 14.39 | 23.54 | 2.00 | 90.0 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.20 | 10.40 | 16.93 | 2.00 | 66.3 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.59 | 22.67 | 38.15 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.75 | 19.62 | 30.63 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.63 | 17.43 | 28.89 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.99 | 16.44 | 25.62 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.54 | 14.56 | 23.99 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.10
- Actual score: 37.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.37, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.04 | 9.59 | 15.87 | 2.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 4.0 | 0.33 | 0.80 | 1.28 | 0.00 | 5.5 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.33 | 13.14 | 20.59 | 6.00 | 76.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.18 | 10.24 | 16.73 | 2.00 | 75.0 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.20 | 8.44 | 13.62 | 1.00 | 71.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.27 | 6.92 | 11.41 | 9.00 | 66.4 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.85 | 5.55 | 9.79 | 0.00 | 9.0 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.37 | 16.68 | 25.53 | 2.00 | 84.2 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.39 | 15.56 | 25.48 | 2.00 | 72.5 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.51 | 7.64 | 12.70 | 2.00 | 46.8 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.12 | 22.52 | 37.64 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.63 | 15.83 | 24.45 | 2.00 | 85.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.87 | 15.74 | 25.69 | 10.00 | 85.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.16 | 15.25 | 23.96 | 2.00 | 87.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.68 | 12.14 | 18.68 | 2.00 | 67.8 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.38
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.46) beats the best remaining Bench Boost opportunity (6.76).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 10.22, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.46) beats the best remaining Bench Boost opportunity (6.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.79 | 11.65 | 18.11 | 6.00 | 88.4 | 90.0 |
| Bench 1 | Bench Boost | Gabriel Słonina | GK | 7 | 4.0 | 0.15 | 1.19 | 1.24 | 0.00 | 5.1 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.86 | 12.16 | 18.78 | 1.00 | 70.4 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.01 | 11.93 | 18.45 | 9.00 | 84.4 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.81 | 7.94 | 12.25 | 6.00 | 72.2 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.21 | 6.96 | 10.83 | 0.00 | 57.4 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.88 | 3.65 | 6.34 | 0.00 | 8.6 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.63 | 17.15 | 26.11 | 7.00 | 79.6 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.13 | 15.44 | 23.96 | 2.00 | 67.2 | 71.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.19 | 7.50 | 11.96 | 0.00 | 48.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.15 | 23.60 | 37.68 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.58 | 17.22 | 25.29 | 13.00 | 82.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.01 | 14.67 | 23.93 | 2.00 | 75.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.10 | 12.63 | 19.51 | 3.00 | 69.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.72 | 11.45 | 17.88 | 3.00 | 74.0 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.41
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.46) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Reinildo Mandava -> Micky van de Ven (projected gain 3.40, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.46) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.37 | 10.61 | 17.08 | 2.00 | 80.9 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 4.0 | 0.00 | 0.68 | 1.12 | 0.00 | 5.4 | 0.0 |
| XI | XI | Micky van de Ven | DEF | 18 | 4.7 | 4.11 | 12.08 | 19.23 | 1.00 | 89.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.12 | 11.81 | 18.46 | 2.00 | 81.5 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.32 | 10.28 | 16.96 | 0.00 | 60.4 | 63.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.52 | 6.91 | 11.09 | 4.00 | 64.6 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.84 | 2.84 | 4.80 | 1.00 | 4.7 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.53 | 16.31 | 26.06 | 2.00 | 79.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.34 | 11.42 | 19.27 | 8.00 | 46.1 | 66.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.55 | 4.91 | 8.34 | 1.00 | 26.9 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.43 | 22.24 | 36.47 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.84 | 17.91 | 27.21 | 5.00 | 83.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.25 | 14.70 | 23.44 | 10.00 | 80.5 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.96 | 11.97 | 19.64 | 7.00 | 74.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.25 | 10.42 | 17.34 | 9.00 | 75.5 | 90.0 |