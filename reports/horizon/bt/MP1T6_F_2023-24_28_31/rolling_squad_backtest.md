# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 225.15
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
- Predicted score: 96.16
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.35) beats the best remaining Triple Captain opportunity (8.85).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.35) beats the best remaining Triple Captain opportunity (8.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.26 | 11.18 | 18.15 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.46 | 0.94 | 2.00 | 7.7 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.87 | 13.02 | 20.33 | 2.00 | 84.1 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.27 | 12.34 | 18.97 | 5.00 | 164.7 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.50 | 9.90 | 14.59 | 8.00 | 167.8 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.81 | 7.82 | 12.44 | 6.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.64 | 7.17 | 11.51 | 2.00 | 74.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.21 | 22.54 | 34.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.51 | 19.15 | 30.74 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.80 | 17.42 | 25.92 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.93 | 18.72 | 29.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.21 | 17.83 | 30.20 | 2.00 | 55.7 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.34 | 15.26 | 24.63 | 2.00 | 78.8 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.32 | 14.78 | 23.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.65 | 8.39 | 12.45 | 2.00 | 106.2 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.10
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.89 | 9.00 | 15.11 | 3.00 | 79.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.19 | 2.70 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.34 | 15.75 | 23.53 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.15 | 18.56 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.08 | 14.78 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.55 | 11.19 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.68 | 9.93 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.66 | 34.70 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.76 | 16.48 | 26.87 | 2.00 | 82.7 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.44 | 22.27 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.06 | 17.99 | 27.49 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.01 | 29.19 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.30 | 25.08 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.89 | 21.65 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.42 | 7.81 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.38
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 13.25, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.37 | 10.34 | 16.90 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.15 | 1.06 | 1.76 | 8.00 | 15.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.17 | 8.78 | 14.43 | 1.00 | 77.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.44 | 8.04 | 13.68 | 7.00 | 52.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.12 | 6.21 | 10.27 | 2.00 | 55.5 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.12 | 4.47 | 7.61 | 0.00 | 43.7 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.38 | 4.32 | 7.29 | 2.00 | 45.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.42 | 18.07 | 30.26 | 2.00 | 62.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.27 | 15.74 | 26.61 | 1.00 | 83.5 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.03 | 9.15 | 16.04 | 7.00 | 43.1 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.83 | 13.04 | 22.46 | 3.00 | 43.2 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.08 | 12.02 | 19.95 | 3.00 | 47.9 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.76 | 10.02 | 16.93 | 3.00 | 48.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.47 | 8.42 | 15.63 | 10.00 | 54.0 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.29 | 3.65 | 6.15 | 3.00 | 25.3 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.51
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.64) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.64) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.09 | 6.60 | 11.60 | 0.00 | 55.1 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.58 | 4.11 | 6.28 | 2.00 | 46.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.27 | 10.99 | 17.98 | 7.00 | 78.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.98 | 8.82 | 14.25 | 1.00 | 77.8 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.81 | 7.96 | 12.77 | 7.00 | 76.8 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.28 | 6.20 | 10.01 | 6.00 | 66.6 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.15 | 6.13 | 9.89 | 0.00 | 66.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.20 | 20.35 | 34.38 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.50 | 12.71 | 20.24 | 2.00 | 75.2 | 89.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.07 | 8.39 | 16.66 | 0.00 | 36.2 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.25 | 16.34 | 26.71 | 0.00 | 76.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.59 | 13.61 | 22.72 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.13 | 12.25 | 20.55 | 20.00 | 62.6 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.57 | 12.06 | 20.04 | 11.00 | 74.5 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.85 | 5.26 | 8.59 | 6.00 | 40.2 | 26.0 |