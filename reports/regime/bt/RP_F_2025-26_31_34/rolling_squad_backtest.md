# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 284.88
- Total actual points: 226.00
- Average predicted points: 71.22
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
- Predicted score: 63.49
- Actual score: 51.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.75 | 18.19 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.35 | 0.71 | 0.00 | 0.7 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.64 | 16.50 | 26.03 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.55 | 24.68 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.44 | 14.16 | 21.56 | 0.00 | 90.0 | 36.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.89 | 11.00 | 17.79 | -1.00 | 86.8 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.78 | 10.83 | 17.66 | 4.00 | 85.1 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.23 | 18.06 | 28.91 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.49 | 15.39 | 24.34 | 4.00 | 90.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.39 | 15.18 | 24.70 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.30 | 21.86 | 35.21 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.82 | 17.66 | 28.94 | 2.00 | 88.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.17 | 15.55 | 24.33 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.81 | 15.50 | 23.78 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.1 | 4.09 | 11.24 | 17.87 | 2.00 | 80.6 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.11
- Actual score: 68.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 0.98, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.96 | 8.83 | 15.15 | 1.00 | 57.7 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.25 | 0.56 | 0.87 | 0.00 | 2.4 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.54 | 12.01 | 18.20 | 5.00 | 88.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.97 | 11.65 | 20.13 | 4.00 | 63.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.77 | 11.16 | 18.55 | 9.00 | 78.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.64 | 11.07 | 17.53 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.08 | 9.81 | 16.24 | 4.00 | 83.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.70 | 14.80 | 24.77 | 2.00 | 78.0 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.13 | 13.96 | 22.64 | 14.00 | 88.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.59 | 13.17 | 21.23 | 13.00 | 84.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.11 | 21.42 | 34.63 | 4.00 | 90.0 | 90.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.22 | 15.93 | 26.39 | 4.00 | 87.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.39 | 13.08 | 21.11 | 5.00 | 80.4 | 90.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.0 | 3.61 | 11.10 | 17.58 | 12.00 | 83.5 | 90.0 |
| Bench 3 | Bench | Anthony Gordon | MID | 15 | 7.3 | 3.61 | 10.84 | 17.50 | 3.00 | 68.6 | 70.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 104.59
- Actual score: 56.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.83) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Adrien Truffert -> Marcos Senesi Barón (projected gain 2.34, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.83) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.95 | 9.37 | 15.87 | 1.00 | 73.3 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.12 | 0.41 | 0.70 | 0.00 | 2.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.93 | 14.64 | 22.06 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.34 | 13.00 | 19.28 | 12.00 | 160.6 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.26 | 12.65 | 20.96 | 8.00 | 89.4 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.63 | 11.89 | 18.36 | 5.00 | 169.9 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.64 | 11.19 | 19.53 | 0.00 | 69.5 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.39 | 17.05 | 27.06 | 0.00 | 172.8 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.69 | 13.53 | 22.14 | 2.00 | 85.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 4.26 | 12.98 | 21.35 | 2.00 | 84.3 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.50 | 19.33 | 30.35 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.67 | 19.21 | 32.12 | 6.00 | 90.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.15 | 13.88 | 21.14 | 5.00 | 180.0 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.46 | 13.12 | 21.18 | 5.00 | 81.3 | 90.0 |
| Bench 4 | Bench Boost | Anthony Gordon | MID | 15 | 7.3 | 3.11 | 10.22 | 17.32 | 0.00 | 62.6 | 0.0 |

## GW34

- Train rows: 186843
- Bank: -0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 59.69
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.87) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Anthony Gordon -> Declan Rice (projected gain 6.18, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.87) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.46 | 12.38 | 19.61 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.26 | 0.61 | 1.00 | 0.00 | 2.5 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.14 | 17.30 | 27.14 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.71 | 15.43 | 24.88 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 0.00 | 13.45 | 22.01 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.43 | 21.88 | 0.00 | 0.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.93 | 19.92 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.26 | 17.33 | 27.22 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.46 | 15.95 | 25.59 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.04 | 18.33 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.37 | 21.11 | 34.97 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 14.15 | 24.30 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.03 | 14.07 | 22.69 | 1.00 | 88.6 | 90.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 13.48 | 21.76 | 0.00 | 0.0 | 0.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.52 | 12.90 | 21.24 | 2.00 | 85.4 | 90.0 |