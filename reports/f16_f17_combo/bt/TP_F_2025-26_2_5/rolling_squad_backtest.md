# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 258.86
- Total actual points: 226.00
- Average predicted points: 64.72
- Average actual points: 56.50
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
- Predicted score: 70.23
- Actual score: 52.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.88 | 11.03 | 18.05 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Kjell Scherpen | GK | 6 | 4.0 | 0.01 | 0.00 | 0.00 | 0.00 | 2.9 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.11 | 16.71 | 26.27 | 1.00 | 90.0 | 8.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.62 | 12.24 | 19.68 | 5.00 | 90.0 | 68.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.48 | 12.15 | 19.31 | 6.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.00 | 10.00 | 15.73 | 3.00 | 81.4 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.57 | 8.91 | 15.28 | -1.00 | 77.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.41 | 17.71 | 29.20 | 9.00 | 86.9 | 79.0 |
| XI | XI | Chris Wood | FWD | 16 | 7.6 | 4.70 | 14.98 | 24.55 | 2.00 | 90.0 | 87.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.19 | 10.38 | 16.80 | 2.00 | 64.8 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.61 | 22.56 | 37.83 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.56 | 19.07 | 29.64 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.56 | 17.15 | 28.46 | 0.00 | 90.0 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.11 | 16.87 | 26.35 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.57 | 14.63 | 24.06 | 3.00 | 90.0 | 85.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Chris Wood
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.47
- Actual score: 37.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.20 | 9.98 | 16.45 | 2.00 | 85.9 | 90.0 |
| Bench 1 | Bench | Kjell Scherpen | GK | 6 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.43 | 13.44 | 21.03 | 6.00 | 80.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.24 | 10.27 | 16.65 | 2.00 | 76.9 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.13 | 8.24 | 13.16 | 1.00 | 67.7 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.24 | 6.86 | 11.23 | 9.00 | 64.7 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.40 | 4.55 | 8.45 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Chris Wood | FWD | 16 | 7.6 | 6.49 | 17.05 | 26.11 | 2.00 | 89.5 | 72.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.32 | 15.37 | 25.10 | 2.00 | 69.4 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.52 | 7.67 | 12.65 | 2.00 | 46.4 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.11 | 22.28 | 37.07 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.72 | 16.18 | 25.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.88 | 15.72 | 25.54 | 10.00 | 86.3 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.20 | 15.31 | 24.00 | 2.00 | 88.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.63 | 11.94 | 18.23 | 2.00 | 64.8 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.40 -> 1.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 65.19
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.88) beats the best remaining Bench Boost opportunity (6.07).
- Transfer: Chris Wood -> João Pedro Junqueira de Jesus (projected gain 10.00, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.88) beats the best remaining Bench Boost opportunity (6.07).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.92 | 12.03 | 18.54 | 6.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Kjell Scherpen | GK | 6 | 4.0 | 0.00 | 0.13 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.97 | 12.47 | 19.08 | 1.00 | 74.6 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.05 | 11.95 | 18.27 | 9.00 | 85.5 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.76 | 7.81 | 11.88 | 6.00 | 69.5 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.18 | 6.95 | 10.68 | 0.00 | 55.7 | 90.0 |
| Bench 4 | Bench Boost | Daniel Ballard | DEF | 17 | 4.6 | 0.46 | 2.72 | 5.08 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.70 | 17.40 | 26.34 | 7.00 | 82.5 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.08 | 15.26 | 23.53 | 2.00 | 64.1 | 71.0 |
| Bench 2 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.20 | 7.54 | 11.88 | 0.00 | 48.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.15 | 23.45 | 37.15 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.67 | 17.60 | 25.78 | 13.00 | 86.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.04 | 14.81 | 23.94 | 2.00 | 76.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.17 | 12.77 | 19.53 | 3.00 | 71.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.68 | 11.25 | 17.37 | 3.00 | 71.1 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.30 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.98
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.47) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Reinildo Mandava -> Marc Guéhi (projected gain 3.42, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.47) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.5 | 3.52 | 10.98 | 17.46 | 2.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Kjell Scherpen | GK | 6 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 0.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.7 | 4.13 | 11.91 | 17.99 | 7.00 | 82.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.16 | 11.81 | 18.26 | 2.00 | 82.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.48 | 10.66 | 17.35 | 0.00 | 66.0 | 63.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.50 | 6.88 | 10.95 | 4.00 | 63.4 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 0.65 | 2.58 | 4.44 | 1.00 | 0.0 | 53.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.59 | 16.45 | 26.12 | 2.00 | 81.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.33 | 11.27 | 18.87 | 8.00 | 44.1 | 66.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.61 | 5.05 | 8.41 | 1.00 | 28.1 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.45 | 22.10 | 35.98 | 5.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.92 | 18.25 | 27.66 | 5.00 | 87.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.28 | 14.73 | 23.36 | 10.00 | 81.7 | 86.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.02 | 12.07 | 19.60 | 7.00 | 76.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.20 | 10.22 | 16.87 | 9.00 | 72.5 | 90.0 |