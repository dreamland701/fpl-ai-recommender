# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 207.09
- Total actual points: 308.00
- Average predicted points: 51.77
- Average actual points: 77.00
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
- Bank: 100.00 -> 0.40
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Morgan Gibbs-White
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 47.24
- Actual score: 46.00
- Chip advisory: bench_boost (0.57): Bench depth is strong enough that a Bench Boost is worth considering.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.25 | 10.15 | 15.72 | 6.00 | 86.1 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.65 | 7.36 | 12.04 | 8.00 | 83.8 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.66 | 13.25 | 20.84 | 1.00 | 88.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 4.03 | 11.50 | 17.64 | 6.00 | 91.1 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.13 | 10.08 | 15.91 | 1.00 | 82.6 | 45.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.1 | 3.16 | 9.87 | 15.39 | 4.00 | 83.6 | 90.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.10 | 9.77 | 16.22 | -1.00 | 81.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.18 | 13.75 | 21.11 | 2.00 | 87.2 | 87.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 3.72 | 12.77 | 20.57 | 6.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | 2 | 8.7 | 3.50 | 11.39 | 17.12 | 1.00 | 73.5 | 30.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 4.81 | 15.71 | 26.44 | 5.00 | 96.1 | 90.0 |
| Vice Captain | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 4.41 | 14.07 | 21.86 | 4.00 | 85.5 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 3.78 | 12.44 | 18.11 | 4.00 | 95.3 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.2 | 3.56 | 12.19 | 19.96 | 2.00 | 61.9 | 74.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.89 | 11.76 | 18.20 | 1.00 | 85.3 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.40 -> 0.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Antoine Semenyo
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 60.60
- Actual score: 77.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (13.51) beats the best remaining Bench Boost opportunity (11.83).
- Transfer: Morgan Gibbs-White -> Dominik Szoboszlai (projected gain 2.96, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (13.51) beats the best remaining Bench Boost opportunity (11.83).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.30 | 10.00 | 16.70 | 9.00 | 87.9 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.10 | 7.53 | 12.37 | 3.00 | 85.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 3.54 | 11.40 | 18.66 | 11.00 | 75.7 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.49 | 10.42 | 17.06 | 1.00 | 88.7 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.74 | 9.95 | 16.40 | 2.00 | 89.5 | 90.0 |
| Bench 3 | Bench Boost | Neco Williams | DEF | 16 | 4.8 | 2.69 | 8.05 | 13.61 | 2.00 | 73.8 | 90.0 |
| Bench 4 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.47 | 7.77 | 13.20 | 4.00 | 82.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 3.92 | 12.96 | 21.40 | 2.00 | 85.8 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.96 | 12.06 | 20.91 | 2.00 | 87.2 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.40 | 10.30 | 17.79 | 9.00 | 69.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.91 | 17.08 | 28.62 | 3.00 | 102.2 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.20 | 12.78 | 20.04 | 0.00 | 92.9 | 0.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.1 | 4.19 | 12.41 | 20.42 | 2.00 | 87.6 | 90.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 13 | 8.2 | 4.84 | 11.69 | 18.90 | 12.00 | 95.9 | 180.0 |
| Bench 2 | Bench Boost | Elliot Anderson | MID | 16 | 5.6 | 2.92 | 9.06 | 15.02 | 12.00 | 73.8 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.90 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 47.86
- Actual score: 87.00
- Transfer: Neco Williams -> Marc Guéhi (projected gain 3.20, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 3.73 | 9.53 | 15.27 | 6.00 | 88.1 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 2.46 | 6.94 | 11.49 | 2.00 | 88.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.94 | 13.00 | 20.87 | 6.00 | 93.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 3.98 | 11.88 | 19.72 | 2.00 | 106.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.24 | 9.48 | 15.67 | 14.00 | 86.2 | 90.0 |
| Bench 3 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 2.96 | 8.78 | 14.53 | 3.00 | 83.3 | 90.0 |
| Bench 2 | Bench | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.00 | 8.71 | 13.69 | 0.00 | 85.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.50 | 10.39 | 17.38 | 2.00 | 82.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.30 | 10.11 | 17.07 | 2.00 | 82.7 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.8 | 3.19 | 9.51 | 16.00 | 15.00 | 76.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.41 | 16.01 | 26.38 | 9.00 | 102.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 4.34 | 12.87 | 21.33 | 1.00 | 97.1 | 55.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.69 | 10.89 | 18.27 | 9.00 | 84.5 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.11 | 9.14 | 15.34 | 12.00 | 84.6 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.49 | 7.78 | 13.39 | 1.00 | 62.9 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.60 -> 0.90
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 51.39
- Actual score: 98.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Pascal Groß (projected gain 1.17, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (4.70) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub outfielders: Pedro Porro Sauceda.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 3.45 | 10.12 | 16.49 | 0.00 | 87.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.59 | 8.31 | 13.61 | 6.00 | 87.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 4.22 | 11.80 | 19.18 | 1.00 | 90.9 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.90 | 11.02 | 17.89 | 2.00 | 93.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 3.75 | 9.99 | 16.29 | 0.00 | 99.3 | 0.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.19 | 8.48 | 13.58 | 8.00 | 87.2 | 90.0 |
| Bench 3 | Autosub In | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.23 | 8.41 | 13.68 | 10.00 | 83.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.04 | 11.98 | 19.27 | 2.00 | 87.8 | 90.0 |
| XI | XI | Ollie Watkins | FWD | 2 | 8.7 | 3.29 | 10.43 | 17.72 | 13.00 | 81.7 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.40 | 9.40 | 15.73 | 12.00 | 83.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 4.70 | 16.17 | 27.40 | 14.00 | 83.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 3.93 | 11.28 | 18.41 | 6.00 | 85.0 | 57.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.6 | 3.56 | 10.66 | 17.63 | 2.00 | 84.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 7.0 | 3.75 | 10.59 | 17.72 | 2.00 | 89.2 | 90.0 |
| Bench 2 | Bench | Elliot Anderson | MID | 16 | 5.6 | 3.28 | 9.52 | 15.92 | 2.00 | 90.6 | 64.0 |