# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 268.35
- Total actual points: 299.00
- Average predicted points: 67.09
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
- Vice captain: Phil Foden
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 59.10
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Rodrigo Muniz Carvalho replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 3.04 | 8.42 | 13.87 | 3.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.68 | 4.54 | 6.78 | 1.00 | 52.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.93 | 11.23 | 18.53 | 5.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.45 | 10.00 | 16.38 | 6.00 | 78.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.21 | 8.79 | 14.39 | 2.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Kristoffer Ajer | DEF | 4 | 4.4 | 2.70 | 7.85 | 13.00 | 1.00 | 85.0 | 90.0 |
| Bench 4 | Bench | Mads Roerslev Rasmussen | DEF | 4 | 4.4 | 2.66 | 7.81 | 13.25 | 1.00 | 77.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.3 | 5.57 | 16.96 | 29.69 | 8.00 | 61.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.58 | 11.84 | 20.02 | 2.00 | 73.2 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.85 | 10.30 | 16.27 | 2.00 | 69.2 | 85.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.34 | 17.27 | 26.52 | 5.00 | 90.0 | 73.0 |
| Vice Captain | Bench | Phil Foden | MID | 13 | 8.2 | 5.72 | 16.34 | 26.59 | 0.00 | 90.0 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.1 | 5.44 | 15.99 | 26.03 | 5.00 | 85.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.07 | 14.26 | 23.47 | 1.00 | 90.0 | 53.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.39 | 13.11 | 21.71 | 3.00 | 79.5 | 88.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Cole Palmer
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 55.14
- Actual score: 80.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Antonee Robinson replaced Kristoffer Ajer.
- Autosub: Rodrigo Muniz Carvalho replaced Phil Foden.
- Autosub: Mads Roerslev Rasmussen replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.88 | 8.38 | 13.65 | 9.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.97 | 4.95 | 7.34 | 0.00 | 59.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.28 | 11.72 | 18.87 | 1.00 | 87.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.09 | 11.02 | 17.27 | 0.00 | 83.1 | 90.0 |
| XI | Bench | Kristoffer Ajer | DEF | 4 | 4.4 | 3.28 | 8.64 | 14.21 | 0.00 | 85.6 | 0.0 |
| Bench 3 | Autosub In | Antonee Robinson | DEF | 10 | 4.6 | 2.93 | 8.35 | 13.56 | 6.00 | 77.7 | 90.0 |
| Bench 4 | Autosub In | Mads Roerslev Rasmussen | DEF | 4 | 4.4 | 2.82 | 7.71 | 12.67 | 5.00 | 76.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.19 | 20.06 | 33.00 | 10.00 | 90.0 | 80.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.00 | 11.51 | 18.84 | 7.00 | 71.0 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.7 | 3.15 | 9.01 | 14.64 | 2.00 | 61.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 6.0 | 5.77 | 15.62 | 24.12 | 26.00 | 87.0 | 79.0 |
| XI | XI | Son Heung-min | MID | 18 | 10.0 | 4.65 | 14.38 | 23.71 | 1.00 | 78.2 | 57.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.71 | 13.30 | 21.30 | 3.00 | 82.0 | 78.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.72 | 10.97 | 18.38 | 0.00 | 50.5 | 0.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.8 | 3.39 | 10.24 | 17.22 | 0.00 | 61.1 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.00 -> 1.60
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Eberechi Eze
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 79.26
- Actual score: 107.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.05) beats the best remaining Bench Boost opportunity (10.44).
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Jarrod Bowen -> Eberechi Eze (projected gain 5.23, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.05) beats the best remaining Bench Boost opportunity (10.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.88 | 8.64 | 14.26 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.78 | 2.40 | 3.91 | 0.00 | 28.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.22 | 12.65 | 19.89 | 14.00 | 172.2 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 7.91 | 12.14 | 18.56 | 12.00 | 166.8 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.85 | 8.34 | 13.73 | 1.00 | 78.2 | 90.0 |
| XI | XI | Mads Roerslev Rasmussen | DEF | 4 | 4.4 | 2.76 | 7.66 | 12.46 | 1.00 | 77.9 | 14.0 |
| Bench 3 | Bench Boost | Kristoffer Ajer | DEF | 4 | 4.4 | 1.24 | 3.85 | 7.22 | 6.00 | 37.4 | 75.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.2 | 6.04 | 17.88 | 29.26 | 0.00 | 70.8 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.51 | 14.34 | 22.63 | 8.00 | 180.0 | 176.0 |
| Bench 2 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.6 | 2.60 | 8.24 | 13.49 | 5.00 | 55.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.1 | 4.99 | 16.08 | 24.88 | 0.00 | 90.0 | 0.0 |
| Vice Captain | XI | Eberechi Eze | MID | 8 | 6.1 | 9.08 | 13.44 | 19.98 | 14.00 | 168.4 | 162.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 7.94 | 12.91 | 20.63 | 20.00 | 133.4 | 180.0 |
| Bench 4 | Bench Boost | Son Heung-min | MID | 18 | 10.0 | 0.00 | 12.51 | 21.69 | 0.00 | 0.0 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 2.95 | 9.43 | 16.39 | 16.00 | 39.8 | 71.0 |

## GW35

- Train rows: 130234
- Bank: 1.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Son Heung-min
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 74.85
- Actual score: 65.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.13) beats the best remaining Triple Captain opportunity (0.00).
- Chip advisory: triple_captain (0.64): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Eberechi Eze -> Anthony Gordon (projected gain 3.55, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (12.13) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Rodrigo Muniz Carvalho replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Bernd Leno | GK | 10 | 4.8 | 2.98 | 8.37 | 13.68 | 3.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.62 | 1.53 | 2.98 | 1.00 | 20.3 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.71 | 13.25 | 20.79 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.54 | 12.63 | 19.60 | 1.00 | 90.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.00 | 8.38 | 13.63 | 2.00 | 76.5 | 90.0 |
| Bench 3 | Bench | Kristoffer Ajer | DEF | 4 | 4.4 | 2.43 | 6.87 | 11.29 | 2.00 | 60.8 | 83.0 |
| Bench 4 | Bench | Mads Roerslev Rasmussen | DEF | 4 | 4.4 | 2.08 | 6.10 | 10.34 | 1.00 | 51.4 | 6.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 4.72 | 14.28 | 24.13 | 5.00 | 33.7 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.91 | 13.41 | 20.56 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.5 | 3.41 | 9.76 | 15.11 | 6.00 | 60.0 | 84.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 6.09 | 17.12 | 27.16 | 2.00 | 90.0 | 88.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.93 | 15.35 | 24.75 | 8.00 | 120.1 | 180.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.92 | 13.93 | 22.17 | 0.00 | 73.4 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.2 | 5.21 | 13.31 | 19.89 | 10.00 | 80.4 | 81.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 6.98 | 12.99 | 21.66 | 9.00 | 107.9 | 180.0 |