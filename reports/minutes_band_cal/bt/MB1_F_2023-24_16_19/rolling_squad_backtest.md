# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 220.46
- Total actual points: 195.00
- Average predicted points: 55.11
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
- Predicted score: 58.58
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.25 | 9.21 | 14.79 | 9.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.28 | 0.47 | 0.82 | 0.00 | 4.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.47 | 13.22 | 22.15 | -1.00 | 82.5 | 85.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.43 | 10.56 | 17.19 | 5.00 | 76.0 | 90.0 |
| XI | XI | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.57 | 9.45 | 15.11 | 7.00 | 78.8 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.76 | 6.20 | 10.36 | 1.00 | 75.3 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.31 | 6.12 | 9.91 | 5.00 | 76.2 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 7.84 | 23.15 | 37.98 | 0.00 | 82.5 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.21 | 12.56 | 20.51 | 5.00 | 68.0 | 90.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.91 | 7.73 | 12.33 | 2.00 | 71.0 | 90.0 |
| Vice Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.32 | 18.98 | 31.69 | 13.00 | 82.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.9 | 5.18 | 15.87 | 26.06 | 2.00 | 82.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.56 | 13.24 | 21.34 | 2.00 | 82.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.08 | 12.30 | 19.57 | 2.00 | 80.4 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.81 | 11.52 | 19.24 | 1.00 | 79.3 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.92
- Actual score: 53.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Auston Trusty replaced Kieran Trippier.
- Autosub: Cameron Archer replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.23 | 9.86 | 15.87 | 3.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.00 | 0.20 | 0.35 | 0.00 | 5.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.22 | 11.84 | 19.31 | 8.00 | 82.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.36 | 10.05 | 18.04 | 0.00 | 64.4 | 0.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 3.30 | 9.75 | 15.74 | 0.00 | 81.2 | 0.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.20 | 6.55 | 10.38 | 1.00 | 77.1 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 3.89 | 7.47 | 0.00 | 0.0 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.06 | 14.38 | 22.64 | 2.00 | 83.1 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.48 | 14.02 | 25.97 | 0.00 | 31.6 | 0.0 |
| Bench 2 | Autosub In | Cameron Archer | FWD | 17 | 4.6 | 2.78 | 8.05 | 12.90 | 2.00 | 71.2 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 6.74 | 20.77 | 34.17 | 3.00 | 82.5 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.85 | 16.97 | 27.46 | 3.00 | 82.5 | 88.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.29 | 12.37 | 19.32 | 8.00 | 81.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.96 | 11.23 | 18.15 | 6.00 | 73.4 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.69 | 10.65 | 17.78 | 14.00 | 72.3 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 46.68
- Actual score: 45.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.09 | 8.79 | 14.64 | 1.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Tom McGill | GK | 5 | 3.9 | 0.27 | 0.64 | 1.05 | 0.00 | 7.4 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.36 | 12.60 | 19.34 | 2.00 | 80.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.85 | 11.72 | 19.91 | 2.00 | 64.1 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.99 | 6.39 | 10.31 | 1.00 | 79.3 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 1.58 | 4.78 | 7.72 | 5.00 | 50.1 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 9 | 4.5 | 0.82 | 3.96 | 7.24 | 1.00 | 33.2 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.85 | 27.46 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Julián Álvarez | FWD | 13 | 6.9 | 0.00 | 9.47 | 16.28 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 2.56 | 7.70 | 12.00 | 8.00 | 76.3 | 89.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 5.99 | 19.10 | 31.82 | 7.00 | 82.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.39 | 16.69 | 26.78 | 1.00 | 82.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.35 | 12.05 | 19.36 | 1.00 | 82.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 3.89 | 11.45 | 18.51 | 8.00 | 79.7 | 87.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.65 | 10.89 | 17.86 | 2.00 | 63.7 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 60.28
- Actual score: 37.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.05) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.05) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.05 | 8.89 | 14.77 | 0.00 | 82.4 | 90.0 |
| Bench 1 | Bench Boost | Tom McGill | GK | 5 | 3.9 | 0.27 | 0.65 | 1.16 | 0.00 | 9.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 4.94 | 13.43 | 22.05 | 1.00 | 79.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.96 | 11.91 | 18.82 | 5.00 | 81.4 | 90.0 |
| Bench 3 | Bench Boost | Vitalii Mykolenko | DEF | 9 | 4.5 | 2.45 | 7.73 | 12.64 | 1.00 | 75.1 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 2.55 | 6.90 | 10.79 | 1.00 | 81.0 | 90.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.42 | 6.52 | 10.43 | 1.00 | 70.6 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.46 | 11.03 | 21.05 | 0.00 | 24.1 | 0.0 |
| Bench 2 | Bench Boost | Julián Álvarez | FWD | 13 | 6.8 | 2.91 | 9.21 | 15.48 | 8.00 | 51.6 | 90.0 |
| XI | XI | Cameron Archer | FWD | 17 | 4.6 | 3.24 | 8.61 | 13.78 | 5.00 | 80.1 | 85.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.2 | 6.65 | 19.68 | 32.97 | 3.00 | 82.6 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.75 | 16.11 | 26.17 | 2.00 | 82.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.81 | 12.95 | 21.04 | 1.00 | 79.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 3.93 | 12.37 | 19.97 | 6.00 | 80.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.25 | 10.40 | 16.87 | 0.00 | 59.1 | 0.0 |