# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW11
- Simulated weeks: GW12-GW15
- Total predicted points: 251.54
- Total actual points: 218.00
- Average predicted points: 62.88
- Average actual points: 54.50
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
- Bank: 100.00 -> 0.60
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Kaoru Mitoma
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 60.61
- Actual score: 68.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.13 | 12.51 | 19.22 | 2.00 | 85.8 | 90.0 |
| Bench 1 | Bench | Guglielmo Vicario | GK | 18 | 5.2 | 3.78 | 11.23 | 20.83 | 1.00 | 89.3 | 90.0 |
| Bench 4 | Bench | Kieran Trippier | DEF | 15 | 7.0 | 3.27 | 16.09 | 26.39 | 1.00 | 76.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.3 | 3.91 | 11.81 | 19.54 | 9.00 | 77.3 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.51 | 11.05 | 17.37 | 1.00 | 83.5 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 3.49 | 10.51 | 18.12 | 5.00 | 84.6 | 90.0 |
| Bench 3 | Bench | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 3.42 | 10.40 | 18.00 | 6.00 | 85.8 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 5.39 | 13.92 | 20.08 | 5.00 | 79.4 | 90.0 |
| Bench 2 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.5 | 3.69 | 10.70 | 18.63 | 5.00 | 84.4 | 90.0 |
| XI | XI | Eddie Nketiah | FWD | 1 | 5.7 | 4.87 | 9.11 | 17.25 | 1.00 | 76.0 | 9.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 8.44 | 22.49 | 40.23 | 16.00 | 87.8 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 4.65 | 18.04 | 35.39 | 2.00 | 87.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.6 | 4.57 | 16.55 | 29.77 | 8.00 | 89.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 3.74 | 16.35 | 27.39 | 2.00 | 85.8 | 90.0 |
| Vice Captain | XI | Kaoru Mitoma | MID | 5 | 6.5 | 5.46 | 16.10 | 23.53 | 1.00 | 82.4 | 45.0 |

## GW13

- Train rows: 112534
- Bank: 0.60 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Jarrod Bowen
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.51
- Actual score: 46.00
- Transfer: Kaoru Mitoma -> James Ward-Prowse (projected gain 6.46, hit 0)
- Autosub: Eddie Nketiah replaced Jarrod Bowen.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.20 | 12.02 | 19.36 | 3.00 | 85.4 | 90.0 |
| Bench 1 | Bench | Guglielmo Vicario | GK | 18 | 5.2 | 3.50 | 11.82 | 19.64 | 2.00 | 88.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.91 | 14.95 | 21.31 | 1.00 | 88.6 | 90.0 |
| Bench 4 | Bench | Fabian Schär | DEF | 15 | 5.2 | 2.87 | 10.67 | 17.05 | 2.00 | 86.0 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 5.3 | 3.07 | 10.30 | 16.48 | 6.00 | 86.6 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 3.32 | 10.27 | 17.65 | 5.00 | 88.4 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 3.33 | 10.22 | 17.18 | 12.00 | 84.6 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 3.52 | 12.51 | 19.96 | 1.00 | 82.1 | 84.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.5 | 3.43 | 11.40 | 19.60 | 7.00 | 82.7 | 82.0 |
| Bench 2 | Autosub In | Eddie Nketiah | FWD | 1 | 5.7 | 3.35 | 8.70 | 15.61 | 1.00 | 63.4 | 24.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 12.9 | 6.04 | 20.78 | 36.04 | 5.00 | 89.2 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.7 | 5.80 | 18.03 | 32.76 | 2.00 | 88.4 | 90.0 |
| Vice Captain | Bench | Jarrod Bowen | MID | 19 | 7.6 | 5.92 | 15.91 | 27.27 | 0.00 | 82.2 | 0.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.8 | 4.23 | 15.68 | 28.07 | 2.00 | 87.7 | 90.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.2 | 4.77 | 15.10 | 21.31 | 2.00 | 86.4 | 90.0 |

## GW14

