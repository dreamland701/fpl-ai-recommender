# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 204.98
- Total actual points: 270.00
- Average predicted points: 51.25
- Average actual points: 67.50
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
- Predicted score: 46.59
- Actual score: 45.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | -1 | 6.0 | 3.26 | 9.38 | 14.68 | 6.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | -1 | 4.2 | 2.60 | 7.29 | 11.34 | 2.00 | 83.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.2 | 3.85 | 11.23 | 18.54 | 1.00 | 90.1 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 7.1 | 3.66 | 11.16 | 17.98 | 6.00 | 89.6 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.1 | 3.06 | 9.30 | 14.72 | 6.00 | 83.0 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | -1 | 5.1 | 3.05 | 8.93 | 13.83 | 4.00 | 75.7 | 90.0 |
| Bench 4 | Bench | Marcos Senesi Barón | DEF | -1 | 5.2 | 3.04 | 8.53 | 14.15 | 14.00 | 74.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | -1 | 7.4 | 3.83 | 11.30 | 18.24 | 6.00 | 79.0 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | -1 | 7.7 | 3.88 | 11.01 | 17.88 | 2.00 | 85.0 | 87.0 |
| Bench 2 | Bench | Ollie Watkins | FWD | -1 | 8.7 | 3.27 | 10.25 | 15.70 | 1.00 | 72.8 | 30.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | -1 | 10.3 | 5.32 | 15.51 | 25.49 | 5.00 | 94.1 | 90.0 |
| Vice Captain | XI | Morgan Gibbs-White | MID | -1 | 7.5 | 3.90 | 11.61 | 18.07 | 4.00 | 84.4 | 20.0 |
| XI | XI | Morgan Rogers | MID | -1 | 7.4 | 3.59 | 11.49 | 18.60 | 1.00 | 76.2 | 90.0 |
| XI | XI | Elliot Anderson | MID | -1 | 5.6 | 3.53 | 11.05 | 17.06 | 1.00 | 86.9 | 45.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | -1 | 5.1 | 3.38 | 10.82 | 16.56 | 2.00 | 90.2 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Marc Guéhi
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 61.18
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.96) beats the best remaining Bench Boost opportunity (12.86).
- Transfer: Elliot Anderson -> Carlos Henrique Casimiro (projected gain 1.64, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.96) beats the best remaining Bench Boost opportunity (12.86).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | -1 | 6.0 | 3.35 | 8.95 | 14.12 | 9.00 | 88.8 | 90.0 |
| Bench 1 | Bench Boost | Mads Hermansen | GK | -1 | 4.2 | 2.46 | 6.31 | 9.27 | 2.00 | 83.2 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | -1 | 5.1 | 4.58 | 11.52 | 16.29 | 15.00 | 140.8 | 180.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 7.2 | 4.34 | 11.47 | 18.26 | 11.00 | 93.3 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | -1 | 5.2 | 3.97 | 10.29 | 16.28 | 8.00 | 94.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.2 | 3.42 | 9.18 | 15.39 | 2.00 | 90.2 | 90.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | -1 | 6.1 | 2.92 | 7.83 | 12.40 | 5.00 | 85.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | -1 | 7.4 | 3.58 | 11.53 | 18.33 | 2.00 | 86.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | -1 | 7.8 | 3.59 | 9.71 | 15.51 | 2.00 | 85.5 | 90.0 |
| Bench 3 | Bench Boost | Ollie Watkins | FWD | -1 | 8.8 | 3.04 | 7.45 | 11.66 | 9.00 | 68.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | -1 | 10.4 | 5.92 | 15.94 | 25.73 | 3.00 | 99.8 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | -1 | 7.6 | 3.73 | 10.78 | 17.38 | 0.00 | 73.6 | 0.0 |
| XI | XI | Morgan Rogers | MID | -1 | 7.5 | 3.56 | 10.39 | 16.18 | 2.00 | 83.0 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | -1 | 5.8 | 3.58 | 10.38 | 15.56 | 0.00 | 92.9 | 0.0 |
| Bench 2 | Bench Boost | Kiernan Dewsbury-Hall | MID | -1 | 5.2 | 3.21 | 8.76 | 13.92 | 5.00 | 85.9 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.20 -> 1.20
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 47.24
- Actual score: 76.00
- Transfer: Morgan Gibbs-White -> Rayan Cherki (projected gain 1.45, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | -1 | 6.1 | 4.04 | 9.57 | 14.61 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Mads Hermansen | GK | -1 | 4.2 | 2.11 | 5.45 | 8.57 | 5.00 | 82.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | -1 | 7.2 | 4.95 | 12.13 | 18.89 | 6.00 | 93.8 | 90.0 |
| XI | XI | Marc Guéhi | DEF | -1 | 5.1 | 3.86 | 11.73 | 18.41 | 2.00 | 100.8 | 90.0 |
| XI | XI | Marcos Senesi Barón | DEF | -1 | 5.2 | 3.15 | 8.87 | 14.63 | 4.00 | 84.0 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | -1 | 6.1 | 2.98 | 8.68 | 14.10 | 14.00 | 66.1 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 6.2 | 3.10 | 7.88 | 11.40 | 8.00 | 83.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | -1 | 7.3 | 3.54 | 10.00 | 16.24 | 2.00 | 84.8 | 90.0 |
| Bench 3 | Bench | Jarrod Bowen | FWD | -1 | 7.7 | 2.64 | 8.25 | 14.29 | 2.00 | 56.9 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.8 | 3.02 | 8.15 | 12.78 | 15.00 | 76.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | -1 | 10.4 | 5.84 | 15.69 | 24.95 | 9.00 | 99.4 | 90.0 |
| XI | XI | Rayan Cherki | MID | -1 | 6.6 | 3.19 | 10.09 | 16.07 | 1.00 | 51.9 | 34.0 |
| XI | XI | Morgan Rogers | MID | -1 | 7.5 | 3.33 | 9.29 | 14.44 | 12.00 | 80.2 | 90.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | -1 | 5.2 | 3.38 | 9.09 | 13.89 | 2.00 | 83.7 | 90.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | -1 | 5.8 | 2.11 | 6.28 | 10.61 | 1.00 | 31.1 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 1.20 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Virgil van Dijk
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 49.98
- Actual score: 71.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (4.85) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Rayan Cherki -> Declan Rice (projected gain 1.57, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (4.85) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Mads Hermansen replaced David Raya Martín.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | -1 | 6.1 | 3.41 | 8.85 | 13.04 | 0.00 | 87.2 | 0.0 |
| Bench 1 | Autosub In | Mads Hermansen | GK | -1 | 4.2 | 2.68 | 5.92 | 8.85 | 7.00 | 83.9 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 7.3 | 3.79 | 10.78 | 16.82 | 1.00 | 90.4 | 45.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | -1 | 6.1 | 4.15 | 10.69 | 17.03 | 2.00 | 94.0 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | -1 | 5.1 | 3.97 | 9.90 | 15.43 | 0.00 | 101.2 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | -1 | 5.2 | 3.34 | 9.18 | 14.80 | 2.00 | 71.2 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | -1 | 6.2 | 2.61 | 7.54 | 12.05 | 0.00 | 61.4 | 0.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | -1 | 7.3 | 3.38 | 9.58 | 15.60 | 2.00 | 66.3 | 90.0 |
| XI | XI | Ollie Watkins | FWD | -1 | 8.7 | 3.22 | 8.57 | 13.77 | 13.00 | 75.8 | 90.0 |
| Bench 2 | Bench | Jarrod Bowen | FWD | -1 | 7.7 | 3.06 | 7.74 | 12.67 | 12.00 | 57.0 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | -1 | 10.4 | 4.85 | 15.74 | 25.07 | 14.00 | 81.1 | 90.0 |
| XI | Bench | Morgan Rogers | MID | -1 | 7.4 | 3.39 | 9.80 | 14.84 | 0.00 | 87.7 | 0.0 |
| XI | Bench | Declan Rice | MID | -1 | 7.2 | 3.54 | 9.29 | 14.05 | 0.00 | 84.1 | 0.0 |
| XI | XI | Kiernan Dewsbury-Hall | MID | -1 | 5.3 | 3.24 | 7.95 | 12.20 | 2.00 | 82.4 | 83.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | -1 | 5.9 | 1.99 | 5.37 | 9.43 | 0.00 | 40.8 | 0.0 |