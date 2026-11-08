# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 254.33
- Total actual points: 223.00
- Average predicted points: 63.58
- Average actual points: 55.75
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
- Predicted score: 70.28
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 4.05 | 10.60 | 17.14 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 4.0 | 0.38 | 1.04 | 1.74 | 0.00 | 13.4 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.29 | 17.35 | 27.49 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.42 | 12.09 | 19.32 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.57 | 11.93 | 18.95 | 5.00 | 89.8 | 68.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.13 | 10.51 | 16.73 | 3.00 | 87.9 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.66 | 9.22 | 15.88 | -1.00 | 81.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.38 | 19.10 | 31.75 | 2.00 | 78.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.58 | 18.21 | 30.09 | 9.00 | 90.0 | 79.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.47 | 10.79 | 17.46 | 2.00 | 68.6 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.60 | 22.70 | 38.15 | 5.00 | 90.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.83 | 19.97 | 31.25 | 2.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.95 | 16.24 | 25.23 | 6.00 | 90.0 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.54 | 14.52 | 23.88 | 3.00 | 90.0 | 85.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.83 | 12.81 | 21.44 | 2.00 | 90.0 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.15
- Actual score: 35.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 0.84 | 3.94 | 7.15 | 0.00 | 38.3 | 90.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 4.0 | 0.36 | 0.91 | 1.45 | 0.00 | 6.6 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.33 | 13.09 | 20.47 | 6.00 | 75.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.20 | 10.24 | 16.71 | 2.00 | 74.7 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.29 | 8.68 | 14.03 | 1.00 | 73.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.36 | 7.11 | 11.71 | 9.00 | 67.9 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.91 | 5.81 | 10.26 | 0.00 | 11.5 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.80 | 20.82 | 33.89 | 9.00 | 83.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.60 | 15.95 | 26.04 | 2.00 | 74.7 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.50 | 7.77 | 12.96 | 2.00 | 48.8 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.14 | 22.59 | 37.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.62 | 15.76 | 24.31 | 2.00 | 84.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.16 | 15.21 | 23.88 | 2.00 | 87.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.89 | 12.54 | 19.26 | 2.00 | 69.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.14 | 10.59 | 17.31 | 3.00 | 76.4 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 67.77
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.45) beats the best remaining Bench Boost opportunity (9.20).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 4.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.45) beats the best remaining Bench Boost opportunity (9.20).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.87 | 6.44 | 9.86 | 0.00 | 66.6 | 0.0 |
| Bench 1 | Bench Boost | Gabriel Słonina | GK | 7 | 4.0 | 0.18 | 1.31 | 1.41 | 0.00 | 6.3 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.42 | 12.58 | 18.86 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.88 | 12.16 | 18.72 | 1.00 | 69.9 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.01 | 11.94 | 18.43 | 9.00 | 84.3 | 90.0 |
| Bench 2 | Bench Boost | Reinildo Mandava | DEF | 17 | 4.0 | 2.89 | 8.18 | 12.62 | 6.00 | 74.2 | 90.0 |
| Bench 4 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.13 | 7.03 | 11.04 | 0.00 | 59.5 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.82 | 20.63 | 33.12 | 13.00 | 79.2 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.46 | 15.95 | 24.60 | 2.00 | 69.5 | 71.0 |
| Bench 3 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.21 | 7.66 | 12.24 | 0.00 | 50.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.18 | 23.70 | 37.80 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.65 | 17.26 | 25.27 | 13.00 | 81.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.22 | 12.73 | 19.56 | 3.00 | 68.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.86 | 11.75 | 18.33 | 3.00 | 76.1 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.81 | 10.55 | 16.46 | 1.00 | 77.1 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 61.13
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.49) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.49) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 0.59 | 2.92 | 5.26 | 0.00 | 32.3 | 0.0 |
| Bench 1 | Bench | Gabriel Słonina | GK | 7 | 4.0 | 0.02 | 0.80 | 1.29 | 0.00 | 6.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.13 | 11.84 | 18.46 | 2.00 | 81.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.06 | 11.57 | 17.56 | 7.00 | 77.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.35 | 10.27 | 16.88 | 0.00 | 59.7 | 63.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.36 | 8.90 | 13.73 | -2.00 | 80.7 | 32.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.53 | 7.05 | 11.34 | 4.00 | 66.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.30 | 21.56 | 35.61 | 9.00 | 87.7 | 75.0 |
| Bench 2 | Bench | Hugo Ekitiké | FWD | 12 | 8.7 | 3.31 | 11.55 | 19.56 | 8.00 | 48.4 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.50 | 4.98 | 8.49 | 1.00 | 28.6 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.46 | 22.33 | 36.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.88 | 17.92 | 27.18 | 5.00 | 82.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.06 | 12.06 | 19.69 | 7.00 | 74.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.37 | 10.72 | 17.79 | 9.00 | 77.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.64 | 9.55 | 15.26 | 15.00 | 75.7 | 90.0 |