# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 279.39
- Total actual points: 212.00
- Average predicted points: 69.85
- Average actual points: 53.00
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
- Predicted score: 61.25
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.80 | 18.19 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.10 | 0.36 | 0.00 | 3.9 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.58 | 16.34 | 25.74 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.72 | 24.83 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.28 | 13.70 | 20.79 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.90 | 11.07 | 17.98 | -1.00 | 86.1 | 90.0 |
| XI | XI | Joe Rodon | DEF | 11 | 3.9 | 3.28 | 8.79 | 14.08 | 6.00 | 80.8 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.28 | 18.24 | 29.14 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.52 | 15.51 | 24.49 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.46 | 15.41 | 25.09 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.10 | 21.44 | 34.66 | 13.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Antoine Semenyo | MID | 13 | 8.3 | 0.00 | 17.34 | 29.09 | 0.00 | 0.0 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.72 | 17.29 | 28.18 | 2.00 | 87.6 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 6.04 | 16.25 | 25.22 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 3.09 | 8.19 | 13.14 | 2.00 | 71.1 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.79
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.59) beats the best remaining Bench Boost opportunity (17.05).
- Transfer: Anthony Gordon -> Dominik Szoboszlai (projected gain 2.35, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.59) beats the best remaining Bench Boost opportunity (17.05).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.26 | 9.43 | 16.22 | 1.00 | 71.3 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.32 | 0.44 | 0.64 | 0.00 | 4.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.02 | 11.78 | 20.31 | 4.00 | 62.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.85 | 11.40 | 18.91 | 9.00 | 77.9 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.60 | 11.03 | 17.55 | 3.00 | 90.0 | 90.0 |
| Bench 3 | Bench Boost | Joe Rodon | DEF | 11 | 3.9 | 3.06 | 9.07 | 14.56 | 0.00 | 81.7 | 0.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 2.07 | 6.70 | 11.32 | 2.00 | 48.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.79 | 15.14 | 25.37 | 2.00 | 77.6 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.10 | 14.03 | 22.90 | 14.00 | 88.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.66 | 13.47 | 21.79 | 13.00 | 84.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.99 | 21.18 | 34.30 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.13 | 15.68 | 25.97 | 4.00 | 85.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.43 | 13.24 | 22.58 | 2.00 | 57.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.37 | 13.10 | 21.22 | 5.00 | 80.6 | 90.0 |
| Bench 2 | Bench Boost | Pape Matar Sarr | MID | 18 | 4.5 | 3.15 | 8.83 | 13.98 | 1.00 | 78.2 | 29.0 |

## GW33

- Train rows: 186014
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Antoine Semenyo
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 103.78
- Actual score: 46.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.87) beats the best remaining Triple Captain opportunity (6.74).
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Malick Thiaw -> Marcos Senesi Barón (projected gain 3.11, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.87) beats the best remaining Triple Captain opportunity (6.74).
- Autosub: Gabriel dos Santos Magalhães replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.04 | 9.54 | 16.02 | 1.00 | 78.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.87 | 14.56 | 21.90 | 6.00 | 180.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.43 | 13.04 | 21.43 | 8.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.73 | 11.99 | 18.45 | 5.00 | 171.7 | 180.0 |
| Bench 2 | Autosub In | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.80 | 11.52 | 19.89 | 0.00 | 71.9 | 90.0 |
| Bench 3 | Bench | Joe Rodon | DEF | 11 | 3.9 | 3.03 | 5.92 | 9.83 | 1.00 | 76.0 | 46.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.68 | 17.48 | 27.68 | 0.00 | 176.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.88 | 14.04 | 22.87 | 2.00 | 87.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.36 | 13.30 | 21.85 | 2.00 | 87.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.71 | 19.28 | 32.06 | 6.00 | 90.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.27 | 18.96 | 29.66 | 2.00 | 180.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 10.73 | 16.89 | 27.14 | 5.00 | 179.6 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.52 | 13.30 | 21.41 | 5.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 2.26 | 6.78 | 11.29 | 0.00 | 53.7 | 0.0 |

## GW34

- Train rows: 186843
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 48.58
- Actual score: 44.00
- Transfer: none
- No transfer was applied this week.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.41 | 12.24 | 19.35 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.05 | 0.14 | 0.27 | 0.00 | 0.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.11 | 17.22 | 26.98 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.71 | 15.40 | 24.78 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.89 | 22.82 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.75 | 19.75 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Joe Rodon | DEF | 11 | 3.9 | 0.00 | 5.22 | 10.05 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.18 | 17.24 | 27.16 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.53 | 16.17 | 25.92 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 11.92 | 21.14 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.29 | 20.90 | 34.58 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 0.00 | 15.86 | 26.36 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 5.03 | 14.09 | 22.69 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 12.43 | 22.19 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Pape Matar Sarr | MID | 18 | 4.5 | 1.04 | 3.03 | 6.68 | 0.00 | 23.0 | 0.0 |