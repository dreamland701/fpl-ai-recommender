# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 283.82
- Total actual points: 293.00
- Average predicted points: 70.95
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
- Predicted score: 60.10
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.74 | 8.80 | 14.97 | 1.00 | 83.9 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.26 | 0.38 | 0.59 | 3.00 | 1.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.58 | 13.05 | 20.99 | 4.00 | 86.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.90 | 11.25 | 18.74 | 2.00 | 77.9 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.71 | 10.01 | 15.90 | 1.00 | 72.4 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.16 | 8.46 | 13.86 | 1.00 | 79.5 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.09 | 7.40 | 12.27 | 1.00 | 79.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 6.80 | 18.68 | 28.94 | 13.00 | 72.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.95 | 16.51 | 27.36 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 3.99 | 10.52 | 17.18 | 5.00 | 71.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.27 | 16.37 | 26.76 | 15.00 | 75.9 | 66.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.76 | 16.04 | 25.77 | 3.00 | 90.0 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.91 | 14.37 | 23.53 | 2.00 | 87.2 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 4.95 | 14.04 | 22.30 | 7.00 | 80.4 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.74 | 13.65 | 22.06 | 10.00 | 83.8 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 106.90
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (20.57) beats the best remaining Triple Captain opportunity (9.80).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> William Saliba (projected gain 4.67, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (20.57) beats the best remaining Triple Captain opportunity (9.80).
- Autosub: Cole Palmer replaced Elijah Adebayo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dubravka | GK | 15 | 4.2 | 2.76 | 8.29 | 13.97 | 2.00 | 78.7 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.92 | 4.79 | 6.68 | 5.00 | 72.5 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.66 | 12.78 | 20.86 | 1.00 | 84.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.41 | 11.98 | 19.07 | 6.00 | 87.7 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 5.72 | 10.25 | 15.60 | 1.00 | 127.0 | 154.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 2.48 | 8.10 | 13.30 | 2.00 | 80.4 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 1.94 | 6.48 | 10.93 | -1.00 | 78.0 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 15.97 | 23.59 | 35.55 | 10.00 | 180.0 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.45 | 13.82 | 23.55 | 13.00 | 76.5 | 90.0 |
| XI | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 5.64 | 10.30 | 16.05 | 0.00 | 129.6 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.18 | 17.54 | 28.83 | 15.00 | 79.0 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 11.01 | 17.25 | 26.45 | 5.00 | 161.7 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 10.40 | 16.10 | 24.10 | 4.00 | 151.3 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.58 | 11.19 | 18.84 | 2.00 | 61.5 | 70.0 |
| Bench 2 | Autosub In | Cole Palmer | MID | 7 | 5.8 | 2.79 | 10.59 | 18.49 | 2.00 | 66.6 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 53.74
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.93 | 6.82 | 11.60 | 0.00 | 78.2 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 5.68 | 9.03 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.88 | 13.10 | 21.20 | 0.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.54 | 12.60 | 19.75 | 2.00 | 87.5 | 90.0 |
| Bench 2 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 9.93 | 16.66 | 0.00 | 0.0 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.02 | 8.49 | 13.96 | 6.00 | 78.8 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.04 | 5.91 | 9.78 | 1.00 | 69.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.66 | 24.43 | 37.22 | 5.00 | 90.0 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.05 | 19.79 | 31.59 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.00 | 4.69 | 8.77 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.45 | 21.10 | 32.55 | 10.00 | 90.0 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.52 | 18.16 | 28.77 | 11.00 | 90.0 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 0.00 | 10.91 | 18.23 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 0.00 | 10.57 | 18.48 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 0.00 | 10.24 | 17.90 | 0.00 | 0.0 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 63.07
- Actual score: 87.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.61) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Jarrod Bowen (projected gain 6.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.61) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.50 | 4.27 | 7.67 | 7.00 | 44.0 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 1.23 | 3.57 | 5.55 | 9.00 | 36.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.49 | 12.98 | 21.44 | 1.00 | 88.0 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.39 | 12.04 | 18.92 | 6.00 | 80.8 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.43 | 7.68 | 13.16 | 1.00 | 74.5 | 90.0 |
| Bench 2 | Bench Boost | Alfie Doughty | DEF | 12 | 4.6 | 2.14 | 6.31 | 10.80 | 5.00 | 43.7 | 90.0 |
| XI | XI | Lorenz Assignon | DEF | 6 | 4.0 | 2.17 | 5.92 | 9.61 | 1.00 | 72.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.76 | 22.66 | 35.49 | 6.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.47 | 18.93 | 29.42 | 13.00 | 86.3 | 90.0 |
| Bench 4 | Bench Boost | Elijah Adebayo | FWD | 12 | 4.9 | 0.35 | 2.35 | 4.95 | 0.00 | 7.9 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.24 | 19.89 | 32.66 | 7.00 | 82.7 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.58 | 16.71 | 26.91 | 15.00 | 88.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.55 | 12.86 | 20.70 | 5.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.13 | 8.85 | 15.32 | 5.00 | 46.5 | 90.0 |
| Bench 3 | Bench Boost | Richarlison de Andrade | MID | 18 | 7.1 | 1.89 | 5.88 | 11.53 | 0.00 | 24.2 | 0.0 |