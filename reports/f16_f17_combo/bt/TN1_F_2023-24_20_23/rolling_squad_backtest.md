# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 233.34
- Total actual points: 298.00
- Average predicted points: 58.33
- Average actual points: 74.50
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
- Predicted score: 63.58
- Actual score: 84.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.59 | 9.31 | 15.08 | 11.00 | 78.8 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.8 | 0.26 | 0.96 | 1.82 | 0.00 | 9.8 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.4 | 5.63 | 16.25 | 25.97 | 0.00 | 90.0 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.36 | 12.85 | 20.52 | 2.00 | 89.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.23 | 9.60 | 15.35 | 1.00 | 85.2 | 90.0 |
| Bench 4 | Bench | Auston Trusty | DEF | 17 | 3.9 | 1.99 | 6.37 | 10.08 | 1.00 | 78.5 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.06 | 5.65 | 9.17 | 1.00 | 64.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.89 | 16.08 | 25.54 | 8.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 5.10 | 14.09 | 21.90 | 7.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.43 | 7.89 | 12.56 | 1.00 | 72.3 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.3 | 7.67 | 21.12 | 34.44 | 16.00 | 90.0 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.9 | 5.97 | 17.57 | 28.81 | 9.00 | 90.0 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.48 | 16.23 | 26.40 | 7.00 | 86.7 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 5.22 | 15.33 | 24.69 | 3.00 | 90.0 | 90.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 3.77 | 9.84 | 15.85 | 4.00 | 77.2 | 90.0 |

## GW21

- Train rows: 118627
- Bank: 0.00 -> 1.90
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Phil Foden
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 57.40
- Actual score: 44.00
- Transfer: Son Heung-min -> Phil Foden (projected gain 11.36, hit 0)
- Autosub: Amari'i Bell replaced Trent Alexander-Arnold.
- Autosub: Auston Trusty replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.89 | 10.61 | 17.53 | 3.00 | 89.8 | 90.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.43 | 1.15 | 2.18 | 0.00 | 13.3 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.7 | 4.53 | 13.53 | 21.80 | 6.00 | 90.0 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 11 | 8.4 | 3.75 | 12.45 | 20.94 | 0.00 | 69.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.36 | 9.50 | 15.56 | 17.00 | 85.5 | 80.0 |
| Bench 3 | Autosub In | Auston Trusty | DEF | 17 | 3.9 | 2.34 | 6.39 | 10.45 | 1.00 | 73.7 | 79.0 |
| Bench 2 | Autosub In | Amari'i Bell | DEF | 12 | 3.9 | 2.36 | 6.29 | 10.36 | 2.00 | 71.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 6.05 | 17.04 | 26.85 | 1.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.29 | 12.95 | 20.31 | 2.00 | 68.5 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.5 | 2.30 | 6.66 | 10.99 | 1.00 | 50.9 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 7.30 | 19.48 | 30.73 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Phil Foden | MID | 13 | 7.9 | 6.20 | 17.63 | 26.81 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 4.91 | 14.26 | 23.16 | 2.00 | 86.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.2 | 2.91 | 11.09 | 21.38 | 0.00 | 31.1 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.90 | 8.85 | 13.98 | 2.00 | 72.2 | 90.0 |

## GW22

- Train rows: 119414
- Bank: 1.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Ollie Watkins
- Effective captain: Bukayo Saka
- Chip used: bench_boost
- Predicted score: 56.40
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (6.89) beats the best remaining Bench Boost opportunity (7.55).
- Transfer: Auston Trusty -> William Saliba (projected gain 4.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (6.89) beats the best remaining Bench Boost opportunity (7.55).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.38 | 9.41 | 15.76 | 3.00 | 78.4 | 90.0 |
| Bench 1 | Bench Boost | Caoimhin Kelleher | GK | 11 | 3.7 | 0.43 | 1.09 | 2.15 | 0.00 | 12.8 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.30 | 12.66 | 20.89 | 1.00 | 81.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.91 | 10.75 | 17.45 | 2.00 | 81.4 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.17 | 8.88 | 14.47 | 2.00 | 67.9 | 90.0 |
| Bench 3 | Bench Boost | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.17 | 8.63 | 15.62 | 1.00 | 26.5 | 22.0 |
| Bench 2 | Bench Boost | Amari'i Bell | DEF | 12 | 3.9 | 2.31 | 6.23 | 10.38 | 6.00 | 70.6 | 90.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.8 | 5.04 | 14.72 | 23.94 | 7.00 | 78.1 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.36 | 12.86 | 20.43 | 13.00 | 61.8 | 86.0 |
| Bench 4 | Bench Boost | Cameron Archer | FWD | 17 | 4.4 | 1.98 | 6.00 | 10.33 | 1.00 | 44.9 | 3.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 9.0 | 5.95 | 16.84 | 26.95 | 10.00 | 77.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 11 | 13.1 | 3.31 | 12.70 | 23.47 | 0.00 | 22.6 | 0.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 8.0 | 3.89 | 12.05 | 20.66 | 1.00 | 64.1 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 3.56 | 11.94 | 19.08 | 6.00 | 43.3 | 76.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.69 | 8.30 | 13.83 | 1.00 | 69.6 | 90.0 |

## GW23

- Train rows: 120213
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Ollie Watkins
- Vice captain: Bukayo Saka
- Effective captain: Ollie Watkins
- Chip used: triple_captain
- Predicted score: 55.95
- Actual score: 106.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.82) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Ollie Watkins. Optimizer chose Triple Captain here because the current estimated captain upside (5.82) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Trent Alexander-Arnold replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.2 | 3.20 | 9.62 | 15.62 | 1.00 | 83.8 | 45.0 |
| Bench 1 | Bench | Caoimhin Kelleher | GK | 11 | 3.7 | 0.00 | 0.29 | 0.78 | 0.00 | 1.8 | 0.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.8 | 4.12 | 12.11 | 19.80 | 1.00 | 82.2 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.6 | 3.53 | 10.39 | 16.74 | 1.00 | 83.4 | 90.0 |
| Bench 2 | Autosub In | Trent Alexander-Arnold | DEF | 11 | 8.4 | 2.79 | 10.07 | 17.17 | 1.00 | 45.8 | 57.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 5.0 | 3.05 | 9.83 | 15.76 | -1.00 | 82.7 | 90.0 |
| Bench 3 | Bench | Amari'i Bell | DEF | 12 | 3.9 | 2.25 | 6.86 | 10.91 | 0.00 | 72.9 | 90.0 |
| Captain | Captain | Ollie Watkins | FWD | 2 | 8.8 | 5.82 | 16.27 | 26.18 | 18.00 | 90.0 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.9 | 4.68 | 12.97 | 21.56 | 2.00 | 60.8 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 17 | 4.3 | 1.25 | 4.34 | 8.12 | 1.00 | 26.4 | 25.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.61 | 16.74 | 26.77 | 9.00 | 86.4 | 78.0 |
| XI | XI | Phil Foden | MID | 13 | 7.9 | 4.37 | 13.02 | 21.43 | 20.00 | 66.1 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.9 | 3.95 | 11.93 | 20.51 | 2.00 | 74.1 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 11 | 13.0 | 3.06 | 11.83 | 20.70 | 0.00 | 25.0 | 0.0 |
| XI | XI | Alejandro Garnacho | MID | 14 | 4.8 | 2.92 | 9.08 | 14.38 | 16.00 | 70.0 | 90.0 |