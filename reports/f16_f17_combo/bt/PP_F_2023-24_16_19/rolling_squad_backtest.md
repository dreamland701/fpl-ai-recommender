# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 239.36
- Total actual points: 161.00
- Average predicted points: 59.84
- Average actual points: 40.25
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
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 61.37
- Actual score: 30.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Charlie Taylor replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.38 | 9.56 | 15.52 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.10 | 0.20 | 0.00 | 4.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.16 | 15.15 | 24.93 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.79 | 14.35 | 23.69 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.58 | 10.78 | 17.61 | 5.00 | 77.9 | 90.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 4.0 | 2.40 | 7.30 | 11.33 | 1.00 | 71.4 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.65 | 5.84 | 9.84 | 1.00 | 70.6 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.41 | 24.59 | 39.89 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.63 | 14.63 | 24.42 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.69 | 4.29 | 6.51 | 0.00 | 37.2 | 52.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 5.82 | 17.61 | 28.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.90 | 13.71 | 23.07 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.62 | 13.39 | 21.68 | 2.00 | 88.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.07 | 12.27 | 19.59 | 2.00 | 78.1 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.59 | 10.77 | 17.99 | 1.00 | 76.5 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.34
- Actual score: 64.00
- Transfer: none
- No transfer was applied this week.
- Autosub: William Osula replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.34 | 10.26 | 16.59 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.28 | 0.29 | 0.33 | 0.00 | 5.1 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.70 | 14.80 | 24.26 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.83 | 13.51 | 21.50 | 8.00 | 90.0 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 6.9 | 3.43 | 10.29 | 18.36 | 0.00 | 65.8 | 0.0 |
| Bench 2 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.75 | 5.11 | 8.39 | 0.00 | 57.2 | 0.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 4.89 | 8.67 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.83 | 17.35 | 28.25 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.60 | 14.12 | 25.98 | 0.00 | 34.2 | 0.0 |
| Bench 3 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.39 | 4.33 | 6.70 | 1.00 | 36.3 | 32.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.44 | 18.66 | 29.74 | 3.00 | 90.0 | 88.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.47 | 12.83 | 20.16 | 8.00 | 84.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.85 | 10.89 | 17.45 | 6.00 | 69.2 | 83.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.3 | 2.90 | 10.79 | 18.26 | 0.00 | 66.7 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.51 | 9.98 | 16.46 | 14.00 | 65.9 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 61.97
- Actual score: 34.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.30) beats the best remaining Triple Captain opportunity (7.85).
- Transfer: Bruno Borges Fernandes -> Dejan Kulusevski (projected gain 2.58, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (6.30) beats the best remaining Triple Captain opportunity (7.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.77 | 10.75 | 17.40 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.23 | 0.49 | 0.49 | 0.00 | 5.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.40 | 14.20 | 23.59 | 5.00 | 86.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.52 | 12.98 | 20.00 | 2.00 | 82.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 3.93 | 11.99 | 20.25 | 2.00 | 65.5 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 1.28 | 3.92 | 6.31 | 5.00 | 42.8 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.20 | 3.84 | 6.72 | 6.00 | 43.6 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.99 | 19.06 | 29.72 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.29 | 26.35 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | William Osula | FWD | 17 | 4.3 | 1.23 | 4.10 | 6.61 | 0.00 | 35.2 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.95 | 18.35 | 29.12 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.51 | 13.18 | 20.88 | 8.00 | 90.0 | 87.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 7.2 | 4.55 | 13.16 | 21.18 | 1.00 | 84.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.66 | 12.82 | 20.12 | 1.00 | 88.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.42 | 10.22 | 16.74 | 2.00 | 57.8 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Trent Alexander-Arnold
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 61.70
- Actual score: 33.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.88) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Pascal Groß (projected gain 3.08, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.88) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.15 | 9.31 | 15.55 | 0.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.39 | 0.68 | 0.85 | 0.00 | 7.6 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.20 | 15.95 | 25.79 | 8.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.9 | 5.02 | 13.94 | 23.05 | 1.00 | 86.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.08 | 12.21 | 19.40 | 5.00 | 83.2 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.10 | 6.12 | 9.96 | 1.00 | 68.4 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.22 | 5.90 | 9.30 | 1.00 | 64.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.87 | 14.99 | 23.85 | 2.00 | 81.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.56 | 11.09 | 20.99 | 0.00 | 26.6 | 0.0 |
| Bench 4 | Bench Boost | William Osula | FWD | 17 | 4.3 | 1.16 | 3.00 | 5.01 | 1.00 | 23.6 | 4.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.32 | 17.76 | 28.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.51 | 14.05 | 22.37 | 6.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.67 | 12.72 | 20.73 | 1.00 | 79.4 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.4 | 4.18 | 12.28 | 20.33 | 2.00 | 85.8 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 7.2 | 3.95 | 12.16 | 19.87 | 1.00 | 78.1 | 90.0 |