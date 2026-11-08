# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 433.12
- Total actual points: 412.00
- Average predicted points: 61.87
- Average actual points: 58.86
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
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.59 | 13.32 | 21.77 | 1.00 | 99.3 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 4.40 | 12.89 | 21.11 | 2.00 | 99.0 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.5 | 7.20 | 20.87 | 34.21 | 1.00 | 119.8 | 8.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.75 | 13.98 | 22.85 | 3.00 | 103.8 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.34 | 13.29 | 21.90 | 5.00 | 96.9 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 4.17 | 12.68 | 20.71 | -1.00 | 92.6 | 90.0 |
| Bench 4 | Bench | Pascal Struijk | DEF | 11 | 4.5 | 4.06 | 12.67 | 20.97 | 0.00 | 95.8 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.5 | 5.87 | 17.38 | 28.71 | 9.00 | 83.1 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.45 | 15.73 | 25.70 | 15.00 | 81.9 | 90.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.54 | 12.97 | 21.21 | 2.00 | 81.2 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.98 | 23.61 | 39.03 | 5.00 | 110.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.79 | 19.74 | 32.28 | 0.00 | 101.1 | 0.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 6.54 | 19.14 | 31.40 | 2.00 | 115.5 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.61 | 16.70 | 27.67 | 2.00 | 99.5 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 5.41 | 16.45 | 26.77 | 2.00 | 99.5 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.82
- Actual score: 59.00
- League average score: 51.00
- Transfer: Anton Stach -> Josh Cullen (projected gain 1.73, hit 0)
- Autosub outfielders: Eliezer Mayenda Dossou, Pascal Struijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 3.16 | 9.96 | 16.25 | 2.00 | 89.1 | 90.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.16 | 9.39 | 15.39 | 8.00 | 84.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.35 | 12.72 | 18.86 | 8.00 | 80.8 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.14 | 12.64 | 20.03 | 4.00 | 85.1 | 70.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.6 | 4.01 | 12.06 | 18.92 | 0.00 | 46.8 | 0.0 |
| Bench 3 | Autosub In | Pascal Struijk | DEF | 11 | 4.5 | 2.76 | 8.58 | 13.40 | 6.00 | 76.8 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.40 | 7.49 | 11.21 | 9.00 | 69.4 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.02 | 15.13 | 24.30 | 9.00 | 83.2 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.64 | 14.71 | 23.16 | 2.00 | 68.2 | 78.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 3.06 | 9.34 | 15.12 | 2.00 | 58.8 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.72 | 21.27 | 34.29 | 3.00 | 94.3 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.33 | 15.15 | 23.55 | 10.00 | 76.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.56 | 14.94 | 22.44 | 2.00 | 80.9 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.54 | 14.25 | 23.30 | 0.00 | 44.3 | 0.0 |
| XI | XI | Josh Cullen | MID | 3 | 5.0 | 4.62 | 13.55 | 21.10 | 2.00 | 91.9 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.38
- Actual score: 63.00
- League average score: 0.00
- Transfer: Cole Palmer -> Bryan Mbeumo (projected gain 6.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.46 | 10.40 | 17.12 | 10.00 | 91.1 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 3.07 | 9.04 | 14.79 | 0.00 | 87.6 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.37 | 12.93 | 19.95 | 6.00 | 75.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.48 | 12.87 | 19.58 | 8.00 | 83.0 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.21 | 9.45 | 14.99 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.90 | 8.37 | 13.02 | 0.00 | 71.0 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.56 | 8.03 | 13.37 | 0.00 | 32.3 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.42 | 16.47 | 25.38 | 7.00 | 79.3 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 4.27 | 12.88 | 20.41 | 2.00 | 59.7 | 71.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.76 | 8.31 | 13.73 | 0.00 | 57.3 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.78 | 20.35 | 33.11 | 9.00 | 88.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.09 | 15.79 | 24.83 | 2.00 | 76.5 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.81 | 14.90 | 24.13 | 2.00 | 81.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.65 | 13.74 | 21.80 | 3.00 | 86.2 | 90.0 |
| XI | XI | Josh Cullen | MID | 3 | 5.0 | 4.06 | 11.52 | 17.54 | 3.00 | 81.1 | 62.0 |

## GW5

- Train rows: 164124
- Bank: 2.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.70
- Actual score: 58.00
- League average score: 0.00
- Transfer: Josh Cullen -> Antoine Semenyo (projected gain 7.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.54 | 10.51 | 17.30 | 2.00 | 92.2 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 1.16 | 4.68 | 8.46 | 0.00 | 47.1 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.62 | 13.75 | 22.07 | 1.00 | 85.7 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.57 | 13.18 | 20.56 | 4.00 | 82.2 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.20 | 9.03 | 14.45 | 4.00 | 80.2 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.69 | 7.53 | 11.69 | 4.00 | 67.5 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.88 | 5.85 | 9.74 | 1.00 | 22.0 | 53.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.76 | 17.23 | 27.74 | 2.00 | 84.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.8 | 3.78 | 11.79 | 19.04 | 8.00 | 51.3 | 66.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.66 | 5.21 | 8.87 | 1.00 | 29.5 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.78 | 20.39 | 33.27 | 5.00 | 88.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.4 | 5.52 | 16.49 | 25.79 | 5.00 | 72.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.31 | 15.15 | 24.41 | 10.00 | 79.1 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.91 | 14.28 | 23.32 | 3.00 | 78.6 | 69.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.92 | 12.36 | 20.39 | 9.00 | 82.2 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.67
- Actual score: 33.00
- League average score: 0.00
- Transfer: none
- No transfer was applied this week.
- Autosub outfielders: Daniel Ballard.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.17 | 9.59 | 15.96 | 10.00 | 87.5 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 4.9 | 1.40 | 3.98 | 7.18 | 0.00 | 32.1 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.60 | 13.47 | 21.54 | 1.00 | 90.3 | 27.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.20 | 12.81 | 21.85 | 2.00 | 75.0 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 2.91 | 8.91 | 14.45 | 3.00 | 86.0 | 90.0 |
| Bench 2 | Autosub In | Daniel Ballard | DEF | 17 | 4.6 | 2.83 | 7.05 | 12.24 | 1.00 | 35.6 | 15.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.48 | 7.03 | 12.26 | 1.00 | 76.2 | 90.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.17 | 18.11 | 28.73 | 2.00 | 94.9 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 8.8 | 3.94 | 12.41 | 19.71 | 0.00 | 59.8 | 0.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.50 | 4.77 | 9.03 | 0.00 | 28.7 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.28 | 18.67 | 31.78 | 2.00 | 86.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.68 | 18.15 | 27.76 | 7.00 | 85.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.33 | 15.06 | 25.06 | -1.00 | 77.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.82 | 13.97 | 22.28 | 2.00 | 92.2 | 82.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.28 | 12.43 | 21.32 | 2.00 | 68.8 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 63.03
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.32) beats the best remaining Triple Captain opportunity (7.45).
- League average score: 0.00
- Transfer: Daniel Ballard -> Michael Keane (projected gain 4.19, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.32) beats the best remaining Triple Captain opportunity (7.45).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.39 | 10.37 | 17.26 | 2.00 | 92.5 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 4.8 | 0.67 | 2.73 | 5.29 | 0.00 | 19.2 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.23 | 12.46 | 20.59 | 1.00 | 88.4 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.5 | 4.31 | 11.75 | 19.01 | 4.00 | 83.3 | 64.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 3.65 | 10.94 | 18.84 | 7.00 | 60.2 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.38 | 9.67 | 14.68 | 1.00 | 85.6 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.74 | 7.65 | 11.96 | 1.00 | 74.7 | 78.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.46 | 16.65 | 27.89 | 2.00 | 90.0 | 73.0 |
| Bench 3 | Bench | Hugo Ekitiké | FWD | 12 | 8.7 | 1.99 | 6.87 | 12.35 | 1.00 | 21.4 | 16.0 |
| Bench 4 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.01 | 3.82 | 7.41 | 1.00 | 20.3 | 32.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 6.29 | 18.83 | 30.13 | 18.00 | 93.0 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.67 | 17.11 | 28.93 | 2.00 | 77.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.21 | 15.06 | 24.93 | 3.00 | 69.3 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.36 | 13.13 | 20.63 | 3.00 | 76.4 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.49 | 12.76 | 20.76 | 6.00 | 73.8 | 76.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 65.01
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (8.46) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Pascal Struijk -> Nordi Mukiele (projected gain 3.18, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (8.46) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 3.68 | 10.15 | 16.48 | 7.00 | 87.5 | 90.0 |
| Bench 1 | Bench Boost | James Trafford | GK | 13 | 4.8 | 0.74 | 2.53 | 4.74 | 0.00 | 16.7 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.17 | 12.16 | 20.18 | 1.00 | 79.2 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 4.32 | 11.79 | 18.48 | 17.00 | 81.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.25 | 11.70 | 19.09 | 3.00 | 92.0 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.5 | 3.06 | 9.59 | 15.91 | 1.00 | 74.4 | 90.0 |
| Bench 3 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.66 | 7.19 | 11.09 | 1.00 | 69.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.72 | 14.57 | 25.02 | 2.00 | 78.9 | 90.0 |
| Bench 2 | Bench Boost | Hugo Ekitiké | FWD | 12 | 8.7 | 2.67 | 8.20 | 14.09 | 1.00 | 33.8 | 28.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.35 | 6.23 | 10.32 | 1.00 | 36.6 | 14.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 6.96 | 20.37 | 33.06 | 4.00 | 105.7 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.51 | 16.72 | 28.49 | 2.00 | 74.4 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.50 | 14.46 | 24.10 | 8.00 | 75.9 | 84.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.02 | 12.51 | 20.66 | 9.00 | 69.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.8 | 4.46 | 12.50 | 20.53 | 1.00 | 77.7 | 58.0 |