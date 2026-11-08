# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 225.65
- Total actual points: 173.00
- Average predicted points: 56.41
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
- Predicted score: 96.70
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.42) beats the best remaining Triple Captain opportunity (8.86).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.42) beats the best remaining Triple Captain opportunity (8.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.32 | 11.26 | 18.20 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.01 | 0.67 | 1.16 | 2.00 | 11.7 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.93 | 13.10 | 20.39 | 2.00 | 85.3 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.33 | 12.38 | 19.00 | 5.00 | 166.5 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.58 | 9.95 | 14.63 | 8.00 | 170.0 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.87 | 7.90 | 12.50 | 6.00 | 73.0 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.71 | 7.26 | 11.57 | 2.00 | 75.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.22 | 22.51 | 34.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.55 | 19.18 | 30.72 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.87 | 17.45 | 25.91 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.93 | 18.70 | 29.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.06 | 18.10 | 31.00 | 2.00 | 52.5 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.39 | 15.34 | 24.67 | 2.00 | 80.0 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.37 | 14.84 | 23.77 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.78 | 8.48 | 12.51 | 2.00 | 109.9 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.09
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.98 | 9.11 | 15.19 | 3.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.38 | 2.83 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.36 | 15.79 | 23.57 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.04 | 18.44 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 8.89 | 14.56 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.44 | 11.05 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.57 | 9.81 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.72 | 34.65 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.60 | 16.66 | 27.62 | 2.00 | 78.9 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.22 | 22.01 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.08 | 18.02 | 27.51 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 16.92 | 29.07 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.35 | 25.01 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.76 | 21.49 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.31 | 7.69 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 43.24
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.44 | 10.45 | 16.98 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.28 | 1.27 | 1.96 | 8.00 | 19.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.23 | 8.86 | 14.49 | 1.00 | 78.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.55 | 8.21 | 13.82 | 7.00 | 55.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.20 | 6.33 | 10.35 | 2.00 | 57.8 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.23 | 4.65 | 7.75 | 0.00 | 46.7 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.49 | 4.49 | 7.43 | 2.00 | 48.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.52 | 18.23 | 30.39 | 2.00 | 65.7 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.34 | 15.84 | 26.67 | 1.00 | 85.3 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.11 | 9.25 | 16.10 | 7.00 | 45.3 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.73 | 13.34 | 23.36 | 3.00 | 41.8 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.18 | 12.18 | 20.08 | 3.00 | 50.7 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.86 | 10.17 | 17.05 | 3.00 | 50.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.57 | 8.57 | 15.74 | 10.00 | 56.4 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.42 | 3.83 | 6.29 | 3.00 | 28.7 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 59.62
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.48) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.48) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.05 | 6.56 | 11.61 | 0.00 | 54.3 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.53 | 4.05 | 6.31 | 2.00 | 46.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.22 | 10.93 | 18.00 | 7.00 | 77.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.90 | 8.72 | 14.22 | 1.00 | 76.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.73 | 7.85 | 12.74 | 7.00 | 75.2 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.22 | 6.14 | 10.02 | 6.00 | 65.5 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.10 | 6.08 | 9.92 | 0.00 | 65.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.13 | 20.26 | 34.37 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.41 | 12.58 | 20.17 | 2.00 | 73.3 | 89.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.05 | 8.38 | 16.71 | 0.00 | 35.7 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.22 | 16.31 | 26.75 | 0.00 | 76.4 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.53 | 13.54 | 22.72 | 5.00 | 89.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.09 | 12.20 | 20.56 | 20.00 | 62.0 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.50 | 11.98 | 20.03 | 11.00 | 73.0 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.81 | 5.22 | 8.63 | 6.00 | 39.8 | 26.0 |