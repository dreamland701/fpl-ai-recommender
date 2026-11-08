# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 284.09
- Total actual points: 289.00
- Average predicted points: 71.02
- Average actual points: 72.25
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
- Predicted score: 58.66
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.34 | 9.78 | 16.25 | 6.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.04 | 0.23 | 0.00 | 2.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.14 | 14.37 | 22.54 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 3.65 | 10.96 | 18.67 | 1.00 | 78.8 | 90.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.93 | 10.84 | 17.05 | 1.00 | 83.9 | 45.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.12 | 8.15 | 13.35 | 2.00 | 56.6 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 2.45 | 6.76 | 10.19 | 0.00 | 53.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.49 | 18.38 | 29.90 | 7.00 | 75.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.76 | 13.91 | 23.52 | 6.00 | 83.5 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.07 | 12.92 | 22.12 | 2.00 | 76.5 | 87.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.42 | 19.25 | 32.42 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.11 | 14.64 | 23.94 | 4.00 | 80.0 | 20.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.65 | 13.31 | 21.38 | 1.00 | 86.2 | 45.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.62 | 13.09 | 20.43 | 4.00 | 90.0 | 90.0 |
| Bench 2 | Bench | Enzo Le Fée | MID | 17 | 4.8 | 3.92 | 10.86 | 16.98 | 4.00 | 79.1 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Marc Guéhi
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 92.37
- Actual score: 96.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.65) beats the best remaining Triple Captain opportunity (8.93).
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.70): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Nikola Milenković -> Marc Guéhi (projected gain 4.07, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.65) beats the best remaining Triple Captain opportunity (8.93).
- Autosub: James Justin replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.69 | 10.66 | 17.41 | 9.00 | 81.7 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.14 | 1.38 | 1.65 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.24 | 14.75 | 23.24 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 8.15 | 13.01 | 20.06 | 15.00 | 179.1 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.64 | 12.41 | 20.02 | 2.00 | 85.5 | 90.0 |
| Bench 3 | Autosub In | James Justin | DEF | 11 | 3.9 | 2.78 | 8.23 | 13.82 | 4.00 | 71.7 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 1.39 | 4.51 | 7.39 | 0.00 | 38.9 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.55 | 21.87 | 34.53 | 11.00 | 180.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.00 | 12.96 | 22.21 | 2.00 | 79.1 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.93 | 12.50 | 21.33 | 2.00 | 77.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.15 | 20.91 | 34.13 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.96 | 13.84 | 21.31 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.37 | 11.14 | 19.55 | 0.00 | 51.0 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.59 | 10.59 | 17.80 | 12.00 | 66.7 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.38 | 9.57 | 15.61 | 3.00 | 74.7 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.52
- Actual score: 89.00
- Transfer: Morgan Gibbs-White -> Declan Rice (projected gain 4.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.68 | 12.09 | 19.27 | 6.00 | 84.6 | 90.0 |
| Bench 1 | Bench | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.28 | 15.90 | 25.15 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.57 | 13.29 | 22.06 | 2.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.94 | 11.32 | 18.78 | 14.00 | 85.0 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.52 | 13.04 | 6.00 | 61.0 | 90.0 |
| Bench 4 | Bench | Gabriel Gudmundsson | DEF | 11 | 3.8 | 0.09 | 0.52 | 2.82 | 0.00 | 8.7 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 14.6 | 6.19 | 18.92 | 31.95 | 9.00 | 79.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.77 | 13.64 | 22.71 | 2.00 | 84.9 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.38 | 13.30 | 22.82 | 2.00 | 84.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.89 | 20.32 | 33.08 | 9.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.74 | 12.66 | 20.62 | 5.00 | 78.4 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.63 | 11.26 | 19.26 | 12.00 | 80.1 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.59 | 9.89 | 15.83 | 13.00 | 72.3 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.72 | 8.25 | 14.35 | 1.00 | 48.1 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 72.54
- Actual score: 54.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (9.74) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Gabriel Gudmundsson -> Jaka Bijol (projected gain 0.20, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (9.74) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.30 | 11.89 | 18.88 | 0.00 | 83.3 | 0.0 |
| Bench 1 | Bench Boost | Marcus Bettinelli | GK | 13 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 0.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.32 | 14.61 | 23.47 | 1.00 | 87.9 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.08 | 14.12 | 22.51 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.64 | 12.83 | 20.49 | 0.00 | 90.0 | 0.0 |
| Bench 2 | Bench Boost | Jaka Bijol | DEF | 11 | 3.9 | 3.83 | 10.83 | 16.89 | 1.00 | 87.7 | 69.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.46 | 9.62 | 15.31 | 1.00 | 78.0 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.26 | 20.75 | 34.32 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.35 | 15.09 | 24.74 | 12.00 | 90.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 4.11 | 12.35 | 20.53 | 2.00 | 81.2 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.76 | 20.21 | 33.33 | 14.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.61 | 13.44 | 21.54 | 0.00 | 82.7 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.22 | 12.67 | 21.20 | 2.00 | 90.0 | 64.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.88 | 10.28 | 16.48 | 5.00 | 75.5 | 90.0 |
| Bench 4 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.45 | 7.41 | 13.65 | 0.00 | 52.3 | 0.0 |