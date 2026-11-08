# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 227.88
- Total actual points: 159.00
- Average predicted points: 56.97
- Average actual points: 39.75
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
- Predicted score: 89.64
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.49) beats the best remaining Bench Boost opportunity (8.57).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.49) beats the best remaining Bench Boost opportunity (8.57).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 6.95 | 13.53 | 19.81 | 4.00 | 156.1 | 180.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.28 | 0.62 | 2.00 | 0.2 | 34.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.91 | 12.88 | 18.54 | 8.00 | 155.5 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.77 | 12.85 | 20.10 | 2.00 | 88.0 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.56 | 12.02 | 18.47 | 5.00 | 120.8 | 180.0 |
| Bench 4 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.71 | 7.21 | 11.53 | 2.00 | 73.3 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 3.78 | 7.06 | 10.88 | 2.00 | 108.6 | 151.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.4 | 7.15 | 22.13 | 34.20 | 2.00 | 93.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 6.01 | 18.36 | 29.68 | 2.00 | 95.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 10.09 | 17.47 | 24.71 | 8.00 | 152.6 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.18 | 18.65 | 29.45 | 2.00 | 98.8 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.01 | 16.87 | 28.57 | 2.00 | 49.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.37 | 14.69 | 23.57 | 2.00 | 92.8 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.31 | 14.29 | 23.00 | 2.00 | 77.0 | 90.0 |
| Bench 3 | Bench Boost | Kobbie Mainoo | MID | 14 | 4.4 | 2.74 | 7.10 | 11.41 | 3.00 | 71.9 | 78.0 |

## GW29

- Train rows: 125157
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Ollie Watkins
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 44.04
- Actual score: 11.00
- Transfer: Norberto Murara Neto -> Mark Flekken (projected gain 3.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.5 | 4.28 | 11.36 | 17.31 | 2.00 | 108.4 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.15 | 1.36 | 2.88 | 0.00 | 8.5 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.51 | 15.80 | 23.83 | 1.00 | 116.7 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 1.35 | 9.14 | 16.25 | 0.00 | 39.5 | 0.0 |
| Bench 2 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 1.03 | 7.63 | 13.25 | 0.00 | 57.1 | 0.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 2.57 | 6.83 | 10.54 | 2.00 | 81.4 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.13 | 4.28 | 8.26 | 0.00 | 34.5 | 0.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.4 | 3.72 | 20.06 | 35.29 | 0.00 | 46.7 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.65 | 17.23 | 28.34 | 2.00 | 89.5 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 1.67 | 13.57 | 23.79 | 0.00 | 40.9 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 3.12 | 18.01 | 32.08 | 0.00 | 41.9 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 5.99 | 17.58 | 27.16 | 2.00 | 113.6 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 2.48 | 14.92 | 25.74 | 0.00 | 41.5 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 1.70 | 11.55 | 20.52 | 0.00 | 35.2 | 0.0 |
| Bench 3 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 0.53 | 4.99 | 9.32 | 0.00 | 34.3 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Erling Haaland
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 35.99
- Actual score: 34.00
- Transfer: Mark Flekken -> Alphonse Areola (projected gain 5.50, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 2.86 | 9.99 | 16.59 | 2.00 | 87.9 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.25 | 1.11 | 1.77 | 8.00 | 10.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 1.51 | 6.88 | 12.14 | 7.00 | 41.6 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.04 | 5.83 | 9.64 | 2.00 | 56.4 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 1.25 | 5.25 | 8.62 | 0.00 | 69.4 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.04 | 4.55 | 9.67 | 2.00 | 27.1 | 82.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.10 | 3.73 | 6.39 | 2.00 | 39.8 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.03 | 17.62 | 29.48 | 2.00 | 53.9 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.48 | 15.71 | 26.19 | 1.00 | 83.1 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.74 | 8.74 | 15.32 | 7.00 | 38.9 | 84.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.42 | 12.35 | 20.15 | 3.00 | 46.3 | 60.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 2.68 | 12.19 | 21.45 | 3.00 | 29.2 | 77.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.07 | 9.04 | 15.62 | 3.00 | 39.9 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | MID | 19 | 7.9 | 1.29 | 7.74 | 14.71 | 10.00 | 34.7 | 90.0 |
| XI | XI | Kobbie Mainoo | MID | 14 | 4.4 | 1.44 | 3.98 | 6.94 | 3.00 | 40.9 | 79.0 |

## GW31

- Train rows: 126837
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 58.20
- Actual score: 58.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.06) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.06) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Alfie Doughty replaced Chris Richards.
- Autosub: Teden Mengi replaced Bukayo Saka.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Alphonse Areola | GK | 19 | 4.3 | 2.03 | 7.22 | 12.73 | 0.00 | 62.9 | 0.0 |
| XI | XI | Stefan Ortega Moreno | GK | 13 | 3.7 | 2.11 | 4.91 | 7.37 | 2.00 | 50.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.30 | 11.19 | 18.33 | 7.00 | 80.9 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 3.13 | 8.14 | 12.92 | 7.00 | 81.3 | 90.0 |
| Bench 2 | Autosub In | Alfie Doughty | DEF | 12 | 4.7 | 1.61 | 7.81 | 13.65 | 1.00 | 64.3 | 90.0 |
| XI | Bench | Chris Richards | DEF | 8 | 3.9 | 1.75 | 5.54 | 9.10 | 0.00 | 60.8 | 0.0 |
| Bench 4 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 1.11 | 4.83 | 8.32 | 1.00 | 70.5 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.3 | 7.06 | 19.70 | 33.25 | 0.00 | 93.7 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.75 | 12.68 | 20.06 | 2.00 | 79.8 | 89.0 |
| Bench 3 | Bench | Ollie Watkins | FWD | 2 | 8.9 | 1.25 | 8.99 | 17.67 | 0.00 | 28.0 | 0.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 5.98 | 15.50 | 25.51 | 0.00 | 73.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.90 | 12.72 | 21.56 | 5.00 | 84.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.56 | 11.81 | 19.53 | 20.00 | 59.4 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.76 | 11.67 | 19.31 | 11.00 | 76.3 | 90.0 |
| XI | XI | Kobbie Mainoo | MID | 14 | 4.4 | 1.78 | 5.56 | 9.36 | 2.00 | 57.9 | 90.0 |