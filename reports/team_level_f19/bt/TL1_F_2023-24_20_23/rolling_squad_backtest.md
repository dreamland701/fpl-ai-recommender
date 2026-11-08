# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 234.49
- Total actual points: 283.00
- Average predicted points: 58.62
- Average actual points: 70.75
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
- Vice captain: Ollie Watkins
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.36
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.58 | 9.22 | 14.92 | 11.00 | 78.1 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.44 | 1.13 | 2.01 | 0.00 | 15.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.63 | 16.26 | 26.00 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.22 | 12.62 | 20.24 | 2.00 | 88.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.23 | 9.58 | 15.43 | 1.00 | 85.4 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.02 | 6.36 | 9.95 | 1.00 | 78.3 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.09 | 5.75 | 8.90 | 2.00 | 68.4 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.94 | 15.85 | 25.26 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.18 | 14.08 | 22.10 | 7.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.45 | 7.89 | 12.44 | 1.00 | 71.6 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.68 | 21.12 | 34.43 | 16.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.81 | 17.30 | 28.49 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.48 | 16.24 | 26.53 | 7.00 | 86.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.21 | 15.28 | 24.61 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.71 | 10.01 | 16.12 | 4.00 | 76.6 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.96
- Actual score: 43.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.50, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.11 | 10.58 | 17.36 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.30 | 0.80 | 1.59 | 0.00 | 13.1 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.49 | 13.44 | 21.74 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.72 | 12.30 | 20.62 | 0.00 | 72.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.44 | 9.63 | 15.66 | 17.00 | 87.7 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.32 | 6.32 | 10.06 | 1.00 | 76.0 | 79.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.85 | 5.85 | 9.33 | 0.00 | 72.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.94 | 16.80 | 26.51 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.29 | 13.11 | 20.64 | 2.00 | 66.8 | 90.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.23 | 6.54 | 10.55 | 1.00 | 51.6 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.41 | 19.74 | 30.99 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.24 | 17.79 | 27.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.12 | 14.26 | 23.06 | 2.00 | 88.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.84 | 10.83 | 20.97 | 0.00 | 32.7 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.93 | 9.09 | 14.38 | 2.00 | 71.2 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.18
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.99) beats the best remaining Triple Captain opportunity (6.79).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.66, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.99) beats the best remaining Triple Captain opportunity (6.79).
- Autosub: Chris Richards replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.38 | 9.35 | 15.64 | 3.00 | 81.1 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.36 | 0.82 | 1.71 | 0.00 | 12.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.39 | 12.77 | 20.93 | 1.00 | 83.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.93 | 10.72 | 17.35 | 2.00 | 83.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.18 | 8.85 | 14.40 | 2.00 | 70.0 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.12 | 8.40 | 15.29 | 1.00 | 27.2 | 22.0 |
| Bench 2 | Autosub In | Chris Richards | DEF | 8 | 3.9 | 2.50 | 6.11 | 10.02 | 1.00 | 75.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.16 | 14.88 | 24.00 | 7.00 | 80.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.57 | 12.98 | 20.51 | 13.00 | 63.2 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.85 | 5.70 | 9.81 | 1.00 | 44.4 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.99 | 16.95 | 27.03 | 10.00 | 80.1 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.18 | 12.38 | 23.10 | 0.00 | 21.8 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.78 | 12.08 | 19.17 | 6.00 | 44.8 | 76.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.86 | 11.98 | 20.54 | 1.00 | 66.1 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.77 | 8.56 | 14.13 | 1.00 | 71.2 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 57.00
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.33) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.33) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.16 | 9.51 | 15.57 | 1.00 | 82.9 | 45.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.47 | 0.95 | 0.00 | 7.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.99 | 11.89 | 19.55 | 1.00 | 81.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.55 | 10.48 | 16.81 | 1.00 | 82.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.99 | 10.28 | 17.42 | 1.00 | 51.4 | 57.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.07 | 9.91 | 15.83 | -1.00 | 81.5 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.11 | 6.18 | 9.91 | 0.00 | 74.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.83 | 16.04 | 25.85 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.92 | 13.46 | 22.16 | 2.00 | 68.1 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.29 | 4.35 | 8.05 | 1.00 | 30.9 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.64 | 16.82 | 26.87 | 9.00 | 85.2 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.37 | 13.04 | 21.45 | 20.00 | 65.2 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.44 | 12.57 | 21.67 | 0.00 | 33.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.88 | 11.82 | 20.49 | 2.00 | 72.7 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.92 | 9.18 | 14.52 | 16.00 | 69.2 | 90.0 |