# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 253.32
- Total actual points: 231.00
- Average predicted points: 63.33
- Average actual points: 57.75
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 69.90
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 4.04 | 10.57 | 17.07 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench | Angus Gunn | GK | 16 | 4.0 | 0.58 | 1.18 | 1.91 | 0.00 | 10.6 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.29 | 17.39 | 27.57 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.41 | 12.06 | 19.25 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.56 | 11.89 | 18.88 | 5.00 | 89.7 | 68.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.12 | 10.47 | 16.65 | 3.00 | 87.8 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.65 | 9.18 | 15.81 | -1.00 | 81.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.23 | 18.93 | 31.56 | 2.00 | 78.2 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.59 | 18.26 | 30.18 | 9.00 | 90.0 | 79.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.26 | 10.58 | 17.22 | 2.00 | 68.5 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.59 | 22.61 | 37.98 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.85 | 20.08 | 31.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.95 | 16.28 | 25.30 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.54 | 14.51 | 23.86 | 3.00 | 90.0 | 85.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.83 | 12.79 | 21.40 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.13
- Actual score: 35.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.42 | 4.52 | 7.72 | 0.00 | 38.2 | 90.0 |
| Bench 1 | Bench | Angus Gunn | GK | 16 | 4.0 | 0.36 | 0.99 | 1.62 | 0.00 | 7.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.32 | 13.07 | 20.43 | 6.00 | 75.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.16 | 10.12 | 16.50 | 2.00 | 74.5 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.26 | 8.59 | 13.89 | 1.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.32 | 7.03 | 11.61 | 9.00 | 68.0 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.03 | 6.64 | 11.90 | 0.00 | 13.7 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.72 | 20.67 | 33.68 | 9.00 | 83.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.45 | 15.76 | 25.83 | 2.00 | 74.7 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.56 | 7.78 | 12.92 | 2.00 | 48.7 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.14 | 22.51 | 37.60 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.59 | 15.72 | 24.27 | 2.00 | 84.7 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.16 | 15.20 | 23.88 | 2.00 | 87.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.72 | 12.26 | 18.89 | 2.00 | 69.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.05 | 10.50 | 17.20 | 3.00 | 76.4 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.22
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.54) beats the best remaining Bench Boost opportunity (9.35).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 4.62, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.54) beats the best remaining Bench Boost opportunity (9.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 2.10 | 6.68 | 10.10 | 0.00 | 66.6 | 0.0 |
| Bench 1 | Bench Boost | Angus Gunn | GK | 16 | 4.0 | 0.01 | 1.21 | 1.36 | 0.00 | 8.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.42 | 12.58 | 18.88 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.84 | 12.02 | 18.50 | 1.00 | 69.7 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.00 | 11.86 | 18.32 | 9.00 | 84.3 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.40 | 8.11 | 13.03 | 0.00 | 62.0 | 90.0 |
| Bench 2 | Bench Boost | Reinildo Mandava | DEF | 17 | 4.0 | 2.86 | 8.08 | 12.47 | 6.00 | 74.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.66 | 20.38 | 32.78 | 13.00 | 79.0 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.19 | 15.62 | 24.26 | 2.00 | 69.4 | 71.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.24 | 7.65 | 12.20 | 0.00 | 50.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.17 | 23.62 | 37.67 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.56 | 17.14 | 25.15 | 13.00 | 81.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.08 | 12.48 | 19.23 | 3.00 | 68.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.77 | 11.56 | 18.05 | 3.00 | 75.9 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.74 | 10.45 | 16.35 | 1.00 | 77.0 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.07
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.47) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.47) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 0.97 | 3.33 | 5.67 | 0.00 | 32.2 | 0.0 |
| Bench 1 | Bench | Angus Gunn | GK | 16 | 4.0 | 0.43 | 1.18 | 1.86 | 0.00 | 9.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.11 | 11.76 | 18.28 | 2.00 | 81.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 3.99 | 11.49 | 17.37 | 7.00 | 76.9 | 90.0 |
| Bench 2 | Bench | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.29 | 10.14 | 16.59 | 0.00 | 59.5 | 63.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.35 | 8.88 | 13.61 | -2.00 | 80.6 | 32.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.56 | 7.08 | 11.28 | 4.00 | 66.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.29 | 21.52 | 35.47 | 9.00 | 87.6 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.39 | 11.52 | 19.37 | 8.00 | 48.0 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.59 | 5.04 | 8.50 | 1.00 | 28.5 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.45 | 22.24 | 36.38 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.81 | 17.86 | 27.03 | 5.00 | 82.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.95 | 11.91 | 19.42 | 7.00 | 74.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.30 | 10.60 | 17.55 | 9.00 | 77.5 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.56 | 9.48 | 15.13 | 15.00 | 75.7 | 90.0 |