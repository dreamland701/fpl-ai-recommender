# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 223.80
- Total actual points: 173.00
- Average predicted points: 55.95
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
- Predicted score: 95.46
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.20) beats the best remaining Triple Captain opportunity (8.69).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.20) beats the best remaining Triple Captain opportunity (8.69).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.24 | 11.10 | 18.00 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.47 | 0.96 | 2.00 | 7.7 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.87 | 13.02 | 20.32 | 2.00 | 84.0 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.22 | 12.24 | 18.74 | 5.00 | 164.7 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.50 | 9.89 | 14.55 | 8.00 | 167.7 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.81 | 7.79 | 12.39 | 6.00 | 71.5 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.65 | 7.20 | 11.56 | 2.00 | 74.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.08 | 21.96 | 33.62 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.51 | 19.16 | 30.81 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.65 | 17.14 | 25.35 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.79 | 17.97 | 28.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.20 | 17.91 | 30.28 | 2.00 | 55.8 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.49 | 15.97 | 26.06 | 2.00 | 80.1 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.30 | 14.69 | 23.60 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.61 | 8.29 | 12.24 | 2.00 | 106.1 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 25.98
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.88 | 8.94 | 15.00 | 3.00 | 79.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.21 | 2.75 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.26 | 15.46 | 22.97 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.10 | 18.47 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.03 | 14.68 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.54 | 11.16 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.74 | 10.05 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.08 | 33.60 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.77 | 16.55 | 27.02 | 2.00 | 82.8 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 12.91 | 21.24 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.03 | 17.89 | 27.32 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.01 | 29.15 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 14.65 | 23.85 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 13.58 | 23.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.37 | 7.70 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.10
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.37 | 10.33 | 16.88 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.15 | 1.08 | 1.80 | 8.00 | 15.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.15 | 8.70 | 14.29 | 1.00 | 76.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.44 | 8.04 | 13.67 | 7.00 | 52.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.11 | 6.18 | 10.22 | 2.00 | 55.5 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.11 | 4.43 | 7.52 | 0.00 | 43.5 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.38 | 4.33 | 7.31 | 2.00 | 45.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.30 | 17.57 | 29.31 | 2.00 | 61.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.29 | 15.89 | 26.95 | 1.00 | 83.7 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.94 | 8.81 | 15.38 | 7.00 | 41.7 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.84 | 13.24 | 22.83 | 3.00 | 43.2 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.95 | 11.40 | 18.79 | 3.00 | 46.9 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.96 | 10.92 | 18.64 | 3.00 | 50.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.45 | 8.35 | 15.52 | 10.00 | 53.6 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.29 | 3.60 | 6.05 | 3.00 | 25.3 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.26
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.68) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.68) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.08 | 6.59 | 11.58 | 0.00 | 55.0 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.58 | 4.14 | 6.35 | 2.00 | 46.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.26 | 10.93 | 17.88 | 7.00 | 78.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.97 | 8.75 | 14.10 | 1.00 | 77.6 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.81 | 7.96 | 12.77 | 7.00 | 76.8 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.27 | 6.20 | 10.01 | 6.00 | 66.5 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.15 | 6.17 | 9.97 | 0.00 | 66.4 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.08 | 19.87 | 33.46 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.42 | 12.44 | 19.69 | 2.00 | 73.9 | 89.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.10 | 8.58 | 17.07 | 0.00 | 36.4 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.24 | 16.45 | 26.92 | 0.00 | 76.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.56 | 13.50 | 22.53 | 5.00 | 90.0 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.78 | 12.97 | 21.76 | 11.00 | 76.4 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.02 | 11.67 | 19.50 | 20.00 | 61.7 | 79.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.84 | 5.20 | 8.47 | 6.00 | 40.2 | 26.0 |