- Train rows: 113281
- Bank: 0.90 -> 2.80
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.27
- Actual score: 58.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.83) beats the best remaining Triple Captain opportunity (9.95).
- Transfer: Jarrod Bowen -> Morgan Gibbs-White (projected gain 8.40, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (7.83) beats the best remaining Triple Captain opportunity (9.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alphonse Areola | GK | 19 | 4.3 | 4.31 | 12.24 | 18.47 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Guglielmo Vicario | GK | 18 | 5.2 | 2.45 | 10.44 | 16.70 | 1.00 | 88.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.16 | 11.98 | 25.56 | 12.00 | 86.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 3.63 | 11.66 | 18.51 | 1.00 | 85.7 | 90.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.2 | 2.25 | 9.55 | 15.78 | 0.00 | 89.4 | 90.0 |
| XI | XI | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 2.80 | 8.47 | 15.33 | 2.00 | 86.7 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 2.50 | 7.59 | 15.93 | 6.00 | 83.9 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.5 | 4.80 | 13.23 | 20.27 | 2.00 | 78.9 | 90.0 |
| Bench 3 | Bench | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.5 | 2.40 | 12.40 | 20.06 | 5.00 | 76.9 | 90.0 |
| Bench 2 | Bench | Eddie Nketiah | FWD | 1 | 5.7 | 2.49 | 7.03 | 10.77 | 1.00 | 39.2 | 23.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.83 | 21.51 | 38.12 | 5.00 | 86.9 | 90.0 |
| XI | XI | Son Heung-min | MID | 18 | 9.6 | 3.56 | 17.61 | 26.32 | 10.00 | 74.1 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 5.7 | 5.13 | 15.05 | 22.73 | 2.00 | 82.6 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 6.9 | 5.29 | 14.71 | 28.09 | 5.00 | 81.7 | 77.0 |
| XI | XI | James Ward-Prowse | MID | 19 | 6.2 | 4.60 | 11.21 | 18.16 | 1.00 | 83.6 | 90.0 |

## GW15

- Train rows: 114034
- Bank: 2.80 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Son Heung-min
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 71.14
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.74) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Morgan Gibbs-White -> Martin Ødegaard (projected gain 5.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.74) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Guglielmo Vicario | GK | 18 | 5.2 | 4.15 | 11.88 | 21.14 | 2.00 | 88.2 | 90.0 |
| Bench 1 | Bench Boost | Alphonse Areola | GK | 19 | 4.3 | 2.84 | 11.54 | 16.78 | 0.00 | 85.6 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 7.0 | 4.59 | 12.79 | 23.47 | 1.00 | 86.7 | 90.0 |
| XI | XI | Pedro Porro | DEF | 18 | 5.2 | 3.89 | 12.06 | 21.35 | 5.00 | 86.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.4 | 4.15 | 10.08 | 16.76 | 1.00 | 84.4 | 90.0 |
| XI | XI | Fabian Schär | DEF | 15 | 5.2 | 3.63 | 9.21 | 15.98 | 1.00 | 83.5 | 90.0 |
| Bench 3 | Bench Boost | Diogo Dalot Teixeira | DEF | 14 | 5.0 | 2.49 | 8.09 | 15.00 | 1.00 | 85.4 | 90.0 |
| XI | XI | Matheus Santos Carneiro Da Cunha | FWD | 20 | 5.5 | 4.39 | 11.47 | 20.07 | 5.00 | 85.2 | 86.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 11 | 7.6 | 4.62 | 10.34 | 21.75 | 3.00 | 72.9 | 23.0 |
| Bench 4 | Bench Boost | Eddie Nketiah | FWD | 1 | 5.6 | 2.15 | 8.12 | 13.70 | 0.00 | 41.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 11 | 13.0 | 7.10 | 24.30 | 39.33 | 3.00 | 87.3 | 66.0 |
| XI | XI | Martin Ødegaard | MID | 1 | 8.3 | 5.88 | 17.04 | 23.66 | 5.00 | 74.9 | 90.0 |
| Vice Captain | XI | Son Heung-min | MID | 18 | 9.6 | 6.31 | 17.02 | 30.15 | 2.00 | 88.8 | 87.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 6.9 | 4.59 | 14.90 | 26.98 | 6.00 | 87.1 | 39.0 |
| Bench 2 | Bench Boost | James Ward-Prowse | MID | 19 | 6.2 | 3.26 | 11.10 | 14.74 | 8.00 | 68.9 | 90.0 |