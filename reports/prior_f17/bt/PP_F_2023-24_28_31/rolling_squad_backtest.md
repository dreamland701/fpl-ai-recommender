# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 234.84
- Total actual points: 184.00
- Average predicted points: 58.71
- Average actual points: 46.00
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
- Predicted score: 94.14
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.30) beats the best remaining Triple Captain opportunity (8.93).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Dominic Solanke. Optimizer chose Triple Captain here because the current estimated captain upside (15.30) beats the best remaining Triple Captain opportunity (8.93).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.15 | 10.63 | 17.13 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.31 | 0.60 | 2.00 | 7.2 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.91 | 13.06 | 20.35 | 2.00 | 85.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.65 | 12.39 | 19.39 | 1.00 | 80.9 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.07 | 12.04 | 18.46 | 5.00 | 160.1 | 180.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.57 | 6.71 | 10.63 | 2.00 | 71.4 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 4.22 | 6.64 | 10.32 | 2.00 | 134.2 | 151.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 7.27 | 22.74 | 35.18 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.63 | 19.54 | 31.38 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 12.10 | 17.85 | 26.58 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.92 | 18.65 | 29.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.23 | 17.89 | 30.27 | 2.00 | 56.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.46 | 15.14 | 24.32 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.57 | 13.41 | 21.90 | 11.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Saša Lukić | MID | 10 | 4.3 | 1.67 | 4.29 | 6.53 | 2.00 | 43.6 | 69.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 33.30
- Actual score: 31.00
- Transfer: Gabriel dos Santos Magalhães -> Antonee Robinson (projected gain 0.49, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.79 | 8.50 | 14.17 | 3.00 | 75.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.01 | 2.40 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.20 | 15.40 | 22.97 | 1.00 | 90.0 | 45.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.13 | 18.56 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.29 | 9.90 | 15.23 | 11.00 | 86.4 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 2.31 | 6.45 | 10.02 | 2.00 | 74.5 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 5.16 | 9.03 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.78 | 35.01 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.89 | 16.91 | 27.61 | 2.00 | 86.6 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 14.01 | 23.31 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.20 | 18.43 | 28.24 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.05 | 29.34 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.25 | 25.04 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.2 | 0.00 | 12.51 | 21.70 | 0.00 | 0.0 | 0.0 |
| XI | XI | Saša Lukić | MID | 10 | 4.3 | 1.42 | 3.91 | 5.83 | 8.00 | 40.6 | 80.0 |

## GW30

- Train rows: 125995
- Bank: 0.80 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 44.93
- Actual score: 42.00
- Transfer: Alfie Doughty -> Cristian Romero (projected gain 2.81, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.24 | 9.77 | 15.84 | 2.00 | 87.7 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.15 | 0.93 | 1.48 | 8.00 | 14.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.30 | 9.09 | 14.96 | 1.00 | 81.1 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.1 | 3.17 | 8.56 | 14.04 | 2.00 | 74.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.51 | 8.18 | 13.92 | 7.00 | 54.1 | 90.0 |
| Bench 3 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.71 | 5.80 | 9.30 | 0.00 | 74.2 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.31 | 3.92 | 6.50 | 2.00 | 43.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.46 | 18.15 | 30.41 | 2.00 | 64.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.39 | 16.08 | 27.21 | 1.00 | 87.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.19 | 9.68 | 16.98 | 7.00 | 47.6 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.88 | 13.11 | 22.57 | 3.00 | 45.0 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.06 | 12.01 | 19.92 | 3.00 | 47.3 | 60.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.71 | 10.42 | 17.88 | 2.00 | 61.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.56 | 8.59 | 15.90 | 10.00 | 56.7 | 90.0 |
| Bench 2 | Bench | Saša Lukić | MID | 10 | 4.3 | 2.25 | 5.85 | 8.86 | 2.00 | 53.7 | 62.0 |

## GW31

- Train rows: 126837
- Bank: 0.40 -> 1.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.47
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Ollie Watkins -> Alexander Isak (projected gain 4.71, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 1.95 | 6.00 | 10.47 | 0.00 | 50.5 | 0.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.56 | 3.93 | 5.92 | 2.00 | 45.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.32 | 11.06 | 18.10 | 7.00 | 80.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.13 | 9.18 | 14.87 | 1.00 | 82.4 | 90.0 |
| XI | XI | Cristian Romero | DEF | 18 | 5.1 | 3.10 | 8.64 | 14.10 | 1.00 | 81.8 | 90.0 |
| Bench 2 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.06 | 5.65 | 8.96 | 0.00 | 63.3 | 0.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 1.58 | 5.17 | 8.62 | 1.00 | 78.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.21 | 20.17 | 34.08 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.63 | 13.09 | 20.93 | 2.00 | 79.3 | 89.0 |
| XI | XI | Alexander Isak | FWD | 15 | 7.7 | 4.73 | 12.95 | 20.04 | 8.00 | 78.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.28 | 16.31 | 26.66 | 0.00 | 78.3 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.65 | 13.62 | 22.71 | 5.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 4.07 | 12.21 | 20.48 | 8.00 | 80.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.10 | 12.12 | 20.28 | 20.00 | 61.7 | 79.0 |
| Bench 3 | Bench Boost | Saša Lukić | MID | 10 | 4.3 | 1.87 | 5.15 | 8.00 | 1.00 | 47.1 | 32.0 |