# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 225.91
- Total actual points: 173.00
- Average predicted points: 56.48
- Average actual points: 43.25
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Alfie Doughty
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 97.17
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.63) beats the best remaining Triple Captain opportunity (8.70).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.63) beats the best remaining Triple Captain opportunity (8.70).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.13 | 10.76 | 17.24 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.68 | 1.25 | 2.00 | 5.7 | 34.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.77 | 12.81 | 19.85 | 5.00 | 170.2 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.80 | 12.69 | 19.83 | 2.00 | 85.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.50 | 9.87 | 14.58 | 8.00 | 171.7 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.83 | 7.85 | 12.58 | 6.00 | 74.0 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.56 | 6.99 | 11.25 | 2.00 | 76.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.09 | 22.43 | 34.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.41 | 18.68 | 29.97 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 12.08 | 17.35 | 25.55 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.05 | 18.91 | 30.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.14 | 17.52 | 29.56 | 2.00 | 56.3 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.34 | 15.18 | 24.37 | 2.00 | 79.0 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.24 | 14.41 | 23.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.68 | 8.39 | 12.53 | 2.00 | 107.4 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.24
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.73 | 8.49 | 14.10 | 3.00 | 77.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.41 | 3.02 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.62 | 16.17 | 24.25 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.14 | 18.58 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 8.89 | 14.62 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.63 | 11.46 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.66 | 9.94 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.62 | 34.46 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.73 | 16.23 | 26.39 | 2.00 | 82.9 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.20 | 22.03 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.08 | 17.76 | 27.03 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.02 | 29.14 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 16.07 | 26.32 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 13.08 | 22.09 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.65 | 8.17 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 41.97
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.39, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.26 | 9.97 | 16.14 | 2.00 | 89.6 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.24 | 1.23 | 1.95 | 8.00 | 12.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.13 | 8.59 | 14.18 | 1.00 | 78.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.40 | 8.00 | 13.52 | 7.00 | 53.4 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.10 | 6.16 | 10.29 | 2.00 | 57.4 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.17 | 4.65 | 7.99 | 0.00 | 45.2 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.44 | 4.37 | 7.48 | 2.00 | 47.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.40 | 18.67 | 31.04 | 2.00 | 62.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.13 | 15.50 | 26.04 | 1.00 | 82.6 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.09 | 9.31 | 16.18 | 7.00 | 42.8 | 84.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.25 | 13.05 | 21.56 | 3.00 | 50.0 | 60.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.67 | 12.86 | 22.25 | 3.00 | 43.6 | 77.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.78 | 10.16 | 17.28 | 3.00 | 49.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.36 | 8.02 | 15.10 | 10.00 | 53.4 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.36 | 3.73 | 6.24 | 3.00 | 26.2 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.53
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.68) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.68) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 1.95 | 6.04 | 10.71 | 0.00 | 51.9 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.62 | 4.16 | 6.29 | 2.00 | 44.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.24 | 10.99 | 17.83 | 7.00 | 80.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.05 | 8.86 | 14.31 | 1.00 | 80.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.83 | 7.87 | 12.65 | 7.00 | 78.8 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.29 | 6.36 | 10.26 | 6.00 | 68.5 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.14 | 6.08 | 9.83 | 0.00 | 68.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.09 | 20.24 | 33.99 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.59 | 12.83 | 20.27 | 2.00 | 75.7 | 89.0 |
| Bench 4 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 1.93 | 8.15 | 16.23 | 0.00 | 35.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.24 | 16.26 | 26.43 | 0.00 | 76.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.53 | 13.08 | 21.80 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.27 | 12.66 | 21.08 | 20.00 | 64.5 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.68 | 12.39 | 20.51 | 11.00 | 75.3 | 90.0 |
| Bench 3 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.99 | 5.48 | 8.86 | 6.00 | 41.2 | 26.0 |