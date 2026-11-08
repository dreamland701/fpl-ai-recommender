# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 233.70
- Total actual points: 287.00
- Average predicted points: 58.42
- Average actual points: 71.75
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
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 63.09
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.53 | 9.73 | 16.02 | 11.00 | 77.1 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.39 | 1.27 | 2.17 | 0.00 | 14.4 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.59 | 15.50 | 25.03 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.33 | 12.46 | 20.15 | 2.00 | 88.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.19 | 9.65 | 15.56 | 1.00 | 84.3 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.93 | 6.12 | 9.74 | 1.00 | 77.1 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 1.98 | 5.41 | 8.83 | 1.00 | 61.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.85 | 16.16 | 26.08 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.04 | 13.44 | 21.16 | 7.00 | 83.8 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.36 | 7.31 | 11.89 | 1.00 | 70.7 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.63 | 21.48 | 35.14 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.92 | 17.81 | 29.57 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.45 | 16.22 | 26.60 | 7.00 | 85.9 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.19 | 14.99 | 24.42 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.73 | 9.38 | 15.26 | 4.00 | 76.1 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.79
- Actual score: 44.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 19.33, hit 0)
- Autosub: Auston Trusty replaced Trent Alexander-Arnold.
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.99 | 11.02 | 18.00 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.42 | 1.40 | 3.06 | 0.00 | 11.8 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.50 | 13.10 | 21.22 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.84 | 12.38 | 25.12 | 0.00 | 71.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.43 | 9.72 | 15.58 | 17.00 | 86.9 | 80.0 |
| Bench 2 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.40 | 6.42 | 10.21 | 1.00 | 74.8 | 79.0 |
| Bench 3 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.31 | 6.22 | 12.28 | 2.00 | 70.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.03 | 17.04 | 27.18 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.22 | 11.93 | 22.77 | 2.00 | 66.6 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.31 | 6.53 | 10.61 | 1.00 | 50.4 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.41 | 19.55 | 30.94 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.16 | 16.58 | 30.53 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 5.01 | 14.15 | 22.70 | 2.00 | 88.6 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.95 | 12.02 | 26.97 | 0.00 | 31.8 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.84 | 8.36 | 13.30 | 2.00 | 70.8 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 3.60
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 55.72
- Actual score: 77.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.84).
- Transfer: Trent Alexander-Arnold -> Kieran Trippier (projected gain 8.78, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (6.03) beats the best remaining Triple Captain opportunity (6.84).
- Autosub: Amari'i Bell replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.45 | 9.68 | 15.59 | 3.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.41 | 1.37 | 2.54 | 0.00 | 11.5 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.39 | 12.21 | 15.79 | 1.00 | 82.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 3.45 | 10.53 | 17.78 | 7.00 | 72.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.22 | 8.56 | 13.79 | 2.00 | 69.1 | 90.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.39 | 6.32 | 10.21 | 6.00 | 72.0 | 90.0 |
| Bench 3 | Bench | Auston Trusty | DEF | 17 | 3.9 | 2.16 | 5.92 | 9.51 | 0.00 | 68.4 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.12 | 14.96 | 24.24 | 7.00 | 79.7 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.44 | 11.90 | 22.78 | 13.00 | 63.2 | 86.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.4 | 1.95 | 5.64 | 9.66 | 1.00 | 43.2 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 6.03 | 16.53 | 26.30 | 10.00 | 79.5 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.94 | 11.50 | 18.85 | 1.00 | 65.2 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.63 | 10.85 | 20.12 | 6.00 | 44.9 | 76.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.1 | 3.25 | 10.82 | 20.02 | 0.00 | 21.2 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.75 | 8.14 | 13.16 | 1.00 | 70.6 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 3.60 -> 0.40
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: bench_boost
- Predicted score: 57.10
- Actual score: 82.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.81) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Alejandro Garnacho -> Diogo Teixeira da Silva (projected gain 7.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.81) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.14 | 9.48 | 15.18 | 1.00 | 82.1 | 45.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.73 | 1.19 | 0.00 | 6.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.7 | 4.35 | 12.33 | 20.18 | 9.00 | 79.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.06 | 11.83 | 15.63 | 1.00 | 80.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 2.99 | 9.66 | 15.78 | -1.00 | 81.2 | 90.0 |
| Bench 3 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.19 | 8.52 | 10.27 | 0.00 | 71.2 | 90.0 |
| Bench 2 | Bench Boost | Auston Trusty | DEF | 17 | 3.9 | 2.28 | 6.10 | 9.60 | 0.00 | 72.3 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.88 | 16.64 | 25.18 | 2.00 | 67.8 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.76 | 16.00 | 25.86 | 18.00 | 90.0 | 90.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.3 | 1.34 | 4.79 | 8.64 | 1.00 | 30.0 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.56 | 16.75 | 27.36 | 9.00 | 85.0 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.31 | 16.53 | 24.42 | 20.00 | 64.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.0 | 3.38 | 15.85 | 20.47 | 0.00 | 32.8 | 0.0 |
| XI | XI | Diogo Teixeira da Silva | MID | 11 | 8.0 | 3.20 | 14.35 | 17.02 | 2.00 | 60.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.88 | 11.62 | 19.92 | 2.00 | 72.2 | 90.0 |