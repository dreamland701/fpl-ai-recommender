# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 258.29
- Total actual points: 256.00
- Average predicted points: 64.57
- Average actual points: 64.00
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
- Captain: B.Fernandes
- Vice captain: João Pedro
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 63.11
- Actual score: 96.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.52 | 12.32 | 19.57 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.72 | 9.68 | 15.03 | 10.00 | 84.7 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.69 | 14.52 | 22.19 | 1.00 | 76.3 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.73 | 12.47 | 20.39 | 2.00 | 91.3 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.63 | 12.25 | 20.15 | 11.00 | 91.1 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 4.83 | 12.00 | 19.60 | 1.00 | 89.0 | 90.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 4.54 | 11.40 | 17.11 | 9.00 | 89.5 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 5.96 | 15.51 | 23.72 | 9.00 | 104.4 | 90.0 |
| Bench 4 | Bench | Thiago | FWD | 4 | 8.0 | 3.97 | 12.16 | 19.42 | 2.00 | 77.7 | 90.0 |
| Bench 3 | Bench | Gonzalo | FWD | 10 | 6.0 | 4.42 | 11.28 | 17.51 | 2.00 | 89.2 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 5.97 | 17.33 | 25.75 | 23.00 | 93.4 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.73 | 15.88 | 24.00 | 4.00 | 100.3 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.90 | 14.49 | 24.04 | 4.00 | 90.5 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 5.27 | 14.39 | 23.56 | 7.00 | 92.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.90 | 13.91 | 22.65 | 5.00 | 87.0 | 90.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Wissa
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 60.73
- Actual score: 38.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Gonzalo -> Wissa (projected gain 2.62, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 6.0 | 4.04 | 10.98 | 17.33 | 3.00 | 86.1 | 90.0 |
| XI | XI | Tzolakis | GK | 11 | 4.5 | 4.47 | 10.53 | 16.82 | 6.00 | 89.8 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.88 | 12.71 | 20.20 | 2.00 | 91.9 | 66.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.78 | 12.24 | 18.68 | 6.00 | 94.3 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 4.13 | 10.53 | 16.67 | 6.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Mendy | DEF | 11 | 4.0 | 3.86 | 10.43 | 16.00 | 8.00 | 73.4 | 70.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.13 | 10.02 | 14.89 | 8.00 | 80.5 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.61 | 14.45 | 21.77 | 1.00 | 92.0 | 90.0 |
| Vice Captain | XI | Wissa | FWD | 17 | 6.1 | 5.65 | 13.68 | 20.56 | 1.00 | 96.8 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 4 | 8.0 | 3.88 | 11.07 | 17.96 | 2.00 | 72.6 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.55 | 19.72 | 31.56 | 2.00 | 98.9 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.30 | 14.33 | 22.62 | 3.00 | 88.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.26 | 14.09 | 22.10 | 0.00 | 90.1 | 45.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 4.41 | 13.41 | 22.12 | 1.00 | 84.9 | 90.0 |
| Bench 4 | Bench | Rogers | MID | 6 | 7.5 | 3.73 | 12.66 | 21.81 | 6.00 | 79.7 | 86.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: Palmer
- Effective captain: Rogers
- Chip used: triple_captain
- Predicted score: 67.64
- Actual score: 78.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.17) beats the best remaining Triple Captain opportunity (8.46).
- Transfer: Virgil -> Tarkowski (projected gain 1.31, hit 0)
- Chip used: Triple Captain on Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (7.17) beats the best remaining Triple Captain opportunity (8.46).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.44 | 12.28 | 19.38 | 14.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.19 | 9.13 | 14.30 | 2.00 | 82.3 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.60 | 12.97 | 20.00 | 6.00 | 88.0 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 6.0 | 3.90 | 11.11 | 17.74 | 8.00 | 85.4 | 90.0 |
| Bench 2 | Bench | Guéhi | DEF | 15 | 6.0 | 3.48 | 10.55 | 17.22 | 6.00 | 83.1 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.60 | 10.35 | 16.06 | 2.00 | 84.0 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.66 | 9.79 | 13.64 | 1.00 | 51.7 | 58.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.10 | 17.08 | 24.77 | 12.00 | 103.2 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 7.9 | 3.49 | 10.11 | 15.56 | 1.00 | 71.1 | 90.0 |
| Bench 3 | Bench | Wissa | FWD | 17 | 6.1 | 3.00 | 8.31 | 13.29 | 2.00 | 46.4 | 90.0 |
| Captain | Captain | Rogers | MID | 6 | 7.5 | 7.17 | 18.26 | 25.64 | 8.00 | 124.9 | 90.0 |
| Vice Captain | XI | Palmer | MID | 6 | 9.6 | 6.67 | 17.21 | 26.38 | 5.00 | 112.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 4.77 | 15.14 | 24.10 | 2.00 | 74.6 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.90 | 13.35 | 20.80 | 3.00 | 83.4 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.60 | 8.57 | 13.31 | 4.00 | 55.2 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Rogers
- Effective captain: B.Fernandes
- Chip used: bench_boost
- Predicted score: 66.82
- Actual score: 44.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.62) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Wissa -> Calvert-Lewin (projected gain 2.12, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.62) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.53 | 12.33 | 19.98 | 1.00 | 94.8 | 90.0 |
| Bench 1 | Bench Boost | Tzolakis | GK | 11 | 4.5 | 3.11 | 9.00 | 14.10 | 6.00 | 83.7 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.38 | 12.58 | 20.34 | 1.00 | 85.4 | 90.0 |
| XI | XI | Tarkowski | DEF | 9 | 6.0 | 4.60 | 11.54 | 18.76 | 14.00 | 90.5 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.17 | 9.94 | 15.02 | 4.00 | 86.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.46 | 9.46 | 15.01 | 1.00 | 81.8 | 77.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.70 | 5.15 | 9.23 | 0.00 | 28.4 | 0.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 5.10 | 12.14 | 18.63 | 2.00 | 86.6 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.7 | 3.57 | 11.92 | 22.05 | 0.00 | 74.9 | 0.0 |
| Bench 3 | Bench Boost | Thiago | FWD | 4 | 7.8 | 3.36 | 9.59 | 15.69 | 5.00 | 74.5 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.06 | 17.42 | 29.41 | 2.00 | 91.8 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.6 | 5.11 | 14.99 | 23.38 | 2.00 | 87.7 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.6 | 4.11 | 12.28 | 20.21 | 2.00 | 72.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.04 | 11.67 | 19.42 | 2.00 | 77.2 | 80.0 |
| Bench 2 | Bench Boost | M.Sangaré | MID | 4 | 5.6 | 3.46 | 10.03 | 16.12 | 0.00 | 72.6 | 21.0 |