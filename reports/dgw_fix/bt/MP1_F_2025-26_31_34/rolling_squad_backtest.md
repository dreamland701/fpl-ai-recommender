# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 286.60
- Total actual points: 226.00
- Average predicted points: 71.65
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
- Predicted score: 64.08
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.84 | 18.38 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.04 | 0.00 | 2.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.77 | 16.81 | 26.49 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.58 | 24.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.58 | 14.44 | 21.92 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.89 | 11.04 | 17.89 | -1.00 | 86.3 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.82 | 10.92 | 17.79 | 4.00 | 86.2 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.41 | 18.57 | 29.75 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.58 | 15.67 | 24.83 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.39 | 15.27 | 24.95 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.36 | 22.01 | 35.43 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.67 | 17.17 | 28.07 | 2.00 | 86.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.19 | 15.64 | 24.52 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.87 | 15.57 | 23.83 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.1 | 4.10 | 11.32 | 18.05 | 2.00 | 81.8 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.73
- Actual score: 68.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 1.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.93 | 8.87 | 15.22 | 1.00 | 59.9 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.20 | 0.19 | 0.17 | 0.00 | 1.6 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.58 | 12.11 | 18.35 | 5.00 | 89.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.98 | 11.75 | 20.26 | 4.00 | 62.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.67 | 11.17 | 17.69 | 3.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.74 | 11.12 | 18.47 | 9.00 | 76.5 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.03 | 9.69 | 16.04 | 4.00 | 82.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.83 | 15.24 | 25.51 | 2.00 | 79.3 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.06 | 13.88 | 22.60 | 14.00 | 88.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.62 | 13.34 | 21.57 | 13.00 | 84.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.01 | 21.16 | 34.20 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.02 | 15.38 | 25.47 | 4.00 | 84.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.27 | 12.80 | 20.69 | 5.00 | 79.3 | 90.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.0 | 3.64 | 11.19 | 17.77 | 12.00 | 84.7 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.41 | 10.28 | 16.57 | 3.00 | 64.5 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 105.01
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.58) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Adrien Truffert -> Marcos Senesi Barón (projected gain 2.59, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.58) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.98 | 9.44 | 16.01 | 1.00 | 76.7 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 10.16 | 14.92 | 22.47 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.41 | 13.06 | 19.35 | 12.00 | 162.1 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 4.24 | 12.61 | 20.89 | 8.00 | 87.1 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.72 | 11.99 | 18.52 | 5.00 | 171.0 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.68 | 11.30 | 19.69 | 0.00 | 69.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.87 | 17.73 | 28.18 | 0.00 | 179.8 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.67 | 13.57 | 22.28 | 2.00 | 84.1 | 90.0 |
| Bench 2 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.5 | 4.20 | 12.92 | 21.36 | 2.00 | 84.3 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.46 | 19.18 | 30.05 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.53 | 18.85 | 31.54 | 6.00 | 90.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.26 | 14.05 | 21.43 | 5.00 | 180.0 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.37 | 12.91 | 20.89 | 5.00 | 80.8 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 2.99 | 9.85 | 16.71 | 0.00 | 60.2 | 0.0 |

## GW34

- Train rows: 186843
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 60.78
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anthony Gordon -> Declan Rice (projected gain 7.00, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.96) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.62 | 12.79 | 20.31 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.09 | 0.10 | 0.18 | 0.00 | 3.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.39 | 17.92 | 28.08 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.87 | 15.84 | 25.50 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.76 | 22.43 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.54 | 22.00 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 12.18 | 20.26 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.39 | 17.77 | 27.98 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.54 | 16.21 | 26.06 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.22 | 18.68 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.46 | 21.33 | 35.30 | 5.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.03 | 14.08 | 22.72 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 13.58 | 21.90 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.57 | 23.32 | 0.00 | 0.0 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.55 | 13.03 | 21.48 | 2.00 | 85.7 | 90.0 |