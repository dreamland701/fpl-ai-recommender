# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 239.34
- Total actual points: 171.00
- Average predicted points: 59.84
- Average actual points: 42.75
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
- Predicted score: 62.04
- Actual score: 30.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Charlie Taylor replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.47 | 9.70 | 15.64 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.00 | 0.00 | 0.00 | 1.00 | 1.0 | 3.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.22 | 15.26 | 25.04 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.85 | 14.43 | 23.76 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.64 | 10.88 | 17.69 | 5.00 | 79.7 | 90.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 4.0 | 2.45 | 7.38 | 11.40 | 1.00 | 72.7 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.71 | 5.94 | 9.93 | 1.00 | 72.4 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.45 | 24.64 | 39.92 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.68 | 14.71 | 24.50 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | William Osula | FWD | 17 | 4.3 | 1.79 | 4.45 | 6.69 | 0.00 | 40.1 | 52.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 5.86 | 17.69 | 28.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.94 | 13.78 | 23.14 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.70 | 13.52 | 21.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.11 | 12.33 | 19.64 | 2.00 | 79.2 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.66 | 10.89 | 18.13 | 1.00 | 78.7 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.76
- Actual score: 71.00
- Transfer: Kieran Trippier -> William Saliba (projected gain 2.42, hit 0)
- Autosub: William Osula replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.43 | 10.40 | 16.71 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.04 | 0.87 | 1.33 | 0.00 | 12.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.75 | 14.90 | 24.34 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.75 | 13.36 | 21.42 | 8.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.19 | 11.74 | 18.44 | 7.00 | 87.7 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.00 | 4.97 | 8.64 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.31 | 4.08 | 7.13 | 0.00 | 46.4 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.87 | 17.42 | 28.30 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.53 | 14.43 | 26.78 | 0.00 | 32.6 | 0.0 |
| Bench 2 | Autosub In | William Osula | FWD | 17 | 4.3 | 1.48 | 4.46 | 6.81 | 1.00 | 38.7 | 32.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.48 | 18.73 | 29.78 | 3.00 | 90.0 | 88.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.52 | 12.90 | 20.18 | 8.00 | 85.5 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.71 | 11.07 | 18.13 | 6.00 | 66.0 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.58 | 10.09 | 16.57 | 14.00 | 68.1 | 90.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.3 | 2.47 | 9.78 | 17.01 | 0.00 | 56.0 | 0.0 |

## GW18

- Train rows: 116314
- Bank: 1.40 -> -0.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 61.59
- Actual score: 30.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.21) beats the best remaining Triple Captain opportunity (7.75).
- Transfer: William Osula -> Matheus Santos Carneiro Da Cunha (projected gain 6.83, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (6.21) beats the best remaining Triple Captain opportunity (7.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.71 | 10.68 | 17.38 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Remi Matthews | GK | 8 | 3.9 | 0.45 | 0.83 | 1.20 | 0.00 | 9.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.32 | 14.12 | 23.57 | 5.00 | 84.8 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.43 | 12.86 | 19.90 | 2.00 | 80.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.56 | 11.00 | 17.58 | 2.00 | 88.5 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.25 | 3.90 | 6.36 | 5.00 | 42.9 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.17 | 3.82 | 6.75 | 6.00 | 43.5 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.90 | 18.93 | 29.61 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.40 | 26.43 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.63 | 10.48 | 16.87 | 1.00 | 75.9 | 85.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.87 | 18.25 | 29.05 | 1.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.42 | 13.06 | 20.79 | 8.00 | 89.5 | 87.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.55 | 12.66 | 20.01 | 1.00 | 86.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.06 | 10.62 | 18.15 | 1.00 | 55.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.34 | 10.14 | 16.71 | 2.00 | 56.1 | 90.0 |

## GW19

- Train rows: 117083
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Trent Alexander-Arnold
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 60.96
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.53) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cole Palmer -> Dwight McNeil (projected gain 0.03, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.53) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.7 | 3.10 | 9.26 | 15.56 | 0.00 | 89.2 | 90.0 |
| Bench 1 | Bench Boost | Remi Matthews | GK | 8 | 3.9 | 0.24 | 0.81 | 1.21 | 0.00 | 10.2 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.10 | 15.83 | 25.71 | 8.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.00 | 12.10 | 19.33 | 5.00 | 81.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.25 | 11.54 | 18.37 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.05 | 6.07 | 9.96 | 1.00 | 67.7 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.16 | 5.85 | 9.29 | 1.00 | 63.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.80 | 14.91 | 23.79 | 2.00 | 79.6 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.61 | 11.24 | 21.22 | 0.00 | 28.5 | 0.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.7 | 3.19 | 9.63 | 15.68 | 5.00 | 68.8 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.24 | 17.66 | 28.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.44 | 13.95 | 22.30 | 6.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.58 | 12.60 | 20.65 | 1.00 | 77.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.91 | 11.95 | 19.87 | 1.00 | 76.6 | 90.0 |
| Bench 2 | Bench Boost | Dwight McNeil | MID | 9 | 5.4 | 3.08 | 9.93 | 16.06 | 5.00 | 80.9 | 90.0 |