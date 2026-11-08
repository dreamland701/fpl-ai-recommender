# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 280.20
- Total actual points: 299.00
- Average predicted points: 70.05
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
- Predicted score: 59.45
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.10 | 8.62 | 14.08 | 3.00 | 82.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.72 | 4.77 | 7.12 | 1.00 | 49.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.93 | 11.17 | 18.31 | 5.00 | 83.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.59 | 10.53 | 17.03 | 5.00 | 80.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.44 | 9.89 | 16.11 | 6.00 | 78.6 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.45 | 6.63 | 10.59 | 2.00 | 67.2 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.03 | 6.40 | 10.55 | 1.00 | 74.1 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.75 | 17.33 | 30.22 | 8.00 | 65.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.41 | 13.09 | 19.51 | 2.00 | 74.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.51 | 11.86 | 19.86 | 2.00 | 72.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.23 | 17.33 | 26.66 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.53 | 16.31 | 26.55 | 5.00 | 86.4 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.69 | 16.25 | 26.56 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.04 | 14.25 | 23.43 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.85 | 8.33 | 14.08 | 2.00 | 79.8 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.90
- Actual score: 85.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.55, hit 0)
- Autosub: Jan Paul van Hecke replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.91 | 8.50 | 13.80 | 9.00 | 81.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.00 | 5.20 | 7.75 | 0.00 | 56.1 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.39 | 11.89 | 19.01 | 1.00 | 88.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.16 | 11.16 | 17.40 | 0.00 | 83.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.00 | 11.13 | 17.83 | 5.00 | 82.1 | 66.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.63 | 7.22 | 11.42 | 2.00 | 82.2 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.58 | 7.01 | 11.01 | 1.00 | 68.1 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.36 | 20.48 | 33.70 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.18 | 12.83 | 19.49 | 12.00 | 75.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.97 | 11.37 | 18.58 | 7.00 | 70.5 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.74 | 15.76 | 24.25 | 26.00 | 86.0 | 79.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.36 | 14.79 | 23.15 | 2.00 | 84.4 | 65.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.77 | 14.75 | 24.35 | 1.00 | 79.6 | 57.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.71 | 10.93 | 18.40 | 0.00 | 50.3 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.26 | 7.88 | 13.28 | 7.00 | 78.3 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Luis Díaz
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 84.80
- Actual score: 97.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.53) beats the best remaining Bench Boost opportunity (10.51).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.58, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.53) beats the best remaining Bench Boost opportunity (10.51).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.94 | 8.78 | 14.52 | 2.00 | 83.8 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.77 | 2.52 | 4.09 | 0.00 | 25.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.35 | 12.79 | 20.00 | 14.00 | 175.2 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.91 | 12.40 | 19.42 | 26.00 | 160.6 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 7.95 | 12.22 | 18.62 | 12.00 | 169.0 | 180.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.11 | 6.57 | 10.60 | 0.00 | 78.7 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.23 | 6.53 | 10.65 | 2.00 | 60.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.21 | 18.32 | 30.01 | 0.00 | 75.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.03 | 14.59 | 22.91 | 2.00 | 85.1 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.50 | 14.30 | 22.45 | 8.00 | 180.0 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.88 | 15.91 | 24.86 | 0.00 | 88.9 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.42 | 14.56 | 23.30 | 18.00 | 90.0 | 90.0 |
| Vice Captain | XI | Luis Díaz | MID | 11 | 7.7 | 8.97 | 13.67 | 20.87 | 3.00 | 134.5 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 12.90 | 22.38 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.04 | 8.29 | 13.33 | 2.00 | 81.8 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 78.05
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.85) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.64): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.85) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.04 | 8.48 | 13.94 | 3.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.63 | 1.69 | 3.15 | 1.00 | 17.3 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.12 | 14.58 | 23.11 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.75 | 13.35 | 21.02 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.55 | 12.71 | 19.78 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.36 | 6.50 | 10.49 | 0.00 | 77.7 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.04 | 6.16 | 10.08 | 0.00 | 68.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.98 | 16.51 | 26.22 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.86 | 14.84 | 25.08 | 5.00 | 37.6 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.88 | 13.32 | 20.65 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.98 | 17.60 | 28.13 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.65 | 15.25 | 24.60 | 8.00 | 119.5 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.15 | 13.19 | 21.87 | 9.00 | 112.5 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.78 | 13.11 | 20.49 | 5.00 | 78.9 | 78.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.86 | 8.02 | 13.16 | 2.00 | 84.1 | 77.0 |