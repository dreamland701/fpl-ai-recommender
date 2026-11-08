# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 265.68
- Total actual points: 242.00
- Average predicted points: 66.42
- Average actual points: 60.50
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
- Predicted score: 65.36
- Actual score: 82.00
- Chip advisory: bench_boost (0.65): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.57 | 12.76 | 20.41 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.69 | 9.97 | 16.33 | 10.00 | 81.7 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.99 | 15.49 | 24.64 | 1.00 | 68.3 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.99 | 13.89 | 22.56 | 2.00 | 91.3 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.93 | 13.55 | 21.54 | 11.00 | 91.1 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 4.78 | 13.24 | 21.16 | 1.00 | 88.0 | 90.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 4.70 | 12.71 | 20.17 | 9.00 | 89.5 | 90.0 |
| Captain | Captain | João Pedro | FWD | 6 | 7.6 | 6.32 | 18.01 | 29.17 | 9.00 | 115.4 | 90.0 |
| Bench 4 | Bench | Thiago | FWD | 4 | 8.0 | 4.11 | 12.95 | 21.44 | 2.00 | 70.7 | 90.0 |
| Bench 3 | Bench | Gonzalo | FWD | 10 | 6.0 | 4.29 | 11.90 | 19.23 | 2.00 | 89.2 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.24 | 18.69 | 31.10 | 23.00 | 95.4 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.81 | 16.74 | 27.28 | 4.00 | 105.3 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.13 | 15.88 | 26.27 | 4.00 | 90.5 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 5.37 | 15.36 | 24.94 | 7.00 | 94.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.90 | 14.95 | 24.70 | 5.00 | 85.0 | 90.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Wissa
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 62.20
- Actual score: 34.00
- Chip advisory: bench_boost (0.60): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Gonzalo -> Wissa (projected gain 3.72, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 6.0 | 3.95 | 11.55 | 18.80 | 3.00 | 84.1 | 90.0 |
| XI | XI | Tzolakis | GK | 11 | 4.5 | 4.09 | 11.02 | 17.75 | 6.00 | 89.8 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 5.08 | 14.05 | 22.33 | 2.00 | 92.9 | 66.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 5.04 | 13.49 | 21.19 | 6.00 | 96.3 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.07 | 11.57 | 18.98 | 8.00 | 75.5 | 90.0 |
| Bench 2 | Bench | Virgil | DEF | 14 | 6.5 | 3.91 | 10.97 | 17.82 | 6.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 3.79 | 10.66 | 17.10 | 8.00 | 64.4 | 70.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.90 | 16.28 | 26.98 | 1.00 | 93.0 | 90.0 |
| Vice Captain | XI | Wissa | FWD | 17 | 6.1 | 5.96 | 14.67 | 22.21 | 1.00 | 106.8 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 3.99 | 11.70 | 19.24 | 2.00 | 62.6 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.88 | 21.93 | 36.84 | 2.00 | 108.9 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.64 | 15.46 | 24.38 | 0.00 | 90.1 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.40 | 14.95 | 24.36 | 3.00 | 87.0 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 4.26 | 14.28 | 23.71 | 1.00 | 81.9 | 90.0 |
| Bench 3 | Bench | Rogers | MID | 6 | 7.5 | 3.86 | 13.74 | 23.22 | 6.00 | 73.7 | 86.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: Palmer
- Effective captain: Rogers
- Chip used: triple_captain
- Predicted score: 70.78
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.42) beats the best remaining Triple Captain opportunity (8.76).
- Transfer: M.Sangaré -> Janelt (projected gain 0.40, hit 0)
- Chip used: Triple Captain on Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (7.42) beats the best remaining Triple Captain opportunity (8.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.43 | 12.67 | 20.31 | 14.00 | 95.0 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.08 | 9.37 | 15.35 | 2.00 | 78.3 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 5.20 | 14.35 | 22.59 | 6.00 | 87.0 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 4.12 | 11.39 | 18.46 | 8.00 | 82.8 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.73 | 11.25 | 18.69 | 6.00 | 80.1 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.92 | 11.23 | 17.88 | 1.00 | 71.7 | 58.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 3.61 | 10.68 | 17.14 | 2.00 | 81.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.62 | 18.72 | 29.85 | 12.00 | 111.2 | 90.0 |
| Bench 3 | Bench | Thiago | FWD | 4 | 7.9 | 3.51 | 10.53 | 17.61 | 1.00 | 61.1 | 90.0 |
| Bench 4 | Bench | Wissa | FWD | 17 | 6.1 | 2.99 | 9.06 | 14.33 | 2.00 | 57.4 | 90.0 |
| Captain | Captain | Rogers | MID | 6 | 7.5 | 7.42 | 19.82 | 31.04 | 8.00 | 125.9 | 90.0 |
| Vice Captain | XI | Palmer | MID | 6 | 9.6 | 6.84 | 18.42 | 29.05 | 5.00 | 113.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 4.89 | 17.09 | 29.54 | 2.00 | 75.6 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.92 | 13.86 | 22.77 | 3.00 | 79.4 | 90.0 |
| XI | XI | Janelt | MID | 4 | 5.0 | 3.85 | 11.02 | 17.81 | 4.00 | 84.4 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.70 -> 0.80
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Rogers
- Effective captain: B.Fernandes
- Chip used: bench_boost
- Predicted score: 67.33
- Actual score: 41.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.07) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Wissa -> Calvert-Lewin (projected gain 3.75, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.07) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.51 | 13.12 | 21.11 | 1.00 | 96.8 | 90.0 |
| Bench 1 | Bench Boost | Tzolakis | GK | 11 | 4.5 | 3.15 | 9.25 | 15.03 | 6.00 | 80.7 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.60 | 13.44 | 21.52 | 1.00 | 83.4 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.06 | 11.94 | 19.50 | 4.00 | 84.6 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.94 | 11.60 | 18.87 | 8.00 | 84.3 | 90.0 |
| Bench 2 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.45 | 9.75 | 16.16 | 1.00 | 76.8 | 77.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 2.08 | 6.58 | 13.04 | 0.00 | 44.4 | 0.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 5.19 | 13.48 | 21.01 | 2.00 | 84.6 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.7 | 3.73 | 12.65 | 23.53 | 0.00 | 66.9 | 0.0 |
| XI | XI | Thiago | FWD | 4 | 7.8 | 3.50 | 10.25 | 17.27 | 5.00 | 66.5 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.30 | 18.58 | 31.34 | 2.00 | 92.8 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.6 | 5.25 | 16.02 | 25.40 | 2.00 | 85.7 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.6 | 3.98 | 12.97 | 21.50 | 2.00 | 63.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.90 | 12.27 | 20.82 | 2.00 | 70.2 | 80.0 |
| Bench 3 | Bench Boost | Janelt | MID | 4 | 5.0 | 3.39 | 10.20 | 16.60 | 3.00 | 76.0 | 90.0 |