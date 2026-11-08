# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW29
- Simulated weeks: GW30-GW38
- Total predicted points: 586.79
- Total actual points: 517.00
- Average predicted points: 65.20
- Average actual points: 57.44
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW29 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW30

- Train rows: 183541
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Antoine Semenyo
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Antoine Semenyo
- Chip used: none
- Predicted score: 66.52
- Actual score: 47.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Elliot Anderson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.29 | 12.53 | 20.55 | 7.00 | 93.8 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.60 | 10.34 | 16.81 | 6.00 | 91.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.34 | 15.37 | 24.88 | 2.00 | 89.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.21 | 15.35 | 25.54 | 9.00 | 98.9 | 90.0 |
| XI | XI | Jurriën Timber | DEF | 1 | 6.3 | 4.77 | 13.62 | 22.08 | 1.00 | 86.9 | 37.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.2 | 4.52 | 12.95 | 21.01 | 2.00 | 90.5 | 90.0 |
| Bench 3 | Bench | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.26 | 12.02 | 19.38 | 10.00 | 92.4 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 6.96 | 19.66 | 32.02 | 2.00 | 98.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.33 | 14.79 | 23.77 | 6.00 | 89.9 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 3.55 | 10.22 | 16.42 | 0.00 | 76.0 | 90.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.2 | 7.00 | 20.09 | 32.01 | 2.00 | 105.6 | 74.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.0 | 6.56 | 19.61 | 31.92 | 10.00 | 100.6 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.00 | 15.83 | 25.89 | 2.00 | 74.8 | 90.0 |
| XI | Bench | Crysencio Summerville | MID | 19 | 5.7 | 4.55 | 13.29 | 21.32 | 0.00 | 89.6 | 0.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.4 | 4.49 | 12.68 | 20.40 | 2.00 | 88.6 | 87.0 |

## GW31

