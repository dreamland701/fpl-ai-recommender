# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 269.82
- Total actual points: 238.00
- Average predicted points: 67.45
- Average actual points: 59.50
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
- Bank: 100.00 -> 0.70
- Free transfers: 1 -> 2
- Captain: Mendy
- Vice captain: João Pedro
- Effective captain: Mendy
- Chip used: none
- Predicted score: 67.06
- Actual score: 63.00
- Chip advisory: bench_boost (0.65): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.57 | 12.76 | 20.41 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.81 | 10.30 | 16.87 | 10.00 | 84.7 | 90.0 |
| Captain | Captain | Mendy | DEF | 11 | 4.0 | 6.62 | 17.13 | 27.23 | 1.00 | 76.3 | 58.0 |
| XI | XI | Gabriel | DEF | 1 | 8.0 | 4.99 | 14.31 | 23.19 | 8.00 | 85.1 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.99 | 13.89 | 22.56 | 2.00 | 91.3 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 5.05 | 13.45 | 21.41 | 0.00 | 82.4 | 90.0 |
| Bench 2 | Bench | Virgil | DEF | 14 | 6.5 | 4.83 | 13.38 | 21.37 | 1.00 | 89.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 6.32 | 18.01 | 29.17 | 9.00 | 104.4 | 90.0 |
| Bench 3 | Bench | Thiago | FWD | 4 | 8.0 | 4.53 | 14.27 | 23.63 | 2.00 | 77.7 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 4.15 | 12.65 | 21.33 | 1.00 | 65.7 | 45.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 6.24 | 18.69 | 31.10 | 23.00 | 93.4 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.81 | 16.74 | 27.28 | 4.00 | 100.3 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.13 | 15.88 | 26.27 | 4.00 | 90.5 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.71 | 15.41 | 24.57 | 0.00 | 78.2 | 45.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 5.01 | 15.26 | 25.22 | 5.00 | 87.0 | 90.0 |

## GW3

- Train rows: 192260
- Bank: 0.70 -> 0.60
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Ajayi
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 62.41
- Actual score: 41.00
- Transfer: Mendy -> Ajayi (projected gain 2.05, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 6.0 | 4.03 | 11.80 | 19.21 | 3.00 | 86.1 | 90.0 |
| XI | XI | Tzolakis | GK | 11 | 4.5 | 4.09 | 11.02 | 17.75 | 6.00 | 89.8 | 90.0 |
| Vice Captain | XI | Ajayi | DEF | 11 | 4.1 | 5.79 | 14.20 | 22.09 | 5.00 | 122.7 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 8.0 | 4.37 | 13.67 | 22.81 | 2.00 | 78.2 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 5.26 | 13.55 | 20.72 | 4.00 | 92.7 | 76.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.36 | 12.40 | 20.34 | 8.00 | 80.5 | 90.0 |
| Bench 2 | Bench | Virgil | DEF | 14 | 6.5 | 4.13 | 11.60 | 18.86 | 6.00 | 81.5 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.90 | 16.28 | 26.98 | 1.00 | 92.0 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 4.62 | 13.55 | 22.29 | 2.00 | 72.6 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.98 | 9.76 | 16.68 | 2.00 | 27.0 | 65.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.88 | 21.93 | 36.84 | 2.00 | 98.9 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.64 | 15.46 | 24.38 | 0.00 | 90.1 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.46 | 15.11 | 24.61 | 3.00 | 88.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.14 | 14.75 | 24.92 | 6.00 | 79.7 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.20 | 9.08 | 16.25 | 5.00 | 16.7 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: João Pedro
- Effective captain: Rogers
- Chip used: triple_captain
- Predicted score: 70.46
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.42) beats the best remaining Triple Captain opportunity (8.76).
- Transfer: Tzolis -> Ødegaard (projected gain 5.03, hit 0)
- Chip used: Triple Captain on Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (7.42) beats the best remaining Triple Captain opportunity (8.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.43 | 12.67 | 20.31 | 14.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.25 | 9.91 | 16.23 | 2.00 | 82.3 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 8.0 | 4.71 | 14.02 | 23.02 | 9.00 | 83.9 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 4.47 | 12.03 | 18.82 | 11.00 | 76.2 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 4.25 | 11.76 | 19.06 | 8.00 | 62.8 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.90 | 11.75 | 19.53 | 6.00 | 83.1 | 90.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.1 | 3.83 | 9.64 | 17.00 | 1.00 | 87.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 6.62 | 18.72 | 29.85 | 12.00 | 103.2 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 7.9 | 4.08 | 12.24 | 20.47 | 1.00 | 71.1 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 3.34 | 9.65 | 16.06 | 12.00 | 63.2 | 62.0 |
| Captain | Captain | Rogers | MID | 6 | 7.5 | 7.42 | 19.82 | 31.04 | 8.00 | 124.9 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.24 | 18.31 | 31.65 | 2.00 | 74.6 | 90.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 5.36 | 14.63 | 23.36 | 3.00 | 90.6 | 84.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.14 | 14.49 | 23.80 | 3.00 | 83.4 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 3.53 | 12.17 | 20.62 | 4.00 | 55.2 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.30 -> 2.10
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Rogers
- Effective captain: B.Fernandes
- Chip used: bench_boost
- Predicted score: 69.88
- Actual score: 41.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.57) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Thiago -> Calvert-Lewin (projected gain 2.27, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.57) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.51 | 13.12 | 21.11 | 1.00 | 94.8 | 90.0 |
| Bench 1 | Bench Boost | Tzolakis | GK | 11 | 4.5 | 3.29 | 9.66 | 15.70 | 6.00 | 83.7 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 8.0 | 4.69 | 14.06 | 23.14 | 1.00 | 85.2 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.14 | 12.20 | 19.92 | 4.00 | 86.6 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 4.03 | 11.85 | 19.28 | 8.00 | 86.3 | 90.0 |
| Bench 3 | Bench Boost | De Cuyper | DEF | 5 | 4.7 | 3.12 | 11.20 | 18.58 | 6.00 | 76.1 | 90.0 |
| Bench 4 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 2.87 | 7.80 | 11.97 | 1.00 | 71.1 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.7 | 4.19 | 14.19 | 26.38 | 0.00 | 74.9 | 0.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 5.30 | 13.77 | 21.46 | 2.00 | 86.6 | 90.0 |
| Bench 2 | Bench Boost | Emersonn | FWD | 12 | 5.5 | 3.29 | 10.85 | 17.99 | 2.00 | 66.4 | 80.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.30 | 18.58 | 31.34 | 2.00 | 91.8 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.6 | 5.36 | 16.35 | 25.93 | 2.00 | 87.7 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.30 | 13.53 | 22.96 | 2.00 | 77.2 | 80.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 4.23 | 13.28 | 21.74 | 2.00 | 70.6 | 72.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.96 | 11.78 | 19.59 | 0.00 | 72.6 | 21.0 |