# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 256.33
- Total actual points: 234.00
- Average predicted points: 64.08
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
- Predicted score: 65.38
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Issa Kaboré replaced Benjamin White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.83 | 10.35 | 16.52 | 2.00 | 88.4 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.09 | 0.41 | 0.86 | 0.00 | 8.9 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.17 | 16.83 | 26.65 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 5.21 | 13.49 | 21.15 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Benjamin White | DEF | 1 | 5.8 | 4.76 | 12.26 | 19.45 | 0.00 | 90.0 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.93 | 6.53 | 10.95 | 1.00 | 76.9 | 90.0 |
| Bench 3 | Autosub In | Issa Kaboré | DEF | 12 | 4.0 | 1.99 | 6.24 | 10.88 | 1.00 | 67.7 | 86.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.12 | 23.08 | 39.29 | 16.00 | 88.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.70 | 17.25 | 27.31 | 6.00 | 86.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.2 | 4.43 | 13.56 | 22.12 | 5.00 | 84.3 | 78.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 6.08 | 18.51 | 31.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.42 | 15.77 | 24.54 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 4.76 | 14.43 | 25.01 | 5.00 | 58.5 | 80.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.75 | 13.46 | 21.04 | 2.00 | 85.9 | 90.0 |
| Bench 2 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 2.15 | 6.73 | 11.55 | 2.00 | 77.8 | 85.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.87
- Actual score: 45.00
- Transfer: Anthony Gordon -> Cole Palmer (projected gain 4.28, hit 0)
- Autosub: Benjamin White replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.80 | 10.33 | 16.37 | 3.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.35 | 0.59 | 0.97 | 0.00 | 7.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.88 | 14.29 | 23.28 | 1.00 | 87.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.43 | 12.86 | 19.68 | 6.00 | 90.0 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.78 | 7.64 | 12.57 | 1.00 | 80.2 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.89 | 5.39 | 9.61 | 0.00 | 59.0 | 0.0 |
| Bench 4 | Autosub In | Benjamin White | DEF | 1 | 5.7 | 0.43 | 2.26 | 4.95 | 1.00 | 6.8 | 1.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.24 | 22.97 | 39.08 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.78 | 15.84 | 24.30 | 5.00 | 80.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.1 | 3.69 | 11.36 | 18.75 | 2.00 | 65.2 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.86 | 16.90 | 26.74 | 8.00 | 87.7 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.95 | 14.88 | 24.63 | 2.00 | 85.7 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.33 | 13.82 | 21.23 | 2.00 | 90.0 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 3.89 | 11.91 | 20.79 | 0.00 | 58.5 | 0.0 |
| Bench 2 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 2.58 | 7.02 | 11.82 | 0.00 | 76.2 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.60 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.84
- Actual score: 81.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.64) beats the best remaining Bench Boost opportunity (5.32).
- Transfer: Jarrod Bowen -> Bryan Mbeumo (projected gain 10.46, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.64) beats the best remaining Bench Boost opportunity (5.32).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.69 | 9.91 | 15.87 | 2.00 | 86.1 | 90.0 |
| Bench 1 | Bench Boost | Jordan Amissah | GK | 17 | 3.9 | 0.22 | 0.46 | 0.87 | 0.00 | 7.0 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.64 | 13.60 | 22.50 | 12.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.24 | 11.87 | 18.53 | 1.00 | 82.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.7 | 2.84 | 7.76 | 12.86 | 1.00 | 50.3 | 11.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.81 | 7.65 | 12.47 | 10.00 | 80.1 | 90.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.73 | 2.85 | 5.47 | 1.00 | 27.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.10 | 24.54 | 40.40 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.49 | 14.05 | 24.91 | 11.00 | 66.2 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 5.34 | 12.47 | 18.86 | 5.00 | 51.0 | 86.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.1 | 6.42 | 17.96 | 27.64 | 5.00 | 90.0 | 77.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.7 | 6.24 | 17.39 | 27.70 | 8.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.96 | 13.13 | 22.72 | 10.00 | 77.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.12 | 10.41 | 16.62 | 1.00 | 62.4 | 24.0 |
| Bench 3 | Bench Boost | Marvelous Nakamba | MID | 12 | 4.4 | 0.87 | 2.96 | 5.75 | 0.00 | 33.9 | 0.0 |

## GW15

- Train rows: 114034
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 67.25
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.97) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 2.29, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.97) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.21 | 9.31 | 15.13 | 0.00 | 85.0 | 0.0 |
| Bench 1 | Bench | Jordan Amissah | GK | 17 | 3.9 | 0.03 | 0.14 | 0.37 | 0.00 | 7.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.31 | 15.05 | 24.49 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.08 | 11.53 | 18.36 | 1.00 | 82.5 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.88 | 8.05 | 13.16 | 1.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.74 | 5.67 | 9.37 | 0.00 | 61.7 | 90.0 |
| Bench 2 | Bench | Benjamin White | DEF | 1 | 5.7 | 1.81 | 5.33 | 9.71 | 4.00 | 30.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.97 | 24.34 | 39.86 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.53 | 14.72 | 24.85 | 1.00 | 82.3 | 89.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.16 | 12.71 | 20.93 | 2.00 | 71.0 | 67.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.16 | 17.38 | 27.95 | 5.00 | 89.5 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.54 | 15.75 | 26.59 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 3.79 | 12.34 | 19.83 | 6.00 | 61.1 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.69 | 10.66 | 17.19 | 10.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 0.29 | 1.93 | 3.98 | 0.00 | 23.9 | 0.0 |