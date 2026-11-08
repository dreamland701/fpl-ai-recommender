# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 255.11
- Total actual points: 257.00
- Average predicted points: 63.78
- Average actual points: 64.25
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
- Predicted score: 57.45
- Actual score: 48.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.20 | 9.83 | 16.34 | 6.00 | 77.9 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.24 | 0.37 | 0.84 | 0.00 | 5.5 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.95 | 14.44 | 22.68 | 6.00 | 93.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.01 | 11.14 | 17.36 | 1.00 | 60.9 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.2 | 3.34 | 11.02 | 18.78 | 1.00 | 73.5 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 3.38 | 10.04 | 15.55 | 0.00 | 78.9 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.13 | 8.16 | 13.36 | 2.00 | 55.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 6.52 | 18.70 | 30.54 | 7.00 | 78.8 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.66 | 13.66 | 22.99 | 6.00 | 82.0 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.58 | 7.16 | 11.07 | 2.00 | 61.4 | 90.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.31 | 19.15 | 32.25 | 5.00 | 102.1 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.83 | 14.29 | 23.24 | 4.00 | 73.6 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.46 | 13.15 | 20.53 | 4.00 | 95.1 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.43 | 12.56 | 19.95 | 1.00 | 82.0 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.18 | 12.29 | 20.17 | 1.00 | 74.5 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.40
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: bench_boost
- Predicted score: 72.73
- Actual score: 71.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (12.76) beats the best remaining Bench Boost opportunity (8.99).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Elliot Anderson -> Kiernan Dewsbury-Hall (projected gain 1.52, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (12.76) beats the best remaining Bench Boost opportunity (8.99).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.69 | 10.71 | 17.49 | 9.00 | 82.9 | 90.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.07 | 0.53 | 0.00 | 6.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.18 | 14.83 | 23.40 | 11.00 | 93.7 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 5.32 | 12.57 | 18.83 | 5.00 | 99.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.45 | 12.46 | 20.12 | 2.00 | 82.3 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.22 | 10.46 | 15.74 | 4.00 | 103.1 | 180.0 |
| Bench 3 | Bench Boost | James Justin | DEF | 11 | 3.9 | 2.80 | 8.24 | 13.83 | 4.00 | 71.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 8.84 | 22.25 | 35.26 | 11.00 | 129.5 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.66 | 12.21 | 20.75 | 2.00 | 73.2 | 90.0 |
| Bench 4 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.63 | 7.83 | 11.64 | 2.00 | 69.5 | 66.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.06 | 20.79 | 33.93 | 3.00 | 103.9 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.81 | 13.93 | 21.47 | 0.00 | 91.9 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.36 | 12.62 | 20.52 | 2.00 | 75.0 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.76 | 11.33 | 18.15 | 5.00 | 82.5 | 90.0 |
| Bench 2 | Bench Boost | Morgan Gibbs-White | MID | 16 | 7.6 | 3.12 | 10.80 | 18.86 | 0.00 | 45.2 | 0.0 |

## GW37

- Train rows: 189343
- Bank: 0.40 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.21
- Actual score: 75.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 5.86, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.62 | 12.12 | 19.34 | 6.00 | 83.8 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.7 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.17 | 15.97 | 25.29 | 6.00 | 93.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.47 | 13.36 | 22.17 | 2.00 | 108.6 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.08 | 11.47 | 17.93 | 3.00 | 104.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.84 | 11.37 | 18.88 | 14.00 | 83.5 | 90.0 |
| Bench 2 | Bench | James Justin | DEF | 11 | 3.9 | 2.61 | 7.51 | 13.03 | 6.00 | 59.9 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.20 | 19.31 | 32.73 | 9.00 | 80.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.71 | 13.35 | 22.11 | 2.00 | 84.0 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.47 | 6.82 | 10.55 | 11.00 | 57.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.88 | 20.21 | 32.87 | 9.00 | 108.5 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 4.18 | 10.85 | 17.81 | 2.00 | 81.6 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.4 | 3.47 | 10.58 | 18.09 | 12.00 | 68.4 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.05 | 8.49 | 15.49 | 7.00 | 33.9 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.69 | 8.34 | 14.52 | 1.00 | 48.2 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.50 -> 0.60
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 66.71
- Actual score: 63.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.17) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Carlos Henrique Casimiro -> Elliot Anderson (projected gain 2.34, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (7.17) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Kiernan Dewsbury-Hall replaced Marc Guéhi.
- Autosub: Mateus Mané replaced Morgan Rogers.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.23 | 11.92 | 18.93 | 0.00 | 82.4 | 0.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.8 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.17 | 14.68 | 23.61 | 1.00 | 85.9 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 5.06 | 14.19 | 22.64 | 2.00 | 99.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.60 | 12.86 | 20.53 | 0.00 | 96.3 | 0.0 |
| XI | XI | James Justin | DEF | 11 | 3.9 | 3.37 | 9.61 | 15.29 | 1.00 | 75.6 | 90.0 |
| Bench 3 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.21 | 9.36 | 14.83 | 0.00 | 84.3 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 14.6 | 7.17 | 21.14 | 35.09 | 0.00 | 94.9 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.87 | 12.01 | 19.82 | 2.00 | 77.8 | 90.0 |
| Bench 4 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 3.09 | 8.21 | 13.01 | 2.00 | 66.5 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.76 | 20.14 | 33.21 | 14.00 | 105.6 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.26 | 12.54 | 21.14 | 9.00 | 76.5 | 90.0 |
| XI | Bench | Morgan Rogers | MID | 2 | 7.3 | 3.83 | 12.45 | 20.44 | 0.00 | 83.2 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.7 | 4.08 | 11.92 | 19.76 | 2.00 | 90.1 | 64.0 |
| Bench 2 | Autosub In | Kiernan Dewsbury-Hall | MID | 9 | 5.2 | 3.26 | 9.62 | 16.13 | 2.00 | 72.6 | 83.0 |