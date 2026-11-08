# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 278.15
- Total actual points: 290.00
- Average predicted points: 69.54
- Average actual points: 72.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.65
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.17 | 8.78 | 14.21 | 3.00 | 83.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.92 | 5.24 | 7.82 | 1.00 | 56.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.09 | 11.36 | 18.51 | 5.00 | 81.1 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.66 | 10.69 | 17.01 | 5.00 | 79.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.53 | 9.93 | 16.02 | 6.00 | 79.1 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.90 | 11.08 | 2.00 | 70.7 | 83.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.35 | 6.43 | 10.51 | 2.00 | 74.6 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.07 | 17.76 | 31.02 | 8.00 | 71.4 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.43 | 13.43 | 20.05 | 2.00 | 74.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.52 | 12.03 | 19.94 | 2.00 | 75.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.66 | 16.40 | 25.52 | 5.00 | 82.8 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.06 | 15.08 | 24.83 | 5.00 | 79.1 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.20 | 15.02 | 25.05 | 0.00 | 82.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.59 | 13.11 | 21.97 | 1.00 | 82.8 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.98 | 8.56 | 14.32 | 2.00 | 78.6 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.05
- Actual score: 84.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.06, hit 0)
- Autosub: Charlie Taylor replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.97 | 8.59 | 13.84 | 9.00 | 81.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.18 | 5.71 | 8.58 | 0.00 | 62.9 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.30 | 11.36 | 17.59 | 0.00 | 80.6 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.13 | 11.31 | 17.77 | 5.00 | 81.9 | 66.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.10 | 10.97 | 17.88 | 1.00 | 80.8 | 90.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.62 | 7.08 | 11.17 | 1.00 | 71.4 | 45.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.41 | 5.24 | 8.91 | 0.00 | 66.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.10 | 19.58 | 32.72 | 10.00 | 82.8 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.27 | 13.11 | 19.82 | 12.00 | 75.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.08 | 11.59 | 19.10 | 7.00 | 75.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.81 | 16.09 | 24.66 | 26.00 | 82.0 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.92 | 15.04 | 24.72 | 1.00 | 78.2 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.29 | 14.50 | 22.62 | 2.00 | 81.3 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.99 | 11.45 | 19.45 | 0.00 | 53.2 | 0.0 |
| Bench 3 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.30 | 7.98 | 13.28 | 7.00 | 80.3 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.20 -> 2.30
- Free transfers: 2 -> 2
- Captain: Luis Díaz
- Vice captain: Eberechi Eze
- Effective captain: Luis Díaz
- Chip used: bench_boost
- Predicted score: 85.65
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.24) beats the best remaining Bench Boost opportunity (9.55).
- Transfer: Phil Foden -> Eberechi Eze (projected gain 4.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.24) beats the best remaining Bench Boost opportunity (9.55).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.55 | 7.66 | 13.09 | 2.00 | 79.6 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.60 | 2.31 | 3.78 | 0.00 | 26.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.21 | 12.40 | 18.74 | 12.00 | 163.9 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.00 | 12.37 | 19.12 | 26.00 | 160.2 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 7.76 | 11.89 | 18.81 | 14.00 | 160.7 | 180.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.36 | 6.71 | 10.86 | 2.00 | 64.5 | 90.0 |
| Bench 3 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 1.40 | 4.02 | 6.88 | 1.00 | 42.1 | 34.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.44 | 18.60 | 30.48 | 0.00 | 79.4 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.13 | 14.76 | 23.22 | 2.00 | 82.8 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 8.76 | 13.40 | 21.36 | 8.00 | 165.5 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.41 | 14.74 | 23.52 | 0.00 | 79.1 | 0.0 |
| Captain | Captain | Luis Díaz | MID | 11 | 7.7 | 8.98 | 13.87 | 21.08 | 3.00 | 140.3 | 163.0 |
| Vice Captain | XI | Eberechi Eze | MID | 8 | 6.1 | 8.92 | 13.32 | 19.75 | 14.00 | 162.9 | 162.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 11.91 | 21.12 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.14 | 8.50 | 13.58 | 2.00 | 80.1 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 2.30 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 76.80
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.05) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Eberechi Eze -> Bruno Borges Fernandes (projected gain 6.14, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (12.05) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.16 | 8.53 | 14.06 | 3.00 | 80.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.49 | 1.54 | 2.92 | 1.00 | 18.0 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.72 | 13.54 | 21.90 | 1.00 | 82.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.46 | 12.59 | 20.30 | 1.00 | 82.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.19 | 11.84 | 18.77 | 1.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.17 | 6.45 | 10.58 | 0.00 | 71.5 | 0.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 0.93 | 3.28 | 5.82 | 0.00 | 34.1 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.54 | 15.92 | 25.54 | 13.00 | 82.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.95 | 15.21 | 25.92 | 5.00 | 38.7 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.52 | 12.40 | 19.81 | 2.00 | 82.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 5.41 | 16.17 | 26.37 | 4.00 | 82.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.85 | 15.69 | 25.29 | 8.00 | 124.4 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.65 | 13.42 | 22.07 | 9.00 | 122.1 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.64 | 12.87 | 20.06 | 5.00 | 79.7 | 78.0 |
| Bench 2 | Bench | Ross Barkley | MID | 12 | 4.6 | 2.93 | 8.12 | 13.26 | 2.00 | 82.0 | 77.0 |