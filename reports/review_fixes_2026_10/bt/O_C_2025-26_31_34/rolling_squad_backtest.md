# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 277.91
- Total actual points: 214.00
- Average predicted points: 69.48
- Average actual points: 53.50
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
- Predicted score: 63.14
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Pascal Groß, Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.36 | 11.33 | 19.28 | 0.00 | 75.0 | 0.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.64 | 10.52 | 17.06 | 2.00 | 94.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.17 | 15.36 | 25.06 | 3.00 | 96.0 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.55 | 14.63 | 25.05 | 0.00 | 78.6 | 0.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 4.60 | 12.72 | 20.58 | -1.00 | 92.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.43 | 12.55 | 20.15 | 1.00 | 90.4 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.65 | 11.75 | 20.00 | 0.00 | 72.6 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.57 | 19.28 | 31.23 | 2.00 | 95.8 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.39 | 15.22 | 24.49 | 4.00 | 91.7 | 90.0 |
| Bench 4 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 3.45 | 9.62 | 15.39 | 2.00 | 73.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 6.87 | 20.43 | 33.13 | 13.00 | 108.6 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.37 | 16.98 | 28.68 | 0.00 | 73.9 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.90 | 14.75 | 23.44 | 3.00 | 93.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.77 | 14.73 | 24.51 | 2.00 | 73.8 | 90.0 |
| Bench 2 | Autosub In | Pascal Groß | MID | 6 | 5.5 | 4.43 | 12.82 | 20.05 | 2.00 | 93.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 63.27
- Actual score: 57.00
- Transfer: Pascal Groß -> Elliot Anderson (projected gain 0.59, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.51 | 9.98 | 16.37 | 2.00 | 94.0 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.17 | 9.82 | 16.85 | 1.00 | 61.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.41 | 15.55 | 24.51 | 9.00 | 96.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.08 | 12.17 | 21.15 | 4.00 | 60.7 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.77 | 11.72 | 18.92 | 3.00 | 92.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.80 | 11.70 | 19.04 | 4.00 | 85.7 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.07 | 9.27 | 16.03 | 15.00 | 53.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.22 | 18.29 | 29.82 | 2.00 | 93.2 | 81.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.52 | 15.60 | 24.49 | 13.00 | 94.3 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.37 | 10.30 | 16.24 | 2.00 | 74.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.95 | 23.11 | 36.44 | 4.00 | 114.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.07 | 15.16 | 24.55 | 4.00 | 83.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.3 | 4.64 | 14.43 | 24.73 | 2.00 | 58.6 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.93 | 14.32 | 22.56 | 5.00 | 86.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.19 | 12.14 | 20.06 | 4.00 | 83.5 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 85.05
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (24.08) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: James Hill -> Konstantinos Mavropanos (projected gain 1.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (24.08) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.39 | 10.92 | 18.40 | 1.00 | 80.7 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 4.40 | 10.68 | 16.88 | 4.00 | 117.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.03 | 14.93 | 25.00 | 8.00 | 97.4 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.4 | 5.10 | 14.66 | 22.61 | 6.00 | 105.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.58 | 14.36 | 23.26 | 8.00 | 113.6 | 180.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.45 | 13.44 | 22.99 | 0.00 | 77.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 5.47 | 13.28 | 20.88 | 6.00 | 111.8 | 180.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.11 | 16.95 | 27.83 | 0.00 | 106.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.65 | 15.98 | 25.94 | 2.00 | 95.6 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.95 | 12.00 | 17.92 | 8.00 | 98.8 | 180.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.93 | 20.59 | 34.28 | 6.00 | 102.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 5.99 | 16.25 | 27.39 | 5.00 | 100.4 | 154.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.99 | 15.40 | 25.08 | 2.00 | 104.2 | 90.0 |
| Bench 2 | Bench Boost | Dominik Szoboszlai | MID | 12 | 7.1 | 4.59 | 13.41 | 21.83 | 5.00 | 84.0 | 90.0 |
| Bench 3 | Bench Boost | Elliot Anderson | MID | 16 | 5.5 | 4.50 | 12.24 | 19.57 | 2.00 | 81.3 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 66.45
- Actual score: 42.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.95) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Dominik Szoboszlai -> Rayan Cherki (projected gain 1.81, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (4.95) beats the best remaining Triple Captain opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.45 | 11.14 | 18.60 | 0.00 | 109.3 | 0.0 |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.50 | 10.42 | 17.60 | 10.00 | 79.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.42 | 15.60 | 25.77 | 4.00 | 101.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.94 | 15.48 | 25.01 | 0.00 | 104.4 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.83 | 14.84 | 23.48 | 0.00 | 105.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.40 | 12.89 | 21.91 | 8.00 | 78.3 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.47 | 12.78 | 20.59 | 4.00 | 91.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.73 | 14.38 | 24.13 | 1.00 | 87.4 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.50 | 13.36 | 20.68 | 0.00 | 89.9 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 2.79 | 11.34 | 20.45 | 0.00 | 26.5 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.45 | 18.70 | 32.00 | 5.00 | 99.4 | 90.0 |
| Vice Captain | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.53 | 17.42 | 28.77 | 0.00 | 89.7 | 0.0 |
| XI | Bench | Rayan Cherki | MID | 13 | 6.4 | 4.79 | 14.53 | 23.39 | 0.00 | 80.1 | 0.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 10.5 | 3.62 | 12.33 | 20.90 | 0.00 | 53.3 | 0.0 |
| Bench 2 | Bench | Elliot Anderson | MID | 16 | 5.6 | 4.08 | 11.67 | 18.73 | 9.00 | 82.0 | 90.0 |