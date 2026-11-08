# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 280.84
- Total actual points: 299.00
- Average predicted points: 70.21
- Average actual points: 74.75
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
- Predicted score: 59.59
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.09 | 8.60 | 14.08 | 3.00 | 85.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.69 | 4.67 | 6.94 | 1.00 | 51.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.97 | 11.32 | 18.59 | 5.00 | 82.6 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.59 | 10.53 | 17.01 | 5.00 | 79.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.47 | 10.00 | 16.31 | 6.00 | 77.7 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.44 | 6.59 | 10.51 | 2.00 | 66.5 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.04 | 6.44 | 10.62 | 1.00 | 73.4 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.75 | 17.31 | 30.15 | 8.00 | 64.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.41 | 13.11 | 19.56 | 2.00 | 74.4 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.53 | 11.94 | 20.01 | 2.00 | 73.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.26 | 17.45 | 26.89 | 5.00 | 90.0 | 73.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.70 | 16.32 | 26.70 | 0.00 | 90.0 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.50 | 16.19 | 26.29 | 5.00 | 85.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.06 | 14.34 | 23.60 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.89 | 8.48 | 14.37 | 2.00 | 80.7 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.97
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.35, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.90 | 8.48 | 13.79 | 9.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.97 | 5.11 | 7.60 | 0.00 | 58.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.42 | 12.03 | 19.26 | 1.00 | 87.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.17 | 11.20 | 17.47 | 0.00 | 82.8 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.00 | 11.14 | 17.82 | 5.00 | 81.0 | 66.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.64 | 7.25 | 11.48 | 2.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.57 | 6.96 | 10.90 | 1.00 | 67.3 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.35 | 20.46 | 33.65 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.19 | 12.90 | 19.62 | 12.00 | 75.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.99 | 11.47 | 18.76 | 7.00 | 70.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.77 | 15.86 | 24.46 | 26.00 | 85.8 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.75 | 14.66 | 24.17 | 1.00 | 78.9 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.33 | 14.64 | 22.87 | 2.00 | 84.0 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.74 | 11.05 | 18.63 | 0.00 | 50.0 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.29 | 8.01 | 13.54 | 7.00 | 79.0 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 85.02
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.50) beats the best remaining Bench Boost opportunity (10.47).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.50) beats the best remaining Bench Boost opportunity (10.47).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.94 | 8.78 | 14.55 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.73 | 2.42 | 3.91 | 0.00 | 28.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.42 | 12.92 | 20.22 | 14.00 | 173.2 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.92 | 12.41 | 19.42 | 26.00 | 158.5 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 7.98 | 12.26 | 18.69 | 12.00 | 167.0 | 180.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.12 | 6.60 | 10.65 | 0.00 | 77.9 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.22 | 6.48 | 10.55 | 2.00 | 60.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.20 | 18.26 | 29.87 | 0.00 | 73.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.04 | 14.64 | 23.01 | 2.00 | 85.2 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.58 | 14.49 | 22.82 | 8.00 | 180.0 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.92 | 16.08 | 25.18 | 0.00 | 88.4 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.41 | 14.51 | 23.22 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.88 | 13.48 | 20.52 | 3.00 | 133.5 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 12.79 | 22.16 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.07 | 8.44 | 13.62 | 2.00 | 82.4 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 78.27
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.93) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.64): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.93) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.03 | 8.46 | 13.92 | 3.00 | 82.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.60 | 1.59 | 3.00 | 1.00 | 19.8 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.14 | 14.65 | 23.24 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.80 | 13.53 | 21.36 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.58 | 12.83 | 20.00 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.37 | 6.54 | 10.53 | 0.00 | 76.7 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.04 | 6.14 | 10.05 | 0.00 | 67.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.98 | 16.51 | 26.24 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.84 | 14.76 | 24.93 | 5.00 | 36.4 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.91 | 13.48 | 20.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.97 | 17.54 | 28.01 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.73 | 15.40 | 24.88 | 8.00 | 118.3 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.10 | 13.07 | 21.64 | 9.00 | 110.5 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.73 | 12.89 | 20.08 | 5.00 | 78.5 | 78.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.90 | 8.19 | 13.49 | 2.00 | 84.8 | 77.0 |