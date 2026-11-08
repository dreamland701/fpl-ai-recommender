# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 267.53
- Total actual points: 247.00
- Average predicted points: 66.88
- Average actual points: 61.75
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
- Bank: 100.00 -> 0.20
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 61.33
- Actual score: 41.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.17 | 12.59 | 20.06 | 6.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 3.04 | 9.05 | 14.79 | 2.00 | 82.9 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.47 | 16.37 | 25.19 | 6.00 | 95.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.98 | 15.45 | 24.61 | 1.00 | 93.5 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.15 | 12.14 | 20.01 | -1.00 | 80.7 | 90.0 |
| Bench 2 | Bench | Nico O'Reilly | DEF | 13 | 5.1 | 4.01 | 12.05 | 19.36 | 1.00 | 60.9 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.87 | 11.69 | 18.92 | 1.00 | 83.0 | 45.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 5.04 | 15.27 | 24.14 | 2.00 | 85.9 | 87.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 5.04 | 14.87 | 24.45 | 6.00 | 82.7 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.53 | 10.76 | 18.90 | 8.00 | 47.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.59 | 20.35 | 33.62 | 5.00 | 100.7 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.07 | 15.44 | 24.80 | 4.00 | 85.0 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 5.03 | 14.62 | 22.48 | 4.00 | 100.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.65 | 13.93 | 22.98 | 2.00 | 66.1 | 74.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.55 | 13.81 | 22.18 | 1.00 | 78.7 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.20 -> 1.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 78.70
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.76) beats the best remaining Bench Boost opportunity (14.76).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Morgan Rogers -> Rayan Cherki (projected gain 1.43, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.76) beats the best remaining Bench Boost opportunity (14.76).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.16 | 11.89 | 19.85 | 9.00 | 89.3 | 90.0 |
| Bench 1 | Bench Boost | Mads Hermansen | GK | 19 | 4.2 | 2.66 | 7.94 | 13.39 | 2.00 | 83.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.67 | 16.10 | 25.82 | 11.00 | 99.2 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.1 | 5.78 | 13.87 | 21.15 | 5.00 | 104.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.76 | 13.23 | 22.04 | 2.00 | 91.6 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.50 | 10.07 | 17.02 | 4.00 | 80.8 | 90.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | 16 | 4.8 | 3.31 | 9.72 | 16.28 | 2.00 | 69.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.60 | 14.37 | 23.93 | 2.00 | 86.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.53 | 13.12 | 22.35 | 2.00 | 84.8 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.08 | 11.70 | 20.92 | 2.00 | 72.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.94 | 20.74 | 34.31 | 3.00 | 103.9 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.37 | 15.33 | 24.87 | 12.00 | 106.0 | 180.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 6.17 | 14.62 | 22.90 | 5.00 | 100.9 | 70.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 4.59 | 13.76 | 23.42 | 0.00 | 68.2 | 0.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 4.64 | 13.67 | 21.26 | 0.00 | 94.0 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 1.10 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.41
- Actual score: 56.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 4.86, hit 0)
- Autosub: Neco Williams replaced João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.60 | 12.58 | 20.40 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 2.66 | 8.11 | 13.52 | 5.00 | 81.3 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 6.07 | 16.47 | 26.56 | 6.00 | 97.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.32 | 15.57 | 25.74 | 2.00 | 119.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.01 | 12.26 | 20.51 | 14.00 | 86.5 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.70 | 10.88 | 17.92 | 3.00 | 84.0 | 90.0 |
| Bench 2 | Autosub In | Neco Williams | DEF | 16 | 4.8 | 3.55 | 10.74 | 17.47 | 1.00 | 84.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.46 | 13.41 | 22.76 | 2.00 | 81.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.09 | 12.50 | 21.37 | 2.00 | 79.1 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.27 | 12.37 | 20.45 | 0.00 | 73.3 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.83 | 20.25 | 33.13 | 9.00 | 103.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.89 | 17.39 | 28.25 | 1.00 | 109.3 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.35 | 13.67 | 22.46 | 1.00 | 66.1 | 34.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.69 | 9.72 | 17.24 | 7.00 | 40.5 | 90.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.7 | 2.93 | 8.82 | 15.28 | 1.00 | 48.0 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.20 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 67.09
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Konstantinos Mavropanos -> Marcos Senesi Barón (projected gain 1.82, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.87) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mads Hermansen replaced David Raya Martín.
- Autosub: Neco Williams replaced Marc Guéhi.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.0 | 4.25 | 12.61 | 20.46 | 0.00 | 87.9 | 0.0 |
| Bench 1 | Autosub In | Mads Hermansen | GK | 19 | 4.2 | 2.93 | 8.33 | 13.63 | 7.00 | 83.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.40 | 15.47 | 25.14 | 1.00 | 93.3 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.17 | 14.93 | 24.15 | 2.00 | 99.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 5.02 | 14.44 | 23.36 | 0.00 | 104.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.45 | 13.23 | 21.72 | 2.00 | 93.4 | 90.0 |
| Bench 2 | Autosub In | Neco Williams | DEF | 16 | 4.8 | 3.62 | 10.51 | 17.15 | 2.00 | 87.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.68 | 13.88 | 22.78 | 2.00 | 89.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.20 | 11.79 | 19.83 | 12.00 | 79.9 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.00 | 8.92 | 14.93 | 1.00 | 45.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.87 | 20.53 | 34.01 | 14.00 | 104.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.12 | 14.80 | 24.12 | 6.00 | 83.2 | 57.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.17 | 12.63 | 20.78 | 1.00 | 63.4 | 32.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 4.01 | 12.44 | 21.19 | 9.00 | 70.8 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.83 | 8.30 | 14.88 | 0.00 | 58.2 | 0.0 |