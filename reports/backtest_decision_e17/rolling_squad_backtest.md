# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 206.65
- Total actual points: 300.00
- Average predicted points: 51.66
- Average actual points: 75.00
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
- Bank: 100.00 -> 1.00
- Free transfers: 1 -> 2
- Captain: Morgan Gibbs-White
- Vice captain: Bruno Borges Fernandes
- Effective captain: Morgan Gibbs-White
- Chip used: none
- Predicted score: 49.05
- Actual score: 45.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.25 | 10.15 | 15.72 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 2.47 | 7.93 | 12.71 | 2.00 | 83.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.06 | 12.85 | 19.84 | 1.00 | 88.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.03 | 11.50 | 17.64 | 6.00 | 91.1 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.1 | 3.16 | 9.87 | 15.49 | 4.00 | 83.6 | 90.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.10 | 9.77 | 15.92 | -1.00 | 81.6 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.13 | 9.38 | 14.91 | 1.00 | 82.6 | 45.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.18 | 13.45 | 20.41 | 2.00 | 87.2 | 87.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.02 | 12.77 | 20.57 | 6.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | 2 | 8.7 | 3.50 | 11.39 | 16.42 | 1.00 | 73.5 | 30.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.3 | 4.81 | 15.71 | 26.44 | 5.00 | 96.1 | 90.0 |
| Captain | Captain | Morgan Gibbs-White | MID | 16 | 7.5 | 4.81 | 14.37 | 21.86 | 4.00 | 85.5 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 4.08 | 12.44 | 18.41 | 4.00 | 95.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 3.96 | 12.19 | 19.56 | 2.00 | 72.9 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.89 | 11.76 | 17.90 | 1.00 | 85.3 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 1.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 59.36
- Actual score: 76.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.67) beats the best remaining Bench Boost opportunity (12.28).
- Transfer: Morgan Gibbs-White -> Dominik Szoboszlai (projected gain 4.06, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.67) beats the best remaining Bench Boost opportunity (12.28).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.30 | 10.00 | 16.70 | 9.00 | 87.9 | 90.0 |
| Bench 1 | Bench Boost | Mads Hermansen | GK | 19 | 4.2 | 2.26 | 6.67 | 11.29 | 2.00 | 84.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.54 | 11.40 | 18.66 | 11.00 | 75.7 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.49 | 10.42 | 17.06 | 1.00 | 88.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.74 | 9.95 | 16.30 | 2.00 | 89.5 | 90.0 |
| Bench 3 | Bench Boost | Neco Williams | DEF | 16 | 4.8 | 2.69 | 8.05 | 13.61 | 2.00 | 73.8 | 90.0 |
| Bench 4 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.47 | 7.37 | 12.50 | 4.00 | 82.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 3.92 | 12.26 | 20.40 | 2.00 | 85.8 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.96 | 11.36 | 19.41 | 2.00 | 87.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.40 | 10.30 | 17.69 | 9.00 | 69.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.61 | 17.08 | 28.62 | 3.00 | 92.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.19 | 12.41 | 20.42 | 2.00 | 87.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.44 | 11.29 | 18.60 | 12.00 | 85.9 | 180.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 3.80 | 10.68 | 16.94 | 0.00 | 92.9 | 0.0 |
| Bench 2 | Bench Boost | Elliot Anderson | MID | 16 | 5.6 | 2.92 | 8.36 | 13.82 | 12.00 | 73.8 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 1.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 47.56
- Actual score: 87.00
- Transfer: Neco Williams -> Marc Guéhi (projected gain 3.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 3.73 | 9.93 | 15.87 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | 19 | 4.2 | 2.32 | 7.12 | 11.81 | 5.00 | 82.8 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.64 | 12.40 | 20.07 | 6.00 | 93.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 3.98 | 11.88 | 19.72 | 2.00 | 106.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.24 | 9.88 | 16.37 | 14.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.96 | 8.78 | 14.53 | 3.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.00 | 8.71 | 13.79 | 0.00 | 85.1 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.49 | 10.91 | 18.40 | 15.00 | 76.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.50 | 10.39 | 17.48 | 2.00 | 82.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.30 | 9.81 | 16.67 | 2.00 | 82.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.41 | 15.91 | 26.38 | 9.00 | 92.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.34 | 12.87 | 21.33 | 1.00 | 97.1 | 55.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.39 | 10.39 | 17.37 | 9.00 | 84.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.11 | 9.44 | 15.84 | 12.00 | 84.6 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.49 | 8.08 | 14.19 | 1.00 | 58.9 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.20 -> 1.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Igor Thiago Nascimento Rodrigues
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 50.68
- Actual score: 92.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Pedro Porro Sauceda -> Sven Botman (projected gain 0.48, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (4.70) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mads Hermansen replaced David Raya Martín.
- Autosub outfielders: Elliot Anderson.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.45 | 9.82 | 15.99 | 0.00 | 87.0 | 0.0 |
| Bench 1 | Autosub In | Mads Hermansen | GK | 19 | 4.2 | 2.46 | 7.22 | 11.88 | 7.00 | 84.7 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 3.52 | 11.40 | 18.88 | 1.00 | 70.9 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.90 | 10.72 | 17.59 | 2.00 | 94.2 | 90.0 |
| XI | XI | Sven Botman | DEF | 15 | 4.9 | 3.56 | 10.38 | 16.34 | 3.00 | 88.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.75 | 10.29 | 16.69 | 0.00 | 96.3 | 0.0 |
| Bench 3 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.19 | 8.78 | 14.08 | 8.00 | 87.2 | 90.0 |
| Vice Captain | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.04 | 12.28 | 19.97 | 2.00 | 87.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 3.29 | 10.43 | 17.82 | 13.00 | 81.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.40 | 9.40 | 15.73 | 12.00 | 83.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 4.70 | 16.17 | 27.40 | 14.00 | 83.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 3.93 | 11.58 | 18.81 | 6.00 | 85.0 | 57.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.75 | 10.59 | 17.72 | 2.00 | 89.2 | 90.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.28 | 9.92 | 16.62 | 2.00 | 90.6 | 64.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.9 | 2.55 | 7.60 | 13.70 | 0.00 | 70.1 | 0.0 |