# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 235.73
- Total actual points: 217.00
- Average predicted points: 58.93
- Average actual points: 54.25
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
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.05
- Actual score: 74.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.71 | 10.28 | 16.91 | 11.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.22 | 9.46 | 15.58 | 2.00 | 87.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.3 | 5.03 | 14.93 | 24.17 | 0.00 | 85.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.51 | 12.93 | 21.26 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.90 | 12.45 | 21.01 | 0.00 | 81.3 | 0.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 11 | 6.2 | 3.87 | 11.32 | 18.36 | 1.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 3.03 | 9.57 | 15.67 | 0.00 | 75.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.30 | 11.77 | 18.87 | 2.00 | 83.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 4.21 | 11.16 | 17.55 | 2.00 | 84.6 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.76 | 8.79 | 14.20 | 1.00 | 76.2 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 6.60 | 19.21 | 31.36 | 16.00 | 89.3 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.79 | 16.88 | 28.11 | 9.00 | 90.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.65 | 16.27 | 25.92 | 7.00 | 85.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.78 | 14.25 | 23.38 | 3.00 | 84.7 | 90.0 |
| XI | XI | Anthony Elanga | MID | 16 | 5.0 | 3.97 | 11.23 | 18.07 | 5.00 | 88.8 | 86.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 60.47
- Actual score: 33.00
- Transfer: Kieran Trippier -> William Saliba (projected gain 0.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.97 | 11.40 | 18.75 | 3.00 | 90.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 2.99 | 8.86 | 14.66 | 9.00 | 89.2 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 4.66 | 13.93 | 22.59 | 0.00 | 82.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 3.91 | 12.16 | 20.20 | 6.00 | 87.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.84 | 10.73 | 17.49 | 6.00 | 84.5 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 11 | 6.2 | 3.37 | 9.89 | 16.15 | 6.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 3.18 | 9.81 | 16.06 | 0.00 | 84.5 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.63 | 12.66 | 19.97 | 2.00 | 85.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.76 | 10.49 | 16.62 | 8.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.53 | 7.53 | 12.60 | 1.00 | 53.6 | 23.0 |
| Captain | Bench | Mohamed Salah | MID | 11 | 13.3 | 7.59 | 22.05 | 35.40 | 0.00 | 101.9 | 0.0 |
| XI | Bench | Son Heung-min | MID | 18 | 9.9 | 5.82 | 17.91 | 29.92 | 0.00 | 94.9 | 0.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.13 | 16.64 | 26.66 | 3.00 | 88.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.76 | 13.91 | 22.49 | 2.00 | 81.5 | 90.0 |
| XI | Bench | Anthony Elanga | MID | 16 | 5.0 | 3.80 | 11.05 | 18.03 | 0.00 | 84.5 | 0.0 |

## GW22

- Train rows: 119414
- Bank: 1.20 -> 3.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.46
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.85).
- Transfer: Son Heung-min -> Phil Foden (projected gain 5.65, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.05) beats the best remaining Triple Captain opportunity (6.85).
- Autosub outfielders: Cameron Archer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.71 | 10.91 | 18.05 | 3.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.5 | 3.16 | 9.34 | 15.53 | 10.00 | 92.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.32 | 12.79 | 21.13 | 1.00 | 83.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.92 | 11.13 | 18.04 | 2.00 | 82.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 3.59 | 10.25 | 16.46 | 2.00 | 79.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.5 | 2.49 | 8.75 | 15.88 | 1.00 | 31.0 | 22.0 |
| Bench 4 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 1.71 | 5.86 | 10.32 | 2.00 | 46.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.36 | 12.28 | 19.23 | 2.00 | 78.8 | 70.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.58 | 10.74 | 17.01 | 1.00 | 83.0 | 45.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.17 | 6.75 | 11.54 | 1.00 | 46.3 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 6.05 | 17.07 | 26.91 | 10.00 | 80.1 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 4.79 | 14.14 | 22.24 | 6.00 | 62.1 | 76.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.1 | 4.15 | 12.66 | 21.41 | 1.00 | 63.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 3.43 | 12.55 | 23.22 | 0.00 | 21.2 | 0.0 |
| Bench 3 | Bench | Anthony Elanga | MID | 16 | 5.1 | 1.99 | 7.19 | 12.51 | 1.00 | 47.8 | 12.0 |

## GW23

- Train rows: 120213
- Bank: 3.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Julián Álvarez
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 59.75
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.37) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cameron Archer -> Julián Álvarez (projected gain 5.98, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.37) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.35 | 10.80 | 17.84 | 1.00 | 86.4 | 45.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.5 | 3.30 | 9.77 | 16.22 | 2.00 | 93.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 4.40 | 13.10 | 21.54 | 1.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.59 | 10.87 | 17.88 | 1.00 | 85.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.3 | 3.04 | 9.83 | 16.26 | 1.00 | 81.9 | 90.0 |
| Bench 2 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.5 | 2.49 | 9.18 | 15.92 | 1.00 | 44.7 | 57.0 |
| XI | XI | Marcos Senesi | DEF | 3 | 4.5 | 2.97 | 8.32 | 13.41 | 1.00 | 73.1 | 90.0 |
| Vice Captain | XI | Julián Álvarez | FWD | 13 | 7.0 | 5.35 | 14.91 | 23.94 | 2.00 | 79.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 3.58 | 10.72 | 17.91 | 8.00 | 64.0 | 87.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 5.0 | 2.43 | 8.05 | 13.94 | 0.00 | 49.9 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.1 | 5.79 | 16.88 | 27.45 | 9.00 | 87.3 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 4.52 | 13.69 | 22.77 | 20.00 | 72.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.1 | 4.01 | 12.56 | 21.51 | 2.00 | 73.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.1 | 2.99 | 11.27 | 19.84 | 0.00 | 30.3 | 0.0 |
| Bench 4 | Bench Boost | Anthony Elanga | MID | 16 | 5.1 | 2.15 | 7.14 | 12.61 | 2.00 | 39.9 | 77.0 |