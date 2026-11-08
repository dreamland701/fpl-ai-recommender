# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 227.43
- Total actual points: 173.00
- Average predicted points: 56.86
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
- Predicted score: 97.28
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.53) beats the best remaining Triple Captain opportunity (8.97).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.53) beats the best remaining Triple Captain opportunity (8.97).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.40 | 11.13 | 18.09 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.83 | 1.37 | 2.00 | 8.3 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.88 | 12.99 | 20.34 | 2.00 | 85.4 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 7.92 | 11.78 | 18.19 | 5.00 | 167.5 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.79 | 9.76 | 14.44 | 8.00 | 169.9 | 180.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.83 | 7.97 | 12.61 | 6.00 | 72.6 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.85 | 7.39 | 11.73 | 2.00 | 74.6 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.31 | 22.86 | 35.19 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.48 | 19.02 | 30.56 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.98 | 17.38 | 25.77 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.03 | 19.05 | 30.03 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.17 | 17.85 | 30.20 | 2.00 | 56.0 | 90.0 |
| Bench 2 | Bench | Martin Ødegaard | MID | 1 | 8.5 | 5.32 | 15.25 | 24.63 | 2.00 | 79.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.44 | 14.74 | 23.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.91 | 8.29 | 12.29 | 2.00 | 108.3 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 25.78
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.89 | 9.05 | 15.13 | 3.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.41 | 3.07 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.11 | 15.05 | 22.63 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.10 | 18.50 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.10 | 14.71 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.80 | 11.51 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.95 | 10.25 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.83 | 34.99 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.68 | 16.34 | 26.69 | 2.00 | 82.8 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.45 | 22.18 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.04 | 18.03 | 27.51 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 16.93 | 29.09 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.52 | 25.42 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.84 | 21.58 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.45 | 7.73 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 43.13
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.62, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.43 | 10.48 | 17.03 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.28 | 1.41 | 2.21 | 8.00 | 15.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.32 | 8.85 | 14.55 | 1.00 | 77.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.54 | 8.21 | 13.82 | 7.00 | 53.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.07 | 6.10 | 10.09 | 2.00 | 56.6 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.23 | 4.81 | 8.00 | 0.00 | 44.2 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.40 | 4.44 | 7.49 | 2.00 | 46.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.55 | 18.27 | 30.64 | 2.00 | 63.0 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.20 | 15.53 | 26.35 | 1.00 | 84.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.97 | 9.03 | 15.83 | 7.00 | 43.7 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.92 | 13.14 | 22.58 | 3.00 | 43.7 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.21 | 12.26 | 20.37 | 3.00 | 47.7 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.86 | 10.16 | 17.09 | 3.00 | 49.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.52 | 8.54 | 15.72 | 10.00 | 54.5 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.25 | 3.55 | 5.97 | 3.00 | 26.5 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 61.24
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.79) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.79) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.12 | 6.72 | 11.68 | 0.00 | 55.9 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.67 | 4.31 | 6.57 | 2.00 | 47.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.39 | 10.97 | 17.92 | 7.00 | 79.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.98 | 8.88 | 14.33 | 1.00 | 78.8 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.78 | 7.86 | 12.64 | 7.00 | 78.1 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.36 | 6.38 | 10.34 | 6.00 | 67.7 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.17 | 6.27 | 10.06 | 0.00 | 67.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.27 | 20.54 | 34.63 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.47 | 12.60 | 20.11 | 2.00 | 76.3 | 89.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.13 | 8.37 | 16.66 | 0.00 | 36.5 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.34 | 16.37 | 26.64 | 0.00 | 77.1 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.60 | 13.69 | 22.77 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.19 | 12.45 | 20.81 | 20.00 | 62.8 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.68 | 12.09 | 19.98 | 11.00 | 75.0 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.82 | 5.17 | 8.45 | 6.00 | 41.5 | 26.0 |