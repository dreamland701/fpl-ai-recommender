# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 435.18
- Total actual points: 406.00
- Average predicted points: 62.17
- Average actual points: 58.00
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
- Predicted score: 72.51
- Actual score: 52.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Eliezer Mayenda Dossou.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.59 | 13.32 | 21.79 | 1.00 | 99.2 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 4.40 | 12.88 | 21.11 | 2.00 | 99.0 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.5 | 7.20 | 20.87 | 34.24 | 1.00 | 119.7 | 8.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.75 | 14.01 | 22.91 | 3.00 | 103.7 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.34 | 13.30 | 21.92 | 5.00 | 96.9 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 4.16 | 12.67 | 20.70 | -1.00 | 92.7 | 90.0 |
| Bench 4 | Bench | Pascal Struijk | DEF | 11 | 4.5 | 4.05 | 12.64 | 20.91 | 0.00 | 96.0 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.5 | 5.87 | 17.38 | 28.72 | 9.00 | 82.8 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.47 | 15.85 | 25.95 | 15.00 | 81.0 | 90.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.55 | 12.98 | 21.25 | 2.00 | 81.0 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.98 | 23.60 | 39.02 | 5.00 | 110.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.79 | 19.71 | 32.23 | 0.00 | 101.3 | 0.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 6.53 | 19.13 | 31.37 | 2.00 | 115.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.61 | 16.68 | 27.63 | 2.00 | 99.7 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 5.41 | 16.46 | 26.81 | 2.00 | 99.4 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.14
- Actual score: 58.00
- League average score: 51.00
- Transfer: James Trafford -> Robert Lynch Sánchez (projected gain 1.92, hit 0)
- Autosub outfielders: Eliezer Mayenda Dossou, Pascal Struijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.81 | 11.31 | 18.13 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.5 | 3.16 | 9.40 | 15.40 | 8.00 | 84.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.35 | 12.73 | 18.88 | 8.00 | 80.8 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.14 | 12.64 | 20.02 | 4.00 | 85.2 | 70.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.6 | 4.01 | 12.04 | 18.87 | 0.00 | 46.9 | 0.0 |
| Bench 3 | Autosub In | Pascal Struijk | DEF | 11 | 4.5 | 2.75 | 8.56 | 13.35 | 6.00 | 76.9 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.40 | 7.49 | 11.19 | 9.00 | 69.5 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.03 | 15.21 | 24.45 | 9.00 | 82.7 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.65 | 14.71 | 23.17 | 2.00 | 68.1 | 78.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 3.06 | 9.33 | 15.09 | 2.00 | 58.7 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.72 | 21.29 | 34.32 | 3.00 | 94.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.33 | 15.15 | 23.53 | 10.00 | 76.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.55 | 14.91 | 22.38 | 2.00 | 81.1 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.53 | 14.23 | 23.26 | 0.00 | 44.4 | 0.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.28 | 11.83 | 18.22 | 3.00 | 77.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.29
- Actual score: 53.00
- League average score: 0.00
- Transfer: Cole Palmer -> Bryan Mbeumo (projected gain 6.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.62 | 10.93 | 17.86 | 2.00 | 86.7 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.5 | 3.47 | 10.41 | 17.15 | 10.00 | 91.1 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.37 | 12.91 | 19.92 | 6.00 | 75.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.48 | 12.87 | 19.59 | 8.00 | 83.0 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.21 | 9.44 | 14.98 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.89 | 8.36 | 13.00 | 0.00 | 71.0 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.55 | 8.02 | 13.35 | 0.00 | 32.3 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.43 | 16.53 | 25.49 | 7.00 | 79.0 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 4.27 | 12.87 | 20.38 | 2.00 | 59.7 | 71.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.76 | 8.33 | 13.76 | 0.00 | 57.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.78 | 20.36 | 33.13 | 9.00 | 88.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.09 | 15.78 | 24.80 | 2.00 | 76.6 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.81 | 14.91 | 24.14 | 2.00 | 81.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.65 | 13.73 | 21.76 | 3.00 | 86.3 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.82 | 10.85 | 16.81 | 1.00 | 76.2 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 2.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.69
- Actual score: 58.00
- League average score: 0.00
- Transfer: Anton Stach -> Antoine Semenyo (projected gain 6.94, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.43 | 10.62 | 17.46 | -3.00 | 85.7 | 4.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.54 | 10.52 | 17.33 | 2.00 | 92.1 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.62 | 13.74 | 22.03 | 1.00 | 85.7 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.57 | 13.18 | 20.57 | 4.00 | 82.2 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.20 | 9.02 | 14.43 | 4.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.69 | 7.50 | 11.64 | 4.00 | 67.6 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.88 | 5.84 | 9.72 | 1.00 | 22.1 | 53.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.77 | 17.27 | 27.82 | 2.00 | 84.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.8 | 3.78 | 11.78 | 19.02 | 8.00 | 51.3 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.66 | 5.21 | 8.88 | 1.00 | 29.3 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.78 | 20.39 | 33.26 | 5.00 | 88.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.4 | 5.51 | 16.47 | 25.76 | 5.00 | 72.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.31 | 15.15 | 24.40 | 10.00 | 79.1 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.90 | 14.27 | 23.30 | 3.00 | 78.6 | 69.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.92 | 12.36 | 20.39 | 9.00 | 82.3 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.60
- Actual score: 33.00
- League average score: 0.00
- Transfer: none
- No transfer was applied this week.
- Autosub outfielders: Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.17 | 9.60 | 15.99 | 10.00 | 87.4 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.41 | 7.55 | 12.95 | 1.00 | 51.8 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.58 | 13.44 | 21.49 | 1.00 | 90.4 | 27.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.19 | 12.74 | 21.84 | 2.00 | 74.8 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 2.89 | 8.84 | 14.39 | 3.00 | 86.1 | 90.0 |
| Bench 2 | Autosub In | Daniel Ballard | DEF | 17 | 4.6 | 2.83 | 7.03 | 12.24 | 1.00 | 35.6 | 15.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.43 | 6.88 | 12.18 | 1.00 | 76.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.20 | 18.21 | 28.82 | 2.00 | 95.0 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 8.8 | 3.96 | 12.48 | 19.74 | 0.00 | 59.8 | 0.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.48 | 4.72 | 9.03 | 0.00 | 28.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.26 | 18.58 | 31.73 | 2.00 | 86.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.69 | 18.19 | 27.75 | 7.00 | 86.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.33 | 15.04 | 25.04 | -1.00 | 77.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.82 | 13.97 | 22.28 | 2.00 | 92.3 | 82.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.26 | 12.35 | 21.27 | 2.00 | 68.6 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 63.01
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (7.44).
- League average score: 0.00
- Transfer: Daniel Ballard -> Michael Keane (projected gain 4.23, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (7.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.40 | 10.38 | 17.28 | 2.00 | 92.6 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.58 | 7.84 | 13.41 | 2.00 | 67.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.22 | 12.44 | 20.58 | 1.00 | 88.3 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.5 | 4.32 | 11.77 | 19.04 | 4.00 | 83.3 | 64.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 3.65 | 10.94 | 18.83 | 7.00 | 60.3 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.37 | 9.66 | 14.65 | 1.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.74 | 7.63 | 11.94 | 1.00 | 74.7 | 78.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.45 | 16.62 | 27.86 | 2.00 | 89.9 | 73.0 |
| Bench 3 | Bench | Hugo Ekitiké | FWD | 12 | 8.7 | 2.00 | 6.88 | 12.35 | 1.00 | 21.3 | 16.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.01 | 3.82 | 7.43 | 1.00 | 20.3 | 32.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 6.29 | 18.81 | 30.10 | 18.00 | 93.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.67 | 17.11 | 28.91 | 2.00 | 77.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.22 | 15.07 | 24.94 | 3.00 | 69.4 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.36 | 13.11 | 20.60 | 3.00 | 76.4 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.48 | 12.75 | 20.74 | 6.00 | 73.8 | 76.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 66.94
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.42) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Pascal Struijk -> Nordi Mukiele (projected gain 3.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.42) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 3.68 | 10.17 | 16.51 | 7.00 | 87.5 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.70 | 7.99 | 13.33 | 5.00 | 71.4 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.17 | 12.15 | 20.16 | 1.00 | 79.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 4.31 | 11.79 | 18.47 | 17.00 | 81.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.25 | 11.69 | 19.07 | 3.00 | 92.0 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.5 | 3.05 | 9.59 | 15.90 | 1.00 | 74.3 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.66 | 7.19 | 11.08 | 1.00 | 69.2 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.72 | 14.57 | 25.04 | 2.00 | 78.6 | 90.0 |
| Bench 2 | Bench Boost | Hugo Ekitiké | FWD | 12 | 8.7 | 2.67 | 8.20 | 14.11 | 1.00 | 33.7 | 28.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.36 | 6.25 | 10.34 | 1.00 | 36.6 | 14.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 6.95 | 20.36 | 33.05 | 4.00 | 105.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.51 | 16.71 | 28.48 | 2.00 | 74.4 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.50 | 14.47 | 24.10 | 8.00 | 75.9 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.01 | 12.50 | 20.65 | 9.00 | 69.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.8 | 4.45 | 12.49 | 20.52 | 1.00 | 77.7 | 58.0 |