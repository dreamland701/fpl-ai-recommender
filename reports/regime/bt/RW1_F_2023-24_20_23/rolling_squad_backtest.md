# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 230.06
- Total actual points: 274.00
- Average predicted points: 57.51
- Average actual points: 68.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW19 are included before the first simulated week.
- League-average scores were not available for this run.

## GW20

- Train rows: 117854
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Trent Alexander-Arnold
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.85
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.30 | 8.76 | 14.05 | 11.00 | 76.1 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.36 | 1.18 | 2.06 | 0.00 | 14.4 | 0.0 |
| Vice Captain | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.81 | 16.60 | 26.58 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.41 | 12.85 | 20.39 | 2.00 | 89.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.78 | 10.87 | 17.73 | 0.00 | 89.4 | 90.0 |
| Bench 2 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.02 | 6.26 | 9.91 | 1.00 | 77.2 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.93 | 5.40 | 8.71 | 1.00 | 62.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.73 | 15.67 | 24.83 | 8.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.42 | 11.16 | 17.17 | 2.00 | 80.9 | 90.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 1.71 | 4.75 | 7.08 | 0.00 | 47.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.42 | 20.54 | 33.60 | 16.00 | 90.0 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.9 | 5.68 | 16.94 | 27.88 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.34 | 16.33 | 26.44 | 7.00 | 83.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.01 | 14.66 | 23.65 | 3.00 | 90.0 | 90.0 |
| XI | XI | Michael Olise | MID | 8 | 5.8 | 3.54 | 11.01 | 18.31 | 15.00 | 79.8 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.78
- Actual score: 32.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 10.58, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Amari'i Bell replaced Michael Olise.
- Autosub: Rodrigo Muniz Carvalho replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.69 | 9.92 | 16.10 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.45 | 1.31 | 2.33 | 0.00 | 12.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.58 | 13.18 | 21.15 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.80 | 13.11 | 21.74 | 0.00 | 74.8 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 4.03 | 10.73 | 17.11 | 6.00 | 86.5 | 90.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.42 | 6.36 | 10.17 | 1.00 | 75.2 | 79.0 |
| Bench 3 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.29 | 6.13 | 10.10 | 2.00 | 71.0 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.92 | 16.36 | 25.48 | 1.00 | 90.0 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 4.66 | 12.77 | 19.52 | 2.00 | 86.1 | 90.0 |
| Bench 4 | Autosub In | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 0.74 | 2.67 | 4.47 | 1.00 | 20.0 | 8.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.39 | 19.14 | 29.69 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.27 | 16.88 | 25.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.86 | 13.62 | 21.80 | 2.00 | 88.9 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.49 | 10.97 | 21.10 | 0.00 | 27.1 | 0.0 |
| XI | Bench | Michael Olise | MID | 8 | 5.8 | 2.71 | 10.00 | 17.66 | 0.00 | 70.9 | 0.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 55.03
- Actual score: 61.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (6.67).
- Transfer: Michael Olise -> Pascal Groß (projected gain 5.02, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (5.88) beats the best remaining Triple Captain opportunity (6.67).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.18 | 8.62 | 14.15 | 3.00 | 79.7 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.49 | 1.16 | 2.11 | 0.00 | 12.0 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.40 | 12.12 | 19.71 | 1.00 | 84.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.84 | 10.03 | 16.19 | 2.00 | 81.4 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.48 | 8.79 | 15.62 | 1.00 | 30.9 | 22.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.46 | 6.26 | 10.19 | 6.00 | 72.8 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.20 | 6.18 | 9.95 | 0.00 | 69.5 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.00 | 14.43 | 22.79 | 7.00 | 78.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.51 | 10.32 | 16.39 | 2.00 | 71.6 | 70.0 |
| Bench 4 | Bench | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 1.24 | 3.43 | 5.46 | 1.00 | 23.1 | 45.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.88 | 16.08 | 25.38 | 10.00 | 79.0 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.80 | 12.47 | 21.90 | 0.00 | 26.5 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.16 | 11.46 | 19.16 | 1.00 | 69.9 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.62 | 11.24 | 18.33 | 2.00 | 74.7 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.39 | 10.82 | 17.49 | 6.00 | 50.4 | 76.0 |

## GW23

- Train rows: 120213
- Bank: 1.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 55.38
- Actual score: 92.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Timo Werner (projected gain 3.97, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 2.90 | 8.61 | 13.96 | 1.00 | 80.2 | 45.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.52 | 1.02 | 0.00 | 7.2 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 3.98 | 11.67 | 19.07 | 1.00 | 82.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.07 | 10.40 | 17.43 | 1.00 | 51.7 | 57.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.35 | 9.88 | 15.87 | 1.00 | 80.7 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.42 | 6.36 | 10.04 | 0.00 | 73.5 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.13 | 6.33 | 10.30 | 0.00 | 71.6 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.61 | 15.54 | 24.50 | 18.00 | 88.5 | 90.0 |
| XI | XI | Timo Werner | FWD | 18 | 6.5 | 3.73 | 10.32 | 16.62 | 2.00 | 68.7 | 85.0 |
| Bench 4 | Bench Boost | Rodrigo Muniz Carvalho | FWD | 10 | 4.4 | 1.54 | 3.98 | 6.28 | 8.00 | 34.1 | 73.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.49 | 16.37 | 25.89 | 9.00 | 82.8 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.35 | 12.86 | 20.98 | 20.00 | 65.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.54 | 12.56 | 21.01 | 0.00 | 34.5 | 0.0 |
| XI | XI | Pascal Groß | MID | 5 | 6.5 | 3.81 | 11.57 | 18.76 | 11.00 | 79.6 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.86 | 11.41 | 19.50 | 2.00 | 72.5 | 90.0 |