# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 245.14
- Total actual points: 246.00
- Average predicted points: 61.28
- Average actual points: 61.50
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
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 53.04
- Actual score: 58.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Dean Henderson | GK | 8 | 5.1 | 3.15 | 11.55 | 17.78 | 2.00 | 88.8 | 90.0 |
| XI | XI | Caoimhín Kelleher | GK | 5 | 4.8 | 4.01 | 11.17 | 17.77 | 8.00 | 87.7 | 90.0 |
| XI | XI | Nathan Collins | DEF | 5 | 4.9 | 4.45 | 12.25 | 17.65 | 6.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Nico O'Reilly | DEF | 13 | 5.2 | 3.31 | 12.24 | 19.09 | 1.00 | 83.9 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.97 | 11.64 | 20.99 | 6.00 | 84.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.41 | 11.59 | 21.64 | 6.00 | 87.2 | 90.0 |
| Bench 4 | Bench | Chris Richards | DEF | 8 | 4.4 | 2.69 | 10.29 | 18.06 | 1.00 | 82.3 | 14.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.65 | 14.52 | 23.33 | 6.00 | 83.9 | 90.0 |
| Bench 2 | Bench | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.38 | 11.80 | 18.25 | 5.00 | 62.8 | 45.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.76 | 10.90 | 19.75 | 8.00 | 43.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.07 | 15.76 | 28.14 | 5.00 | 87.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.06 | 14.69 | 22.71 | 1.00 | 83.6 | 45.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.72 | 14.51 | 22.22 | 5.00 | 86.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.15 | 13.97 | 23.22 | 2.00 | 75.6 | 74.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.5 | 3.71 | 12.83 | 22.87 | 0.00 | 69.0 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Nico O'Reilly
- Vice captain: Rayan Cherki
- Effective captain: Nico O'Reilly
- Chip used: triple_captain
- Predicted score: 75.84
- Actual score: 79.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (12.11) beats the best remaining Triple Captain opportunity (7.18).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.62): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Igor Jesus Maciel da Cruz -> Dominic Calvert-Lewin (projected gain 3.90, hit 0)
- Chip used: Triple Captain on Nico O'Reilly. Optimizer chose Triple Captain here because the current estimated captain upside (12.11) beats the best remaining Triple Captain opportunity (7.18).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 5.88 | 13.17 | 19.57 | 3.00 | 167.0 | 180.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.18 | 8.57 | 14.36 | 3.00 | 87.1 | 90.0 |
| Captain | Captain | Nico O'Reilly | DEF | 13 | 5.2 | 8.31 | 17.33 | 20.33 | 5.00 | 159.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.61 | 15.58 | 25.58 | 11.00 | 86.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 3.79 | 12.27 | 20.53 | 5.00 | 85.9 | 90.0 |
| Bench 4 | Bench | Nathan Collins | DEF | 5 | 4.9 | 2.17 | 10.79 | 16.06 | 1.00 | 79.9 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.4 | 4.54 | 9.61 | 16.85 | 4.00 | 126.1 | 180.0 |
| Bench 2 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.42 | 13.12 | 22.46 | 2.00 | 86.2 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 4.59 | 13.04 | 21.95 | 7.00 | 82.6 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.31 | 9.73 | 13.91 | 2.00 | 76.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.85 | 18.74 | 30.36 | 3.00 | 86.5 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.5 | 7.84 | 18.64 | 25.61 | 5.00 | 159.5 | 70.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.59 | 15.50 | 20.02 | 12.00 | 118.9 | 180.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.3 | 3.48 | 14.60 | 20.30 | 2.00 | 65.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.72 | 10.58 | 15.23 | 12.00 | 65.3 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.02
- Actual score: 45.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: Nico O'Reilly -> Pedro Porro Sauceda (projected gain 3.07, hit 0)
- Autosub: Chris Richards replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 3.73 | 11.02 | 19.34 | 0.00 | 89.3 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.00 | 9.66 | 16.52 | 2.00 | 88.7 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.65 | 14.83 | 23.50 | 6.00 | 83.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 6.1 | 4.43 | 13.00 | 19.53 | 8.00 | 82.2 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.2 | 4.21 | 12.82 | 18.84 | 0.00 | 81.5 | 90.0 |
| Bench 3 | Bench | Nathan Collins | DEF | 5 | 4.9 | 3.53 | 10.26 | 16.33 | 3.00 | 83.8 | 90.0 |
| Bench 2 | Autosub In | Chris Richards | DEF | 8 | 4.4 | 3.58 | 9.76 | 17.33 | 0.00 | 83.2 | 29.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.90 | 15.69 | 18.71 | 7.00 | 83.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.69 | 12.49 | 22.40 | 2.00 | 83.2 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.04 | 12.09 | 19.93 | 0.00 | 78.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.11 | 16.82 | 31.11 | 9.00 | 87.9 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.3 | 4.90 | 13.47 | 21.87 | 2.00 | 73.5 | 88.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.17 | 12.42 | 20.13 | 1.00 | 79.3 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.07 | 11.96 | 19.06 | 1.00 | 53.8 | 34.0 |
| Bench 4 | Bench | Elliot Anderson | MID | 16 | 5.6 | 3.41 | 10.22 | 16.57 | 12.00 | 80.7 | 90.0 |

## GW38

- Train rows: 190183
- Bank: 0.40 -> 0.40
- Free transfers: 2 -> 2
- Captain: Antoine Semenyo
- Vice captain: Bruno Borges Fernandes
- Effective captain: Antoine Semenyo
- Chip used: bench_boost
- Predicted score: 60.24
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.35) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Rayan Cherki -> Enzo Fernández (projected gain 6.33, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.35) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Dean Henderson | GK | 8 | 5.1 | 3.28 | 10.36 | 15.45 | 2.00 | 74.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 3.02 | 9.26 | 15.35 | 6.00 | 86.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.02 | 14.83 | 22.36 | 1.00 | 84.1 | 45.0 |
| XI | XI | William Saliba | DEF | 1 | 6.2 | 3.94 | 12.31 | 19.15 | 0.00 | 84.6 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.80 | 11.49 | 19.13 | 10.00 | 88.3 | 90.0 |
| Bench 2 | Bench Boost | Nathan Collins | DEF | 5 | 4.9 | 2.94 | 11.09 | 17.23 | 3.00 | 82.6 | 90.0 |
| Bench 4 | Bench Boost | Chris Richards | DEF | 8 | 4.4 | 1.50 | 5.54 | 9.52 | 0.00 | 29.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.23 | 14.09 | 20.45 | 2.00 | 84.1 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 11 | 5.8 | 3.64 | 10.19 | 16.57 | 2.00 | 84.0 | 68.0 |
| Bench 3 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 1.89 | 5.34 | 12.49 | 1.00 | 47.1 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 4.65 | 15.68 | 26.28 | 14.00 | 86.3 | 90.0 |
| XI | XI | Enzo Fernández | MID | 7 | 6.5 | 4.34 | 14.84 | 23.05 | 1.00 | 86.8 | 90.0 |
| XI | XI | Cole Palmer | MID | 7 | 10.3 | 4.64 | 14.07 | 24.17 | 8.00 | 80.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.77 | 12.43 | 18.10 | 2.00 | 83.0 | 64.0 |
| Captain | Captain | Antoine Semenyo | MID | 13 | 8.0 | 5.29 | 12.18 | 19.76 | 6.00 | 69.8 | 57.0 |