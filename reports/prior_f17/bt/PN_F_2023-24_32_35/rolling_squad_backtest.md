# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 283.64
- Total actual points: 306.00
- Average predicted points: 70.91
- Average actual points: 76.50
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
- Predicted score: 59.83
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.15 | 8.88 | 14.48 | 3.00 | 86.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.75 | 4.92 | 7.34 | 1.00 | 51.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.05 | 11.39 | 18.66 | 5.00 | 83.1 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.64 | 10.69 | 17.12 | 5.00 | 78.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.51 | 9.98 | 16.23 | 6.00 | 77.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.37 | 6.52 | 10.37 | 2.00 | 65.4 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.02 | 6.41 | 10.61 | 1.00 | 73.4 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.96 | 17.57 | 30.66 | 8.00 | 66.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.42 | 13.55 | 20.37 | 2.00 | 72.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.52 | 12.16 | 20.32 | 2.00 | 74.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.14 | 17.73 | 27.33 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.55 | 16.42 | 26.67 | 5.00 | 86.6 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.68 | 16.30 | 26.78 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.07 | 14.37 | 23.65 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.95 | 8.64 | 14.54 | 2.00 | 80.8 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.99
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.36, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.96 | 8.68 | 14.10 | 9.00 | 84.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.01 | 5.38 | 8.08 | 0.00 | 58.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.59 | 12.34 | 19.75 | 1.00 | 88.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.28 | 11.41 | 17.77 | 0.00 | 83.1 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.10 | 11.32 | 17.89 | 5.00 | 80.2 | 66.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.64 | 7.24 | 11.53 | 2.00 | 81.2 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.46 | 6.69 | 10.46 | 1.00 | 66.0 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.55 | 20.90 | 34.55 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.25 | 13.18 | 20.05 | 12.00 | 73.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.01 | 11.51 | 18.93 | 7.00 | 71.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.78 | 16.15 | 24.84 | 26.00 | 84.5 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.87 | 15.07 | 24.87 | 1.00 | 80.3 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.26 | 14.54 | 22.78 | 2.00 | 83.6 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.79 | 11.00 | 18.72 | 0.00 | 48.4 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.30 | 8.09 | 13.59 | 7.00 | 78.8 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 86.12
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.50) beats the best remaining Bench Boost opportunity (10.49).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.50) beats the best remaining Bench Boost opportunity (10.49).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.03 | 9.03 | 14.99 | 2.00 | 87.3 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.69 | 2.52 | 4.08 | 0.00 | 28.3 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.72 | 13.25 | 20.68 | 14.00 | 176.8 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.15 | 12.45 | 18.89 | 12.00 | 169.4 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.99 | 12.42 | 19.25 | 26.00 | 157.6 | 180.0 |
| Bench 2 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.19 | 6.81 | 11.01 | 0.00 | 78.1 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.19 | 6.28 | 10.14 | 2.00 | 58.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.40 | 18.67 | 30.75 | 0.00 | 77.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.08 | 14.78 | 23.35 | 2.00 | 84.8 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.73 | 14.77 | 23.24 | 8.00 | 180.0 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.86 | 16.03 | 25.26 | 0.00 | 86.7 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.40 | 14.53 | 23.46 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.86 | 13.76 | 20.88 | 3.00 | 133.4 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.25 | 23.05 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.10 | 8.55 | 13.76 | 2.00 | 82.6 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 78.70
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.67) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.16, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.67) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.78 | 10.79 | 17.37 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.58 | 1.75 | 3.20 | 1.00 | 19.7 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.16 | 14.74 | 23.45 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.91 | 13.93 | 22.13 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.64 | 13.17 | 20.55 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.42 | 6.78 | 10.90 | 0.00 | 76.9 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.00 | 6.02 | 9.84 | 0.00 | 65.9 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 7.00 | 17.28 | 27.40 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.98 | 15.28 | 26.00 | 5.00 | 39.0 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.01 | 13.83 | 21.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.85 | 17.44 | 28.06 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.47 | 15.24 | 24.58 | 8.00 | 115.5 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.30 | 13.05 | 21.51 | 9.00 | 113.5 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.64 | 12.98 | 20.36 | 5.00 | 78.4 | 78.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.89 | 8.19 | 13.45 | 2.00 | 84.5 | 77.0 |