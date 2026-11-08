# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW19
- Simulated weeks: GW20-GW23
- Total predicted points: 277.51
- Total actual points: 244.00
- Average predicted points: 69.38
- Average actual points: 61.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW19 are included before the first simulated week.
- League-average scores were not available for this run.

## GW20

- Train rows: 146484
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.64
- Actual score: 71.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jacob Murphy replaced Morgan Rogers.
- Autosub: João Pedro Junqueira de Jesus replaced Matheus Santos Carneiro Da Cunha.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.82 | 11.31 | 18.70 | 3.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.8 | 3.22 | 9.53 | 15.54 | 9.00 | 88.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.93 | 13.64 | 22.14 | 0.00 | 83.9 | 85.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.34 | 12.19 | 20.03 | 1.00 | 88.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 3.91 | 11.69 | 19.25 | 2.00 | 81.2 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.1 | 3.74 | 11.19 | 18.16 | 6.00 | 84.9 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.7 | 3.78 | 11.06 | 17.72 | 2.00 | 80.6 | 90.0 |
| XI | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 7.1 | 4.06 | 12.98 | 21.43 | 0.00 | 72.1 | 0.0 |
| Bench 3 | Autosub In | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.68 | 11.37 | 18.82 | 9.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Jamie Vardy | FWD | 11 | 5.6 | 2.90 | 8.86 | 14.41 | 5.00 | 60.6 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 9.74 | 26.89 | 43.96 | 7.00 | 112.4 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.70 | 20.56 | 34.07 | 10.00 | 94.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 5.10 | 14.79 | 24.27 | 19.00 | 89.4 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 5.5 | 4.77 | 13.02 | 20.92 | 0.00 | 86.4 | 0.0 |
| Bench 2 | Autosub In | Jacob Murphy | MID | 15 | 5.0 | 3.73 | 11.70 | 19.19 | 5.00 | 70.1 | 85.0 |

## GW21

- Train rows: 147195
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 62.70
- Actual score: 48.00
- Transfer: Matheus Santos Carneiro Da Cunha -> Chris Wood (projected gain 0.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.97 | 11.31 | 18.56 | 2.00 | 86.5 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.8 | 3.06 | 9.71 | 15.94 | 3.00 | 86.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 3.99 | 12.49 | 20.64 | 2.00 | 75.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.07 | 11.92 | 19.60 | 7.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Ola Aina | DEF | 16 | 5.1 | 3.71 | 11.40 | 18.38 | 2.00 | 84.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.3 | 4.00 | 11.10 | 18.04 | 2.00 | 82.5 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.7 | 3.75 | 11.03 | 17.40 | 6.00 | 73.1 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 3.99 | 12.13 | 19.20 | 9.00 | 72.7 | 89.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 4.06 | 11.42 | 18.61 | 1.00 | 80.8 | 77.0 |
| Bench 3 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.26 | 9.51 | 15.34 | 2.00 | 67.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.86 | 26.47 | 43.69 | 2.00 | 104.7 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.31 | 21.42 | 35.63 | 10.00 | 104.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.6 | 5.80 | 17.11 | 27.60 | 2.00 | 99.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.0 | 4.03 | 12.07 | 19.54 | 3.00 | 75.8 | 77.0 |
| Bench 4 | Bench | Morgan Rogers | MID | 2 | 5.5 | 2.24 | 7.65 | 13.52 | 6.00 | 40.2 | 90.0 |

## GW22

- Train rows: 147919
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 73.45
- Actual score: 57.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (11.46).
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Morgan Rogers -> Amad Diallo (projected gain 4.31, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (8.68) beats the best remaining Triple Captain opportunity (11.46).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martin | GK | 1 | 5.6 | 3.62 | 10.63 | 17.62 | 1.00 | 85.0 | 90.0 |
| XI | XI | Matz Sels | GK | 16 | 4.8 | 3.65 | 10.44 | 17.17 | 1.00 | 87.3 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 4.9 | 4.61 | 13.09 | 21.41 | 8.00 | 92.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.04 | 12.52 | 21.10 | 11.00 | 78.4 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.1 | 4.20 | 11.84 | 19.29 | 4.00 | 85.1 | 90.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 3.92 | 11.08 | 17.52 | 4.00 | 75.9 | 65.0 |
| Bench 4 | Bench | William Saliba | DEF | 1 | 6.3 | 3.63 | 10.45 | 17.03 | 0.00 | 80.6 | 0.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.8 | 4.87 | 13.64 | 22.46 | 12.00 | 83.3 | 82.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.7 | 3.63 | 10.71 | 17.64 | 2.00 | 72.2 | 90.0 |
| Bench 2 | Bench | Jamie Vardy | FWD | 11 | 5.5 | 3.70 | 10.32 | 16.47 | 2.00 | 74.3 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.68 | 25.75 | 42.20 | 3.00 | 98.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 7.44 | 21.74 | 35.85 | 2.00 | 104.7 | 83.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.55 | 16.70 | 27.60 | 2.00 | 95.6 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 5.17 | 14.61 | 23.50 | 2.00 | 94.8 | 90.0 |
| XI | XI | Jacob Murphy | MID | 15 | 5.0 | 3.93 | 11.53 | 19.25 | 2.00 | 73.0 | 65.0 |

## GW23

- Train rows: 148648
- Bank: 0.30 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Cole Palmer
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 76.71
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.74) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Jamie Vardy -> Raúl Jiménez (projected gain 0.41, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.74) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martin | GK | 1 | 5.6 | 3.48 | 10.39 | 17.21 | 9.00 | 85.5 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 4.9 | 3.10 | 9.66 | 15.92 | 1.00 | 84.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.1 | 4.90 | 14.22 | 23.09 | 5.00 | 85.4 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.0 | 4.55 | 12.80 | 20.90 | 2.00 | 90.9 | 90.0 |
| XI | XI | Ola Aina | DEF | 16 | 5.2 | 4.02 | 11.88 | 19.28 | 1.00 | 90.0 | 78.0 |
| XI | XI | Lewis Hall | DEF | 15 | 4.8 | 4.17 | 11.28 | 17.90 | 2.00 | 72.9 | 90.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | 1 | 6.3 | 2.14 | 6.87 | 11.76 | 9.00 | 45.0 | 90.0 |
| XI | XI | Chris Wood | FWD | 16 | 6.9 | 4.99 | 14.70 | 23.53 | 2.00 | 82.2 | 90.0 |
| XI | XI | Raúl Jiménez | FWD | 9 | 5.7 | 4.00 | 11.10 | 17.89 | 2.00 | 63.2 | 63.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.6 | 3.60 | 10.59 | 17.38 | 1.00 | 73.7 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.6 | 8.35 | 24.29 | 39.79 | 8.00 | 92.3 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.4 | 6.61 | 20.27 | 34.02 | 2.00 | 95.3 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.7 | 5.76 | 16.85 | 28.10 | 7.00 | 96.9 | 90.0 |
| XI | XI | Amad Diallo | MID | 14 | 5.4 | 4.80 | 14.11 | 23.02 | 3.00 | 90.2 | 90.0 |
| Bench 2 | Bench Boost | Jacob Murphy | MID | 15 | 5.0 | 3.89 | 10.75 | 18.01 | 6.00 | 68.8 | 90.0 |