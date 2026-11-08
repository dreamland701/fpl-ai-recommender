# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 295.42
- Total actual points: 293.00
- Average predicted points: 73.85
- Average actual points: 73.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 121022
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Ollie Watkins
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.13
- Actual score: 67.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.53 | 9.20 | 15.23 | 0.00 | 67.4 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.12 | 0.16 | 0.34 | 3.00 | 0.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.58 | 13.05 | 20.88 | 4.00 | 87.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.95 | 11.34 | 18.75 | 2.00 | 79.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.75 | 10.04 | 15.89 | 1.00 | 73.5 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.22 | 8.55 | 13.91 | 1.00 | 81.1 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.14 | 7.47 | 12.30 | 1.00 | 80.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.29 | 19.27 | 29.87 | 13.00 | 83.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.00 | 16.57 | 27.27 | 2.00 | 90.0 | 90.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 4.81 | 12.25 | 20.22 | 5.00 | 88.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.30 | 16.43 | 26.65 | 15.00 | 77.5 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.77 | 16.02 | 25.65 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.93 | 14.37 | 23.42 | 2.00 | 88.1 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.93 | 13.97 | 22.16 | 7.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 5.9 | 4.76 | 13.71 | 21.96 | 10.00 | 84.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 112.49
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (22.14) beats the best remaining Triple Captain opportunity (10.76).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> William Saliba (projected gain 3.89, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (22.14) beats the best remaining Triple Captain opportunity (10.76).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.33 | 9.28 | 15.07 | 3.00 | 82.7 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 2.52 | 4.47 | 6.32 | 5.00 | 59.6 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.69 | 12.82 | 20.83 | 1.00 | 85.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.45 | 12.04 | 19.05 | 6.00 | 88.9 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.77 | 10.26 | 15.57 | 1.00 | 129.1 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.52 | 8.16 | 13.33 | 2.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.00 | 6.56 | 10.99 | -1.00 | 79.6 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 17.54 | 25.46 | 38.69 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.54 | 13.98 | 23.61 | 13.00 | 79.2 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.72 | 10.35 | 16.06 | 0.00 | 132.4 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.24 | 17.61 | 28.72 | 15.00 | 80.7 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.06 | 17.26 | 26.34 | 5.00 | 164.3 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.41 | 16.05 | 23.96 | 4.00 | 153.0 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.65 | 11.35 | 18.89 | 2.00 | 63.5 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.86 | 10.73 | 18.55 | 2.00 | 69.2 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 55.55
- Actual score: 51.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.78 | 10.03 | 16.33 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 7.72 | 12.47 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.91 | 13.14 | 21.20 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.56 | 12.63 | 19.71 | 2.00 | 88.2 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 9.70 | 16.40 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.07 | 8.56 | 13.99 | 6.00 | 80.1 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.10 | 6.00 | 9.85 | 1.00 | 70.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.59 | 24.32 | 36.92 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.04 | 19.73 | 31.38 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.66 | 8.73 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.41 | 21.04 | 32.28 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.50 | 18.14 | 28.64 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 11.01 | 18.19 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.49 | 18.36 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.15 | 17.78 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.25
- Actual score: 93.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.63) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Jarrod Bowen (projected gain 6.82, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.63) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.64 | 9.86 | 15.86 | 13.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.26 | 3.62 | 5.54 | 9.00 | 37.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.53 | 13.05 | 21.48 | 1.00 | 89.4 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.44 | 12.11 | 18.92 | 6.00 | 82.0 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.50 | 7.79 | 13.24 | 1.00 | 76.2 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.20 | 6.38 | 10.84 | 5.00 | 45.5 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.23 | 6.01 | 9.68 | 1.00 | 74.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 8.07 | 23.50 | 36.61 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.50 | 19.05 | 29.42 | 13.00 | 87.4 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.11 | 1.82 | 4.29 | 0.00 | 1.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.25 | 19.90 | 32.49 | 7.00 | 83.4 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.58 | 16.70 | 26.80 | 15.00 | 88.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.56 | 12.88 | 20.65 | 5.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.25 | 9.02 | 15.44 | 5.00 | 49.7 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 2.06 | 6.19 | 11.84 | 0.00 | 28.6 | 0.0 |