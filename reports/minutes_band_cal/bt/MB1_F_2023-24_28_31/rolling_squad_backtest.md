# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 226.70
- Total actual points: 183.00
- Average predicted points: 56.68
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
- Predicted score: 93.77
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.50) beats the best remaining Bench Boost opportunity (9.93).
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.50) beats the best remaining Bench Boost opportunity (9.93).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.78 | 9.87 | 16.27 | 2.00 | 82.7 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.36 | 0.84 | 2.00 | 6.7 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.95 | 13.09 | 20.35 | 2.00 | 82.5 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.42 | 12.41 | 18.99 | 5.00 | 161.5 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.65 | 9.97 | 14.61 | 8.00 | 164.6 | 180.0 |
| Bench 4 | Bench Boost | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.90 | 8.05 | 12.87 | 6.00 | 75.7 | 90.0 |
| Bench 3 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 4.49 | 7.02 | 11.01 | 2.00 | 144.0 | 151.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 6.73 | 21.23 | 32.88 | 2.00 | 82.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.04 | 17.83 | 28.86 | 2.00 | 82.7 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 10.84 | 16.11 | 24.05 | 8.00 | 165.5 | 180.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.41 | 18.31 | 30.94 | 2.00 | 60.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 5.46 | 17.41 | 27.71 | 2.00 | 82.7 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.36 | 15.23 | 24.44 | 2.00 | 80.6 | 90.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | MID | 19 | 7.9 | 4.85 | 13.46 | 21.86 | 2.00 | 82.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 4.6 | 6.05 | 8.87 | 13.19 | 2.00 | 116.2 | 61.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Jarrod Bowen
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 30.58
- Actual score: 23.00
- Transfer: Illia Zabarnyi -> Antonee Robinson (projected gain 0.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.92 | 8.98 | 14.94 | 3.00 | 81.2 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 1.09 | 2.61 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 4.85 | 14.42 | 21.68 | 1.00 | 82.7 | 45.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 9.82 | 16.71 | 0.00 | 0.0 | 0.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.18 | 9.39 | 14.26 | 11.00 | 79.3 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 2.41 | 6.64 | 10.18 | 2.00 | 78.2 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 0.00 | 5.22 | 9.34 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 19.33 | 32.85 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.83 | 16.53 | 26.84 | 2.00 | 81.2 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 12.11 | 20.42 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.57 | 16.66 | 25.64 | 2.00 | 82.7 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 15.68 | 27.34 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 13.97 | 23.23 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 11.56 | 19.80 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Justin Kluivert | MID | 3 | 4.6 | 0.00 | 4.65 | 8.24 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 43.72
- Actual score: 42.00
- Transfer: Alfie Doughty -> Timothy Castagne (projected gain 2.33, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.88 | 9.01 | 15.07 | 2.00 | 82.8 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.09 | 0.96 | 1.66 | 8.00 | 14.1 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.20 | 8.75 | 14.24 | 1.00 | 79.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.65 | 8.49 | 14.37 | 7.00 | 57.3 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 10 | 4.5 | 2.99 | 8.19 | 13.44 | 1.00 | 72.9 | 84.0 |
| Bench 2 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.83 | 5.95 | 9.40 | 0.00 | 78.2 | 90.0 |
| Bench 4 | Bench | Jan Paul van Hecke | DEF | 5 | 4.1 | 1.07 | 4.37 | 7.51 | 0.00 | 42.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 5.50 | 18.29 | 30.68 | 2.00 | 66.9 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.34 | 15.80 | 26.62 | 1.00 | 81.9 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.98 | 9.05 | 15.94 | 7.00 | 42.1 | 84.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.77 | 12.94 | 22.36 | 3.00 | 42.2 | 77.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.28 | 12.47 | 20.65 | 3.00 | 52.9 | 60.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.96 | 10.47 | 17.63 | 3.00 | 53.4 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.67 | 8.87 | 16.33 | 10.00 | 59.0 | 90.0 |
| Bench 3 | Bench | Justin Kluivert | MID | 3 | 4.6 | 1.24 | 3.55 | 6.05 | 3.00 | 24.3 | 72.0 |

## GW31

- Train rows: 126837
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 58.63
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.73) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Stefan Ortega Moreno replaced Alphonse Areola.
- Autosub: Justin Kluivert replaced Timothy Castagne.
- Autosub: Teden Mengi replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 2.28 | 7.03 | 12.28 | 0.00 | 60.1 | 0.0 |
| Bench 1 | Autosub In | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.77 | 4.54 | 6.97 | 2.00 | 51.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.30 | 10.96 | 17.81 | 7.00 | 80.7 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 10 | 4.5 | 3.01 | 8.79 | 14.08 | 1.00 | 79.7 | 90.0 |
| XI | Bench | Timothy Castagne | DEF | 10 | 4.5 | 2.76 | 7.90 | 13.00 | 0.00 | 74.8 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 5 | 4.1 | 2.36 | 6.42 | 10.42 | 6.00 | 70.7 | 90.0 |
| Bench 4 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 1.73 | 5.47 | 9.05 | 1.00 | 78.9 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.3 | 6.73 | 19.04 | 32.62 | 0.00 | 82.7 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.52 | 12.68 | 20.07 | 2.00 | 77.0 | 89.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | 2 | 8.9 | 2.02 | 8.29 | 16.56 | 0.00 | 35.2 | 0.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.28 | 16.31 | 26.54 | 0.00 | 78.6 | 0.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.22 | 12.47 | 20.96 | 20.00 | 66.8 | 79.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.11 | 12.30 | 20.97 | 5.00 | 82.7 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.60 | 12.03 | 19.87 | 11.00 | 76.4 | 90.0 |
| Bench 3 | Autosub In | Justin Kluivert | MID | 3 | 4.6 | 1.79 | 5.16 | 8.49 | 6.00 | 39.3 | 26.0 |