# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 237.88
- Total actual points: 205.00
- Average predicted points: 59.47
- Average actual points: 51.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW27 are included before the first simulated week.
- League-average scores were not available for this run.

## GW28

- Train rows: 152512
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 67.30
- Actual score: 60.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.44 | 10.75 | 16.37 | 2.00 | 89.4 | 90.0 |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 3.67 | 10.75 | 16.19 | 10.00 | 87.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.47 | 12.08 | 16.79 | 2.00 | 82.5 | 90.0 |
| XI | XI | Tyrick Mitchell | DEF | 7 | 4.8 | 4.18 | 10.76 | 15.97 | 6.00 | 78.7 | 71.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 5.48 | 10.63 | 22.77 | 2.00 | 78.9 | 88.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 6.2 | 3.55 | 10.51 | 17.42 | 2.00 | 84.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.06 | 9.95 | 16.29 | 1.00 | 87.5 | 86.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.57 | 10.54 | 16.26 | 2.00 | 80.1 | 90.0 |
| Bench 3 | Bench | Jørgen Strand Larsen | FWD | 20 | 5.2 | 2.71 | 7.21 | 11.51 | 1.00 | 54.5 | 73.0 |
| Bench 4 | Bench | Paul Onuachu | FWD | 17 | 4.9 | 1.81 | 6.15 | 10.58 | 0.00 | 48.3 | 6.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.0 | 8.82 | 22.11 | 35.69 | 1.00 | 81.6 | 72.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.96 | 21.90 | 34.93 | 15.00 | 85.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 5.78 | 17.93 | 24.25 | 2.00 | 87.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.97 | 12.85 | 21.11 | 1.00 | 79.1 | 89.0 |
| XI | XI | Pedro Lomba Neto | MID | 6 | 6.3 | 5.37 | 12.66 | 20.75 | 3.00 | 65.9 | 90.0 |

## GW29

- Train rows: 153301
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Cole Palmer
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 39.89
- Actual score: 48.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 4.02 | 10.42 | 17.66 | 3.00 | 88.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 7 | 4.6 | 0.18 | 5.84 | 11.29 | 0.00 | 2.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.78 | 11.03 | 17.72 | 9.00 | 85.1 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 0.12 | 9.31 | 17.58 | 0.00 | 1.1 | 0.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.3 | 3.24 | 9.29 | 15.50 | 0.00 | 83.8 | 0.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 0.00 | 6.38 | 13.92 | 0.00 | 2.1 | 0.0 |
| Bench 3 | Bench | Tyrick Mitchell | DEF | 7 | 4.8 | 0.08 | 5.98 | 11.25 | 0.00 | 0.0 | 0.0 |
| XI | XI | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 3.83 | 11.77 | 19.49 | 2.00 | 80.1 | 79.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.2 | 3.66 | 7.51 | 11.31 | 13.00 | 65.0 | 89.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 1.41 | 5.41 | 8.15 | 7.00 | 27.8 | 45.0 |
| Vice Captain | Bench | Cole Palmer | MID | 6 | 10.9 | 4.26 | 18.36 | 27.98 | 0.00 | 62.3 | 0.0 |
| Bench 2 | Bench | Mohamed Salah | MID | 12 | 13.8 | 1.21 | 17.73 | 30.77 | 0.00 | 1.1 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 3.89 | 13.33 | 20.14 | 1.00 | 85.3 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 4 | 8.1 | 4.51 | 13.26 | 22.39 | 6.00 | 88.2 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 6 | 6.3 | 2.67 | 11.55 | 19.08 | 1.00 | 61.6 | 90.0 |

## GW30

- Train rows: 154090
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Antoine Semenyo
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.65
- Actual score: 59.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.03) beats the best remaining Bench Boost opportunity (11.43).
- Transfer: Pedro Porro -> Daniel Muñoz (projected gain 0.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.03) beats the best remaining Bench Boost opportunity (11.43).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 3.46 | 9.29 | 17.10 | 2.00 | 75.0 | 90.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 5.1 | 2.14 | 8.76 | 15.88 | 3.00 | 74.8 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 4.21 | 11.82 | 20.02 | 2.00 | 78.5 | 75.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.96 | 11.54 | 17.74 | 2.00 | 87.0 | 90.0 |
| Bench 2 | Bench Boost | Trent Alexander-Arnold | DEF | 12 | 7.3 | 3.34 | 11.51 | 16.23 | 0.00 | 61.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.08 | 10.56 | 19.56 | 8.00 | 83.2 | 90.0 |
| XI | XI | Tyrick Mitchell | DEF | 7 | 4.8 | 3.46 | 8.97 | 15.66 | 1.00 | 69.7 | 57.0 |
| Bench 4 | Bench Boost | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.1 | 2.24 | 9.39 | 18.13 | 1.00 | 48.6 | 78.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.90 | 8.26 | 13.33 | 7.00 | 62.0 | 88.0 |
| Bench 3 | Bench Boost | Jørgen Strand Larsen | FWD | 20 | 5.2 | 2.31 | 5.06 | 8.45 | 9.00 | 48.1 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.7 | 8.38 | 27.89 | 40.51 | 3.00 | 88.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.19 | 13.00 | 18.02 | 8.00 | 77.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 3 | 5.7 | 5.22 | 12.99 | 22.13 | 2.00 | 82.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 6 | 10.8 | 4.02 | 11.91 | 21.43 | 6.00 | 41.9 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 6 | 6.3 | 4.36 | 11.07 | 18.26 | 2.00 | 65.8 | 90.0 |

## GW31

- Train rows: 154881
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.03
- Actual score: 38.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.00) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 7 | 4.6 | 3.50 | 10.86 | 17.48 | 3.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 2.48 | 10.72 | 17.46 | 3.00 | 89.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.17 | 11.82 | 18.52 | 2.00 | 85.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.02 | 11.70 | 20.69 | 1.00 | 85.3 | 90.0 |
| XI | XI | Daniel Muñoz | DEF | 7 | 5.1 | 3.94 | 11.26 | 17.67 | 8.00 | 76.2 | 90.0 |
| Bench 2 | Bench | Tyrick Mitchell | DEF | 7 | 4.8 | 2.87 | 9.15 | 16.80 | 2.00 | 67.7 | 62.0 |
| Bench 4 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.3 | 1.11 | 5.29 | 9.22 | 0.00 | 24.0 | 0.0 |
| Bench 3 | Bench | Norberto Bercique Gomes Betuncal | FWD | 8 | 5.0 | 2.46 | 9.86 | 14.84 | 2.00 | 48.7 | 64.0 |
| XI | XI | Jørgen Strand Larsen | FWD | 20 | 5.2 | 3.25 | 9.80 | 16.13 | 6.00 | 72.1 | 90.0 |
| XI | XI | Paul Onuachu | FWD | 17 | 4.9 | 2.93 | 8.20 | 12.53 | 1.00 | 70.8 | 17.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.8 | 8.00 | 25.33 | 42.04 | 2.00 | 85.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 10.7 | 6.02 | 21.46 | 33.12 | 1.00 | 81.7 | 31.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 8.1 | 4.36 | 12.30 | 23.24 | 3.00 | 85.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 3 | 5.7 | 4.26 | 11.67 | 19.16 | 6.00 | 78.8 | 90.0 |
| XI | XI | Pedro Lomba Neto | MID | 6 | 6.2 | 3.58 | 11.60 | 18.64 | 1.00 | 73.5 | 31.0 |