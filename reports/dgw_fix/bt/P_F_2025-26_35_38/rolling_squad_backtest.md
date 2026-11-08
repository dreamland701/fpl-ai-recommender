# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 266.50
- Total actual points: 232.00
- Average predicted points: 66.62
- Average actual points: 58.00
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
- Predicted score: 54.90
- Actual score: 44.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Jaydee Canvot replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Dean Henderson | GK | 8 | 5.1 | 2.82 | 11.18 | 17.07 | 2.00 | 75.8 | 90.0 |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.45 | 10.41 | 17.21 | 6.00 | 81.8 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.93 | 15.20 | 21.54 | 0.00 | 81.2 | 45.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.12 | 14.96 | 23.49 | 6.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 3.84 | 14.74 | 21.64 | 1.00 | 57.8 | 90.0 |
| Bench 2 | Autosub In | Jaydee Canvot | DEF | 8 | 4.5 | 3.48 | 13.70 | 19.87 | 0.00 | 80.8 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.13 | 13.31 | 20.61 | 4.00 | 61.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.71 | 13.85 | 23.12 | 6.00 | 83.1 | 90.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.58 | 10.21 | 16.52 | 5.00 | 63.1 | 45.0 |
| Bench 3 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 3.13 | 8.99 | 14.47 | 1.00 | 68.2 | 64.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.41 | 19.37 | 32.60 | 5.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.11 | 15.42 | 23.13 | 5.00 | 57.5 | 90.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.44 | 14.84 | 25.25 | 0.00 | 63.2 | 0.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.43 | 13.14 | 20.35 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.46 | 12.55 | 20.10 | 1.00 | 83.0 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Rayan Cherki
- Vice captain: Marc Guéhi
- Effective captain: Rayan Cherki
- Chip used: triple_captain
- Predicted score: 88.49
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.48) beats the best remaining Triple Captain opportunity (8.80).
- Chip advisory: triple_captain (0.63): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Daniel Muñoz Mejía -> Maxence Lacroix (projected gain 1.73, hit 0)
- Chip used: Triple Captain on Rayan Cherki. Optimizer chose Triple Captain here because the current estimated captain upside (13.48) beats the best remaining Triple Captain opportunity (8.80).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.
- Autosub: Igor Jesus Maciel da Cruz replaced Mohamed Salah.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.78 | 11.10 | 18.17 | 9.00 | 83.8 | 90.0 |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 5.23 | 10.25 | 16.33 | 3.00 | 147.5 | 180.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 8.21 | 16.30 | 25.95 | 15.00 | 180.0 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.26 | 15.20 | 24.20 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 7.87 | 14.93 | 22.87 | 5.00 | 145.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 7.43 | 13.82 | 21.25 | 4.00 | 153.3 | 180.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.38 | 12.72 | 19.56 | 4.00 | 155.7 | 180.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.85 | 12.37 | 20.94 | 2.00 | 76.6 | 90.0 |
| Bench 3 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.04 | 9.01 | 14.90 | 1.00 | 54.3 | 82.0 |
| Bench 4 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 2.59 | 8.20 | 13.27 | 1.00 | 57.4 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.17 | 20.87 | 34.34 | 3.00 | 90.0 | 90.0 |
| Captain | Captain | Rayan Cherki | MID | 13 | 6.5 | 9.33 | 17.16 | 26.78 | 5.00 | 147.7 | 70.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.82 | 13.94 | 21.66 | 0.00 | 90.0 | 0.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.29 | 13.20 | 22.60 | 0.00 | 43.0 | 0.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.37 | 9.76 | 16.19 | 12.00 | 63.0 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.59
- Actual score: 56.00
- Transfer: Nico O'Reilly -> James Tarkowski (projected gain 3.01, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.80 | 12.63 | 20.19 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Dean Henderson | GK | 8 | 5.1 | 3.45 | 9.51 | 14.59 | 0.00 | 90.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.27 | 16.25 | 25.93 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.74 | 13.65 | 22.56 | 2.00 | 90.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 4.53 | 12.32 | 18.52 | 2.00 | 90.0 | 60.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 4.47 | 12.18 | 19.34 | 3.00 | 86.5 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.30 | 11.68 | 17.95 | 3.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.68 | 13.13 | 21.76 | 2.00 | 83.9 | 90.0 |
| Bench 2 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.94 | 9.22 | 15.22 | 2.00 | 61.6 | 83.0 |
| Bench 3 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 2.47 | 7.41 | 12.25 | 6.00 | 52.8 | 64.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.34 | 33.29 | 9.00 | 90.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.30 | 11.16 | 19.98 | 1.00 | 30.1 | 16.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.25 | 10.57 | 17.52 | 1.00 | 52.0 | 34.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.46 | 10.55 | 17.78 | 12.00 | 77.5 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.47 | 7.94 | 13.92 | 1.00 | 43.1 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.51
- Actual score: 57.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.94) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Maxence Lacroix -> Marcos Senesi Barón (projected gain 2.97, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.94) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.38 | 12.23 | 19.57 | 0.00 | 84.9 | 0.0 |
| Bench 1 | Bench Boost | Dean Henderson | GK | 8 | 5.1 | 2.46 | 7.25 | 11.47 | 2.00 | 81.4 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.35 | 14.95 | 24.31 | 1.00 | 88.5 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.70 | 13.15 | 21.01 | 0.00 | 90.0 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.41 | 13.01 | 21.09 | 2.00 | 90.0 | 90.0 |
| XI | XI | James Tarkowski | DEF | 9 | 5.7 | 3.50 | 10.60 | 16.97 | 3.00 | 76.7 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 3.26 | 9.39 | 14.64 | 0.00 | 84.9 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.04 | 12.17 | 20.18 | 2.00 | 80.5 | 90.0 |
| Bench 2 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.09 | 8.99 | 14.66 | 2.00 | 65.4 | 90.0 |
| Bench 3 | Bench Boost | Valentín Castellanos | FWD | 19 | 5.5 | 2.97 | 7.98 | 12.92 | 8.00 | 53.9 | 87.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.83 | 20.33 | 33.68 | 14.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.05 | 12.10 | 19.70 | 2.00 | 90.0 | 64.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.79 | 12.01 | 20.78 | 6.00 | 37.0 | 73.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.43 | 10.17 | 16.70 | 1.00 | 51.1 | 32.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.42 | 7.52 | 13.61 | 0.00 | 51.8 | 0.0 |