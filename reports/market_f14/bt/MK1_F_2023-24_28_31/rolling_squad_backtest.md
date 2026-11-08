# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 223.70
- Total actual points: 166.00
- Average predicted points: 55.93
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
- Vice captain: Alfie Doughty
- Effective captain: Dominic Solanke
- Chip used: triple_captain
- Predicted score: 97.49
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.47) beats the best remaining Triple Captain opportunity (8.50).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.47) beats the best remaining Triple Captain opportunity (8.50).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 7.69 | 13.53 | 19.81 | 4.00 | 157.2 | 180.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.28 | 0.62 | 2.00 | 1.3 | 34.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 7.29 | 12.88 | 18.54 | 8.00 | 150.3 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.67 | 12.85 | 20.10 | 2.00 | 83.0 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 7.80 | 12.02 | 18.47 | 5.00 | 168.2 | 180.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.65 | 7.21 | 11.53 | 2.00 | 72.1 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 4.06 | 7.06 | 10.88 | 2.00 | 132.0 | 151.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 6.92 | 22.13 | 34.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.14 | 18.36 | 29.68 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.57 | 17.47 | 24.71 | 8.00 | 162.7 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.76 | 18.65 | 29.45 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.19 | 16.87 | 28.57 | 2.00 | 67.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.35 | 14.69 | 23.57 | 2.00 | 90.0 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.99 | 14.29 | 23.00 | 2.00 | 74.7 | 90.0 |
| Bench 4 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 2.48 | 7.10 | 11.41 | 3.00 | 65.2 | 78.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Jarrod Bowen
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 29.86
- Actual score: 11.00
- Transfer: Norberto Murara Neto -> Mark Flekken (projected gain 5.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 3.95 | 11.36 | 17.31 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.36 | 2.88 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.45 | 15.80 | 23.83 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 9.14 | 16.25 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 7.63 | 13.25 | 0.00 | 0.0 | 0.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 2.45 | 6.83 | 10.54 | 2.00 | 77.0 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 4.28 | 8.26 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.06 | 35.29 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 6.07 | 17.23 | 28.34 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.57 | 23.79 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 18.01 | 32.08 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.86 | 17.58 | 27.16 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 14.92 | 25.74 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 11.55 | 20.52 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 0.00 | 4.99 | 9.32 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 38.27
- Actual score: 42.00
- Transfer: Mark Flekken -> Alphonse Areola (projected gain 5.50, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.16 | 9.99 | 16.59 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.13 | 1.11 | 1.77 | 8.00 | 9.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 1.99 | 6.88 | 12.14 | 7.00 | 50.8 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 1.83 | 5.83 | 9.64 | 2.00 | 51.4 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 1.54 | 5.25 | 8.62 | 0.00 | 78.6 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 1.00 | 4.55 | 9.67 | 2.00 | 45.9 | 82.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.14 | 3.73 | 6.39 | 2.00 | 41.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.31 | 17.62 | 29.48 | 2.00 | 58.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.28 | 15.71 | 26.19 | 1.00 | 80.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.75 | 8.74 | 15.32 | 7.00 | 37.2 | 84.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.21 | 12.35 | 20.15 | 3.00 | 41.6 | 60.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.50 | 12.19 | 21.45 | 3.00 | 41.4 | 77.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.35 | 9.04 | 15.62 | 3.00 | 43.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.04 | 7.74 | 14.71 | 10.00 | 47.8 | 90.0 |
| Bench 2 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 1.21 | 3.98 | 6.94 | 3.00 | 35.9 | 79.0 |

## GW31

- Train rows: 126837
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 58.08
- Actual score: 58.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.97) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.97) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.29 | 7.22 | 12.73 | 0.00 | 67.2 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.83 | 4.91 | 7.37 | 2.00 | 44.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.25 | 11.19 | 18.33 | 7.00 | 78.4 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.84 | 8.14 | 12.92 | 7.00 | 74.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 2.27 | 7.81 | 13.65 | 1.00 | 80.5 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 1.91 | 5.54 | 9.10 | 0.00 | 65.0 | 0.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.50 | 4.83 | 8.32 | 1.00 | 83.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.05 | 19.70 | 33.25 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.50 | 12.68 | 20.06 | 2.00 | 74.2 | 89.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 2.29 | 8.99 | 17.67 | 0.00 | 43.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.99 | 15.50 | 25.51 | 0.00 | 77.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.11 | 12.72 | 21.56 | 5.00 | 88.5 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.09 | 11.81 | 19.53 | 20.00 | 57.4 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.39 | 11.67 | 19.31 | 11.00 | 70.1 | 90.0 |
| Bench 3 | Bench Boost | Kobbie Mainoo | MID | 14 | 4.4 | 1.74 | 5.56 | 9.36 | 2.00 | 56.8 | 90.0 |