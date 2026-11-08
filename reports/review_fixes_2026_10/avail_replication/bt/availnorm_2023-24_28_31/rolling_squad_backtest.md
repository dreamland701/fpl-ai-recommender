# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 221.05
- Total actual points: 237.00
- Average predicted points: 55.26
- Average actual points: 59.25
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
- Predicted score: 79.80
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.73) beats the best remaining Bench Boost opportunity (12.87).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.73) beats the best remaining Bench Boost opportunity (12.87).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.87 | 10.45 | 16.96 | 2.00 | 98.0 | 90.0 |
| Bench 1 | Bench Boost | Ederson Santana de Moraes | GK | 13 | 5.5 | 2.50 | 8.57 | 14.27 | 0.00 | 86.1 | 55.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.53 | 12.15 | 18.96 | 2.00 | 83.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.23 | 11.21 | 17.51 | 1.00 | 75.4 | 90.0 |
| Bench 3 | Bench Boost | Virgil van Dijk | DEF | 11 | 6.4 | 2.98 | 9.85 | 16.09 | 2.00 | 84.6 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 4.9 | 3.14 | 8.81 | 14.36 | 6.00 | 52.4 | 75.0 |
| Bench 4 | Bench Boost | Lewis Dunk | DEF | 5 | 5.2 | 2.91 | 8.74 | 14.29 | 7.00 | 59.9 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 8.83 | 20.07 | 29.83 | 8.00 | 126.7 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.04 | 17.79 | 28.62 | 2.00 | 99.0 | 90.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.5 | 5.13 | 10.90 | 15.89 | 15.00 | 87.1 | 180.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.2 | 6.66 | 19.26 | 32.43 | 2.00 | 63.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.64 | 17.31 | 27.41 | 2.00 | 99.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.11 | 14.01 | 22.49 | 2.00 | 94.2 | 90.0 |
| Bench 2 | Bench Boost | Kevin De Bruyne | MID | 13 | 10.6 | 3.98 | 13.82 | 23.45 | 6.00 | 52.4 | 68.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 5.43 | 12.18 | 19.38 | 9.00 | 104.6 | 177.0 |

## GW29

