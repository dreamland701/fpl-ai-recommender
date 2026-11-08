# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW13
- Simulated weeks: GW14-GW17
- Total predicted points: 248.48
- Total actual points: 277.00
- Average predicted points: 62.12
- Average actual points: 69.25
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW13 are included before the first simulated week.
- League-average scores were not available for this run.

## GW14

- Train rows: 170850
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Bukayo Saka
- Vice captain: Bryan Mbeumo
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 56.65
- Actual score: 65.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.91 | 11.98 | 19.66 | 6.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.7 | 3.80 | 9.98 | 16.23 | 6.00 | 85.2 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.94 | 14.19 | 23.36 | 1.00 | 85.9 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.1 | 3.90 | 13.24 | 21.54 | 14.00 | 84.0 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 4.06 | 12.70 | 21.37 | 8.00 | 87.9 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.6 | 4.28 | 12.60 | 21.44 | 9.00 | 84.4 | 90.0 |
| Bench 2 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.58 | 12.47 | 21.26 | 1.00 | 84.7 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 4.34 | 12.75 | 22.86 | 2.00 | 76.5 | 90.0 |
| Bench 4 | Bench | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 3.15 | 12.36 | 21.64 | 1.00 | 75.9 | 30.0 |
| Bench 3 | Bench | Danny Welbeck | FWD | 6 | 6.6 | 3.40 | 11.22 | 20.01 | 1.00 | 70.8 | 23.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.1 | 5.65 | 16.74 | 26.89 | 6.00 | 80.4 | 29.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 8.9 | 5.31 | 16.72 | 25.29 | 4.00 | 86.2 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.8 | 4.81 | 16.17 | 24.28 | 4.00 | 81.7 | 90.0 |
| XI | XI | Declan Rice | MID | 1 | 7.0 | 5.27 | 15.10 | 22.52 | 3.00 | 82.9 | 82.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.6 | 5.53 | 14.00 | 24.82 | 2.00 | 84.5 | 90.0 |

## GW15

