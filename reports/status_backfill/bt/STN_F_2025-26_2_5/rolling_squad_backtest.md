# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 264.07
- Total actual points: 246.00
- Average predicted points: 66.02
- Average actual points: 61.50
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
- Captain: Tijjani Reijnders
- Vice captain: Antoine Semenyo
- Effective captain: Tijjani Reijnders
- Chip used: none
- Predicted score: 71.56
- Actual score: 49.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Martin Dúbravka replaced Marco Bizot.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 3.97 | 10.60 | 17.14 | 0.00 | 91.6 | 0.0 |
| Bench 1 | Autosub In | Martin Dúbravka | GK | 3 | 4.0 | 3.30 | 8.52 | 13.78 | 6.00 | 97.4 | 90.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 7.18 | 17.35 | 27.49 | 1.00 | 98.7 | 8.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.58 | 12.09 | 19.32 | 6.00 | 107.4 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.67 | 11.93 | 18.95 | 5.00 | 93.0 | 68.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 4.15 | 10.51 | 16.73 | 3.00 | 86.7 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.65 | 9.22 | 15.88 | -1.00 | 81.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.41 | 18.96 | 31.60 | 2.00 | 85.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.99 | 18.21 | 30.09 | 9.00 | 100.5 | 79.0 |
| XI | XI | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.18 | 10.62 | 17.29 | 2.00 | 66.7 | 62.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.5 | 7.41 | 22.70 | 38.15 | 5.00 | 114.8 | 90.0 |
| Captain | Captain | Tijjani Reijnders | MID | 13 | 5.6 | 7.51 | 19.97 | 31.25 | 2.00 | 145.5 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.1 | 7.41 | 16.24 | 25.23 | 6.00 | 124.1 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.73 | 14.52 | 23.88 | 3.00 | 99.6 | 85.0 |
| Bench 3 | Bench | Anton Stach | MID | 11 | 5.0 | 3.89 | 12.81 | 21.44 | 2.00 | 89.8 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.13
- Actual score: 37.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.91 | 8.66 | 13.96 | 2.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.43 | 4.56 | 7.79 | 0.00 | 38.2 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 4.65 | 13.08 | 20.45 | 6.00 | 82.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 3.13 | 10.21 | 16.68 | 2.00 | 73.8 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.25 | 8.65 | 14.01 | 1.00 | 72.5 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.26 | 7.06 | 11.66 | 9.00 | 66.5 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.79 | 5.81 | 10.26 | 0.00 | 8.5 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.92 | 20.74 | 33.82 | 9.00 | 87.7 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.72 | 15.78 | 25.87 | 2.00 | 79.2 | 78.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.52 | 7.83 | 13.02 | 2.00 | 48.2 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.07 | 22.59 | 37.74 | 3.00 | 108.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.12 | 15.72 | 24.27 | 2.00 | 93.2 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 5.47 | 15.21 | 23.88 | 2.00 | 92.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 12.37 | 19.10 | 2.00 | 69.9 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.03 | 10.52 | 17.24 | 3.00 | 74.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 69.73
- Actual score: 81.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.15) beats the best remaining Triple Captain opportunity (9.99).
- Transfer: Daniel Ballard -> Marc Guéhi (projected gain 4.56, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.15) beats the best remaining Triple Captain opportunity (9.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.13 | 9.36 | 14.24 | 3.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 2.08 | 6.67 | 10.07 | 0.00 | 66.2 | 0.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.70 | 12.58 | 18.86 | 6.00 | 100.7 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.0 | 3.86 | 12.13 | 18.69 | 1.00 | 69.9 | 45.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.07 | 11.93 | 18.43 | 9.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Reinildo Mandava | DEF | 17 | 4.0 | 2.86 | 8.15 | 12.59 | 6.00 | 73.9 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.27 | 7.17 | 11.17 | 0.00 | 59.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.74 | 20.49 | 32.98 | 13.00 | 81.1 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.34 | 15.68 | 24.35 | 2.00 | 71.7 | 71.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.23 | 7.71 | 12.28 | 0.00 | 50.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.12 | 23.70 | 37.80 | 9.00 | 105.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 6.07 | 17.17 | 25.19 | 13.00 | 88.9 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 4.04 | 12.59 | 19.44 | 3.00 | 67.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.69 | 11.67 | 18.25 | 3.00 | 74.1 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.73 | 10.49 | 16.41 | 1.00 | 76.1 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.64
- Actual score: 79.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.25) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.25) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.41 | 9.58 | 15.09 | 4.00 | 91.4 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 0.95 | 3.36 | 5.71 | 0.00 | 31.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.0 | 4.13 | 11.82 | 18.45 | 2.00 | 81.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 4.6 | 4.11 | 11.51 | 17.51 | 7.00 | 77.8 | 90.0 |
| Bench 2 | Bench Boost | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.19 | 10.22 | 16.84 | 0.00 | 57.7 | 63.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.33 | 8.90 | 13.73 | -2.00 | 79.6 | 32.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.51 | 7.08 | 11.37 | 4.00 | 64.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 6.50 | 21.56 | 35.61 | 9.00 | 91.8 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.23 | 11.66 | 19.67 | 8.00 | 45.4 | 66.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.57 | 5.09 | 8.60 | 1.00 | 28.6 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.38 | 22.33 | 36.59 | 5.00 | 102.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 6.25 | 17.85 | 27.12 | 5.00 | 88.8 | 90.0 |
| XI | XI | Mohammed Kudus | MID | 18 | 6.5 | 3.92 | 11.96 | 19.59 | 7.00 | 73.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.25 | 10.65 | 17.72 | 9.00 | 76.1 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.56 | 9.49 | 15.20 | 15.00 | 74.7 | 90.0 |