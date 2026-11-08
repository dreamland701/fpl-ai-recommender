# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 277.46
- Total actual points: 259.00
- Average predicted points: 69.37
- Average actual points: 64.75
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
- Predicted score: 56.09
- Actual score: 46.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.21 | 9.89 | 16.20 | 6.00 | 83.3 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.22 | 0.45 | 0.80 | 0.00 | 6.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.91 | 14.53 | 22.59 | 6.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 3.97 | 11.56 | 17.27 | 0.00 | 81.8 | 45.0 |
| XI | XI | Nikola Milenković | DEF | 16 | 5.1 | 3.85 | 10.79 | 16.74 | 1.00 | 84.1 | 45.0 |
| Bench 2 | Bench | Jaydee Canvot | DEF | 8 | 4.5 | 3.59 | 10.40 | 16.18 | 0.00 | 81.9 | 90.0 |
| Bench 3 | Bench | Chris Richards | DEF | 8 | 4.4 | 3.32 | 9.78 | 14.90 | 1.00 | 81.5 | 14.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 5.82 | 16.88 | 27.46 | 7.00 | 63.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.76 | 13.69 | 22.66 | 6.00 | 85.3 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.84 | 7.54 | 11.51 | 2.00 | 69.4 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 5.92 | 18.00 | 30.32 | 5.00 | 90.0 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.88 | 14.03 | 22.47 | 4.00 | 80.9 | 20.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.31 | 12.86 | 19.54 | 4.00 | 90.0 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.41 | 12.69 | 19.89 | 1.00 | 83.9 | 45.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.14 | 11.87 | 19.18 | 1.00 | 76.3 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Marc Guéhi
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 96.01
- Actual score: 98.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.85) beats the best remaining Triple Captain opportunity (8.62).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Nikola Milenković -> Marc Guéhi (projected gain 2.93, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.85) beats the best remaining Triple Captain opportunity (8.62).
- Autosub: Elliot Anderson replaced Carlos Henrique Casimiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.69 | 10.84 | 17.40 | 9.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.08 | 0.48 | 0.00 | 5.6 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.13 | 14.89 | 23.41 | 11.00 | 90.0 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 8.00 | 12.68 | 20.31 | 15.00 | 180.0 | 180.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 6.81 | 10.97 | 16.85 | 4.00 | 156.1 | 180.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 6.29 | 9.80 | 14.92 | 3.00 | 112.7 | 171.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.4 | 4.21 | 7.60 | 12.58 | 4.00 | 99.2 | 180.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.05 | 20.75 | 33.56 | 11.00 | 180.0 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 3.85 | 12.16 | 20.53 | 2.00 | 79.6 | 90.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.82 | 8.09 | 12.30 | 2.00 | 73.5 | 66.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.73 | 19.72 | 32.05 | 3.00 | 90.0 | 90.0 |
| XI | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.82 | 13.75 | 20.91 | 0.00 | 90.0 | 0.0 |
| XI | XI | Morgan Rogers | MID | 2 | 7.5 | 4.36 | 12.20 | 19.41 | 2.00 | 77.3 | 90.0 |
| Bench 3 | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.08 | 10.21 | 17.47 | 0.00 | 49.6 | 0.0 |
| Bench 2 | Autosub In | Elliot Anderson | MID | 16 | 5.6 | 3.38 | 9.78 | 15.91 | 12.00 | 63.6 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.07
- Actual score: 69.00
- Transfer: Morgan Rogers -> Declan Rice (projected gain 1.29, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.51 | 11.94 | 18.47 | 6.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.85 | 15.34 | 23.78 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.61 | 12.93 | 21.34 | 2.00 | 90.0 | 90.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 4.62 | 12.38 | 19.35 | 3.00 | 90.0 | 90.0 |
| XI | XI | Daniel Muñoz Mejía | DEF | 8 | 5.8 | 4.42 | 11.54 | 17.73 | 6.00 | 90.0 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.4 | 4.29 | 11.29 | 18.04 | 0.00 | 90.0 | 29.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 5.94 | 18.02 | 30.39 | 9.00 | 80.7 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.68 | 13.03 | 21.46 | 2.00 | 86.5 | 90.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.37 | 6.64 | 10.58 | 11.00 | 56.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.56 | 19.36 | 31.37 | 9.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.47 | 11.85 | 18.89 | 5.00 | 76.8 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.54 | 10.74 | 18.01 | 12.00 | 79.9 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.07 | 7.96 | 14.55 | 7.00 | 34.7 | 90.0 |
| Bench 2 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.50 | 7.68 | 13.38 | 1.00 | 41.6 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.20 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 65.29
- Actual score: 46.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.77) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Daniel Muñoz Mejía -> Marcos Senesi Barón (projected gain 2.56, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.77) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.09 | 11.59 | 17.93 | 0.00 | 85.0 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.0 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.95 | 13.98 | 22.22 | 1.00 | 87.4 | 45.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 5.2 | 4.43 | 12.61 | 20.35 | 2.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.47 | 12.44 | 19.42 | 0.00 | 90.0 | 0.0 |
| XI | XI | Jaydee Canvot | DEF | 8 | 4.5 | 3.47 | 9.84 | 15.62 | 0.00 | 84.3 | 0.0 |
| Bench 4 | Bench Boost | Chris Richards | DEF | 8 | 4.4 | 2.23 | 6.99 | 11.76 | 0.00 | 54.3 | 0.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.72 | 19.57 | 31.54 | 0.00 | 90.0 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.92 | 11.95 | 19.75 | 2.00 | 78.9 | 90.0 |
| Bench 2 | Bench Boost | Mateus Mané | FWD | 20 | 4.2 | 2.93 | 8.04 | 12.65 | 2.00 | 67.7 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.43 | 19.11 | 31.51 | 14.00 | 90.0 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.2 | 4.23 | 12.45 | 19.69 | 0.00 | 79.1 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.13 | 11.83 | 20.08 | 9.00 | 75.7 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.96 | 11.41 | 18.73 | 2.00 | 90.0 | 64.0 |
| Bench 3 | Bench Boost | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.60 | 7.42 | 14.07 | 0.00 | 55.5 | 0.0 |