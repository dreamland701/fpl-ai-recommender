# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 242.42
- Total actual points: 238.00
- Average predicted points: 60.60
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
- Predicted score: 60.03
- Actual score: 63.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.09 | 11.42 | 18.27 | 6.00 | 90.3 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 3.41 | 9.22 | 15.11 | 10.00 | 81.7 | 90.0 |
| Captain | Captain | Mendy | DEF | 11 | 4.0 | 5.93 | 15.33 | 24.38 | 1.00 | 68.3 | 58.0 |
| XI | XI | Gabriel | DEF | 1 | 8.0 | 4.46 | 12.81 | 20.76 | 8.00 | 83.1 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.47 | 12.43 | 20.20 | 2.00 | 91.3 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.52 | 12.04 | 19.17 | 0.00 | 78.4 | 90.0 |
| Bench 2 | Bench | Virgil | DEF | 14 | 6.5 | 4.33 | 11.97 | 19.13 | 1.00 | 88.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 5.66 | 16.12 | 26.11 | 9.00 | 115.4 | 90.0 |
| Bench 3 | Bench | Thiago | FWD | 4 | 8.0 | 4.06 | 12.77 | 21.15 | 2.00 | 70.7 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 3.71 | 11.32 | 19.09 | 1.00 | 52.7 | 45.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.58 | 16.73 | 27.84 | 23.00 | 95.4 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.20 | 14.98 | 24.42 | 4.00 | 105.3 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.60 | 14.22 | 23.51 | 4.00 | 90.5 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.11 | 13.79 | 21.99 | 0.00 | 72.2 | 45.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.48 | 13.66 | 22.58 | 5.00 | 85.0 | 90.0 |

## GW3

- Train rows: 192260
- Bank: 0.70 -> 0.60
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Ajayi
- Effective captain: B.Fernandes
- Chip used: none
- Predicted score: 56.40
- Actual score: 41.00
- Transfer: Mendy -> Ajayi (projected gain 1.86, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Raya | GK | 1 | 6.0 | 3.64 | 10.66 | 17.36 | 3.00 | 84.1 | 90.0 |
| XI | XI | Tzolakis | GK | 11 | 4.5 | 3.70 | 9.96 | 16.04 | 6.00 | 89.8 | 90.0 |
| Vice Captain | XI | Ajayi | DEF | 11 | 4.1 | 5.23 | 12.83 | 19.96 | 5.00 | 123.7 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 8.0 | 3.95 | 12.35 | 20.62 | 2.00 | 72.2 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.75 | 12.25 | 18.72 | 4.00 | 93.7 | 76.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.94 | 11.20 | 18.38 | 8.00 | 75.5 | 90.0 |
| Bench 2 | Bench | Virgil | DEF | 14 | 6.5 | 3.73 | 10.48 | 17.04 | 6.00 | 77.5 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.43 | 14.72 | 24.38 | 1.00 | 93.0 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 8.0 | 4.18 | 12.25 | 20.14 | 2.00 | 62.6 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.69 | 8.82 | 15.08 | 2.00 | 41.0 | 65.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 6.22 | 19.81 | 33.29 | 2.00 | 108.9 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.09 | 13.97 | 22.03 | 0.00 | 90.1 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.93 | 13.65 | 22.24 | 3.00 | 87.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.74 | 13.33 | 22.52 | 6.00 | 73.7 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 1.99 | 8.21 | 14.69 | 5.00 | 25.7 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.60 -> 0.30
- Free transfers: 2 -> 2
- Captain: Rogers
- Vice captain: João Pedro
- Effective captain: Rogers
- Chip used: triple_captain
- Predicted score: 62.69
- Actual score: 93.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (7.79).
- Transfer: Tzolis -> Ødegaard (projected gain 4.47, hit 0)
- Chip used: Triple Captain on Rogers. Optimizer chose Triple Captain here because the current estimated captain upside (6.60) beats the best remaining Triple Captain opportunity (7.79).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.94 | 11.27 | 18.07 | 14.00 | 95.0 | 90.0 |
| Bench 1 | Bench | Tzolakis | GK | 11 | 4.5 | 2.90 | 8.81 | 14.44 | 2.00 | 78.3 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 8.0 | 4.19 | 12.47 | 20.48 | 9.00 | 79.9 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.97 | 10.71 | 16.74 | 11.00 | 69.2 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.79 | 10.46 | 16.96 | 8.00 | 82.8 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.47 | 10.46 | 17.38 | 6.00 | 80.1 | 90.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.1 | 3.41 | 8.58 | 15.12 | 1.00 | 88.0 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 5.89 | 16.65 | 26.56 | 12.00 | 111.2 | 90.0 |
| XI | XI | Thiago | FWD | 4 | 7.9 | 3.63 | 10.89 | 18.21 | 1.00 | 61.1 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 2.97 | 8.59 | 14.29 | 12.00 | 49.2 | 62.0 |
| Captain | Captain | Rogers | MID | 6 | 7.5 | 6.60 | 17.63 | 27.62 | 8.00 | 125.9 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 4.67 | 16.29 | 28.16 | 2.00 | 75.6 | 90.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 4.77 | 13.02 | 20.78 | 3.00 | 90.6 | 84.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.57 | 12.89 | 21.17 | 3.00 | 79.4 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 3.14 | 10.83 | 18.34 | 4.00 | 36.2 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.30 -> 2.10
- Free transfers: 2 -> 2
- Captain: B.Fernandes
- Vice captain: Rogers
- Effective captain: B.Fernandes
- Chip used: bench_boost
- Predicted score: 63.29
- Actual score: 41.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.38) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Thiago -> Calvert-Lewin (projected gain 2.05, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.38) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.09 | 11.88 | 19.12 | 1.00 | 96.8 | 90.0 |
| Bench 1 | Bench Boost | Tzolakis | GK | 11 | 4.5 | 2.98 | 8.75 | 14.22 | 6.00 | 80.7 | 90.0 |
| XI | XI | Gabriel | DEF | 1 | 8.0 | 4.25 | 12.74 | 20.95 | 1.00 | 83.2 | 90.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 3.75 | 11.05 | 18.04 | 4.00 | 84.6 | 90.0 |
| XI | XI | Virgil | DEF | 14 | 6.5 | 3.65 | 10.73 | 17.46 | 8.00 | 84.3 | 90.0 |
| Bench 3 | Bench Boost | De Cuyper | DEF | 5 | 4.7 | 2.82 | 10.14 | 16.83 | 6.00 | 68.1 | 90.0 |
| Bench 4 | Bench Boost | Ajayi | DEF | 11 | 4.1 | 2.60 | 7.07 | 10.84 | 1.00 | 91.1 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.7 | 3.79 | 12.85 | 23.89 | 0.00 | 66.9 | 0.0 |
| XI | XI | Calvert-Lewin | FWD | 13 | 6.0 | 4.80 | 12.47 | 19.44 | 2.00 | 84.6 | 90.0 |
| Bench 2 | Bench Boost | Emersonn | FWD | 12 | 5.5 | 2.98 | 9.83 | 16.30 | 2.00 | 54.4 | 80.0 |
| Captain | Captain | B.Fernandes | MID | 16 | 12.0 | 5.70 | 16.83 | 28.39 | 2.00 | 92.8 | 90.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.6 | 4.85 | 14.81 | 23.49 | 2.00 | 85.7 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 3.90 | 12.25 | 20.79 | 2.00 | 70.2 | 80.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.83 | 12.03 | 19.69 | 2.00 | 60.6 | 72.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 3.59 | 10.67 | 17.74 | 0.00 | 63.6 | 21.0 |