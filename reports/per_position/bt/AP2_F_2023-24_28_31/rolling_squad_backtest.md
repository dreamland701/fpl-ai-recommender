# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 218.76
- Total actual points: 174.00
- Average predicted points: 54.69
- Average actual points: 43.50
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Dominic Solanke
- Vice captain: Alfie Doughty
- Effective captain: Dominic Solanke
- Chip used: bench_boost
- Predicted score: 87.44
- Actual score: 55.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.77) beats the best remaining Bench Boost opportunity (8.28).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.66): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.77) beats the best remaining Bench Boost opportunity (8.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 3.43 | 11.97 | 20.52 | 3.00 | 80.0 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.00 | 0.00 | 2.00 | 7.7 | 34.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 5.01 | 13.51 | 20.61 | 2.00 | 84.1 | 90.0 |
| Vice Captain | XI | Alfie Doughty | DEF | 12 | 4.7 | 8.62 | 11.67 | 17.65 | 5.00 | 164.7 | 180.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.90 | 10.10 | 14.89 | 8.00 | 167.8 | 180.0 |
| Bench 4 | Bench Boost | Chris Richards | DEF | 8 | 3.9 | 2.33 | 6.78 | 10.51 | 2.00 | 74.3 | 90.0 |
| Bench 2 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 4.28 | 6.60 | 9.97 | 2.00 | 135.9 | 151.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.4 | 5.12 | 18.96 | 30.00 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 5.70 | 18.07 | 29.15 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Dominic Solanke | FWD | 3 | 7.2 | 9.82 | 14.35 | 22.96 | 8.00 | 180.0 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 6.45 | 19.88 | 31.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.51 | 17.19 | 29.15 | 2.00 | 55.7 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 5.36 | 15.84 | 25.23 | 2.00 | 78.8 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.75 | 15.39 | 24.28 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Kobbie Mainoo | MID | 14 | 4.4 | 2.35 | 7.01 | 11.45 | 3.00 | 66.6 | 78.0 |

## GW29

- Train rows: 125157
- Bank: 0.10 -> 0.20
- Free transfers: 2 -> 2
- Captain: Jarrod Bowen
- Vice captain: Mark Flekken
- Effective captain: Jarrod Bowen
- Chip used: none
- Predicted score: 30.46
- Actual score: 11.00
- Transfer: Jordan Pickford -> Mark Flekken (projected gain 4.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | Mark Flekken | GK | 4 | 4.5 | 5.42 | 13.10 | 20.21 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.49 | 1.69 | 0.00 | 0.0 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 5.40 | 15.40 | 21.78 | 1.00 | 90.0 | 45.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.8 | 0.00 | 11.15 | 18.38 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 9.04 | 13.99 | 0.00 | 0.0 | 0.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 2.30 | 6.31 | 9.48 | 2.00 | 76.4 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 0.00 | 4.85 | 8.47 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.4 | 0.00 | 19.22 | 32.05 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 9.0 | 4.42 | 14.82 | 23.42 | 2.00 | 82.7 | 90.0 |
| XI | Bench | Dominic Solanke | FWD | 3 | 7.2 | 0.00 | 13.21 | 22.09 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Jarrod Bowen | MID | 19 | 7.9 | 6.46 | 18.18 | 27.18 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 0.00 | 17.57 | 28.09 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.00 | 15.72 | 27.42 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Martin Ødegaard | MID | 1 | 8.5 | 0.00 | 13.19 | 22.25 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 0.00 | 5.93 | 10.43 | 0.00 | 0.0 | 0.0 |

## GW30

- Train rows: 125995
- Bank: 0.20 -> 0.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Erling Haaland
- Effective captain: Ollie Watkins
- Chip used: none
- Predicted score: 40.53
- Actual score: 41.00
- Transfer: Mark Flekken -> Alphonse Areola (projected gain 5.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.38 | 10.62 | 17.77 | 2.00 | 90.0 | 45.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.00 | 0.22 | 0.59 | 8.00 | 15.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 2.22 | 8.08 | 13.41 | 7.00 | 52.2 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.19 | 6.29 | 9.94 | 2.00 | 55.5 | 90.0 |
| XI | XI | Teden Mengi | DEF | 12 | 3.9 | 1.52 | 5.23 | 8.30 | 0.00 | 76.2 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 3.9 | 1.30 | 3.78 | 6.29 | 2.00 | 45.7 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 0.00 | 0.45 | 1.39 | 2.00 | 35.6 | 82.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 4.89 | 16.20 | 27.78 | 2.00 | 62.9 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 9.0 | 5.57 | 16.01 | 26.11 | 1.00 | 83.5 | 45.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 2.61 | 8.87 | 16.14 | 7.00 | 43.1 | 84.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 3.52 | 13.44 | 21.85 | 3.00 | 47.9 | 60.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 3.57 | 11.91 | 20.63 | 3.00 | 43.2 | 77.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 2.88 | 10.12 | 17.13 | 3.00 | 48.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 2.62 | 8.37 | 16.42 | 10.00 | 54.0 | 90.0 |
| Bench 2 | Bench | Kobbie Mainoo | MID | 14 | 4.4 | 1.62 | 4.82 | 8.18 | 3.00 | 40.3 | 79.0 |

## GW31

- Train rows: 126837
- Bank: 0.40 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 60.33
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.88) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Alphonse Areola -> Mark Flekken (projected gain 2.63, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (6.88) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Alfie Doughty replaced Chris Richards.
- Autosub: Kobbie Mainoo replaced Bukayo Saka.
- Autosub: Teden Mengi replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Mark Flekken | GK | 4 | 4.6 | 3.37 | 10.06 | 17.93 | 11.00 | 86.3 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.87 | 4.47 | 6.46 | 2.00 | 46.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.21 | 10.54 | 17.53 | 7.00 | 78.9 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.87 | 8.06 | 12.52 | 7.00 | 76.8 | 90.0 |
| XI | Bench | Chris Richards | DEF | 8 | 3.9 | 2.01 | 5.72 | 8.96 | 0.00 | 66.3 | 0.0 |
| Bench 3 | Autosub In | Alfie Doughty | DEF | 12 | 4.7 | 1.51 | 4.63 | 8.09 | 1.00 | 66.2 | 90.0 |
| Bench 4 | Autosub In | Teden Mengi | DEF | 12 | 3.9 | 1.16 | 4.14 | 7.38 | 1.00 | 80.5 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.3 | 6.88 | 18.73 | 31.04 | 0.00 | 90.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 4.34 | 11.87 | 19.80 | 2.00 | 75.2 | 89.0 |
| XI | Bench | Ollie Watkins | FWD | 2 | 8.9 | 2.84 | 8.95 | 16.44 | 0.00 | 36.2 | 0.0 |
| Vice Captain | Bench | Bukayo Saka | MID | 1 | 9.0 | 6.36 | 16.79 | 26.98 | 0.00 | 76.8 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 4.31 | 13.11 | 22.32 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.1 | 4.47 | 12.82 | 21.84 | 20.00 | 62.6 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.92 | 12.71 | 21.27 | 11.00 | 74.5 | 90.0 |
| Bench 2 | Autosub In | Kobbie Mainoo | MID | 14 | 4.4 | 1.92 | 5.79 | 9.64 | 2.00 | 57.8 | 90.0 |