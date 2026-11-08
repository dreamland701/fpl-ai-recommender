# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2026-27 GW1-GW1
- Simulated weeks: GW2-GW6
- Total predicted points: 344.25
- Total actual points: 342.00
- Average predicted points: 68.85
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
- Predicted score: 69.87
- Actual score: 89.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.59 | 12.46 | 19.85 | 6.00 | 84.9 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.02 | 0.52 | 1.03 | 0.00 | 0.3 | 0.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 6.08 | 15.33 | 24.40 | 1.00 | 74.6 | 58.0 |
| XI | XI | Guéhi | DEF | 15 | 6.0 | 4.82 | 13.92 | 22.71 | 2.00 | 89.9 | 90.0 |
| Bench 3 | Bench | De Cuyper | DEF | 5 | 4.6 | 4.37 | 13.02 | 20.91 | 0.00 | 69.4 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.92 | 12.76 | 20.17 | 9.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Ajayi | DEF | 11 | 4.0 | 4.41 | 11.25 | 18.47 | 6.00 | 56.0 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.36 | 23.39 | 38.28 | 13.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.66 | 16.80 | 27.24 | 9.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 3.35 | 10.16 | 17.15 | 1.00 | 52.7 | 45.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.66 | 19.03 | 31.65 | 23.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.57 | 16.26 | 26.50 | 4.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 4.81 | 15.59 | 25.79 | 4.00 | 84.1 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 4.65 | 14.88 | 24.69 | 5.00 | 82.1 | 90.0 |
| XI | XI | Tzolis | MID | 1 | 6.5 | 5.41 | 14.11 | 22.42 | 0.00 | 71.9 | 45.0 |

## GW3

