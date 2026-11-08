# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 234.43
- Total actual points: 283.00
- Average predicted points: 58.61
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
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.44
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.52 | 9.21 | 15.02 | 11.00 | 77.6 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.46 | 1.43 | 2.61 | 0.00 | 15.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.63 | 16.34 | 26.17 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.31 | 12.77 | 20.43 | 2.00 | 88.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.19 | 9.51 | 15.24 | 1.00 | 84.1 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.93 | 6.27 | 9.97 | 1.00 | 77.0 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.04 | 5.70 | 8.94 | 2.00 | 68.4 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.89 | 16.13 | 25.68 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.03 | 13.99 | 21.80 | 7.00 | 83.9 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.34 | 7.79 | 12.51 | 1.00 | 71.3 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.75 | 21.43 | 34.98 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.98 | 17.67 | 29.03 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.45 | 16.20 | 26.41 | 7.00 | 86.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.22 | 15.35 | 24.75 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.72 | 9.79 | 15.84 | 4.00 | 75.8 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.00
- Actual score: 43.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.13, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.97 | 10.72 | 17.58 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.51 | 1.43 | 2.66 | 0.00 | 13.1 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.48 | 13.44 | 21.71 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.87 | 12.69 | 21.20 | 0.00 | 71.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.42 | 9.56 | 15.50 | 17.00 | 86.7 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.40 | 6.46 | 10.43 | 1.00 | 74.7 | 79.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.74 | 5.66 | 9.16 | 0.00 | 72.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.07 | 17.13 | 27.04 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.22 | 12.89 | 20.32 | 2.00 | 66.7 | 90.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.29 | 6.68 | 10.99 | 1.00 | 51.1 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.42 | 19.69 | 30.92 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.16 | 17.56 | 26.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.05 | 14.51 | 23.38 | 2.00 | 88.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 3.06 | 11.49 | 21.96 | 0.00 | 32.2 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.84 | 8.78 | 13.94 | 2.00 | 70.4 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 56.50
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.06) beats the best remaining Triple Captain opportunity (6.86).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.65, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.06) beats the best remaining Triple Captain opportunity (6.86).
- Autosub: Chris Richards replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.44 | 9.50 | 15.82 | 3.00 | 80.2 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.50 | 1.38 | 2.69 | 0.00 | 12.9 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.38 | 12.75 | 20.92 | 1.00 | 82.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.92 | 10.76 | 17.40 | 2.00 | 82.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.21 | 8.92 | 14.44 | 2.00 | 68.9 | 90.0 |
| Bench 3 | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.21 | 8.73 | 15.76 | 1.00 | 26.4 | 22.0 |
| Bench 2 | Autosub In | Chris Richards | DEF | 8 | 3.9 | 2.37 | 6.13 | 10.11 | 1.00 | 75.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.16 | 14.96 | 24.21 | 7.00 | 79.8 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.43 | 12.98 | 20.55 | 13.00 | 63.3 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.94 | 5.94 | 10.26 | 1.00 | 43.8 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.06 | 17.06 | 27.22 | 10.00 | 79.7 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.38 | 13.00 | 24.04 | 0.00 | 21.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.00 | 12.28 | 20.91 | 1.00 | 65.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.65 | 12.11 | 19.27 | 6.00 | 45.0 | 76.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.75 | 8.40 | 13.89 | 1.00 | 70.3 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 56.49
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.26) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.26) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.13 | 9.49 | 15.50 | 1.00 | 82.4 | 45.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.82 | 1.66 | 0.00 | 8.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.05 | 12.00 | 19.69 | 1.00 | 80.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.96 | 10.34 | 17.55 | 1.00 | 51.0 | 57.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.42 | 10.21 | 16.55 | 1.00 | 82.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.98 | 9.69 | 15.59 | -1.00 | 81.0 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.06 | 6.08 | 9.84 | 0.00 | 74.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.80 | 16.28 | 26.27 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.87 | 13.30 | 22.01 | 2.00 | 67.9 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.34 | 4.47 | 8.34 | 1.00 | 30.6 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.56 | 16.69 | 26.79 | 9.00 | 85.1 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.29 | 12.87 | 21.27 | 20.00 | 64.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.47 | 12.83 | 22.10 | 0.00 | 33.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.91 | 11.90 | 20.54 | 2.00 | 72.0 | 90.0 |
| Bench 2 | Bench Boost | Alejandro Garnacho | MID | 14 | 4.8 | 2.87 | 9.00 | 14.29 | 16.00 | 68.4 | 90.0 |