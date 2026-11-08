# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 231.23
- Total actual points: 282.00
- Average predicted points: 57.81
- Average actual points: 70.50
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
- Predicted score: 62.71
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.41 | 8.95 | 14.41 | 11.00 | 73.8 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.42 | 1.30 | 2.29 | 0.00 | 11.8 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.81 | 16.82 | 26.98 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.40 | 12.97 | 20.65 | 2.00 | 89.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.09 | 9.41 | 15.14 | 1.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.98 | 6.28 | 9.99 | 1.00 | 78.3 | 90.0 |
| Bench 4 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.94 | 5.45 | 8.85 | 1.00 | 62.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.72 | 15.67 | 24.77 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.98 | 13.46 | 20.86 | 7.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.41 | 7.66 | 12.12 | 1.00 | 69.6 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.60 | 21.22 | 34.71 | 16.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.81 | 17.29 | 28.45 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.38 | 16.28 | 26.41 | 7.00 | 84.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.08 | 14.96 | 24.12 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.82 | 9.88 | 15.97 | 4.00 | 78.0 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.35
- Actual score: 43.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.96, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Cameron Archer replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.81 | 10.27 | 16.67 | 3.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.48 | 1.37 | 2.45 | 0.00 | 9.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.56 | 13.38 | 21.54 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.91 | 13.24 | 22.05 | 0.00 | 74.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.42 | 9.64 | 15.57 | 17.00 | 88.8 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.41 | 6.40 | 10.32 | 1.00 | 76.0 | 79.0 |
| Bench 4 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.29 | 6.18 | 10.22 | 2.00 | 71.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.90 | 16.41 | 25.65 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.13 | 12.17 | 19.20 | 2.00 | 65.8 | 90.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 17 | 4.5 | 2.34 | 6.59 | 10.56 | 1.00 | 48.9 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.41 | 19.48 | 30.40 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.25 | 17.33 | 26.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.93 | 14.03 | 22.54 | 2.00 | 89.3 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.78 | 11.43 | 21.96 | 0.00 | 31.2 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.85 | 8.84 | 14.02 | 2.00 | 72.9 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 55.20
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.94) beats the best remaining Triple Captain opportunity (6.73).
- Transfer: Alejandro Garnacho -> Pascal Groß (projected gain 2.85, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.94) beats the best remaining Triple Captain opportunity (6.73).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.28 | 8.92 | 14.69 | 3.00 | 77.6 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.50 | 1.27 | 2.36 | 0.00 | 9.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.40 | 12.42 | 20.33 | 1.00 | 84.9 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.42 | 8.98 | 16.11 | 1.00 | 30.5 | 22.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.26 | 8.65 | 14.20 | 2.00 | 70.8 | 90.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.42 | 6.27 | 10.30 | 6.00 | 73.2 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.18 | 6.19 | 10.00 | 0.00 | 70.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 4.98 | 14.35 | 22.87 | 7.00 | 78.3 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.35 | 12.54 | 19.88 | 13.00 | 62.5 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.94 | 5.61 | 9.53 | 1.00 | 41.8 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.94 | 16.49 | 26.17 | 10.00 | 79.1 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.61 | 12.69 | 22.99 | 0.00 | 25.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.02 | 11.61 | 19.68 | 1.00 | 68.3 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.50 | 11.36 | 18.28 | 6.00 | 47.8 | 76.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.56 | 11.17 | 18.23 | 2.00 | 72.5 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 55.97
- Actual score: 83.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.91) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.91) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.98 | 8.88 | 14.39 | 1.00 | 78.8 | 45.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.67 | 1.29 | 0.00 | 4.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.01 | 11.84 | 19.37 | 1.00 | 82.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.09 | 10.67 | 18.01 | 1.00 | 53.4 | 57.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.95 | 9.60 | 15.45 | -1.00 | 83.8 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.15 | 6.45 | 10.43 | 0.00 | 72.1 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.35 | 6.31 | 10.06 | 0.00 | 74.3 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.60 | 15.56 | 24.73 | 18.00 | 89.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.78 | 12.69 | 21.09 | 2.00 | 66.2 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.41 | 4.43 | 8.08 | 1.00 | 28.5 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.51 | 16.51 | 26.28 | 9.00 | 84.0 | 78.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.59 | 12.99 | 22.10 | 0.00 | 35.9 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.32 | 12.81 | 21.05 | 20.00 | 64.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.85 | 11.56 | 19.91 | 2.00 | 73.1 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.77 | 11.37 | 18.51 | 11.00 | 78.2 | 90.0 |