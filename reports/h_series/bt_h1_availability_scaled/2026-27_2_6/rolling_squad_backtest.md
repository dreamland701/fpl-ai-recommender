# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 348.33
- Total actual points: 321.00
- Average predicted points: 69.67
- Average actual points: 64.20
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
- Captain: Haaland
- Vice captain: Mendy
- Effective captain: Haaland
- Chip used: none
- Predicted score: 73.67
- Actual score: 93.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.67 | 12.73 | 20.34 | 6.00 | 88.6 | 90.0 |
| Bench 1 | Bench | Button | GK | 12 | 4.0 | 0.00 | 0.03 | 0.22 | 0.00 | 1.8 | 0.0 |
| Vice Captain | XI | Mendy | DEF | 11 | 4.0 | 6.67 | 16.85 | 26.80 | 1.00 | 74.6 | 58.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.97 | 14.68 | 23.40 | 0.00 | 70.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.93 | 12.88 | 20.43 | 9.00 | 89.7 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 3.93 | 11.22 | 18.04 | 0.00 | 89.2 | 90.0 |
| Bench 4 | Bench | Giles | DEF | 11 | 4.0 | 3.77 | 9.99 | 16.05 | 6.00 | 78.3 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.21 | 22.93 | 37.48 | 13.00 | 89.7 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.76 | 17.18 | 27.93 | 9.00 | 89.4 | 90.0 |
| Bench 2 | Bench | Emersonn | FWD | 12 | 5.5 | 4.62 | 14.01 | 23.66 | 1.00 | 55.2 | 45.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 6.58 | 18.80 | 31.26 | 23.00 | 90.7 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 6.64 | 18.01 | 29.43 | 11.00 | 69.7 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 6.41 | 16.74 | 26.63 | 0.00 | 75.6 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.58 | 16.34 | 26.66 | 4.00 | 89.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.02 | 16.28 | 26.95 | 4.00 | 86.6 | 90.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 70.22
- Actual score: 52.00
- Transfer: Giles -> Ajayi (projected gain 5.10, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.12 | 11.87 | 19.36 | 3.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Button | GK | 12 | 4.0 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 5.45 | 15.07 | 23.91 | 5.00 | 88.3 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.67 | 13.87 | 21.25 | 4.00 | 82.0 | 76.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.97 | 13.39 | 21.04 | 6.00 | 91.0 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 4.61 | 12.89 | 20.68 | 8.00 | 69.8 | 70.0 |
| Bench 2 | Bench | O'Shea | DEF | 12 | 4.0 | 2.74 | 7.68 | 12.35 | 3.00 | 77.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.10 | 25.08 | 40.47 | 9.00 | 88.6 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.79 | 16.09 | 26.71 | 1.00 | 89.4 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.16 | 6.98 | 11.92 | 2.00 | 41.5 | 65.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.86 | 21.87 | 36.73 | 2.00 | 90.6 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 5.63 | 16.34 | 26.91 | 2.00 | 78.0 | 89.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.38 | 15.77 | 24.93 | 0.00 | 85.7 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.54 | 14.98 | 24.42 | 3.00 | 88.7 | 90.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.05 | 6.81 | 12.10 | 5.00 | 34.3 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: João Pedro
- Effective captain: Haaland
- Chip used: none
- Predicted score: 63.58
- Actual score: 76.00
- Transfer: Emersonn -> Barry (projected gain 0.76, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.13 | 12.16 | 19.52 | 14.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Button | GK | 12 | 4.0 | 0.00 | 0.08 | 0.19 | 0.00 | 3.5 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 4.54 | 13.12 | 20.53 | 11.00 | 66.2 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 4.42 | 12.71 | 20.25 | 1.00 | 75.8 | 58.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.1 | 3.84 | 12.05 | 19.54 | 1.00 | 82.6 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.89 | 11.23 | 18.00 | 2.00 | 87.5 | 90.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.99 | 8.24 | 13.14 | 1.00 | 78.4 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.84 | 22.80 | 37.48 | 9.00 | 89.2 | 90.0 |
| Vice Captain | XI | João Pedro | FWD | 6 | 7.6 | 6.07 | 17.94 | 28.64 | 12.00 | 89.4 | 90.0 |
| XI | XI | Barry | FWD | 9 | 5.6 | 4.45 | 12.69 | 20.32 | 2.00 | 64.4 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.66 | 18.57 | 32.01 | 2.00 | 85.3 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 5.45 | 16.35 | 27.03 | 8.00 | 75.5 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.41 | 14.86 | 24.38 | 3.00 | 84.3 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.4 | 3.90 | 12.04 | 20.51 | 3.00 | 63.3 | 80.0 |
| Bench 4 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.76 | 8.96 | 15.14 | 4.00 | 41.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 73.06
- Actual score: 40.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (9.38).
- Transfer: De Cuyper -> Bogle (projected gain 2.42, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.61) beats the best remaining Triple Captain opportunity (9.38).
- Autosub: Tzolis replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.15 | 12.54 | 20.27 | 1.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Button | GK | 12 | 4.0 | 0.04 | 0.14 | 0.19 | 0.00 | 2.5 | 0.0 |
| XI | XI | Bogle | DEF | 13 | 4.6 | 4.84 | 12.52 | 19.52 | 5.00 | 71.2 | 66.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.73 | 11.06 | 18.58 | 1.00 | 84.3 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.79 | 10.65 | 17.65 | 1.00 | 80.4 | 77.0 |
| Bench 3 | Bench | O'Shea | DEF | 12 | 4.0 | 2.56 | 7.16 | 12.12 | 2.00 | 72.5 | 90.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.15 | 6.78 | 11.40 | 0.00 | 44.5 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.61 | 24.83 | 40.34 | 6.00 | 88.5 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 4.40 | 13.94 | 23.76 | 0.00 | 68.8 | 0.0 |
| XI | XI | Barry | FWD | 9 | 5.6 | 5.11 | 13.64 | 21.08 | 6.00 | 62.4 | 90.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.47 | 18.95 | 31.89 | 2.00 | 90.6 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 5.49 | 16.95 | 27.75 | 2.00 | 84.2 | 80.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.75 | 14.24 | 24.10 | 2.00 | 77.9 | 80.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.50 | 12.98 | 21.55 | 0.00 | 69.6 | 21.0 |
| Bench 2 | Autosub In | Tzolis | MID | 1 | 6.4 | 3.66 | 11.82 | 20.09 | 2.00 | 63.8 | 72.0 |

## GW6

- Train rows: 194240
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 67.79
- Actual score: 60.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.04) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Tzolis -> Groß (projected gain 10.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.04) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.35 | 12.74 | 20.57 | 3.00 | 89.7 | 90.0 |
| Bench 1 | Bench Boost | Button | GK | 12 | 4.0 | 0.26 | 0.35 | 0.54 | 0.00 | 3.9 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 2.96 | 9.25 | 16.52 | 1.00 | 80.3 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.06 | 8.73 | 14.57 | 1.00 | 72.6 | 90.0 |
| Bench 2 | Bench Boost | Bogle | DEF | 13 | 4.6 | 2.47 | 8.48 | 14.37 | 1.00 | 54.5 | 85.0 |
| XI | XI | O'Shea | DEF | 12 | 4.0 | 3.24 | 8.37 | 13.23 | 11.00 | 79.4 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.85 | 6.38 | 12.77 | 3.00 | 42.3 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.05 | 23.73 | 39.13 | 6.00 | 88.6 | 79.0 |
| XI | XI | Barry | FWD | 9 | 5.6 | 4.31 | 13.06 | 20.69 | 6.00 | 67.9 | 85.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 3.49 | 11.35 | 19.85 | 12.00 | 37.1 | 71.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.9 | 6.99 | 19.20 | 29.36 | 6.00 | 91.6 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.10 | 18.07 | 30.57 | 1.00 | 90.2 | 90.0 |
| XI | XI | Saka | MID | 1 | 9.5 | 5.92 | 17.73 | 28.95 | 2.00 | 83.7 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 4.24 | 13.34 | 22.65 | 0.00 | 71.9 | 0.0 |
| Bench 3 | Bench Boost | M.Sangaré | MID | 4 | 5.6 | 2.46 | 7.62 | 13.41 | 1.00 | 39.6 | 38.0 |