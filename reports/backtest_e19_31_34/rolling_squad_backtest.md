# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW31-GW34
- Total predicted points: 210.10
- Total actual points: 212.00
- Average predicted points: 52.52
- Average actual points: 53.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW26 are included before the first simulated week.
- League-average scores were not available for this run.

## GW31

- Train rows: 184363
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 47.74
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Adrien Truffert.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.18 | 8.30 | 14.40 | 0.00 | 53.5 | 0.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.89 | 7.98 | 13.25 | 2.00 | 89.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.80 | 12.29 | 20.51 | 3.00 | 90.8 | 90.0 |
| Bench 3 | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.00 | 10.79 | 19.30 | 0.00 | 59.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.75 | 10.61 | 17.18 | 1.00 | 88.7 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.45 | 10.27 | 16.49 | -1.00 | 89.7 | 90.0 |
| Bench 2 | Autosub In | Adrien Truffert | DEF | 4 | 4.6 | 3.24 | 9.37 | 15.06 | 4.00 | 86.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.62 | 13.93 | 23.24 | 2.00 | 88.6 | 77.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.76 | 11.25 | 19.35 | 2.00 | 89.2 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 2.80 | 8.07 | 12.87 | 5.00 | 69.1 | 8.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 5.20 | 16.02 | 26.59 | 13.00 | 106.3 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.01 | 13.10 | 21.09 | 3.00 | 91.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 3.86 | 12.70 | 21.35 | 2.00 | 76.3 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 3.36 | 12.41 | 21.75 | 0.00 | 50.3 | 0.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 3.83 | 11.26 | 17.24 | 2.00 | 91.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 53.84
- Actual score: 59.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.14) beats the best remaining Triple Captain opportunity (15.01).
- Transfer: Pascal Groß -> Jaidon Anthony (projected gain 0.60, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.14) beats the best remaining Triple Captain opportunity (15.01).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 2.59 | 8.11 | 13.79 | 1.00 | 68.7 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 2.77 | 8.02 | 12.89 | 2.00 | 89.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.95 | 12.70 | 20.04 | 9.00 | 90.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.24 | 10.49 | 18.39 | 4.00 | 70.6 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 2.85 | 9.38 | 15.14 | 3.00 | 88.8 | 90.0 |
| Bench 2 | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 2.57 | 8.50 | 13.66 | 4.00 | 85.7 | 90.0 |
| Bench 3 | Bench | Adrien Truffert | DEF | 4 | 4.6 | 2.38 | 7.62 | 12.69 | 4.00 | 85.3 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.28 | 12.89 | 21.78 | 2.00 | 67.1 | 81.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.5 | 3.85 | 11.47 | 18.34 | 14.00 | 86.4 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 1.85 | 6.99 | 11.85 | 1.00 | 32.6 | 10.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.14 | 18.35 | 29.52 | 4.00 | 110.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.01 | 13.17 | 21.96 | 4.00 | 87.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.3 | 3.86 | 12.43 | 21.33 | 2.00 | 66.1 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.40 | 9.97 | 16.13 | 5.00 | 66.2 | 90.0 |
| XI | XI | Jaidon Anthony | MID | 3 | 5.0 | 3.21 | 9.97 | 15.19 | 2.00 | 85.6 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Cole Palmer
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 63.99
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (18.55) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Adrien Truffert -> Marc Guéhi (projected gain 1.67, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (18.55) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 2.83 | 9.34 | 15.81 | 1.00 | 82.2 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.00 | 7.56 | 12.34 | 4.00 | 133.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.76 | 12.15 | 20.59 | 8.00 | 92.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.07 | 10.09 | 16.20 | 8.00 | 129.0 | 180.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.20 | 9.96 | 15.23 | 6.00 | 131.5 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.17 | 9.47 | 17.10 | 0.00 | 57.8 | 90.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 3.95 | 9.03 | 14.24 | 5.00 | 130.4 | 180.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 4.51 | 12.57 | 21.25 | 0.00 | 92.8 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 3.67 | 12.40 | 20.89 | 2.00 | 89.9 | 90.0 |
| Bench 4 | Bench Boost | Raúl Jiménez Rodríguez | FWD | 10 | 6.2 | 1.66 | 5.28 | 9.10 | 1.00 | 22.3 | 23.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 5.97 | 18.77 | 32.21 | 6.00 | 101.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.84 | 12.88 | 21.40 | 5.00 | 97.6 | 154.0 |
| Vice Captain | XI | Cole Palmer | MID | 7 | 10.6 | 5.15 | 12.41 | 20.73 | 2.00 | 100.8 | 90.0 |
| Bench 2 | Bench Boost | Dominik Szoboszlai | MID | 12 | 7.1 | 3.29 | 9.58 | 16.16 | 5.00 | 65.7 | 90.0 |
| XI | XI | Jaidon Anthony | MID | 3 | 5.0 | 3.97 | 9.08 | 14.49 | 4.00 | 95.7 | 168.0 |

## GW34

- Train rows: 186843
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 44.53
- Actual score: 44.00
- Transfer: João Pedro Junqueira de Jesus -> Igor Thiago Nascimento Rodrigues (projected gain 1.82, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.20 | 9.38 | 15.46 | 0.00 | 86.3 | 0.0 |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.91 | 9.05 | 14.97 | 10.00 | 81.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 3.93 | 12.26 | 20.99 | 4.00 | 95.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.57 | 11.51 | 19.37 | 8.00 | 81.4 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.05 | 10.72 | 17.80 | 0.00 | 79.8 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 3.02 | 10.59 | 17.10 | 0.00 | 84.0 | 0.0 |
| XI | Bench | James Hill | DEF | 4 | 4.2 | 2.67 | 8.66 | 14.88 | 0.00 | 77.3 | 0.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.99 | 12.84 | 21.45 | 1.00 | 87.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.6 | 3.86 | 11.35 | 19.01 | 10.00 | 85.1 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.1 | 1.75 | 4.97 | 8.66 | 2.00 | 25.0 | 65.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 5.08 | 15.71 | 27.41 | 5.00 | 98.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 3.44 | 12.92 | 21.97 | 0.00 | 66.6 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 3.94 | 11.45 | 18.49 | 1.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Cole Palmer | MID | 7 | 10.5 | 2.53 | 11.43 | 20.17 | 0.00 | 39.0 | 0.0 |
| Bench 3 | Bench | Jaidon Anthony | MID | 3 | 5.0 | 2.51 | 10.30 | 17.31 | 0.00 | 70.4 | 0.0 |