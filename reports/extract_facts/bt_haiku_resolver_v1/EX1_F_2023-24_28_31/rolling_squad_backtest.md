# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 224.75
- Total actual points: 173.00
- Average predicted points: 56.19
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
- Predicted score: 95.65
- Actual score: 53.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.25) beats the best remaining Triple Captain opportunity (8.83).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.25) beats the best remaining Triple Captain opportunity (8.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.26 | 11.18 | 18.13 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.45 | 0.93 | 2.00 | 7.6 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.86 | 13.02 | 20.30 | 2.00 | 84.0 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.18 | 12.22 | 18.79 | 5.00 | 163.2 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.45 | 9.84 | 14.50 | 8.00 | 166.9 | 180.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.81 | 7.82 | 12.44 | 6.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.65 | 7.18 | 11.53 | 2.00 | 74.3 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.19 | 22.53 | 34.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.50 | 19.15 | 30.68 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.70 | 17.31 | 25.72 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.90 | 18.65 | 29.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.23 | 17.95 | 30.23 | 2.00 | 56.4 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.33 | 15.28 | 24.61 | 2.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 5.30 | 14.73 | 23.66 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.64 | 8.40 | 12.43 | 2.00 | 106.1 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 25.87
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.91 | 9.06 | 15.18 | 3.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.18 | 2.70 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.24 | 15.53 | 23.22 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.14 | 18.53 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.09 | 14.79 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.56 | 11.20 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.69 | 9.95 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.73 | 34.68 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.80 | 16.15 | 27.39 | 2.00 | 78.0 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.49 | 22.27 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 5.96 | 17.74 | 27.14 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.05 | 29.15 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.30 | 25.03 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 12.89 | 21.61 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.41 | 7.79 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.63
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.37 | 10.33 | 16.87 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.14 | 1.06 | 1.75 | 8.00 | 15.0 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.20 | 8.84 | 14.51 | 1.00 | 77.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.45 | 8.06 | 13.68 | 7.00 | 52.3 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.13 | 6.24 | 10.30 | 2.00 | 55.6 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.12 | 4.49 | 7.62 | 0.00 | 43.8 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.38 | 4.33 | 7.30 | 2.00 | 45.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.41 | 18.13 | 30.26 | 2.00 | 63.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.31 | 15.86 | 26.72 | 1.00 | 84.4 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.08 | 9.30 | 16.19 | 7.00 | 44.1 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.86 | 13.14 | 22.56 | 3.00 | 44.2 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.08 | 12.06 | 19.98 | 3.00 | 48.4 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.76 | 10.03 | 16.92 | 3.00 | 48.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.59 | 8.72 | 16.02 | 10.00 | 56.2 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.30 | 3.67 | 6.16 | 3.00 | 25.5 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 60.60
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.64) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.64) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.13 | 6.70 | 11.72 | 0.00 | 55.9 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.57 | 4.10 | 6.27 | 2.00 | 46.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.27 | 10.98 | 17.95 | 7.00 | 78.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.98 | 8.80 | 14.21 | 1.00 | 77.8 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.81 | 7.97 | 12.78 | 7.00 | 76.8 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.28 | 6.20 | 10.01 | 6.00 | 66.6 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.15 | 6.13 | 9.89 | 0.00 | 66.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.20 | 20.36 | 34.33 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.49 | 12.70 | 20.19 | 2.00 | 75.2 | 89.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | 2 | 8.9 | 2.08 | 8.30 | 17.49 | 0.00 | 33.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.26 | 16.35 | 26.68 | 0.00 | 77.2 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.61 | 13.67 | 22.78 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.15 | 12.33 | 20.61 | 20.00 | 63.4 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.58 | 12.07 | 20.03 | 11.00 | 74.6 | 90.0 |
| Bench 4 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 1.85 | 5.27 | 8.59 | 6.00 | 40.3 | 26.0 |