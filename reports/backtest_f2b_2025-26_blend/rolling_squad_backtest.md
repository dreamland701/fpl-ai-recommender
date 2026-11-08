# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 435.16
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
- Predicted score: 72.53
- Actual score: 52.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Eliezer Mayenda Dossou.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.59 | 13.33 | 21.80 | 1.00 | 99.2 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 4.40 | 12.88 | 21.10 | 2.00 | 99.0 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.5 | 7.20 | 20.89 | 34.26 | 1.00 | 119.7 | 8.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.76 | 14.04 | 22.96 | 3.00 | 103.6 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.34 | 13.32 | 21.96 | 5.00 | 96.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 4.16 | 12.67 | 20.69 | -1.00 | 92.7 | 90.0 |
| Bench 4 | Bench | Pascal Struijk | DEF | 11 | 4.5 | 4.05 | 12.59 | 20.84 | 0.00 | 96.2 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.5 | 5.87 | 17.39 | 28.74 | 9.00 | 82.8 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.49 | 16.01 | 26.24 | 15.00 | 80.4 | 90.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.55 | 13.01 | 21.30 | 2.00 | 80.8 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.98 | 23.60 | 39.01 | 5.00 | 110.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.78 | 19.67 | 32.16 | 0.00 | 101.4 | 0.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 6.53 | 19.10 | 31.32 | 2.00 | 115.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.60 | 16.65 | 27.58 | 2.00 | 99.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 5.41 | 16.49 | 26.85 | 2.00 | 99.3 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.15
- Actual score: 58.00
- League average score: 0.00
- Transfer: James Trafford -> Robert Lynch Sánchez (projected gain 1.94, hit 0)
- Autosub outfielders: Eliezer Mayenda Dossou, Pascal Struijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.82 | 11.34 | 18.18 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.5 | 3.16 | 9.40 | 15.41 | 8.00 | 84.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.35 | 12.74 | 18.89 | 8.00 | 80.8 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.14 | 12.63 | 20.02 | 4.00 | 85.2 | 70.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.6 | 4.01 | 12.01 | 18.83 | 0.00 | 47.0 | 0.0 |
| Bench 3 | Autosub In | Pascal Struijk | DEF | 11 | 4.5 | 2.75 | 8.53 | 13.31 | 6.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.40 | 7.47 | 11.17 | 9.00 | 69.6 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.04 | 15.31 | 24.63 | 9.00 | 82.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.65 | 14.72 | 23.19 | 2.00 | 68.0 | 78.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 3.06 | 9.31 | 15.06 | 2.00 | 58.7 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.73 | 21.30 | 34.34 | 3.00 | 94.1 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.33 | 15.14 | 23.52 | 10.00 | 76.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.55 | 14.86 | 22.30 | 2.00 | 81.2 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.53 | 14.20 | 23.21 | 0.00 | 44.5 | 0.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.28 | 11.84 | 18.25 | 3.00 | 77.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.30
- Actual score: 53.00
- League average score: 0.00
- Transfer: Cole Palmer -> Bryan Mbeumo (projected gain 6.63, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.62 | 10.95 | 17.90 | 2.00 | 86.6 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.5 | 3.47 | 10.43 | 17.19 | 10.00 | 91.0 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.37 | 12.89 | 19.88 | 6.00 | 75.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.48 | 12.87 | 19.60 | 8.00 | 83.1 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.20 | 9.44 | 14.97 | 2.00 | 81.8 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.89 | 8.35 | 12.97 | 0.00 | 71.1 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.55 | 8.00 | 13.32 | 0.00 | 32.4 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.44 | 16.60 | 25.62 | 7.00 | 78.7 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 4.27 | 12.85 | 20.35 | 2.00 | 59.7 | 71.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.77 | 8.36 | 13.81 | 0.00 | 56.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.78 | 20.36 | 33.14 | 9.00 | 88.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.08 | 15.76 | 24.78 | 2.00 | 76.7 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.81 | 14.91 | 24.15 | 2.00 | 81.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.64 | 13.71 | 21.73 | 3.00 | 86.4 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.82 | 10.85 | 16.80 | 1.00 | 76.2 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 2.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.68
- Actual score: 58.00
- League average score: 0.00
- Transfer: Anton Stach -> Antoine Semenyo (projected gain 6.91, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.43 | 10.63 | 17.47 | -3.00 | 85.7 | 4.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.55 | 10.54 | 17.36 | 2.00 | 92.0 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.61 | 13.73 | 22.00 | 1.00 | 85.9 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.58 | 13.19 | 20.58 | 4.00 | 82.3 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.20 | 8.99 | 14.40 | 4.00 | 80.3 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.68 | 7.49 | 11.60 | 4.00 | 67.8 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.87 | 5.84 | 9.70 | 1.00 | 22.2 | 53.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.78 | 17.36 | 27.92 | 2.00 | 84.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.8 | 3.78 | 11.77 | 19.00 | 8.00 | 51.3 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.66 | 5.24 | 8.91 | 1.00 | 29.2 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.78 | 20.38 | 33.24 | 5.00 | 88.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.4 | 5.51 | 16.45 | 25.73 | 5.00 | 73.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.31 | 15.13 | 24.38 | 10.00 | 79.1 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.90 | 14.26 | 23.29 | 3.00 | 78.6 | 69.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.92 | 12.34 | 20.38 | 9.00 | 82.3 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.58
- Actual score: 33.00
- League average score: 0.00
- Transfer: none
- No transfer was applied this week.
- Autosub outfielders: Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.17 | 9.61 | 16.02 | 10.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.41 | 7.56 | 12.95 | 1.00 | 51.9 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.58 | 13.43 | 21.47 | 1.00 | 90.4 | 27.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.19 | 12.74 | 21.84 | 2.00 | 74.8 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 2.88 | 8.81 | 14.35 | 3.00 | 86.1 | 90.0 |
| Bench 2 | Autosub In | Daniel Ballard | DEF | 17 | 4.6 | 2.83 | 7.01 | 12.23 | 1.00 | 35.6 | 15.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.42 | 6.83 | 12.14 | 1.00 | 76.0 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.20 | 18.29 | 28.89 | 2.00 | 95.2 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 8.8 | 3.97 | 12.50 | 19.75 | 0.00 | 59.9 | 0.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.48 | 4.71 | 9.06 | 0.00 | 28.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.25 | 18.57 | 31.72 | 2.00 | 86.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.69 | 18.18 | 27.72 | 7.00 | 86.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.33 | 15.03 | 25.01 | -1.00 | 77.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.82 | 13.95 | 22.26 | 2.00 | 92.2 | 82.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.25 | 12.33 | 21.24 | 2.00 | 68.6 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 62.99
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (7.44).
- League average score: 0.00
- Transfer: Daniel Ballard -> Michael Keane (projected gain 4.26, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (7.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.40 | 10.40 | 17.30 | 2.00 | 92.6 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.58 | 7.84 | 13.39 | 2.00 | 67.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.22 | 12.43 | 20.58 | 1.00 | 88.3 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.5 | 4.33 | 11.78 | 19.05 | 4.00 | 83.3 | 64.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 3.65 | 10.91 | 18.79 | 7.00 | 60.4 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.37 | 9.66 | 14.63 | 1.00 | 85.7 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.73 | 7.61 | 11.92 | 1.00 | 74.7 | 78.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.45 | 16.63 | 27.87 | 2.00 | 89.9 | 73.0 |
| Bench 3 | Bench | Hugo Ekitiké | FWD | 12 | 8.7 | 2.00 | 6.87 | 12.34 | 1.00 | 21.1 | 16.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.01 | 3.84 | 7.45 | 1.00 | 20.4 | 32.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 6.28 | 18.80 | 30.08 | 18.00 | 93.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.67 | 17.12 | 28.89 | 2.00 | 78.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.22 | 15.07 | 24.92 | 3.00 | 69.5 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.36 | 13.10 | 20.58 | 3.00 | 76.4 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.48 | 12.76 | 20.72 | 6.00 | 74.0 | 76.0 |

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
- Transfer: Pascal Struijk -> Nordi Mukiele (projected gain 3.21, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.42) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 3.68 | 10.19 | 16.54 | 7.00 | 87.6 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.70 | 7.98 | 13.33 | 5.00 | 71.3 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.17 | 12.12 | 20.13 | 1.00 | 79.3 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 4.31 | 11.80 | 18.46 | 17.00 | 81.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.25 | 11.69 | 19.07 | 3.00 | 92.0 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.5 | 3.05 | 9.57 | 15.90 | 1.00 | 74.1 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.66 | 7.17 | 11.08 | 1.00 | 69.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.72 | 14.59 | 25.09 | 2.00 | 78.4 | 90.0 |
| Bench 2 | Bench Boost | Hugo Ekitiké | FWD | 12 | 8.7 | 2.68 | 8.19 | 14.11 | 1.00 | 33.5 | 28.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.36 | 6.29 | 10.38 | 1.00 | 36.7 | 14.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 6.95 | 20.35 | 33.04 | 4.00 | 105.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.51 | 16.70 | 28.47 | 2.00 | 74.3 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.50 | 14.45 | 24.09 | 8.00 | 75.9 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.01 | 12.50 | 20.64 | 9.00 | 69.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.8 | 4.45 | 12.50 | 20.52 | 1.00 | 77.8 | 58.0 |