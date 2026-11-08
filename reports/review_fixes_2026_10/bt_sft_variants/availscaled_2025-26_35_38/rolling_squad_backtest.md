# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 265.52
- Total actual points: 262.00
- Average predicted points: 66.38
- Average actual points: 65.50
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
- Bank: 100.00 -> 0.00
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Morgan Gibbs-White
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.91
- Actual score: 47.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.45 | 10.53 | 17.50 | 6.00 | 84.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.15 | 8.67 | 14.18 | 8.00 | 85.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 14.42 | 22.64 | 6.00 | 91.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.67 | 12.99 | 20.25 | 1.00 | 70.7 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 3.59 | 11.88 | 20.26 | 1.00 | 78.8 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.8 | 3.74 | 10.90 | 17.56 | 1.00 | 76.5 | 45.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.17 | 10.13 | 17.86 | -1.00 | 72.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.82 | 14.12 | 23.77 | 6.00 | 85.0 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | FWD | 19 | 7.8 | 3.93 | 13.14 | 22.36 | 2.00 | 73.9 | 87.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 4.03 | 11.71 | 19.02 | 5.00 | 70.3 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.31 | 19.14 | 32.23 | 5.00 | 98.0 | 90.0 |
| Vice Captain | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.12 | 15.19 | 24.74 | 4.00 | 77.9 | 20.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.05 | 13.71 | 23.71 | 2.00 | 59.5 | 74.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 5.05 | 13.41 | 21.38 | 5.00 | 72.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.43 | 13.05 | 21.44 | 1.00 | 79.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Rayan Cherki
- Vice captain: Antoine Semenyo
- Effective captain: Rayan Cherki
- Chip used: bench_boost
- Predicted score: 81.67
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.30) beats the best remaining Bench Boost opportunity (14.59).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Virgil van Dijk -> Maxence Lacroix (projected gain 1.63, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.30) beats the best remaining Bench Boost opportunity (14.59).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.87 | 11.17 | 18.22 | 9.00 | 86.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.52 | 8.33 | 13.95 | 3.00 | 81.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 6.90 | 16.31 | 24.42 | 5.00 | 119.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.20 | 14.89 | 23.50 | 11.00 | 93.1 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 6.12 | 14.55 | 21.93 | 4.00 | 94.5 | 180.0 |
| Bench 3 | Bench Boost | Neco Williams | DEF | 16 | 4.8 | 3.32 | 9.70 | 16.21 | 2.00 | 70.1 | 90.0 |
| Bench 4 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.08 | 9.49 | 15.88 | 4.00 | 79.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.95 | 13.20 | 22.44 | 2.00 | 78.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.91 | 12.94 | 22.02 | 2.00 | 78.3 | 90.0 |
| Bench 2 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.72 | 11.03 | 18.49 | 1.00 | 66.0 | 82.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.08 | 20.83 | 34.00 | 3.00 | 103.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 7.49 | 18.70 | 29.35 | 12.00 | 76.9 | 180.0 |
| Captain | Captain | Rayan Cherki | MID | 13 | 6.5 | 7.88 | 18.37 | 28.11 | 5.00 | 93.9 | 70.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.13 | 14.50 | 25.46 | 0.00 | 26.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.63 | 13.41 | 21.82 | 2.00 | 80.2 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.90 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.64
- Actual score: 54.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 3.82, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.79 | 12.54 | 19.97 | 6.00 | 87.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.32 | 9.56 | 15.67 | 2.00 | 87.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.17 | 15.96 | 25.28 | 6.00 | 92.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.62 | 13.73 | 22.75 | 2.00 | 103.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 4.36 | 12.45 | 19.06 | 2.00 | 97.0 | 60.0 |
| Bench 2 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.35 | 9.92 | 16.44 | 3.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.17 | 9.79 | 15.96 | 1.00 | 81.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.83 | 13.71 | 22.72 | 2.00 | 85.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.30 | 12.81 | 21.82 | 2.00 | 83.8 | 90.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.41 | 10.70 | 17.81 | 2.00 | 71.1 | 83.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.21 | 32.88 | 9.00 | 98.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.48 | 16.11 | 26.02 | 1.00 | 94.5 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.09 | 14.25 | 23.78 | 1.00 | 63.0 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.82 | 11.67 | 19.98 | 12.00 | 75.1 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.55 | 11.04 | 20.37 | 7.00 | 28.1 | 90.0 |

## GW38

- Train rows: 190183
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.30
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.82) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Maxence Lacroix -> Virgil van Dijk (projected gain 3.64, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.82) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Konstantinos Mavropanos replaced Marc Guéhi.
- Autosub: Igor Jesus Maciel da Cruz replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.40 | 12.36 | 19.61 | 0.00 | 86.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.77 | 8.75 | 14.50 | 6.00 | 85.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.25 | 14.90 | 23.95 | 1.00 | 87.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.10 | 14.30 | 22.82 | 2.00 | 96.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 13.01 | 20.76 | 0.00 | 94.5 | 0.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.86 | 10.71 | 17.12 | 8.00 | 85.5 | 90.0 |
| Bench 4 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.30 | 9.54 | 15.58 | 2.00 | 83.6 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.43 | 14.22 | 23.04 | 12.00 | 96.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.10 | 12.70 | 20.98 | 2.00 | 81.8 | 90.0 |
| Bench 3 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.52 | 10.12 | 16.84 | 2.00 | 55.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.82 | 20.26 | 33.40 | 14.00 | 96.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 5.23 | 14.71 | 23.77 | 6.00 | 84.5 | 57.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.52 | 13.32 | 22.48 | 9.00 | 80.7 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.30 | 13.29 | 21.99 | 1.00 | 62.7 | 32.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.3 | 3.88 | 12.70 | 20.89 | 0.00 | 83.9 | 0.0 |