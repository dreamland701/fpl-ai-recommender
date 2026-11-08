# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW4
- Total predicted points: 199.89
- Total actual points: 229.00
- Average predicted points: 66.63
- Average actual points: 76.33
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 64.12
- Actual score: 92.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.67 | 11.22 | 18.42 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Kelleher | GK | 4 | 5.0 | 3.02 | 9.13 | 15.10 | 2.00 | 84.9 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 6.09 | 17.73 | 29.16 | 1.00 | 86.0 | 58.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 5.28 | 15.55 | 25.82 | 6.00 | 81.2 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.68 | 13.22 | 21.37 | 9.00 | 97.7 | 90.0 |
| Bench 2 | Bench | Guéhi | DEF | 15 | 6.0 | 4.18 | 12.26 | 20.19 | 2.00 | 82.1 | 90.0 |
| XI | XI | Shaw | DEF | 16 | 4.5 | 4.22 | 11.84 | 19.31 | 2.00 | 86.9 | 72.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 6.43 | 18.92 | 31.12 | 13.00 | 78.1 | 90.0 |
| Bench 3 | Bench | Calvert-Lewin | FWD | 13 | 6.0 | 4.17 | 12.52 | 20.72 | 8.00 | 80.2 | 90.0 |
| Bench 4 | Bench | Gonzalo | FWD | 10 | 6.0 | 4.08 | 11.83 | 19.25 | 2.00 | 87.5 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.19 | 17.85 | 29.41 | 23.00 | 90.4 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.5 | 5.79 | 17.14 | 28.30 | 4.00 | 84.9 | 90.0 |
| XI | XI | Mbeumo | MID | 16 | 8.0 | 5.48 | 15.15 | 24.44 | 11.00 | 83.2 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.25 | 15.14 | 24.84 | 4.00 | 95.5 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 4.62 | 13.86 | 22.65 | 0.00 | 74.2 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Haaland
- Effective captain: B.Fernandes
- Chip used: triple_captain
- Predicted score: 67.04
- Actual score: 52.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.65) beats the best remaining Triple Captain opportunity (7.54).
- Transfer: Tzolis -> Ndiaye (projected gain 0.34, hit 0)
- Chip used: Triple Captain on B.Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.65) beats the best remaining Triple Captain opportunity (7.54).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.84 | 11.92 | 19.17 | 3.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Kelleher | GK | 4 | 5.0 | 3.22 | 9.20 | 14.92 | 2.00 | 80.8 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 4.41 | 13.15 | 21.57 | 5.00 | 85.8 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.46 | 12.89 | 20.84 | 6.00 | 93.6 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.15 | 12.06 | 19.44 | 8.00 | 80.1 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.93 | 11.91 | 19.39 | 8.00 | 71.6 | 70.0 |
| Bench 4 | Bench | Shaw | DEF | 16 | 4.5 | 3.20 | 9.45 | 15.58 | 4.00 | 72.5 | 90.0 |
| Vice Captain | XI | Haaland | FWD | 15 | 15.5 | 6.35 | 18.86 | 30.60 | 9.00 | 80.1 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 3.93 | 11.93 | 19.70 | 1.00 | 79.0 | 72.0 |
| Bench 3 | Bench | Gonzalo | FWD | 10 | 6.0 | 3.59 | 10.35 | 16.71 | 2.00 | 78.5 | 90.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.65 | 20.17 | 33.44 | 2.00 | 99.3 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.33 | 15.56 | 25.04 | 3.00 | 90.6 | 90.0 |
| XI | XI | Mbeumo | MID | 16 | 8.0 | 5.09 | 14.99 | 24.60 | 8.00 | 81.7 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.09 | 14.40 | 23.01 | 0.00 | 77.9 | 45.0 |
| XI | XI | Ndiaye | MID | 15 | 6.0 | 4.44 | 12.20 | 19.44 | 3.00 | 77.8 | 86.0 |

## GW4

- Train rows: 192914
- Bank: 0.50 -> 1.00
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 68.73
- Actual score: 85.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Ndiaye -> Groß (projected gain 0.69, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.97 | 11.96 | 19.56 | 14.00 | 84.9 | 90.0 |
| Bench 1 | Bench Boost | Kelleher | GK | 4 | 5.0 | 2.88 | 8.83 | 14.47 | 3.00 | 80.8 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.85 | 12.10 | 19.45 | 1.00 | 80.1 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.92 | 12.05 | 19.66 | 1.00 | 74.8 | 58.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.88 | 11.92 | 19.29 | 2.00 | 88.6 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.70 | 11.42 | 18.95 | 6.00 | 82.3 | 90.0 |
| Bench 4 | Bench Boost | Shaw | DEF | 16 | 4.5 | 3.16 | 9.37 | 15.62 | 0.00 | 78.2 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 6.50 | 20.08 | 32.73 | 9.00 | 82.6 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 3.86 | 11.08 | 18.43 | 10.00 | 67.1 | 77.0 |
| Bench 3 | Bench Boost | Gonzalo | FWD | 10 | 6.0 | 3.41 | 10.19 | 16.59 | 2.00 | 77.5 | 76.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 5.93 | 18.34 | 30.55 | 2.00 | 86.8 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.20 | 15.01 | 24.51 | 3.00 | 86.4 | 90.0 |
| XI | XI | Mbeumo | MID | 16 | 8.0 | 4.23 | 12.83 | 21.80 | 2.00 | 74.9 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.5 | 4.09 | 12.03 | 19.64 | 17.00 | 78.6 | 90.0 |
| Bench 2 | Bench Boost | M.Sangaré | MID | 4 | 5.7 | 3.65 | 11.36 | 18.45 | 4.00 | 55.5 | 90.0 |