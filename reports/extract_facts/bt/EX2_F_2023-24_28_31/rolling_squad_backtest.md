# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 226.39
- Total actual points: 173.00
- Average predicted points: 56.60
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
- Predicted score: 96.22
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.30) beats the best remaining Triple Captain opportunity (8.84).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.30) beats the best remaining Triple Captain opportunity (8.84).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.32 | 11.28 | 18.23 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.65 | 1.12 | 2.00 | 11.5 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.92 | 13.12 | 20.40 | 2.00 | 85.3 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.25 | 12.29 | 18.86 | 5.00 | 165.3 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.54 | 9.90 | 14.55 | 8.00 | 169.3 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.87 | 7.92 | 12.53 | 6.00 | 73.0 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.71 | 7.28 | 11.60 | 2.00 | 75.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.20 | 22.55 | 34.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.55 | 19.20 | 30.72 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.75 | 17.31 | 25.66 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.92 | 18.71 | 29.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.11 | 18.24 | 31.15 | 2.00 | 53.7 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.41 | 15.37 | 24.72 | 2.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.35 | 14.80 | 23.70 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.76 | 8.46 | 12.49 | 2.00 | 109.8 | 61.0 |

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
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.00 | 9.19 | 15.32 | 3.00 | 82.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.37 | 2.80 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.30 | 15.63 | 23.35 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.08 | 18.47 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 8.94 | 14.61 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.48 | 11.11 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.62 | 9.87 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.77 | 34.65 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.48 | 16.85 | 28.37 | 2.00 | 74.9 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.32 | 22.08 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.00 | 17.83 | 27.22 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.00 | 29.15 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.38 | 25.01 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.81 | 21.53 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.32 | 7.69 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 43.64
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.44 | 10.46 | 17.00 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.27 | 1.25 | 1.91 | 8.00 | 18.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.26 | 8.95 | 14.60 | 1.00 | 79.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.55 | 8.23 | 13.85 | 7.00 | 55.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.21 | 6.36 | 10.38 | 2.00 | 57.9 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.24 | 4.66 | 7.76 | 0.00 | 46.8 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.49 | 4.50 | 7.43 | 2.00 | 48.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.54 | 18.32 | 30.50 | 2.00 | 66.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.38 | 15.95 | 26.84 | 1.00 | 86.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.16 | 9.39 | 16.28 | 7.00 | 46.2 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.80 | 13.51 | 23.60 | 3.00 | 43.1 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.22 | 12.28 | 20.23 | 3.00 | 51.2 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.86 | 10.20 | 17.09 | 3.00 | 50.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.68 | 8.86 | 16.17 | 10.00 | 58.4 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.42 | 3.84 | 6.30 | 3.00 | 28.8 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.74
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.85) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.85) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 2.11 | 6.69 | 11.81 | 0.00 | 55.2 | 0.0 |
| XI | XI | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.75 | 6.00 | 8.73 | 2.00 | 60.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.22 | 10.95 | 18.02 | 7.00 | 77.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.91 | 8.73 | 14.25 | 1.00 | 76.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.74 | 7.89 | 12.78 | 7.00 | 75.4 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.23 | 6.15 | 10.05 | 6.00 | 65.7 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.11 | 6.10 | 9.95 | 0.00 | 65.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.12 | 20.27 | 34.41 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.43 | 12.62 | 20.19 | 2.00 | 73.5 | 89.0 |
| Bench 4 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 1.82 | 8.27 | 17.27 | 0.00 | 32.4 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.22 | 16.31 | 26.76 | 0.00 | 76.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.55 | 13.61 | 22.84 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.11 | 12.26 | 20.69 | 20.00 | 62.7 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.49 | 11.98 | 20.04 | 11.00 | 73.1 | 90.0 |
| Bench 3 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.82 | 5.25 | 8.67 | 6.00 | 40.0 | 26.0 |