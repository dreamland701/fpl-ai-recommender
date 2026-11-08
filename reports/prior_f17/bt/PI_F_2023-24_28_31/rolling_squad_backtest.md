# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 224.96
- Total actual points: 172.00
- Average predicted points: 56.24
- Average actual points: 43.00
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
- Predicted score: 96.25
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.45) beats the best remaining Triple Captain opportunity (8.65).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.45) beats the best remaining Triple Captain opportunity (8.65).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.23 | 11.09 | 18.02 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.78 | 1.54 | 2.00 | 8.9 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.82 | 12.91 | 20.18 | 2.00 | 84.0 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.26 | 12.31 | 18.91 | 5.00 | 164.3 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.52 | 9.91 | 14.59 | 8.00 | 167.7 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.81 | 7.82 | 12.46 | 6.00 | 71.9 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.67 | 7.26 | 11.70 | 2.00 | 74.8 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.04 | 22.11 | 34.08 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.55 | 19.21 | 30.82 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.90 | 17.53 | 26.07 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.91 | 18.65 | 29.49 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.22 | 17.85 | 30.23 | 2.00 | 55.8 | 90.0 |
| Bench 2 | Bench | Martin Ødegaard | MID | 1 | 8.5 | 5.36 | 15.31 | 24.71 | 2.00 | 78.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.38 | 14.90 | 23.89 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.65 | 8.36 | 12.37 | 2.00 | 105.8 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.23
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.86 | 8.92 | 15.00 | 3.00 | 79.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.48 | 3.26 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.34 | 15.75 | 23.50 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.02 | 18.38 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.07 | 14.75 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.55 | 11.19 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.76 | 10.10 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.22 | 34.04 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.80 | 16.55 | 26.97 | 2.00 | 82.6 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.53 | 22.40 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.11 | 18.12 | 27.66 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.01 | 29.19 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.23 | 24.99 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.93 | 21.71 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.38 | 7.73 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Erling Haaland
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 42.04
- Actual score: 42.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.34 | 10.25 | 16.76 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.24 | 1.37 | 2.34 | 8.00 | 16.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.17 | 8.76 | 14.37 | 1.00 | 76.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.39 | 7.91 | 13.50 | 7.00 | 52.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.11 | 6.18 | 10.21 | 2.00 | 55.4 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.12 | 4.48 | 7.63 | 0.00 | 43.9 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.40 | 4.42 | 7.47 | 2.00 | 46.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.25 | 17.62 | 29.55 | 2.00 | 63.0 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.30 | 15.80 | 26.69 | 1.00 | 83.5 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.04 | 9.16 | 16.04 | 7.00 | 43.0 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.84 | 13.05 | 22.48 | 3.00 | 43.3 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.04 | 11.93 | 19.81 | 3.00 | 47.9 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.78 | 10.07 | 17.01 | 3.00 | 48.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.50 | 8.49 | 15.73 | 10.00 | 53.9 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.29 | 3.62 | 6.07 | 3.00 | 25.1 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.45
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.80) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.80) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.06 | 6.51 | 11.47 | 0.00 | 55.2 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.66 | 4.41 | 6.85 | 2.00 | 47.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.22 | 10.88 | 17.82 | 7.00 | 78.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.99 | 8.83 | 14.22 | 1.00 | 77.6 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.80 | 7.93 | 12.72 | 7.00 | 76.7 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.18 | 6.23 | 10.08 | 0.00 | 66.8 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.28 | 6.21 | 10.02 | 6.00 | 66.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.07 | 19.96 | 33.77 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.53 | 12.78 | 20.33 | 2.00 | 75.1 | 89.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.11 | 8.48 | 16.77 | 0.00 | 36.1 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.28 | 16.42 | 26.82 | 0.00 | 76.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.63 | 13.71 | 22.86 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.12 | 12.23 | 20.51 | 20.00 | 62.7 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.60 | 12.13 | 20.14 | 11.00 | 74.6 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.84 | 5.23 | 8.51 | 6.00 | 40.0 | 26.0 |