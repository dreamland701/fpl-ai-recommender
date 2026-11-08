# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 221.60
- Total actual points: 159.00
- Average predicted points: 55.40
- Average actual points: 39.75
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
- Predicted score: 60.70
- Actual score: 26.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Alejandro Garnacho replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Sánchez | GK | 7 | 4.6 | 3.66 | 9.94 | 16.78 | 3.00 | 90.0 | 83.0 |
| Bench 1 | Bench | Andy Lonergan | GK | 9 | 3.9 | 0.00 | 0.00 | 0.00 | 0.00 | 0.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.72 | 13.88 | 22.03 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.74 | 13.47 | 22.42 | 4.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.97 | 11.18 | 17.89 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.24 | 7.27 | 11.10 | 1.00 | 70.9 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.04 | 5.49 | 8.84 | 5.00 | 72.1 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 7.17 | 22.17 | 36.11 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.22 | 14.36 | 23.43 | 2.00 | 85.3 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 5.47 | 14.23 | 25.11 | 5.00 | 78.1 | 90.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 5.81 | 17.45 | 27.94 | 2.00 | 89.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.19 | 14.53 | 24.25 | 1.00 | 87.8 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.51 | 13.09 | 20.44 | 2.00 | 79.9 | 73.0 |
| XI | XI | Scott McTominay | MID | 14 | 4.9 | 4.07 | 10.75 | 16.77 | 2.00 | 80.6 | 90.0 |
| Bench 2 | Autosub In | Alejandro Garnacho | MID | 14 | 4.8 | 3.79 | 9.91 | 15.66 | 2.00 | 65.9 | 78.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 51.98
- Actual score: 52.00
- Transfer: Kieran Trippier -> William Saliba (projected gain 4.28, hit 0)
- Autosub: Alejandro Garnacho replaced Bruno Borges Fernandes.
- Autosub: Auston Trusty replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Robert Sánchez | GK | 7 | 4.6 | 2.11 | 7.96 | 13.80 | 0.00 | 66.2 | 0.0 |
| Bench 1 | Bench | Andy Lonergan | GK | 9 | 3.9 | 0.05 | 0.00 | 0.06 | 0.00 | 0.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 5.02 | 16.38 | 26.54 | 9.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.66 | 11.81 | 18.69 | 6.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.02 | 10.99 | 17.21 | 7.00 | 86.9 | 90.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 1.94 | 5.98 | 9.46 | 1.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.79 | 4.53 | 7.31 | 0.00 | 52.5 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.26 | 17.07 | 26.86 | 9.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.03 | 15.90 | 27.30 | 2.00 | 89.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 3.79 | 13.55 | 24.36 | 0.00 | 29.5 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.42 | 18.52 | 29.08 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.26 | 11.89 | 18.76 | 6.00 | 70.6 | 83.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.3 | 2.91 | 11.21 | 18.64 | 0.00 | 64.4 | 0.0 |
| XI | XI | Scott McTominay | MID | 14 | 4.9 | 3.06 | 10.06 | 15.09 | 3.00 | 75.8 | 90.0 |
| Bench 2 | Autosub In | Alejandro Garnacho | MID | 14 | 4.8 | 2.50 | 8.42 | 13.14 | 3.00 | 58.9 | 70.0 |

## GW18

- Train rows: 116314
- Bank: 1.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 49.81
- Actual score: 30.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (0.56) beats the best remaining Bench Boost opportunity (2.34).
- Transfer: Andy Lonergan -> Emiliano Martínez Romero (projected gain 8.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (0.56) beats the best remaining Bench Boost opportunity (2.34).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.79 | 11.85 | 18.40 | 2.00 | 88.9 | 90.0 |
| Bench 1 | Bench Boost | Robert Sánchez | GK | 7 | 4.6 | 0.76 | 3.58 | 7.45 | 0.00 | 33.5 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.58 | 14.94 | 24.91 | 5.00 | 87.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.26 | 11.11 | 17.80 | 2.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.40 | 10.84 | 16.96 | 2.00 | 90.0 | 90.0 |
| XI | XI | Auston Trusty | DEF | 17 | 3.9 | 1.68 | 5.66 | 9.23 | 1.00 | 76.7 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 1.17 | 3.23 | 5.96 | 6.00 | 43.5 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.35 | 17.79 | 27.58 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Julián Álvarez | FWD | 13 | 6.9 | 0.00 | 15.26 | 26.07 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench Boost | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 12.69 | 23.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.93 | 18.07 | 28.85 | 1.00 | 87.4 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 2.83 | 11.21 | 18.69 | 1.00 | 52.5 | 90.0 |
| XI | XI | Scott McTominay | MID | 14 | 4.9 | 3.42 | 10.99 | 16.80 | 2.00 | 82.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.64 | 10.96 | 17.56 | 2.00 | 58.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.65 | 8.73 | 13.93 | 2.00 | 58.1 | 84.0 |

## GW19

- Train rows: 117083
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Trent Alexander-Arnold
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 59.11
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.02) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Robert Sánchez -> Jordan Pickford (projected gain 0.75, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.02) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Scott McTominay replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.4 | 3.24 | 10.73 | 17.22 | 2.00 | 77.0 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.76 | 10.05 | 16.12 | 2.00 | 78.6 | 90.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 6.00 | 17.00 | 27.11 | 8.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.33 | 11.93 | 18.47 | 1.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.1 | 3.71 | 10.78 | 17.68 | 7.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.38 | 6.24 | 9.85 | 1.00 | 77.6 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.90 | 5.54 | 9.09 | 1.00 | 68.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.45 | 14.01 | 22.68 | 2.00 | 78.8 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 3.62 | 12.70 | 21.88 | 8.00 | 52.5 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 13.9 | 3.78 | 11.42 | 21.05 | 0.00 | 23.3 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.02 | 17.70 | 27.92 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 5.07 | 13.15 | 21.42 | 1.00 | 79.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.81 | 11.53 | 19.26 | 1.00 | 70.2 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.7 | 3.04 | 8.95 | 14.15 | 14.00 | 60.0 | 90.0 |
| Bench 2 | Autosub In | Scott McTominay | MID | 14 | 4.9 | 2.93 | 8.80 | 14.49 | 1.00 | 75.2 | 9.0 |