# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 219.69
- Total actual points: 195.00
- Average predicted points: 54.92
- Average actual points: 48.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 114791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.19
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.09 | 8.96 | 14.47 | 9.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.33 | 0.56 | 0.93 | 0.00 | 5.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.51 | 13.40 | 22.26 | -1.00 | 82.7 | 85.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.48 | 10.63 | 17.39 | 5.00 | 75.3 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.41 | 9.20 | 14.79 | 7.00 | 77.6 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.81 | 6.27 | 10.56 | 1.00 | 74.6 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.35 | 6.20 | 10.11 | 5.00 | 75.4 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 7.88 | 23.33 | 38.09 | 0.00 | 82.7 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.19 | 12.53 | 20.49 | 5.00 | 68.0 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.89 | 7.71 | 12.31 | 2.00 | 71.1 | 90.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.36 | 19.16 | 31.80 | 13.00 | 82.7 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.22 | 16.06 | 26.17 | 2.00 | 82.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.39 | 13.00 | 21.01 | 2.00 | 81.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.12 | 12.38 | 19.77 | 2.00 | 79.7 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.65 | 11.27 | 18.91 | 1.00 | 78.2 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.55
- Actual score: 53.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.05 | 9.61 | 15.52 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.29 | 0.46 | 0.00 | 6.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.27 | 12.02 | 19.39 | 8.00 | 82.2 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.26 | 9.81 | 17.56 | 0.00 | 60.9 | 0.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.13 | 9.50 | 15.39 | 0.00 | 80.0 | 0.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.24 | 6.62 | 10.59 | 1.00 | 76.3 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 4.07 | 7.55 | 0.00 | 0.0 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.89 | 14.13 | 22.30 | 2.00 | 81.9 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.54 | 14.11 | 26.04 | 0.00 | 32.6 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.76 | 8.04 | 12.88 | 2.00 | 71.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.79 | 20.94 | 34.26 | 3.00 | 82.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.89 | 17.15 | 27.54 | 3.00 | 82.7 | 88.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.33 | 12.44 | 19.54 | 8.00 | 80.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.94 | 11.22 | 18.14 | 6.00 | 73.5 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.67 | 10.64 | 17.77 | 14.00 | 72.4 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 46.87
- Actual score: 45.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.13 | 8.93 | 14.74 | 1.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.32 | 0.73 | 1.16 | 0.00 | 8.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.39 | 12.65 | 19.52 | 2.00 | 79.3 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.83 | 11.70 | 19.88 | 2.00 | 64.0 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 2.02 | 6.44 | 10.48 | 1.00 | 78.6 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 1.63 | 4.94 | 7.92 | 5.00 | 52.0 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 0.88 | 4.06 | 7.33 | 1.00 | 34.2 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.61 | 26.97 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Julián Álvarez | FWD | 13 | 6.9 | 0.00 | 9.61 | 16.37 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.59 | 7.74 | 12.17 | 8.00 | 75.7 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.03 | 19.24 | 31.91 | 7.00 | 82.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.43 | 16.83 | 26.88 | 1.00 | 82.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.39 | 12.19 | 19.46 | 1.00 | 82.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 3.93 | 11.59 | 18.61 | 8.00 | 79.8 | 87.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.47 | 10.39 | 17.05 | 2.00 | 59.1 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.08
- Actual score: 37.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.17) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.17) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 2.87 | 8.64 | 14.42 | 0.00 | 81.4 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.31 | 0.74 | 1.27 | 0.00 | 10.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.76 | 13.18 | 21.70 | 1.00 | 78.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.99 | 11.98 | 19.02 | 5.00 | 80.6 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.5 | 2.49 | 7.80 | 12.84 | 1.00 | 74.3 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 2.59 | 6.97 | 10.99 | 1.00 | 80.2 | 90.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.40 | 6.51 | 10.40 | 1.00 | 70.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.51 | 11.13 | 21.13 | 0.00 | 25.1 | 0.0 |
| Bench 2 | Bench Boost | Julián Álvarez | FWD | 13 | 6.8 | 2.96 | 9.35 | 15.65 | 8.00 | 53.5 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.28 | 8.69 | 13.98 | 5.00 | 79.3 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.71 | 19.83 | 33.07 | 3.00 | 82.7 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.81 | 16.26 | 26.27 | 2.00 | 82.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.63 | 12.70 | 20.69 | 1.00 | 78.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 3.99 | 12.52 | 20.07 | 6.00 | 80.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.07 | 9.91 | 16.08 | 0.00 | 54.4 | 0.0 |