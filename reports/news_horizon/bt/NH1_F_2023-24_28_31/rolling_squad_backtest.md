# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 225.67
- Total actual points: 173.00
- Average predicted points: 56.42
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
- Predicted score: 96.04
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.34) beats the best remaining Triple Captain opportunity (8.83).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.34) beats the best remaining Triple Captain opportunity (8.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.26 | 11.16 | 18.10 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.50 | 1.07 | 2.00 | 7.5 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.87 | 12.98 | 20.26 | 2.00 | 83.9 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.23 | 12.38 | 19.11 | 5.00 | 163.9 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.49 | 9.90 | 14.62 | 8.00 | 167.4 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.82 | 7.80 | 12.39 | 6.00 | 71.8 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.66 | 7.15 | 11.44 | 2.00 | 74.6 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.19 | 22.46 | 34.58 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.49 | 19.08 | 30.64 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.79 | 17.46 | 26.03 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.91 | 18.67 | 29.54 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.26 | 18.38 | 31.40 | 2.00 | 56.8 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.35 | 15.24 | 24.55 | 2.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.33 | 14.78 | 23.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.63 | 8.38 | 12.45 | 2.00 | 105.8 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.11
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.90 | 8.97 | 15.00 | 3.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.19 | 2.77 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.31 | 15.83 | 23.80 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.09 | 18.40 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.03 | 14.68 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.49 | 11.04 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.62 | 9.78 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.57 | 34.46 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.81 | 17.11 | 28.27 | 2.00 | 83.8 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.34 | 22.10 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.04 | 18.04 | 27.67 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.60 | 30.47 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.24 | 24.94 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.85 | 21.52 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.39 | 7.76 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.62
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.38 | 10.32 | 16.82 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.13 | 1.10 | 1.88 | 8.00 | 14.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.17 | 8.74 | 14.33 | 1.00 | 77.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.46 | 7.99 | 13.51 | 7.00 | 52.6 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.14 | 6.16 | 10.08 | 2.00 | 55.9 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.14 | 4.43 | 7.45 | 0.00 | 44.2 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.40 | 4.28 | 7.13 | 2.00 | 46.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.44 | 17.96 | 29.93 | 2.00 | 63.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.28 | 15.68 | 26.45 | 1.00 | 83.8 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.05 | 9.04 | 15.73 | 7.00 | 43.3 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.85 | 12.98 | 22.26 | 3.00 | 43.7 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.10 | 11.96 | 19.75 | 3.00 | 48.3 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.79 | 9.99 | 16.79 | 3.00 | 48.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.51 | 8.31 | 15.25 | 10.00 | 54.8 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.31 | 3.64 | 6.08 | 3.00 | 25.6 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.90
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.72) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.72) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.16 | 7.15 | 12.73 | 0.00 | 56.7 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.55 | 4.14 | 6.44 | 2.00 | 46.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.28 | 10.99 | 17.94 | 7.00 | 79.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.00 | 8.82 | 14.20 | 1.00 | 78.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.82 | 7.94 | 12.69 | 7.00 | 77.1 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.29 | 6.21 | 9.99 | 6.00 | 66.9 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.16 | 6.14 | 9.86 | 0.00 | 66.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.23 | 20.31 | 34.22 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.51 | 12.68 | 20.15 | 2.00 | 75.4 | 89.0 |
| Bench 2 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.17 | 8.89 | 17.60 | 0.00 | 38.3 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.29 | 16.37 | 26.69 | 0.00 | 77.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.63 | 13.61 | 22.62 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.16 | 12.23 | 20.43 | 20.00 | 63.2 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.59 | 12.07 | 20.03 | 11.00 | 74.9 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.85 | 5.28 | 8.62 | 6.00 | 40.2 | 26.0 |