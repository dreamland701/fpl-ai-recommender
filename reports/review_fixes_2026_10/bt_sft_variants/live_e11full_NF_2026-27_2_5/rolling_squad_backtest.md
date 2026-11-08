# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 212.86
- Total actual points: 211.00
- Average predicted points: 53.22
- Average actual points: 52.75
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
- Bank: 100.00 -> 0.80
- Free transfers: 1 -> 2
- Captain: João Pedro
- Vice captain: B.Fernandes
- Effective captain: João Pedro
- Chip used: none
- Predicted score: 53.29
- Actual score: 68.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.77 | 11.26 | 17.01 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.29 | 8.47 | 13.63 | 10.00 | 82.7 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 4.79 | 12.29 | 18.64 | 1.00 | 74.3 | 58.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.88 | 11.44 | 17.96 | 1.00 | 90.0 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.79 | 11.39 | 18.26 | 2.00 | 89.3 | 90.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 3.70 | 11.11 | 17.77 | 9.00 | 88.5 | 90.0 |
| Bench 4 | Bench | Lacroix | DEF | 6 | 6.0 | 3.43 | 10.71 | 17.11 | 1.00 | 92.8 | 90.0 |
| Captain | Captain | João Pedro | FWD | 6 | 7.6 | 5.32 | 15.51 | 24.47 | 9.00 | 105.4 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 3.71 | 11.85 | 19.04 | 2.00 | 78.7 | 90.0 |
| Bench 3 | Bench | Gonzalo | FWD | 10 | 6.0 | 3.59 | 10.40 | 16.93 | 2.00 | 90.2 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 5.24 | 16.49 | 26.70 | 23.00 | 96.4 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.71 | 15.24 | 24.08 | 4.00 | 100.3 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 4.47 | 13.86 | 22.04 | 7.00 | 93.8 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.93 | 12.78 | 21.27 | 4.00 | 89.5 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 4.35 | 12.37 | 19.19 | 0.00 | 76.2 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Wissa
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 50.33
- Actual score: 38.00
- Transfer: Gonzalo -> Wissa (projected gain 4.10, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 6.0 | 3.35 | 10.55 | 16.20 | 3.00 | 84.1 | 90.0 |
| XI | XI | Tzolakis | GK | 11 | 4.5 | 3.59 | 9.62 | 15.35 | 6.00 | 90.8 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.14 | 12.19 | 19.19 | 6.00 | 95.3 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.27 | 9.57 | 15.68 | 8.00 | 76.5 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.11 | 9.47 | 15.52 | 6.00 | 82.5 | 90.0 |
| Bench 3 | Bench | Lacroix | DEF | 6 | 6.0 | 2.23 | 7.91 | 13.27 | 2.00 | 81.0 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 2.79 | 7.76 | 12.50 | 8.00 | 71.4 | 70.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.00 | 14.68 | 23.98 | 1.00 | 92.0 | 90.0 |
| Vice Captain | XI | Wissa | FWD | 17 | 6.1 | 5.36 | 13.07 | 19.51 | 1.00 | 111.8 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 3.19 | 10.30 | 16.94 | 2.00 | 51.6 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 5.68 | 19.33 | 31.64 | 2.00 | 105.9 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.64 | 13.76 | 21.28 | 0.00 | 94.1 | 45.0 |
| XI | XI | Palmer | MID | 6 | 9.5 | 3.26 | 13.08 | 21.21 | 1.00 | 82.9 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.40 | 13.05 | 20.96 | 3.00 | 86.0 | 90.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 1.17 | 5.69 | 10.41 | 5.00 | 36.7 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.70 -> 0.40
- Free transfers: 2 -> 2
- Captain: Palmer
- Vice captain: João Pedro
- Effective captain: Palmer
- Chip used: triple_captain
- Predicted score: 55.30
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.84) beats the best remaining Triple Captain opportunity (6.89).
- Transfer: Tzolis -> Ødegaard (projected gain 4.56, hit 0)
- Chip used: Triple Captain on Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (5.84) beats the best remaining Triple Captain opportunity (6.89).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.93 | 11.57 | 18.11 | 14.00 | 97.0 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 2.68 | 7.97 | 13.15 | 2.00 | 79.3 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.13 | 9.85 | 16.39 | 6.00 | 81.1 | 90.0 |
| XI | XI | Lacroix | DEF | 6 | 6.0 | 3.30 | 9.79 | 15.43 | 1.00 | 88.0 | 4.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.62 | 9.79 | 15.86 | 8.00 | 85.8 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 2.92 | 8.33 | 13.28 | 1.00 | 76.7 | 58.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 2.61 | 8.18 | 12.64 | 2.00 | 81.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 5.72 | 17.02 | 26.75 | 12.00 | 113.2 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 7.9 | 3.01 | 9.53 | 15.61 | 1.00 | 70.1 | 90.0 |
| Bench 3 | Bench | Wissa | FWD | 17 | 6.1 | 2.39 | 7.76 | 11.43 | 2.00 | 64.4 | 90.0 |
| Captain | Captain | Palmer | MID | 6 | 9.6 | 5.84 | 15.92 | 24.85 | 5.00 | 116.2 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 3.69 | 15.59 | 27.04 | 2.00 | 76.6 | 90.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 4.46 | 12.73 | 19.96 | 3.00 | 95.6 | 84.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.02 | 12.06 | 19.67 | 3.00 | 81.4 | 90.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 1.92 | 7.09 | 11.33 | 4.00 | 26.2 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Gvardiol
- Effective captain: B.Fernandes
- Chip used: bench_boost
- Predicted score: 53.94
- Actual score: 39.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Lacroix -> Gvardiol (projected gain 2.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.81 | 11.32 | 17.31 | 1.00 | 95.8 | 90.0 |
| Bench 1 | Bench Boost | Tzolakis | GK | 11 | 4.5 | 2.75 | 8.05 | 12.63 | 6.00 | 82.7 | 90.0 |
| Vice Captain | XI | Gvardiol | DEF | 15 | 5.7 | 4.22 | 11.78 | 18.61 | 4.00 | 97.8 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.34 | 10.40 | 16.87 | 8.00 | 85.3 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 2.96 | 9.04 | 14.40 | 4.00 | 85.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 2.95 | 8.55 | 14.16 | 1.00 | 79.8 | 77.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.68 | 5.48 | 10.94 | 0.00 | 53.4 | 0.0 |
| XI | XI | João Pedro | FWD | 6 | 7.7 | 2.93 | 10.95 | 20.03 | 0.00 | 67.9 | 0.0 |
| XI | XI | Thiago | FWD | 4 | 7.8 | 3.20 | 9.25 | 15.07 | 5.00 | 67.5 | 90.0 |
| Bench 3 | Bench Boost | Wissa | FWD | 17 | 6.1 | 2.82 | 8.62 | 13.23 | 0.00 | 72.3 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 5.30 | 16.08 | 26.94 | 2.00 | 95.8 | 90.0 |
| XI | XI | Palmer | MID | 6 | 9.6 | 3.78 | 11.37 | 17.80 | 2.00 | 67.1 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.20 | 10.87 | 18.32 | 2.00 | 73.2 | 80.0 |
| Bench 2 | Bench Boost | Ødegaard | MID | 1 | 6.7 | 2.84 | 9.52 | 15.39 | 2.00 | 66.6 | 72.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 2.87 | 8.62 | 13.96 | 0.00 | 69.6 | 21.0 |