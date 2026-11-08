# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 225.19
- Total actual points: 173.00
- Average predicted points: 56.30
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
- Predicted score: 97.18
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.51) beats the best remaining Triple Captain opportunity (8.89).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.51) beats the best remaining Triple Captain opportunity (8.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.30 | 11.27 | 18.27 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.00 | 0.02 | 2.00 | 1.8 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.83 | 12.94 | 20.20 | 2.00 | 83.0 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.46 | 12.55 | 19.28 | 5.00 | 168.9 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.46 | 9.84 | 14.49 | 8.00 | 166.7 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.76 | 7.68 | 12.22 | 6.00 | 70.4 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.56 | 6.97 | 11.21 | 2.00 | 72.4 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.24 | 22.61 | 34.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.51 | 19.16 | 30.74 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.96 | 17.60 | 26.18 | 8.00 | 180.0 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.71 | 19.03 | 32.05 | 2.00 | 66.8 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.92 | 18.68 | 29.50 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Martin Ødegaard | MID | 1 | 8.5 | 5.20 | 14.93 | 24.13 | 2.00 | 75.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.26 | 14.63 | 23.50 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.61 | 8.35 | 12.39 | 2.00 | 105.4 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Jarrod Bowen
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 27.39
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.88 | 8.98 | 15.07 | 3.00 | 79.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.06 | 2.52 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.67 | 16.46 | 24.61 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.29 | 18.78 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.46 | 15.37 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.56 | 11.20 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.67 | 9.92 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.62 | 34.66 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 6.33 | 17.81 | 28.91 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.80 | 22.84 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 18.45 | 31.40 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.9 | 6.18 | 18.26 | 27.90 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.40 | 25.24 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.74 | 21.42 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.57 | 8.04 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 40.33
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 3.69, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.45 | 10.54 | 17.19 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.60 | 1.04 | 8.00 | 10.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.02 | 8.43 | 13.89 | 1.00 | 73.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.29 | 7.74 | 13.21 | 7.00 | 48.8 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 1.94 | 5.84 | 9.70 | 2.00 | 51.7 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.91 | 4.02 | 6.90 | 0.00 | 39.0 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.16 | 3.85 | 6.57 | 2.00 | 41.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.23 | 17.71 | 29.70 | 2.00 | 58.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.19 | 15.59 | 26.38 | 1.00 | 81.8 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.79 | 8.64 | 15.24 | 7.00 | 37.6 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.64 | 12.67 | 21.89 | 3.00 | 39.0 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.89 | 11.63 | 19.35 | 3.00 | 43.8 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.49 | 9.43 | 16.03 | 3.00 | 42.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.17 | 7.72 | 14.56 | 10.00 | 47.2 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.12 | 3.26 | 5.54 | 3.00 | 21.4 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.28
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.58) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.58) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.58 | 7.73 | 13.33 | 0.00 | 66.0 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.53 | 3.98 | 6.07 | 2.00 | 45.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.26 | 10.96 | 17.94 | 7.00 | 78.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.96 | 8.76 | 14.14 | 1.00 | 77.3 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.76 | 7.85 | 12.60 | 7.00 | 75.7 | 90.0 |
| Bench 2 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.22 | 6.06 | 9.80 | 6.00 | 65.3 | 90.0 |
| Bench 3 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.05 | 5.91 | 9.55 | 0.00 | 64.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.12 | 20.18 | 34.13 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.48 | 12.65 | 20.14 | 2.00 | 74.7 | 89.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 2.32 | 8.95 | 17.52 | 0.00 | 41.8 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.25 | 16.34 | 26.71 | 0.00 | 76.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.43 | 13.23 | 22.14 | 5.00 | 87.3 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.00 | 11.95 | 20.09 | 20.00 | 59.7 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.43 | 11.74 | 19.55 | 11.00 | 71.4 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.78 | 5.08 | 8.32 | 6.00 | 38.6 | 26.0 |