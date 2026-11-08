# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 224.86
- Total actual points: 173.00
- Average predicted points: 56.22
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
- Predicted score: 96.19
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.35) beats the best remaining Triple Captain opportunity (8.94).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.35) beats the best remaining Triple Captain opportunity (8.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.21 | 10.98 | 17.76 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.60 | 1.18 | 2.00 | 5.2 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.82 | 12.82 | 19.98 | 2.00 | 84.9 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.39 | 12.54 | 19.34 | 5.00 | 165.2 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.52 | 9.94 | 14.69 | 8.00 | 169.9 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.80 | 7.77 | 12.36 | 6.00 | 72.5 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.64 | 7.14 | 11.47 | 2.00 | 75.5 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.29 | 22.83 | 35.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.46 | 18.93 | 30.33 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.80 | 17.42 | 25.90 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.96 | 18.82 | 29.78 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.19 | 17.76 | 30.08 | 2.00 | 56.8 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.33 | 15.22 | 24.55 | 2.00 | 78.3 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.32 | 14.79 | 23.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.62 | 8.35 | 12.37 | 2.00 | 106.0 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.07
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.84 | 8.79 | 14.70 | 3.00 | 77.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.33 | 2.94 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.40 | 15.96 | 23.91 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 10.98 | 18.27 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.13 | 14.89 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.49 | 11.09 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.64 | 9.87 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.93 | 35.20 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.72 | 16.33 | 26.58 | 2.00 | 82.6 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.56 | 22.49 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.05 | 18.00 | 27.51 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 16.96 | 29.10 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.46 | 25.37 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.94 | 21.73 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.36 | 7.70 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.25
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.32 | 10.14 | 16.50 | 2.00 | 89.6 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.19 | 1.20 | 1.97 | 8.00 | 12.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.16 | 8.72 | 14.34 | 1.00 | 78.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.40 | 7.87 | 13.37 | 7.00 | 53.4 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.12 | 6.24 | 10.34 | 2.00 | 56.8 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.12 | 4.47 | 7.60 | 0.00 | 44.5 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.37 | 4.31 | 7.29 | 2.00 | 47.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.48 | 18.32 | 30.72 | 2.00 | 64.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.20 | 15.45 | 26.07 | 1.00 | 83.2 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.03 | 9.12 | 15.96 | 7.00 | 43.0 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.77 | 12.83 | 22.08 | 3.00 | 43.9 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.10 | 12.12 | 20.13 | 3.00 | 48.5 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.77 | 10.04 | 16.96 | 3.00 | 48.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.43 | 8.28 | 15.39 | 10.00 | 54.3 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.27 | 3.57 | 5.99 | 3.00 | 25.2 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.35
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.59) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.59) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.05 | 6.45 | 11.29 | 0.00 | 52.3 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.61 | 4.23 | 6.47 | 2.00 | 44.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.23 | 10.84 | 17.72 | 7.00 | 80.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.98 | 8.81 | 14.24 | 1.00 | 78.5 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.81 | 7.97 | 12.81 | 7.00 | 77.9 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.27 | 6.20 | 10.02 | 6.00 | 67.6 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.14 | 6.11 | 9.86 | 0.00 | 67.6 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.23 | 20.46 | 34.59 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.48 | 12.64 | 20.09 | 2.00 | 74.6 | 89.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.01 | 8.16 | 16.21 | 0.00 | 35.7 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.20 | 16.17 | 26.42 | 0.00 | 77.2 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.55 | 13.47 | 22.47 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.14 | 12.30 | 20.63 | 20.00 | 63.3 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.58 | 12.11 | 20.12 | 11.00 | 74.6 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.83 | 5.20 | 8.48 | 6.00 | 40.0 | 26.0 |