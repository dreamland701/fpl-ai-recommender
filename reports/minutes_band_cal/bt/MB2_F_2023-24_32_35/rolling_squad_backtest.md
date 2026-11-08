# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 274.64
- Total actual points: 300.00
- Average predicted points: 68.66
- Average actual points: 75.00
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
- Predicted score: 57.66
- Actual score: 49.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Alejandro Garnacho replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.07 | 8.65 | 14.03 | 3.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.97 | 5.39 | 8.00 | 1.00 | 58.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.99 | 11.23 | 18.33 | 5.00 | 80.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.65 | 10.68 | 17.10 | 5.00 | 78.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.52 | 9.93 | 16.11 | 6.00 | 78.3 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.91 | 11.08 | 2.00 | 70.7 | 83.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.35 | 6.44 | 10.51 | 2.00 | 74.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 6.07 | 17.77 | 31.01 | 8.00 | 71.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.42 | 13.43 | 20.14 | 2.00 | 73.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.51 | 12.02 | 20.03 | 2.00 | 74.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 6.71 | 16.53 | 25.64 | 5.00 | 82.9 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.12 | 15.21 | 24.95 | 5.00 | 79.2 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.26 | 15.15 | 25.17 | 0.00 | 82.9 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.64 | 13.23 | 22.09 | 1.00 | 82.9 | 53.0 |
| Bench 2 | Autosub In | Alejandro Garnacho | MID | 14 | 4.9 | 2.84 | 8.59 | 14.22 | 2.00 | 75.0 | 79.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.70
- Actual score: 87.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 4.09, hit 0)
- Autosub: Alejandro Garnacho replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.86 | 8.42 | 13.61 | 9.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.23 | 5.87 | 8.76 | 0.00 | 64.8 | 0.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.12 | 11.32 | 17.86 | 5.00 | 81.0 | 66.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.19 | 11.18 | 17.36 | 0.00 | 79.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.16 | 11.12 | 18.00 | 1.00 | 80.9 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.62 | 7.08 | 11.17 | 1.00 | 71.5 | 45.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.32 | 5.05 | 8.54 | 0.00 | 61.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.15 | 19.73 | 32.84 | 10.00 | 82.9 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.26 | 13.12 | 19.91 | 12.00 | 74.7 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.08 | 11.59 | 19.11 | 7.00 | 75.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.69 | 15.92 | 24.44 | 26.00 | 81.1 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.80 | 14.87 | 24.49 | 1.00 | 77.3 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 5.18 | 14.33 | 22.39 | 2.00 | 80.4 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.04 | 11.61 | 19.63 | 0.00 | 55.2 | 0.0 |
| Bench 2 | Autosub In | Alejandro Garnacho | MID | 14 | 4.9 | 3.27 | 9.11 | 14.51 | 4.00 | 75.8 | 45.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Luis Díaz
- Vice captain: Dominic Solanke
- Effective captain: Luis Díaz
- Chip used: bench_boost
- Predicted score: 81.77
- Actual score: 96.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.88) beats the best remaining Bench Boost opportunity (9.66).
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 4.27, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.88) beats the best remaining Bench Boost opportunity (9.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.60 | 7.79 | 13.20 | 2.00 | 79.7 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.65 | 2.40 | 3.89 | 0.00 | 27.7 | 0.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.00 | 12.40 | 19.23 | 26.00 | 158.6 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 7.96 | 12.21 | 18.47 | 12.00 | 161.9 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 7.86 | 12.02 | 18.91 | 14.00 | 160.9 | 180.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.36 | 6.70 | 10.86 | 2.00 | 64.5 | 90.0 |
| Bench 3 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 1.44 | 4.11 | 7.00 | 1.00 | 43.1 | 34.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.44 | 18.64 | 30.59 | 0.00 | 78.6 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 5.01 | 14.57 | 22.96 | 2.00 | 81.8 | 90.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 7.2 | 8.86 | 13.53 | 21.46 | 8.00 | 165.7 | 176.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.46 | 14.87 | 23.62 | 0.00 | 79.2 | 0.0 |
| Captain | Captain | Luis Díaz | MID | 11 | 7.7 | 8.97 | 13.86 | 21.08 | 3.00 | 140.4 | 163.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.01 | 13.39 | 21.85 | 18.00 | 82.9 | 90.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 12.04 | 21.22 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.9 | 3.17 | 8.40 | 13.42 | 5.00 | 63.9 | 90.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 77.51
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.16) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.61): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (12.16) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.03 | 8.36 | 13.81 | 3.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.54 | 1.64 | 3.04 | 1.00 | 19.0 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.78 | 13.67 | 21.99 | 1.00 | 82.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.51 | 12.72 | 20.39 | 1.00 | 82.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.24 | 11.98 | 18.85 | 1.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.16 | 6.44 | 10.57 | 0.00 | 71.5 | 0.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 0.98 | 3.38 | 5.92 | 0.00 | 35.0 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 6.60 | 16.06 | 25.63 | 13.00 | 82.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.00 | 15.31 | 26.02 | 5.00 | 39.6 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.58 | 12.54 | 19.90 | 2.00 | 82.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.47 | 16.31 | 26.46 | 4.00 | 82.9 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.96 | 15.85 | 25.48 | 8.00 | 128.4 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.76 | 13.59 | 22.26 | 9.00 | 126.0 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.64 | 12.89 | 20.16 | 5.00 | 79.0 | 78.0 |
| Bench 2 | Bench | Alejandro Garnacho | MID | 14 | 4.9 | 3.29 | 9.12 | 14.69 | 2.00 | 66.1 | 90.0 |