- Train rows: 125157
- Bank: 1.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 56.52
- Actual score: 12.00
- Transfer: Lewis Dunk -> Alfie Doughty (projected gain 11.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.34 | 10.72 | 17.90 | 3.00 | 78.5 | 90.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.64 | 5.92 | 10.42 | 0.00 | 51.3 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 6.93 | 18.80 | 28.28 | 1.00 | 123.5 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 2.67 | 8.57 | 14.21 | 0.00 | 70.5 | 0.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 2.33 | 7.49 | 12.33 | 0.00 | 62.3 | 0.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 1.99 | 6.93 | 11.96 | 0.00 | 57.8 | 0.0 |
| Bench 4 | Bench | Pervis Estupiñán | DEF | 5 | 4.9 | 1.88 | 5.80 | 9.90 | 0.00 | 43.3 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 7.46 | 20.70 | 33.48 | 2.00 | 98.0 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 3.12 | 10.45 | 17.36 | 0.00 | 67.9 | 0.0 |
| Bench 2 | Bench | Antoine Semenyo | FWD | 3 | 4.5 | 2.77 | 8.42 | 13.73 | 0.00 | 81.4 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 7.52 | 20.71 | 31.85 | 2.00 | 121.6 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 4.41 | 14.45 | 25.40 | 0.00 | 68.3 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 4.55 | 12.90 | 20.27 | 2.00 | 98.0 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.62 | 11.41 | 19.24 | 0.00 | 67.3 | 0.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.6 | 3.03 | 9.95 | 17.25 | 0.00 | 45.8 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 1.50 -> 3.60
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Ollie Watkins
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 34.60
- Actual score: 64.00
- Transfer: Jarrod Bowen -> Cole Palmer (projected gain 3.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.97 | 9.26 | 15.08 | 2.00 | 93.7 | 45.0 |
| Bench 1 | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.52 | 6.55 | 11.42 | 0.00 | 44.4 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 3.11 | 9.19 | 15.24 | 1.00 | 56.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.34 | 8.26 | 14.08 | 7.00 | 48.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 1.75 | 6.75 | 11.48 | 6.00 | 38.1 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 4.9 | 1.74 | 6.07 | 10.26 | 1.00 | 31.5 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.31 | 3.71 | 8.08 | 2.00 | 35.2 | 82.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 4.15 | 13.66 | 23.25 | 1.00 | 76.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.75 | 9.27 | 16.29 | 7.00 | 32.9 | 84.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.5 | 2.44 | 7.08 | 11.77 | 2.00 | 44.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 5.8 | 4.57 | 11.73 | 18.98 | 15.00 | 67.7 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.4 | 2.08 | 9.64 | 17.60 | 3.00 | 16.7 | 90.0 |
| Bench 2 | Bench | Bukayo Saka | MID | 1 | 9.1 | 1.20 | 8.67 | 15.89 | 3.00 | 33.6 | 77.0 |
| Bench 3 | Bench | Phil Foden | MID | 13 | 8.1 | 0.77 | 7.63 | 13.35 | 3.00 | 40.7 | 60.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 2.14 | 7.47 | 12.74 | 4.00 | 79.6 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 3.60 -> 4.80
- Free transfers: 2 -> 2
- Captain: Alexander Isak
- Vice captain: Dominic Solanke
- Effective captain: Alexander Isak
- Chip used: triple_captain
- Predicted score: 50.13
- Actual score: 87.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.85) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Ollie Watkins -> Alexander Isak (projected gain 5.91, hit 0)
- Chip used: Triple Captain on Alexander Isak. Optimizer chose Triple Captain here because the current estimated captain upside (4.85) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Virgil van Dijk replaced Pervis Estupiñán.
- Autosub: Ross Barkley replaced Bukayo Saka.
- Autosub: Alfie Doughty replaced Kevin De Bruyne.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Ederson Santana de Moraes | GK | 13 | 5.5 | 1.89 | 6.00 | 10.86 | 0.00 | 34.0 | 0.0 |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 1.24 | 4.08 | 7.45 | 0.00 | 64.4 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 3.85 | 10.13 | 16.59 | 7.00 | 77.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.62 | 9.24 | 14.97 | 6.00 | 70.7 | 90.0 |
| XI | Bench | Pervis Estupiñán | DEF | 5 | 4.9 | 3.04 | 8.35 | 13.35 | 0.00 | 62.5 | 0.0 |
| Bench 4 | Autosub In | Alfie Doughty | DEF | 12 | 4.7 | 2.11 | 7.56 | 12.80 | 1.00 | 77.1 | 90.0 |
| Bench 3 | Autosub In | Virgil van Dijk | DEF | 11 | 6.5 | 2.25 | 5.94 | 9.70 | 2.00 | 71.3 | 90.0 |
| Captain | Captain | Alexander Isak | FWD | 15 | 7.7 | 4.85 | 12.71 | 19.66 | 8.00 | 80.0 | 90.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.20 | 11.72 | 18.63 | 2.00 | 76.4 | 89.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.5 | 2.70 | 7.60 | 12.13 | 3.00 | 64.5 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.97 | 12.46 | 20.95 | 20.00 | 56.4 | 79.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.0 | 4.19 | 12.34 | 20.71 | 0.00 | 76.7 | 0.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.4 | 3.98 | 12.16 | 20.94 | 0.00 | 60.1 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.8 | 4.14 | 11.81 | 18.51 | 20.00 | 72.8 | 90.0 |
| Bench 2 | Autosub In | Ross Barkley | MID | 12 | 4.9 | 2.26 | 7.56 | 12.82 | 2.00 | 89.8 | 90.0 |