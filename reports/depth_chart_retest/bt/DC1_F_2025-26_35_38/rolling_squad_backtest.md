# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 282.34
- Total actual points: 283.00
- Average predicted points: 70.58
- Average actual points: 70.75
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
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.02
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.63 | 10.62 | 17.60 | 6.00 | 83.1 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.27 | 0.34 | 0.77 | 0.00 | 5.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.93 | 13.86 | 21.76 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.53 | 10.68 | 18.25 | 1.00 | 77.9 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.87 | 10.66 | 16.76 | 1.00 | 83.1 | 45.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.10 | 8.08 | 13.23 | 2.00 | 55.8 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.41 | 6.61 | 9.93 | 0.00 | 52.7 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.79 | 19.29 | 31.46 | 7.00 | 79.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 5.08 | 14.70 | 24.65 | 6.00 | 87.1 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 3.98 | 12.20 | 20.67 | 2.00 | 73.8 | 87.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.46 | 19.31 | 32.54 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.79 | 13.58 | 22.12 | 4.00 | 76.6 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.56 | 12.97 | 20.27 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.61 | 12.83 | 20.40 | 1.00 | 84.5 | 45.0 |
| Bench 2 | Bench | Enzo Le Fée | MID | 17 | 4.8 | 3.92 | 10.70 | 16.60 | 4.00 | 78.8 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Marc Guéhi
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 93.76
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.81) beats the best remaining Triple Captain opportunity (9.24).
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Nikola Milenković -> Marc Guéhi (projected gain 3.87, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.81) beats the best remaining Triple Captain opportunity (9.24).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.99 | 11.53 | 18.80 | 9.00 | 85.2 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.03 | 0.45 | 0.00 | 5.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.99 | 14.13 | 22.30 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 7.86 | 12.66 | 19.54 | 15.00 | 175.7 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.50 | 12.09 | 19.55 | 2.00 | 84.4 | 90.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.72 | 8.10 | 13.60 | 4.00 | 70.2 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 1.38 | 4.44 | 7.27 | 0.00 | 37.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 15.06 | 22.71 | 35.98 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.25 | 13.25 | 22.38 | 2.00 | 81.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 3.95 | 12.40 | 21.01 | 2.00 | 76.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.21 | 20.98 | 34.26 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.92 | 13.79 | 21.28 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.09 | 10.21 | 17.94 | 0.00 | 48.2 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.49 | 9.96 | 16.57 | 12.00 | 64.5 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.43 | 9.56 | 15.47 | 3.00 | 74.9 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.72
- Actual score: 89.00
- Transfer: Morgan Gibbs-White -> Declan Rice (projected gain 4.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.94 | 12.83 | 20.46 | 6.00 | 87.9 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.01 | 15.24 | 24.13 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.42 | 12.97 | 21.59 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.76 | 10.90 | 18.15 | 14.00 | 83.1 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.68 | 7.59 | 13.16 | 6.00 | 60.6 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 0.11 | 0.56 | 2.89 | 0.00 | 7.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.49 | 19.91 | 33.65 | 9.00 | 82.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 5.02 | 14.23 | 23.49 | 2.00 | 87.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.33 | 12.78 | 21.69 | 2.00 | 81.6 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.01 | 20.57 | 33.48 | 9.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.60 | 12.13 | 19.67 | 5.00 | 76.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.45 | 10.39 | 17.67 | 12.00 | 77.3 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.68 | 9.99 | 15.88 | 13.00 | 72.9 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.71 | 8.28 | 14.45 | 1.00 | 48.4 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 68.83
- Actual score: 48.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (5.89) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Enzo Le Fée -> Alex Scott (projected gain 0.83, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (5.89) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.59 | 12.70 | 20.16 | 0.00 | 86.7 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.06 | 13.95 | 22.46 | 1.00 | 85.4 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.87 | 13.61 | 21.74 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.44 | 12.32 | 19.68 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.42 | 9.51 | 15.11 | 1.00 | 76.9 | 90.0 |
| Bench 4 | Bench Boost | Gabriel Gudmundsson | DEF | 11 | 3.8 | 0.07 | 0.54 | 2.32 | 0.00 | 7.9 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.47 | 21.47 | 35.58 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.25 | 14.39 | 23.30 | 12.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.44 | 13.09 | 21.54 | 2.00 | 84.7 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.95 | 20.65 | 34.05 | 14.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.48 | 12.89 | 20.53 | 0.00 | 80.7 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.08 | 11.95 | 19.82 | 2.00 | 90.0 | 64.0 |
| XI | XI | Alex Scott | MID | 4 | 4.9 | 3.84 | 11.05 | 17.77 | 0.00 | 80.0 | 0.0 |
| Bench 3 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.40 | 7.36 | 13.63 | 0.00 | 52.0 | 0.0 |