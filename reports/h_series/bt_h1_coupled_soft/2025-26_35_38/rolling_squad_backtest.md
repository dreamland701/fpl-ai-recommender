# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 279.51
- Total actual points: 287.00
- Average predicted points: 69.88
- Average actual points: 71.75
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
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.62
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.22 | 9.70 | 16.21 | 6.00 | 79.8 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.27 | 0.37 | 0.84 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.15 | 14.44 | 22.68 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.61 | 10.97 | 18.73 | 1.00 | 79.0 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.75 | 10.64 | 16.81 | 1.00 | 83.8 | 45.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.60 | 7.71 | 12.92 | 2.00 | 56.6 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.44 | 6.74 | 10.14 | 0.00 | 53.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.41 | 18.55 | 30.39 | 7.00 | 76.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.66 | 13.61 | 22.94 | 6.00 | 83.1 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.96 | 12.07 | 20.44 | 2.00 | 74.1 | 87.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.42 | 19.15 | 32.25 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.97 | 14.21 | 23.16 | 4.00 | 79.3 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.63 | 13.15 | 20.53 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.42 | 12.47 | 19.87 | 1.00 | 84.1 | 45.0 |
| Bench 2 | Bench | Enzo Le Fée | MID | 17 | 4.8 | 3.85 | 10.48 | 16.21 | 4.00 | 78.3 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Marc Guéhi
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 91.96
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.48) beats the best remaining Triple Captain opportunity (9.04).
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Nikola Milenković -> Marc Guéhi (projected gain 4.85, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.48) beats the best remaining Triple Captain opportunity (9.04).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.62 | 10.64 | 17.43 | 9.00 | 81.9 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.07 | 0.53 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.25 | 14.83 | 23.40 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 8.09 | 13.05 | 20.17 | 15.00 | 179.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.59 | 12.41 | 20.07 | 2.00 | 85.7 | 90.0 |
| Bench 2 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 1.39 | 4.50 | 7.37 | 0.00 | 38.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.73 | 22.25 | 35.26 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.82 | 12.16 | 20.69 | 2.00 | 77.1 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.84 | 12.11 | 20.55 | 2.00 | 76.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.16 | 20.79 | 33.93 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.98 | 13.93 | 21.47 | 0.00 | 90.0 | 0.0 |
| Bench 3 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 2.53 | 9.96 | 17.98 | 0.00 | 50.3 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.19 | 9.56 | 16.06 | 12.00 | 64.4 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.24 | 9.13 | 14.78 | 3.00 | 74.0 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 59.53
- Actual score: 89.00
- Transfer: Morgan Gibbs-White -> Declan Rice (projected gain 5.88, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.57 | 12.03 | 19.25 | 6.00 | 84.7 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.28 | 15.97 | 25.29 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.58 | 13.36 | 22.17 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.88 | 11.31 | 18.82 | 14.00 | 85.1 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 0.10 | 0.51 | 2.81 | 0.00 | 8.7 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.14 | 19.17 | 32.58 | 9.00 | 80.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.65 | 13.30 | 22.06 | 2.00 | 84.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.22 | 12.45 | 21.16 | 2.00 | 81.7 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.21 | 32.87 | 9.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.67 | 12.23 | 19.79 | 5.00 | 76.9 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.36 | 10.34 | 17.62 | 12.00 | 77.8 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.40 | 9.43 | 14.99 | 13.00 | 71.7 | 90.0 |
| Bench 3 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.73 | 8.34 | 14.52 | 1.00 | 48.4 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.40
- Actual score: 54.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.01) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gabriel Gudmundsson -> Jaka Bijol (projected gain 1.26, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.01) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.06 | 11.69 | 18.72 | 0.00 | 83.3 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.22 | 14.58 | 23.51 | 1.00 | 88.1 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.09 | 14.19 | 22.64 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.65 | 12.86 | 20.53 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jaka Bijol | DEF | 11 | 3.9 | 3.72 | 10.72 | 16.78 | 1.00 | 87.7 | 69.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.05 | 9.23 | 14.93 | 1.00 | 78.0 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.35 | 21.14 | 35.09 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.18 | 14.18 | 22.98 | 12.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.64 | 11.61 | 19.43 | 2.00 | 80.5 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.78 | 20.14 | 33.21 | 14.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.28 | 12.72 | 20.39 | 0.00 | 81.2 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.08 | 11.92 | 19.76 | 2.00 | 90.0 | 64.0 |
| Bench 2 | Bench Boost | Enzo Le Fée | MID | 17 | 4.8 | 3.50 | 9.65 | 15.49 | 5.00 | 74.9 | 90.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.46 | 7.49 | 13.79 | 0.00 | 52.5 | 0.0 |