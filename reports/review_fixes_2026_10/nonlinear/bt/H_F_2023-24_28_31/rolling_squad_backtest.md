# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW27
- Simulated weeks: GW28-GW31
- Total predicted points: 238.68
- Total actual points: 212.00
- Average predicted points: 59.67
- Average actual points: 53.00
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
- Bank: 100.00 -> 0.60
- Free transfers: 1 -> 2
- Captain: Alfie Doughty
- Vice captain: Norberto Murara Neto
- Effective captain: Alfie Doughty
- Chip used: triple_captain
- Predicted score: 81.72
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.66) beats the best remaining Triple Captain opportunity (8.92).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Alfie Doughty. Optimizer chose Triple Captain here because the current estimated captain upside (12.66) beats the best remaining Triple Captain opportunity (8.92).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | Norberto Murara Neto | GK | 3 | 4.7 | 7.16 | 13.57 | 18.09 | 4.00 | 172.9 | 180.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 2.04 | 9.94 | 18.28 | 2.00 | 86.7 | 90.0 |
| Captain | Captain | Alfie Doughty | DEF | 12 | 4.7 | 8.41 | 16.22 | 25.20 | 5.00 | 157.6 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 3.22 | 12.82 | 18.11 | 2.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Lewis Dunk | DEF | 5 | 5.2 | 3.00 | 11.46 | 17.94 | 7.00 | 71.4 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 6.58 | 10.41 | 13.80 | 8.00 | 165.9 | 180.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.6 | 3.61 | 10.39 | 18.11 | 11.00 | 68.9 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 6.88 | 14.56 | 28.29 | 4.00 | 147.7 | 180.0 |
| Bench 4 | Bench | Julián Álvarez | FWD | 13 | 6.5 | 2.39 | 10.16 | 21.21 | 2.00 | 50.3 | 68.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.5 | 6.19 | 9.01 | 15.99 | 15.00 | 136.7 | 180.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 4.61 | 18.27 | 27.91 | 1.00 | 57.3 | 29.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.2 | 6.76 | 17.83 | 25.08 | 2.00 | 63.6 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.8 | 4.50 | 15.30 | 25.62 | 17.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Kevin De Bruyne | MID | 13 | 10.6 | 3.12 | 13.21 | 29.31 | 6.00 | 70.3 | 68.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 6.98 | 11.74 | 21.38 | 9.00 | 160.5 | 177.0 |

## GW29

