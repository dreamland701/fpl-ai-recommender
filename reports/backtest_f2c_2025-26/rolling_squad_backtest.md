# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW8
- Total predicted points: 434.49
- Total actual points: 400.00
- Average predicted points: 62.07
- Average actual points: 57.14
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
- Predicted score: 74.69
- Actual score: 47.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 81.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Eliezer Mayenda Dossou.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 4.74 | 13.83 | 22.61 | 2.00 | 103.6 | 90.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.76 | 13.83 | 22.57 | 1.00 | 101.5 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.5 | 7.40 | 21.47 | 35.18 | 1.00 | 122.5 | 8.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.95 | 14.61 | 23.94 | 3.00 | 107.1 | 90.0 |
| Bench 3 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.60 | 14.08 | 23.07 | 5.00 | 101.0 | 90.0 |
| XI | XI | Aaron Wan-Bissaka | DEF | 19 | 4.5 | 4.62 | 13.19 | 21.34 | 0.00 | 99.6 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 4.28 | 13.00 | 21.24 | -1.00 | 94.3 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.5 | 6.05 | 17.94 | 29.69 | 9.00 | 86.2 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.57 | 16.30 | 26.75 | 15.00 | 83.1 | 90.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.71 | 13.50 | 22.05 | 2.00 | 83.1 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 8.14 | 24.10 | 39.88 | 5.00 | 113.9 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 6.88 | 20.11 | 32.92 | 2.00 | 120.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.86 | 19.93 | 32.63 | 0.00 | 104.0 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.78 | 17.12 | 28.19 | 2.00 | 100.6 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 5.53 | 16.84 | 27.42 | 2.00 | 101.1 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.42
- Actual score: 61.00
- League average score: 0.00
- Transfer: James Trafford -> Robert Lynch Sánchez (projected gain 1.91, hit 0)
- Autosub outfielders: Eliezer Mayenda Dossou, Gabriel Gudmundsson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.96 | 11.76 | 18.83 | 6.00 | 91.8 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.5 | 3.32 | 9.85 | 16.07 | 8.00 | 86.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.32 | 12.61 | 18.67 | 8.00 | 79.9 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.12 | 12.57 | 19.88 | 4.00 | 85.4 | 70.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.6 | 4.08 | 12.22 | 19.11 | 0.00 | 47.9 | 0.0 |
| Bench 2 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.5 | 3.34 | 10.25 | 16.58 | 0.00 | 84.7 | 0.0 |
| Bench 4 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.31 | 7.24 | 10.80 | 9.00 | 68.8 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.12 | 15.54 | 24.97 | 9.00 | 83.8 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.74 | 14.98 | 23.60 | 2.00 | 69.0 | 78.0 |
| Bench 3 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 3.16 | 9.59 | 15.45 | 2.00 | 59.8 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.75 | 21.35 | 34.42 | 3.00 | 94.2 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.56 | 14.91 | 22.43 | 2.00 | 81.7 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.15 | 14.63 | 22.68 | 10.00 | 74.2 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.62 | 14.46 | 23.60 | 0.00 | 46.0 | 0.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 4.26 | 11.79 | 18.16 | 3.00 | 78.1 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.79
- Actual score: 51.00
- League average score: 0.00
- Transfer: Cole Palmer -> Bryan Mbeumo (projected gain 6.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.77 | 11.37 | 18.57 | 2.00 | 89.1 | 90.0 |
| Bench 1 | Bench | Robin Roefs | GK | 17 | 4.5 | 3.54 | 10.65 | 17.53 | 10.00 | 92.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.42 | 12.69 | 19.30 | 8.00 | 82.1 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.27 | 12.63 | 19.46 | 6.00 | 74.7 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.84 | 8.20 | 12.73 | 0.00 | 70.5 | 90.0 |
| Bench 3 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 2.59 | 8.12 | 13.51 | 0.00 | 33.2 | 0.0 |
| Bench 4 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 2.19 | 6.82 | 11.65 | 0.00 | 44.2 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.47 | 16.72 | 25.79 | 7.00 | 79.7 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.7 | 4.28 | 12.87 | 20.39 | 2.00 | 59.8 | 71.0 |
| Bench 2 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.81 | 8.47 | 13.99 | 0.00 | 57.6 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.74 | 20.27 | 33.00 | 9.00 | 87.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.99 | 15.49 | 24.31 | 2.00 | 75.2 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.82 | 14.93 | 24.15 | 2.00 | 81.0 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.65 | 13.73 | 21.80 | 3.00 | 86.7 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 3.79 | 10.77 | 16.67 | 1.00 | 76.0 | 90.0 |

## GW5

- Train rows: 164124
- Bank: 2.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 57.75
- Actual score: 58.00
- League average score: 0.00
- Transfer: Anton Stach -> Antoine Semenyo (projected gain 6.95, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 3.46 | 10.73 | 17.64 | -3.00 | 86.7 | 4.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.57 | 10.61 | 17.50 | 2.00 | 92.6 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.53 | 13.50 | 21.63 | 1.00 | 85.0 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.53 | 13.07 | 20.33 | 4.00 | 81.3 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.60 | 7.27 | 11.25 | 4.00 | 66.8 | 90.0 |
| Bench 2 | Bench | Daniel Ballard | DEF | 17 | 4.6 | 1.89 | 5.88 | 9.79 | 1.00 | 22.7 | 53.0 |
| Bench 4 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.4 | 1.64 | 5.16 | 9.17 | 0.00 | 32.2 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 5.75 | 17.27 | 27.77 | 2.00 | 84.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.8 | 3.76 | 11.72 | 18.87 | 8.00 | 50.7 | 66.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.66 | 5.23 | 8.92 | 1.00 | 29.4 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.74 | 20.28 | 33.06 | 5.00 | 87.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.4 | 5.46 | 16.32 | 25.52 | 5.00 | 72.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.23 | 14.90 | 23.99 | 10.00 | 77.9 | 86.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.90 | 14.26 | 23.26 | 3.00 | 78.5 | 69.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 3.92 | 12.35 | 20.40 | 9.00 | 82.3 | 90.0 |

## GW6

- Train rows: 164865
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.24
- Actual score: 31.00
- League average score: 0.00
- Transfer: none
- No transfer was applied this week.
- Autosub outfielders: Gabriel Gudmundsson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.20 | 9.67 | 16.12 | 10.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 5.0 | 2.44 | 7.66 | 13.10 | 1.00 | 52.4 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.52 | 13.26 | 21.19 | 1.00 | 89.7 | 27.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.17 | 12.66 | 21.73 | 2.00 | 74.4 | 90.0 |
| XI | XI | Daniel Ballard | DEF | 17 | 4.6 | 2.84 | 7.01 | 12.24 | 1.00 | 35.8 | 15.0 |
| Bench 2 | Autosub In | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.38 | 6.73 | 11.97 | 1.00 | 75.5 | 90.0 |
| Bench 4 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.3 | 0.96 | 3.15 | 7.49 | 0.00 | 19.4 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 6.20 | 18.29 | 28.89 | 2.00 | 95.2 | 90.0 |
| XI | Bench | Hugo Ekitiké | FWD | 12 | 8.8 | 3.94 | 12.43 | 19.64 | 0.00 | 59.4 | 0.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.49 | 4.72 | 9.07 | 0.00 | 28.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.21 | 18.46 | 31.55 | 2.00 | 85.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.6 | 5.66 | 18.12 | 27.62 | 7.00 | 85.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.23 | 14.77 | 24.58 | -1.00 | 76.8 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.84 | 14.01 | 22.36 | 2.00 | 92.5 | 82.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.22 | 12.25 | 21.12 | 2.00 | 68.3 | 90.0 |

## GW7

- Train rows: 165607
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: triple_captain
- Predicted score: 61.98
- Actual score: 85.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (7.44).
- League average score: 0.00
- Transfer: Daniel Ballard -> Michael Keane (projected gain 5.85, hit 0)
- Chip used: Triple Captain on Antoine Semenyo. Optimizer chose Triple Captain here because the current estimated captain upside (6.31) beats the best remaining Triple Captain opportunity (7.44).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.39 | 10.37 | 17.24 | 2.00 | 92.5 | 90.0 |
| Bench 1 | Bench | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.59 | 7.87 | 13.43 | 2.00 | 67.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.19 | 12.33 | 20.43 | 1.00 | 87.9 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.5 | 4.34 | 11.80 | 19.08 | 4.00 | 83.5 | 64.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 3.63 | 10.83 | 18.65 | 7.00 | 60.0 | 90.0 |
| XI | XI | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.70 | 7.51 | 11.77 | 1.00 | 74.3 | 78.0 |
| Bench 4 | Bench | Aaron Wan-Bissaka | DEF | 19 | 4.3 | 0.70 | 3.35 | 6.88 | 1.00 | 20.9 | 78.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.8 | 5.42 | 16.57 | 27.76 | 2.00 | 89.7 | 73.0 |
| Bench 2 | Bench | Hugo Ekitiké | FWD | 12 | 8.7 | 1.94 | 6.68 | 12.05 | 1.00 | 20.3 | 16.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 0.98 | 3.77 | 7.31 | 1.00 | 19.9 | 32.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.7 | 6.28 | 18.80 | 30.08 | 18.00 | 93.1 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.60 | 16.93 | 28.58 | 2.00 | 77.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.09 | 14.69 | 24.32 | 3.00 | 67.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.7 | 4.35 | 13.07 | 20.54 | 3.00 | 76.2 | 75.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 4.43 | 12.60 | 20.47 | 6.00 | 73.2 | 76.0 |

## GW8

- Train rows: 166350
- Bank: 0.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Mohamed Salah
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 66.62
- Actual score: 67.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.33) beats the best remaining Bench Boost opportunity (0.00).
- League average score: 0.00
- Transfer: Aaron Wan-Bissaka -> Nordi Mukiele (projected gain 4.48, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.33) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.6 | 3.66 | 10.11 | 16.41 | 7.00 | 87.2 | 90.0 |
| Bench 1 | Bench Boost | Robert Lynch Sánchez | GK | 7 | 4.9 | 2.71 | 8.02 | 13.40 | 5.00 | 71.6 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.6 | 4.15 | 12.08 | 20.05 | 1.00 | 79.1 | 90.0 |
| XI | XI | Nordi Mukiele | DEF | 17 | 4.0 | 4.25 | 11.62 | 18.17 | 17.00 | 80.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.20 | 11.56 | 18.87 | 3.00 | 91.3 | 90.0 |
| XI | XI | Michael Keane | DEF | 9 | 4.5 | 3.07 | 9.61 | 15.97 | 1.00 | 74.5 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.65 | 7.17 | 11.07 | 1.00 | 69.1 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 4.71 | 14.57 | 25.06 | 2.00 | 78.3 | 90.0 |
| Bench 3 | Bench Boost | Hugo Ekitiké | FWD | 12 | 8.7 | 2.61 | 7.99 | 13.78 | 1.00 | 32.5 | 28.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.33 | 6.20 | 10.23 | 1.00 | 36.2 | 14.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 7.8 | 7.00 | 20.47 | 33.25 | 4.00 | 106.5 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 14.5 | 5.42 | 16.45 | 28.07 | 2.00 | 73.1 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 4.40 | 14.17 | 23.62 | 8.00 | 74.5 | 84.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.8 | 4.50 | 12.61 | 20.70 | 1.00 | 78.2 | 58.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.1 | 3.97 | 12.39 | 20.45 | 9.00 | 69.2 | 90.0 |