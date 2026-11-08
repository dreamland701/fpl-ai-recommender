# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 267.34
- Total actual points: 247.00
- Average predicted points: 66.84
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
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.17 | 12.53 | 19.86 | 6.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 3.02 | 9.02 | 14.71 | 2.00 | 83.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.47 | 16.21 | 24.70 | 6.00 | 95.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.99 | 15.39 | 24.35 | 1.00 | 93.4 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 4.12 | 12.09 | 19.70 | -1.00 | 80.8 | 90.0 |
| Bench 2 | Bench | Nico O'Reilly | DEF | 13 | 5.1 | 4.01 | 11.92 | 19.14 | 1.00 | 60.9 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.86 | 11.60 | 18.76 | 1.00 | 83.0 | 45.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 5.01 | 15.10 | 23.72 | 2.00 | 86.0 | 87.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 5.06 | 14.78 | 23.97 | 6.00 | 82.6 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.7 | 3.55 | 10.79 | 18.84 | 8.00 | 47.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.60 | 20.21 | 33.06 | 5.00 | 100.7 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.06 | 15.30 | 24.47 | 4.00 | 85.0 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 5.03 | 14.36 | 22.16 | 4.00 | 99.9 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.65 | 13.87 | 22.85 | 2.00 | 66.2 | 74.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 4.58 | 13.69 | 21.82 | 1.00 | 78.7 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 78.73
- Actual score: 64.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.73) beats the best remaining Bench Boost opportunity (14.70).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Morgan Rogers -> Rayan Cherki (projected gain 1.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.73) beats the best remaining Bench Boost opportunity (14.70).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.18 | 12.03 | 19.98 | 9.00 | 89.2 | 90.0 |
| Bench 1 | Bench Boost | Mads Hermansen | GK | 19 | 4.2 | 2.64 | 7.93 | 13.33 | 2.00 | 83.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.70 | 16.05 | 25.67 | 11.00 | 99.2 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.76 | 13.76 | 20.85 | 5.00 | 104.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.75 | 13.35 | 22.10 | 2.00 | 91.7 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.47 | 10.11 | 17.07 | 4.00 | 80.9 | 90.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | 16 | 4.8 | 3.32 | 9.71 | 16.29 | 2.00 | 69.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.61 | 14.40 | 23.83 | 2.00 | 86.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.50 | 13.15 | 22.28 | 2.00 | 84.9 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.08 | 11.92 | 21.14 | 2.00 | 72.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.96 | 20.72 | 34.18 | 3.00 | 103.9 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 6.36 | 15.43 | 24.80 | 12.00 | 106.0 | 180.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 6.16 | 14.57 | 22.70 | 5.00 | 100.9 | 70.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.60 | 13.76 | 23.35 | 0.00 | 68.2 | 0.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.66 | 13.49 | 21.13 | 0.00 | 93.9 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 1.20 -> 1.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.35
- Actual score: 56.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 4.96, hit 0)
- Autosub outfielders: Neco Williams.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.57 | 12.55 | 20.35 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 2.68 | 8.10 | 13.42 | 5.00 | 81.3 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.04 | 16.42 | 26.41 | 6.00 | 97.4 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.30 | 15.61 | 25.74 | 2.00 | 119.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.98 | 12.26 | 20.37 | 14.00 | 86.5 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.71 | 10.85 | 17.79 | 3.00 | 83.9 | 90.0 |
| Bench 2 | Autosub In | Neco Williams | DEF | 16 | 4.8 | 3.57 | 10.68 | 17.25 | 1.00 | 84.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.45 | 13.44 | 22.64 | 2.00 | 81.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.10 | 12.55 | 21.27 | 2.00 | 79.1 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 4.30 | 12.38 | 20.39 | 0.00 | 73.3 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.85 | 20.22 | 32.88 | 9.00 | 103.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.87 | 17.37 | 28.06 | 1.00 | 109.3 | 55.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 4.33 | 13.70 | 22.43 | 1.00 | 66.2 | 34.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 2.70 | 9.69 | 17.08 | 7.00 | 40.5 | 90.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.95 | 8.86 | 15.26 | 1.00 | 48.0 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 66.93
- Actual score: 86.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.86) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Konstantinos Mavropanos -> Marcos Senesi Barón (projected gain 1.79, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.86) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mads Hermansen replaced David Raya Martín.
- Autosub outfielders: Neco Williams.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.24 | 12.57 | 20.45 | 0.00 | 87.9 | 0.0 |
| Bench 1 | Autosub In | Mads Hermansen | GK | 19 | 4.2 | 2.93 | 8.30 | 13.56 | 7.00 | 83.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 5.39 | 15.36 | 24.95 | 1.00 | 93.3 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.15 | 14.83 | 23.94 | 2.00 | 99.9 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.99 | 14.34 | 23.14 | 0.00 | 104.4 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.47 | 13.12 | 21.55 | 2.00 | 93.3 | 90.0 |
| Bench 2 | Autosub In | Neco Williams | DEF | 16 | 4.8 | 3.60 | 10.48 | 16.91 | 2.00 | 87.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.69 | 13.83 | 22.61 | 2.00 | 89.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.20 | 11.76 | 19.71 | 12.00 | 79.9 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.5 | 3.02 | 8.93 | 14.97 | 1.00 | 45.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.86 | 20.52 | 33.87 | 14.00 | 104.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.09 | 14.75 | 24.00 | 6.00 | 83.2 | 57.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.6 | 4.14 | 12.62 | 20.78 | 1.00 | 63.5 | 32.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 3.99 | 12.42 | 21.06 | 9.00 | 70.9 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.9 | 2.82 | 8.26 | 14.83 | 0.00 | 58.3 | 0.0 |