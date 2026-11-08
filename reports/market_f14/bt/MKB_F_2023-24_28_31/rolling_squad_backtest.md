# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 224.22
- Total actual points: 173.00
- Average predicted points: 56.05
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
- Predicted score: 96.79
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.50) beats the best remaining Triple Captain opportunity (8.88).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.50) beats the best remaining Triple Captain opportunity (8.88).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.36 | 11.43 | 18.48 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.29 | 0.67 | 2.00 | 1.2 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.73 | 12.64 | 19.78 | 2.00 | 83.5 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.06 | 12.02 | 18.53 | 5.00 | 171.1 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.54 | 10.13 | 14.96 | 8.00 | 167.2 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.72 | 7.63 | 12.15 | 6.00 | 70.6 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.61 | 7.10 | 11.39 | 2.00 | 72.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.24 | 22.70 | 35.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.40 | 18.90 | 30.40 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.95 | 17.74 | 26.45 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.02 | 19.02 | 30.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.61 | 18.70 | 31.62 | 2.00 | 67.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.30 | 14.72 | 23.62 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Martin Ødegaard | MID | 1 | 8.5 | 5.10 | 14.62 | 23.70 | 2.00 | 76.1 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.71 | 8.65 | 12.87 | 2.00 | 105.8 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Jarrod Bowen
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 27.17
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.89 | 9.05 | 15.18 | 3.00 | 79.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.13 | 2.62 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.60 | 16.27 | 24.35 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.14 | 18.57 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.55 | 15.50 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.54 | 11.17 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.77 | 10.06 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.30 | 34.23 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 6.28 | 17.70 | 28.78 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.89 | 22.98 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 18.26 | 31.15 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.9 | 6.13 | 18.18 | 27.80 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.31 | 25.11 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.62 | 21.26 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.62 | 8.12 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 40.04
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 3.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.44 | 10.55 | 17.22 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.12 | 1.08 | 1.74 | 8.00 | 9.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.02 | 8.45 | 13.91 | 1.00 | 73.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.14 | 7.34 | 12.66 | 7.00 | 49.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 1.87 | 5.68 | 9.46 | 2.00 | 52.1 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.94 | 4.04 | 6.91 | 0.00 | 39.2 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.13 | 3.75 | 6.44 | 2.00 | 41.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.29 | 17.91 | 30.00 | 2.00 | 58.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.19 | 15.60 | 26.38 | 1.00 | 81.8 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.72 | 8.47 | 14.99 | 7.00 | 38.0 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.49 | 12.25 | 21.31 | 3.00 | 39.3 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.05 | 12.07 | 19.98 | 3.00 | 42.8 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.37 | 9.10 | 15.57 | 3.00 | 42.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.17 | 7.73 | 14.58 | 10.00 | 47.2 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.03 | 3.06 | 5.26 | 3.00 | 21.8 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.21
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.65) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.65) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.49 | 7.50 | 13.01 | 0.00 | 66.7 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.75 | 4.55 | 6.91 | 2.00 | 45.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.29 | 11.02 | 18.06 | 7.00 | 78.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.87 | 8.52 | 13.80 | 1.00 | 77.7 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.74 | 7.79 | 12.51 | 7.00 | 75.8 | 90.0 |
| Bench 2 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.16 | 5.92 | 9.61 | 6.00 | 65.8 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 1.99 | 5.75 | 9.34 | 0.00 | 64.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.16 | 20.32 | 34.35 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.43 | 12.52 | 19.94 | 2.00 | 74.9 | 89.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 2.28 | 8.80 | 17.24 | 0.00 | 42.1 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.21 | 16.19 | 26.54 | 0.00 | 77.2 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.33 | 12.95 | 21.75 | 5.00 | 87.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.17 | 12.41 | 20.75 | 20.00 | 59.3 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.45 | 11.75 | 19.60 | 11.00 | 71.7 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.75 | 5.02 | 8.22 | 6.00 | 38.7 | 26.0 |