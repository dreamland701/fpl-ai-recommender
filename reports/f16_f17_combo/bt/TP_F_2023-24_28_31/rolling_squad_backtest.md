# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 233.80
- Total actual points: 181.00
- Average predicted points: 58.45
- Average actual points: 45.25
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
- Predicted score: 94.74
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.39) beats the best remaining Triple Captain opportunity (8.95).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.39) beats the best remaining Triple Captain opportunity (8.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.20 | 10.70 | 17.18 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.01 | 0.53 | 0.83 | 2.00 | 11.3 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.97 | 13.16 | 20.43 | 2.00 | 86.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.73 | 12.53 | 19.49 | 1.00 | 82.8 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.11 | 12.06 | 18.47 | 5.00 | 161.5 | 180.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.63 | 6.81 | 10.70 | 2.00 | 72.9 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 4.31 | 6.69 | 10.36 | 2.00 | 136.6 | 151.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.29 | 22.74 | 35.11 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.69 | 19.60 | 31.40 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 12.19 | 17.91 | 26.59 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.91 | 18.63 | 29.41 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.08 | 18.14 | 31.02 | 2.00 | 53.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.52 | 15.24 | 24.38 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.65 | 13.53 | 21.99 | 11.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Saša Lukić | MID | 10 | 4.3 | 1.47 | 4.00 | 6.16 | 2.00 | 36.9 | 69.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 33.19
- Actual score: 31.00
- Transfer: Gabriel dos Santos Magalhães -> Antonee Robinson (projected gain 0.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.87 | 8.60 | 14.26 | 3.00 | 77.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.21 | 2.53 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.20 | 15.40 | 22.97 | 1.00 | 90.0 | 45.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.04 | 18.45 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.37 | 10.02 | 15.34 | 11.00 | 88.1 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 2.35 | 6.50 | 10.06 | 2.00 | 75.6 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.05 | 8.90 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.87 | 34.98 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.72 | 17.08 | 28.31 | 2.00 | 82.8 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.81 | 23.07 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.25 | 18.50 | 28.29 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 16.98 | 29.24 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.29 | 24.97 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.2 | 0.00 | 12.61 | 21.68 | 0.00 | 0.0 | 0.0 |
| XI | XI | Saša Lukić | MID | 10 | 4.3 | 1.20 | 3.59 | 5.43 | 8.00 | 33.3 | 80.0 |

## GW30

- Train rows: 125995
- Bank: 0.80 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 45.93
- Actual score: 42.00
- Transfer: Alfie Doughty -> Cristian Romero (projected gain 2.91, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.31 | 9.87 | 15.92 | 2.00 | 89.4 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.28 | 1.15 | 1.68 | 8.00 | 18.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.38 | 9.22 | 15.06 | 1.00 | 83.1 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.1 | 3.25 | 8.69 | 14.13 | 2.00 | 76.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.63 | 8.38 | 14.10 | 7.00 | 57.3 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.74 | 5.83 | 9.30 | 0.00 | 74.9 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.43 | 4.10 | 6.65 | 2.00 | 46.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.57 | 18.34 | 30.60 | 2.00 | 67.2 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.47 | 16.22 | 27.32 | 1.00 | 89.3 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.29 | 9.82 | 17.09 | 7.00 | 50.2 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.78 | 13.40 | 23.43 | 3.00 | 43.6 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.16 | 12.18 | 20.07 | 3.00 | 50.2 | 60.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.84 | 10.62 | 18.04 | 2.00 | 64.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.68 | 8.78 | 16.06 | 10.00 | 59.6 | 90.0 |
| Bench 2 | Bench | Saša Lukić | MID | 10 | 4.3 | 2.30 | 5.93 | 8.91 | 2.00 | 55.0 | 62.0 |

## GW31

- Train rows: 126837
- Bank: 0.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 59.94
- Actual score: 53.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.77) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Cristian Romero -> Gabriel dos Santos Magalhães (projected gain 1.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.77) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 1.91 | 5.96 | 10.51 | 0.00 | 49.5 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.51 | 3.87 | 5.95 | 2.00 | 45.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.27 | 11.02 | 18.15 | 7.00 | 79.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.97 | 10.22 | 16.72 | 6.00 | 77.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.07 | 9.11 | 14.88 | 1.00 | 80.9 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.01 | 5.60 | 8.99 | 0.00 | 62.3 | 0.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.45 | 4.98 | 8.51 | 1.00 | 75.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.15 | 20.12 | 34.11 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.56 | 12.99 | 20.89 | 2.00 | 77.6 | 89.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.9 | 2.16 | 8.61 | 17.07 | 0.00 | 39.1 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.26 | 16.32 | 26.74 | 0.00 | 78.1 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.59 | 13.58 | 22.75 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.03 | 12.18 | 20.52 | 8.00 | 80.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.05 | 12.07 | 20.32 | 20.00 | 60.9 | 79.0 |
| Bench 3 | Bench Boost | Saša Lukić | MID | 10 | 4.3 | 1.80 | 5.06 | 7.98 | 1.00 | 45.5 | 32.0 |