# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW15
- Simulated weeks: GW16-GW19
- Total predicted points: 233.60
- Total actual points: 155.00
- Average predicted points: 58.40
- Average actual points: 38.75
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
- Predicted score: 60.95
- Actual score: 25.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Harry Maguire replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.32 | 9.24 | 15.75 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.00 | 0.55 | 0.98 | 0.00 | 7.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.02 | 14.90 | 24.43 | -1.00 | 90.0 | 85.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.66 | 14.18 | 23.61 | 4.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 3.47 | 10.74 | 17.49 | 5.00 | 74.4 | 90.0 |
| Bench 2 | Autosub In | Harry Maguire | DEF | 14 | 4.3 | 2.97 | 8.09 | 13.62 | 1.00 | 84.8 | 90.0 |
| Bench 3 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.67 | 7.35 | 12.05 | 5.00 | 78.1 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.0 | 8.64 | 25.14 | 40.78 | 0.00 | 90.0 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.46 | 14.15 | 23.55 | 2.00 | 86.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.42 | 12.90 | 20.98 | 5.00 | 64.3 | 90.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 5.77 | 17.62 | 28.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.3 | 4.76 | 13.46 | 22.69 | 1.00 | 89.2 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.12 | 12.58 | 20.08 | 2.00 | 79.3 | 73.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.67 | 11.09 | 18.75 | 1.00 | 81.3 | 90.0 |
| Bench 4 | Bench | James McAtee | MID | 17 | 4.4 | 2.50 | 6.75 | 10.88 | 8.00 | 66.3 | 80.0 |

## GW17

- Train rows: 115549
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.49
- Actual score: 72.00
- Transfer: Kieran Trippier -> William Saliba (projected gain 1.72, hit 0)
- Autosub: James McAtee replaced Bruno Borges Fernandes.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 2.68 | 9.17 | 14.95 | 10.00 | 84.6 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.38 | 0.75 | 1.15 | 0.00 | 7.9 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.58 | 14.59 | 24.10 | 9.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.3 | 4.60 | 13.05 | 20.86 | 8.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.13 | 11.74 | 18.53 | 7.00 | 85.0 | 90.0 |
| Bench 3 | Bench | Harry Maguire | DEF | 14 | 4.3 | 2.21 | 7.97 | 12.85 | 0.00 | 78.0 | 0.0 |
| Bench 4 | Bench | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.09 | 6.15 | 10.12 | 0.00 | 62.4 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.58 | 16.57 | 27.02 | 9.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.01 | 14.54 | 23.04 | 2.00 | 85.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.0 | 4.56 | 14.35 | 26.47 | 0.00 | 33.1 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.41 | 18.70 | 29.77 | 3.00 | 90.0 | 88.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.91 | 11.20 | 18.03 | 6.00 | 70.5 | 83.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 8.3 | 2.91 | 10.95 | 18.36 | 0.00 | 62.0 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.4 | 3.70 | 10.35 | 17.17 | 14.00 | 68.8 | 90.0 |
| Bench 2 | Autosub In | James McAtee | MID | 17 | 4.4 | 2.46 | 7.13 | 11.65 | 1.00 | 69.6 | 90.0 |

## GW18

- Train rows: 116314
- Bank: 1.40 -> 2.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 58.65
- Actual score: 24.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.15) beats the best remaining Triple Captain opportunity (7.85).
- Transfer: Bruno Borges Fernandes -> Dejan Kulusevski (projected gain 2.62, hit 0)
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (6.15) beats the best remaining Triple Captain opportunity (7.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.45 | 10.44 | 17.26 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.48 | 0.99 | 1.28 | 0.00 | 7.7 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.1 | 4.35 | 14.19 | 23.63 | 5.00 | 84.2 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 4.30 | 12.41 | 19.24 | 2.00 | 78.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 3.65 | 11.26 | 17.88 | 2.00 | 88.7 | 90.0 |
| XI | XI | Jarrad Branthwaite | DEF | 9 | 4.1 | 1.38 | 4.93 | 8.19 | 1.00 | 48.7 | 90.0 |
| Bench 2 | Bench | Harry Maguire | DEF | 14 | 4.3 | 1.10 | 4.35 | 7.55 | 0.00 | 34.7 | 0.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.5 | 6.84 | 18.17 | 28.27 | 2.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Erling Haaland | FWD | 13 | 14.0 | 0.00 | 14.85 | 27.39 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Julián Álvarez | FWD | 13 | 6.9 | 0.00 | 11.17 | 18.69 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.9 | 5.94 | 18.40 | 29.11 | 1.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 4.74 | 13.22 | 20.90 | 1.00 | 90.0 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 7.2 | 4.44 | 12.93 | 20.98 | 1.00 | 83.7 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 3.66 | 10.68 | 17.41 | 2.00 | 59.2 | 90.0 |
| XI | XI | James McAtee | MID | 17 | 4.4 | 2.21 | 7.19 | 11.60 | 1.00 | 75.6 | 14.0 |

## GW19

- Train rows: 117083
- Bank: 2.40 -> 2.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Trent Alexander-Arnold
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 59.51
- Actual score: 34.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.69) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Julián Álvarez -> Dominic Solanke (projected gain 4.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.69) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.27 | 9.83 | 16.12 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.40 | 0.86 | 1.34 | 0.00 | 10.4 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.2 | 5.21 | 15.65 | 25.48 | 8.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.4 | 3.94 | 11.91 | 18.88 | 5.00 | 80.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.5 | 4.26 | 11.51 | 18.27 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Jarrad Branthwaite | DEF | 9 | 4.1 | 2.21 | 6.87 | 10.77 | 0.00 | 68.5 | 90.0 |
| Bench 4 | Bench Boost | Harry Maguire | DEF | 14 | 4.2 | 0.84 | 3.23 | 5.64 | 0.00 | 25.4 | 0.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.6 | 4.64 | 14.22 | 22.57 | 2.00 | 76.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.92 | 13.54 | 21.36 | 6.00 | 80.2 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 13.9 | 3.53 | 11.21 | 21.42 | 0.00 | 25.6 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.9 | 6.22 | 17.55 | 28.20 | 2.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 6.1 | 4.65 | 12.79 | 20.97 | 1.00 | 81.1 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 7.2 | 3.92 | 12.20 | 19.93 | 1.00 | 78.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.5 | 3.03 | 9.79 | 15.90 | 0.00 | 55.1 | 0.0 |
| Bench 2 | Bench Boost | James McAtee | MID | 17 | 4.4 | 2.24 | 5.96 | 9.92 | 5.00 | 53.0 | 90.0 |