# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 255.56
- Total actual points: 234.00
- Average predicted points: 63.89
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
- Predicted score: 65.78
- Actual score: 73.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Issa Kaboré replaced Benjamin White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.89 | 10.43 | 16.60 | 2.00 | 89.9 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.25 | 0.58 | 0.91 | 0.00 | 3.4 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 7.0 | 6.22 | 16.91 | 26.73 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 5.21 | 13.49 | 21.14 | 9.00 | 90.0 | 90.0 |
| XI | Bench | Benjamin White | DEF | 1 | 5.8 | 4.76 | 12.26 | 19.44 | 0.00 | 90.0 | 0.0 |
| Bench 4 | Bench | Charlie Taylor | DEF | 6 | 4.0 | 1.99 | 6.62 | 11.04 | 1.00 | 78.5 | 90.0 |
| Bench 3 | Autosub In | Issa Kaboré | DEF | 12 | 4.0 | 2.09 | 6.40 | 11.06 | 1.00 | 70.5 | 86.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.22 | 23.15 | 39.34 | 16.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 5.74 | 17.30 | 27.36 | 6.00 | 86.9 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.2 | 4.43 | 13.57 | 22.13 | 5.00 | 84.4 | 78.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 6.12 | 18.57 | 31.14 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 5.45 | 15.81 | 24.57 | 8.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.6 | 4.72 | 14.71 | 25.48 | 5.00 | 57.1 | 80.0 |
| XI | XI | Anthony Gordon | MID | 15 | 5.8 | 4.79 | 13.52 | 21.10 | 2.00 | 86.7 | 90.0 |
| Bench 2 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 2.22 | 6.83 | 11.66 | 2.00 | 79.7 | 85.0 |

## GW13

- Train rows: 112534
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 57.96
- Actual score: 45.00
- Transfer: Anthony Gordon -> Cole Palmer (projected gain 4.18, hit 0)
- Autosub: Benjamin White replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.86 | 10.41 | 16.45 | 3.00 | 88.7 | 90.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.14 | 0.38 | 0.70 | 0.00 | 2.1 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.93 | 14.36 | 23.34 | 1.00 | 88.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 4.47 | 12.92 | 19.72 | 6.00 | 90.0 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.84 | 7.73 | 12.65 | 1.00 | 81.8 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.94 | 5.46 | 9.65 | 0.00 | 59.8 | 0.0 |
| Bench 4 | Autosub In | Benjamin White | DEF | 1 | 5.7 | 0.47 | 2.80 | 5.89 | 1.00 | 7.4 | 1.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.16 | 23.14 | 39.48 | 7.00 | 87.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.81 | 15.88 | 24.31 | 5.00 | 80.8 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.1 | 3.73 | 11.45 | 18.84 | 2.00 | 66.4 | 90.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.6 | 5.89 | 16.95 | 26.78 | 8.00 | 88.4 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.99 | 14.94 | 24.67 | 2.00 | 86.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 4.31 | 13.78 | 21.17 | 2.00 | 90.0 | 74.0 |
| XI | Bench | Jarrod Bowen | MID | 19 | 7.6 | 3.82 | 12.11 | 21.20 | 0.00 | 56.1 | 0.0 |
| Bench 2 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 2.65 | 7.12 | 11.91 | 0.00 | 77.9 | 0.0 |

## GW14

- Train rows: 113281
- Bank: 0.60 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bryan Mbeumo
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 65.89
- Actual score: 81.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (4.35) beats the best remaining Bench Boost opportunity (5.01).
- Transfer: Jarrod Bowen -> Bryan Mbeumo (projected gain 10.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (4.35) beats the best remaining Bench Boost opportunity (5.01).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 3.74 | 9.99 | 15.94 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench Boost | João Neves Virgínia | GK | 9 | 3.9 | 0.10 | 0.32 | 0.60 | 0.00 | 1.9 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.69 | 13.66 | 22.55 | 12.00 | 87.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.28 | 11.93 | 18.55 | 1.00 | 83.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.7 | 2.93 | 7.91 | 13.00 | 1.00 | 52.7 | 11.0 |
| Bench 2 | Bench Boost | Charlie Taylor | DEF | 6 | 4.0 | 2.87 | 7.74 | 12.55 | 10.00 | 81.7 | 90.0 |
| Bench 4 | Bench Boost | Issa Kaboré | DEF | 12 | 4.0 | 0.57 | 2.55 | 5.02 | 1.00 | 21.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 8.13 | 24.57 | 40.41 | 7.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.42 | 14.22 | 25.31 | 11.00 | 64.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 5.38 | 12.54 | 18.94 | 5.00 | 51.9 | 86.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.1 | 6.39 | 17.90 | 27.55 | 5.00 | 90.0 | 77.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.7 | 6.27 | 17.45 | 27.75 | 8.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 4.01 | 13.22 | 22.80 | 10.00 | 79.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 5.2 | 3.16 | 10.46 | 16.64 | 1.00 | 63.7 | 24.0 |
| Bench 3 | Bench Boost | Marvelous Nakamba | MID | 12 | 4.4 | 0.82 | 3.31 | 6.52 | 0.00 | 32.6 | 0.0 |

## GW15

- Train rows: 114034
- Bank: 1.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 65.93
- Actual score: 35.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Cole Palmer -> Hwang Hee-chan (projected gain 2.21, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Alphonse Areola | GK | 19 | 4.3 | 3.13 | 9.21 | 15.10 | 0.00 | 83.6 | 0.0 |
| Bench 1 | Bench | João Neves Virgínia | GK | 9 | 3.9 | 0.23 | 0.52 | 0.98 | 0.00 | 7.2 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 5.21 | 14.93 | 24.43 | 1.00 | 90.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 3.99 | 11.40 | 18.30 | 1.00 | 80.8 | 90.0 |
| XI | XI | Charlie Taylor | DEF | 6 | 4.0 | 2.79 | 7.95 | 13.13 | 1.00 | 80.3 | 90.0 |
| Bench 3 | Bench | Issa Kaboré | DEF | 12 | 4.0 | 1.69 | 5.62 | 9.41 | 0.00 | 61.7 | 90.0 |
| Bench 2 | Bench | Benjamin White | DEF | 1 | 5.7 | 1.83 | 5.41 | 9.90 | 4.00 | 32.4 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.0 | 7.84 | 24.15 | 39.73 | 2.00 | 90.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.4 | 4.45 | 14.60 | 24.77 | 1.00 | 80.9 | 89.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 7.0 | 4.06 | 12.59 | 20.88 | 2.00 | 69.4 | 67.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.7 | 6.04 | 17.23 | 27.88 | 5.00 | 87.3 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 5.45 | 15.65 | 26.56 | 2.00 | 90.0 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.1 | 3.70 | 12.22 | 19.77 | 6.00 | 59.8 | 39.0 |
| XI | XI | Hwang Hee-chan | MID | 20 | 5.6 | 3.59 | 10.54 | 17.12 | 10.00 | 81.8 | 90.0 |
| Bench 4 | Bench | Marvelous Nakamba | MID | 12 | 4.4 | 0.29 | 1.95 | 4.08 | 0.00 | 24.9 | 0.0 |