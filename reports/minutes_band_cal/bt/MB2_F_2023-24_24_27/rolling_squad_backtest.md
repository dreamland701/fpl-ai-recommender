# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 279.30
- Total actual points: 303.00
- Average predicted points: 69.82
- Average actual points: 75.75
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
- Predicted score: 58.58
- Actual score: 72.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.70 | 9.03 | 14.74 | 0.00 | 73.3 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.25 | 0.37 | 0.60 | 3.00 | 1.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.19 | 11.91 | 19.40 | 4.00 | 79.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.94 | 11.27 | 18.74 | 2.00 | 79.0 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.75 | 10.04 | 15.89 | 1.00 | 73.5 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.20 | 8.49 | 13.85 | 1.00 | 80.7 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.14 | 7.42 | 12.26 | 1.00 | 80.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.84 | 18.70 | 28.94 | 13.00 | 73.8 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.57 | 15.36 | 25.77 | 2.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 4.08 | 10.75 | 17.61 | 5.00 | 75.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.31 | 16.40 | 26.76 | 15.00 | 77.0 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.37 | 14.90 | 24.18 | 3.00 | 82.8 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.87 | 13.92 | 22.04 | 7.00 | 77.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.66 | 13.53 | 21.80 | 10.00 | 81.2 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.53 | 13.22 | 21.94 | 2.00 | 80.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 105.07
- Actual score: 82.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (19.79) beats the best remaining Triple Captain opportunity (9.32).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> Gabriel dos Santos Magalhães (projected gain 3.88, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (19.79) beats the best remaining Triple Captain opportunity (9.32).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.19 | 9.06 | 14.74 | 3.00 | 78.2 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 2.91 | 4.78 | 6.69 | 5.00 | 72.5 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.58 | 12.67 | 20.61 | 1.00 | 81.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.25 | 11.85 | 18.57 | 6.00 | 83.2 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.92 | 10.49 | 16.04 | 1.00 | 135.1 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.41 | 7.99 | 13.05 | 2.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.98 | 6.49 | 10.89 | -1.00 | 79.1 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.19 | 22.46 | 33.95 | 10.00 | 165.8 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.48 | 13.83 | 23.52 | 13.00 | 77.5 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.83 | 10.53 | 16.50 | 0.00 | 137.7 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.22 | 17.55 | 28.80 | 15.00 | 80.0 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 10.87 | 17.14 | 26.20 | 5.00 | 156.3 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.47 | 16.12 | 24.07 | 4.00 | 153.3 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.68 | 11.43 | 19.29 | 2.00 | 65.6 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.89 | 10.82 | 18.94 | 2.00 | 70.7 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.70 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 52.67
- Actual score: 51.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.34 | 8.80 | 14.58 | 2.00 | 82.2 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 4.54 | 7.34 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.1 | 4.25 | 12.04 | 18.76 | 2.00 | 79.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.49 | 11.96 | 19.50 | 0.00 | 82.8 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 8.79 | 14.96 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.06 | 8.49 | 13.91 | 6.00 | 79.9 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.13 | 6.16 | 10.24 | 1.00 | 73.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.27 | 23.30 | 35.53 | 5.00 | 82.8 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.66 | 18.66 | 29.89 | 9.00 | 82.8 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 5.31 | 9.70 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.06 | 19.97 | 30.86 | 10.00 | 82.8 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.13 | 17.03 | 27.07 | 11.00 | 82.8 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.91 | 18.18 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.14 | 17.67 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 9.43 | 16.79 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 62.98
- Actual score: 98.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.59) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Martin Ødegaard (projected gain 7.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.59) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.20 | 8.62 | 14.07 | 13.00 | 82.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.22 | 3.57 | 5.56 | 9.00 | 36.5 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.09 | 11.81 | 19.67 | 1.00 | 80.8 | 51.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.2 | 4.20 | 11.33 | 17.61 | 6.00 | 76.6 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.47 | 7.68 | 13.12 | 1.00 | 75.6 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.13 | 6.30 | 10.82 | 5.00 | 43.6 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.21 | 5.93 | 9.57 | 1.00 | 74.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.36 | 21.49 | 33.73 | 6.00 | 82.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.07 | 17.76 | 27.65 | 13.00 | 79.1 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.35 | 2.35 | 4.95 | 0.00 | 7.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.17 | 19.81 | 32.44 | 7.00 | 80.1 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.18 | 15.54 | 25.14 | 15.00 | 80.9 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.72 | 13.47 | 23.02 | 10.00 | 75.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.38 | 9.47 | 16.25 | 5.00 | 53.2 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.88 | 5.87 | 11.54 | 0.00 | 24.2 | 0.0 |