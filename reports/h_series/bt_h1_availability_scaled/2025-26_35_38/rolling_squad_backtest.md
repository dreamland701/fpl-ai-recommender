# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW34
- Simulated weeks: GW35-GW38
- Total predicted points: 292.88
- Total actual points: 274.00
- Average predicted points: 73.22
- Average actual points: 68.50
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
- Predicted score: 62.15
- Actual score: 54.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.50 | 10.28 | 17.10 | 6.00 | 81.3 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.27 | 0.37 | 0.84 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 4.96 | 13.92 | 21.86 | 6.00 | 87.8 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 4.48 | 12.76 | 19.88 | 1.00 | 61.1 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.8 | 3.73 | 10.40 | 16.74 | 1.00 | 75.7 | 45.0 |
| Bench 4 | Bench | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.51 | 10.36 | 18.22 | -1.00 | 72.0 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 3.63 | 9.50 | 15.56 | 2.00 | 59.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 7.18 | 20.43 | 33.37 | 7.00 | 76.2 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.4 | 4.93 | 14.29 | 24.05 | 6.00 | 84.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.55 | 14.00 | 23.75 | 2.00 | 77.6 | 87.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.34 | 18.91 | 31.85 | 5.00 | 89.2 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 5.62 | 15.78 | 25.14 | 5.00 | 60.1 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 5.43 | 15.38 | 25.02 | 4.00 | 80.4 | 20.0 |
| Bench 2 | Bench | Pascal Groß | MID | 6 | 5.5 | 4.12 | 12.30 | 21.59 | 2.00 | 59.3 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 4.25 | 11.53 | 17.84 | 4.00 | 81.0 | 90.0 |

## GW36

- Train rows: 188505
- Bank: 0.00 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Rayan Cherki
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 98.73
- Actual score: 83.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (17.73) beats the best remaining Triple Captain opportunity (8.98).
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (17.73) beats the best remaining Triple Captain opportunity (8.98).
- Autosub: Enzo Le Fée replaced Morgan Gibbs-White.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.86 | 11.21 | 18.32 | 9.00 | 83.2 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.07 | 0.53 | 0.00 | 6.2 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.16 | 14.58 | 23.00 | 11.00 | 90.0 | 90.0 |
| XI | XI | Nico O'Reilly | DEF | 13 | 5.2 | 8.45 | 13.61 | 20.38 | 5.00 | 145.2 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.04 | 9.14 | 15.29 | 4.00 | 76.4 | 90.0 |
| Bench 3 | Bench | Neco Williams | DEF | 16 | 4.8 | 2.88 | 8.30 | 13.86 | 2.00 | 62.8 | 90.0 |
| Bench 4 | Bench | James Justin | DEF | 11 | 3.9 | 2.78 | 8.24 | 13.83 | 4.00 | 71.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 14.6 | 14.63 | 22.10 | 35.02 | 11.00 | 180.1 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.30 | 13.57 | 23.05 | 2.00 | 79.6 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.26 | 13.45 | 22.85 | 2.00 | 79.2 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.07 | 20.54 | 33.53 | 3.00 | 89.4 | 90.0 |
| Vice Captain | XI | Rayan Cherki | MID | 13 | 6.5 | 10.38 | 16.34 | 25.02 | 5.00 | 144.2 | 70.0 |
| XI | Bench | Morgan Gibbs-White | MID | 16 | 7.6 | 3.85 | 12.56 | 21.94 | 0.00 | 51.3 | 0.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 4.46 | 11.74 | 19.46 | 6.00 | 81.1 | 90.0 |
| Bench 2 | Autosub In | Enzo Le Fée | MID | 17 | 4.8 | 3.73 | 10.32 | 16.65 | 3.00 | 76.8 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Erling Haaland
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 60.24
- Actual score: 65.00
- Transfer: Nico O'Reilly -> Marc Guéhi (projected gain 3.54, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.77 | 12.34 | 19.68 | 6.00 | 85.1 | 90.0 |
| Bench 1 | Bench | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.3 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.19 | 15.72 | 24.90 | 6.00 | 90.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.50 | 13.14 | 21.81 | 2.00 | 89.5 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.43 | 9.96 | 16.49 | 3.00 | 80.2 | 90.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.8 | 3.22 | 9.67 | 15.76 | 1.00 | 80.4 | 90.0 |
| Bench 3 | Bench | James Justin | DEF | 11 | 3.9 | 2.66 | 7.51 | 13.03 | 6.00 | 61.0 | 90.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 6.66 | 20.49 | 34.72 | 9.00 | 79.4 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.3 | 4.86 | 13.79 | 22.84 | 2.00 | 85.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.51 | 13.33 | 22.68 | 2.00 | 83.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.83 | 20.01 | 32.55 | 9.00 | 90.0 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.25 | 14.66 | 24.51 | 1.00 | 52.1 | 34.0 |
| XI | XI | Pascal Groß | MID | 6 | 5.5 | 3.40 | 10.92 | 19.17 | 3.00 | 69.0 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 4.00 | 10.82 | 17.12 | 13.00 | 74.9 | 90.0 |
| Bench 4 | Bench | Morgan Gibbs-White | MID | 16 | 7.5 | 2.17 | 8.49 | 15.49 | 7.00 | 36.7 | 90.0 |

## GW38

- Train rows: 190183
- Bank: 0.10 -> -0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 71.76
- Actual score: 72.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.97) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Neco Williams -> Sven Botman (projected gain 0.90, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.97) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.28 | 11.85 | 18.83 | 0.00 | 82.1 | 0.0 |
| Bench 1 | Bench Boost | Hákon Rafn Valdimarsson | GK | 5 | 3.8 | 0.00 | 0.00 | 0.00 | 0.00 | 1.4 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.29 | 14.58 | 23.45 | 1.00 | 87.0 | 45.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.51 | 12.50 | 19.95 | 0.00 | 87.4 | 0.0 |
| XI | XI | Sven Botman | DEF | 15 | 4.9 | 3.89 | 11.32 | 17.73 | 3.00 | 86.1 | 90.0 |
| Bench 3 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.79 | 10.45 | 16.71 | 8.00 | 83.9 | 90.0 |
| Bench 4 | Bench Boost | James Justin | DEF | 11 | 3.9 | 3.37 | 9.37 | 14.91 | 1.00 | 78.3 | 90.0 |
| Captain | XI | Erling Haaland | FWD | 13 | 14.6 | 7.27 | 20.91 | 34.71 | 0.00 | 87.9 | 0.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 5.07 | 13.90 | 22.53 | 12.00 | 88.9 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 7.2 | 3.94 | 11.70 | 19.32 | 2.00 | 79.9 | 90.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.62 | 19.67 | 32.44 | 14.00 | 86.7 | 90.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.39 | 13.08 | 22.05 | 9.00 | 76.1 | 90.0 |
| XI | XI | Rayan Cherki | MID | 13 | 6.5 | 4.25 | 12.80 | 21.21 | 1.00 | 50.1 | 32.0 |
| Bench 2 | Bench Boost | Pascal Groß | MID | 6 | 5.5 | 3.81 | 11.44 | 18.91 | 2.00 | 78.7 | 90.0 |
| XI | XI | Enzo Le Fée | MID | 17 | 4.8 | 3.99 | 10.37 | 16.45 | 5.00 | 75.5 | 90.0 |