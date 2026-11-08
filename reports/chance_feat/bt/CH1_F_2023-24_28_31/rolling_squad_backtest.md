# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 225.41
- Total actual points: 173.00
- Average predicted points: 56.35
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
- Predicted score: 96.26
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.36) beats the best remaining Triple Captain opportunity (8.83).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.36) beats the best remaining Triple Captain opportunity (8.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.26 | 11.15 | 18.09 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.52 | 1.06 | 2.00 | 7.8 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.87 | 12.97 | 20.23 | 2.00 | 83.9 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.28 | 12.40 | 19.09 | 5.00 | 165.0 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.50 | 9.90 | 14.60 | 8.00 | 167.8 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.81 | 7.79 | 12.38 | 6.00 | 71.6 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.64 | 7.14 | 11.46 | 2.00 | 74.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.20 | 22.43 | 34.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.50 | 19.08 | 30.60 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.81 | 17.47 | 26.02 | 8.00 | 180.0 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.31 | 18.68 | 31.91 | 2.00 | 58.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.93 | 18.66 | 29.48 | 2.00 | 90.0 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.33 | 15.22 | 24.55 | 2.00 | 78.7 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.32 | 14.78 | 23.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.64 | 8.38 | 12.43 | 2.00 | 106.2 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.25
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.89 | 8.95 | 15.00 | 3.00 | 79.2 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.20 | 2.74 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.35 | 15.88 | 23.79 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.06 | 18.39 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.01 | 14.65 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.47 | 11.02 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.60 | 9.77 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.56 | 34.51 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.88 | 17.42 | 28.75 | 2.00 | 85.5 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.32 | 22.05 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.07 | 18.08 | 27.67 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.53 | 30.25 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.23 | 24.93 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.83 | 21.52 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.38 | 7.73 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.24
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.37 | 10.31 | 16.82 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.15 | 1.12 | 1.86 | 8.00 | 15.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.16 | 8.73 | 14.33 | 1.00 | 77.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.43 | 7.96 | 13.51 | 7.00 | 52.0 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.10 | 6.12 | 10.09 | 2.00 | 55.2 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.11 | 4.40 | 7.47 | 0.00 | 43.5 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.37 | 4.25 | 7.16 | 2.00 | 45.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.40 | 17.94 | 29.99 | 2.00 | 62.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.26 | 15.66 | 26.46 | 1.00 | 83.3 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.02 | 9.00 | 15.74 | 7.00 | 42.6 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.82 | 12.94 | 22.27 | 3.00 | 42.9 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.06 | 11.94 | 19.78 | 3.00 | 47.6 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.75 | 9.96 | 16.81 | 3.00 | 48.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.45 | 8.24 | 15.28 | 10.00 | 53.4 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.29 | 3.62 | 6.08 | 3.00 | 25.2 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.67
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.74) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.74) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.18 | 7.41 | 13.23 | 0.00 | 57.4 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.58 | 4.17 | 6.40 | 2.00 | 46.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.27 | 10.97 | 17.94 | 7.00 | 78.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.98 | 8.80 | 14.20 | 1.00 | 77.8 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.80 | 7.92 | 12.69 | 7.00 | 76.7 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.27 | 6.20 | 10.00 | 6.00 | 66.6 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.14 | 6.12 | 9.87 | 0.00 | 66.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.20 | 20.29 | 34.28 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.49 | 12.66 | 20.14 | 2.00 | 75.0 | 89.0 |
| Bench 2 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.16 | 9.12 | 18.13 | 0.00 | 38.3 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.25 | 16.34 | 26.72 | 0.00 | 76.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.58 | 13.57 | 22.65 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.13 | 12.21 | 20.46 | 20.00 | 62.5 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.57 | 12.06 | 20.05 | 11.00 | 74.6 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.85 | 5.28 | 8.62 | 6.00 | 40.2 | 26.0 |