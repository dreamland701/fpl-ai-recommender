# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 213.62
- Total actual points: 264.00
- Average predicted points: 53.41
- Average actual points: 66.00
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW34 are included before the first simulated week.
- League-average scores were pulled from official FPL event metadata when available.

## GW35

- Train rows: 187673
- Bank: 100.00 -> 2.40
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 47.33
- Actual score: 38.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- League average score: 0.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.43 | 10.53 | 16.67 | 6.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 2.69 | 8.01 | 13.12 | 2.00 | 83.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 3.95 | 12.11 | 18.50 | 6.00 | 93.5 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.58 | 11.33 | 18.22 | 1.00 | 91.0 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.37 | 10.52 | 16.30 | -1.00 | 82.1 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.23 | 10.41 | 16.62 | 4.00 | 78.8 | 90.0 |
| Bench 4 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.22 | 10.09 | 16.18 | 1.00 | 83.7 | 45.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.87 | 12.43 | 19.70 | 2.00 | 87.0 | 87.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.01 | 12.05 | 19.68 | 6.00 | 86.1 | 90.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | 2 | 8.7 | 3.38 | 11.04 | 16.42 | 1.00 | 64.6 | 30.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 5.00 | 16.18 | 26.97 | 5.00 | 95.9 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.70 | 12.45 | 18.82 | 1.00 | 83.3 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 4.01 | 11.97 | 18.94 | 4.00 | 85.3 | 20.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.88 | 11.78 | 18.84 | 1.00 | 86.3 | 45.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.1 | 3.53 | 11.19 | 17.29 | 2.00 | 92.0 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 2.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Marc Guéhi
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 61.88
- Actual score: 73.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.06) beats the best remaining Bench Boost opportunity (12.13).
- League average score: 0.00
- Transfer: Elliot Anderson -> Dominik Szoboszlai (projected gain 3.52, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.06) beats the best remaining Bench Boost opportunity (12.13).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.45 | 10.02 | 16.69 | 9.00 | 89.6 | 90.0 |
| Bench 1 | Bench Boost | Mads Hermansen | GK | 19 | 4.2 | 2.14 | 6.68 | 11.11 | 2.00 | 83.9 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.03 | 12.79 | 19.97 | 15.00 | 141.7 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.42 | 12.13 | 19.79 | 11.00 | 95.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.58 | 9.72 | 16.71 | 2.00 | 90.6 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.97 | 8.68 | 14.71 | 4.00 | 82.3 | 90.0 |
| Bench 4 | Bench Boost | Neco Williams | DEF | 16 | 4.8 | 2.59 | 7.47 | 12.31 | 2.00 | 56.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.08 | 12.27 | 21.04 | 2.00 | 85.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 3.74 | 12.27 | 20.14 | 2.00 | 87.8 | 90.0 |
| Bench 2 | Bench Boost | Ollie Watkins | FWD | 2 | 8.8 | 3.04 | 8.76 | 15.31 | 9.00 | 68.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.97 | 17.33 | 28.47 | 3.00 | 98.4 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.15 | 12.28 | 20.26 | 2.00 | 87.5 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.03 | 12.11 | 20.04 | 2.00 | 84.3 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 3.37 | 9.87 | 17.49 | 0.00 | 44.9 | 0.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.34 | 9.81 | 16.01 | 5.00 | 88.3 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.90 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 50.57
- Actual score: 63.00
- League average score: 0.00
- Transfer: Morgan Gibbs-White -> Antoine Semenyo (projected gain 4.97, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 3.69 | 9.86 | 15.64 | 6.00 | 89.0 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 2.47 | 7.51 | 12.42 | 5.00 | 82.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.90 | 12.62 | 20.24 | 6.00 | 94.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.11 | 12.10 | 19.90 | 2.00 | 118.0 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.06 | 8.89 | 14.60 | 3.00 | 83.7 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.1 | 2.96 | 8.80 | 14.78 | 14.00 | 87.5 | 90.0 |
| Bench 4 | Bench | Neco Williams | DEF | 16 | 4.8 | 2.70 | 7.34 | 11.61 | 1.00 | 85.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.01 | 12.29 | 20.79 | 2.00 | 85.4 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.45 | 9.98 | 16.78 | 2.00 | 82.0 | 90.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | 2 | 8.8 | 2.99 | 9.33 | 15.67 | 15.00 | 76.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.93 | 16.83 | 27.41 | 9.00 | 98.1 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.92 | 14.25 | 22.68 | 1.00 | 100.5 | 55.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.42 | 9.96 | 16.67 | 9.00 | 84.2 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.80 | 9.94 | 16.35 | 2.00 | 84.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.36 | 9.47 | 15.73 | 12.00 | 81.2 | 90.0 |

## GW38

- Train rows: 190183
- Bank: 0.40 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 53.84
- Actual score: 90.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.53) beats the best remaining Triple Captain opportunity (0.00).
- League average score: 0.00
- Transfer: Konstantinos Mavropanos -> Jaka Bijol (projected gain 1.63, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.53) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mads Hermansen replaced David Raya Martín.
- Autosub outfielders: Kiernan Dewsbury-Hall, Jaka Bijol.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.83 | 11.04 | 18.00 | 0.00 | 88.0 | 0.0 |
| Bench 1 | Autosub In | Mads Hermansen | GK | 19 | 4.2 | 2.66 | 7.30 | 11.89 | 7.00 | 84.8 | 90.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.18 | 11.77 | 18.73 | 2.00 | 95.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 4.15 | 11.56 | 18.78 | 1.00 | 92.4 | 45.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.62 | 10.36 | 17.15 | 0.00 | 93.1 | 0.0 |
| Bench 3 | Autosub In | Jaka Bijol | DEF | 11 | 3.9 | 3.11 | 9.04 | 13.64 | 1.00 | 90.1 | 69.0 |
| Bench 4 | Bench | Neco Williams | DEF | 16 | 4.8 | 2.74 | 7.67 | 12.21 | 2.00 | 86.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.80 | 10.63 | 17.20 | 2.00 | 87.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 3.18 | 10.49 | 17.94 | 13.00 | 81.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.41 | 9.79 | 16.34 | 12.00 | 83.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.53 | 16.73 | 28.18 | 14.00 | 99.1 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.06 | 11.86 | 18.66 | 6.00 | 83.9 | 57.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.4 | 3.49 | 10.91 | 17.77 | 0.00 | 89.4 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.51 | 9.73 | 16.91 | 2.00 | 68.4 | 90.0 |
| Bench 2 | Autosub In | Kiernan Dewsbury-Hall | MID | 9 | 5.3 | 3.16 | 8.46 | 13.48 | 2.00 | 83.7 | 83.0 |