# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 236.78
- Total actual points: 176.00
- Average predicted points: 59.19
- Average actual points: 44.00
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
- Predicted score: 81.59
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.30) beats the best remaining Bench Boost opportunity (8.66).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.30) beats the best remaining Bench Boost opportunity (8.66).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.17 | 11.27 | 18.27 | 2.00 | 98.0 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.00 | 0.02 | 2.00 | 1.8 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.81 | 12.94 | 20.20 | 2.00 | 83.8 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.71 | 12.55 | 19.28 | 5.00 | 115.9 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 4.66 | 9.84 | 14.49 | 8.00 | 112.8 | 180.0 |
| Bench 3 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.81 | 7.68 | 12.22 | 6.00 | 72.2 | 90.0 |
| Bench 4 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.54 | 6.97 | 11.21 | 2.00 | 72.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.4 | 7.34 | 22.61 | 34.87 | 2.00 | 96.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.53 | 19.16 | 30.74 | 2.00 | 99.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 7.80 | 17.60 | 26.18 | 8.00 | 126.7 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.58 | 19.03 | 32.05 | 2.00 | 63.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.11 | 18.68 | 29.50 | 2.00 | 99.3 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.26 | 14.93 | 24.13 | 2.00 | 75.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.33 | 14.63 | 23.50 | 2.00 | 94.2 | 90.0 |
| Bench 2 | Bench Boost | Justin Kluivert | MID | 3 | 4.6 | 4.13 | 8.35 | 12.39 | 2.00 | 79.6 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Erling Haaland
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 59.70
- Actual score: 10.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.75 | 8.98 | 15.07 | 3.00 | 78.5 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.06 | 2.52 | 0.00 | 5.1 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 6.11 | 16.46 | 24.61 | 1.00 | 123.5 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 3.38 | 11.29 | 18.78 | 0.00 | 70.5 | 0.0 |
| XI | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 2.85 | 9.46 | 15.37 | 0.00 | 87.6 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.79 | 6.56 | 11.20 | 0.00 | 55.5 | 0.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.39 | 5.67 | 9.92 | 0.00 | 56.5 | 0.0 |
| Vice Captain | Bench | Erling Haaland | FWD | 13 | 14.4 | 6.53 | 20.62 | 34.66 | 0.00 | 74.8 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.43 | 17.81 | 28.91 | 2.00 | 98.0 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 4.06 | 13.80 | 22.84 | 0.00 | 67.9 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 5.65 | 18.45 | 31.40 | 0.00 | 68.3 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.70 | 18.26 | 27.90 | 2.00 | 121.6 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 4.80 | 15.40 | 25.24 | 0.00 | 67.3 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 3.74 | 12.74 | 21.42 | 0.00 | 61.7 | 0.0 |
| Bench 4 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.16 | 4.57 | 8.04 | 0.00 | 30.3 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Erling Haaland
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 37.13
- Actual score: 42.00
- Transfer: Alfie Doughty -> Antonee Robinson (projected gain 4.90, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.39 | 10.54 | 17.19 | 2.00 | 93.7 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.60 | 1.04 | 8.00 | 10.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 2.87 | 8.43 | 13.89 | 1.00 | 70.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.18 | 7.74 | 13.21 | 7.00 | 48.5 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.01 | 5.84 | 9.70 | 2.00 | 52.5 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.91 | 4.02 | 6.90 | 0.00 | 39.3 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.15 | 3.85 | 6.57 | 2.00 | 40.2 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 4.82 | 17.71 | 29.70 | 2.00 | 56.1 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 4.82 | 15.59 | 26.38 | 1.00 | 76.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.53 | 8.64 | 15.24 | 7.00 | 32.9 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.20 | 12.67 | 21.89 | 3.00 | 33.6 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 2.61 | 11.63 | 19.35 | 3.00 | 40.7 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.45 | 9.43 | 16.03 | 3.00 | 42.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 1.43 | 7.72 | 14.56 | 10.00 | 34.2 | 90.0 |
| Bench 2 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.16 | 3.26 | 5.54 | 3.00 | 21.8 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 58.35
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.85) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.85) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Stefan Ortega Moreno replaced Alphonse Areola.
- Autosub: Justin Kluivert replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 2.44 | 7.73 | 13.33 | 0.00 | 64.4 | 0.0 |
| Bench 1 | Autosub In | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.52 | 3.98 | 6.07 | 2.00 | 45.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.15 | 10.96 | 17.94 | 7.00 | 77.2 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.6 | 3.00 | 8.76 | 14.14 | 1.00 | 77.6 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.78 | 7.85 | 12.60 | 7.00 | 75.5 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.18 | 6.06 | 9.80 | 6.00 | 65.1 | 90.0 |
| Bench 2 | Bench | Chris Richards | DEF | 8 | 3.9 | 2.01 | 5.91 | 9.55 | 0.00 | 62.9 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.3 | 6.85 | 20.18 | 34.13 | 0.00 | 94.9 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.55 | 12.65 | 20.14 | 2.00 | 76.4 | 89.0 |
| Bench 4 | Bench | Ollie Watkins | FWD | 2 | 8.9 | 1.58 | 8.95 | 17.52 | 0.00 | 30.1 | 0.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.19 | 16.34 | 26.71 | 0.00 | 76.7 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.32 | 13.23 | 22.14 | 5.00 | 84.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.80 | 11.95 | 20.09 | 20.00 | 56.4 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.38 | 11.74 | 19.55 | 11.00 | 70.8 | 90.0 |
| Bench 3 | Autosub In | Justin Kluivert | MID | 3 | 4.6 | 1.74 | 5.08 | 8.32 | 6.00 | 37.5 | 26.0 |