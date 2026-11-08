# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 282.72
- Total actual points: 229.00
- Average predicted points: 70.68
- Average actual points: 57.25
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
- Predicted score: 70.31
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: James Hill replaced Gabriel dos Santos Magalhães.
- Autosub: Junior Kroupi replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.25 | 10.88 | 18.43 | 0.00 | 75.2 | 0.0 |
| XI | XI | Bernd Leno | GK | 10 | 4.9 | 3.65 | 9.19 | 14.33 | 3.00 | 88.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 6.17 | 16.88 | 26.52 | 3.00 | 113.8 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 6.00 | 14.64 | 22.17 | 0.00 | 110.8 | 36.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.50 | 14.62 | 24.81 | 0.00 | 79.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.67 | 12.81 | 20.07 | 1.00 | 97.0 | 90.0 |
| Bench 2 | Autosub In | James Hill | DEF | 4 | 4.2 | 3.99 | 11.21 | 18.11 | -1.00 | 87.4 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.55 | 18.61 | 29.80 | 2.00 | 98.5 | 77.0 |
| Bench 3 | Autosub In | Junior Kroupi | FWD | 4 | 4.7 | 2.99 | 8.32 | 13.07 | 5.00 | 62.5 | 17.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.3 | 2.16 | 7.78 | 13.58 | 0.00 | 59.3 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 8.00 | 22.70 | 36.36 | 13.00 | 129.1 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.77 | 17.17 | 28.06 | 2.00 | 88.8 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.15 | 16.19 | 27.19 | 0.00 | 74.7 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.55 | 15.92 | 24.88 | 3.00 | 104.3 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 6.29 | 15.86 | 24.21 | 10.00 | 107.7 | 88.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.00
- Actual score: 47.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.98 | 8.94 | 15.34 | 1.00 | 60.2 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 1.81 | 6.20 | 10.64 | 2.00 | 68.9 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.60 | 11.97 | 18.25 | 5.00 | 91.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.07 | 11.79 | 20.31 | 4.00 | 61.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.82 | 11.33 | 17.94 | 3.00 | 95.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.42 | 10.97 | 18.29 | 9.00 | 70.4 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.40 | 10.65 | 17.46 | 4.00 | 82.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.87 | 15.08 | 25.31 | 2.00 | 77.5 | 81.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.7 | 2.32 | 7.60 | 12.29 | 6.00 | 49.4 | 84.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.2 | 1.57 | 5.17 | 9.56 | 2.00 | 40.7 | 70.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.24 | 21.50 | 34.66 | 4.00 | 108.2 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 4.96 | 15.24 | 25.32 | 4.00 | 83.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.20 | 13.11 | 22.52 | 2.00 | 56.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.21 | 12.74 | 20.62 | 5.00 | 76.3 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.17 | 10.11 | 16.38 | 3.00 | 59.2 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 81.17
- Actual score: 80.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.61) beats the best remaining Bench Boost opportunity (0.60).
- Chip advisory: triple_captain (0.60): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Adam Armstrong -> Dominic Calvert-Lewin (projected gain 1.32, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.61) beats the best remaining Bench Boost opportunity (0.60).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.82 | 9.34 | 15.90 | 1.00 | 73.8 | 90.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.9 | 2.53 | 7.48 | 12.39 | 10.00 | 80.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 6.36 | 14.80 | 22.38 | 6.00 | 126.3 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 5.54 | 12.91 | 19.23 | 12.00 | 109.8 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 3.99 | 12.36 | 20.56 | 8.00 | 82.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 5.01 | 11.88 | 18.43 | 5.00 | 111.4 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.44 | 11.13 | 19.46 | 0.00 | 64.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.57 | 17.51 | 27.92 | 0.00 | 115.3 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 5.93 | 13.56 | 19.85 | 8.00 | 115.8 | 180.0 |
| XI | XI | Junior Kroupi | FWD | 4 | 4.6 | 4.50 | 10.20 | 15.86 | 10.00 | 92.1 | 137.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 7.53 | 18.90 | 29.68 | 2.00 | 126.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 5.84 | 18.36 | 31.02 | 6.00 | 87.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.39 | 16.55 | 26.63 | 5.00 | 108.9 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.15 | 12.60 | 20.45 | 5.00 | 76.1 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.06 | 9.76 | 16.58 | 0.00 | 57.9 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 76.23
- Actual score: 48.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.45) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: João Pedro Junqueira de Jesus -> Jarrod Bowen (projected gain 5.83, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.45) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.81 | 12.81 | 20.32 | 10.00 | 101.0 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.59 | 7.86 | 13.07 | 7.00 | 80.9 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.99 | 18.33 | 28.58 | 4.00 | 128.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.05 | 15.83 | 25.48 | 8.00 | 105.1 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.44 | 13.72 | 22.37 | 0.00 | 100.8 | 0.0 |
| XI | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.36 | 13.52 | 21.97 | 0.00 | 98.3 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.93 | 12.14 | 20.20 | 0.00 | 95.6 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 6.94 | 17.81 | 28.00 | 10.00 | 123.1 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.98 | 11.89 | 18.82 | 0.00 | 82.1 | 0.0 |
| Bench 3 | Bench | Junior Kroupi | FWD | 4 | 4.6 | 2.71 | 8.97 | 15.51 | 0.00 | 59.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.95 | 21.62 | 35.62 | 5.00 | 124.8 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.39 | 16.66 | 27.49 | 0.00 | 91.3 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.26 | 14.25 | 22.87 | 1.00 | 92.1 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.15 | 13.58 | 23.33 | 0.00 | 61.9 | 0.0 |
| Bench 4 | Bench | Anthony Gordon | MID | 15 | 7.3 | 1.34 | 6.47 | 12.70 | 0.00 | 28.6 | 0.0 |