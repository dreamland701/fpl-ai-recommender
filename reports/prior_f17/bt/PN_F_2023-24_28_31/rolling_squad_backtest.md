# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 225.50
- Total actual points: 173.00
- Average predicted points: 56.38
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
- Predicted score: 96.29
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.45) beats the best remaining Triple Captain opportunity (8.84).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.45) beats the best remaining Triple Captain opportunity (8.84).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.31 | 11.34 | 18.42 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.60 | 1.16 | 2.00 | 8.7 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.88 | 13.05 | 20.37 | 2.00 | 84.5 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.17 | 12.14 | 18.60 | 5.00 | 163.3 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.45 | 9.74 | 14.26 | 8.00 | 165.0 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.84 | 7.90 | 12.57 | 6.00 | 72.1 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.69 | 7.32 | 11.76 | 2.00 | 75.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.20 | 22.61 | 34.94 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.54 | 19.25 | 30.91 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.90 | 17.54 | 26.08 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.95 | 18.76 | 29.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.18 | 17.74 | 30.05 | 2.00 | 55.4 | 90.0 |
| Bench 2 | Bench | Martin Ødegaard | MID | 1 | 8.5 | 5.32 | 15.21 | 24.55 | 2.00 | 78.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.35 | 14.87 | 23.87 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.55 | 8.17 | 12.02 | 2.00 | 104.8 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 26.18
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.94 | 9.17 | 15.40 | 3.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.35 | 3.07 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.27 | 15.53 | 23.15 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.22 | 18.78 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 8.89 | 14.52 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.64 | 11.44 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.83 | 10.27 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.74 | 34.98 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.78 | 16.57 | 27.02 | 2.00 | 83.4 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.59 | 22.60 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.09 | 18.08 | 27.64 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 16.99 | 29.24 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.36 | 25.27 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.92 | 21.79 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.20 | 7.50 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.49
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.40 | 10.48 | 17.15 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.19 | 1.21 | 2.00 | 8.00 | 16.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.20 | 8.84 | 14.51 | 1.00 | 77.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.46 | 8.11 | 13.80 | 7.00 | 52.7 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.08 | 6.02 | 9.92 | 2.00 | 53.6 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.15 | 4.57 | 7.78 | 0.00 | 44.2 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.43 | 4.47 | 7.53 | 2.00 | 46.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.41 | 18.10 | 30.36 | 2.00 | 62.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.30 | 15.86 | 26.82 | 1.00 | 84.3 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.08 | 9.32 | 16.33 | 7.00 | 44.2 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.82 | 13.01 | 22.42 | 3.00 | 43.2 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.08 | 12.07 | 20.05 | 3.00 | 48.1 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.77 | 10.05 | 16.98 | 3.00 | 48.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.49 | 8.47 | 15.69 | 10.00 | 54.5 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.24 | 3.44 | 5.78 | 3.00 | 24.4 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.55
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.67) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.67) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.11 | 6.68 | 11.75 | 0.00 | 55.6 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.62 | 4.25 | 6.53 | 2.00 | 47.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.28 | 11.03 | 18.06 | 7.00 | 79.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.01 | 8.89 | 14.35 | 1.00 | 78.5 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.76 | 7.74 | 12.38 | 7.00 | 74.8 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.30 | 6.30 | 10.18 | 6.00 | 67.0 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.18 | 6.25 | 10.08 | 0.00 | 67.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.18 | 20.33 | 34.38 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.53 | 12.83 | 20.44 | 2.00 | 76.0 | 89.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.09 | 8.44 | 16.74 | 0.00 | 36.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.22 | 16.26 | 26.56 | 0.00 | 76.4 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.60 | 13.61 | 22.69 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.14 | 12.27 | 20.57 | 20.00 | 62.8 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.57 | 12.05 | 20.02 | 11.00 | 74.6 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.78 | 5.04 | 8.19 | 6.00 | 39.1 | 26.0 |