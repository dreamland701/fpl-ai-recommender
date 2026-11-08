# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 226.94
- Total actual points: 180.00
- Average predicted points: 56.74
- Average actual points: 45.00
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
- Predicted score: 96.48
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.35) beats the best remaining Bench Boost opportunity (9.35).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.35) beats the best remaining Bench Boost opportunity (9.35).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.48 | 11.87 | 19.27 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.22 | 0.55 | 2.00 | 5.7 | 34.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.74 | 12.81 | 19.64 | 5.00 | 171.1 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.68 | 12.50 | 19.50 | 2.00 | 82.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.41 | 9.61 | 14.05 | 8.00 | 168.5 | 180.0 |
| Bench 4 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.68 | 7.54 | 12.03 | 6.00 | 69.1 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 4.32 | 6.59 | 10.16 | 2.00 | 139.4 | 151.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 6.94 | 21.84 | 33.66 | 2.00 | 88.6 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.74 | 19.77 | 31.76 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 11.68 | 17.30 | 25.71 | 8.00 | 178.6 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.85 | 18.36 | 28.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.01 | 17.22 | 29.22 | 2.00 | 55.1 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.48 | 15.50 | 24.96 | 2.00 | 81.8 | 90.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | MID | 19 | 7.9 | 5.09 | 14.13 | 22.70 | 2.00 | 90.0 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 5.72 | 8.44 | 12.55 | 2.00 | 109.8 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Jarrod Bowen
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 28.62
- Actual score: 12.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.10 | 9.65 | 16.16 | 3.00 | 80.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.19 | 2.71 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.54 | 16.31 | 24.44 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 10.65 | 17.76 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 8.63 | 14.02 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 6.35 | 10.88 | 0.00 | 0.0 | 0.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 2.26 | 6.25 | 9.69 | 2.00 | 75.4 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 20.58 | 34.57 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.96 | 17.12 | 27.92 | 2.00 | 84.2 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.30 | 22.02 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.81 | 17.35 | 26.48 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 16.69 | 28.72 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 15.16 | 24.84 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 13.19 | 22.09 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.44 | 7.86 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 42.51
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 3.09, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.61 | 11.08 | 18.08 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.23 | 1.21 | 1.94 | 8.00 | 15.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.03 | 8.46 | 13.94 | 1.00 | 74.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.38 | 7.80 | 13.25 | 7.00 | 52.5 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.05 | 5.95 | 9.85 | 2.00 | 55.3 | 90.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.69 | 5.44 | 8.60 | 0.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.12 | 4.53 | 7.73 | 0.00 | 42.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.45 | 18.23 | 30.50 | 2.00 | 63.1 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.41 | 16.17 | 27.30 | 1.00 | 84.9 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.01 | 9.09 | 15.91 | 7.00 | 42.0 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.75 | 12.83 | 22.16 | 3.00 | 43.8 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.14 | 12.18 | 20.20 | 3.00 | 49.0 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.84 | 10.25 | 17.33 | 3.00 | 49.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.37 | 7.98 | 14.87 | 10.00 | 54.5 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.34 | 3.75 | 6.32 | 3.00 | 27.2 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 59.33
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.20) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.20) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Stefan Ortega Moreno replaced Alphonse Areola.
- Autosub: Justin Kluivert replaced Bukayo Saka.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 2.24 | 7.11 | 12.43 | 0.00 | 55.5 | 0.0 |
| Bench 1 | Autosub In | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.96 | 5.17 | 7.97 | 2.00 | 50.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.10 | 10.60 | 17.38 | 7.00 | 76.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.87 | 8.59 | 13.90 | 1.00 | 75.6 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.68 | 7.66 | 12.31 | 7.00 | 75.0 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.20 | 6.11 | 9.89 | 6.00 | 64.6 | 90.0 |
| Bench 4 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 1.65 | 4.97 | 8.20 | 1.00 | 83.7 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.3 | 7.20 | 20.42 | 34.49 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.44 | 12.61 | 20.08 | 2.00 | 73.5 | 89.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | 2 | 8.9 | 2.17 | 8.71 | 17.16 | 0.00 | 37.0 | 0.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.11 | 16.05 | 26.30 | 0.00 | 75.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.43 | 13.13 | 21.96 | 5.00 | 89.8 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.61 | 12.27 | 20.39 | 11.00 | 75.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.04 | 12.11 | 20.34 | 20.00 | 61.4 | 79.0 |
| Bench 3 | Autosub In | Justin Kluivert | MID | 3 | 4.6 | 1.98 | 5.46 | 8.87 | 6.00 | 44.2 | 26.0 |