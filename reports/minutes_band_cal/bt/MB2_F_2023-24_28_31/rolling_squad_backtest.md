# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 224.66
- Total actual points: 183.00
- Average predicted points: 56.16
- Average actual points: 45.75
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
- Chip used: bench_boost
- Predicted score: 93.51
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.58) beats the best remaining Bench Boost opportunity (9.99).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.58) beats the best remaining Bench Boost opportunity (9.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.85 | 10.00 | 16.44 | 2.00 | 82.9 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.45 | 0.95 | 2.00 | 7.7 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.80 | 12.89 | 20.06 | 2.00 | 81.4 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.12 | 12.21 | 18.70 | 5.00 | 159.3 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.35 | 9.77 | 14.32 | 8.00 | 162.4 | 180.0 |
| Bench 4 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.91 | 8.06 | 12.88 | 6.00 | 75.8 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 4.50 | 7.02 | 11.01 | 2.00 | 144.2 | 151.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 6.79 | 21.36 | 33.05 | 2.00 | 82.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.10 | 17.97 | 29.03 | 2.00 | 82.9 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 10.97 | 16.24 | 24.22 | 8.00 | 165.8 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.21 | 17.83 | 30.20 | 2.00 | 55.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.52 | 17.54 | 27.88 | 2.00 | 82.9 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.38 | 15.27 | 24.59 | 2.00 | 80.0 | 90.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | MID | 19 | 7.9 | 4.91 | 13.60 | 22.03 | 2.00 | 82.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 6.13 | 9.01 | 13.38 | 2.00 | 119.6 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Jarrod Bowen
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 30.45
- Actual score: 23.00
- Transfer: Illia Zabarnyi -> Antonee Robinson (projected gain 0.43, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.92 | 9.00 | 15.04 | 3.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.18 | 2.72 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 4.91 | 14.57 | 21.86 | 1.00 | 82.9 | 45.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 9.97 | 16.89 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.04 | 9.20 | 14.01 | 11.00 | 78.1 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 2.42 | 6.65 | 10.28 | 2.00 | 77.5 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 5.37 | 9.51 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 19.48 | 33.03 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.76 | 16.48 | 26.87 | 2.00 | 82.7 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 12.26 | 20.59 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 17.01 | 29.19 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.63 | 16.81 | 25.81 | 2.00 | 82.9 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 14.12 | 23.41 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 11.71 | 19.97 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.67 | 8.25 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.78
- Actual score: 41.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.94 | 9.17 | 15.25 | 2.00 | 82.9 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.14 | 1.06 | 1.77 | 8.00 | 15.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.21 | 8.77 | 14.37 | 1.00 | 78.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.69 | 8.64 | 14.57 | 7.00 | 59.0 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 1.84 | 5.98 | 9.53 | 0.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.11 | 4.47 | 7.63 | 0.00 | 43.7 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.81 | 4.15 | 8.80 | 2.00 | 35.6 | 82.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.51 | 18.30 | 30.69 | 2.00 | 67.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.20 | 15.60 | 26.30 | 1.00 | 80.8 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.03 | 9.14 | 16.05 | 7.00 | 43.0 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.82 | 13.03 | 22.48 | 3.00 | 43.2 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.32 | 12.62 | 20.84 | 3.00 | 54.6 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 3.01 | 10.62 | 17.82 | 3.00 | 55.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.72 | 9.02 | 16.53 | 10.00 | 60.7 | 90.0 |
| Bench 2 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.29 | 3.64 | 6.16 | 3.00 | 25.3 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 57.93
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.78) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.78) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Stefan Ortega Moreno replaced Alphonse Areola.
- Autosub: Alfie Doughty replaced Bukayo Saka.
- Autosub: Justin Kluivert replaced Erling Haaland.
- Autosub: Teden Mengi replaced Ollie Watkins.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 2.09 | 6.60 | 11.60 | 0.00 | 55.1 | 0.0 |
| Bench 1 | Autosub In | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.83 | 4.70 | 7.14 | 2.00 | 53.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.29 | 10.98 | 17.93 | 7.00 | 79.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.00 | 8.81 | 14.19 | 1.00 | 78.8 | 90.0 |
| Bench 2 | Autosub In | Alfie Doughty | DEF | 12 | 4.7 | 1.93 | 7.23 | 12.51 | 1.00 | 66.2 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.37 | 6.41 | 10.43 | 6.00 | 70.8 | 90.0 |
| Bench 4 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 1.61 | 5.30 | 8.79 | 1.00 | 77.7 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.3 | 6.78 | 19.20 | 32.76 | 0.00 | 82.9 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.51 | 12.70 | 20.19 | 2.00 | 76.2 | 89.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.9 | 2.07 | 8.39 | 16.66 | 0.00 | 36.2 | 0.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.27 | 16.32 | 26.65 | 0.00 | 77.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.17 | 12.46 | 21.10 | 5.00 | 82.9 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.22 | 12.46 | 20.96 | 20.00 | 66.9 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.59 | 12.05 | 19.98 | 11.00 | 75.5 | 90.0 |
| Bench 3 | Autosub In | Justin Kluivert | MID | 3 | 4.6 | 1.84 | 5.26 | 8.60 | 6.00 | 40.2 | 26.0 |