# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 226.86
- Total actual points: 173.00
- Average predicted points: 56.71
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
- Predicted score: 98.01
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.97) beats the best remaining Triple Captain opportunity (8.44).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.97) beats the best remaining Triple Captain opportunity (8.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.06 | 10.55 | 16.87 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.56 | 0.99 | 2.00 | 8.2 | 34.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 9.03 | 12.83 | 19.95 | 5.00 | 173.1 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.79 | 12.66 | 19.94 | 2.00 | 84.8 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.47 | 9.83 | 14.47 | 8.00 | 171.4 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.86 | 7.95 | 12.84 | 6.00 | 74.2 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.48 | 6.84 | 11.09 | 2.00 | 75.7 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 6.83 | 21.74 | 33.33 | 2.00 | 85.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.39 | 18.50 | 29.80 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 12.42 | 17.46 | 25.50 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.06 | 18.84 | 30.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.09 | 17.24 | 29.08 | 2.00 | 54.6 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.30 | 15.03 | 24.03 | 2.00 | 79.5 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.18 | 14.07 | 22.46 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.74 | 8.44 | 12.69 | 2.00 | 109.1 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Alfie Doughty
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.47
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.64 | 8.28 | 13.79 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.39 | 2.88 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.83 | 16.35 | 24.56 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.44 | 19.12 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 8.88 | 14.63 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.88 | 11.91 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.80 | 10.16 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.19 | 33.61 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.75 | 16.12 | 26.34 | 2.00 | 83.1 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.19 | 22.00 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.13 | 17.58 | 26.71 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.13 | 29.26 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 16.41 | 26.86 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 13.11 | 22.20 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.98 | 8.72 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 41.59
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.29, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.20 | 9.87 | 16.02 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.22 | 1.07 | 1.64 | 8.00 | 15.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.11 | 8.47 | 14.09 | 1.00 | 77.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.42 | 8.12 | 13.76 | 7.00 | 51.7 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.08 | 6.03 | 10.15 | 2.00 | 55.8 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.20 | 4.77 | 8.28 | 0.00 | 44.5 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.47 | 4.38 | 7.56 | 2.00 | 46.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.29 | 18.59 | 30.82 | 2.00 | 58.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.11 | 15.64 | 26.24 | 1.00 | 82.5 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.14 | 9.39 | 16.28 | 7.00 | 41.9 | 84.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.33 | 13.52 | 22.33 | 3.00 | 49.7 | 60.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.57 | 12.78 | 22.40 | 3.00 | 42.3 | 77.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.73 | 10.01 | 17.18 | 3.00 | 48.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.34 | 7.91 | 15.10 | 10.00 | 52.8 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.42 | 3.88 | 6.54 | 3.00 | 26.7 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.79
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.77) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.77) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 1.87 | 5.75 | 10.37 | 0.00 | 54.4 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.59 | 3.95 | 5.88 | 2.00 | 46.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.28 | 11.24 | 18.18 | 7.00 | 78.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.13 | 8.94 | 14.44 | 1.00 | 80.5 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.86 | 7.83 | 12.56 | 7.00 | 78.5 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.32 | 6.50 | 10.51 | 6.00 | 68.4 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.16 | 6.16 | 9.90 | 0.00 | 68.0 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.99 | 19.94 | 33.36 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.70 | 13.08 | 20.65 | 2.00 | 77.1 | 89.0 |
| Bench 4 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 1.89 | 8.20 | 16.45 | 0.00 | 36.1 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.29 | 16.43 | 26.72 | 0.00 | 76.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.53 | 12.97 | 21.51 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.34 | 12.85 | 21.31 | 20.00 | 65.1 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.72 | 12.47 | 20.60 | 11.00 | 75.6 | 90.0 |
| Bench 3 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 2.14 | 5.83 | 9.37 | 6.00 | 42.8 | 26.0 |