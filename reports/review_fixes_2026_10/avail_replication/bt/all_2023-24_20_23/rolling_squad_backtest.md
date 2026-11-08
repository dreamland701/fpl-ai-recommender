# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 196.02
- Total actual points: 204.00
- Average predicted points: 49.01
- Average actual points: 51.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW19 are included before the first simulated week.
- League-average scores were not available for this run.

## GW20

- Train rows: 117854
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.00
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.68 | 8.00 | 12.55 | 2.00 | 89.3 | 90.0 |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.21 | 7.89 | 12.36 | 11.00 | 81.0 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 4.75 | 13.26 | 22.14 | 0.00 | 96.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.34 | 11.07 | 17.64 | 2.00 | 91.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.35 | 10.23 | 16.29 | 0.00 | 92.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.33 | 9.18 | 15.07 | 1.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Vladimír Coufal | DEF | 19 | 4.6 | 2.77 | 7.43 | 12.57 | 0.00 | 85.3 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.44 | 8.94 | 13.71 | 2.00 | 60.5 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.29 | 8.37 | 12.99 | 2.00 | 78.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.13 | 6.52 | 9.92 | 1.00 | 75.2 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.07 | 19.28 | 31.34 | 16.00 | 104.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 4.62 | 14.99 | 25.00 | 9.00 | 96.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 4.20 | 13.77 | 23.05 | 7.00 | 90.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.34 | 13.25 | 21.61 | 3.00 | 98.0 | 90.0 |
| Bench 2 | Bench | Michael Olise | MID | 8 | 5.8 | 3.28 | 9.65 | 15.67 | 15.00 | 79.3 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.20 -> 2.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 53.31
- Actual score: 40.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.13, hit 0)
- Autosub: Cameron Archer replaced Trent Alexander-Arnold.
- Autosub: Vladimír Coufal replaced Michael Olise.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.42 | 9.76 | 16.07 | 3.00 | 95.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.51 | 7.75 | 13.15 | 9.00 | 87.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.26 | 11.88 | 19.13 | 6.00 | 103.8 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.35 | 10.99 | 18.36 | 0.00 | 69.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.60 | 9.80 | 15.25 | 6.00 | 93.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.29 | 9.53 | 14.81 | 6.00 | 95.9 | 90.0 |
| Bench 4 | Autosub In | Vladimír Coufal | DEF | 19 | 4.6 | 1.28 | 3.80 | 6.98 | -2.00 | 28.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.77 | 10.67 | 16.07 | 2.00 | 93.7 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 2.77 | 7.73 | 12.35 | 8.00 | 73.6 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.11 | 5.58 | 9.15 | 1.00 | 62.8 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.49 | 18.11 | 28.30 | 3.00 | 120.4 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.25 | 16.57 | 25.12 | 2.00 | 115.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.08 | 11.39 | 19.56 | 2.00 | 69.4 | 90.0 |
| XI | Bench | Michael Olise | MID | 8 | 5.8 | 2.54 | 9.72 | 16.81 | 0.00 | 77.9 | 0.0 |
| Bench 3 | Bench | Mohamed Salah | MID | 11 | 13.2 | 1.72 | 9.35 | 18.48 | 0.00 | 12.5 | 0.0 |

## GW22

- Train rows: 119414
- Bank: 2.10 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Martin Ødegaard
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 45.27
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.11) beats the best remaining Triple Captain opportunity (5.80).
- Transfer: Phil Foden -> Martin Ødegaard (projected gain 4.83, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.11) beats the best remaining Triple Captain opportunity (5.80).
- Autosub: Trent Alexander-Arnold replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.85 | 7.76 | 12.94 | 3.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.48 | 7.18 | 11.88 | 10.00 | 88.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.81 | 11.40 | 18.05 | 1.00 | 87.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.29 | 9.18 | 14.66 | 2.00 | 86.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 2.77 | 8.55 | 13.15 | 2.00 | 80.8 | 90.0 |
| Bench 3 | Autosub In | Trent Alexander-Arnold | DEF | 11 | 8.4 | 1.87 | 7.51 | 12.78 | 1.00 | 17.5 | 22.0 |
| Bench 2 | Bench | Vladimír Coufal | DEF | 19 | 4.6 | 2.05 | 5.24 | 9.01 | 0.00 | 70.8 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.12 | 9.58 | 15.02 | 2.00 | 77.7 | 70.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 2.37 | 7.71 | 12.03 | 1.00 | 76.3 | 45.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.84 | 5.38 | 8.93 | 1.00 | 56.2 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.11 | 14.67 | 23.31 | 10.00 | 86.6 | 90.0 |
| Vice Captain | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.35 | 11.74 | 18.75 | 2.00 | 80.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 2.26 | 10.62 | 19.52 | 0.00 | 7.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 2.96 | 10.53 | 18.35 | 1.00 | 38.9 | 90.0 |
| XI | XI | Michael Olise | MID | 8 | 5.8 | 2.14 | 6.37 | 11.86 | 16.00 | 51.5 | 69.0 |

## GW23

- Train rows: 120213
- Bank: 1.50 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Julián Álvarez
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 44.44
- Actual score: 34.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.76) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Julián Álvarez (projected gain 4.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.76) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.2 | 2.28 | 8.21 | 13.66 | 1.00 | 83.6 | 45.0 |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 2.39 | 6.59 | 11.10 | 2.00 | 86.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.39 | 10.66 | 16.95 | 1.00 | 85.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.63 | 8.52 | 14.25 | 1.00 | 62.7 | 57.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 2.80 | 8.42 | 13.91 | 1.00 | 84.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 2.64 | 7.85 | 12.72 | 1.00 | 82.4 | 90.0 |
| Bench 4 | Bench Boost | Vladimír Coufal | DEF | 19 | 4.6 | 0.66 | 3.03 | 5.75 | 1.00 | 28.5 | 71.0 |
| Vice Captain | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.19 | 11.64 | 18.98 | 2.00 | 70.7 | 90.0 |
| Bench 2 | Bench Boost | Chris Wood | FWD | 16 | 4.9 | 1.87 | 6.59 | 11.40 | 0.00 | 53.4 | 0.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 0.95 | 3.29 | 6.09 | 1.00 | 13.6 | 25.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 4.55 | 14.45 | 23.86 | 9.00 | 88.6 | 78.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 3.07 | 11.10 | 17.23 | 2.00 | 77.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.28 | 10.95 | 18.70 | 0.00 | 25.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.99 | 10.27 | 17.24 | 2.00 | 73.9 | 90.0 |
| XI | XI | Michael Olise | MID | 8 | 5.8 | 2.21 | 8.19 | 14.27 | 1.00 | 65.3 | 10.0 |