# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 226.00
- Total actual points: 228.00
- Average predicted points: 56.50
- Average actual points: 57.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW30 are included before the first simulated week.
- League-average scores were not available for this run.

## GW31

- Train rows: 184363
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.85
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Hill replaced Gabriel dos Santos Magalhães.
- Autosub: Junior Kroupi replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.63 | 9.05 | 15.28 | 0.00 | 75.0 | 0.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.05 | 7.74 | 12.00 | 3.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.93 | 14.15 | 22.23 | 3.00 | 113.9 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.68 | 12.25 | 20.76 | 0.00 | 79.3 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 4.90 | 12.13 | 18.32 | 0.00 | 111.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.74 | 10.56 | 16.53 | 1.00 | 95.6 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.2 | 3.18 | 9.21 | 14.85 | -1.00 | 85.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.45 | 15.66 | 25.03 | 2.00 | 99.2 | 77.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.7 | 2.36 | 6.73 | 10.50 | 5.00 | 60.2 | 17.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.3 | 1.76 | 6.45 | 11.20 | 0.00 | 59.6 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.27 | 18.60 | 29.91 | 13.00 | 126.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.78 | 14.46 | 23.59 | 2.00 | 89.5 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 4.20 | 13.55 | 22.73 | 0.00 | 73.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.41 | 13.15 | 20.54 | 3.00 | 103.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.18 | 13.09 | 19.95 | 10.00 | 108.4 | 88.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 50.60
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.74) beats the best remaining Triple Captain opportunity (14.24).
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.78, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.74) beats the best remaining Triple Captain opportunity (14.24).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.43 | 7.49 | 12.80 | 1.00 | 60.4 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 1.62 | 5.33 | 8.95 | 2.00 | 70.6 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 3.92 | 10.41 | 15.64 | 5.00 | 91.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.29 | 10.08 | 17.37 | 4.00 | 62.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.12 | 9.56 | 15.04 | 3.00 | 95.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 2.86 | 9.51 | 15.75 | 9.00 | 71.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.72 | 8.86 | 14.48 | 4.00 | 81.9 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 3.92 | 13.23 | 22.14 | 2.00 | 77.2 | 81.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 1.97 | 6.31 | 10.06 | 6.00 | 49.6 | 84.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.2 | 1.39 | 4.27 | 7.78 | 2.00 | 42.0 | 70.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.74 | 18.56 | 30.03 | 4.00 | 106.9 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.09 | 13.36 | 22.10 | 4.00 | 83.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 3.55 | 11.38 | 19.42 | 2.00 | 56.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.47 | 11.03 | 17.77 | 5.00 | 77.5 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 2.71 | 8.75 | 14.03 | 3.00 | 60.9 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 66.74
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.38) beats the best remaining Bench Boost opportunity (0.16).
- Transfer: Adam Armstrong -> Dominic Calvert-Lewin (projected gain 0.87, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.38) beats the best remaining Bench Boost opportunity (0.16).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.37 | 7.72 | 13.06 | 1.00 | 74.9 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.9 | 2.16 | 6.25 | 10.19 | 10.00 | 81.2 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 5.17 | 12.11 | 18.36 | 6.00 | 126.8 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.57 | 10.62 | 15.80 | 12.00 | 109.7 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 3.34 | 10.26 | 17.07 | 8.00 | 84.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 4.12 | 9.76 | 15.12 | 5.00 | 111.9 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 2.83 | 9.21 | 16.08 | 0.00 | 65.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.42 | 14.36 | 23.04 | 0.00 | 118.3 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.66 | 11.02 | 16.15 | 8.00 | 114.5 | 180.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 3.75 | 8.44 | 13.04 | 10.00 | 93.3 | 137.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 6.12 | 15.52 | 24.58 | 2.00 | 129.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.06 | 15.26 | 25.80 | 6.00 | 88.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 5.11 | 13.51 | 21.89 | 5.00 | 109.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.48 | 10.50 | 17.06 | 5.00 | 78.7 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 2.44 | 8.05 | 13.63 | 0.00 | 58.1 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 51.81
- Actual score: 43.00
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 4.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.70 | 10.50 | 16.76 | 10.00 | 101.3 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.09 | 6.46 | 10.68 | 7.00 | 80.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.18 | 14.72 | 23.26 | 4.00 | 126.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.64 | 13.01 | 21.10 | 8.00 | 105.5 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.44 | 11.30 | 18.53 | 0.00 | 101.1 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 3.37 | 11.12 | 18.17 | 0.00 | 98.4 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.05 | 10.00 | 16.72 | 0.00 | 96.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.7 | 5.27 | 14.59 | 23.17 | 10.00 | 123.0 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.10 | 9.81 | 15.59 | 0.00 | 82.8 | 0.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.14 | 7.41 | 12.81 | 0.00 | 59.5 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.91 | 17.52 | 29.30 | 5.00 | 123.9 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 4.13 | 13.63 | 22.70 | 0.00 | 90.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.96 | 11.56 | 18.77 | 1.00 | 92.3 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 3.20 | 11.15 | 19.28 | 0.00 | 61.8 | 0.0 |
| Bench 4 | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.04 | 5.36 | 10.49 | 0.00 | 28.8 | 0.0 |