# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 254.57
- Total actual points: 222.00
- Average predicted points: 63.64
- Average actual points: 55.50
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
- Predicted score: 70.08
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 4.09 | 10.65 | 17.17 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.72 | 1.50 | 2.42 | 0.00 | 10.9 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.23 | 17.15 | 27.19 | 1.00 | 90.0 | 8.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.66 | 12.20 | 19.45 | 5.00 | 90.0 | 68.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.40 | 11.99 | 19.15 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.07 | 10.26 | 16.28 | 3.00 | 88.4 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.72 | 9.38 | 16.19 | -1.00 | 82.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.46 | 19.70 | 32.95 | 2.00 | 79.9 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.62 | 18.28 | 30.22 | 9.00 | 90.0 | 79.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.19 | 10.33 | 16.77 | 2.00 | 67.8 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.65 | 22.85 | 38.44 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.67 | 19.38 | 30.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.95 | 16.27 | 25.31 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.51 | 14.36 | 23.57 | 3.00 | 90.0 | 85.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.82 | 12.71 | 21.23 | 2.00 | 88.7 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.33
- Actual score: 35.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.50 | 4.78 | 8.13 | 0.00 | 35.2 | 90.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.51 | 1.42 | 2.31 | 0.00 | 5.8 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.35 | 13.21 | 20.70 | 6.00 | 76.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.14 | 10.11 | 16.52 | 2.00 | 75.6 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.22 | 8.46 | 13.67 | 1.00 | 74.0 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.35 | 7.22 | 11.96 | 9.00 | 69.2 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.99 | 6.01 | 10.64 | 0.00 | 12.6 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.90 | 21.36 | 34.92 | 9.00 | 84.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.46 | 15.82 | 25.94 | 2.00 | 74.9 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.53 | 7.69 | 12.75 | 2.00 | 48.1 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.16 | 22.66 | 37.90 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.64 | 15.92 | 24.64 | 2.00 | 85.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.10 | 15.01 | 23.51 | 2.00 | 86.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.62 | 11.97 | 18.40 | 2.00 | 69.3 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.06 | 10.46 | 17.12 | 3.00 | 74.8 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.73
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.86) beats the best remaining Bench Boost opportunity (9.68).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 4.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.86) beats the best remaining Bench Boost opportunity (9.68).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 2.19 | 6.99 | 10.53 | 0.00 | 63.5 | 0.0 |
| Bench 1 | Bench Boost | Tom King | GK | 9 | 4.0 | 0.46 | 1.85 | 2.18 | 0.00 | 4.4 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.38 | 12.51 | 18.68 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.86 | 12.18 | 18.73 | 1.00 | 70.6 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.98 | 11.87 | 18.29 | 9.00 | 85.4 | 90.0 |
| Bench 2 | Bench Boost | Reinildo Mandava | DEF | 17 | 4.0 | 2.84 | 8.05 | 12.36 | 6.00 | 74.6 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.33 | 7.42 | 11.57 | 0.00 | 60.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.87 | 21.21 | 34.21 | 13.00 | 80.4 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.19 | 15.68 | 24.28 | 2.00 | 69.3 | 71.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.21 | 7.58 | 12.00 | 0.00 | 50.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.21 | 23.87 | 38.06 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.59 | 17.34 | 25.46 | 13.00 | 81.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.03 | 12.40 | 19.03 | 3.00 | 67.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.65 | 11.26 | 17.46 | 3.00 | 75.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.75 | 10.48 | 16.31 | 1.00 | 75.6 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.44
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.53) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.53) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 1.07 | 3.67 | 6.21 | 0.00 | 29.5 | 0.0 |
| Bench 1 | Bench | Tom King | GK | 9 | 4.0 | 0.21 | 1.24 | 2.06 | 0.00 | 5.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.10 | 11.76 | 18.29 | 2.00 | 82.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 3.97 | 11.41 | 17.35 | 7.00 | 77.8 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.32 | 10.27 | 16.93 | 0.00 | 60.5 | 63.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.32 | 8.76 | 13.43 | -2.00 | 81.1 | 32.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.61 | 7.24 | 11.66 | 4.00 | 67.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.49 | 22.21 | 36.78 | 9.00 | 89.0 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.38 | 11.58 | 19.53 | 8.00 | 48.2 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.55 | 4.90 | 8.25 | 1.00 | 28.1 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.51 | 22.51 | 36.91 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.82 | 17.91 | 27.24 | 5.00 | 82.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.89 | 11.75 | 19.22 | 7.00 | 73.7 | 90.0 |
| Bench 2 | Bench | Tijjani Reijnders | MID | 13 | 5.6 | 3.19 | 10.25 | 17.03 | 9.00 | 76.9 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.56 | 9.46 | 15.13 | 15.00 | 74.6 | 90.0 |