# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 226.16
- Total actual points: 173.00
- Average predicted points: 56.54
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
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.64) beats the best remaining Triple Captain opportunity (8.62).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.64) beats the best remaining Triple Captain opportunity (8.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.16 | 10.91 | 17.55 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.52 | 0.99 | 2.00 | 8.1 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.85 | 12.88 | 20.18 | 2.00 | 84.5 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.69 | 12.65 | 19.54 | 5.00 | 169.5 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.50 | 9.85 | 14.53 | 8.00 | 169.6 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.84 | 7.91 | 12.69 | 6.00 | 73.1 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.57 | 7.03 | 11.31 | 2.00 | 75.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.03 | 22.15 | 34.00 | 2.00 | 88.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.46 | 18.87 | 30.33 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 12.09 | 17.38 | 25.59 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.02 | 18.82 | 29.99 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.16 | 17.58 | 29.66 | 2.00 | 55.4 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.34 | 15.19 | 24.42 | 2.00 | 79.4 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.24 | 14.39 | 23.02 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.71 | 8.42 | 12.61 | 2.00 | 107.9 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.26
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.76 | 8.64 | 14.42 | 3.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.26 | 2.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.57 | 16.01 | 23.95 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.30 | 18.88 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 8.87 | 14.56 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.70 | 11.57 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.72 | 10.03 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.37 | 34.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.76 | 16.35 | 26.63 | 2.00 | 83.1 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.11 | 21.86 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.08 | 17.75 | 27.01 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.06 | 29.21 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.93 | 26.06 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 13.03 | 22.01 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.70 | 8.27 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.07
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.46, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.29 | 10.12 | 16.43 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.20 | 1.08 | 1.71 | 8.00 | 15.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.15 | 8.66 | 14.30 | 1.00 | 77.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.44 | 8.16 | 13.82 | 7.00 | 52.3 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.10 | 6.15 | 10.26 | 2.00 | 56.1 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.17 | 4.67 | 8.03 | 0.00 | 44.4 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.44 | 4.40 | 7.52 | 2.00 | 46.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.35 | 18.45 | 30.62 | 2.00 | 60.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.18 | 15.73 | 26.48 | 1.00 | 82.9 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.09 | 9.34 | 16.25 | 7.00 | 42.8 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.71 | 13.03 | 22.58 | 3.00 | 43.0 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.23 | 12.96 | 21.39 | 3.00 | 49.3 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.78 | 10.14 | 17.23 | 3.00 | 49.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.39 | 8.13 | 15.31 | 10.00 | 53.1 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.37 | 3.80 | 6.37 | 3.00 | 26.4 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.65
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.71) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.71) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 1.97 | 6.13 | 10.92 | 0.00 | 54.7 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.58 | 4.02 | 6.06 | 2.00 | 46.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.28 | 11.14 | 18.10 | 7.00 | 78.8 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.06 | 8.89 | 14.35 | 1.00 | 79.4 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.84 | 7.88 | 12.66 | 7.00 | 77.6 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.29 | 6.37 | 10.28 | 6.00 | 67.5 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.16 | 6.12 | 9.90 | 0.00 | 67.1 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.07 | 20.14 | 33.79 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.60 | 12.89 | 20.41 | 2.00 | 76.2 | 89.0 |
| Bench 4 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 1.97 | 8.34 | 16.60 | 0.00 | 36.1 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.28 | 16.41 | 26.69 | 0.00 | 76.4 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.56 | 13.20 | 22.02 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.26 | 12.62 | 21.00 | 20.00 | 64.0 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.66 | 12.34 | 20.41 | 11.00 | 75.2 | 90.0 |
| Bench 3 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 2.00 | 5.53 | 8.96 | 6.00 | 41.5 | 26.0 |