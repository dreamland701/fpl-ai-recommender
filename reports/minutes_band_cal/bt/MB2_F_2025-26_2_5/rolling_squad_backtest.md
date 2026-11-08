# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 249.41
- Total actual points: 257.00
- Average predicted points: 62.35
- Average actual points: 64.25
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
- Predicted score: 65.58
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Martin Dúbravka replaced Marco Bizot.
- Autosub: Lyle Foster replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Marco Bizot | GK | 2 | 4.5 | 3.53 | 9.08 | 15.03 | 0.00 | 83.1 | 0.0 |
| Bench 1 | Autosub In | Martin Dúbravka | GK | 3 | 4.0 | 2.86 | 7.00 | 11.66 | 6.00 | 83.1 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.6 | 6.77 | 15.83 | 25.37 | 1.00 | 83.1 | 8.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 4.03 | 10.27 | 16.49 | 1.00 | 81.9 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.61 | 9.05 | 15.52 | -1.00 | 79.8 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.61 | 8.99 | 14.61 | 3.00 | 81.1 | 90.0 |
| Bench 4 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.02 | 6.82 | 12.05 | 2.00 | 79.5 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.0 | 6.26 | 18.97 | 31.65 | 2.00 | 79.1 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 5.06 | 16.69 | 27.97 | 9.00 | 83.1 | 79.0 |
| Bench 2 | Autosub In | Lyle Foster | FWD | 3 | 5.0 | 2.82 | 7.49 | 12.22 | 2.00 | 70.7 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.08 | 21.17 | 36.04 | 5.00 | 83.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 6.31 | 18.45 | 29.14 | 2.00 | 83.1 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.11 | 15.91 | 26.75 | 0.00 | 83.1 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.1 | 6.43 | 14.72 | 23.11 | 6.00 | 83.1 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.31 | 11.29 | 19.32 | 2.00 | 83.1 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 54.24
- Actual score: 52.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 8.36, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.44 | 7.14 | 11.85 | 2.00 | 80.2 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 1.42 | 4.57 | 7.82 | 0.00 | 38.3 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.28 | 8.68 | 14.06 | 1.00 | 74.3 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.80 | 8.39 | 13.67 | 2.00 | 75.7 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.05 | 7.76 | 12.78 | 7.00 | 77.1 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.40 | 7.26 | 12.02 | 9.00 | 71.7 | 79.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.91 | 5.81 | 10.26 | 0.00 | 11.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 6.67 | 20.56 | 33.44 | 9.00 | 81.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.46 | 15.81 | 25.93 | 2.00 | 75.6 | 78.0 |
| Bench 3 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.37 | 7.45 | 12.21 | 6.00 | 67.6 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 6.63 | 21.07 | 35.63 | 3.00 | 83.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 4.54 | 15.53 | 23.89 | 2.00 | 82.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.82 | 15.52 | 25.25 | 10.00 | 83.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.81 | 12.56 | 19.46 | 2.00 | 73.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.06 | 10.54 | 17.29 | 3.00 | 77.2 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 1.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 65.17
- Actual score: 77.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.70) beats the best remaining Triple Captain opportunity (9.45).
- Transfer: Daniel Ballard -> Marc Cucurella Saseta (projected gain 4.98, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.70) beats the best remaining Triple Captain opportunity (9.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.64 | 7.82 | 12.12 | 3.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Marco Bizot | GK | 2 | 4.5 | 2.18 | 6.88 | 10.43 | 0.00 | 70.3 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.93 | 12.33 | 19.05 | 1.00 | 73.6 | 45.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.66 | 8.36 | 12.96 | 6.00 | 76.1 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 2.88 | 8.17 | 12.64 | 6.00 | 75.1 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 4.0 | 2.60 | 7.42 | 11.54 | 4.00 | 68.5 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.27 | 7.17 | 11.17 | 0.00 | 59.5 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.0 | 6.68 | 20.51 | 33.03 | 13.00 | 80.1 | 86.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 5.28 | 15.88 | 24.71 | 2.00 | 73.2 | 71.0 |
| Bench 2 | Bench | Lyle Foster | FWD | 3 | 5.0 | 2.91 | 8.66 | 13.37 | 2.00 | 73.5 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.68 | 22.16 | 35.67 | 9.00 | 83.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.2 | 5.52 | 16.99 | 24.83 | 13.00 | 78.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.01 | 14.67 | 23.89 | 2.00 | 76.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.79 | 11.70 | 18.30 | 3.00 | 77.0 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.75 | 10.51 | 16.45 | 1.00 | 78.0 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Erling Haaland
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.42
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.73) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.73) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.92 | 8.06 | 12.96 | 4.00 | 83.1 | 90.0 |
| Bench 1 | Bench Boost | Marco Bizot | GK | 2 | 4.5 | 0.96 | 3.36 | 5.74 | 0.00 | 32.2 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.1 | 3.50 | 10.78 | 17.66 | 0.00 | 64.7 | 63.0 |
| XI | XI | Joe Rodon | DEF | 11 | 4.0 | 3.74 | 9.18 | 13.60 | 2.00 | 80.2 | 90.0 |
| XI | XI | Reinildo Mandava | DEF | 17 | 4.0 | 3.33 | 8.75 | 13.39 | -2.00 | 78.6 | 32.0 |
| Bench 3 | Bench Boost | Trai Hume | DEF | 17 | 4.5 | 3.03 | 8.58 | 13.92 | 4.00 | 80.3 | 90.0 |
| Bench 4 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.64 | 7.28 | 11.73 | 4.00 | 69.9 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.1 | 5.80 | 20.05 | 33.47 | 9.00 | 80.9 | 75.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 3.61 | 12.21 | 20.50 | 8.00 | 53.4 | 66.0 |
| Bench 2 | Bench Boost | Lyle Foster | FWD | 3 | 5.0 | 3.07 | 8.44 | 13.51 | 6.00 | 74.4 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.96 | 20.81 | 34.45 | 5.00 | 83.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.3 | 5.78 | 17.70 | 26.78 | 5.00 | 80.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.21 | 14.52 | 23.01 | 10.00 | 78.1 | 86.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.32 | 10.66 | 17.77 | 9.00 | 78.5 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.58 | 9.50 | 15.25 | 15.00 | 76.6 | 90.0 |