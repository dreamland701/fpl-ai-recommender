# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 235.41
- Total actual points: 252.00
- Average predicted points: 58.85
- Average actual points: 63.00
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
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.60
- Actual score: 69.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.50 | 9.47 | 15.44 | 11.00 | 77.7 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.07 | 8.99 | 14.64 | 2.00 | 87.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.76 | 16.12 | 25.84 | 0.00 | 93.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.54 | 13.04 | 20.86 | 2.00 | 92.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.94 | 11.22 | 18.18 | 0.00 | 91.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.93 | 11.05 | 17.90 | 1.00 | 83.9 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.15 | 9.40 | 15.08 | 1.00 | 84.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.25 | 10.92 | 16.92 | 2.00 | 79.8 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.69 | 9.85 | 15.55 | 2.00 | 76.1 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.43 | 7.86 | 12.58 | 1.00 | 70.5 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.59 | 21.14 | 34.50 | 16.00 | 103.4 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.93 | 17.58 | 28.88 | 9.00 | 96.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.52 | 16.40 | 26.68 | 7.00 | 89.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.36 | 15.27 | 24.60 | 3.00 | 95.8 | 90.0 |
| Bench 2 | Bench | Dwight McNeil | MID | 9 | 5.4 | 3.29 | 10.08 | 16.46 | 1.00 | 79.8 | 73.0 |

## GW21

- Train rows: 118627
- Bank: 0.20 -> 2.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 60.36
- Actual score: 59.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 9.52, hit 0)
- Autosub: Dwight McNeil replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.11 | 11.15 | 18.25 | 3.00 | 95.2 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.81 | 8.13 | 13.54 | 9.00 | 86.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.86 | 13.85 | 22.36 | 6.00 | 102.3 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.55 | 12.16 | 20.38 | 0.00 | 65.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 4.10 | 11.30 | 17.85 | 6.00 | 91.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.19 | 11.28 | 18.14 | 6.00 | 91.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.44 | 9.58 | 15.54 | 17.00 | 87.7 | 80.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.98 | 12.64 | 19.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.28 | 9.31 | 15.20 | 8.00 | 69.6 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.31 | 6.52 | 10.71 | 1.00 | 49.2 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.91 | 20.06 | 31.45 | 3.00 | 119.2 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.93 | 17.81 | 27.14 | 2.00 | 116.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.10 | 14.31 | 23.06 | 2.00 | 89.2 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 11 | 13.2 | 1.95 | 11.23 | 21.49 | 0.00 | 13.2 | 0.0 |
| Bench 2 | Autosub In | Dwight McNeil | MID | 9 | 5.4 | 2.85 | 8.42 | 14.08 | 1.00 | 70.3 | 27.0 |

## GW22

- Train rows: 119414
- Bank: 2.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Julián Álvarez
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 57.01
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (7.07).
- Transfer: Chris Wood -> Julián Álvarez (projected gain 3.92, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.23) beats the best remaining Triple Captain opportunity (7.07).
- Autosub: Dwight McNeil replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.44 | 9.75 | 16.22 | 3.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.88 | 8.46 | 14.36 | 10.00 | 88.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.61 | 12.96 | 21.28 | 1.00 | 85.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.98 | 10.86 | 17.52 | 2.00 | 84.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.76 | 10.09 | 16.26 | 2.00 | 79.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.38 | 9.92 | 15.97 | 2.00 | 76.9 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.38 | 8.87 | 15.98 | 1.00 | 28.9 | 22.0 |
| Vice Captain | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.65 | 12.92 | 20.45 | 13.00 | 66.5 | 86.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.93 | 10.86 | 17.04 | 2.00 | 71.9 | 70.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.94 | 5.91 | 10.20 | 1.00 | 40.5 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.23 | 17.12 | 27.26 | 10.00 | 83.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.10 | 11.79 | 22.08 | 0.00 | 14.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.79 | 11.65 | 19.93 | 1.00 | 58.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.65 | 11.60 | 18.49 | 6.00 | 43.4 | 76.0 |
| Bench 2 | Autosub In | Dwight McNeil | MID | 9 | 5.4 | 2.43 | 7.34 | 12.84 | 3.00 | 58.5 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Julián Álvarez
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 56.44
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.44) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.44) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.08 | 9.68 | 15.83 | 1.00 | 81.2 | 45.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 2.79 | 8.37 | 14.16 | 2.00 | 85.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.19 | 12.22 | 20.07 | 1.00 | 84.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.39 | 10.30 | 16.68 | 1.00 | 83.3 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.73 | 9.88 | 16.87 | 1.00 | 46.2 | 57.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.99 | 9.63 | 15.51 | -1.00 | 81.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 2.94 | 9.62 | 15.74 | 1.00 | 79.5 | 90.0 |
| Vice Captain | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.98 | 13.24 | 21.89 | 2.00 | 67.8 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.77 | 8.69 | 14.93 | 8.00 | 48.4 | 87.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.15 | 4.42 | 8.25 | 1.00 | 24.0 | 25.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.56 | 16.78 | 26.91 | 9.00 | 87.5 | 78.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.61 | 12.70 | 21.85 | 0.00 | 36.4 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.21 | 12.63 | 20.91 | 20.00 | 62.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.71 | 11.58 | 20.03 | 2.00 | 67.8 | 90.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 2.77 | 8.10 | 13.60 | 2.00 | 69.8 | 84.0 |