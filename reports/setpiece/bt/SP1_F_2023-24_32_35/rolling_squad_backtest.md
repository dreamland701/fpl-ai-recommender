# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 265.63
- Total actual points: 305.00
- Average predicted points: 66.41
- Average actual points: 76.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW31 are included before the first simulated week.
- League-average scores were not available for this run.

## GW32

- Train rows: 127681
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 58.97
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Antoine Semenyo replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.13 | 8.81 | 14.36 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.73 | 4.87 | 7.25 | 1.00 | 51.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.03 | 11.29 | 18.48 | 5.00 | 82.6 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.59 | 10.50 | 16.80 | 5.00 | 77.2 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.92 | 8.79 | 14.83 | 2.00 | 72.8 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.41 | 6.63 | 10.54 | 2.00 | 66.2 | 83.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.20 | 6.05 | 10.06 | 2.00 | 76.8 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.86 | 17.11 | 29.74 | 8.00 | 65.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.42 | 13.61 | 20.55 | 2.00 | 72.4 | 90.0 |
| Bench 2 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 2.54 | 6.62 | 11.26 | 2.00 | 48.6 | 68.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.23 | 18.02 | 27.84 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.44 | 16.00 | 25.85 | 5.00 | 84.8 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.58 | 15.79 | 25.81 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.03 | 14.26 | 23.47 | 1.00 | 90.0 | 53.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.51 | 13.56 | 22.77 | 3.00 | 80.6 | 88.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 55.82
- Actual score: 78.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Alfie Doughty replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.93 | 8.59 | 13.94 | 9.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.99 | 5.35 | 8.05 | 0.00 | 57.9 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.56 | 12.22 | 19.54 | 1.00 | 87.8 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.05 | 11.11 | 17.52 | 5.00 | 79.4 | 66.0 |
| Bench 3 | Autosub In | Alfie Doughty | DEF | 12 | 4.6 | 2.44 | 8.13 | 13.57 | 0.00 | 75.7 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 3.9 | 2.51 | 6.82 | 10.66 | 1.00 | 66.9 | 45.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.78 | 6.05 | 10.16 | 0.00 | 79.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.45 | 20.46 | 33.67 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.26 | 13.25 | 20.25 | 12.00 | 73.7 | 90.0 |
| Bench 2 | Bench | Antoine Semenyo | FWD | 3 | 4.5 | 2.55 | 7.13 | 11.64 | 0.00 | 57.3 | 0.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.84 | 16.42 | 25.31 | 26.00 | 84.3 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.77 | 14.68 | 24.11 | 1.00 | 78.6 | 57.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.95 | 14.23 | 23.31 | 3.00 | 82.9 | 78.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.69 | 10.58 | 17.96 | 0.00 | 47.3 | 0.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.38 | 10.12 | 17.24 | 0.00 | 59.7 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.00 -> 1.60
- Free transfers: 2 -> 2
- Captain: Eberechi Eze
- Vice captain: William Saliba
- Effective captain: Eberechi Eze
- Chip used: bench_boost
- Predicted score: 74.23
- Actual score: 119.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.93) beats the best remaining Bench Boost opportunity (7.65).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Jarrod Bowen -> Eberechi Eze (projected gain 7.46, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.93) beats the best remaining Bench Boost opportunity (7.65).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.00 | 8.94 | 14.85 | 2.00 | 86.8 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.67 | 2.50 | 4.05 | 0.00 | 27.8 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 5.8 | 8.62 | 13.09 | 20.40 | 14.00 | 174.8 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.86 | 12.23 | 18.95 | 26.00 | 155.5 | 180.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.5 | 2.77 | 7.74 | 12.66 | -1.00 | 74.9 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 3.9 | 2.24 | 6.40 | 10.32 | 2.00 | 59.8 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 0.81 | 2.56 | 4.56 | 0.00 | 31.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.30 | 18.22 | 29.85 | 0.00 | 76.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.08 | 14.82 | 23.48 | 2.00 | 84.9 | 90.0 |
| Bench 2 | Bench Boost | Antoine Semenyo | FWD | 3 | 4.5 | 2.02 | 4.34 | 7.39 | 10.00 | 51.3 | 117.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.94 | 16.33 | 25.76 | 0.00 | 86.8 | 0.0 |
| Captain | Captain | Eberechi Eze | MID | 8 | 6.1 | 9.26 | 14.35 | 21.70 | 14.00 | 171.2 | 162.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 8.59 | 14.19 | 22.75 | 20.00 | 138.3 | 180.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 12.84 | 22.19 | 0.00 | 0.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 2.81 | 9.02 | 16.02 | 16.00 | 38.8 | 71.0 |

## GW35

- Train rows: 130234
- Bank: 1.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 76.61
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.79) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.64): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Alfie Doughty -> Fabian Schär (projected gain 4.08, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.79) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Antoine Semenyo replaced Phil Foden.
- Autosub: Teden Mengi replaced Eberechi Eze.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.09 | 8.53 | 14.15 | 3.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.57 | 1.74 | 3.22 | 1.00 | 19.1 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.11 | 14.55 | 23.13 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.90 | 13.89 | 22.05 | 1.00 | 90.0 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.7 | 4.25 | 11.41 | 18.13 | 1.00 | 86.8 | 45.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.05 | 6.15 | 10.05 | 0.00 | 66.8 | 0.0 |
| Bench 4 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 2.02 | 5.53 | 9.06 | 1.00 | 66.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 7.00 | 17.27 | 27.39 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.89 | 14.84 | 25.14 | 5.00 | 38.2 | 28.0 |
| Bench 2 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 3.15 | 8.29 | 13.01 | 2.00 | 69.9 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 6.27 | 18.32 | 29.55 | 2.00 | 90.0 | 88.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.59 | 15.51 | 25.04 | 8.00 | 114.8 | 180.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.81 | 13.89 | 22.45 | 0.00 | 70.7 | 0.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.05 | 12.67 | 20.82 | 9.00 | 108.9 | 180.0 |
| XI | Bench | Eberechi Eze | MID | 8 | 6.1 | 3.47 | 10.66 | 17.29 | 0.00 | 64.5 | 0.0 |