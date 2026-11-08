# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW35-GW38
- Total predicted points: 211.33
- Total actual points: 339.00
- Average predicted points: 52.83
- Average actual points: 84.75
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW26 are included before the first simulated week.
- League-average scores were not available for this run.

## GW35

- Train rows: 187673
- Bank: 100.00 -> 0.70
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Jarrod Bowen
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 47.54
- Actual score: 46.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.25 | 10.15 | 15.82 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 2.47 | 7.23 | 11.41 | 2.00 | 83.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.66 | 13.25 | 19.84 | 1.00 | 88.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.03 | 13.20 | 20.24 | 6.00 | 90.1 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.1 | 3.16 | 9.87 | 15.39 | 4.00 | 83.6 | 90.0 |
| Bench 3 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.10 | 9.77 | 15.92 | -1.00 | 81.6 | 90.0 |
| Bench 4 | Bench | Marc Guéhi | DEF | 13 | 5.1 | 2.99 | 9.77 | 15.67 | 4.00 | 74.3 | 90.0 |
| Vice Captain | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.48 | 13.45 | 21.01 | 2.00 | 87.2 | 87.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.02 | 12.77 | 20.57 | 6.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | 2 | 8.7 | 3.50 | 11.39 | 17.12 | 1.00 | 73.5 | 30.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 4.81 | 15.71 | 26.44 | 5.00 | 98.1 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 4.11 | 13.37 | 21.86 | 4.00 | 85.5 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 4.08 | 12.44 | 17.41 | 4.00 | 97.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 3.56 | 11.49 | 18.96 | 2.00 | 61.9 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.59 | 11.46 | 18.10 | 1.00 | 85.3 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.70 -> 0.80
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 62.16
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.92) beats the best remaining Bench Boost opportunity (11.95).
- Transfer: Morgan Gibbs-White -> Morgan Rogers (projected gain 1.73, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.92) beats the best remaining Bench Boost opportunity (11.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 2.90 | 8.90 | 14.80 | 9.00 | 87.9 | 90.0 |
| Bench 1 | Bench Boost | Mads Hermansen | GK | 19 | 4.2 | 2.26 | 5.97 | 10.09 | 2.00 | 84.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.24 | 12.80 | 20.66 | 11.00 | 94.7 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.44 | 10.99 | 17.68 | 15.00 | 139.4 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.74 | 10.65 | 17.70 | 2.00 | 89.5 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.49 | 9.72 | 15.96 | 1.00 | 88.7 | 90.0 |
| Bench 4 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.47 | 7.77 | 13.20 | 4.00 | 82.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 3.92 | 12.96 | 21.80 | 2.00 | 85.8 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.56 | 11.36 | 19.41 | 2.00 | 87.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.70 | 10.30 | 17.69 | 9.00 | 69.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.91 | 17.88 | 29.32 | 3.00 | 102.2 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.84 | 11.69 | 18.80 | 12.00 | 94.9 | 180.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.03 | 11.41 | 18.71 | 2.00 | 83.1 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.80 | 11.08 | 17.54 | 0.00 | 92.9 | 0.0 |
| Bench 3 | Bench Boost | Elliot Anderson | MID | 16 | 5.6 | 2.92 | 9.06 | 14.92 | 12.00 | 73.8 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.80 -> 1.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 48.44
- Actual score: 99.00
- Transfer: Carlos Henrique Casimiro -> Adam Wharton (projected gain 2.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.03 | 10.53 | 16.87 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 2.02 | 6.42 | 10.61 | 5.00 | 82.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 13.00 | 20.77 | 6.00 | 93.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 3.98 | 11.88 | 19.72 | 2.00 | 115.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.24 | 9.48 | 15.67 | 14.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.96 | 9.18 | 15.43 | 3.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.00 | 8.71 | 13.69 | 0.00 | 85.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.80 | 11.79 | 19.88 | 2.00 | 82.5 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.19 | 9.21 | 15.40 | 15.00 | 76.7 | 90.0 |
| Bench 4 | Bench | Jarrod Bowen | FWD | 19 | 7.7 | 2.90 | 8.41 | 14.97 | 2.00 | 58.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.41 | 16.41 | 26.68 | 9.00 | 92.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.34 | 12.97 | 21.33 | 1.00 | 97.1 | 55.0 |
| XI | XI | Adam Wharton | MID | 8 | 5.0 | 3.74 | 11.14 | 16.78 | 11.00 | 90.2 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 3.24 | 9.69 | 16.07 | 12.00 | 80.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.11 | 9.44 | 15.84 | 12.00 | 84.6 | 90.0 |

## GW38

- Train rows: 190183
- Bank: 1.60 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 53.19
- Actual score: 105.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (5.40) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Elliot Anderson -> Dominik Szoboszlai (projected gain 1.97, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (5.40) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mads Hermansen replaced David Raya Martín.
- Autosub outfielders: Pedro Porro Sauceda, Konstantinos Mavropanos.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.45 | 10.12 | 16.49 | 0.00 | 87.0 | 0.0 |
| Bench 1 | Autosub In | Mads Hermansen | GK | 19 | 4.2 | 2.46 | 7.22 | 11.58 | 7.00 | 84.7 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 4.22 | 12.10 | 19.28 | 1.00 | 90.9 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.90 | 11.02 | 17.69 | 2.00 | 95.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.75 | 10.69 | 17.49 | 0.00 | 99.3 | 0.0 |
| Bench 2 | Autosub In | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.23 | 9.11 | 15.08 | 10.00 | 83.4 | 90.0 |
| Bench 3 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.19 | 8.48 | 13.78 | 8.00 | 87.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.64 | 11.28 | 18.27 | 2.00 | 87.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 3.29 | 11.13 | 19.02 | 13.00 | 81.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.40 | 9.40 | 15.73 | 12.00 | 83.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.40 | 16.97 | 28.40 | 14.00 | 92.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 4.05 | 11.89 | 19.92 | 2.00 | 89.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 3.93 | 11.58 | 18.61 | 6.00 | 85.0 | 57.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.4 | 3.36 | 10.41 | 17.61 | 0.00 | 89.0 | 0.0 |
| Bench 4 | Bench | Adam Wharton | MID | 8 | 5.0 | 3.02 | 9.10 | 14.21 | 1.00 | 84.9 | 16.0 |