# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 263.72
- Total actual points: 268.00
- Average predicted points: 65.93
- Average actual points: 67.00
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
- Predicted score: 59.26
- Actual score: 46.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | -1 | 6.0 | 3.96 | 11.78 | 18.78 | 6.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | -1 | 4.2 | 3.00 | 8.59 | 13.64 | 2.00 | 79.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.2 | 4.85 | 15.13 | 24.54 | 1.00 | 90.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | -1 | 7.1 | 5.06 | 15.06 | 23.98 | 6.00 | 89.6 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | -1 | 5.1 | 3.95 | 11.89 | 18.56 | 4.00 | 82.7 | 90.0 |
| Bench 2 | Bench | Konstantinos Mavropanos | DEF | -1 | 4.5 | 3.89 | 11.33 | 18.89 | -1.00 | 76.2 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | -1 | 4.8 | 3.83 | 11.14 | 17.75 | 1.00 | 80.4 | 45.0 |
| XI | XI | Jarrod Bowen | FWD | -1 | 7.7 | 4.88 | 14.81 | 23.88 | 2.00 | 83.0 | 87.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | -1 | 7.4 | 4.83 | 14.10 | 23.24 | 6.00 | 80.0 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 7.7 | 3.62 | 10.66 | 17.97 | 8.00 | 44.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | -1 | 10.3 | 6.52 | 19.51 | 31.49 | 5.00 | 96.1 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | -1 | 7.5 | 4.90 | 14.61 | 23.57 | 4.00 | 81.4 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | -1 | 5.7 | 4.73 | 13.66 | 21.49 | 4.00 | 97.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | -1 | 8.2 | 4.56 | 13.40 | 21.58 | 2.00 | 65.5 | 74.0 |
| XI | XI | Morgan Rogers | MID | -1 | 7.4 | 4.49 | 13.39 | 21.60 | 1.00 | 77.2 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.20 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 76.90
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.40) beats the best remaining Bench Boost opportunity (15.23).
- Transfer: Pedro Porro Sauceda -> Marc Guéhi (projected gain 2.39, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.40) beats the best remaining Bench Boost opportunity (15.23).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | -1 | 6.0 | 4.15 | 11.65 | 18.52 | 9.00 | 87.8 | 90.0 |
| Bench 1 | Bench Boost | Mads Hermansen | GK | -1 | 4.2 | 2.66 | 7.61 | 12.17 | 2.00 | 79.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 7.2 | 5.54 | 15.47 | 24.26 | 11.00 | 95.3 | 90.0 |
| XI | XI | Marc Guéhi | DEF | -1 | 5.1 | 5.98 | 14.52 | 21.79 | 15.00 | 120.8 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.2 | 4.72 | 13.08 | 21.39 | 2.00 | 91.2 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | -1 | 4.5 | 3.39 | 9.73 | 15.99 | 4.00 | 76.8 | 90.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | -1 | 4.8 | 3.30 | 9.42 | 15.26 | 2.00 | 66.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | -1 | 7.4 | 4.48 | 13.93 | 22.83 | 2.00 | 84.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | -1 | 7.8 | 4.49 | 12.81 | 21.11 | 2.00 | 82.5 | 90.0 |
| Bench 2 | Bench Boost | João Pedro Junqueira de Jesus | FWD | -1 | 7.5 | 4.28 | 12.05 | 20.12 | 2.00 | 73.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | -1 | 10.4 | 6.92 | 19.94 | 31.73 | 3.00 | 100.8 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | -1 | 8.2 | 6.50 | 15.63 | 23.84 | 12.00 | 109.0 | 180.0 |
| XI | XI | Morgan Gibbs-White | MID | -1 | 7.6 | 4.63 | 13.38 | 21.88 | 0.00 | 64.6 | 0.0 |
| XI | XI | Carlos Henrique Casimiro | MID | -1 | 5.8 | 4.48 | 13.28 | 20.66 | 0.00 | 93.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | -1 | 7.5 | 4.46 | 12.79 | 20.58 | 2.00 | 80.0 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.30 -> 1.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.58
- Actual score: 67.00
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 2.67, hit 0)
- Autosub outfielders: Konstantinos Mavropanos.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | -1 | 6.1 | 4.54 | 12.07 | 18.71 | 6.00 | 88.5 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | -1 | 4.2 | 2.71 | 7.85 | 12.57 | 5.00 | 78.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | -1 | 7.2 | 5.95 | 16.03 | 24.89 | 6.00 | 95.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | -1 | 5.1 | 5.46 | 15.73 | 24.41 | 2.00 | 120.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.1 | 3.98 | 12.28 | 20.10 | 14.00 | 86.1 | 90.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | -1 | 4.5 | 3.70 | 10.79 | 17.02 | 3.00 | 80.7 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | -1 | 4.8 | 3.49 | 10.33 | 16.48 | 1.00 | 81.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | -1 | 7.3 | 4.44 | 13.20 | 21.74 | 2.00 | 81.8 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | -1 | 7.7 | 4.04 | 12.15 | 20.29 | 2.00 | 76.9 | 90.0 |
| XI | Bench | João Pedro Junqueira de Jesus | FWD | -1 | 7.5 | 4.26 | 12.09 | 19.49 | 0.00 | 72.0 | 0.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | -1 | 10.4 | 6.84 | 19.69 | 30.95 | 9.00 | 100.4 | 90.0 |
| XI | XI | Antoine Semenyo | MID | -1 | 8.1 | 5.90 | 17.10 | 26.80 | 1.00 | 111.8 | 55.0 |
| XI | XI | Rayan Cherki | MID | -1 | 6.6 | 4.29 | 13.39 | 21.47 | 1.00 | 68.9 | 34.0 |
| XI | XI | Morgan Rogers | MID | -1 | 7.5 | 4.03 | 11.59 | 18.94 | 12.00 | 75.2 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | -1 | 5.8 | 2.71 | 8.58 | 14.71 | 1.00 | 47.1 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 66.98
- Actual score: 84.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.85) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Neco Williams -> Marcos Senesi Barón (projected gain 2.38, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.85) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mads Hermansen replaced David Raya Martín.
- Autosub outfielders: Konstantinos Mavropanos, João Pedro Junqueira de Jesus.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | -1 | 6.1 | 4.21 | 11.95 | 18.44 | 0.00 | 85.2 | 0.0 |
| Bench 1 | Autosub In | Mads Hermansen | GK | -1 | 4.2 | 2.98 | 8.02 | 12.55 | 7.00 | 79.9 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | -1 | 7.3 | 5.29 | 14.78 | 22.82 | 1.00 | 91.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.1 | 5.25 | 14.69 | 23.03 | 2.00 | 96.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | -1 | 5.1 | 4.97 | 13.90 | 21.43 | 0.00 | 102.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | -1 | 5.2 | 4.54 | 13.18 | 20.80 | 2.00 | 91.2 | 90.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | -1 | 4.5 | 3.92 | 10.85 | 17.11 | 8.00 | 83.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | -1 | 7.3 | 4.68 | 13.58 | 21.60 | 2.00 | 86.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | -1 | 7.7 | 4.16 | 11.34 | 18.37 | 12.00 | 77.0 | 90.0 |
| Bench 3 | Autosub In | João Pedro Junqueira de Jesus | FWD | -1 | 7.5 | 2.93 | 8.79 | 14.39 | 1.00 | 44.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | -1 | 10.4 | 6.85 | 19.74 | 31.07 | 14.00 | 101.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | -1 | 8.1 | 5.07 | 14.21 | 22.10 | 6.00 | 83.5 | 57.0 |
| XI | Bench | Morgan Rogers | MID | -1 | 7.4 | 4.19 | 12.90 | 20.64 | 0.00 | 86.7 | 0.0 |
| XI | XI | Rayan Cherki | MID | -1 | 6.6 | 4.08 | 11.95 | 18.74 | 1.00 | 63.2 | 32.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | -1 | 5.9 | 2.59 | 7.67 | 13.43 | 0.00 | 57.8 | 0.0 |