- Train rows: 184363
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.03
- Actual score: 42.00
- League average score: 0.00
- Transfer: Elliot Anderson -> Pascal Groß (projected gain 1.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.41 | 11.42 | 19.37 | 0.00 | 73.6 | 0.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.79 | 10.92 | 17.69 | 2.00 | 94.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 5.17 | 15.33 | 25.00 | 3.00 | 94.4 | 90.0 |
| XI | Bench | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.31 | 13.92 | 23.89 | 0.00 | 78.5 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.0 | 4.38 | 12.38 | 19.85 | 1.00 | 89.6 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.59 | 11.56 | 19.70 | 0.00 | 72.9 | 0.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.3 | 2.98 | 10.36 | 17.44 | 0.00 | 49.1 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 6.40 | 18.80 | 30.46 | 2.00 | 94.2 | 77.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 5.35 | 15.18 | 24.46 | 4.00 | 93.8 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 3.49 | 9.75 | 15.63 | 2.00 | 74.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.1 | 6.83 | 20.29 | 32.90 | 13.00 | 108.3 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.3 | 5.36 | 16.92 | 28.55 | 0.00 | 71.9 | 0.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.62 | 14.33 | 23.87 | 2.00 | 73.8 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.40 | 12.72 | 19.86 | 2.00 | 92.4 | 90.0 |
| Bench 4 | Bench | Crysencio Summerville | MID | 19 | 5.7 | 2.37 | 7.99 | 14.09 | 0.00 | 44.4 | 0.0 |

## GW32

- Train rows: 185188
- Bank: 0.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.62
- Actual score: 56.00
- League average score: 0.00
- Transfer: Crysencio Summerville -> Jaidon Anthony (projected gain 1.47, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 3.69 | 10.49 | 17.20 | 2.00 | 94.1 | 90.0 |
| Bench 1 | Bench | David Raya Martín | GK | 1 | 6.0 | 3.26 | 10.05 | 17.20 | 1.00 | 60.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.37 | 15.43 | 24.29 | 9.00 | 95.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.91 | 11.71 | 20.43 | 4.00 | 60.9 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 3.71 | 11.44 | 18.61 | 4.00 | 84.5 | 90.0 |
| Bench 3 | Bench | Jurriën Timber | DEF | 1 | 6.3 | 3.11 | 9.83 | 16.55 | 0.00 | 47.4 | 0.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.2 | 3.09 | 9.36 | 16.19 | 15.00 | 55.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.01 | 17.72 | 28.90 | 2.00 | 92.1 | 81.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.47 | 15.46 | 24.27 | 13.00 | 96.5 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.38 | 10.39 | 16.44 | 2.00 | 75.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.2 | 7.86 | 22.80 | 35.91 | 4.00 | 113.3 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 4.91 | 14.73 | 23.85 | 4.00 | 82.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.3 | 4.70 | 14.60 | 25.01 | 2.00 | 58.2 | 90.0 |
| XI | XI | Jaidon Anthony | MID | 3 | 5.0 | 4.15 | 11.79 | 18.70 | 2.00 | 84.8 | 90.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.00 | 11.53 | 18.47 | 6.00 | 84.0 | 90.0 |

## GW33

- Train rows: 186014
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 83.17
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (22.48) beats the best remaining Bench Boost opportunity (14.53).
- Chip advisory: bench_boost (0.65): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- League average score: 0.00
- Transfer: Jaidon Anthony -> Alex Scott (projected gain 0.54, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (22.48) beats the best remaining Bench Boost opportunity (14.53).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | David Raya Martín | GK | 1 | 6.0 | 3.47 | 11.15 | 18.78 | 1.00 | 80.4 | 90.0 |
| XI | XI | Martin Dúbravka | GK | 3 | 4.0 | 4.52 | 10.99 | 17.38 | 4.00 | 117.8 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.13 | 15.22 | 25.44 | 8.00 | 96.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.67 | 14.60 | 23.64 | 8.00 | 114.3 | 180.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.1 | 5.45 | 13.22 | 20.79 | 6.00 | 111.9 | 180.0 |
| Bench 3 | Bench Boost | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.36 | 13.19 | 22.58 | 0.00 | 79.3 | 90.0 |
| Bench 4 | Bench Boost | Jurriën Timber | DEF | 1 | 6.3 | 1.66 | 6.33 | 12.10 | 0.00 | 24.9 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.05 | 16.77 | 27.53 | 0.00 | 107.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.59 | 15.82 | 25.69 | 2.00 | 98.1 | 90.0 |
| Bench 2 | Bench Boost | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.93 | 12.03 | 18.01 | 8.00 | 100.3 | 180.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.88 | 20.46 | 34.07 | 6.00 | 102.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.08 | 16.59 | 27.97 | 5.00 | 101.3 | 154.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.6 | 5.90 | 15.16 | 24.69 | 2.00 | 104.0 | 90.0 |
| XI | XI | Alex Scott | MID | 4 | 5.0 | 5.28 | 12.98 | 20.09 | 5.00 | 115.2 | 180.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 5.31 | 12.82 | 19.84 | 16.00 | 110.7 | 180.0 |

## GW34

- Train rows: 186843
- Bank: 0.60 -> 1.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.61
- Actual score: 33.00
- League average score: 0.00
- Transfer: Jurriën Timber -> Nico O'Reilly (projected gain 3.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.51 | 11.28 | 18.84 | 0.00 | 108.7 | 0.0 |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.56 | 10.62 | 17.96 | 10.00 | 79.5 | 90.0 |
| XI | Bench | Nico O'Reilly | DEF | 13 | 5.1 | 5.31 | 16.12 | 25.12 | 0.00 | 94.3 | 0.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.3 | 5.49 | 15.75 | 25.96 | 4.00 | 99.3 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.86 | 15.23 | 24.59 | 0.00 | 103.5 | 0.0 |
| XI | Bench | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.70 | 14.43 | 22.79 | 0.00 | 104.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.42 | 12.95 | 22.03 | 8.00 | 79.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.74 | 14.44 | 24.27 | 1.00 | 88.5 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 4.39 | 13.09 | 20.25 | 0.00 | 91.7 | 0.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 2.63 | 10.87 | 19.68 | 0.00 | 27.9 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.52 | 18.86 | 32.25 | 5.00 | 99.0 | 90.0 |
| XI | Bench | Antoine Semenyo | MID | 13 | 8.2 | 5.48 | 17.28 | 28.56 | 0.00 | 89.0 | 0.0 |
| XI | Bench | Pascal Groß | MID | 6 | 5.5 | 4.58 | 13.99 | 22.54 | 0.00 | 103.2 | 0.0 |
| XI | Bench | Alex Scott | MID | 4 | 5.0 | 4.44 | 13.71 | 21.72 | 0.00 | 103.9 | 0.0 |
| Bench 3 | Bench | Cole Palmer | MID | 7 | 10.5 | 3.43 | 11.81 | 20.08 | 0.00 | 54.8 | 0.0 |

## GW35

- Train rows: 187673
- Bank: 1.70 -> 4.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.43
- Actual score: 62.00
- League average score: 0.00
- Transfer: Cole Palmer -> Morgan Gibbs-White (projected gain 5.97, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.13 | 12.43 | 19.67 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.50 | 7.78 | 13.32 | 2.00 | 69.2 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.45 | 16.11 | 24.50 | 6.00 | 94.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.98 | 15.33 | 24.22 | 1.00 | 92.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.1 | 3.95 | 11.69 | 18.74 | 1.00 | 58.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 3.83 | 11.61 | 19.02 | 4.00 | 71.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 3.58 | 10.64 | 18.08 | 14.00 | 66.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 5.01 | 14.65 | 23.78 | 6.00 | 83.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.61 | 10.97 | 19.14 | 8.00 | 46.9 | 90.0 |
| Bench 2 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.6 | 3.48 | 9.19 | 15.32 | 6.00 | 56.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.60 | 20.18 | 32.97 | 5.00 | 98.9 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.01 | 15.07 | 24.04 | 4.00 | 82.3 | 20.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.69 | 14.02 | 23.11 | 2.00 | 67.6 | 74.0 |
| Bench 3 | Bench | Pascal Groß | MID | 6 | 5.5 | 3.02 | 9.09 | 15.77 | 2.00 | 55.3 | 90.0 |
| Bench 4 | Bench | Alex Scott | MID | 4 | 5.0 | 2.72 | 8.17 | 14.45 | 3.00 | 58.7 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 4.70 -> 2.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 72.98
- Actual score: 77.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (10.07) beats the best remaining Triple Captain opportunity (8.56).
- League average score: 0.00
- Transfer: Alex Scott -> Dominik Szoboszlai (projected gain 1.02, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (10.07) beats the best remaining Triple Captain opportunity (8.56).
- Autosub outfielders: João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.25 | 12.22 | 20.29 | 9.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 3.29 | 9.59 | 15.75 | 0.00 | 92.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.72 | 16.13 | 25.79 | 11.00 | 98.6 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 6.03 | 14.79 | 23.07 | 15.00 | 121.7 | 180.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 5.04 | 14.08 | 23.12 | 8.00 | 97.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.88 | 13.72 | 22.71 | 2.00 | 91.6 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.70 | 13.60 | 20.60 | 5.00 | 103.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.64 | 14.47 | 23.94 | 2.00 | 86.8 | 90.0 |
| Bench 2 | Autosub In | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.24 | 12.38 | 21.93 | 2.00 | 73.8 | 90.0 |
| Bench 4 | Bench | Dominic Calvert-Lewin | FWD | 11 | 5.7 | 4.01 | 11.05 | 18.11 | 7.00 | 81.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.97 | 20.73 | 34.17 | 3.00 | 102.4 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.47 | 15.79 | 25.43 | 12.00 | 108.4 | 180.0 |
| XI | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 4.67 | 13.87 | 23.49 | 0.00 | 64.9 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.65 | 13.38 | 22.06 | 2.00 | 85.5 | 90.0 |
| Bench 3 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.06 | 10.93 | 18.34 | 6.00 | 80.2 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 2.70 -> 3.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.57
- Actual score: 76.00
- League average score: 0.00
- Transfer: Morgan Gibbs-White -> Ismaïla Sarr (projected gain 3.22, hit 0)
- Autosub outfielders: Dominic Calvert-Lewin.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.59 | 12.56 | 20.34 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 1.52 | 5.66 | 10.23 | 0.00 | 48.5 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.00 | 16.32 | 26.24 | 6.00 | 97.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.31 | 15.60 | 25.70 | 2.00 | 119.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.06 | 12.50 | 20.78 | 14.00 | 86.5 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.07 | 12.10 | 20.90 | 4.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.3 | 3.28 | 10.10 | 17.19 | 2.00 | 62.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.51 | 13.59 | 22.89 | 2.00 | 82.4 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.29 | 12.39 | 20.41 | 0.00 | 73.3 | 0.0 |
| Bench 2 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.39 | 10.16 | 17.23 | 7.00 | 69.2 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.93 | 20.43 | 33.21 | 9.00 | 102.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.92 | 17.55 | 28.38 | 1.00 | 111.5 | 55.0 |
| XI | XI | Ismaïla Sarr | MID | 8 | 6.4 | 4.84 | 13.35 | 20.90 | 7.00 | 85.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.12 | 12.56 | 21.07 | 9.00 | 81.2 | 90.0 |
| Bench 4 | Bench | Pascal Groß | MID | 6 | 5.6 | 3.19 | 9.87 | 16.99 | 3.00 | 71.1 | 90.0 |

## GW38

- Train rows: 190183
- Bank: 3.90 -> 2.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.86
- Actual score: 47.00
- League average score: 0.00
- Transfer: Pascal Groß -> Morgan Rogers (projected gain 1.89, hit 0)
- Autosub outfielders: Dominic Calvert-Lewin, João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.33 | 12.74 | 20.70 | 0.00 | 87.0 | 0.0 |
| Bench 1 | Bench | Martin Dúbravka | GK | 3 | 4.0 | 2.33 | 6.39 | 10.92 | 0.00 | 45.7 | 0.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.38 | 15.37 | 24.73 | 2.00 | 98.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 5.35 | 15.26 | 24.78 | 1.00 | 93.4 | 45.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 5.02 | 14.36 | 23.15 | 0.00 | 103.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.51 | 13.16 | 21.60 | 2.00 | 91.8 | 90.0 |
| Bench 2 | Bench | Nico O'Reilly | DEF | 13 | 5.3 | 4.09 | 11.55 | 18.93 | 0.00 | 78.1 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.80 | 14.13 | 23.10 | 2.00 | 88.5 | 90.0 |
| Bench 3 | Autosub In | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.72 | 10.98 | 18.19 | 2.00 | 84.1 | 68.0 |
| Bench 4 | Autosub In | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.03 | 9.00 | 15.11 | 1.00 | 47.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.93 | 20.73 | 34.18 | 14.00 | 103.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.16 | 14.96 | 24.36 | 6.00 | 84.9 | 57.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.81 | 13.73 | 22.91 | 2.00 | 88.4 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.4 | 4.29 | 13.41 | 21.77 | 0.00 | 88.4 | 0.0 |
| XI | XI | Ismaïla Sarr | MID | 8 | 6.4 | 4.34 | 12.33 | 19.49 | 1.00 | 78.8 | 45.0 |