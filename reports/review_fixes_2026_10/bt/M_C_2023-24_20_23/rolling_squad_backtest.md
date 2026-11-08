# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 236.00
- Total actual points: 224.00
- Average predicted points: 59.00
- Average actual points: 56.00
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
- Predicted score: 59.04
- Actual score: 74.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Kieran Trippier.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.74 | 10.40 | 17.17 | 11.00 | 79.4 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.17 | 9.41 | 15.60 | 2.00 | 87.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.3 | 5.01 | 14.95 | 24.26 | 0.00 | 85.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 4.54 | 13.04 | 21.40 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.90 | 12.45 | 21.19 | 0.00 | 81.3 | 0.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 11 | 6.2 | 3.86 | 11.29 | 18.44 | 1.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 3.00 | 9.52 | 15.74 | 0.00 | 75.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.26 | 11.69 | 18.74 | 2.00 | 83.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 4.19 | 11.23 | 17.62 | 2.00 | 84.6 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.6 | 2.75 | 8.75 | 14.17 | 1.00 | 76.2 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 6.58 | 19.18 | 31.56 | 16.00 | 89.4 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.82 | 17.00 | 28.44 | 9.00 | 90.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.65 | 16.25 | 26.06 | 7.00 | 85.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.81 | 14.27 | 23.60 | 3.00 | 84.7 | 90.0 |
| XI | XI | Anthony Elanga | MID | 16 | 5.0 | 3.96 | 11.17 | 17.97 | 5.00 | 88.9 | 86.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 60.51
- Actual score: 40.00
- Transfer: Kieran Trippier -> William Saliba (projected gain 0.81, hit 0)
- Autosub: Virgil van Dijk replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.95 | 11.36 | 18.89 | 3.00 | 90.6 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.02 | 8.92 | 14.77 | 9.00 | 89.1 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.3 | 4.68 | 14.08 | 22.84 | 0.00 | 82.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.6 | 3.89 | 12.18 | 20.25 | 6.00 | 87.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.85 | 10.75 | 17.54 | 6.00 | 84.5 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 11 | 6.2 | 3.40 | 10.00 | 16.31 | 6.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 3.18 | 9.83 | 16.15 | 0.00 | 84.6 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.59 | 12.57 | 19.90 | 2.00 | 85.2 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.79 | 10.59 | 16.90 | 8.00 | 80.8 | 90.0 |
| Bench 4 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.49 | 7.47 | 12.48 | 1.00 | 53.6 | 23.0 |
| Captain | Bench | Mohamed Salah | MID | 11 | 13.3 | 7.62 | 22.02 | 35.40 | 0.00 | 101.9 | 0.0 |
| XI | Bench | Son Heung-min | MID | 18 | 9.9 | 5.81 | 17.90 | 29.95 | 0.00 | 95.0 | 0.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.14 | 16.66 | 26.76 | 3.00 | 88.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.73 | 13.83 | 22.31 | 2.00 | 81.5 | 90.0 |
| XI | Bench | Anthony Elanga | MID | 16 | 5.0 | 3.83 | 11.07 | 18.05 | 0.00 | 84.4 | 0.0 |

## GW22

- Train rows: 119414
- Bank: 1.20 -> 3.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.55
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.02) beats the best remaining Triple Captain opportunity (6.83).
- Transfer: Son Heung-min -> Phil Foden (projected gain 5.53, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.02) beats the best remaining Triple Captain opportunity (6.83).
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.74 | 10.97 | 18.32 | 3.00 | 83.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 9 | 4.4 | 3.16 | 9.33 | 15.63 | 10.00 | 92.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.34 | 12.78 | 21.00 | 1.00 | 83.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.89 | 11.07 | 17.96 | 2.00 | 82.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.60 | 10.28 | 16.50 | 2.00 | 79.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.50 | 8.80 | 15.96 | 1.00 | 31.0 | 22.0 |
| Bench 4 | Bench | Marcos Senesi | DEF | 3 | 4.5 | 1.68 | 5.77 | 10.25 | 2.00 | 46.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.35 | 12.19 | 19.14 | 2.00 | 78.8 | 70.0 |
| XI | XI | Chris Wood | FWD | 16 | 4.9 | 3.62 | 10.78 | 17.25 | 1.00 | 83.0 | 45.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.18 | 6.77 | 11.43 | 1.00 | 46.3 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.02 | 16.95 | 26.54 | 10.00 | 80.1 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 4.81 | 14.05 | 21.98 | 6.00 | 62.0 | 76.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.18 | 12.60 | 21.36 | 1.00 | 63.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 3.44 | 12.49 | 23.21 | 0.00 | 21.2 | 0.0 |
| Bench 3 | Bench | Anthony Elanga | MID | 16 | 5.0 | 2.03 | 7.26 | 12.46 | 1.00 | 47.8 | 12.0 |

## GW23

- Train rows: 120213
- Bank: 3.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Julián Álvarez
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 59.91
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.45) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cameron Archer -> Julián Álvarez (projected gain 5.98, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.45) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.34 | 10.85 | 18.00 | 1.00 | 86.4 | 45.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 9 | 4.4 | 3.27 | 9.75 | 16.27 | 2.00 | 93.3 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.40 | 12.99 | 21.32 | 1.00 | 88.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.59 | 10.87 | 17.79 | 1.00 | 85.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.2 | 3.08 | 9.90 | 16.31 | 1.00 | 81.8 | 90.0 |
| Bench 2 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.53 | 9.21 | 15.92 | 1.00 | 44.7 | 57.0 |
| XI | XI | Marcos Senesi | DEF | 3 | 4.5 | 2.95 | 8.26 | 13.28 | 1.00 | 73.1 | 90.0 |
| Vice Captain | XI | Julián Álvarez | FWD | 13 | 7.0 | 5.37 | 14.94 | 24.04 | 2.00 | 79.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.59 | 10.75 | 17.78 | 8.00 | 64.0 | 87.0 |
| Bench 3 | Bench Boost | Chris Wood | FWD | 16 | 4.9 | 2.46 | 8.26 | 14.28 | 0.00 | 49.9 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.78 | 16.80 | 27.14 | 9.00 | 87.3 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.55 | 13.71 | 22.41 | 20.00 | 72.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.00 | 12.56 | 21.54 | 2.00 | 73.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.1 | 3.03 | 11.44 | 19.81 | 0.00 | 30.2 | 0.0 |
| Bench 4 | Bench Boost | Anthony Elanga | MID | 16 | 5.0 | 2.19 | 7.22 | 12.70 | 2.00 | 39.8 | 77.0 |