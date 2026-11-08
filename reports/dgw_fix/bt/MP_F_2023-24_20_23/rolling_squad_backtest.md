# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 234.05
- Total actual points: 295.00
- Average predicted points: 58.51
- Average actual points: 73.75
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
- Predicted score: 63.23
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.59 | 9.89 | 16.30 | 11.00 | 78.4 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.16 | 0.69 | 1.27 | 0.00 | 9.3 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.52 | 15.31 | 24.75 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.39 | 12.62 | 20.39 | 2.00 | 89.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.14 | 9.51 | 15.34 | 1.00 | 83.0 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.90 | 6.06 | 9.64 | 1.00 | 76.6 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.95 | 5.33 | 8.71 | 1.00 | 61.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.91 | 16.31 | 26.33 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.12 | 13.65 | 21.49 | 7.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.37 | 7.33 | 11.90 | 1.00 | 70.8 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.61 | 21.45 | 35.13 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.95 | 17.88 | 29.69 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.52 | 16.41 | 26.91 | 7.00 | 87.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.17 | 14.95 | 24.35 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.70 | 9.31 | 15.14 | 4.00 | 75.5 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 58.18
- Actual score: 44.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.59, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 4.12 | 11.37 | 18.54 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.23 | 0.92 | 2.20 | 0.00 | 7.6 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.63 | 13.42 | 21.72 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.62 | 11.81 | 24.09 | 0.00 | 66.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.43 | 9.71 | 15.56 | 17.00 | 86.7 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.37 | 6.34 | 10.08 | 1.00 | 74.1 | 79.0 |
| Bench 3 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.31 | 6.21 | 12.27 | 2.00 | 70.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.07 | 17.16 | 27.37 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.20 | 11.86 | 22.63 | 2.00 | 66.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.22 | 6.30 | 10.25 | 1.00 | 48.4 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.57 | 19.94 | 31.54 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.29 | 16.91 | 31.13 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.96 | 14.02 | 22.48 | 2.00 | 87.4 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.93 | 11.98 | 26.91 | 0.00 | 31.3 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.80 | 8.26 | 13.13 | 2.00 | 70.0 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 56.92
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.75) beats the best remaining Bench Boost opportunity (7.40).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.75) beats the best remaining Bench Boost opportunity (7.40).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.52 | 9.87 | 15.86 | 3.00 | 81.4 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.18 | 0.78 | 1.66 | 0.00 | 6.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.44 | 12.36 | 15.98 | 1.00 | 84.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.98 | 10.83 | 17.40 | 2.00 | 82.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.72 | 9.86 | 15.79 | 2.00 | 80.3 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.27 | 8.05 | 14.53 | 1.00 | 28.7 | 22.0 |
| Bench 2 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.37 | 6.28 | 10.16 | 6.00 | 71.7 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.09 | 14.92 | 24.18 | 7.00 | 79.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.42 | 11.83 | 22.65 | 13.00 | 62.7 | 86.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.4 | 1.92 | 5.59 | 9.57 | 1.00 | 42.7 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.08 | 16.65 | 26.47 | 10.00 | 80.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.75 | 11.00 | 18.07 | 1.00 | 61.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.47 | 10.43 | 19.34 | 6.00 | 41.3 | 76.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.1 | 2.93 | 9.96 | 18.62 | 0.00 | 14.1 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.68 | 7.96 | 12.88 | 1.00 | 69.1 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 55.72
- Actual score: 103.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.79) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Alejandro Garnacho -> Ross Barkley (projected gain 2.19, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (5.79) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Trent Alexander-Arnold replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.19 | 9.60 | 15.33 | 1.00 | 83.1 | 45.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.00 | 0.26 | 0.00 | 1.3 | 0.0 |
| Bench 2 | Autosub In | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.74 | 12.92 | 16.77 | 1.00 | 46.6 | 57.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.12 | 11.97 | 15.81 | 1.00 | 82.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.47 | 10.47 | 17.21 | 1.00 | 81.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.94 | 9.54 | 15.60 | -1.00 | 80.1 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.14 | 8.37 | 10.09 | 0.00 | 70.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.86 | 16.53 | 25.00 | 2.00 | 67.2 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.79 | 16.07 | 25.98 | 18.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.3 | 1.31 | 4.72 | 8.54 | 1.00 | 29.3 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.59 | 16.85 | 27.51 | 9.00 | 85.8 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.21 | 16.18 | 23.93 | 20.00 | 62.3 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.0 | 3.44 | 16.00 | 20.64 | 0.00 | 33.9 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.78 | 11.36 | 19.51 | 2.00 | 70.0 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.9 | 2.76 | 10.90 | 13.69 | 13.00 | 68.9 | 90.0 |