# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 284.11
- Total actual points: 301.00
- Average predicted points: 71.03
- Average actual points: 75.25
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
- Predicted score: 59.71
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Ross Barkley replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.12 | 8.74 | 14.22 | 3.00 | 85.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.72 | 4.84 | 7.19 | 1.00 | 51.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.04 | 11.33 | 18.54 | 5.00 | 82.8 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.63 | 10.70 | 17.17 | 5.00 | 77.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.49 | 9.93 | 16.14 | 6.00 | 77.2 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.43 | 6.70 | 10.67 | 2.00 | 66.5 | 83.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.99 | 6.32 | 10.44 | 1.00 | 73.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.97 | 17.48 | 30.44 | 8.00 | 67.1 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.40 | 13.46 | 20.25 | 2.00 | 72.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.48 | 11.99 | 20.01 | 2.00 | 73.2 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.14 | 17.70 | 27.32 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.54 | 16.35 | 26.55 | 5.00 | 86.2 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.68 | 16.30 | 26.77 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.07 | 14.40 | 23.73 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.8 | 2.92 | 8.51 | 14.30 | 2.00 | 80.2 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.55
- Actual score: 85.00
- Transfer: Phil Foden -> Luis Díaz (projected gain 3.72, hit 0)
- Autosub: Jan Paul van Hecke replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.92 | 8.53 | 13.81 | 9.00 | 83.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.97 | 5.27 | 7.89 | 0.00 | 57.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.57 | 12.23 | 19.54 | 1.00 | 87.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.10 | 11.31 | 17.88 | 5.00 | 79.9 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.25 | 11.30 | 17.59 | 0.00 | 82.4 | 90.0 |
| Bench 2 | Autosub In | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.61 | 7.16 | 11.40 | 2.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.86 | 10.74 | 1.00 | 67.0 | 45.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.56 | 20.83 | 34.38 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.23 | 13.09 | 19.90 | 12.00 | 73.5 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.98 | 11.32 | 18.56 | 7.00 | 70.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.76 | 16.07 | 24.73 | 26.00 | 83.9 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.86 | 14.96 | 24.66 | 1.00 | 80.0 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.24 | 14.49 | 22.69 | 2.00 | 83.2 | 65.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.51 | 11.07 | 19.12 | 0.00 | 62.6 | 0.0 |
| Bench 4 | Bench | Ross Barkley | MID | 12 | 4.7 | 2.26 | 7.95 | 13.34 | 7.00 | 78.2 | 90.0 |

## GW34

- Train rows: 129378
- Bank: 0.50 -> 2.10
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Eberechi Eze
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 88.98
- Actual score: 93.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.94) beats the best remaining Bench Boost opportunity (10.46).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Jarrod Bowen -> Eberechi Eze (projected gain 5.49, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.94) beats the best remaining Bench Boost opportunity (10.46).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.99 | 8.87 | 14.70 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.65 | 2.36 | 3.80 | 0.00 | 27.5 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.65 | 13.12 | 20.45 | 14.00 | 174.9 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 7.94 | 12.40 | 19.27 | 26.00 | 156.3 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.07 | 12.33 | 18.71 | 12.00 | 167.4 | 180.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.16 | 6.69 | 10.79 | 0.00 | 77.6 | 90.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.25 | 6.42 | 10.34 | 2.00 | 59.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.40 | 18.52 | 30.41 | 0.00 | 77.2 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.06 | 14.68 | 23.17 | 2.00 | 84.5 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.66 | 14.66 | 23.06 | 8.00 | 180.0 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.84 | 15.95 | 25.12 | 0.00 | 86.1 | 0.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 8.78 | 13.66 | 20.73 | 3.00 | 131.6 | 163.0 |
| Vice Captain | XI | Eberechi Eze | MID | 8 | 6.1 | 8.80 | 13.36 | 19.93 | 14.00 | 167.0 | 162.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.10 | 22.70 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 4.7 | 3.07 | 8.42 | 13.54 | 2.00 | 81.9 | 90.0 |

## GW35

- Train rows: 130234
- Bank: 2.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 76.88
- Actual score: 74.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.62) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Ross Barkley -> Anthony Gordon (projected gain 2.42, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.62) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.09 | 8.48 | 14.05 | 3.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.54 | 1.63 | 3.01 | 1.00 | 18.9 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.17 | 14.82 | 23.63 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.90 | 13.85 | 21.97 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.63 | 13.11 | 20.45 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.38 | 6.66 | 10.70 | 0.00 | 76.4 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.06 | 6.20 | 10.14 | 0.00 | 67.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.99 | 17.26 | 27.35 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.10 | 16.11 | 27.64 | 5.00 | 41.9 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.96 | 13.63 | 21.42 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.42 | 15.19 | 24.52 | 8.00 | 113.9 | 180.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.2 | 4.93 | 13.04 | 20.05 | 10.00 | 77.3 | 81.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.22 | 12.91 | 21.27 | 9.00 | 111.5 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.61 | 12.86 | 20.16 | 5.00 | 77.8 | 78.0 |
| Bench 2 | Bench | Eberechi Eze | MID | 8 | 6.1 | 3.38 | 10.68 | 17.52 | 0.00 | 65.1 | 0.0 |