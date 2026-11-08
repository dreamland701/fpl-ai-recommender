# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW4
- Total predicted points: 166.17
- Total actual points: 231.00
- Average predicted points: 55.39
- Average actual points: 77.00
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
- Bank: 100.00 -> 0.50
- Free transfers: 1 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 52.72
- Actual score: 99.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 2.87 | 9.72 | 15.02 | 6.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Kelleher | GK | 4 | 5.0 | 2.42 | 8.13 | 13.90 | 2.00 | 84.9 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 4.89 | 14.53 | 23.16 | 1.00 | 92.0 | 58.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 4.08 | 13.25 | 21.82 | 6.00 | 87.2 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.68 | 11.62 | 18.97 | 9.00 | 96.7 | 90.0 |
| Bench 3 | Bench | Shaw | DEF | 16 | 4.5 | 3.62 | 10.44 | 17.01 | 2.00 | 85.9 | 72.0 |
| Bench 4 | Bench | O'Shea | DEF | 12 | 4.0 | 3.19 | 9.40 | 14.43 | 0.00 | 88.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 5.43 | 16.22 | 26.22 | 13.00 | 84.1 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.5 | 4.22 | 12.41 | 19.76 | 9.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Calvert-Lewin | FWD | 13 | 6.0 | 3.67 | 11.32 | 18.02 | 8.00 | 83.2 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 5.19 | 15.65 | 25.01 | 23.00 | 91.4 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.5 | 4.59 | 14.04 | 23.30 | 4.00 | 83.9 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.15 | 13.64 | 21.64 | 4.00 | 90.5 | 90.0 |
| XI | XI | Mbeumo | MID | 16 | 8.0 | 4.48 | 12.65 | 19.94 | 11.00 | 83.2 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 3.72 | 12.06 | 19.25 | 0.00 | 78.2 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Haaland
- Effective captain: B.Fernandes
- Chip used: triple_captain
- Predicted score: 55.35
- Actual score: 43.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.45) beats the best remaining Triple Captain opportunity (6.18).
- Transfer: O'Shea -> Davis (projected gain 0.41, hit 0)
- Chip used: Triple Captain on B.Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.45) beats the best remaining Triple Captain opportunity (6.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.24 | 10.92 | 16.57 | 3.00 | 84.4 | 90.0 |
| Bench 1 | Bench | Kelleher | GK | 4 | 5.0 | 2.82 | 7.90 | 12.52 | 2.00 | 82.8 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.56 | 11.59 | 18.84 | 6.00 | 92.6 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 3.51 | 11.45 | 18.37 | 5.00 | 86.8 | 90.0 |
| XI | XI | Davis | DEF | 12 | 4.0 | 3.20 | 9.39 | 14.84 | 1.00 | 91.7 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 2.93 | 9.01 | 14.79 | 8.00 | 78.6 | 70.0 |
| Bench 3 | Bench | Shaw | DEF | 16 | 4.5 | 2.90 | 8.45 | 13.18 | 4.00 | 79.5 | 90.0 |
| Vice Captain | XI | Haaland | FWD | 15 | 15.5 | 5.25 | 16.46 | 26.40 | 9.00 | 85.1 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.30 | 14.92 | 23.50 | 1.00 | 91.8 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 3.43 | 10.63 | 16.60 | 1.00 | 82.0 | 72.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 5.45 | 17.57 | 28.24 | 2.00 | 96.3 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.33 | 13.66 | 21.64 | 3.00 | 89.6 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.09 | 12.70 | 19.91 | 0.00 | 81.9 | 45.0 |
| XI | XI | Mbeumo | MID | 16 | 8.0 | 4.09 | 12.49 | 20.60 | 8.00 | 82.7 | 90.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.88 | 9.45 | 15.51 | 5.00 | 64.4 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: João Pedro
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 58.10
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.73) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: none
- No transfer was applied this week.
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.73) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.47 | 10.86 | 17.36 | 14.00 | 86.9 | 90.0 |
| Bench 1 | Bench Boost | Kelleher | GK | 4 | 5.0 | 2.58 | 7.83 | 12.47 | 3.00 | 83.8 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 2.85 | 9.70 | 15.25 | 1.00 | 82.1 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 2.88 | 9.42 | 14.79 | 2.00 | 88.6 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 2.92 | 9.15 | 15.06 | 1.00 | 79.8 | 58.0 |
| Bench 3 | Bench Boost | Shaw | DEF | 16 | 4.5 | 2.56 | 7.77 | 13.22 | 0.00 | 82.2 | 0.0 |
| Bench 4 | Bench Boost | Davis | DEF | 12 | 4.0 | 2.55 | 7.50 | 12.34 | 14.00 | 85.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 5.70 | 18.88 | 30.43 | 9.00 | 87.6 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.7 | 4.85 | 14.94 | 24.00 | 12.00 | 93.7 | 90.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 3.36 | 9.68 | 16.13 | 10.00 | 75.1 | 77.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 4.73 | 16.84 | 28.05 | 2.00 | 87.8 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.30 | 13.21 | 21.41 | 3.00 | 88.4 | 90.0 |
| XI | XI | Mbeumo | MID | 16 | 8.0 | 3.43 | 11.63 | 19.50 | 2.00 | 78.9 | 90.0 |
| Bench 2 | Bench Boost | M.Sangaré | MID | 4 | 5.7 | 3.05 | 9.76 | 15.05 | 4.00 | 45.5 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 3.17 | 9.72 | 15.46 | 3.00 | 74.8 | 80.0 |