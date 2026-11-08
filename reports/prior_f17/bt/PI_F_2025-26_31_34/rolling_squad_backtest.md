# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 283.89
- Total actual points: 235.00
- Average predicted points: 70.97
- Average actual points: 58.75
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
- Predicted score: 63.19
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.78 | 18.25 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.65 | 16.50 | 25.98 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.16 | 24.09 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.39 | 13.95 | 21.16 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.94 | 11.18 | 18.12 | -1.00 | 86.9 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.78 | 10.82 | 17.62 | 4.00 | 84.5 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.23 | 18.12 | 29.06 | 2.00 | 90.0 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.53 | 15.63 | 25.47 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.50 | 15.47 | 24.51 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.28 | 21.80 | 35.11 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.43 | 16.52 | 27.08 | 2.00 | 88.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.25 | 15.78 | 24.72 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.71 | 15.17 | 23.21 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.1 | 4.15 | 11.44 | 18.23 | 2.00 | 81.8 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 1.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.60
- Actual score: 67.00
- Transfer: Anthony Gordon -> Elliot Anderson (projected gain 0.84, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.96 | 8.84 | 15.17 | 1.00 | 59.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.13 | 0.22 | 0.00 | 4.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.81 | 11.23 | 19.49 | 4.00 | 63.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.80 | 11.22 | 18.61 | 9.00 | 77.2 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.67 | 11.22 | 17.79 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.08 | 9.78 | 16.15 | 4.00 | 82.9 | 90.0 |
| Bench 4 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 1.97 | 6.47 | 10.99 | 2.00 | 46.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.71 | 14.91 | 25.01 | 2.00 | 78.6 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.25 | 14.36 | 23.33 | 14.00 | 89.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.65 | 13.39 | 21.64 | 13.00 | 85.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.06 | 21.28 | 34.40 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.87 | 14.93 | 24.77 | 4.00 | 87.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.44 | 13.23 | 21.37 | 5.00 | 81.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.31 | 12.09 | 19.57 | 4.00 | 82.9 | 90.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.0 | 3.66 | 11.27 | 17.88 | 12.00 | 84.6 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 1.80 -> 0.80
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 99.99
- Actual score: 55.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.79) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: James Hill -> Marcos Senesi Barón (projected gain 2.68, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.79) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.95 | 9.36 | 15.85 | 1.00 | 75.3 | 90.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.07 | 1.35 | 1.60 | 0.00 | 7.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.97 | 14.69 | 22.11 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.31 | 12.78 | 21.14 | 8.00 | 88.0 | 90.0 |
| XI | XI | Adrien Truffert | DEF | 4 | 4.6 | 7.98 | 12.27 | 19.00 | 13.00 | 173.0 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.48 | 10.75 | 18.87 | 0.00 | 69.6 | 90.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 3.14 | 9.28 | 15.14 | 1.00 | 75.2 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.46 | 17.23 | 27.41 | 0.00 | 174.2 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.78 | 13.82 | 22.67 | 2.00 | 85.9 | 90.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.5 | 4.41 | 13.44 | 22.14 | 2.00 | 85.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.60 | 19.01 | 31.79 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 11.83 | 18.34 | 28.75 | 2.00 | 180.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.26 | 14.06 | 21.44 | 5.00 | 180.0 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.51 | 13.28 | 21.46 | 5.00 | 82.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.41 | 11.50 | 18.37 | 2.00 | 77.8 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.80 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 64.11
- Actual score: 62.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.83) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Malick Thiaw -> Konstantinos Mavropanos (projected gain 4.04, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.83) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.45 | 12.34 | 19.55 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.20 | 17.40 | 27.26 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.57 | 15.05 | 24.30 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.53 | 22.12 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 0.00 | 12.99 | 21.22 | 0.00 | 0.0 | 0.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.66 | 12.92 | 20.44 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.40 | 17.80 | 28.01 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.57 | 16.28 | 26.16 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.17 | 18.62 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.33 | 21.00 | 34.78 | 5.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.08 | 14.22 | 22.95 | 1.00 | 89.7 | 90.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 13.69 | 22.14 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.14 | 22.68 | 0.00 | 0.0 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.20 | 12.02 | 19.12 | 9.00 | 83.5 | 90.0 |