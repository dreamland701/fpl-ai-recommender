# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 285.07
- Total actual points: 226.00
- Average predicted points: 71.27
- Average actual points: 56.50
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
- Predicted score: 61.29
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.75 | 18.22 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.06 | 0.27 | 0.00 | 3.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.56 | 16.30 | 25.72 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.67 | 24.84 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.27 | 13.68 | 20.78 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.93 | 11.13 | 18.00 | -1.00 | 86.9 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 3.9 | 3.23 | 8.71 | 14.03 | 6.00 | 79.5 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.26 | 18.22 | 29.16 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.51 | 15.50 | 24.52 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.43 | 15.37 | 25.07 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.19 | 21.59 | 34.77 | 13.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | MID | 13 | 8.3 | 0.00 | 17.31 | 29.12 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.70 | 17.25 | 28.16 | 2.00 | 87.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 6.04 | 16.26 | 25.23 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 3.02 | 8.07 | 13.03 | 2.00 | 68.9 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 66.35
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.64) beats the best remaining Bench Boost opportunity (17.07).
- Transfer: Anthony Gordon -> Dominik Szoboszlai (projected gain 2.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.64) beats the best remaining Bench Boost opportunity (17.07).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.27 | 9.47 | 16.21 | 1.00 | 71.8 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.31 | 0.43 | 0.57 | 0.00 | 3.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.02 | 11.78 | 20.28 | 4.00 | 62.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.89 | 11.48 | 18.95 | 9.00 | 78.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.64 | 11.11 | 17.59 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Joe Rodon | DEF | 11 | 3.9 | 3.09 | 9.13 | 14.58 | 0.00 | 82.7 | 0.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 2.06 | 6.72 | 11.31 | 2.00 | 48.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.83 | 15.24 | 25.44 | 2.00 | 78.8 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.16 | 14.13 | 22.97 | 14.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.71 | 13.57 | 21.86 | 13.00 | 85.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.08 | 21.34 | 34.42 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.19 | 15.78 | 26.04 | 4.00 | 87.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.41 | 13.23 | 22.52 | 2.00 | 57.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.43 | 13.22 | 21.31 | 5.00 | 82.3 | 90.0 |
| Bench 2 | Bench Boost | Pape Matar Sarr | MID | 18 | 4.5 | 3.18 | 8.90 | 14.00 | 1.00 | 79.0 | 29.0 |

## GW33

- Train rows: 186014
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Antoine Semenyo
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 103.12
- Actual score: 47.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.83) beats the best remaining Triple Captain opportunity (6.71).
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Malick Thiaw -> Marcos Senesi Barón (projected gain 8.03, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.83) beats the best remaining Triple Captain opportunity (6.71).
- Autosub: Joe Rodon replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.97 | 9.43 | 15.94 | 1.00 | 76.4 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.13 | 0.19 | 0.00 | 3.7 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.83 | 14.52 | 21.88 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.39 | 12.98 | 21.41 | 8.00 | 89.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.65 | 11.93 | 18.42 | 5.00 | 169.6 | 180.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.72 | 11.39 | 19.78 | 0.00 | 70.0 | 90.0 |
| Bench 2 | Autosub In | Joe Rodon | DEF | 11 | 3.9 | 3.74 | 6.71 | 10.82 | 1.00 | 91.0 | 46.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.58 | 17.39 | 27.61 | 0.00 | 173.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.84 | 14.00 | 22.89 | 2.00 | 86.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.32 | 13.24 | 21.82 | 2.00 | 86.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.69 | 19.25 | 32.07 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.23 | 18.91 | 29.63 | 2.00 | 180.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 10.67 | 16.83 | 27.10 | 5.00 | 178.0 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.50 | 13.26 | 21.40 | 5.00 | 83.3 | 90.0 |
| Bench 4 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.39 | 7.00 | 11.55 | 0.00 | 58.1 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.10 -> 3.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 54.30
- Actual score: 57.00
- Transfer: Cole Palmer -> Morgan Gibbs-White (projected gain 5.42, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.36 | 12.14 | 19.27 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.18 | 0.33 | 0.49 | 0.00 | 4.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.08 | 17.17 | 26.94 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.65 | 15.29 | 24.69 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 14.10 | 23.02 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.93 | 19.93 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 3.9 | 0.00 | 6.00 | 11.07 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.16 | 17.21 | 27.15 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.50 | 16.13 | 25.91 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 11.79 | 21.12 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.27 | 20.87 | 34.58 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 0.00 | 16.20 | 26.79 | 0.00 | 0.0 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.62 | 16.19 | 25.74 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 5.01 | 14.04 | 22.67 | 1.00 | 89.6 | 90.0 |
| XI | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 1.37 | 3.77 | 7.61 | 0.00 | 29.8 | 0.0 |