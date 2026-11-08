# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 231.35
- Total actual points: 262.00
- Average predicted points: 57.84
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
- Predicted score: 48.92
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.97 | 9.05 | 15.04 | 6.00 | 80.0 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.71 | 7.45 | 12.19 | 8.00 | 82.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.25 | 12.40 | 19.46 | 6.00 | 92.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.01 | 11.16 | 17.41 | 1.00 | 59.7 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 3.09 | 10.21 | 17.42 | 1.00 | 72.8 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.8 | 3.22 | 9.37 | 15.10 | 1.00 | 69.5 | 45.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.73 | 8.71 | 15.36 | -1.00 | 62.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.14 | 12.14 | 20.43 | 6.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | FWD | 19 | 7.8 | 3.38 | 11.29 | 19.23 | 2.00 | 64.9 | 87.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.46 | 10.06 | 16.35 | 5.00 | 59.3 | 45.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.42 | 16.45 | 27.71 | 5.00 | 102.0 | 90.0 |
| Vice Captain | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.40 | 13.06 | 21.26 | 4.00 | 70.9 | 20.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 3.48 | 11.79 | 20.38 | 2.00 | 42.5 | 74.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.34 | 11.53 | 18.38 | 5.00 | 62.3 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.81 | 11.22 | 18.43 | 1.00 | 73.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.90
- Free transfers: 2 -> 2
- Captain: Rayan Cherki
- Vice captain: Antoine Semenyo
- Effective captain: Rayan Cherki
- Chip used: bench_boost
- Predicted score: 70.52
- Actual score: 70.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.58) beats the best remaining Bench Boost opportunity (12.59).
- Transfer: Virgil van Dijk -> Maxence Lacroix (projected gain 1.37, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.58) beats the best remaining Bench Boost opportunity (12.59).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.34 | 9.65 | 15.73 | 9.00 | 84.8 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.17 | 7.19 | 12.05 | 3.00 | 77.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.96 | 14.08 | 21.09 | 5.00 | 99.6 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.49 | 12.85 | 20.29 | 11.00 | 94.1 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 5.28 | 12.56 | 18.93 | 4.00 | 104.5 | 180.0 |
| Bench 3 | Bench Boost | Neco Williams | DEF | 16 | 4.8 | 2.86 | 8.38 | 14.00 | 2.00 | 60.1 | 90.0 |
| Bench 4 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.66 | 8.19 | 13.71 | 4.00 | 73.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.41 | 11.40 | 19.38 | 2.00 | 72.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.37 | 11.18 | 19.01 | 2.00 | 72.3 | 90.0 |
| Bench 2 | Bench Boost | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.21 | 9.52 | 15.96 | 1.00 | 53.0 | 82.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.11 | 17.98 | 29.36 | 3.00 | 104.3 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 6.47 | 16.15 | 25.34 | 12.00 | 96.9 | 180.0 |
| Captain | Captain | Rayan Cherki | MID | 13 | 6.5 | 6.81 | 15.86 | 24.28 | 5.00 | 103.9 | 70.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 3.56 | 12.52 | 21.99 | 0.00 | 41.8 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.99 | 11.58 | 18.84 | 2.00 | 74.2 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.90 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 52.30
- Actual score: 54.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 3.35, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.20 | 10.99 | 17.51 | 6.00 | 86.2 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.91 | 8.38 | 13.74 | 2.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.41 | 13.99 | 22.17 | 6.00 | 93.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.05 | 12.04 | 19.95 | 2.00 | 111.5 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.2 | 3.83 | 10.92 | 16.72 | 2.00 | 101.0 | 60.0 |
| Bench 2 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.93 | 8.70 | 14.42 | 3.00 | 75.7 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.8 | 2.78 | 8.58 | 13.99 | 1.00 | 76.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.24 | 12.02 | 19.92 | 2.00 | 83.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.77 | 11.23 | 19.13 | 2.00 | 79.8 | 90.0 |
| XI | XI | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 2.99 | 9.39 | 15.62 | 2.00 | 61.1 | 83.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.04 | 17.72 | 28.83 | 9.00 | 108.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.81 | 14.13 | 22.82 | 1.00 | 104.5 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.59 | 12.50 | 20.85 | 1.00 | 49.0 | 34.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.35 | 10.23 | 17.52 | 12.00 | 67.1 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.23 | 9.68 | 17.86 | 7.00 | 29.1 | 90.0 |

## GW38

- Train rows: 190183
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 59.61
- Actual score: 91.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Maxence Lacroix -> Virgil van Dijk (projected gain 3.23, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.04) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub: Konstantinos Mavropanos replaced Marc Guéhi.
- Autosub: Igor Jesus Maciel da Cruz replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.89 | 10.95 | 17.37 | 0.00 | 84.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.46 | 7.75 | 12.84 | 6.00 | 82.5 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.65 | 13.19 | 21.22 | 1.00 | 86.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.52 | 12.67 | 20.22 | 2.00 | 99.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.12 | 11.52 | 18.39 | 0.00 | 97.5 | 0.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.41 | 9.48 | 15.16 | 8.00 | 83.5 | 90.0 |
| Bench 4 | Bench | Neco Williams | DEF | 16 | 4.8 | 2.93 | 8.45 | 13.80 | 2.00 | 79.6 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.81 | 12.59 | 20.40 | 12.00 | 99.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.63 | 11.25 | 18.58 | 2.00 | 77.8 | 90.0 |
| Bench 3 | Autosub In | Igor Jesus Maciel da Cruz | FWD | 16 | 5.9 | 3.12 | 8.97 | 14.92 | 2.00 | 65.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.04 | 17.95 | 29.58 | 14.00 | 106.7 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.0 | 4.63 | 13.03 | 21.05 | 6.00 | 81.5 | 57.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.00 | 11.80 | 19.91 | 9.00 | 75.7 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 3.81 | 11.77 | 19.48 | 1.00 | 48.7 | 32.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.3 | 3.43 | 11.25 | 18.51 | 0.00 | 80.9 | 0.0 |