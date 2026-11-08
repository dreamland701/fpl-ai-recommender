# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 344.64
- Total actual points: 342.00
- Average predicted points: 68.93
- Average actual points: 68.40
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
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 69.75
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.59 | 12.43 | 19.76 | 6.00 | 86.9 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.01 | 0.46 | 0.89 | 0.00 | 2.4 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 6.07 | 15.35 | 24.43 | 1.00 | 74.7 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.92 | 14.25 | 23.26 | 2.00 | 90.0 | 90.0 |
| Bench 3 | Bench | De Cuyper | DEF | 5 | 4.6 | 4.49 | 13.41 | 21.57 | 0.00 | 69.9 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.94 | 12.86 | 20.36 | 9.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.0 | 4.50 | 11.56 | 19.00 | 6.00 | 56.7 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.34 | 23.36 | 38.25 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.65 | 16.82 | 27.30 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 3.33 | 10.15 | 17.17 | 1.00 | 53.0 | 45.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.63 | 18.92 | 31.48 | 23.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.54 | 16.18 | 26.37 | 4.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.70 | 15.26 | 25.24 | 4.00 | 83.7 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.63 | 14.83 | 24.61 | 5.00 | 82.1 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.39 | 14.03 | 22.30 | 0.00 | 71.7 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 68.47
- Actual score: 50.00
- Transfer: Guéhi -> Calafiori (projected gain 1.96, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.93 | 11.26 | 18.27 | 3.00 | 82.6 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.02 | 0.27 | 0.51 | 0.00 | 2.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 5.72 | 15.83 | 25.12 | 5.00 | 90.0 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.92 | 13.92 | 22.17 | 2.00 | 90.0 | 66.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.55 | 13.62 | 21.02 | 4.00 | 81.3 | 76.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.99 | 13.41 | 21.05 | 6.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.84 | 10.77 | 17.31 | 8.00 | 67.8 | 70.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.22 | 25.50 | 41.22 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.63 | 15.54 | 25.78 | 1.00 | 88.5 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.14 | 6.92 | 11.83 | 2.00 | 40.8 | 65.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.95 | 22.19 | 37.28 | 2.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.06 | 14.75 | 23.27 | 0.00 | 82.7 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.38 | 14.45 | 23.51 | 3.00 | 87.3 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.91 | 13.79 | 23.27 | 6.00 | 75.1 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.00 | 6.62 | 11.77 | 5.00 | 33.2 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 64.54
- Actual score: 79.00
- Transfer: Tzolis -> Ødegaard (projected gain 3.56, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.18 | 12.20 | 19.55 | 14.00 | 89.4 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.08 | 0.44 | 0.80 | 0.00 | 3.5 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.83 | 14.14 | 22.32 | 6.00 | 79.9 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.99 | 12.46 | 20.20 | 1.00 | 84.5 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.90 | 11.25 | 17.94 | 1.00 | 72.9 | 58.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.84 | 11.18 | 17.59 | 11.00 | 64.6 | 90.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 3.78 | 10.91 | 17.49 | 2.00 | 86.7 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.99 | 23.33 | 38.46 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.98 | 17.61 | 28.09 | 12.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 2.55 | 7.30 | 12.19 | 12.00 | 48.3 | 62.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.60 | 19.25 | 30.14 | 8.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.38 | 17.68 | 30.49 | 2.00 | 84.5 | 90.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 4.87 | 14.38 | 23.00 | 3.00 | 80.7 | 84.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.99 | 13.63 | 22.32 | 3.00 | 82.0 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.66 | 8.64 | 14.60 | 4.00 | 40.5 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 69.02
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (9.52).
- Transfer: M.Sangaré -> Groß (projected gain 2.84, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (9.52).
- Autosub: De Cuyper replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.17 | 12.50 | 20.15 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.20 | 0.54 | 0.87 | 0.00 | 3.0 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.33 | 13.08 | 21.03 | 1.00 | 81.6 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.84 | 11.34 | 19.03 | 1.00 | 87.3 | 90.0 |
| Bench 2 | Autosub In | De Cuyper | DEF | 5 | 4.7 | 2.86 | 10.40 | 17.31 | 6.00 | 68.2 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.48 | 9.78 | 16.22 | 1.00 | 78.7 | 77.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.20 | 6.96 | 11.71 | 0.00 | 45.1 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.73 | 25.25 | 41.14 | 6.00 | 90.0 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.85 | 12.15 | 20.72 | 0.00 | 67.7 | 0.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.57 | 8.55 | 14.25 | 2.00 | 52.7 | 80.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.53 | 19.13 | 32.21 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 4.98 | 15.80 | 25.04 | 2.00 | 82.1 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.10 | 12.90 | 21.17 | 14.00 | 89.7 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.11 | 12.26 | 20.73 | 2.00 | 75.2 | 80.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.43 | 11.32 | 18.60 | 2.00 | 58.9 | 72.0 |

## GW6

- Train rows: 194240
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 72.87
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.40) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Emersonn -> Kostoulas (projected gain 3.76, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.40) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.38 | 12.74 | 20.48 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Palmer | GK | 12 | 4.0 | 0.42 | 0.75 | 1.15 | 0.00 | 4.4 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 5.27 | 14.89 | 23.38 | 15.00 | 90.0 | 67.0 |
| XI | XI | Calafiori | DEF | 1 | 5.8 | 4.83 | 13.70 | 22.05 | 9.00 | 88.5 | 81.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.16 | 9.87 | 17.49 | 1.00 | 83.6 | 90.0 |
| Bench 2 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.07 | 8.80 | 14.70 | 1.00 | 73.2 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.87 | 6.43 | 12.74 | 3.00 | 42.9 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.20 | 24.22 | 40.03 | 6.00 | 90.0 | 79.0 |
| XI | XI | Kostoulas | FWD | 5 | 5.6 | 4.61 | 12.55 | 19.04 | 1.00 | 85.1 | 59.0 |
| Bench 3 | Bench Boost | João Pedro | FWD | 6 | 7.6 | 3.03 | 9.85 | 17.25 | 12.00 | 37.7 | 71.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 6.94 | 19.01 | 29.02 | 6.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.17 | 18.31 | 30.99 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.34 | 15.33 | 24.58 | 9.00 | 88.6 | 83.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.74 | 11.46 | 19.10 | 1.00 | 65.0 | 89.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.62 | 11.34 | 19.24 | 0.00 | 70.4 | 0.0 |