- Train rows: 171608
- Bank: 0.10 -> 0.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Bryan Mbeumo
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 55.36
- Actual score: 77.00
- Transfer: Declan Rice -> Dominik Szoboszlai (projected gain 1.07, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.51 | 11.27 | 18.28 | 2.00 | 87.3 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.7 | 2.95 | 8.17 | 13.44 | 2.00 | 85.9 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.58 | 12.44 | 19.50 | 2.00 | 84.2 | 90.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 3.82 | 12.42 | 19.34 | 6.00 | 87.1 | 90.0 |
| Bench 4 | Bench | Trevoh Chalobah | DEF | 7 | 5.2 | 3.06 | 12.23 | 18.36 | 11.00 | 85.8 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.1 | 3.52 | 11.93 | 21.25 | 8.00 | 85.3 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.6 | 3.76 | 11.36 | 18.66 | 4.00 | 84.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.7 | 4.41 | 14.89 | 25.96 | 2.00 | 83.8 | 90.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 7 | 7.4 | 3.74 | 13.12 | 18.03 | 1.00 | 65.7 | 32.0 |
| XI | XI | Danny Welbeck | FWD | 6 | 6.6 | 4.24 | 10.72 | 19.47 | 2.00 | 69.5 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 8.9 | 6.67 | 16.58 | 26.89 | 18.00 | 86.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.1 | 4.28 | 14.42 | 22.23 | 4.00 | 82.7 | 78.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.6 | 4.54 | 14.15 | 21.54 | 8.00 | 88.5 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 14 | 8.5 | 5.12 | 13.96 | 22.42 | 8.00 | 77.6 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.7 | 4.76 | 12.84 | 19.75 | 3.00 | 81.3 | 90.0 |

## GW16

- Train rows: 172367
- Bank: 0.50 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bukayo Saka
- Chip used: triple_captain
- Predicted score: 68.89
- Actual score: 88.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (7.77) beats the best remaining Triple Captain opportunity (9.17).
- Transfer: Bryan Mbeumo -> Phil Foden (projected gain 7.58, hit 0)
- Chip used: Triple Captain on Bukayo Saka. Optimizer chose Triple Captain here because the current estimated captain upside (7.77) beats the best remaining Triple Captain opportunity (9.17).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 4.84 | 12.39 | 21.57 | 2.00 | 87.6 | 90.0 |
| Bench 1 | Bench | Matz Sels | GK | 16 | 4.7 | 2.93 | 9.33 | 14.10 | 0.00 | 72.9 | 0.0 |
| XI | XI | Marc Cucurella Saseta | DEF | 7 | 6.2 | 4.63 | 12.80 | 19.93 | 6.00 | 88.6 | 90.0 |
| Bench 2 | Bench | Maxence Lacroix | DEF | 8 | 5.1 | 3.18 | 11.60 | 20.93 | 1.00 | 87.9 | 90.0 |
| Bench 3 | Bench | Marc Guéhi | DEF | 8 | 5.1 | 3.10 | 11.46 | 20.59 | 1.00 | 86.9 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.6 | 3.37 | 11.02 | 18.72 | 1.00 | 84.1 | 90.0 |
| XI | XI | Trevoh Chalobah | DEF | 7 | 5.3 | 4.15 | 9.37 | 17.99 | 9.00 | 87.3 | 90.0 |
| XI | XI | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 5.14 | 14.36 | 26.59 | 2.00 | 85.3 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.3 | 3.19 | 9.82 | 16.49 | 2.00 | 55.2 | 80.0 |
| Bench 4 | Bench | Danny Welbeck | FWD | 6 | 6.5 | 2.41 | 9.37 | 13.64 | 1.00 | 52.7 | 8.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.0 | 6.02 | 18.05 | 26.29 | 13.00 | 85.6 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.7 | 5.58 | 17.70 | 25.07 | 11.00 | 78.9 | 90.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 10.1 | 7.77 | 17.51 | 28.06 | 11.00 | 77.2 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.6 | 4.73 | 13.56 | 22.68 | 3.00 | 85.8 | 82.0 |
| XI | XI | Antoine Semenyo | MID | 4 | 7.6 | 3.94 | 11.22 | 20.14 | 6.00 | 80.7 | 90.0 |

## GW17

- Train rows: 173127
- Bank: 0.10 -> 1.40
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Antoine Semenyo
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 67.59
- Actual score: 47.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (10.29) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Marc Cucurella Saseta -> Marcos Senesi Barón (projected gain 1.77, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (10.29) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 5.9 | 3.81 | 10.82 | 17.51 | 7.00 | 89.0 | 90.0 |
| Bench 1 | Bench Boost | Matz Sels | GK | 16 | 4.7 | 1.40 | 4.76 | 10.15 | 0.00 | 43.1 | 0.0 |
| XI | XI | Marcos Senesi Barón | DEF | 4 | 4.9 | 4.97 | 13.51 | 19.49 | 4.00 | 83.5 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 8 | 5.2 | 3.71 | 12.15 | 17.70 | 1.00 | 86.9 | 90.0 |
| XI | XI | Chris Richards | DEF | 8 | 4.6 | 4.09 | 12.12 | 19.90 | 2.00 | 84.8 | 90.0 |
| XI | XI | Maxence Lacroix | DEF | 8 | 5.1 | 3.86 | 11.77 | 18.24 | 1.00 | 84.7 | 90.0 |
| Bench 2 | Bench Boost | Trevoh Chalobah | DEF | 7 | 5.3 | 3.39 | 9.58 | 17.85 | 3.00 | 83.5 | 90.0 |
| Bench 3 | Bench Boost | Igor Thiago Nascimento Rodrigues | FWD | 5 | 6.9 | 3.26 | 11.87 | 18.93 | 2.00 | 71.8 | 90.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 7 | 7.2 | 3.75 | 10.20 | 16.14 | 6.00 | 71.1 | 90.0 |
| Bench 4 | Bench Boost | Danny Welbeck | FWD | 6 | 6.5 | 2.25 | 6.78 | 11.73 | 0.00 | 30.0 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.8 | 7.10 | 18.95 | 28.70 | 3.00 | 83.0 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.1 | 4.60 | 16.30 | 26.32 | 1.00 | 85.1 | 45.0 |
| Vice Captain | XI | Antoine Semenyo | MID | 4 | 7.6 | 5.38 | 14.66 | 24.06 | 10.00 | 85.9 | 90.0 |
| XI | XI | Dominik Szoboszlai | MID | 12 | 6.6 | 4.08 | 13.97 | 19.24 | 1.00 | 69.3 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 10.2 | 4.83 | 13.68 | 22.51 | 3.00 | 78.6 | 90.0 |