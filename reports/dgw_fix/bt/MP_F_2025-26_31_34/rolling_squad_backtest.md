# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 296.21
- Total actual points: 252.00
- Average predicted points: 74.05
- Average actual points: 63.00
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
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 67.77
- Actual score: 55.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.10 | 11.75 | 14.32 | 2.00 | 88.8 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.6 | 2.35 | 6.66 | 10.69 | 7.00 | 70.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.77 | 16.67 | 26.44 | 3.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.48 | 16.66 | 19.77 | 1.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.89 | 14.56 | 17.79 | -1.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.82 | 14.27 | 17.48 | 4.00 | 86.2 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.58 | 14.11 | 21.54 | 0.00 | 90.0 | 36.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.41 | 24.13 | 29.21 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.58 | 15.48 | 24.68 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.39 | 15.26 | 25.04 | 2.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.67 | 22.56 | 27.74 | 2.00 | 86.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.36 | 22.03 | 35.38 | 13.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | MID | 13 | 8.3 | 0.00 | 18.05 | 24.20 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.19 | 15.47 | 24.45 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.87 | 15.06 | 23.07 | 10.00 | 90.0 | 88.0 |

## GW32

- Train rows: 185188
- Bank: 0.10 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.37
- Actual score: 67.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.50, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.18 | 8.85 | 14.32 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.6 | 2.60 | 7.04 | 11.04 | 3.00 | 72.1 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.58 | 11.89 | 18.02 | 5.00 | 89.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.74 | 11.59 | 19.14 | 9.00 | 76.5 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.67 | 11.05 | 17.65 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.31 | 10.44 | 17.18 | 4.00 | 82.7 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.03 | 9.65 | 15.91 | 4.00 | 82.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.83 | 15.23 | 25.67 | 2.00 | 79.3 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.06 | 13.89 | 22.73 | 14.00 | 88.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.62 | 13.67 | 22.07 | 13.00 | 84.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.01 | 21.59 | 34.70 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.02 | 15.47 | 25.71 | 4.00 | 84.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.38 | 13.66 | 28.21 | 2.00 | 56.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.27 | 12.90 | 20.77 | 5.00 | 79.3 | 90.0 |
| Bench 2 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.41 | 10.27 | 16.41 | 3.00 | 64.5 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.70 -> 0.50
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 112.28
- Actual score: 75.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (21.38) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.63): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: James Hill -> Konstantinos Mavropanos (projected gain 2.25, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (21.38) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 5.44 | 7.91 | 13.10 | 4.00 | 175.1 | 180.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 4.6 | 2.92 | 7.20 | 11.12 | 2.00 | 73.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 10.16 | 13.55 | 20.92 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.89 | 21.34 | 8.00 | 87.1 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.11 | 12.54 | 19.61 | 6.00 | 90.0 | 90.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.41 | 11.27 | 17.23 | 12.00 | 162.1 | 180.0 |
| XI | XI | Adrien Truffert | DEF | 4 | 4.6 | 8.02 | 11.12 | 17.70 | 13.00 | 175.8 | 180.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.87 | 16.17 | 26.41 | 0.00 | 179.8 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.67 | 13.67 | 22.42 | 2.00 | 84.1 | 90.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.5 | 4.20 | 12.96 | 21.45 | 2.00 | 84.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.53 | 19.36 | 32.35 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.46 | 17.36 | 27.98 | 2.00 | 180.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 10.41 | 15.41 | 30.76 | 5.00 | 162.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.37 | 13.06 | 21.03 | 5.00 | 80.8 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 2.99 | 9.71 | 16.38 | 0.00 | 60.2 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.50 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 58.78
- Actual score: 55.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 10.07, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 0.00 | 8.34 | 16.25 | 0.00 | 0.0 | 0.0 |
| XI | XI | Matz Sels | GK | 16 | 4.6 | 2.58 | 7.25 | 11.53 | 7.00 | 75.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.39 | 17.69 | 28.08 | 4.00 | 90.0 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.70 | 13.03 | 20.73 | 4.00 | 90.0 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.00 | 10.32 | 19.92 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 10.09 | 19.60 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 0.00 | 9.86 | 19.04 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.39 | 17.21 | 27.49 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.54 | 16.01 | 25.88 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 8.02 | 17.27 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.46 | 21.22 | 35.32 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 0.00 | 18.35 | 30.30 | 0.00 | 0.0 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.77 | 16.24 | 26.14 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.03 | 14.02 | 22.51 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 10.14 | 20.79 | 0.00 | 0.0 | 0.0 |