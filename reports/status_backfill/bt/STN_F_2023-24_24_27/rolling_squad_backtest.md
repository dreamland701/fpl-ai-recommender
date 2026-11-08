# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 266.41
- Total actual points: 282.00
- Average predicted points: 66.60
- Average actual points: 70.50
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
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 61.22
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 2.78 | 8.80 | 14.97 | 1.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.29 | 0.38 | 0.59 | 3.00 | 1.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.67 | 13.05 | 20.99 | 4.00 | 89.4 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.9 | 3.85 | 11.25 | 18.74 | 2.00 | 78.6 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.83 | 10.01 | 15.90 | 1.00 | 73.7 | 86.0 |
| Bench 3 | Bench | Max Kilman | DEF | 20 | 4.5 | 3.19 | 8.46 | 13.86 | 1.00 | 78.5 | 90.0 |
| Bench 4 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.10 | 7.40 | 12.27 | 1.00 | 79.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.05 | 18.68 | 28.94 | 13.00 | 80.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.90 | 16.51 | 27.36 | 2.00 | 94.9 | 90.0 |
| Bench 2 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 4.09 | 10.52 | 17.18 | 5.00 | 72.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.16 | 16.37 | 26.76 | 15.00 | 75.8 | 66.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 5.94 | 16.04 | 25.77 | 3.00 | 95.3 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 5.05 | 14.37 | 23.53 | 2.00 | 88.7 | 90.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 5.23 | 14.04 | 22.30 | 7.00 | 84.5 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.9 | 4.72 | 13.65 | 22.06 | 10.00 | 82.0 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Phil Foden
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 76.46
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (16.50) beats the best remaining Bench Boost opportunity (9.38).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Pedro Porro -> William Saliba (projected gain 3.91, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (16.50) beats the best remaining Bench Boost opportunity (9.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Martin Dubravka | GK | 15 | 4.2 | 2.80 | 8.29 | 13.97 | 2.00 | 79.6 | 90.0 |
| XI | XI | Caoimhin Kelleher | GK | 11 | 3.7 | 2.80 | 4.79 | 6.68 | 5.00 | 64.6 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.67 | 12.78 | 20.86 | 1.00 | 86.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.42 | 11.98 | 19.07 | 6.00 | 88.9 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.12 | 10.25 | 15.60 | 1.00 | 93.5 | 154.0 |
| Bench 3 | Bench Boost | Max Kilman | DEF | 20 | 4.5 | 2.51 | 8.10 | 13.30 | 2.00 | 79.8 | 90.0 |
| Bench 4 | Bench Boost | Lorenz Assignon | DEF | 6 | 4.0 | 1.96 | 6.48 | 10.93 | -1.00 | 78.8 | 79.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 9.55 | 23.59 | 35.55 | 10.00 | 129.3 | 180.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 4.20 | 13.82 | 23.55 | 13.00 | 72.8 | 90.0 |
| XI | XI | Elijah Adebayo | FWD | 12 | 4.9 | 4.05 | 10.30 | 16.05 | 0.00 | 93.8 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 6.22 | 17.54 | 28.83 | 15.00 | 78.4 | 68.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 8.0 | 6.84 | 17.25 | 26.45 | 5.00 | 109.9 | 180.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.2 | 6.80 | 16.10 | 24.10 | 4.00 | 106.5 | 43.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.42 | 11.19 | 18.84 | 2.00 | 56.9 | 70.0 |
| Bench 2 | Bench Boost | Cole Palmer | MID | 7 | 5.8 | 2.53 | 10.59 | 18.49 | 2.00 | 61.6 | 70.0 |

## GW26

- Train rows: 122659
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.84
- Actual score: 49.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Lorenz Assignon replaced Alfie Doughty.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Martin Dubravka | GK | 15 | 4.2 | 1.93 | 6.82 | 11.60 | 0.00 | 78.8 | 0.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 1.68 | 5.68 | 9.03 | 0.00 | 62.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.93 | 13.10 | 21.20 | 0.00 | 93.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.61 | 12.60 | 19.75 | 2.00 | 89.8 | 90.0 |
| XI | Bench | Alfie Doughty | DEF | 12 | 4.6 | 3.13 | 9.93 | 16.66 | 0.00 | 73.5 | 0.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 3.12 | 8.49 | 13.96 | 6.00 | 79.8 | 90.0 |
| Bench 3 | Autosub In | Lorenz Assignon | DEF | 6 | 4.0 | 2.07 | 5.91 | 9.78 | 1.00 | 70.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 8.99 | 24.43 | 37.22 | 5.00 | 117.6 | 74.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 7.52 | 19.79 | 31.59 | 9.00 | 118.4 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.84 | 4.69 | 8.77 | 0.00 | 15.6 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 7.88 | 21.10 | 32.55 | 10.00 | 102.4 | 75.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 6.63 | 18.16 | 28.77 | 11.00 | 109.9 | 90.0 |
| XI | Bench | Diogo Teixeira da Silva | MID | 11 | 8.2 | 3.07 | 10.91 | 18.23 | 0.00 | 37.8 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 5.8 | 3.06 | 10.57 | 18.48 | 0.00 | 52.8 | 0.0 |
| Bench 2 | Bench | Richarlison de Andrade | MID | 18 | 7.2 | 2.97 | 10.24 | 17.90 | 0.00 | 48.2 | 0.0 |

## GW27

- Train rows: 123487
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.89
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.95) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Diogo Teixeira da Silva -> Jarrod Bowen (projected gain 7.10, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.95) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dubravka | GK | 15 | 4.2 | 1.50 | 4.27 | 7.67 | 7.00 | 44.1 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 1.41 | 3.57 | 5.55 | 9.00 | 39.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.44 | 12.98 | 21.44 | 1.00 | 88.1 | 51.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.43 | 12.04 | 18.92 | 6.00 | 82.7 | 90.0 |
| XI | XI | Max Kilman | DEF | 20 | 4.5 | 2.43 | 7.68 | 13.16 | 1.00 | 74.1 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 2.15 | 6.31 | 10.80 | 5.00 | 43.4 | 90.0 |
| Bench 2 | Bench | Lorenz Assignon | DEF | 6 | 4.0 | 2.14 | 5.92 | 9.61 | 1.00 | 72.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.4 | 7.95 | 22.66 | 35.49 | 6.00 | 99.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.49 | 18.93 | 29.42 | 13.00 | 83.5 | 90.0 |
| Bench 4 | Bench | Elijah Adebayo | FWD | 12 | 4.9 | 0.17 | 2.35 | 4.95 | 0.00 | 3.7 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 7.41 | 19.89 | 32.66 | 7.00 | 84.2 | 45.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 5.64 | 16.71 | 26.91 | 15.00 | 89.3 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.8 | 4.53 | 12.86 | 20.70 | 5.00 | 93.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.7 | 3.02 | 8.85 | 15.32 | 5.00 | 45.1 | 90.0 |
| Bench 3 | Bench | Richarlison de Andrade | MID | 18 | 7.1 | 1.54 | 5.88 | 11.53 | 0.00 | 17.3 | 0.0 |