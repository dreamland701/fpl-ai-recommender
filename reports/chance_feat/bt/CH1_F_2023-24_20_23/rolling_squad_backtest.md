# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 233.75
- Total actual points: 298.00
- Average predicted points: 58.44
- Average actual points: 74.50
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
- Predicted score: 63.07
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.53 | 9.22 | 15.00 | 11.00 | 77.1 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.39 | 1.16 | 2.10 | 0.00 | 14.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.59 | 16.20 | 25.96 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.32 | 12.81 | 20.49 | 2.00 | 88.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.19 | 9.51 | 15.25 | 1.00 | 84.2 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.92 | 6.25 | 9.93 | 1.00 | 77.0 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.98 | 5.53 | 9.07 | 1.00 | 61.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.85 | 15.98 | 25.43 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.04 | 14.06 | 21.92 | 7.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.36 | 7.75 | 12.37 | 1.00 | 70.5 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.63 | 21.05 | 34.37 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.92 | 17.49 | 28.74 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.45 | 16.17 | 26.33 | 7.00 | 85.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.19 | 15.30 | 24.70 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.72 | 9.78 | 15.80 | 4.00 | 76.0 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.73
- Actual score: 44.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.29, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.99 | 10.74 | 17.59 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.42 | 1.12 | 2.07 | 0.00 | 11.8 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.50 | 13.51 | 21.84 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.83 | 12.53 | 20.90 | 0.00 | 71.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.43 | 9.56 | 15.51 | 17.00 | 86.7 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.40 | 6.43 | 10.37 | 1.00 | 74.6 | 79.0 |
| Bench 3 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.31 | 6.19 | 10.26 | 2.00 | 70.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.03 | 16.99 | 26.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.21 | 12.81 | 20.17 | 2.00 | 66.4 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.30 | 6.59 | 10.75 | 1.00 | 50.1 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.42 | 19.68 | 30.91 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.17 | 17.69 | 27.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.02 | 14.42 | 23.27 | 2.00 | 88.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.89 | 10.68 | 20.39 | 0.00 | 30.4 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.84 | 8.73 | 13.86 | 2.00 | 70.7 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 57.14
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.96) beats the best remaining Bench Boost opportunity (7.61).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.47, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.96) beats the best remaining Bench Boost opportunity (7.61).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.45 | 9.50 | 15.78 | 3.00 | 79.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.41 | 1.07 | 2.09 | 0.00 | 11.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.38 | 12.76 | 20.92 | 1.00 | 82.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.95 | 10.75 | 17.32 | 2.00 | 82.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.32 | 9.81 | 16.25 | 2.00 | 71.6 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.23 | 9.08 | 16.53 | 1.00 | 27.7 | 22.0 |
| Bench 2 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.38 | 6.30 | 10.37 | 6.00 | 71.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.11 | 14.77 | 23.88 | 7.00 | 79.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.43 | 12.90 | 20.37 | 13.00 | 63.0 | 86.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.4 | 1.94 | 5.87 | 10.08 | 1.00 | 43.0 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.02 | 16.89 | 26.90 | 10.00 | 79.3 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.1 | 3.22 | 12.27 | 22.69 | 0.00 | 20.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.93 | 12.05 | 20.53 | 1.00 | 65.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.62 | 11.95 | 18.95 | 6.00 | 44.5 | 76.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.74 | 8.34 | 13.77 | 1.00 | 70.5 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 55.81
- Actual score: 106.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.76) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (5.76) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Alejandro Garnacho replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.14 | 9.53 | 15.55 | 1.00 | 82.1 | 45.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.54 | 1.11 | 0.00 | 6.7 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.06 | 12.01 | 19.69 | 1.00 | 80.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.93 | 10.24 | 17.37 | 1.00 | 50.8 | 57.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.47 | 10.23 | 16.53 | 1.00 | 81.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.98 | 9.70 | 15.62 | -1.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.18 | 6.73 | 10.77 | 0.00 | 71.1 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.76 | 16.14 | 26.02 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.87 | 13.21 | 21.78 | 2.00 | 67.5 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.3 | 1.33 | 4.41 | 8.17 | 1.00 | 29.8 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.55 | 16.57 | 26.55 | 9.00 | 84.7 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.31 | 12.87 | 21.25 | 20.00 | 64.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.0 | 3.36 | 12.35 | 21.21 | 0.00 | 32.2 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.87 | 11.77 | 20.31 | 2.00 | 72.0 | 90.0 |
| Bench 2 | Autosub In | Alejandro Garnacho | MID | 14 | 4.8 | 2.87 | 8.99 | 14.28 | 16.00 | 68.7 | 90.0 |