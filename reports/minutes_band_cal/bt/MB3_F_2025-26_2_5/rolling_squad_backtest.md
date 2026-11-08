# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 257.03
- Total actual points: 240.00
- Average predicted points: 64.26
- Average actual points: 60.00
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
- Predicted score: 70.04
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 4.05 | 10.60 | 17.14 | 0.00 | 90.0 | 0.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 4.0 | 0.23 | 0.84 | 1.58 | 0.00 | 11.9 | 0.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.29 | 17.35 | 27.49 | 1.00 | 90.0 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.42 | 12.09 | 19.32 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.57 | 11.93 | 18.95 | 5.00 | 89.8 | 68.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.13 | 10.51 | 16.73 | 3.00 | 87.9 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.66 | 9.22 | 15.88 | -1.00 | 81.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.27 | 18.95 | 31.51 | 2.00 | 80.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.58 | 18.21 | 30.09 | 9.00 | 90.0 | 79.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.34 | 10.81 | 17.65 | 2.00 | 72.3 | 62.0 |
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
- Predicted score: 55.31
- Actual score: 35.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Marco Bizot | GK | 2 | 4.5 | 1.37 | 4.45 | 7.68 | 0.00 | 37.4 | 90.0 |
| Bench 1 | Bench | Karl Darlow | GK | 11 | 4.0 | 0.32 | 0.82 | 1.40 | 0.00 | 8.0 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.34 | 13.06 | 20.36 | 6.00 | 77.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.20 | 10.20 | 16.59 | 2.00 | 76.4 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.29 | 8.64 | 13.92 | 1.00 | 75.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.39 | 7.26 | 12.03 | 9.00 | 71.5 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.85 | 5.70 | 10.16 | 0.00 | 10.6 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.72 | 20.74 | 33.82 | 9.00 | 83.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.48 | 15.77 | 25.78 | 2.00 | 76.5 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.72 | 8.26 | 13.65 | 2.00 | 52.7 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.14 | 22.59 | 37.74 | 3.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.59 | 15.72 | 24.27 | 2.00 | 84.6 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.16 | 15.21 | 23.88 | 2.00 | 87.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 12.56 | 19.46 | 2.00 | 73.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.08 | 10.50 | 17.14 | 3.00 | 78.1 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 68.32
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.20) beats the best remaining Triple Captain opportunity (10.06).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 4.56, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.20) beats the best remaining Triple Captain opportunity (10.06).
- Autosub: Karl Darlow replaced Marco Bizot.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 2.17 | 6.87 | 10.43 | 0.00 | 70.1 | 0.0 |
| Bench 1 | Autosub In | Karl Darlow | GK | 11 | 4.0 | 0.22 | 1.35 | 1.54 | 3.00 | 8.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.42 | 12.58 | 18.86 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.92 | 12.32 | 19.05 | 1.00 | 73.4 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.00 | 11.93 | 18.43 | 9.00 | 84.3 | 90.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 2.89 | 8.14 | 12.51 | 6.00 | 76.0 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.42 | 7.60 | 11.80 | 0.00 | 63.3 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.70 | 20.48 | 32.90 | 13.00 | 80.9 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.27 | 15.87 | 24.71 | 2.00 | 73.0 | 71.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.40 | 8.14 | 12.91 | 0.00 | 54.4 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.18 | 23.70 | 37.80 | 9.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.56 | 17.17 | 25.19 | 13.00 | 81.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.16 | 12.79 | 19.80 | 3.00 | 72.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 11.67 | 18.17 | 3.00 | 77.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.77 | 10.48 | 16.33 | 1.00 | 78.8 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 63.37
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.46) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.46) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Karl Darlow | GK | 11 | 4.0 | 1.80 | 4.88 | 7.42 | 3.00 | 50.4 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 0.91 | 3.25 | 5.60 | 0.00 | 31.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.12 | 11.82 | 18.45 | 2.00 | 81.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.03 | 11.49 | 17.43 | 7.00 | 78.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.46 | 10.65 | 17.47 | 0.00 | 63.4 | 63.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.36 | 8.90 | 13.73 | -2.00 | 80.7 | 32.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.63 | 7.27 | 11.72 | 4.00 | 69.8 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.30 | 21.56 | 35.61 | 9.00 | 87.7 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.56 | 12.09 | 20.31 | 8.00 | 52.1 | 66.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.54 | 4.98 | 8.50 | 1.00 | 27.7 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.46 | 22.33 | 36.59 | 5.00 | 90.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.81 | 17.85 | 27.12 | 5.00 | 82.4 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.99 | 11.94 | 19.51 | 7.00 | 76.1 | 90.0 |
| Bench 2 | Bench Boost | Tijjani Reijnders | MID | 13 | 5.6 | 3.34 | 10.64 | 17.64 | 9.00 | 79.3 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.60 | 9.47 | 15.12 | 15.00 | 77.5 | 90.0 |