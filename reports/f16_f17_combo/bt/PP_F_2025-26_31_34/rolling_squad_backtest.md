# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 294.43
- Total actual points: 277.00
- Average predicted points: 73.61
- Average actual points: 69.25
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
- Predicted score: 63.25
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 0.00 | 10.78 | 18.37 | 0.00 | 0.0 | 0.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.00 | 0.13 | 0.39 | 0.00 | 3.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.71 | 16.79 | 26.57 | 3.00 | 90.0 | 90.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 0.00 | 14.38 | 24.41 | 0.00 | 0.0 | 0.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.30 | 13.68 | 20.68 | 0.00 | 90.0 | 36.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.4 | 3.83 | 10.75 | 16.87 | 4.00 | 88.6 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.83 | 10.62 | 17.03 | -1.00 | 81.8 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.29 | 18.26 | 29.28 | 2.00 | 90.0 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.42 | 15.32 | 24.98 | 2.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.46 | 15.23 | 24.00 | 4.00 | 90.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.25 | 21.69 | 34.91 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.73 | 17.39 | 28.50 | 2.00 | 89.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.20 | 15.64 | 24.51 | 3.00 | 90.0 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.80 | 15.50 | 23.81 | 10.00 | 90.0 | 88.0 |
| Bench 2 | Bench | Alex Scott | MID | 4 | 5.1 | 4.07 | 11.09 | 17.57 | 2.00 | 79.1 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.20 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 67.26
- Actual score: 84.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.21) beats the best remaining Bench Boost opportunity (17.94).
- Transfer: Anthony Gordon -> Morgan Gibbs-White (projected gain 1.82, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.21) beats the best remaining Bench Boost opportunity (17.94).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.00 | 9.01 | 15.55 | 1.00 | 63.0 | 90.0 |
| Bench 1 | Bench Boost | Ármin Pécsi | GK | 12 | 3.8 | 0.15 | 0.32 | 0.54 | 0.00 | 5.0 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.4 | 4.59 | 12.24 | 18.66 | 5.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.98 | 11.61 | 20.05 | 4.00 | 61.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.86 | 11.50 | 19.17 | 9.00 | 80.9 | 90.0 |
| Bench 3 | Bench Boost | James Hill | DEF | 4 | 4.2 | 3.57 | 10.72 | 16.80 | 3.00 | 89.1 | 90.0 |
| Bench 4 | Bench Boost | Malick Thiaw | DEF | 15 | 5.1 | 1.90 | 6.22 | 10.52 | 2.00 | 43.4 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.78 | 15.05 | 25.22 | 2.00 | 77.9 | 81.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.5 | 5.16 | 14.13 | 23.01 | 14.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.57 | 13.01 | 20.89 | 13.00 | 80.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.06 | 21.23 | 34.29 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.16 | 15.69 | 25.98 | 4.00 | 87.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.41 | 13.17 | 21.30 | 5.00 | 82.8 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.4 | 4.43 | 12.71 | 20.38 | 2.00 | 84.2 | 83.0 |
| Bench 2 | Bench Boost | Alex Scott | MID | 4 | 5.0 | 3.59 | 10.95 | 17.28 | 12.00 | 81.7 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Cole Palmer
- Chip used: triple_captain
- Predicted score: 105.74
- Actual score: 76.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (16.96) beats the best remaining Triple Captain opportunity (6.60).
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Malick Thiaw -> Marcos Senesi Barón (projected gain 1.52, hit 0)
- Chip used: Triple Captain on Cole Palmer. Optimizer chose Triple Captain here because the current estimated captain upside (16.96) beats the best remaining Triple Captain opportunity (6.60).
- Autosub: Virgil van Dijk replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.98 | 9.51 | 16.19 | 1.00 | 78.8 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.01 | 0.18 | 0.37 | 0.00 | 4.6 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 9.87 | 14.39 | 21.52 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.47 | 13.24 | 19.71 | 12.00 | 167.4 | 180.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.3 | 4.34 | 12.93 | 21.45 | 8.00 | 90.0 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 7.52 | 11.51 | 17.58 | 5.00 | 161.8 | 180.0 |
| Bench 4 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.63 | 11.08 | 19.32 | 0.00 | 68.4 | 90.0 |
| Vice Captain | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.57 | 17.30 | 27.45 | 0.00 | 173.1 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.67 | 13.35 | 21.75 | 2.00 | 80.6 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | 19 | 7.5 | 4.31 | 13.16 | 21.72 | 2.00 | 87.0 | 90.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.36 | 19.03 | 29.82 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.60 | 18.99 | 31.74 | 6.00 | 90.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 9.13 | 13.73 | 20.81 | 5.00 | 180.0 | 180.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.47 | 13.16 | 21.28 | 5.00 | 83.2 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.4 | 4.40 | 11.79 | 19.02 | 20.00 | 76.8 | 88.0 |

## GW34

- Train rows: 186843
- Bank: -0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.18
- Actual score: 61.00
- Transfer: Marcos Senesi Barón -> Konstantinos Mavropanos (projected gain 2.71, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.48 | 12.53 | 19.98 | 10.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Ármin Pécsi | GK | 12 | 3.8 | 0.16 | 0.37 | 0.66 | 0.00 | 5.0 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.20 | 17.53 | 27.54 | 4.00 | 90.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.71 | 15.37 | 24.77 | 8.00 | 90.0 | 90.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 13.48 | 22.02 | 0.00 | 0.0 | 0.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.68 | 12.96 | 20.49 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 11.45 | 19.05 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.6 | 6.30 | 17.55 | 27.67 | 10.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.43 | 15.74 | 25.15 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 10.37 | 18.98 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.31 | 20.91 | 34.63 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.4 | 5.73 | 16.43 | 26.12 | 13.00 | 90.0 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.03 | 14.10 | 22.78 | 1.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 13.87 | 23.89 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 0.00 | 13.23 | 21.35 | 0.00 | 0.0 | 0.0 |