# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW30
- Simulated weeks: GW31-GW34
- Total predicted points: 278.12
- Total actual points: 223.00
- Average predicted points: 69.53
- Average actual points: 55.75
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
- Predicted score: 63.21
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Marcos Senesi Barón replaced Gabriel dos Santos Magalhães.
- Autosub: Dominic Calvert-Lewin replaced Antoine Semenyo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.36 | 11.40 | 19.40 | 0.00 | 75.0 | 0.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.65 | 10.60 | 17.29 | 2.00 | 94.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.18 | 15.43 | 25.21 | 3.00 | 96.0 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.56 | 14.68 | 24.94 | 0.00 | 78.6 | 0.0 |
| XI | XI | James Hill | DEF | 4 | 4.2 | 4.59 | 12.75 | 20.61 | -1.00 | 92.9 | 90.0 |
| Bench 2 | Autosub In | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.42 | 12.61 | 20.24 | 1.00 | 90.4 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.65 | 11.86 | 20.13 | 0.00 | 72.6 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.57 | 19.42 | 31.64 | 2.00 | 95.8 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.39 | 15.41 | 24.97 | 4.00 | 91.7 | 90.0 |
| Bench 4 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 3.47 | 9.70 | 15.62 | 2.00 | 73.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 6.89 | 20.57 | 33.71 | 13.00 | 108.6 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.37 | 17.08 | 28.86 | 0.00 | 73.9 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.78 | 14.90 | 24.80 | 2.00 | 73.7 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.91 | 14.86 | 23.81 | 3.00 | 93.5 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.42 | 12.93 | 20.41 | 2.00 | 93.0 | 90.0 |

## GW32

- Train rows: 185188
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 63.37
- Actual score: 57.00
- Transfer: Pascal Groß -> Elliot Anderson (projected gain 0.68, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.52 | 10.08 | 16.63 | 2.00 | 94.0 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.19 | 9.91 | 17.11 | 1.00 | 61.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.41 | 15.61 | 24.67 | 9.00 | 96.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.10 | 12.27 | 21.28 | 4.00 | 60.7 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 3.83 | 11.77 | 19.18 | 4.00 | 85.7 | 90.0 |
| Bench 2 | Bench | James Hill | DEF | 4 | 4.2 | 3.80 | 11.72 | 19.04 | 3.00 | 92.5 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.08 | 9.38 | 16.26 | 15.00 | 53.6 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.21 | 18.37 | 30.13 | 2.00 | 93.3 | 81.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.52 | 15.66 | 24.80 | 13.00 | 94.3 | 90.0 |
| Bench 3 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.35 | 10.28 | 16.41 | 2.00 | 74.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 7.95 | 23.23 | 36.98 | 4.00 | 114.2 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.06 | 15.19 | 24.78 | 4.00 | 83.5 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.3 | 4.65 | 14.61 | 25.15 | 2.00 | 58.5 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.9 | 4.94 | 14.34 | 22.69 | 5.00 | 86.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.5 | 4.22 | 12.25 | 20.15 | 4.00 | 83.5 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 85.06
- Actual score: 69.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (24.09) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: James Hill -> Konstantinos Mavropanos (projected gain 1.90, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (24.09) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.38 | 10.92 | 18.48 | 1.00 | 80.7 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 4.38 | 10.74 | 17.05 | 4.00 | 117.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.03 | 14.92 | 24.98 | 8.00 | 97.4 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.4 | 5.11 | 14.58 | 22.71 | 6.00 | 105.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.61 | 14.39 | 23.49 | 8.00 | 113.6 | 180.0 |
| Bench 4 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.43 | 13.44 | 22.97 | 0.00 | 77.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 5.45 | 13.22 | 20.83 | 6.00 | 111.9 | 180.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.09 | 17.03 | 28.06 | 0.00 | 106.3 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.65 | 15.95 | 26.04 | 2.00 | 95.6 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.92 | 11.89 | 17.99 | 8.00 | 98.9 | 180.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.94 | 20.65 | 34.65 | 6.00 | 102.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.02 | 16.37 | 27.59 | 5.00 | 100.3 | 154.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.98 | 15.40 | 25.02 | 2.00 | 104.3 | 90.0 |
| Bench 2 | Bench Boost | Dominik Szoboszlai | MID | 12 | 7.0 | 4.59 | 13.39 | 21.76 | 5.00 | 84.0 | 90.0 |
| Bench 3 | Bench Boost | Elliot Anderson | MID | 16 | 5.5 | 4.53 | 12.26 | 19.60 | 2.00 | 81.2 | 90.0 |

## GW34

- Train rows: 186843
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 66.48
- Actual score: 51.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.97) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Dominik Szoboszlai -> Rayan Cherki (projected gain 1.87, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (4.97) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Elliot Anderson replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.45 | 11.17 | 18.71 | 0.00 | 109.3 | 0.0 |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.48 | 10.44 | 17.65 | 10.00 | 79.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.43 | 15.65 | 25.76 | 4.00 | 101.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.94 | 15.51 | 25.25 | 0.00 | 104.4 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.1 | 4.83 | 14.78 | 23.71 | 0.00 | 105.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.38 | 12.80 | 22.14 | 8.00 | 78.4 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.4 | 4.47 | 12.75 | 20.72 | 4.00 | 91.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.72 | 14.41 | 24.23 | 1.00 | 87.4 | 90.0 |
| XI | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.50 | 13.36 | 20.84 | 0.00 | 89.9 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 2.79 | 11.41 | 20.74 | 0.00 | 26.5 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 6.47 | 18.76 | 32.30 | 5.00 | 99.3 | 90.0 |
| Vice Captain | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.53 | 17.47 | 28.94 | 0.00 | 89.7 | 0.0 |
| XI | Bench | Rayan Cherki | MID | 13 | 6.4 | 4.79 | 14.54 | 23.50 | 0.00 | 80.1 | 0.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 10.5 | 3.62 | 12.33 | 20.96 | 0.00 | 53.3 | 0.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.5 | 4.06 | 11.62 | 18.70 | 9.00 | 82.0 | 90.0 |