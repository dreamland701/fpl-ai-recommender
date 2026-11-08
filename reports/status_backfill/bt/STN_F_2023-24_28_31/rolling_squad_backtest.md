# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 236.48
- Total actual points: 177.00
- Average predicted points: 59.12
- Average actual points: 44.25
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
- Vice captain: Erling Haaland
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 81.21
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.44) beats the best remaining Bench Boost opportunity (8.67).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.44) beats the best remaining Bench Boost opportunity (8.67).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.13 | 11.18 | 18.15 | 2.00 | 97.2 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.46 | 0.94 | 2.00 | 7.2 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.85 | 13.02 | 20.33 | 2.00 | 84.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.62 | 12.34 | 18.97 | 5.00 | 114.0 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 4.68 | 9.90 | 14.59 | 8.00 | 113.3 | 180.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.86 | 7.82 | 12.44 | 6.00 | 73.4 | 90.0 |
| Bench 4 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.62 | 7.17 | 11.51 | 2.00 | 73.9 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.4 | 7.31 | 22.54 | 34.76 | 2.00 | 95.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.52 | 19.15 | 30.74 | 2.00 | 98.8 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 7.74 | 17.42 | 25.92 | 8.00 | 125.2 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.11 | 18.72 | 29.59 | 2.00 | 99.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.10 | 17.83 | 30.20 | 2.00 | 52.4 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.39 | 15.26 | 24.63 | 2.00 | 78.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.38 | 14.78 | 23.74 | 2.00 | 95.5 | 90.0 |
| Bench 2 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 4.15 | 8.39 | 12.45 | 2.00 | 80.0 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Erling Haaland
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 57.76
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.76 | 9.00 | 15.11 | 3.00 | 78.7 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.19 | 2.70 | 0.00 | 6.2 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.82 | 15.75 | 23.53 | 1.00 | 117.1 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 3.32 | 11.15 | 18.56 | 0.00 | 69.3 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 2.69 | 9.08 | 14.78 | 0.00 | 84.1 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.79 | 6.55 | 11.19 | 0.00 | 55.4 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.39 | 5.68 | 9.93 | 0.00 | 56.5 | 0.0 |
| Vice Captain | Bench | Erling Haaland | FWD | 13 | 14.4 | 6.55 | 20.66 | 34.70 | 0.00 | 75.2 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.90 | 16.48 | 26.87 | 2.00 | 86.0 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 3.91 | 13.44 | 22.27 | 0.00 | 64.5 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.59 | 17.99 | 27.49 | 2.00 | 119.0 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.07 | 17.01 | 29.19 | 0.00 | 55.4 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.75 | 15.30 | 25.08 | 0.00 | 66.4 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 3.80 | 12.89 | 21.65 | 0.00 | 63.0 | 0.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.10 | 4.42 | 7.81 | 0.00 | 28.9 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 38.86
- Actual score: 43.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.32 | 10.34 | 16.90 | 2.00 | 92.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.16 | 1.06 | 1.76 | 8.00 | 14.9 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.00 | 8.78 | 14.43 | 1.00 | 73.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.31 | 8.04 | 13.68 | 7.00 | 51.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.15 | 6.21 | 10.27 | 2.00 | 55.8 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.09 | 4.47 | 7.61 | 0.00 | 43.4 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.34 | 4.32 | 7.29 | 2.00 | 44.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 4.97 | 18.07 | 30.26 | 2.00 | 59.4 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 4.89 | 15.74 | 26.61 | 1.00 | 77.6 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.74 | 9.15 | 16.04 | 7.00 | 37.5 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.35 | 13.04 | 22.46 | 3.00 | 37.0 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.77 | 12.02 | 19.95 | 3.00 | 44.2 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.68 | 10.02 | 16.93 | 3.00 | 47.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 1.72 | 8.42 | 15.63 | 10.00 | 40.5 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.32 | 3.65 | 6.15 | 3.00 | 25.4 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 58.65
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.91) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.91) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Stefan Ortega Moreno replaced Alphonse Areola.
- Autosub: Justin Kluivert replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 1.98 | 6.60 | 11.60 | 0.00 | 54.1 | 0.0 |
| Bench 1 | Autosub In | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.57 | 4.11 | 6.28 | 2.00 | 46.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.17 | 10.99 | 17.98 | 7.00 | 77.5 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.03 | 8.82 | 14.25 | 1.00 | 78.1 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.83 | 7.96 | 12.77 | 7.00 | 76.5 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.24 | 6.20 | 10.01 | 6.00 | 66.3 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.10 | 6.13 | 9.89 | 0.00 | 65.0 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.3 | 6.91 | 20.35 | 34.38 | 0.00 | 96.3 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.58 | 12.71 | 20.24 | 2.00 | 76.9 | 89.0 |
| Bench 4 | Bench | Ollie Watkins | FWD | 2 | 8.9 | 1.34 | 8.39 | 16.66 | 0.00 | 24.9 | 0.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.19 | 16.34 | 26.71 | 0.00 | 76.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.48 | 13.61 | 22.72 | 5.00 | 88.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.92 | 12.25 | 20.55 | 20.00 | 59.1 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.51 | 12.06 | 20.04 | 11.00 | 73.7 | 90.0 |
| Bench 3 | Autosub In | Justin Kluivert | MID | 3 | 4.6 | 1.81 | 5.26 | 8.59 | 6.00 | 39.1 | 26.0 |