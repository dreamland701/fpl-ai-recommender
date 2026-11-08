# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 240.17
- Total actual points: 175.00
- Average predicted points: 60.04
- Average actual points: 43.75
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
- Bank: 100.00 -> 0.70
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Alfie Doughty
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 98.32
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.51) beats the best remaining Triple Captain opportunity (8.89).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.51) beats the best remaining Triple Captain opportunity (8.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.30 | 11.60 | 19.00 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.00 | 0.03 | 2.00 | 1.8 | 34.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.46 | 14.22 | 20.25 | 5.00 | 168.9 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.83 | 8.69 | 16.54 | 2.00 | 83.0 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.46 | 8.30 | 12.80 | 8.00 | 166.7 | 180.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.44 | 7.78 | 14.81 | 1.00 | 74.7 | 90.0 |
| Bench 4 | Bench | Emerson Palmieri dos Santos | DEF | 19 | 4.4 | 2.80 | 7.56 | 12.73 | 0.00 | 74.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.51 | 19.02 | 30.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.24 | 14.96 | 28.12 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.96 | 14.91 | 22.76 | 8.00 | 180.0 | 180.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.26 | 14.36 | 23.22 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.71 | 12.87 | 26.11 | 2.00 | 66.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.92 | 11.98 | 22.82 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 6.75 | 11.89 | 17.78 | 9.00 | 155.2 | 177.0 |
| Bench 3 | Bench | Douglas Luiz Soares de Paulo | MID | 2 | 5.7 | 3.16 | 9.74 | 16.11 | 2.00 | 70.8 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 0.70 -> 0.60
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Jarrod Bowen
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 38.23
- Actual score: 24.00
- Transfer: Emerson Palmieri dos Santos -> Antonee Robinson (projected gain 5.67, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.88 | 9.14 | 15.55 | 3.00 | 79.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.93 | 4.27 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.67 | 15.14 | 22.88 | 1.00 | 90.0 | 45.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 8.90 | 17.71 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.12 | 8.87 | 13.81 | 11.00 | 81.1 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 0.00 | 8.01 | 15.83 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 7.10 | 13.76 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 6.33 | 17.66 | 29.09 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 15.23 | 30.64 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 9.91 | 19.35 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.9 | 6.18 | 17.47 | 27.18 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 13.82 | 28.03 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 11.19 | 22.12 | 0.00 | 0.0 | 0.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.7 | 3.87 | 10.87 | 17.73 | 1.00 | 84.9 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 3.85 | 10.48 | 16.78 | 2.00 | 90.0 | 90.0 |

## GW30

- Train rows: 125995
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 41.99
- Actual score: 37.00
- Transfer: Alfie Doughty -> Cristian Romero (projected gain 2.51, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.45 | 10.82 | 17.85 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.52 | 0.92 | 8.00 | 10.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.29 | 8.27 | 17.02 | 7.00 | 48.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.02 | 8.25 | 13.67 | 1.00 | 73.8 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.1 | 2.97 | 8.10 | 10.70 | 2.00 | 69.1 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 1.66 | 6.46 | 13.34 | 6.00 | 38.9 | 90.0 |
| Bench 3 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 1.94 | 5.68 | 11.68 | 2.00 | 51.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.23 | 18.83 | 32.21 | 2.00 | 58.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.19 | 16.24 | 27.60 | 1.00 | 81.8 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.79 | 9.08 | 19.27 | 7.00 | 37.6 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.64 | 13.59 | 28.48 | 3.00 | 39.0 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.89 | 12.08 | 20.67 | 3.00 | 43.8 | 60.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 2.17 | 8.41 | 15.17 | 10.00 | 47.2 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.7 | 2.74 | 8.30 | 14.26 | 3.00 | 65.4 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 2.55 | 8.02 | 13.86 | 4.00 | 81.0 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 61.63
- Actual score: 54.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.02) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.02) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.58 | 8.12 | 13.84 | 0.00 | 66.0 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.53 | 3.81 | 5.61 | 2.00 | 45.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.26 | 11.40 | 22.28 | 7.00 | 78.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.76 | 9.69 | 18.71 | 6.00 | 71.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 2.96 | 8.42 | 13.27 | 1.00 | 77.3 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.1 | 2.89 | 8.36 | 13.55 | 1.00 | 76.4 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.76 | 7.71 | 14.86 | 7.00 | 75.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.12 | 21.36 | 36.01 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.48 | 12.28 | 23.85 | 2.00 | 74.7 | 89.0 |
| Bench 4 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.32 | 9.94 | 18.88 | 0.00 | 41.8 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.25 | 16.59 | 32.40 | 0.00 | 76.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.43 | 13.28 | 22.05 | 5.00 | 87.3 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.00 | 12.51 | 21.20 | 20.00 | 59.7 | 79.0 |
| Bench 2 | Bench Boost | Douglas Luiz Soares de Paulo | MID | 2 | 5.7 | 2.60 | 8.92 | 15.14 | 1.00 | 76.9 | 63.0 |
| Bench 3 | Bench Boost | Ross Barkley | MID | 12 | 4.9 | 2.57 | 8.29 | 13.94 | 2.00 | 90.0 | 90.0 |