- Train rows: 125157
- Bank: 0.60 -> 1.50
- Free transfers: 2 -> 2
- Captain: Son Heung-min
- Vice captain: Mark Flekken
- Effective captain: Son Heung-min
- Chip used: none
- Predicted score: 29.93
- Actual score: 13.00
- Transfer: Julián Álvarez -> Yoane Wissa (projected gain 4.22, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Vice Captain | XI | Mark Flekken | GK | 4 | 4.5 | 4.36 | 12.63 | 17.44 | 2.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.7 | 0.31 | 7.12 | 16.11 | 0.00 | 2.8 | 0.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.7 | 3.12 | 10.78 | 15.25 | 1.00 | 84.2 | 45.0 |
| XI | Bench | Benjamin White | DEF | 1 | 5.6 | 0.00 | 8.78 | 14.99 | 0.00 | 0.4 | 0.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 0.00 | 8.16 | 17.06 | 0.00 | 1.4 | 0.0 |
| Bench 2 | Bench | Lewis Dunk | DEF | 5 | 5.2 | 0.00 | 7.93 | 12.66 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Illia Zabarnyi | DEF | 3 | 4.5 | 0.00 | 7.61 | 12.53 | 0.00 | 1.5 | 0.0 |
| XI | XI | Yoane Wissa | FWD | 4 | 5.6 | 3.96 | 11.77 | 16.43 | 2.00 | 76.7 | 78.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.2 | 3.78 | 10.99 | 17.98 | 2.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | FWD | 3 | 4.5 | 0.00 | 8.96 | 16.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 9.2 | 0.27 | 16.70 | 30.66 | 0.00 | 1.7 | 0.0 |
| Captain | Captain | Son Heung-min | MID | 18 | 9.9 | 5.05 | 15.52 | 23.17 | 2.00 | 77.4 | 86.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 10.6 | 0.00 | 13.30 | 25.62 | 0.00 | 2.2 | 0.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.0 | 1.15 | 12.01 | 18.82 | 0.00 | 16.2 | 0.0 |
| XI | XI | Ross Barkley | MID | 12 | 5.0 | 3.20 | 9.18 | 15.08 | 2.00 | 79.7 | 90.0 |

## GW30

- Train rows: 125995
- Bank: 1.50 -> 0.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 53.85
- Actual score: 49.00
- Transfer: Ross Barkley -> Alexis Mac Allister (projected gain 7.82, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 2.75 | 7.84 | 15.21 | 2.00 | 75.7 | 90.0 |
| Bench 1 | Bench | Mark Flekken | GK | 4 | 4.5 | 1.68 | 7.35 | 13.24 | 3.00 | 55.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 5.30 | 12.00 | 18.88 | 1.00 | 82.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.6 | 3.22 | 9.40 | 15.08 | 6.00 | 78.6 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 2.31 | 7.31 | 15.59 | 2.00 | 69.2 | 90.0 |
| Bench 3 | Bench | Lewis Dunk | DEF | 5 | 5.2 | 1.94 | 6.64 | 13.34 | 1.00 | 71.8 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.7 | 1.45 | 3.87 | 9.91 | 2.00 | 42.5 | 82.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.5 | 4.18 | 9.86 | 17.40 | 2.00 | 75.3 | 90.0 |
| XI | XI | Carlton Morris | FWD | 12 | 5.1 | 3.15 | 7.60 | 12.72 | 2.00 | 61.0 | 90.0 |
| Bench 2 | Bench | Yoane Wissa | FWD | 4 | 5.6 | 2.33 | 5.42 | 11.45 | 1.00 | 37.3 | 70.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.23 | 17.90 | 25.19 | 7.00 | 85.2 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.1 | 4.40 | 16.48 | 23.67 | 3.00 | 56.2 | 77.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.4 | 3.97 | 14.96 | 26.70 | 3.00 | 66.1 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.59 | 14.63 | 27.60 | 10.00 | 44.3 | 87.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.8 | 4.52 | 12.80 | 20.37 | 4.00 | 80.8 | 90.0 |

## GW31

- Train rows: 126837
- Bank: 0.70 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bukayo Saka
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 73.18
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.21) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Lewis Dunk -> William Saliba (projected gain 6.42, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.21) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.7 | 4.23 | 10.97 | 16.42 | 7.00 | 87.1 | 90.0 |
| Bench 1 | Bench Boost | Mark Flekken | GK | 4 | 4.5 | 3.72 | 8.16 | 13.75 | 11.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.8 | 4.76 | 14.39 | 16.57 | 7.00 | 80.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.5 | 4.39 | 14.05 | 22.73 | 2.00 | 78.7 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.7 | 4.13 | 11.54 | 17.49 | 6.00 | 76.5 | 90.0 |
| XI | XI | Illia Zabarnyi | DEF | 3 | 4.5 | 3.62 | 8.80 | 14.26 | 7.00 | 83.7 | 90.0 |
| Bench 4 | Bench Boost | Alfie Doughty | DEF | 12 | 4.7 | 1.87 | 8.72 | 13.22 | 1.00 | 67.4 | 90.0 |
| Bench 3 | Bench Boost | Carlton Morris | FWD | 12 | 5.1 | 2.03 | 10.06 | 15.92 | 2.00 | 72.1 | 90.0 |
| XI | XI | Antoine Semenyo | FWD | 3 | 4.5 | 4.76 | 9.63 | 16.16 | 3.00 | 80.2 | 45.0 |
| Bench 2 | Bench Boost | Yoane Wissa | FWD | 4 | 5.6 | 3.59 | 8.07 | 14.91 | 2.00 | 52.0 | 72.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.1 | 7.44 | 21.50 | 27.34 | 1.00 | 76.6 | 59.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 6.38 | 17.44 | 26.11 | 0.00 | 71.9 | 0.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.22 | 16.99 | 24.03 | 2.00 | 73.4 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.4 | 5.43 | 14.66 | 22.54 | 0.00 | 65.1 | 0.0 |
| XI | XI | Alexis Mac Allister | MID | 11 | 5.8 | 4.18 | 11.84 | 16.53 | 10.00 | 75.9 | 90.0 |