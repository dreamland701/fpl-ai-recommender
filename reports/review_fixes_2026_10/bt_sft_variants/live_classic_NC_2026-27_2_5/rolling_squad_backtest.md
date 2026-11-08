# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 269.36
- Total actual points: 264.00
- Average predicted points: 67.34
- Average actual points: 66.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 191634
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: João Pedro
- Vice captain: B.Fernandes
- Effective captain: João Pedro
- Chip used: none
- Predicted score: 66.38
- Actual score: 82.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.29 | 12.46 | 20.15 | 6.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.28 | 9.62 | 16.12 | 10.00 | 87.6 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.32 | 15.04 | 24.46 | 1.00 | 77.6 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.88 | 13.98 | 22.78 | 2.00 | 92.5 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 4.95 | 13.51 | 21.52 | 1.00 | 90.6 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.66 | 13.33 | 21.38 | 11.00 | 92.6 | 90.0 |
| Bench 3 | Bench | Egan | DEF | 11 | 4.0 | 4.45 | 12.60 | 20.26 | 9.00 | 96.0 | 90.0 |
| Captain | Captain | João Pedro | FWD | 6 | 7.6 | 6.57 | 17.91 | 28.84 | 9.00 | 111.6 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 4 | 8.0 | 4.66 | 13.40 | 21.97 | 2.00 | 77.3 | 90.0 |
| Bench 4 | Bench | Gonzalo | FWD | 10 | 6.0 | 4.07 | 11.66 | 18.94 | 2.00 | 87.2 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.47 | 19.06 | 31.62 | 23.00 | 99.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 6.06 | 17.04 | 27.68 | 4.00 | 109.2 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 6.01 | 16.79 | 27.17 | 4.00 | 88.7 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 5.42 | 15.05 | 24.36 | 7.00 | 88.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 5.17 | 14.77 | 24.26 | 5.00 | 82.6 | 90.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Wissa
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 63.71
- Actual score: 38.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Gonzalo -> Wissa (projected gain 2.84, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 6.0 | 3.79 | 11.33 | 18.56 | 3.00 | 84.0 | 90.0 |
| XI | XI | Tzolakis | GK | 11 | 4.5 | 3.95 | 11.04 | 17.96 | 6.00 | 96.2 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.85 | 13.82 | 22.08 | 2.00 | 91.7 | 66.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.98 | 13.65 | 21.59 | 6.00 | 103.3 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.01 | 11.62 | 19.12 | 8.00 | 76.8 | 90.0 |
| Bench 3 | Bench | Mendy | DEF | 11 | 4.0 | 3.72 | 10.83 | 17.51 | 8.00 | 71.0 | 70.0 |
| Bench 4 | Bench | Virgil | DEF | 14 | 6.5 | 3.65 | 10.63 | 17.41 | 6.00 | 75.4 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.36 | 16.41 | 26.95 | 1.00 | 92.5 | 90.0 |
| Vice Captain | XI | Wissa | FWD | 17 | 6.1 | 6.04 | 14.79 | 22.37 | 1.00 | 107.7 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 4 | 8.0 | 4.25 | 12.03 | 19.69 | 2.00 | 67.0 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 7.40 | 22.25 | 37.13 | 2.00 | 111.7 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.94 | 15.85 | 24.86 | 0.00 | 91.9 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.96 | 14.60 | 23.99 | 3.00 | 83.9 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 4.55 | 14.32 | 23.60 | 1.00 | 80.1 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.27 | 13.79 | 23.11 | 6.00 | 74.5 | 86.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: Palmer
- Effective captain: Rogers
- Chip used: triple_captain
- Predicted score: 72.60
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (9.25).
- Transfer: Guéhi -> Tarkowski (projected gain 0.87, hit 0)
- Chip used: Triple Captain on Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (7.84) beats the best remaining Triple Captain opportunity (9.25).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.59 | 12.96 | 20.66 | 14.00 | 97.1 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 2.82 | 9.08 | 15.07 | 2.00 | 79.8 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 5.39 | 14.63 | 22.91 | 6.00 | 89.0 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 6.0 | 4.02 | 11.83 | 19.17 | 8.00 | 86.0 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.97 | 11.16 | 18.20 | 8.00 | 81.7 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.70 | 11.04 | 17.74 | 1.00 | 73.7 | 58.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 3.41 | 10.50 | 17.01 | 2.00 | 83.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 7.02 | 18.92 | 29.96 | 12.00 | 110.9 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 7.9 | 3.48 | 10.58 | 17.70 | 1.00 | 61.6 | 90.0 |
| Bench 3 | Bench | Wissa | FWD | 17 | 6.1 | 3.09 | 9.08 | 14.34 | 2.00 | 57.8 | 90.0 |
| Captain | Captain | Rogers | MID | 6 | 7.5 | 7.84 | 19.99 | 31.12 | 8.00 | 125.9 | 90.0 |
| Vice Captain | XI | Palmer | MID | 6 | 9.6 | 7.13 | 18.53 | 29.08 | 5.00 | 111.9 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.12 | 17.11 | 29.48 | 2.00 | 74.7 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.66 | 13.63 | 22.55 | 3.00 | 77.9 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.46 | 8.64 | 14.69 | 4.00 | 36.4 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Rogers
- Effective captain: B.Fernandes
- Chip used: bench_boost
- Predicted score: 66.67
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.73) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Groß (projected gain 3.72, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.73) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.45 | 12.92 | 20.81 | 1.00 | 95.0 | 90.0 |
| Bench 1 | Bench Boost | Tzolakis | GK | 11 | 4.5 | 3.06 | 9.17 | 14.98 | 6.00 | 82.0 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.60 | 13.30 | 21.31 | 1.00 | 82.3 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 6.0 | 4.57 | 12.53 | 20.32 | 14.00 | 90.6 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.92 | 11.61 | 18.92 | 8.00 | 85.1 | 90.0 |
| Bench 2 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.39 | 9.71 | 16.20 | 1.00 | 78.4 | 77.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 2.02 | 6.75 | 13.15 | 0.00 | 46.0 | 0.0 |
| XI | XI | João Pedro | FWD | 6 | 7.7 | 3.78 | 12.62 | 23.23 | 0.00 | 65.3 | 0.0 |
| Bench 3 | Bench Boost | Thiago | FWD | 4 | 7.8 | 3.26 | 9.99 | 16.95 | 5.00 | 63.1 | 90.0 |
| XI | XI | Wissa | FWD | 17 | 6.1 | 3.49 | 9.74 | 15.83 | 0.00 | 65.7 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.14 | 18.63 | 31.47 | 2.00 | 92.7 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.6 | 5.32 | 15.80 | 25.05 | 2.00 | 83.6 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.73 | 13.41 | 21.82 | 14.00 | 91.7 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.6 | 3.97 | 12.70 | 21.11 | 2.00 | 60.5 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.83 | 12.27 | 20.87 | 2.00 | 70.5 | 80.0 |