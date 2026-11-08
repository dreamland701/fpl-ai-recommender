# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 260.20
- Total actual points: 268.00
- Average predicted points: 65.05
- Average actual points: 67.00
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
- Bank: 100.00 -> 2.10
- Free transfers: 1 -> 2
- Captain: B.Fernandes
- Vice captain: João Pedro
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 63.20
- Actual score: 95.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.46 | 11.05 | 17.63 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.76 | 9.47 | 15.05 | 10.00 | 84.7 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 5.77 | 13.91 | 20.38 | 1.00 | 48.3 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.83 | 12.32 | 18.26 | 2.00 | 90.3 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.77 | 11.68 | 18.94 | 0.00 | 58.4 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.72 | 11.58 | 18.76 | 11.00 | 90.1 | 90.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 4.64 | 11.49 | 17.80 | 9.00 | 89.5 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 6.02 | 15.29 | 23.87 | 9.00 | 104.4 | 90.0 |
| Bench 4 | Bench | Thiago | FWD | 4 | 8.0 | 4.21 | 12.09 | 19.93 | 2.00 | 50.7 | 90.0 |
| Bench 3 | Bench | Gonzalo | FWD | 10 | 6.0 | 4.37 | 11.12 | 17.62 | 2.00 | 89.2 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.03 | 16.56 | 25.85 | 23.00 | 75.4 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.62 | 15.17 | 23.04 | 4.00 | 100.3 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.95 | 14.06 | 22.34 | 4.00 | 90.5 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 5.24 | 13.04 | 20.82 | 7.00 | 92.8 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.76 | 12.66 | 20.31 | 5.00 | 87.0 | 90.0 |

## GW3

- Train rows: 192260
- Bank: 2.10 -> 2.00
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Wissa
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 61.32
- Actual score: 36.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Gonzalo -> Wissa (projected gain 2.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 6.0 | 3.87 | 10.64 | 17.06 | 3.00 | 86.1 | 90.0 |
| XI | XI | Tzolakis | GK | 11 | 4.5 | 4.13 | 10.61 | 16.62 | 6.00 | 89.8 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.6 | 4.85 | 12.53 | 19.17 | 2.00 | 91.9 | 66.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.82 | 12.32 | 18.31 | 6.00 | 94.3 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 5.09 | 12.27 | 17.76 | 4.00 | 92.7 | 76.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.13 | 11.28 | 17.18 | 8.00 | 80.5 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 3.91 | 10.16 | 15.85 | 8.00 | 73.4 | 70.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.52 | 14.28 | 21.93 | 1.00 | 92.0 | 90.0 |
| Vice Captain | XI | Wissa | FWD | 17 | 6.1 | 5.53 | 13.22 | 18.59 | 1.00 | 95.8 | 90.0 |
| Bench 2 | Bench | Thiago | FWD | 4 | 8.0 | 4.05 | 10.95 | 17.65 | 2.00 | 61.6 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.68 | 19.48 | 31.53 | 2.00 | 98.9 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.41 | 13.80 | 21.45 | 0.00 | 89.1 | 45.0 |
| Bench 3 | Bench | Rogers | MID | 6 | 7.5 | 3.94 | 13.45 | 22.08 | 6.00 | 79.7 | 86.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.23 | 13.44 | 19.88 | 3.00 | 88.0 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 4.24 | 13.30 | 20.62 | 1.00 | 84.9 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 2.00 -> 0.80
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: Palmer
- Effective captain: Rogers
- Chip used: triple_captain
- Predicted score: 70.37
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.03) beats the best remaining Triple Captain opportunity (8.30).
- Transfer: Thiago -> Isak (projected gain 3.52, hit 0)
- Chip used: Triple Captain on Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (7.03) beats the best remaining Triple Captain opportunity (8.30).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.36 | 12.12 | 19.14 | 14.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.06 | 9.18 | 14.11 | 2.00 | 82.3 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.88 | 12.77 | 19.75 | 6.00 | 67.0 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.62 | 10.83 | 17.31 | 6.00 | 83.1 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.88 | 10.28 | 14.99 | 1.00 | 51.7 | 58.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 3.62 | 10.06 | 16.02 | 2.00 | 84.0 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 4.22 | 9.81 | 15.86 | 11.00 | 76.2 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 6.25 | 16.74 | 24.99 | 12.00 | 103.2 | 90.0 |
| XI | XI | Isak | FWD | 14 | 9.1 | 5.67 | 13.58 | 21.18 | 2.00 | 88.3 | 90.0 |
| Bench 3 | Bench | Wissa | FWD | 17 | 6.1 | 3.15 | 8.99 | 13.34 | 2.00 | 68.4 | 90.0 |
| Captain | Captain | Rogers | MID | 6 | 7.5 | 7.03 | 17.71 | 25.74 | 8.00 | 113.9 | 90.0 |
| Vice Captain | XI | Palmer | MID | 6 | 9.6 | 6.63 | 16.40 | 23.85 | 5.00 | 105.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 4.89 | 14.78 | 24.31 | 2.00 | 55.6 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.89 | 11.97 | 18.62 | 3.00 | 83.4 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.52 | 8.69 | 14.73 | 4.00 | 36.2 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Rogers
- Effective captain: B.Fernandes
- Chip used: bench_boost
- Predicted score: 65.30
- Actual score: 51.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.50) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: M.Sangaré -> Groß (projected gain 2.84, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.50) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.41 | 11.45 | 16.46 | 1.00 | 94.8 | 90.0 |
| Bench 1 | Bench Boost | Tzolakis | GK | 11 | 4.5 | 3.06 | 8.95 | 13.78 | 6.00 | 83.7 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.56 | 12.31 | 18.56 | 1.00 | 85.4 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.09 | 11.34 | 17.71 | 4.00 | 86.6 | 90.0 |
| Bench 3 | Bench Boost | De Cuyper | DEF | 5 | 4.7 | 2.88 | 9.80 | 15.74 | 6.00 | 76.1 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.54 | 9.69 | 15.44 | 1.00 | 81.8 | 77.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 2.08 | 6.58 | 13.04 | 0.00 | 44.4 | 0.0 |
| XI | XI | João Pedro | FWD | 6 | 7.7 | 3.87 | 12.11 | 22.22 | 0.00 | 54.9 | 0.0 |
| XI | XI | Isak | FWD | 14 | 9.1 | 3.70 | 10.69 | 17.24 | 8.00 | 65.4 | 80.0 |
| Bench 2 | Bench Boost | Wissa | FWD | 17 | 6.1 | 3.49 | 9.58 | 14.88 | 0.00 | 73.3 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.09 | 16.28 | 25.99 | 2.00 | 91.8 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.6 | 5.08 | 14.27 | 21.07 | 2.00 | 65.7 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.34 | 12.88 | 20.60 | 14.00 | 92.6 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.6 | 4.07 | 12.07 | 20.35 | 2.00 | 62.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.96 | 11.49 | 19.13 | 2.00 | 77.2 | 80.0 |