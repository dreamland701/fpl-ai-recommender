# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 225.17
- Total actual points: 173.00
- Average predicted points: 56.29
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
- Predicted score: 96.13
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.31) beats the best remaining Triple Captain opportunity (8.82).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.31) beats the best remaining Triple Captain opportunity (8.82).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.31 | 11.25 | 18.17 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.65 | 1.13 | 2.00 | 11.5 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.91 | 13.08 | 20.34 | 2.00 | 85.1 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.25 | 12.27 | 18.82 | 5.00 | 165.2 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.54 | 9.89 | 14.53 | 8.00 | 169.1 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.86 | 7.89 | 12.48 | 6.00 | 72.9 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.70 | 7.26 | 11.58 | 2.00 | 75.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.19 | 22.49 | 34.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.54 | 19.17 | 30.67 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.76 | 17.34 | 25.72 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.90 | 18.63 | 29.39 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.07 | 18.25 | 31.09 | 2.00 | 53.1 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.38 | 15.33 | 24.64 | 2.00 | 80.2 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.34 | 14.79 | 23.68 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.76 | 8.48 | 12.49 | 2.00 | 109.7 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 25.95
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.99 | 9.16 | 15.25 | 3.00 | 81.8 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.36 | 2.80 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.27 | 15.57 | 23.26 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.03 | 18.41 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 8.91 | 14.58 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.45 | 11.07 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.59 | 9.83 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.75 | 34.60 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.71 | 16.36 | 27.97 | 2.00 | 75.8 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.29 | 22.03 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 5.99 | 17.79 | 27.16 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 16.94 | 29.02 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.33 | 24.94 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.76 | 21.46 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.31 | 7.68 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 43.34
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.43 | 10.43 | 16.93 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.27 | 1.26 | 1.93 | 8.00 | 18.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.25 | 8.91 | 14.55 | 1.00 | 79.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.54 | 8.20 | 13.80 | 7.00 | 55.0 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.21 | 6.34 | 10.36 | 2.00 | 57.8 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.23 | 4.64 | 7.74 | 0.00 | 46.7 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.48 | 4.48 | 7.41 | 2.00 | 48.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.49 | 18.26 | 30.38 | 2.00 | 65.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.36 | 15.93 | 26.77 | 1.00 | 85.8 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.15 | 9.38 | 16.24 | 7.00 | 45.9 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.75 | 13.48 | 23.50 | 3.00 | 42.9 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.16 | 12.20 | 20.09 | 3.00 | 50.9 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.84 | 10.16 | 17.02 | 3.00 | 50.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.66 | 8.82 | 16.09 | 10.00 | 58.2 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.41 | 3.83 | 6.28 | 3.00 | 28.7 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 59.74
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.55) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.55) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.09 | 6.65 | 11.73 | 0.00 | 54.9 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.53 | 4.06 | 6.32 | 2.00 | 46.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.22 | 10.93 | 17.97 | 7.00 | 77.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.90 | 8.70 | 14.20 | 1.00 | 76.0 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.74 | 7.87 | 12.75 | 7.00 | 75.2 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.22 | 6.15 | 10.04 | 6.00 | 65.6 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.10 | 6.09 | 9.92 | 0.00 | 65.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.12 | 20.27 | 34.34 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.41 | 12.58 | 20.14 | 2.00 | 73.3 | 89.0 |
| Bench 2 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.11 | 8.27 | 17.39 | 0.00 | 34.3 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.22 | 16.31 | 26.72 | 0.00 | 76.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.54 | 13.58 | 22.78 | 5.00 | 89.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.10 | 12.27 | 20.63 | 20.00 | 62.5 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.50 | 11.99 | 20.03 | 11.00 | 73.1 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.81 | 5.23 | 8.64 | 6.00 | 39.8 | 26.0 |