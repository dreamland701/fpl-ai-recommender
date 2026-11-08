# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 293.08
- Total actual points: 265.00
- Average predicted points: 73.27
- Average actual points: 66.25
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 63.18
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.88 | 18.43 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.04 | 0.22 | 0.00 | 3.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.73 | 16.84 | 26.62 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.44 | 24.43 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.27 | 13.63 | 20.61 | 0.00 | 90.0 | 36.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.4 | 3.89 | 10.84 | 16.96 | 4.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.78 | 10.52 | 16.95 | -1.00 | 80.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.31 | 18.28 | 29.25 | 2.00 | 90.0 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.46 | 15.38 | 25.03 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.46 | 15.20 | 23.93 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.14 | 21.48 | 34.73 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.76 | 17.46 | 28.55 | 2.00 | 89.8 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.20 | 15.63 | 24.49 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.80 | 15.49 | 23.77 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.1 | 4.01 | 10.97 | 17.47 | 2.00 | 77.5 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.53
- Actual score: 67.00
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 1.84, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.03 | 9.06 | 15.65 | 1.00 | 63.7 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.31 | 0.37 | 0.49 | 0.00 | 3.6 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.4 | 4.53 | 12.14 | 18.59 | 5.00 | 89.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.00 | 11.63 | 20.11 | 4.00 | 62.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.85 | 11.47 | 19.17 | 9.00 | 80.5 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.51 | 10.58 | 16.69 | 3.00 | 87.5 | 90.0 |
| Bench 4 | Bench | Malick Thiaw | DEF | 15 | 5.1 | 1.90 | 6.19 | 10.51 | 2.00 | 43.5 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.74 | 14.95 | 25.14 | 2.00 | 76.8 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.11 | 14.03 | 22.94 | 14.00 | 89.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.50 | 12.86 | 20.74 | 13.00 | 78.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.97 | 21.05 | 34.12 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.11 | 15.61 | 25.93 | 4.00 | 85.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.35 | 13.05 | 21.20 | 5.00 | 81.2 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.4 | 4.38 | 12.62 | 20.33 | 2.00 | 82.9 | 83.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.0 | 3.53 | 10.85 | 17.21 | 12.00 | 80.4 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 106.66
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (19.22) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Malick Thiaw -> Marcos Senesi Barón (projected gain 1.42, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (19.22) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.08 | 9.71 | 16.39 | 1.00 | 81.3 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.89 | 14.41 | 21.51 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.55 | 13.31 | 19.76 | 12.00 | 169.6 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.41 | 13.06 | 21.55 | 8.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.58 | 11.55 | 17.59 | 5.00 | 163.5 | 180.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.74 | 11.28 | 19.53 | 0.00 | 71.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.69 | 17.41 | 27.55 | 0.00 | 176.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.70 | 13.37 | 21.72 | 2.00 | 81.5 | 90.0 |
| Bench 3 | Bench Boost | Jarrod Bowen | FWD | 19 | 7.5 | 4.37 | 13.27 | 21.81 | 2.00 | 88.4 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.43 | 19.11 | 29.89 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.65 | 19.05 | 31.76 | 6.00 | 90.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.17 | 13.76 | 20.80 | 5.00 | 180.0 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.51 | 13.23 | 21.32 | 5.00 | 84.1 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.4 | 4.46 | 11.90 | 19.11 | 20.00 | 78.3 | 88.0 |

## GW34

- Train rows: 186843
- Bank: -0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 65.71
- Actual score: 66.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.83) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Marcos Senesi Barón -> Konstantinos Mavropanos (projected gain 3.01, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.83) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.55 | 12.68 | 20.13 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.06 | 0.10 | 0.17 | 0.00 | 0.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.24 | 17.60 | 27.60 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.77 | 15.50 | 24.90 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.30 | 21.83 | 0.00 | 0.0 | 0.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.71 | 13.01 | 20.52 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.20 | 18.78 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.31 | 17.58 | 27.68 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.43 | 15.73 | 25.10 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.54 | 19.08 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.33 | 20.94 | 34.64 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.4 | 5.65 | 16.29 | 26.03 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.06 | 14.16 | 22.83 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.99 | 24.40 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 12.97 | 21.06 | 0.00 | 0.0 | 0.0 |