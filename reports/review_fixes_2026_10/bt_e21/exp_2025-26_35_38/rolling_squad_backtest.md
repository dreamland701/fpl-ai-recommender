# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 231.80
- Total actual points: 244.00
- Average predicted points: 57.95
- Average actual points: 61.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW34 are included before the first simulated week.
- League-average scores were not available for this run.

## GW35

- Train rows: 187673
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 51.88
- Actual score: 36.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Virgil van Dijk replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.26 | 9.63 | 15.03 | 6.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.18 | 7.58 | 12.96 | 3.00 | 80.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.68 | 12.52 | 19.42 | 6.00 | 91.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.81 | 10.44 | 15.08 | 0.00 | 84.5 | 45.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | 12 | 6.2 | 3.39 | 10.25 | 16.94 | 1.00 | 78.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.11 | 10.07 | 15.45 | 1.00 | 42.7 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.8 | 3.45 | 9.62 | 14.37 | 1.00 | 76.5 | 45.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.56 | 9.45 | 14.21 | 5.00 | 70.3 | 45.0 |
| Bench 3 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 3.18 | 8.63 | 12.96 | 1.00 | 76.0 | 64.0 |
| Bench 4 | Bench | Adam Armstrong | FWD | 20 | 5.2 | 2.81 | 7.46 | 12.00 | 2.00 | 65.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.96 | 16.57 | 26.77 | 5.00 | 101.0 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.29 | 12.62 | 20.64 | 0.00 | 43.5 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.20 | 11.76 | 18.13 | 1.00 | 79.5 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.26 | 11.59 | 17.75 | 4.00 | 90.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.37 | 11.38 | 16.94 | 1.00 | 84.0 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Nico O'Reilly
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 62.80
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.14) beats the best remaining Triple Captain opportunity (8.27).
- Transfer: Daniel Muñoz Mejía -> Marcos Senesi Barón (projected gain 2.48, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (9.14) beats the best remaining Triple Captain opportunity (8.27).
- Autosub: Neco Williams replaced Carlos Henrique Casimiro.
- Autosub: Adam Armstrong replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.79 | 9.99 | 15.51 | 9.00 | 86.8 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.50 | 7.62 | 12.98 | 3.00 | 81.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.95 | 13.25 | 20.52 | 11.00 | 92.1 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.25 | 11.35 | 17.13 | 8.00 | 89.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.38 | 11.20 | 17.66 | 2.00 | 85.7 | 90.0 |
| Vice Captain | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.53 | 10.92 | 15.47 | 5.00 | 79.6 | 90.0 |
| Bench 2 | Autosub In | Neco Williams | DEF | 16 | 4.8 | 2.81 | 8.22 | 13.74 | 2.00 | 60.1 | 90.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.04 | 8.19 | 12.89 | 1.00 | 65.0 | 82.0 |
| Bench 4 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 2.57 | 8.19 | 13.39 | 1.00 | 57.0 | 66.0 |
| Bench 3 | Autosub In | Adam Armstrong | FWD | 20 | 5.2 | 2.59 | 7.63 | 12.12 | 2.00 | 68.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.74 | 18.19 | 28.66 | 3.00 | 103.3 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.53 | 11.67 | 16.78 | 0.00 | 69.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.30 | 11.51 | 18.17 | 2.00 | 54.2 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.34 | 11.33 | 18.87 | 0.00 | 31.4 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.46 | 9.47 | 14.48 | 12.00 | 71.5 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.60 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 51.59
- Actual score: 78.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 3.99, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.69 | 10.51 | 16.42 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Bernd Leno | GK | 10 | 4.9 | 2.86 | 8.12 | 13.35 | 2.00 | 80.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.96 | 13.74 | 20.69 | 6.00 | 92.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.40 | 11.65 | 18.37 | 2.00 | 103.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.80 | 10.86 | 16.87 | 14.00 | 85.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 3.30 | 9.70 | 16.25 | 4.00 | 78.9 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.8 | 2.95 | 8.80 | 12.70 | 1.00 | 81.2 | 90.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.89 | 8.64 | 12.96 | 2.00 | 71.1 | 83.0 |
| Bench 2 | Bench | Adam Armstrong | FWD | 20 | 5.2 | 2.78 | 7.70 | 11.98 | 2.00 | 66.2 | 71.0 |
| Bench 3 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 2.46 | 7.37 | 12.32 | 6.00 | 52.4 | 64.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.58 | 17.19 | 27.47 | 9.00 | 98.6 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.44 | 9.76 | 15.10 | 12.00 | 80.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.59 | 9.68 | 15.01 | 12.00 | 75.1 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.42 | 9.22 | 15.36 | 1.00 | 20.8 | 16.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.45 | 7.73 | 13.59 | 1.00 | 43.3 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.70 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.53
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (11.50) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Enzo Fernández (projected gain 2.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (11.50) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.14 | 10.63 | 16.59 | 0.00 | 86.0 | 0.0 |
| Bench 1 | Bench Boost | Bernd Leno | GK | 10 | 4.9 | 2.59 | 7.95 | 13.09 | 6.00 | 80.4 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.95 | 12.31 | 19.15 | 1.00 | 87.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.94 | 12.00 | 18.18 | 2.00 | 96.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.45 | 10.56 | 16.31 | 0.00 | 94.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.26 | 10.50 | 16.38 | 2.00 | 92.3 | 90.0 |
| Bench 2 | Bench Boost | Neco Williams | DEF | 16 | 4.8 | 3.20 | 8.22 | 12.27 | 2.00 | 83.6 | 90.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.08 | 8.21 | 13.37 | 2.00 | 74.0 | 90.0 |
| Bench 3 | Bench Boost | Valentín Castellanos | FWD | 19 | 5.5 | 2.94 | 7.90 | 12.84 | 8.00 | 53.2 | 87.0 |
| Bench 4 | Bench Boost | Adam Armstrong | FWD | 20 | 5.1 | 2.77 | 7.29 | 11.48 | 7.00 | 60.2 | 73.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.26 | 17.04 | 27.88 | 14.00 | 96.7 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.3 | 3.54 | 10.98 | 18.34 | 0.00 | 83.9 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.93 | 10.51 | 18.29 | 6.00 | 25.2 | 73.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.05 | 10.42 | 18.23 | 2.00 | 89.7 | 64.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.5 | 4.16 | 10.36 | 16.93 | 1.00 | 85.5 | 90.0 |