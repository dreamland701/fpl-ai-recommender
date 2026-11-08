# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 430.46
- Total actual points: 365.00
- Average predicted points: 61.49
- Average actual points: 52.14
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 72.81
- Actual score: 51.00
- Chip advisory: bench_boost (0.62): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Pedro Porro Sauceda.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.58 | 13.15 | 21.56 | 1.00 | 98.4 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 4.39 | 12.72 | 20.87 | 2.00 | 98.6 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.5 | 7.20 | 20.75 | 34.07 | 1.00 | 118.8 | 8.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.75 | 13.99 | 22.90 | 3.00 | 103.7 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 4.65 | 13.17 | 21.37 | 1.00 | 94.4 | 90.0 |
| Bench 2 | Autosub In | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.33 | 13.11 | 21.67 | 5.00 | 96.2 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 4.15 | 12.50 | 20.46 | -1.00 | 91.9 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.5 | 5.88 | 17.60 | 29.03 | 9.00 | 84.2 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.47 | 15.76 | 25.89 | 15.00 | 79.4 | 90.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.5 | 4.04 | 12.66 | 21.13 | 1.00 | 58.3 | 19.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.99 | 23.71 | 39.18 | 5.00 | 110.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.77 | 19.47 | 31.88 | 0.00 | 100.7 | 0.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 6.51 | 18.87 | 31.01 | 2.00 | 115.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 5.63 | 16.50 | 26.91 | 2.00 | 95.3 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 5.40 | 16.28 | 26.57 | 2.00 | 98.8 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bryan Mbeumo
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.09
- Actual score: 53.00
- League average score: 51.00
- Transfer: James Trafford -> Robert Lynch Sánchez (projected gain 2.00, hit 0)
- Autosub outfielders: Trai Hume, Raúl Jiménez Rodríguez.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.82 | 11.34 | 18.17 | 6.00 | 89.7 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.5 | 3.16 | 9.34 | 15.32 | 8.00 | 84.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.36 | 12.83 | 19.02 | 8.00 | 81.0 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.13 | 12.49 | 19.82 | 4.00 | 84.9 | 70.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.6 | 4.01 | 12.01 | 18.83 | 0.00 | 46.4 | 0.0 |
| Bench 2 | Autosub In | Trai Hume | DEF | 17 | 4.5 | 3.01 | 9.19 | 14.65 | 2.00 | 79.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.38 | 7.25 | 10.87 | 9.00 | 67.6 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.04 | 15.32 | 24.64 | 9.00 | 82.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.66 | 14.96 | 23.52 | 2.00 | 69.4 | 78.0 |
| Bench 3 | Autosub In | Raúl Jiménez Rodríguez | FWD | 10 | 6.5 | 2.60 | 8.72 | 14.75 | 1.00 | 38.0 | 31.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.74 | 21.48 | 34.60 | 3.00 | 94.2 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.0 | 5.24 | 15.23 | 24.03 | 10.00 | 83.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.55 | 14.84 | 22.27 | 2.00 | 81.0 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.53 | 14.15 | 23.14 | 0.00 | 44.1 | 0.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.28 | 11.69 | 18.04 | 3.00 | 76.0 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 1.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.05
- Actual score: 57.00
- League average score: 0.00
- Transfer: Cole Palmer -> Bruno Borges Fernandes (projected gain 7.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.62 | 10.91 | 17.84 | 2.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.5 | 3.47 | 10.45 | 17.21 | 10.00 | 91.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.49 | 12.88 | 19.60 | 8.00 | 82.9 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.36 | 12.87 | 19.86 | 6.00 | 75.8 | 90.0 |
| XI | XI | Trai Hume | DEF | 17 | 4.5 | 2.93 | 8.73 | 13.85 | 6.00 | 78.1 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.89 | 8.17 | 12.73 | 0.00 | 69.4 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.55 | 7.99 | 13.30 | 0.00 | 31.9 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.43 | 16.58 | 25.59 | 7.00 | 78.7 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 4.27 | 12.92 | 20.44 | 2.00 | 60.2 | 71.0 |
| Bench 3 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.4 | 2.77 | 8.42 | 13.91 | 1.00 | 40.0 | 6.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.79 | 20.41 | 33.20 | 9.00 | 87.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.10 | 15.97 | 25.06 | 2.00 | 78.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.82 | 15.10 | 24.41 | 2.00 | 82.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.65 | 13.73 | 21.76 | 3.00 | 86.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.81 | 10.68 | 16.58 | 1.00 | 74.7 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 1.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.09
- Actual score: 66.00
- League average score: 0.00
- Transfer: Daniel Ballard -> Daniel Muñoz Mejía (projected gain 4.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.43 | 10.62 | 17.47 | -3.00 | 86.0 | 4.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.55 | 10.53 | 17.39 | 2.00 | 92.4 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.61 | 13.69 | 21.97 | 1.00 | 86.0 | 88.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.6 | 4.65 | 13.45 | 20.89 | 2.00 | 81.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.57 | 13.14 | 20.49 | 4.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Trai Hume | DEF | 17 | 4.5 | 3.24 | 9.36 | 15.08 | 4.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.68 | 7.39 | 11.46 | 4.00 | 66.7 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.79 | 17.43 | 28.06 | 2.00 | 85.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.8 | 3.77 | 11.76 | 18.92 | 8.00 | 50.9 | 66.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.4 | 1.99 | 6.58 | 11.00 | 1.00 | 29.4 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.77 | 20.35 | 33.18 | 5.00 | 87.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.31 | 15.25 | 24.52 | 10.00 | 79.5 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.90 | 14.36 | 23.39 | 3.00 | 78.8 | 69.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.92 | 12.33 | 20.38 | 9.00 | 82.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.47 | 9.45 | 14.92 | 15.00 | 71.9 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 59.86
- Actual score: 30.00
- League average score: 0.00
- Transfer: Daniel Muñoz Mejía -> Dan Burn (projected gain 1.34, hit 0)
- Autosub outfielders: Trai Hume.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.19 | 9.66 | 16.14 | 10.00 | 88.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.38 | 7.43 | 12.69 | 1.00 | 50.0 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.0 | 5.27 | 13.44 | 20.95 | 0.00 | 81.6 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.58 | 13.40 | 21.45 | 1.00 | 90.3 | 27.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.19 | 12.76 | 21.86 | 2.00 | 74.9 | 90.0 |
| Bench 2 | Autosub In | Trai Hume | DEF | 17 | 4.5 | 3.15 | 10.01 | 15.68 | 6.00 | 89.3 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.45 | 6.86 | 12.32 | 1.00 | 77.2 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.21 | 18.34 | 28.97 | 2.00 | 95.3 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 8.8 | 3.95 | 12.50 | 19.65 | 0.00 | 59.1 | 0.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.3 | 1.54 | 5.90 | 9.69 | 6.00 | 26.8 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.24 | 18.59 | 31.70 | 2.00 | 86.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.32 | 15.15 | 25.09 | -1.00 | 77.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.83 | 13.99 | 22.35 | 2.00 | 92.6 | 82.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.60 | 12.43 | 19.05 | 2.00 | 84.1 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.23 | 12.32 | 21.12 | 2.00 | 67.7 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 1.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 60.51
- Actual score: 45.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.70) beats the best remaining Triple Captain opportunity (6.98).
- League average score: 0.00
- Transfer: Gabriel Gudmundsson -> Marcos Senesi Barón (projected gain 4.70, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (5.70) beats the best remaining Triple Captain opportunity (6.98).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.40 | 10.42 | 17.32 | 2.00 | 93.4 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.55 | 7.69 | 13.07 | 2.00 | 65.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.8 | 5.05 | 14.78 | 22.87 | 2.00 | 84.9 | 77.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.22 | 12.44 | 20.62 | 1.00 | 88.5 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.0 | 4.27 | 11.88 | 18.51 | 11.00 | 84.3 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 3.65 | 10.93 | 18.79 | 7.00 | 60.5 | 90.0 |
| Bench 2 | Bench | Trai Hume | DEF | 17 | 4.5 | 3.38 | 10.15 | 16.30 | 1.00 | 89.1 | 78.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.44 | 16.70 | 27.93 | 2.00 | 89.6 | 73.0 |
| Bench 3 | Bench | Hugo Ekitiké | FWD | 12 | 8.7 | 2.00 | 6.84 | 12.30 | 1.00 | 20.7 | 16.0 |
| Bench 4 | Bench | Raúl Jiménez Rodríguez | FWD | 10 | 6.3 | 1.67 | 5.62 | 9.62 | 0.00 | 26.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 5.67 | 17.12 | 28.92 | 2.00 | 78.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.22 | 15.17 | 25.03 | 3.00 | 69.6 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.37 | 13.19 | 20.72 | 3.00 | 77.2 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.46 | 12.71 | 20.57 | 6.00 | 72.7 | 76.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.43 | 9.99 | 15.39 | 2.00 | 77.4 | 66.0 |

## GW8

- Train rows: 166350
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Marcos Senesi Barón
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 64.05
- Actual score: 63.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.10) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Anton Stach -> Granit Xhaka (projected gain 3.04, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.10) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 3.68 | 10.22 | 16.56 | 7.00 | 88.0 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.68 | 7.88 | 13.14 | 5.00 | 69.9 | 90.0 |
| Vice Captain | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.74 | 14.66 | 23.29 | 2.00 | 81.5 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.17 | 12.21 | 20.28 | 1.00 | 80.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.26 | 11.70 | 19.15 | 3.00 | 92.4 | 90.0 |
| XI | XI | Dan Burn | DEF | 15 | 5.0 | 3.85 | 11.60 | 18.56 | 2.00 | 88.5 | 90.0 |
| Bench 2 | Bench Boost | Trai Hume | DEF | 17 | 4.5 | 3.56 | 9.35 | 15.30 | 11.00 | 79.6 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.72 | 14.64 | 25.16 | 2.00 | 78.3 | 90.0 |
| Bench 3 | Bench Boost | Hugo Ekitiké | FWD | 12 | 8.7 | 2.69 | 8.15 | 14.10 | 1.00 | 33.3 | 28.0 |
| Bench 4 | Bench Boost | Raúl Jiménez Rodríguez | FWD | 10 | 6.3 | 1.13 | 3.95 | 7.10 | 2.00 | 16.5 | 90.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 5.52 | 16.71 | 28.56 | 2.00 | 74.7 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.50 | 14.49 | 24.15 | 8.00 | 76.0 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.8 | 4.46 | 12.53 | 20.58 | 1.00 | 78.1 | 58.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.00 | 12.41 | 20.47 | 9.00 | 68.5 | 90.0 |
| XI | XI | Granit Xhaka | MID | 17 | 5.0 | 4.56 | 12.34 | 20.01 | 5.00 | 87.9 | 90.0 |