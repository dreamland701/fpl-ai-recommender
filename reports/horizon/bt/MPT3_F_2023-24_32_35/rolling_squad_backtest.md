# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW31
- Simulated weeks: GW32-GW35
- Total predicted points: 295.83
- Total actual points: 289.00
- Average predicted points: 73.96
- Average actual points: 72.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW31 are included before the first simulated week.
- League-average scores were not available for this run.

## GW32

- Train rows: 127681
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Cole Palmer
- Vice captain: Erling Haaland
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.07
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Antoine Semenyo replaced Phil Foden.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 2.87 | 10.63 | 15.76 | 8.00 | 78.1 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.72 | 4.50 | 6.64 | 1.00 | 51.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.04 | 15.62 | 23.10 | 5.00 | 82.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 3.50 | 13.52 | 19.88 | 6.00 | 77.2 | 90.0 |
| XI | XI | Rayan Aït-Nouri | DEF | 20 | 4.7 | 3.24 | 11.43 | 16.16 | 4.00 | 69.0 | 54.0 |
| Bench 3 | Bench | Charlie Taylor | DEF | 6 | 3.9 | 2.43 | 6.33 | 9.99 | 2.00 | 66.5 | 83.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 2.18 | 5.84 | 9.66 | 2.00 | 76.7 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.3 | 5.98 | 18.98 | 33.18 | 8.00 | 67.3 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.49 | 16.29 | 24.63 | 2.00 | 73.3 | 90.0 |
| Bench 2 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 2.58 | 9.23 | 14.07 | 2.00 | 48.9 | 68.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.4 | 5.28 | 20.67 | 29.58 | 8.00 | 61.0 | 90.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.29 | 17.41 | 25.99 | 3.00 | 78.7 | 88.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.0 | 7.14 | 16.99 | 31.74 | 5.00 | 90.0 | 73.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 5.69 | 16.75 | 27.88 | 0.00 | 90.0 | 0.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.9 | 3.43 | 13.72 | 21.00 | 2.00 | 73.0 | 90.0 |

## GW33

- Train rows: 128527
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.10
- Actual score: 62.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 2.91 | 11.31 | 16.63 | 0.00 | 82.9 | 90.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 1.97 | 4.94 | 8.82 | 0.00 | 57.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.57 | 16.81 | 24.57 | 1.00 | 88.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.25 | 15.17 | 21.71 | 0.00 | 82.5 | 90.0 |
| Bench 3 | Bench | Rayan Aït-Nouri | DEF | 20 | 4.7 | 2.22 | 8.64 | 12.23 | 0.00 | 47.4 | 0.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 3.9 | 2.52 | 6.70 | 10.50 | 1.00 | 67.1 | 45.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 1.77 | 5.95 | 10.04 | 0.00 | 79.3 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.3 | 7.57 | 21.84 | 43.67 | 10.00 | 90.0 | 80.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.2 | 3.99 | 15.49 | 23.09 | 7.00 | 71.0 | 90.0 |
| Bench 2 | Bench | Antoine Semenyo | FWD | 3 | 4.5 | 2.58 | 9.91 | 14.69 | 0.00 | 57.5 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 11 | 13.4 | 6.81 | 24.85 | 35.14 | 2.00 | 84.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 6.0 | 5.76 | 20.99 | 33.98 | 26.00 | 83.9 | 79.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 4.70 | 17.73 | 25.89 | 3.00 | 80.7 | 78.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.9 | 3.67 | 13.65 | 19.95 | 2.00 | 75.7 | 90.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.78 | 11.51 | 23.64 | 0.00 | 48.1 | 0.0 |

## GW34

