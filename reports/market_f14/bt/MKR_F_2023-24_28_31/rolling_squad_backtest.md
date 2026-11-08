# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 224.38
- Total actual points: 166.00
- Average predicted points: 56.10
- Average actual points: 41.50
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
- Vice captain: Norberto Murara Neto
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 97.82
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.63) beats the best remaining Triple Captain opportunity (8.63).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.63) beats the best remaining Triple Captain opportunity (8.63).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | Norberto Murara Neto | GK | 3 | 4.7 | 7.76 | 13.37 | 19.63 | 4.00 | 157.7 | 180.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.19 | 0.47 | 2.00 | 1.5 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.60 | 12.88 | 20.15 | 2.00 | 82.9 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 7.36 | 12.73 | 18.36 | 8.00 | 150.8 | 180.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 7.42 | 11.95 | 18.45 | 5.00 | 168.4 | 180.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.63 | 7.21 | 11.54 | 2.00 | 72.0 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 3.69 | 6.99 | 10.85 | 2.00 | 132.2 | 151.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.03 | 22.07 | 34.10 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.10 | 18.38 | 29.72 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.73 | 17.32 | 24.51 | 8.00 | 163.2 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.91 | 18.57 | 29.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.13 | 16.91 | 28.63 | 2.00 | 67.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.40 | 14.66 | 23.52 | 2.00 | 90.0 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.92 | 14.33 | 23.06 | 2.00 | 74.7 | 90.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.45 | 7.12 | 11.44 | 3.00 | 65.2 | 78.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Jarrod Bowen
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 29.96
- Actual score: 11.00
- Transfer: Norberto Murara Neto -> Mark Flekken (projected gain 5.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 3.98 | 11.35 | 17.29 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.36 | 2.87 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.44 | 15.81 | 23.84 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 9.15 | 16.27 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 7.63 | 13.25 | 0.00 | 0.0 | 0.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 2.44 | 6.84 | 10.56 | 2.00 | 77.0 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 4.28 | 8.26 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.09 | 35.36 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 6.09 | 17.23 | 28.34 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.58 | 23.81 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 18.03 | 32.13 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.92 | 17.55 | 27.11 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 14.94 | 25.78 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 11.56 | 20.55 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 0.00 | 4.99 | 9.32 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 38.73
- Actual score: 42.00
- Transfer: Mark Flekken -> Alphonse Areola (projected gain 5.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.22 | 9.96 | 16.54 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.27 | 1.04 | 1.65 | 8.00 | 9.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.06 | 6.83 | 12.07 | 7.00 | 50.9 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 1.80 | 5.85 | 9.67 | 2.00 | 51.4 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 1.53 | 5.25 | 8.62 | 0.00 | 78.6 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.96 | 4.55 | 9.69 | 2.00 | 45.8 | 82.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.08 | 3.75 | 6.44 | 2.00 | 41.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.39 | 17.57 | 29.40 | 2.00 | 58.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.26 | 15.72 | 26.21 | 1.00 | 80.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.70 | 8.77 | 15.37 | 7.00 | 37.1 | 84.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.32 | 12.28 | 20.04 | 3.00 | 41.7 | 60.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.55 | 12.16 | 21.40 | 3.00 | 41.4 | 77.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.43 | 9.00 | 15.54 | 3.00 | 43.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.08 | 7.72 | 14.68 | 10.00 | 47.8 | 90.0 |
| Bench 2 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 1.17 | 4.00 | 6.98 | 3.00 | 35.9 | 79.0 |

## GW31

- Train rows: 126837
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 57.87
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.92) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.24 | 7.24 | 12.77 | 0.00 | 67.2 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.91 | 4.87 | 7.30 | 2.00 | 44.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.22 | 11.21 | 18.37 | 7.00 | 78.3 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.79 | 8.16 | 12.96 | 7.00 | 74.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 2.26 | 7.79 | 13.63 | 1.00 | 80.5 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 1.80 | 5.60 | 9.21 | 0.00 | 64.9 | 0.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.52 | 4.81 | 8.29 | 1.00 | 83.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.09 | 19.68 | 33.21 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.44 | 12.71 | 20.12 | 2.00 | 74.2 | 89.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 2.31 | 8.96 | 17.63 | 0.00 | 43.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.94 | 15.54 | 25.57 | 0.00 | 77.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.06 | 12.74 | 21.61 | 5.00 | 88.5 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.17 | 11.78 | 19.47 | 20.00 | 57.5 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.35 | 11.69 | 19.35 | 11.00 | 70.1 | 90.0 |
| Bench 3 | Bench Boost | Kobbie Mainoo | MID | 14 | 4.4 | 1.70 | 5.58 | 9.40 | 2.00 | 56.7 | 90.0 |