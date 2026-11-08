# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 231.05
- Total actual points: 203.00
- Average predicted points: 57.76
- Average actual points: 50.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW27 are included before the first simulated week.
- League-average scores were not available for this run.

## GW28

- Train rows: 124319
- Bank: 100.00 -> 1.00
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Bukayo Saka
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 85.97
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.72) beats the best remaining Bench Boost opportunity (13.92).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.72) beats the best remaining Bench Boost opportunity (13.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.17 | 11.27 | 18.27 | 2.00 | 97.0 | 90.0 |
| Bench 1 | Bench Boost | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.68 | 9.15 | 15.22 | 0.00 | 89.1 | 55.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.86 | 13.08 | 20.42 | 2.00 | 84.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.56 | 12.11 | 18.93 | 1.00 | 77.4 | 90.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 3.22 | 10.58 | 17.28 | 2.00 | 85.6 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 4.9 | 3.39 | 9.59 | 15.67 | 6.00 | 63.4 | 75.0 |
| Bench 4 | Bench Boost | Lewis Dunk | DEF | 5 | 5.2 | 3.13 | 9.46 | 15.51 | 7.00 | 48.9 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.47 | 21.35 | 31.76 | 8.00 | 111.7 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.53 | 19.16 | 30.74 | 2.00 | 98.0 | 90.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.5 | 5.61 | 11.91 | 17.52 | 15.00 | 77.1 | 180.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.2 | 7.24 | 20.93 | 35.25 | 2.00 | 69.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.11 | 18.68 | 29.50 | 2.00 | 87.3 | 90.0 |
| Bench 2 | Bench Boost | Kevin De Bruyne | MID | 13 | 10.6 | 4.32 | 15.13 | 25.73 | 6.00 | 35.4 | 68.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.33 | 14.63 | 23.50 | 2.00 | 96.2 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.88 | 13.26 | 21.38 | 9.00 | 89.6 | 177.0 |

## GW29

- Train rows: 125157
- Bank: 1.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 50.50
- Actual score: 12.00
- Transfer: Lewis Dunk -> Alfie Doughty (projected gain 9.97, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.75 | 8.98 | 15.07 | 3.00 | 76.5 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.48 | 5.77 | 10.16 | 0.00 | 41.3 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 6.11 | 16.46 | 24.61 | 1.00 | 103.5 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 2.47 | 8.26 | 13.75 | 0.00 | 51.5 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 2.16 | 7.24 | 11.96 | 0.00 | 44.3 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 1.82 | 6.73 | 11.65 | 0.00 | 42.8 | 0.0 |
| Bench 4 | Bench | Pervis Estupiñán | DEF | 5 | 4.9 | 1.80 | 5.92 | 10.09 | 0.00 | 34.3 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.43 | 17.81 | 28.91 | 2.00 | 96.0 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 2.71 | 9.23 | 15.27 | 0.00 | 47.9 | 0.0 |
| Bench 2 | Bench | Antoine Semenyo | FWD | 3 | 4.5 | 2.41 | 7.39 | 11.94 | 0.00 | 61.4 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.70 | 18.26 | 27.90 | 2.00 | 123.6 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 4.31 | 14.07 | 23.95 | 0.00 | 52.3 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 3.87 | 11.11 | 17.55 | 2.00 | 97.0 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.26 | 10.46 | 17.14 | 0.00 | 47.3 | 0.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.6 | 3.01 | 10.39 | 18.04 | 0.00 | 37.8 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 1.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Son Heung-min
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 38.48
- Actual score: 45.00
- Transfer: Bukayo Saka -> Son Heung-min (projected gain 6.55, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.39 | 10.54 | 17.19 | 2.00 | 91.7 | 45.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.72 | 7.64 | 13.36 | 0.00 | 61.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 3.51 | 10.38 | 17.17 | 1.00 | 70.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.71 | 9.60 | 16.39 | 7.00 | 29.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 2.07 | 8.10 | 13.81 | 6.00 | 51.1 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 4.9 | 1.91 | 6.83 | 11.66 | 1.00 | 19.5 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.71 | 5.23 | 10.56 | 2.00 | 37.2 | 82.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 4.88 | 15.77 | 26.69 | 1.00 | 77.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.43 | 11.72 | 20.67 | 7.00 | 20.9 | 84.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.5 | 2.88 | 8.40 | 13.99 | 2.00 | 25.1 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.1 | 4.29 | 13.45 | 23.10 | 10.00 | 38.8 | 87.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.4 | 2.01 | 10.52 | 19.63 | 3.00 | 15.7 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 2.52 | 8.60 | 14.50 | 4.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 1.51 | 8.13 | 15.32 | 10.00 | 36.2 | 90.0 |
| Bench 2 | Bench | Phil Foden | MID | 13 | 8.1 | 1.57 | 6.98 | 11.61 | 3.00 | 20.7 | 60.0 |

## GW31

- Train rows: 126837
- Bank: 0.50 -> 1.70
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Son Heung-min
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 56.10
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.32) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Ollie Watkins -> Alexander Isak (projected gain 5.67, hit 0)
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (5.32) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Alfie Doughty replaced Pervis Estupiñán.
- Autosub: Ross Barkley replaced Kevin De Bruyne.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.13 | 6.78 | 12.29 | 0.00 | 23.0 | 0.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 1.59 | 5.03 | 8.67 | 0.00 | 44.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.30 | 11.34 | 18.57 | 7.00 | 80.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.04 | 10.35 | 16.77 | 6.00 | 75.7 | 90.0 |
| XI | Bench | Pervis Estupiñán | DEF | 5 | 4.9 | 3.38 | 9.28 | 14.84 | 0.00 | 73.5 | 0.0 |
| Bench 3 | Autosub In | Alfie Doughty | DEF | 12 | 4.7 | 2.43 | 8.52 | 14.48 | 1.00 | 78.1 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | 11 | 6.5 | 2.42 | 6.55 | 10.71 | 2.00 | 51.3 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 7.7 | 5.32 | 13.94 | 21.56 | 8.00 | 88.0 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.71 | 13.10 | 20.85 | 2.00 | 79.4 | 89.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.5 | 3.07 | 8.62 | 13.75 | 3.00 | 69.5 | 45.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 10.1 | 5.24 | 15.91 | 26.15 | 2.00 | 74.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.47 | 14.04 | 23.61 | 20.00 | 42.4 | 79.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.4 | 4.41 | 13.48 | 23.18 | 0.00 | 41.1 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.37 | 13.37 | 22.38 | 5.00 | 85.6 | 90.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.9 | 2.56 | 8.43 | 14.23 | 2.00 | 89.8 | 90.0 |