- Train rows: 129378
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Dominic Solanke
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 108.04
- Actual score: 123.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (18.75) beats the best remaining Triple Captain opportunity (13.87).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Rayan Aït-Nouri -> Joachim Andersen (projected gain 7.70, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (18.75) beats the best remaining Triple Captain opportunity (13.87).
- Autosub: Charlie Taylor replaced Cole Palmer.
- Autosub: Antoine Semenyo replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 5.96 | 11.49 | 16.75 | 18.00 | 170.2 | 180.0 |
| Bench 1 | Bench | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.65 | 2.22 | 4.31 | 0.00 | 27.7 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 8.66 | 16.31 | 23.86 | 14.00 | 175.2 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 8.08 | 14.90 | 21.25 | 12.00 | 167.6 | 180.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 6.54 | 11.89 | 17.01 | 11.00 | 172.6 | 180.0 |
| Bench 2 | Autosub In | Charlie Taylor | DEF | 6 | 3.9 | 2.26 | 6.48 | 10.45 | 2.00 | 60.1 | 90.0 |
| Bench 4 | Bench | Teden Mengi | DEF | 12 | 3.9 | 0.81 | 2.52 | 4.62 | 0.00 | 31.2 | 90.0 |
| XI | Bench | Erling Haaland | FWD | 13 | 14.2 | 6.42 | 19.55 | 39.03 | 0.00 | 77.5 | 0.0 |
| Vice Captain | XI | Dominic Solanke | FWD | 3 | 7.2 | 9.66 | 18.26 | 26.65 | 8.00 | 180.0 | 176.0 |
| Bench 3 | Autosub In | Antoine Semenyo | FWD | 3 | 4.5 | 2.08 | 4.84 | 8.18 | 10.00 | 51.9 | 117.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.4 | 13.51 | 25.67 | 36.66 | 3.00 | 176.7 | 106.0 |
| XI | Bench | Cole Palmer | MID | 7 | 6.1 | 4.85 | 21.55 | 36.59 | 0.00 | 86.4 | 0.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.5 | 8.07 | 15.81 | 23.33 | 20.00 | 133.9 | 180.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.9 | 6.37 | 12.29 | 17.95 | 3.00 | 149.7 | 106.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 2.90 | 9.83 | 21.06 | 16.00 | 39.6 | 71.0 |

## GW35

- Train rows: 130234
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Martin Ødegaard
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 72.63
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.80) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alexis Mac Allister -> Dwight McNeil (projected gain 3.37, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.80) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 9 | 4.6 | 3.75 | 10.49 | 16.74 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Stefan Ortega Moreno | GK | 13 | 3.7 | 0.54 | 2.14 | 3.41 | 1.00 | 18.9 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.90 | 13.81 | 21.95 | 1.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.3 | 4.63 | 12.83 | 20.04 | 1.00 | 90.0 | 90.0 |
| XI | XI | Joachim Andersen | DEF | 8 | 4.7 | 4.02 | 10.71 | 16.64 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Charlie Taylor | DEF | 6 | 3.9 | 2.07 | 6.21 | 10.25 | 0.00 | 67.1 | 0.0 |
| Bench 4 | Bench Boost | Teden Mengi | DEF | 12 | 3.9 | 2.02 | 5.66 | 9.34 | 1.00 | 66.9 | 90.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.1 | 5.00 | 20.68 | 33.17 | 5.00 | 39.6 | 28.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.3 | 4.97 | 13.76 | 21.50 | 2.00 | 90.0 | 90.0 |
| Bench 2 | Bench Boost | Antoine Semenyo | FWD | 3 | 4.5 | 3.18 | 8.44 | 13.33 | 2.00 | 70.1 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 6.1 | 8.43 | 24.07 | 36.69 | 8.00 | 114.2 | 180.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 4.91 | 19.28 | 29.63 | 0.00 | 71.7 | 0.0 |
| Vice Captain | XI | Martin Ødegaard | MID | 1 | 8.5 | 6.07 | 17.22 | 27.33 | 2.00 | 90.0 | 88.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.5 | 5.38 | 15.64 | 25.68 | 1.00 | 63.8 | 11.0 |
| XI | XI | Dwight McNeil | MID | 9 | 5.4 | 4.30 | 11.80 | 18.62 | 3.00 | 90.0 | 90.0 |