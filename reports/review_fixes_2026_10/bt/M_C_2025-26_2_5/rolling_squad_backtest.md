# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW1
- Simulated weeks: GW2-GW5
- Total predicted points: 261.04
- Total actual points: 247.00
- Average predicted points: 65.26
- Average actual points: 61.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 161967
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Daniel Ballard
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 72.48
- Actual score: 52.00
- Chip advisory: bench_boost (0.67): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 4.63 | 10.78 | 17.79 | 1.00 | 99.2 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 4.37 | 10.26 | 17.02 | 2.00 | 99.1 | 90.0 |
| Vice Captain | XI | Daniel Ballard | DEF | 17 | 4.5 | 7.24 | 18.29 | 30.19 | 1.00 | 119.6 | 8.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.74 | 11.46 | 18.93 | 3.00 | 103.6 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.33 | 10.77 | 17.98 | 5.00 | 96.8 | 90.0 |
| Bench 3 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 4.20 | 10.15 | 16.73 | -1.00 | 92.6 | 90.0 |
| Bench 4 | Bench | Pascal Struijk | DEF | 11 | 4.5 | 4.08 | 10.06 | 16.85 | 0.00 | 96.1 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.5 | 5.85 | 14.80 | 24.68 | 9.00 | 82.8 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.46 | 13.43 | 22.21 | 15.00 | 80.5 | 90.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 4.59 | 10.51 | 17.36 | 2.00 | 80.8 | 62.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 7.96 | 21.02 | 34.98 | 5.00 | 110.6 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 6.76 | 17.07 | 28.09 | 0.00 | 101.4 | 0.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 6.50 | 16.45 | 27.18 | 2.00 | 115.7 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.60 | 14.08 | 23.57 | 2.00 | 99.8 | 90.0 |
| XI | XI | Anton Stach | MID | 11 | 5.0 | 5.45 | 13.91 | 22.80 | 2.00 | 99.3 | 90.0 |

## GW3

- Train rows: 162672
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Bruno Borges Fernandes
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 58.09
- Actual score: 59.00
- Transfer: Anton Stach -> Josh Cullen (projected gain 1.81, hit 0)
- Autosub: Pascal Struijk replaced Daniel Ballard.
- Autosub: Eliezer Mayenda Dossou replaced Cole Palmer.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 3.17 | 8.46 | 13.96 | 2.00 | 89.1 | 90.0 |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.18 | 7.90 | 13.12 | 8.00 | 84.5 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.16 | 11.51 | 18.77 | 4.00 | 85.1 | 70.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.39 | 10.61 | 17.29 | 8.00 | 80.8 | 90.0 |
| XI | Bench | Daniel Ballard | DEF | 17 | 4.5 | 4.03 | 10.14 | 16.68 | 0.00 | 46.9 | 0.0 |
| Bench 3 | Autosub In | Pascal Struijk | DEF | 11 | 4.5 | 2.73 | 7.47 | 12.33 | 6.00 | 77.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.38 | 6.45 | 10.36 | 9.00 | 69.6 | 79.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.04 | 14.02 | 22.95 | 9.00 | 82.4 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.5 | 4.68 | 13.43 | 21.45 | 2.00 | 68.0 | 78.0 |
| Bench 2 | Autosub In | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 3.08 | 8.04 | 13.33 | 2.00 | 58.7 | 64.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.76 | 20.30 | 33.39 | 3.00 | 94.1 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.5 | 4.57 | 13.62 | 20.75 | 2.00 | 81.2 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.36 | 13.58 | 22.21 | 10.00 | 76.8 | 90.0 |
| XI | Bench | Cole Palmer | MID | 7 | 10.5 | 4.53 | 12.86 | 21.43 | 0.00 | 44.5 | 0.0 |
| XI | XI | Josh Cullen | MID | 3 | 5.0 | 4.61 | 11.73 | 19.18 | 2.00 | 91.8 | 90.0 |

## GW4

