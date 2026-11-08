# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 214.36
- Total actual points: 209.00
- Average predicted points: 53.59
- Average actual points: 52.25
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: João Pedro
- Vice captain: B.Fernandes
- Effective captain: João Pedro
- Chip used: none
- Predicted score: 54.32
- Actual score: 68.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.49 | 10.96 | 16.75 | 6.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Kelleher | GK | 4 | 5.0 | 2.60 | 8.52 | 14.46 | 2.00 | 88.7 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 4.12 | 11.84 | 18.46 | 1.00 | 83.6 | 58.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 4.05 | 11.71 | 18.32 | 1.00 | 92.6 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.68 | 11.48 | 18.48 | 2.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Egan | DEF | 11 | 4.0 | 3.45 | 11.00 | 17.86 | 9.00 | 95.0 | 90.0 |
| Bench 2 | Bench | Lacroix | DEF | 6 | 6.0 | 3.49 | 10.57 | 16.79 | 1.00 | 88.3 | 90.0 |
| Captain | Captain | João Pedro | FWD | 6 | 7.6 | 5.57 | 15.41 | 24.14 | 9.00 | 101.6 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 4.26 | 12.30 | 19.57 | 2.00 | 85.3 | 90.0 |
| Bench 4 | Bench | Gonzalo | FWD | 10 | 6.0 | 3.37 | 10.16 | 16.64 | 2.00 | 88.2 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 5.47 | 16.86 | 27.22 | 23.00 | 100.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.96 | 15.54 | 24.48 | 4.00 | 104.2 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.81 | 13.69 | 22.17 | 4.00 | 87.7 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 4.52 | 13.55 | 21.46 | 7.00 | 87.8 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 3.82 | 11.98 | 18.90 | 0.00 | 78.1 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Wissa
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 51.53
- Actual score: 35.00
- Transfer: Gonzalo -> Wissa (projected gain 4.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.19 | 10.33 | 15.96 | 3.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Kelleher | GK | 4 | 5.0 | 3.09 | 8.25 | 13.01 | 2.00 | 88.9 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.08 | 12.35 | 19.59 | 6.00 | 102.3 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.21 | 9.62 | 15.82 | 8.00 | 77.8 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 2.85 | 9.13 | 15.11 | 6.00 | 80.4 | 90.0 |
| Bench 3 | Bench | Lacroix | DEF | 6 | 6.0 | 2.36 | 7.98 | 13.29 | 2.00 | 79.1 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 2.72 | 7.93 | 12.91 | 8.00 | 78.0 | 70.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.46 | 14.81 | 23.95 | 1.00 | 91.5 | 90.0 |
| Vice Captain | XI | Wissa | FWD | 17 | 6.1 | 5.44 | 13.19 | 19.67 | 1.00 | 112.7 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 3.45 | 10.63 | 17.39 | 2.00 | 56.0 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.20 | 19.65 | 31.93 | 2.00 | 108.7 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.94 | 14.15 | 21.76 | 0.00 | 95.9 | 45.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 3.55 | 13.12 | 21.10 | 1.00 | 81.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.96 | 12.70 | 20.59 | 3.00 | 82.9 | 90.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 1.01 | 5.49 | 10.17 | 5.00 | 35.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Palmer
- Vice captain: João Pedro
- Effective captain: Palmer
- Chip used: triple_captain
- Predicted score: 55.75
- Actual score: 67.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.13) beats the best remaining Triple Captain opportunity (7.24).
- Transfer: Tzolis -> Scott (projected gain 2.62, hit 0)
- Chip used: Triple Captain on Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (6.13) beats the best remaining Triple Captain opportunity (7.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.09 | 11.86 | 18.46 | 14.00 | 99.1 | 90.0 |
| Bench 1 | Bench | Kelleher | GK | 4 | 5.0 | 2.23 | 6.88 | 11.06 | 3.00 | 78.8 | 90.0 |
| XI | XI | Lacroix | DEF | 6 | 6.0 | 3.42 | 9.90 | 15.53 | 1.00 | 87.1 | 4.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.47 | 9.56 | 15.60 | 8.00 | 84.7 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 2.91 | 9.56 | 16.07 | 6.00 | 79.2 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 2.70 | 8.14 | 13.14 | 1.00 | 78.7 | 58.0 |
| Bench 3 | Bench | Egan | DEF | 11 | 4.0 | 2.41 | 8.00 | 12.51 | 2.00 | 83.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 6.12 | 17.22 | 26.86 | 12.00 | 112.9 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 7.9 | 2.98 | 9.58 | 15.70 | 1.00 | 70.6 | 90.0 |
| Bench 2 | Bench | Wissa | FWD | 17 | 6.1 | 2.49 | 7.78 | 11.44 | 2.00 | 64.8 | 90.0 |
| Captain | Captain | Palmer | MID | 6 | 9.6 | 6.13 | 16.03 | 24.88 | 5.00 | 114.9 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 3.92 | 15.61 | 26.98 | 2.00 | 75.7 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.76 | 11.83 | 19.45 | 3.00 | 79.9 | 90.0 |
| XI | XI | Scott | MID | 3 | 6.1 | 3.99 | 11.13 | 17.80 | 4.00 | 91.9 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 1.86 | 7.04 | 11.29 | 4.00 | 26.4 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.50 -> 0.80
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Gvardiol
- Effective captain: B.Fernandes
- Chip used: bench_boost
- Predicted score: 52.76
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.20) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Lacroix -> Gvardiol (projected gain 3.22, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.20) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.75 | 11.12 | 17.01 | 1.00 | 94.0 | 90.0 |
| Bench 1 | Bench Boost | Kelleher | GK | 4 | 5.0 | 2.22 | 6.61 | 10.79 | 6.00 | 80.6 | 90.0 |
| Vice Captain | XI | Gvardiol | DEF | 15 | 5.7 | 4.37 | 12.04 | 18.95 | 4.00 | 99.2 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.32 | 10.41 | 16.92 | 8.00 | 86.1 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.12 | 9.32 | 14.77 | 4.00 | 87.8 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 2.89 | 8.51 | 14.20 | 1.00 | 81.4 | 77.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.62 | 5.65 | 11.05 | 0.00 | 55.0 | 0.0 |
| XI | XI | João Pedro | FWD | 6 | 7.7 | 2.98 | 10.92 | 19.73 | 0.00 | 66.3 | 0.0 |
| XI | XI | Thiago | FWD | 4 | 7.8 | 2.96 | 8.99 | 14.75 | 5.00 | 64.1 | 90.0 |
| XI | XI | Wissa | FWD | 17 | 6.1 | 2.99 | 8.64 | 13.23 | 0.00 | 72.7 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 5.14 | 16.13 | 27.07 | 2.00 | 95.7 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.6 | 3.77 | 11.10 | 17.41 | 2.00 | 64.5 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.13 | 10.87 | 18.37 | 2.00 | 73.5 | 80.0 |
| Bench 2 | Bench Boost | Scott | MID | 3 | 6.1 | 2.69 | 8.87 | 14.39 | 2.00 | 71.2 | 90.0 |
| Bench 3 | Bench Boost | M.Sangaré | MID | 4 | 5.6 | 2.66 | 8.37 | 13.73 | 0.00 | 67.8 | 21.0 |