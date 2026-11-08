# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 309.46
- Total actual points: 299.00
- Average predicted points: 77.36
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
- Vice captain: Mohamed Salah
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.92
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Antoine Semenyo replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 3.58 | 10.31 | 17.97 | 8.00 | 78.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.07 | 6.37 | 8.45 | 1.00 | 51.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.98 | 11.23 | 18.42 | 5.00 | 82.9 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.69 | 10.90 | 17.60 | 5.00 | 77.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.38 | 10.69 | 17.46 | 1.00 | 72.9 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.05 | 5.38 | 8.66 | 2.00 | 76.7 | 90.0 |
| Bench 3 | Bench | Maxime Esteve | DEF | 6 | 4.0 | 2.10 | 5.37 | 8.69 | 2.00 | 73.5 | 90.0 |
| XI | XI | Ivan Toney | FWD | 4 | 8.1 | 3.88 | 12.01 | 20.54 | 1.00 | 85.8 | 9.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 3.73 | 11.72 | 20.04 | 2.00 | 73.3 | 90.0 |
| Bench 2 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 2.49 | 8.21 | 13.74 | 2.00 | 48.9 | 68.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.76 | 19.43 | 28.73 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.49 | 16.71 | 27.23 | 5.00 | 86.3 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.4 | 6.09 | 16.42 | 25.86 | 8.00 | 61.0 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.38 | 15.85 | 26.23 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.20 | 14.78 | 24.06 | 1.00 | 90.0 | 53.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.72
- Actual score: 60.00
- Transfer: Ivan Toney -> Alexander Isak (projected gain 1.26, hit 0)
- Autosub: Maxime Esteve replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 3.92 | 11.45 | 19.34 | 0.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.33 | 7.14 | 9.68 | 0.00 | 57.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.56 | 12.52 | 19.72 | 1.00 | 88.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 4.20 | 11.63 | 18.40 | 2.00 | 78.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.14 | 11.47 | 18.19 | 5.00 | 80.0 | 66.0 |
| Bench 3 | Autosub In | Maxime Esteve | DEF | 6 | 4.0 | 2.32 | 5.78 | 8.92 | 2.00 | 75.1 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.38 | 5.41 | 8.81 | 0.00 | 79.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 3.41 | 11.27 | 17.80 | 12.00 | 73.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.44 | 10.55 | 17.64 | 7.00 | 71.0 | 90.0 |
| Bench 2 | Bench | Antoine Semenyo | FWD | 3 | 4.5 | 2.67 | 7.76 | 12.56 | 0.00 | 57.5 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.4 | 7.26 | 19.69 | 30.10 | 2.00 | 84.1 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 6.60 | 17.10 | 25.71 | 26.00 | 83.9 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 5.21 | 15.92 | 26.05 | 1.00 | 80.1 | 57.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.15 | 10.97 | 18.73 | 0.00 | 48.1 | 0.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.57 | 10.73 | 18.16 | 0.00 | 60.3 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kai Havertz
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 112.38
- Actual score: 124.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.45) beats the best remaining Triple Captain opportunity (15.18).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Jarrod Bowen -> Kai Havertz (projected gain 11.22, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (19.45) beats the best remaining Triple Captain opportunity (15.18).
- Autosub: Antoine Semenyo replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 8.60 | 13.49 | 21.68 | 18.00 | 170.2 | 180.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.27 | 1.07 | 2.24 | 0.00 | 27.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.94 | 13.54 | 20.87 | 14.00 | 175.2 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 9.02 | 13.53 | 20.62 | 2.00 | 168.3 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.74 | 13.42 | 20.87 | 26.00 | 156.4 | 180.0 |
| XI | XI | Maxime Esteve | DEF | 6 | 4.0 | 2.03 | 6.00 | 9.49 | 2.00 | 75.5 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.67 | 2.17 | 3.78 | 0.00 | 31.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 9.33 | 14.23 | 22.12 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.41 | 13.51 | 21.45 | 2.00 | 84.7 | 90.0 |
| Bench 2 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 1.99 | 4.19 | 6.78 | 10.00 | 51.9 | 117.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.4 | 14.56 | 20.91 | 32.73 | 3.00 | 176.7 | 106.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 5.28 | 16.19 | 24.61 | 0.00 | 86.4 | 0.0 |
| Vice Captain | XI | Kai Havertz | MID | 1 | 7.4 | 9.60 | 14.76 | 22.68 | 17.00 | 148.2 | 161.0 |
| Bench 4 | Bench | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.64 | 23.57 | 0.00 | 0.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 2.77 | 9.06 | 15.97 | 16.00 | 39.6 | 71.0 |

## GW35

- Train rows: 130234
- Bank: 0.50 -> 2.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Jordan Pickford
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 79.44
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.85) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Son Heung-min -> Bruno Borges Fernandes (projected gain 5.66, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.85) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | Jordan Pickford | GK | 9 | 4.6 | 6.63 | 17.86 | 26.70 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.02 | 0.00 | 0.00 | 1.00 | 18.9 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.97 | 14.76 | 23.50 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.81 | 13.94 | 21.96 | 1.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.6 | 3.82 | 12.15 | 18.93 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Maxime Esteve | DEF | 6 | 4.0 | 1.49 | 5.22 | 8.54 | 1.00 | 73.3 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.79 | 5.08 | 8.26 | 1.00 | 66.9 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 5.36 | 16.38 | 25.44 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.29 | 14.14 | 22.36 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Antoine Semenyo | FWD | 3 | 4.5 | 3.56 | 8.87 | 13.60 | 2.00 | 70.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.4 | 6.25 | 18.99 | 30.01 | 4.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.5 | 6.49 | 16.68 | 28.43 | 1.00 | 63.8 | 11.0 |
| XI | XI | Kai Havertz | MID | 1 | 7.4 | 5.87 | 16.46 | 26.00 | 13.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 9.39 | 15.25 | 24.64 | 8.00 | 114.2 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 4.31 | 13.58 | 21.86 | 0.00 | 71.7 | 0.0 |