- Train rows: 163384
- Bank: 0.00 -> 2.40
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: triple_captain
- Predicted score: 64.29
- Actual score: 72.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.84) beats the best remaining Triple Captain opportunity (8.38).
- Transfer: Cole Palmer -> Bryan Mbeumo (projected gain 6.65, hit 0)
- Chip used: Triple Captain on Mohamed Salah. Optimizer chose Triple Captain here because the current estimated captain upside (6.84) beats the best remaining Triple Captain opportunity (8.38).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.48 | 11.97 | 15.60 | 10.00 | 91.0 | 90.0 |
| Bench 1 | Bench | James Trafford | GK | 13 | 5.0 | 3.05 | 10.50 | 13.15 | 0.00 | 87.7 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.34 | 13.80 | 18.01 | 6.00 | 75.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.52 | 13.29 | 17.59 | 8.00 | 83.0 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.21 | 10.95 | 13.80 | 2.00 | 81.7 | 90.0 |
| Bench 2 | Bench | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.89 | 9.85 | 11.84 | 0.00 | 71.1 | 90.0 |
| Bench 4 | Bench | Daniel Ballard | DEF | 17 | 4.5 | 2.56 | 8.94 | 11.30 | 0.00 | 32.4 | 0.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 5.46 | 18.16 | 24.53 | 7.00 | 78.7 | 78.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 4.30 | 14.45 | 19.03 | 2.00 | 59.7 | 71.0 |
| Bench 3 | Bench | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 2.78 | 9.92 | 12.43 | 0.00 | 56.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.81 | 22.08 | 32.20 | 9.00 | 87.9 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.79 | 16.43 | 22.75 | 2.00 | 81.1 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.07 | 16.12 | 22.57 | 2.00 | 76.7 | 90.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 4.63 | 15.20 | 20.43 | 3.00 | 86.4 | 90.0 |
| XI | XI | Josh Cullen | MID | 3 | 5.0 | 4.06 | 11.80 | 15.00 | 3.00 | 81.1 | 62.0 |

## GW5

- Train rows: 164124
- Bank: 2.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: João Pedro Junqueira de Jesus
- Effective captain: Mohamed Salah
- Chip used: bench_boost
- Predicted score: 66.18
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.47) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Josh Cullen -> Antoine Semenyo (projected gain 7.46, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.47) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Robin Roefs | GK | 17 | 4.5 | 3.58 | 11.30 | 16.15 | 2.00 | 92.0 | 90.0 |
| Bench 1 | Bench Boost | James Trafford | GK | 13 | 5.0 | 1.19 | 5.42 | 7.27 | 0.00 | 47.1 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.5 | 4.63 | 13.80 | 20.14 | 1.00 | 85.8 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.0 | 4.58 | 12.97 | 18.50 | 4.00 | 82.3 | 90.0 |
| XI | XI | Pascal Struijk | DEF | 11 | 4.5 | 3.16 | 9.16 | 13.22 | 4.00 | 80.3 | 90.0 |
| Bench 2 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 4.0 | 2.65 | 7.70 | 10.38 | 4.00 | 67.8 | 90.0 |
| Bench 3 | Bench Boost | Daniel Ballard | DEF | 17 | 4.5 | 1.91 | 6.36 | 8.21 | 1.00 | 22.1 | 53.0 |
| Vice Captain | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.6 | 5.77 | 17.68 | 26.78 | 2.00 | 84.5 | 90.0 |
| XI | XI | Hugo Ekitiké | FWD | 12 | 8.6 | 3.78 | 12.33 | 17.90 | 8.00 | 51.3 | 66.0 |
| Bench 4 | Bench Boost | Eliezer Mayenda Dossou | FWD | 17 | 5.5 | 1.70 | 5.89 | 7.82 | 1.00 | 29.2 | 10.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 14.5 | 6.78 | 20.97 | 32.38 | 5.00 | 88.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 7.4 | 5.49 | 16.70 | 24.53 | 5.00 | 73.0 | 90.0 |
| XI | XI | Bryan Mbeumo | MID | 14 | 8.0 | 4.91 | 14.83 | 22.06 | 3.00 | 78.6 | 69.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 5.32 | 14.75 | 21.79 | 10.00 | 79.1 | 86.0 |
| XI | XI | Tijjani Reijnders | MID | 13 | 5.6 | 3.95 | 12.71 | 19.29 | 9.00 | 82.3 | 90.0 |