# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 222.11
- Total actual points: 293.00
- Average predicted points: 55.53
- Average actual points: 73.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.30
- Actual score: 85.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.25 | 8.68 | 14.13 | 11.00 | 78.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.79 | 8.21 | 13.39 | 2.00 | 87.3 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.32 | 14.79 | 23.73 | 0.00 | 94.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.06 | 11.61 | 18.59 | 2.00 | 92.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.63 | 10.24 | 16.65 | 1.00 | 83.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.58 | 10.15 | 16.47 | 0.00 | 91.6 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.90 | 8.67 | 13.92 | 1.00 | 84.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.90 | 9.94 | 15.42 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Chris Wood | FWD | 16 | 4.9 | 3.37 | 9.05 | 14.38 | 2.00 | 76.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.27 | 7.32 | 11.74 | 1.00 | 71.2 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 6.93 | 19.28 | 31.60 | 16.00 | 103.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.29 | 15.81 | 26.07 | 9.00 | 96.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 4.93 | 14.78 | 24.19 | 7.00 | 89.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.91 | 14.01 | 22.66 | 3.00 | 96.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 3.59 | 10.61 | 18.03 | 18.00 | 47.6 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.43
- Actual score: 68.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 9.03, hit 0)
- Autosub: Chris Wood replaced Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.72 | 9.94 | 16.28 | 3.00 | 95.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.54 | 7.39 | 12.34 | 9.00 | 86.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.51 | 12.72 | 20.51 | 6.00 | 102.8 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.22 | 11.14 | 18.75 | 0.00 | 66.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.92 | 10.86 | 17.17 | 6.00 | 91.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.89 | 10.44 | 16.80 | 6.00 | 91.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.16 | 8.83 | 14.36 | 17.00 | 87.5 | 80.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.65 | 11.72 | 17.89 | 2.00 | 90.7 | 90.0 |
| Bench 2 | Autosub In | Chris Wood | FWD | 16 | 4.9 | 3.05 | 8.75 | 14.37 | 8.00 | 69.6 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.60 | 7.30 | 11.97 | 1.00 | 49.8 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.32 | 18.52 | 29.09 | 3.00 | 119.4 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.86 | 17.60 | 26.79 | 2.00 | 116.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.6 | 5.47 | 12.94 | 19.66 | 10.00 | 118.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.39 | 10.29 | 17.06 | 2.00 | 89.4 | 90.0 |
| Bench 4 | Bench | Mohamed Salah | MID | 11 | 13.2 | 1.15 | 8.99 | 18.06 | 0.00 | 13.5 | 0.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 4.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Kevin De Bruyne
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 51.67
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.69) beats the best remaining Triple Captain opportunity (6.45).
- Transfer: Mohamed Salah -> Kevin De Bruyne (projected gain 5.16, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.69) beats the best remaining Triple Captain opportunity (6.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.13 | 8.76 | 14.58 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.55 | 7.55 | 12.87 | 10.00 | 87.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.16 | 11.58 | 18.98 | 1.00 | 86.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.96 | 10.93 | 19.79 | 1.00 | 29.5 | 22.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.65 | 9.92 | 16.03 | 2.00 | 84.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.10 | 9.19 | 14.83 | 2.00 | 76.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.32 | 8.90 | 14.44 | 2.00 | 79.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.65 | 10.05 | 15.80 | 2.00 | 72.7 | 70.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 2.59 | 8.19 | 13.39 | 1.00 | 73.3 | 45.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.4 | 2.34 | 7.03 | 12.05 | 1.00 | 41.2 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.69 | 15.60 | 24.91 | 10.00 | 83.6 | 90.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 10.6 | 4.95 | 11.85 | 17.46 | 7.00 | 67.7 | 70.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.11 | 10.82 | 16.59 | 2.00 | 55.5 | 84.0 |
| Bench 4 | Bench | Phil Foden | MID | 13 | 7.9 | 1.66 | 7.65 | 12.57 | 6.00 | 43.0 | 76.0 |
| Bench 3 | Bench | Jarrod Bowen | MID | 19 | 8.0 | 1.98 | 7.63 | 13.95 | 1.00 | 58.9 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 4.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 56.70
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.16) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Ollie Watkins (projected gain 6.02, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.16) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.83 | 8.83 | 14.44 | 1.00 | 81.6 | 45.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 2.51 | 7.60 | 12.92 | 2.00 | 85.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.23 | 11.67 | 19.94 | 1.00 | 46.7 | 57.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.83 | 11.09 | 18.21 | 1.00 | 84.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.12 | 9.49 | 15.39 | 1.00 | 83.1 | 90.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.2 | 2.74 | 9.04 | 14.82 | 1.00 | 79.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.76 | 8.96 | 14.47 | -1.00 | 81.7 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.22 | 14.67 | 23.70 | 18.00 | 93.3 | 90.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 4.9 | 2.35 | 8.13 | 14.31 | 0.00 | 39.4 | 0.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.56 | 5.80 | 10.73 | 1.00 | 24.6 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.04 | 15.30 | 24.57 | 9.00 | 87.6 | 78.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.6 | 4.56 | 14.17 | 22.18 | 5.00 | 30.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.14 | 12.42 | 20.57 | 20.00 | 62.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.98 | 11.48 | 18.43 | 8.00 | 86.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.63 | 11.36 | 19.69 | 2.00 | 67.9 | 90.0 |