- Train rows: 192260
- Bank: 0.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: none
- Predicted score: 68.36
- Actual score: 50.00
- Transfer: Guéhi -> Calafiori (projected gain 1.92, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 3.93 | 11.29 | 18.36 | 3.00 | 80.6 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.03 | 0.33 | 0.65 | 0.00 | 0.0 | 0.0 |
| XI | XI | Ajayi | DEF | 11 | 4.0 | 5.62 | 15.49 | 24.55 | 5.00 | 90.0 | 90.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.83 | 13.59 | 21.62 | 2.00 | 89.8 | 66.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 4.97 | 13.34 | 20.91 | 6.00 | 90.0 | 90.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.6 | 4.46 | 13.33 | 20.55 | 4.00 | 81.2 | 76.0 |
| Bench 2 | Bench | Mendy | DEF | 11 | 4.0 | 3.81 | 10.63 | 17.05 | 8.00 | 67.4 | 70.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 9.23 | 25.48 | 41.16 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 4.63 | 15.51 | 25.70 | 1.00 | 88.2 | 90.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.15 | 6.95 | 11.85 | 2.00 | 40.8 | 65.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.95 | 22.20 | 37.31 | 2.00 | 90.0 | 90.0 |
| XI | XI | M.Sangaré | MID | 4 | 5.6 | 5.16 | 15.10 | 23.84 | 0.00 | 83.2 | 45.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.43 | 14.64 | 23.82 | 3.00 | 87.6 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.5 | 3.92 | 13.82 | 23.33 | 6.00 | 75.0 | 86.0 |
| Bench 4 | Bench | Tzolis | MID | 1 | 6.5 | 2.03 | 6.73 | 11.95 | 5.00 | 33.6 | 90.0 |

## GW4

- Train rows: 192914
- Bank: 0.50 -> 0.20
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Rogers
- Effective captain: Haaland
- Chip used: none
- Predicted score: 64.36
- Actual score: 79.00
- Transfer: Tzolis -> Ødegaard (projected gain 3.77, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.19 | 12.28 | 19.67 | 14.00 | 87.5 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.10 | 0.52 | 0.93 | 0.00 | 1.4 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.75 | 13.87 | 21.85 | 6.00 | 79.8 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.89 | 12.12 | 19.63 | 1.00 | 83.7 | 90.0 |
| XI | XI | Mendy | DEF | 11 | 4.0 | 3.87 | 11.14 | 17.75 | 1.00 | 72.7 | 58.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.7 | 3.75 | 10.89 | 17.11 | 11.00 | 64.5 | 90.0 |
| Bench 2 | Bench | Egan | DEF | 11 | 4.0 | 3.74 | 10.76 | 17.22 | 2.00 | 86.1 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 7.99 | 23.30 | 38.34 | 9.00 | 90.0 | 90.0 |
| XI | XI | João Pedro | FWD | 6 | 7.6 | 5.99 | 17.63 | 28.06 | 12.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Emersonn | FWD | 12 | 5.5 | 2.57 | 7.34 | 12.21 | 12.00 | 48.3 | 62.0 |
| Vice Captain | XI | Rogers | MID | 6 | 7.5 | 6.62 | 19.32 | 30.25 | 8.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 12.0 | 5.39 | 17.73 | 30.57 | 2.00 | 84.6 | 90.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 4.90 | 14.45 | 23.12 | 3.00 | 80.8 | 84.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 5.03 | 13.78 | 22.57 | 3.00 | 82.1 | 90.0 |
| Bench 3 | Bench | M.Sangaré | MID | 4 | 5.6 | 2.74 | 8.90 | 15.03 | 4.00 | 40.9 | 90.0 |

## GW5

- Train rows: 193573
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: B.Fernandes
- Effective captain: Haaland
- Chip used: triple_captain
- Predicted score: 68.95
- Actual score: 50.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (9.51).
- Transfer: M.Sangaré -> Groß (projected gain 2.66, hit 0)
- Chip used: Triple Captain on Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (8.73) beats the best remaining Triple Captain opportunity (9.51).
- Autosub: De Cuyper replaced João Pedro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.17 | 12.57 | 20.27 | 1.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Palmer | GK | 12 | 4.0 | 0.21 | 0.63 | 1.00 | 0.00 | 1.0 | 0.0 |
| XI | XI | Calafiori | DEF | 1 | 5.7 | 4.25 | 12.79 | 20.55 | 1.00 | 81.4 | 90.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.76 | 11.05 | 18.52 | 1.00 | 86.7 | 90.0 |
| Bench 2 | Autosub In | De Cuyper | DEF | 5 | 4.7 | 2.77 | 10.11 | 16.83 | 6.00 | 68.1 | 90.0 |
| XI | XI | Egan | DEF | 11 | 4.0 | 3.45 | 9.67 | 16.02 | 1.00 | 78.3 | 77.0 |
| Bench 4 | Bench | Mendy | DEF | 11 | 4.0 | 2.16 | 6.81 | 11.45 | 0.00 | 44.8 | 0.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.73 | 25.23 | 41.04 | 6.00 | 90.0 | 90.0 |
| XI | Bench | João Pedro | FWD | 6 | 7.7 | 3.86 | 12.17 | 20.70 | 0.00 | 67.6 | 0.0 |
| Bench 3 | Bench | Emersonn | FWD | 12 | 5.5 | 2.60 | 8.60 | 14.27 | 2.00 | 52.6 | 80.0 |
| Vice Captain | XI | B.Fernandes | MID | 16 | 12.0 | 6.54 | 19.18 | 32.30 | 2.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.00 | 15.87 | 25.15 | 2.00 | 82.2 | 90.0 |
| XI | XI | Groß | MID | 5 | 5.7 | 4.13 | 12.99 | 21.33 | 14.00 | 90.0 | 90.0 |
| XI | XI | Szoboszlai | MID | 14 | 7.0 | 4.15 | 12.39 | 20.94 | 2.00 | 75.3 | 80.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.46 | 11.39 | 18.72 | 2.00 | 59.1 | 72.0 |

## GW6

- Train rows: 194240
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Haaland
- Vice captain: Groß
- Effective captain: Haaland
- Chip used: bench_boost
- Predicted score: 72.71
- Actual score: 74.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.34) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Emersonn -> Kostoulas (projected gain 3.07, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.34) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Raya | GK | 1 | 6.0 | 4.39 | 12.82 | 20.65 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench Boost | Palmer | GK | 12 | 4.0 | 0.43 | 0.82 | 1.33 | 0.00 | 2.3 | 0.0 |
| XI | XI | De Cuyper | DEF | 5 | 4.8 | 5.18 | 14.58 | 22.87 | 15.00 | 90.0 | 67.0 |
| XI | XI | Calafiori | DEF | 1 | 5.8 | 4.75 | 13.44 | 21.61 | 9.00 | 88.3 | 81.0 |
| XI | XI | Ajayi | DEF | 11 | 4.1 | 3.08 | 9.58 | 16.99 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench Boost | Egan | DEF | 11 | 4.0 | 3.04 | 8.66 | 14.46 | 1.00 | 72.8 | 90.0 |
| Bench 4 | Bench Boost | Mendy | DEF | 11 | 4.0 | 1.83 | 6.26 | 12.43 | 3.00 | 42.6 | 90.0 |
| Captain | Captain | Haaland | FWD | 15 | 15.5 | 8.20 | 24.20 | 39.96 | 6.00 | 90.0 | 79.0 |
| XI | XI | Kostoulas | FWD | 5 | 5.6 | 4.63 | 12.58 | 19.03 | 1.00 | 84.6 | 59.0 |
| Bench 2 | Bench Boost | João Pedro | FWD | 6 | 7.6 | 3.05 | 9.88 | 17.27 | 12.00 | 37.6 | 71.0 |
| Vice Captain | XI | Groß | MID | 5 | 5.8 | 6.98 | 19.12 | 29.20 | 6.00 | 90.0 | 90.0 |
| XI | XI | B.Fernandes | MID | 16 | 11.9 | 6.19 | 18.36 | 31.09 | 1.00 | 90.0 | 90.0 |
| XI | XI | Rogers | MID | 6 | 7.6 | 5.36 | 15.39 | 24.67 | 9.00 | 88.6 | 83.0 |
| XI | XI | Ødegaard | MID | 1 | 6.7 | 3.77 | 11.55 | 19.24 | 1.00 | 65.2 | 89.0 |
| XI | XI | Szoboszlai | MID | 14 | 6.9 | 3.66 | 11.47 | 19.44 | 0.00 | 70.5 | 0.0 |