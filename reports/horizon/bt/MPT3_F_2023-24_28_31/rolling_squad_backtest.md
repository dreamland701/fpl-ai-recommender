# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 238.80
- Total actual points: 164.00
- Average predicted points: 59.70
- Average actual points: 41.00
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
- Predicted score: 97.30
- Actual score: 60.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.35) beats the best remaining Triple Captain opportunity (8.85).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.35) beats the best remaining Triple Captain opportunity (8.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.26 | 11.51 | 18.86 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.34 | 0.86 | 2.00 | 7.7 | 34.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.27 | 13.92 | 19.85 | 5.00 | 164.7 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.87 | 8.77 | 16.67 | 2.00 | 84.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.50 | 8.37 | 12.92 | 8.00 | 167.8 | 180.0 |
| Bench 2 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.47 | 7.83 | 14.89 | 1.00 | 75.4 | 90.0 |
| Bench 4 | Bench | Emerson Palmieri dos Santos | DEF | 19 | 4.4 | 2.84 | 7.67 | 12.92 | 0.00 | 74.9 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.51 | 19.03 | 30.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.21 | 14.90 | 28.01 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.80 | 14.70 | 22.47 | 8.00 | 180.0 | 180.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.32 | 14.53 | 23.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.93 | 12.02 | 22.90 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 6.81 | 12.01 | 17.94 | 9.00 | 156.4 | 177.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.21 | 12.00 | 24.45 | 2.00 | 55.7 | 90.0 |
| Bench 3 | Bench | Douglas Luiz Soares de Paulo | MID | 2 | 5.7 | 3.26 | 10.02 | 16.54 | 2.00 | 73.1 | 90.0 |

## GW29

- Train rows: 125157
- Bank: 0.70 -> 0.20
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 38.72
- Actual score: 16.00
- Transfer: Gabriel dos Santos Magalhães -> Pedro Porro (projected gain 3.30, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.89 | 9.17 | 15.59 | 3.00 | 79.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 2.05 | 4.45 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.34 | 14.34 | 21.65 | 1.00 | 90.0 | 45.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.31 | 11.45 | 17.40 | 1.00 | 80.8 | 90.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 8.84 | 17.56 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 6.83 | 13.24 | 0.00 | 0.0 | 0.0 |
| XI | XI | Emerson Palmieri dos Santos | DEF | 19 | 4.4 | 0.63 | 2.87 | 5.89 | 2.00 | 26.9 | 83.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.76 | 16.19 | 26.82 | 2.00 | 82.7 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 15.29 | 30.69 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 9.64 | 18.82 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.06 | 17.16 | 26.71 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 12.79 | 26.07 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 11.16 | 22.02 | 0.00 | 0.0 | 0.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.7 | 3.86 | 10.86 | 17.72 | 1.00 | 84.8 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 3.81 | 10.42 | 16.71 | 2.00 | 90.0 | 90.0 |

## GW30

- Train rows: 125995
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.64
- Actual score: 37.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 5.00, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.37 | 10.61 | 17.52 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.15 | 1.03 | 1.71 | 8.00 | 15.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.17 | 8.65 | 14.28 | 1.00 | 77.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.44 | 8.64 | 17.69 | 7.00 | 52.2 | 90.0 |
| Bench 4 | Bench | Emerson Palmieri dos Santos | DEF | 19 | 4.4 | 1.92 | 6.44 | 10.71 | 0.00 | 63.0 | 90.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.12 | 6.11 | 8.51 | 2.00 | 44.4 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.12 | 6.10 | 12.47 | 2.00 | 55.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.42 | 19.27 | 32.86 | 2.00 | 62.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.27 | 16.42 | 27.86 | 1.00 | 83.5 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.03 | 9.67 | 20.36 | 7.00 | 43.1 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.83 | 14.05 | 29.29 | 3.00 | 43.2 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.08 | 12.54 | 21.37 | 3.00 | 47.9 | 60.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 2.47 | 9.19 | 16.38 | 10.00 | 54.0 | 90.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.7 | 2.88 | 8.67 | 14.83 | 3.00 | 68.6 | 90.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 2.61 | 8.18 | 14.12 | 4.00 | 82.3 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.14
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.38) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.38) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.09 | 6.85 | 11.89 | 0.00 | 55.1 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.58 | 3.94 | 5.82 | 2.00 | 46.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.27 | 11.45 | 22.34 | 7.00 | 78.9 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.05 | 8.64 | 13.73 | 2.00 | 68.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.98 | 8.49 | 13.39 | 1.00 | 77.8 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.81 | 7.83 | 15.11 | 7.00 | 76.8 | 90.0 |
| Bench 3 | Bench Boost | Emerson Palmieri dos Santos | DEF | 19 | 4.4 | 2.17 | 6.73 | 11.04 | 2.00 | 66.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.20 | 21.58 | 36.29 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.50 | 12.34 | 23.98 | 2.00 | 75.2 | 89.0 |
| Bench 4 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.07 | 9.32 | 17.90 | 0.00 | 36.2 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.25 | 16.60 | 32.38 | 0.00 | 76.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.59 | 13.69 | 22.69 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.13 | 12.87 | 21.73 | 20.00 | 62.6 | 79.0 |
| XI | XI | Douglas Luiz Soares de Paulo | MID | 2 | 5.7 | 2.69 | 9.17 | 15.53 | 1.00 | 78.9 | 63.0 |
| Bench 2 | Bench Boost | Ross Barkley | MID | 12 | 4.9 | 2.56 | 8.28 | 13.91 | 2.00 | 90.0 | 90.0 |