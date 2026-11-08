# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 235.00
- Total actual points: 164.00
- Average predicted points: 58.75
- Average actual points: 41.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW15 are included before the first simulated week.
- League-average scores were not available for this run.

## GW16

- Train rows: 114791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 60.27
- Actual score: 26.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Josh Brownhill replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.65 | 10.25 | 17.35 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.18 | 0.34 | 0.00 | 6.2 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.81 | 14.60 | 24.14 | 4.00 | 90.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.98 | 14.50 | 23.77 | -1.00 | 90.0 | 85.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.53 | 10.84 | 17.79 | 5.00 | 75.8 | 90.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 2.47 | 7.62 | 11.92 | 1.00 | 73.7 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.54 | 7.10 | 11.65 | 5.00 | 74.6 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.07 | 23.87 | 38.74 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.79 | 15.19 | 25.31 | 2.00 | 89.6 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.36 | 13.03 | 21.16 | 5.00 | 64.9 | 90.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 5.67 | 17.33 | 28.05 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.73 | 13.37 | 22.54 | 1.00 | 88.4 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.95 | 11.89 | 19.09 | 2.00 | 79.2 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.68 | 11.24 | 18.93 | 1.00 | 81.3 | 90.0 |
| Bench 2 | Autosub In | Josh Brownhill | MID | 6 | 4.7 | 2.59 | 8.02 | 12.64 | 2.00 | 75.5 | 90.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.33
- Actual score: 73.00
- Transfer: Kieran Trippier -> William Saliba (projected gain 1.16, hit 0)
- Autosub: Josh Brownhill replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.89 | 9.69 | 15.95 | 10.00 | 87.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.27 | 0.36 | 0.51 | 0.00 | 5.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.66 | 14.90 | 24.50 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.82 | 13.60 | 21.74 | 8.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.82 | 10.83 | 17.09 | 7.00 | 81.7 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 1.89 | 5.91 | 9.71 | 0.00 | 61.2 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.77 | 5.33 | 8.83 | 0.00 | 58.7 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.95 | 17.78 | 28.93 | 9.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.27 | 15.01 | 23.66 | 2.00 | 86.9 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.27 | 13.37 | 24.82 | 0.00 | 29.4 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.26 | 18.30 | 29.20 | 3.00 | 90.0 | 88.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.3 | 2.86 | 10.81 | 18.35 | 0.00 | 62.5 | 0.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.74 | 10.61 | 17.12 | 6.00 | 70.2 | 83.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.54 | 10.28 | 17.12 | 14.00 | 68.8 | 90.0 |
| Bench 2 | Autosub In | Josh Brownhill | MID | 6 | 4.7 | 2.71 | 7.73 | 12.58 | 2.00 | 77.8 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 1.40 -> 0.30
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 59.58
- Actual score: 25.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.37) beats the best remaining Triple Captain opportunity (7.69).
- Transfer: Anthony Gordon -> Dejan Kulusevski (projected gain 2.91, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (6.37) beats the best remaining Triple Captain opportunity (7.69).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.70 | 11.12 | 18.37 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.21 | 0.56 | 0.67 | 0.00 | 5.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.39 | 14.39 | 23.99 | 5.00 | 84.1 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.61 | 13.13 | 20.24 | 2.00 | 82.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.30 | 10.27 | 16.38 | 2.00 | 85.2 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 1.41 | 4.83 | 8.03 | 1.00 | 49.2 | 90.0 |
| Bench 2 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.25 | 4.09 | 7.17 | 6.00 | 45.6 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 7.06 | 19.26 | 30.03 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 13.72 | 25.53 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Julián Álvarez | FWD | 13 | 6.9 | 0.00 | 12.05 | 20.03 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.80 | 17.99 | 28.57 | 1.00 | 90.0 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 7.2 | 4.67 | 13.29 | 21.30 | 1.00 | 87.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.78 | 13.25 | 20.91 | 1.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 2.99 | 10.47 | 17.94 | 1.00 | 50.8 | 90.0 |
| XI | XI | Josh Brownhill | MID | 6 | 4.7 | 2.75 | 7.86 | 12.68 | 3.00 | 81.6 | 90.0 |

## GW19

- Train rows: 117083
- Bank: 0.30 -> 7.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Trent Alexander-Arnold
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 60.82
- Actual score: 40.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.25) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Erling Haaland -> Dominic Solanke (projected gain 4.36, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.25) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.49 | 10.37 | 17.11 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.37 | 0.73 | 1.01 | 0.00 | 8.1 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.30 | 16.25 | 26.24 | 8.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.10 | 12.22 | 19.39 | 5.00 | 82.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.98 | 10.73 | 16.99 | 1.00 | 87.5 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.19 | 6.52 | 10.68 | 1.00 | 70.9 | 90.0 |
| Bench 4 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.01 | 6.39 | 10.31 | 0.00 | 66.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.91 | 15.13 | 24.05 | 2.00 | 77.6 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.94 | 13.66 | 21.71 | 6.00 | 78.8 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 3.40 | 10.60 | 17.71 | 8.00 | 53.1 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.23 | 17.44 | 27.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 7.2 | 3.95 | 12.23 | 20.00 | 1.00 | 78.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.2 | 3.85 | 11.76 | 19.50 | 1.00 | 72.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.19 | 9.94 | 16.01 | 0.00 | 58.4 | 0.0 |
| Bench 2 | Bench Boost | Josh Brownhill | MID | 6 | 4.7 | 2.68 | 7.93 | 12.85 | 2.00 | 82.4 | 90.0 |