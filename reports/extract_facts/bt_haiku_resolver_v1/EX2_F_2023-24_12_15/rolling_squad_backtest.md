# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 255.84
- Total actual points: 234.00
- Average predicted points: 63.96
- Average actual points: 58.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 111791
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Erling Haaland
- Vice captain: Kieran Trippier
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 65.73
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Issa Kaboré replaced Benjamin White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.89 | 10.44 | 16.60 | 2.00 | 89.9 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.11 | 0.45 | 0.86 | 0.00 | 1.3 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.22 | 16.90 | 26.72 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 5.26 | 13.56 | 21.21 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Benjamin White | DEF | 1 | 5.8 | 4.81 | 12.34 | 19.52 | 0.00 | 90.0 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.99 | 6.62 | 11.05 | 1.00 | 78.6 | 90.0 |
| Bench 3 | Autosub In | Issa Kaboré | DEF | 12 | 4.0 | 2.09 | 6.39 | 11.05 | 1.00 | 70.5 | 86.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.13 | 22.95 | 39.06 | 16.00 | 89.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.74 | 17.30 | 27.37 | 6.00 | 86.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.2 | 4.48 | 13.60 | 22.17 | 5.00 | 84.5 | 78.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 6.12 | 18.59 | 31.07 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.45 | 15.81 | 24.58 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 4.74 | 14.61 | 25.13 | 5.00 | 57.9 | 80.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.78 | 13.54 | 21.01 | 2.00 | 86.5 | 90.0 |
| Bench 2 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 2.22 | 6.83 | 11.67 | 2.00 | 79.7 | 85.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.14
- Actual score: 45.00
- Transfer: Anthony Gordon -> Cole Palmer (projected gain 4.32, hit 0)
- Autosub: Benjamin White replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.86 | 10.42 | 16.46 | 3.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.06 | 0.25 | 0.54 | 0.00 | 2.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.93 | 14.35 | 23.34 | 1.00 | 88.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.47 | 12.92 | 19.72 | 6.00 | 90.0 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.84 | 7.73 | 12.65 | 1.00 | 81.8 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.93 | 5.46 | 9.64 | 0.00 | 59.7 | 0.0 |
| Bench 4 | Autosub In | Benjamin White | DEF | 1 | 5.7 | 0.48 | 2.82 | 5.93 | 1.00 | 7.3 | 1.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.20 | 23.08 | 39.19 | 7.00 | 88.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.81 | 15.88 | 24.32 | 5.00 | 80.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.1 | 3.73 | 11.44 | 18.82 | 2.00 | 66.3 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.88 | 16.94 | 26.77 | 8.00 | 88.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.99 | 14.94 | 24.68 | 2.00 | 86.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.36 | 13.92 | 21.34 | 2.00 | 90.0 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 3.87 | 12.07 | 20.94 | 0.00 | 56.5 | 0.0 |
| Bench 2 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 2.65 | 7.12 | 11.92 | 0.00 | 77.9 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.60 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 66.05
- Actual score: 81.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.42) beats the best remaining Bench Boost opportunity (5.10).
- Transfer: Jarrod Bowen -> Bryan Mbeumo (projected gain 10.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.42) beats the best remaining Bench Boost opportunity (5.10).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.75 | 10.00 | 15.94 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench Boost | Loris Karius | GK | 15 | 3.9 | 0.17 | 0.34 | 0.71 | 0.00 | 1.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.69 | 13.66 | 22.56 | 12.00 | 87.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.28 | 11.92 | 18.55 | 1.00 | 83.4 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.7 | 2.97 | 8.03 | 13.33 | 1.00 | 53.4 | 11.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.87 | 7.74 | 12.55 | 10.00 | 81.7 | 90.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.57 | 2.55 | 5.02 | 1.00 | 21.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.13 | 24.58 | 40.43 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.49 | 14.19 | 25.02 | 11.00 | 64.8 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 5.31 | 12.64 | 18.56 | 5.00 | 51.1 | 86.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.1 | 6.44 | 18.03 | 27.91 | 5.00 | 90.0 | 77.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.7 | 6.27 | 17.44 | 27.74 | 8.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.01 | 13.22 | 22.80 | 10.00 | 79.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.17 | 10.46 | 16.65 | 1.00 | 63.7 | 24.0 |
| Bench 3 | Bench Boost | Marvelous Nakamba | MID | 12 | 4.4 | 0.81 | 3.31 | 6.52 | 0.00 | 32.6 | 0.0 |

## GW15

- Train rows: 114034
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.91
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 2.21, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.13 | 9.21 | 15.10 | 0.00 | 83.6 | 0.0 |
| Bench 1 | Bench | Loris Karius | GK | 15 | 3.9 | 0.26 | 0.55 | 1.05 | 0.00 | 6.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.20 | 14.92 | 24.44 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 3.99 | 11.40 | 18.30 | 1.00 | 80.8 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.79 | 7.95 | 13.13 | 1.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.70 | 5.63 | 9.42 | 0.00 | 61.7 | 90.0 |
| Bench 2 | Bench | Benjamin White | DEF | 1 | 5.7 | 1.83 | 5.41 | 9.90 | 4.00 | 32.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.84 | 24.16 | 39.76 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.44 | 14.60 | 24.78 | 1.00 | 80.9 | 89.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.06 | 12.58 | 20.88 | 2.00 | 69.4 | 67.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.04 | 17.23 | 27.88 | 5.00 | 87.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.45 | 15.64 | 26.55 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 3.70 | 12.22 | 19.78 | 6.00 | 59.8 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.59 | 10.54 | 17.13 | 10.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 0.29 | 1.95 | 4.09 | 0.00 | 25.0 | 0.0 |