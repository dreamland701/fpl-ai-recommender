# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 283.58
- Total actual points: 306.00
- Average predicted points: 70.89
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
- Predicted score: 60.75
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Tomáš Souček replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.39 | 9.37 | 15.20 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.75 | 4.64 | 6.69 | 1.00 | 51.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.18 | 11.54 | 18.76 | 5.00 | 86.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 3.83 | 11.00 | 17.49 | 5.00 | 83.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.77 | 10.51 | 16.99 | 6.00 | 85.2 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.40 | 6.56 | 10.35 | 2.00 | 66.1 | 83.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 2.23 | 6.15 | 9.90 | 2.00 | 70.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.86 | 17.25 | 30.12 | 8.00 | 62.8 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.51 | 13.61 | 20.38 | 2.00 | 75.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.71 | 12.59 | 20.92 | 2.00 | 79.8 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.02 | 17.22 | 26.31 | 5.00 | 90.0 | 73.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.62 | 16.46 | 26.63 | 5.00 | 88.5 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.69 | 16.13 | 26.34 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.16 | 14.48 | 23.72 | 1.00 | 90.0 | 53.0 |
| Bench 2 | Autosub In | Tomáš Souček | MID | 19 | 4.9 | 3.04 | 8.37 | 13.23 | 1.00 | 82.8 | 45.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.11
- Actual score: 84.00
- Transfer: Jarrod Bowen -> Luis Díaz (projected gain 3.33, hit 0)
- Autosub: Tomáš Souček replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.19 | 9.19 | 14.77 | 9.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.97 | 5.02 | 7.32 | 0.00 | 57.0 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.68 | 12.46 | 19.82 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.51 | 11.96 | 18.57 | 0.00 | 90.0 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 4.28 | 11.59 | 18.16 | 5.00 | 85.0 | 66.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.49 | 6.72 | 10.41 | 1.00 | 66.7 | 45.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 0.77 | 3.82 | 6.98 | 0.00 | 48.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.41 | 20.50 | 33.90 | 10.00 | 90.0 | 80.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.31 | 13.12 | 19.79 | 12.00 | 75.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.19 | 11.86 | 19.37 | 7.00 | 76.6 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.65 | 15.64 | 23.91 | 26.00 | 80.3 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.96 | 15.11 | 24.76 | 1.00 | 82.6 | 57.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.88 | 13.70 | 21.53 | 2.00 | 71.3 | 65.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.64 | 10.92 | 18.88 | 0.00 | 44.7 | 0.0 |
| Bench 2 | Autosub In | Tomáš Souček | MID | 19 | 4.9 | 2.59 | 6.96 | 11.27 | 1.00 | 67.5 | 21.0 |

## GW34

- Train rows: 129378
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: William Saliba
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 86.14
- Actual score: 99.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.72) beats the best remaining Bench Boost opportunity (9.48).
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Phil Foden -> Bruno Borges Fernandes (projected gain 5.86, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.72) beats the best remaining Bench Boost opportunity (9.48).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.26 | 9.48 | 15.57 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.72 | 2.28 | 3.45 | 0.00 | 28.9 | 0.0 |
| Vice Captain | XI | William Saliba | DEF | 1 | 5.8 | 8.94 | 13.37 | 20.73 | 14.00 | 180.0 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.64 | 12.97 | 19.61 | 12.00 | 180.0 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 8.33 | 12.66 | 19.47 | 26.00 | 167.5 | 180.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.23 | 6.26 | 10.00 | 2.00 | 59.9 | 90.0 |
| Bench 3 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 1.34 | 3.83 | 6.58 | 1.00 | 40.7 | 34.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.30 | 18.74 | 31.16 | 0.00 | 75.1 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 10.04 | 14.99 | 23.46 | 8.00 | 180.0 | 176.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.9 | 4.98 | 14.48 | 22.92 | 2.00 | 82.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.70 | 15.41 | 24.13 | 0.00 | 81.6 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.59 | 14.94 | 24.03 | 18.00 | 90.0 | 90.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 8.75 | 13.50 | 20.36 | 3.00 | 129.7 | 163.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 13.09 | 22.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Tomáš Souček | MID | 19 | 4.9 | 2.29 | 6.75 | 11.53 | 3.00 | 60.2 | 45.0 |

## GW35

- Train rows: 130234
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 77.58
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (11.02) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Bernd Leno -> Jordan Pickford (projected gain 2.01, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (11.02) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.7 | 3.95 | 11.15 | 17.84 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.64 | 1.58 | 2.71 | 1.00 | 21.0 | 45.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.9 | 5.22 | 14.70 | 23.25 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.95 | 13.90 | 21.97 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.81 | 13.54 | 21.06 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.03 | 5.97 | 9.67 | 0.00 | 66.5 | 0.0 |
| Bench 4 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 0.50 | 2.15 | 4.28 | 0.00 | 23.3 | 0.0 |
| XI | XI | Alexander Isak | FWD | 15 | 8.0 | 7.01 | 17.22 | 27.24 | 13.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.93 | 15.48 | 26.57 | 5.00 | 37.7 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 5.11 | 14.01 | 21.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 5.99 | 17.80 | 28.62 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 7.82 | 14.76 | 24.13 | 8.00 | 97.7 | 180.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 7.62 | 13.25 | 21.64 | 9.00 | 122.5 | 180.0 |
| XI | XI | Luis Díaz | MID | 11 | 7.7 | 4.51 | 12.55 | 19.63 | 5.00 | 74.3 | 78.0 |
| Bench 2 | Bench | Tomáš Souček | MID | 19 | 4.9 | 2.22 | 6.98 | 11.75 | 2.00 | 63.7 | 73.0 |