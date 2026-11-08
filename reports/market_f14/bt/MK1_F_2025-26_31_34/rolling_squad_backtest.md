# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 280.42
- Total actual points: 221.00
- Average predicted points: 70.10
- Average actual points: 55.25
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 66.67
- Actual score: 66.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 3.54 | 9.79 | 15.56 | 6.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.04 | 0.20 | 0.00 | 2.3 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.68 | 16.84 | 26.65 | 3.00 | 90.0 | 90.0 |
| XI | XI | Malick Thiaw | DEF | 15 | 5.1 | 5.77 | 14.98 | 22.54 | 0.00 | 90.0 | 36.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.24 | 12.33 | 19.61 | 1.00 | 90.0 | 90.0 |
| Bench 3 | Bench | James Hill | DEF | 4 | 4.2 | 3.73 | 10.97 | 17.90 | -1.00 | 86.6 | 90.0 |
| Bench 4 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 3.64 | 10.82 | 17.79 | 4.00 | 86.8 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.26 | 17.99 | 29.27 | 2.00 | 90.0 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.43 | 15.18 | 24.53 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Hugo Ekitiké | FWD | 12 | 9.2 | 4.62 | 14.71 | 24.31 | 1.00 | 71.9 | 7.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.14 | 21.65 | 34.99 | 13.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.59 | 16.87 | 27.85 | 2.00 | 88.1 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 5.97 | 15.80 | 23.91 | 10.00 | 90.0 | 88.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.06 | 15.54 | 24.49 | 3.00 | 90.0 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.84 | 12.53 | 20.32 | 9.00 | 82.6 | 86.0 |

## GW32

- Train rows: 185188
- Bank: 0.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 53.71
- Actual score: 56.00
- Transfer: Malick Thiaw -> Jan Paul van Hecke (projected gain 2.66, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.58 | 7.74 | 12.82 | 0.00 | 79.8 | 0.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.12 | 0.00 | 0.00 | 0.00 | 2.4 | 0.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 4.60 | 12.28 | 18.62 | 5.00 | 89.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.88 | 11.84 | 19.38 | 9.00 | 74.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.47 | 10.72 | 17.24 | 3.00 | 90.0 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.12 | 10.02 | 16.69 | 4.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 2.86 | 9.35 | 15.72 | 4.00 | 83.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.58 | 14.70 | 25.13 | 2.00 | 81.9 | 81.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.73 | 13.48 | 21.79 | 13.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Hugo Ekitiké | FWD | 12 | 9.2 | 3.05 | 10.10 | 17.64 | 0.00 | 34.6 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.10 | 21.42 | 34.19 | 4.00 | 90.0 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.69 | 14.71 | 24.78 | 4.00 | 85.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.29 | 13.21 | 21.19 | 5.00 | 77.9 | 90.0 |
| XI | XI | Anthony Gordon | MID | 15 | 7.3 | 3.59 | 10.70 | 17.20 | 3.00 | 64.1 | 70.0 |
| Bench 4 | Bench | Harry Wilson | MID | 10 | 6.0 | 2.79 | 8.83 | 15.22 | 2.00 | 59.6 | 79.0 |

## GW33

- Train rows: 186014
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Antoine Semenyo
- Effective captain: Cole Palmer
- Chip used: bench_boost
- Predicted score: 107.90
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.57) beats the best remaining Bench Boost opportunity (0.00).
- Chip advisory: triple_captain (0.69): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Anthony Gordon -> Antoine Semenyo (projected gain 4.99, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.57) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 1.85 | 5.48 | 9.23 | 2.00 | 42.7 | 90.0 |
| Bench 1 | Bench Boost | Tom Heaton | GK | 14 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.8 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 10.35 | 16.13 | 24.31 | 6.00 | 180.0 | 180.0 |
| XI | XI | Jan Paul van Hecke | DEF | 6 | 4.5 | 8.67 | 13.95 | 20.58 | 12.00 | 158.4 | 180.0 |
| XI | XI | Adrien Truffert | DEF | 4 | 4.6 | 8.37 | 13.73 | 20.99 | 13.00 | 168.9 | 180.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 8.13 | 13.45 | 20.49 | 5.00 | 164.1 | 180.0 |
| Bench 2 | Bench Boost | Virgil van Dijk | DEF | 12 | 6.3 | 4.33 | 12.83 | 21.18 | 8.00 | 86.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 10.77 | 17.98 | 27.82 | 0.00 | 172.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.72 | 13.80 | 22.51 | 2.00 | 83.2 | 90.0 |
| Bench 4 | Bench Boost | Hugo Ekitiké | FWD | 12 | 9.2 | 0.96 | 4.33 | 10.00 | 0.00 | 3.0 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 7 | 10.5 | 12.48 | 19.76 | 30.63 | 2.00 | 180.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.13 | 17.91 | 30.81 | 6.00 | 90.0 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 11.12 | 17.67 | 27.45 | 5.00 | 153.2 | 154.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.40 | 13.01 | 21.02 | 5.00 | 80.6 | 90.0 |
| Bench 3 | Bench Boost | Harry Wilson | MID | 10 | 6.0 | 3.13 | 9.55 | 15.93 | 3.00 | 69.1 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Ollie Watkins
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 52.13
- Actual score: 28.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.78) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Hugo Ekitiké -> Ollie Watkins (projected gain 13.28, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.78) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.1 | 2.59 | 7.65 | 12.54 | 3.00 | 73.5 | 90.0 |
| Bench 1 | Bench | Tom Heaton | GK | 14 | 3.8 | 0.09 | 0.00 | 0.05 | 0.00 | 3.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 6.32 | 18.15 | 28.45 | 4.00 | 90.0 | 90.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 0.00 | 11.66 | 19.89 | 0.00 | 0.0 | 0.0 |
| XI | Bench | Adrien Truffert | DEF | 4 | 4.6 | 0.00 | 11.24 | 19.27 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Jan Paul van Hecke | DEF | 6 | 4.5 | 0.00 | 11.18 | 19.09 | 0.00 | 0.0 | 0.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 0.00 | 10.14 | 17.78 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Ollie Watkins | FWD | 2 | 8.7 | 6.46 | 17.65 | 27.35 | 2.00 | 90.0 | 79.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.24 | 15.65 | 25.74 | 1.00 | 90.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 0.00 | 9.31 | 18.51 | 0.00 | 0.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.28 | 20.97 | 34.78 | 5.00 | 90.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 0.00 | 14.58 | 25.19 | 0.00 | 0.0 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 5.05 | 14.54 | 23.31 | 1.00 | 88.9 | 90.0 |
| XI | XI | Harry Wilson | MID | 10 | 6.0 | 4.61 | 12.41 | 19.75 | 2.00 | 90.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 0.00 | 11.72 | 21.50 | 0.00 | 0.0 | 0.0 |