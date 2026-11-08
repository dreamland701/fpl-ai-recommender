# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2025-26 GW1-GW26
- Simulated weeks: GW35-GW38
- Total predicted points: 250.32
- Total actual points: 270.00
- Average predicted points: 62.58
- Average actual points: 67.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW26 are included before the first simulated week.
- League-average scores were not available for this run.

## GW35

- Train rows: 187673
- Bank: 100.00 -> 0.90
- Free transfers: 1 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Morgan Gibbs-White
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 57.50
- Actual score: 38.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Autosub outfielders: Konstantinos Mavropanos.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 3.85 | 11.85 | 18.82 | 6.00 | 84.1 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.05 | 8.66 | 14.14 | 8.00 | 79.8 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.1 | 5.13 | 15.50 | 23.64 | 6.00 | 91.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.56 | 14.45 | 22.94 | 1.00 | 88.9 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.1 | 3.76 | 11.47 | 17.79 | 4.00 | 79.6 | 90.0 |
| Bench 2 | Autosub In | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.70 | 11.27 | 18.52 | -1.00 | 76.6 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.8 | 3.73 | 11.18 | 18.01 | 1.00 | 78.6 | 45.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.78 | 14.75 | 23.31 | 2.00 | 85.2 | 87.0 |
| Bench 3 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 3.22 | 9.33 | 15.05 | 1.00 | 70.1 | 64.0 |
| Bench 4 | Bench | Mateus Mané | FWD | 20 | 4.3 | 2.93 | 8.19 | 12.52 | 2.00 | 65.3 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.3 | 6.31 | 19.71 | 32.44 | 5.00 | 99.1 | 90.0 |
| Vice Captain | XI | Morgan Gibbs-White | MID | 16 | 7.5 | 5.21 | 15.67 | 24.96 | 4.00 | 83.5 | 20.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 14.0 | 4.81 | 15.18 | 24.59 | 0.00 | 71.8 | 0.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.7 | 4.68 | 13.74 | 21.31 | 4.00 | 98.3 | 90.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 4.39 | 12.76 | 20.40 | 1.00 | 83.3 | 45.0 |

## GW36

- Train rows: 188505
- Bank: 0.90 -> 0.60
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Marc Guéhi
- Effective captain: Bruno Borges Fernandes
- Chip used: bench_boost
- Predicted score: 70.65
- Actual score: 68.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (14.78) beats the best remaining Bench Boost opportunity (13.58).
- Transfer: Neco Williams -> Marc Guéhi (projected gain 4.44, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (14.78) beats the best remaining Bench Boost opportunity (13.58).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.0 | 4.00 | 11.60 | 19.30 | 9.00 | 86.9 | 90.0 |
| Bench 1 | Bench Boost | Caoimhín Kelleher | GK | 5 | 4.8 | 2.70 | 8.83 | 14.57 | 3.00 | 82.2 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 5.44 | 15.40 | 24.66 | 11.00 | 95.7 | 90.0 |
| Vice Captain | XI | Marc Guéhi | DEF | 13 | 5.1 | 5.74 | 14.19 | 22.18 | 15.00 | 119.4 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.2 | 4.74 | 13.15 | 21.70 | 2.00 | 89.5 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.2 | 4.29 | 11.72 | 19.26 | 1.00 | 87.7 | 90.0 |
| Bench 2 | Bench Boost | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.27 | 9.77 | 16.60 | 4.00 | 78.6 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.8 | 4.46 | 13.16 | 22.41 | 2.00 | 86.2 | 90.0 |
| Bench 4 | Bench Boost | Valentín Castellanos | FWD | 19 | 5.5 | 2.68 | 8.43 | 13.77 | 1.00 | 59.7 | 66.0 |
| Bench 3 | Bench Boost | Mateus Mané | FWD | 20 | 4.3 | 2.81 | 8.22 | 12.43 | 2.00 | 73.0 | 66.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 7.01 | 21.08 | 34.62 | 3.00 | 103.2 | 90.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 4.80 | 13.78 | 21.54 | 0.00 | 93.9 | 0.0 |
| XI | XI | Morgan Gibbs-White | MID | 16 | 7.6 | 4.37 | 13.26 | 22.66 | 0.00 | 67.2 | 0.0 |
| XI | XI | Mohamed Salah | MID | 12 | 14.0 | 3.89 | 11.46 | 20.19 | 0.00 | 44.5 | 0.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.42 | 10.16 | 16.82 | 12.00 | 64.8 | 90.0 |

## GW37

- Train rows: 189343
- Bank: 0.60 -> 0.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 56.63
- Actual score: 65.00
- Transfer: Morgan Gibbs-White -> Antoine Semenyo (projected gain 7.84, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David Raya Martín | GK | 1 | 6.1 | 4.63 | 12.43 | 20.07 | 6.00 | 87.1 | 90.0 |
| Bench 1 | Bench | Caoimhín Kelleher | GK | 5 | 4.8 | 3.26 | 9.54 | 15.79 | 2.00 | 87.1 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.2 | 6.04 | 16.30 | 26.07 | 6.00 | 94.0 | 90.0 |
| XI | XI | Marc Guéhi | DEF | 13 | 5.1 | 4.98 | 14.98 | 24.82 | 2.00 | 116.3 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 3.84 | 11.88 | 19.77 | 14.00 | 84.2 | 90.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.2 | 4.10 | 11.81 | 18.79 | 0.00 | 82.1 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.46 | 10.28 | 16.93 | 3.00 | 80.3 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.00 | 12.31 | 20.97 | 2.00 | 78.7 | 90.0 |
| Bench 4 | Bench | Valentín Castellanos | FWD | 19 | 5.5 | 2.56 | 7.72 | 12.78 | 6.00 | 54.8 | 64.0 |
| Bench 3 | Bench | Mateus Mané | FWD | 20 | 4.2 | 2.58 | 7.35 | 11.49 | 11.00 | 59.1 | 90.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.71 | 19.81 | 32.38 | 9.00 | 103.0 | 90.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.64 | 16.87 | 27.33 | 1.00 | 107.1 | 55.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.71 | 11.34 | 19.04 | 12.00 | 81.6 | 90.0 |
| Bench 2 | Bench | Mohamed Salah | MID | 12 | 14.0 | 2.78 | 9.63 | 17.47 | 1.00 | 28.3 | 16.0 |
| XI | XI | Carlos Henrique Casimiro | MID | 14 | 5.8 | 2.79 | 8.68 | 15.09 | 1.00 | 47.9 | 80.0 |

## GW38

- Train rows: 190183
- Bank: 0.10 -> 4.10
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Gabriel dos Santos Magalhães
- Effective captain: Bruno Borges Fernandes
- Chip used: triple_captain
- Predicted score: 65.55
- Actual score: 99.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (6.70) beats the best remaining Triple Captain opportunity (0.00).
- Transfer: Mohamed Salah -> Bukayo Saka (projected gain 5.75, hit 0)
- Chip used: Triple Captain on Bruno Borges Fernandes. Optimizer chose Triple Captain here because the current estimated captain upside (6.70) beats the best remaining Triple Captain opportunity (0.00).
- Autosub: Caoimhín Kelleher replaced David Raya Martín.
- Autosub outfielders: Mateus Mané, Valentín Castellanos.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | David Raya Martín | GK | 1 | 6.1 | 4.25 | 12.32 | 19.99 | 0.00 | 85.0 | 0.0 |
| Bench 1 | Autosub In | Caoimhín Kelleher | GK | 5 | 4.8 | 2.89 | 9.01 | 15.01 | 6.00 | 86.0 | 90.0 |
| Vice Captain | XI | Gabriel dos Santos Magalhães | DEF | 1 | 7.3 | 5.42 | 15.40 | 24.88 | 1.00 | 90.9 | 45.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.1 | 4.90 | 14.22 | 22.99 | 2.00 | 96.2 | 90.0 |
| XI | Bench | Marc Guéhi | DEF | 13 | 5.1 | 4.75 | 13.69 | 22.09 | 0.00 | 100.3 | 0.0 |
| XI | XI | Pedro Porro Sauceda | DEF | 18 | 5.2 | 3.93 | 11.31 | 18.28 | 10.00 | 79.4 | 90.0 |
| XI | XI | Konstantinos Mavropanos | DEF | 19 | 4.5 | 3.89 | 10.88 | 17.48 | 8.00 | 85.2 | 90.0 |
| XI | XI | Jarrod Bowen | FWD | 19 | 7.7 | 4.20 | 11.80 | 19.83 | 12.00 | 80.6 | 90.0 |
| Bench 2 | Autosub In | Mateus Mané | FWD | 20 | 4.2 | 3.33 | 9.09 | 14.36 | 2.00 | 72.4 | 90.0 |
| Bench 3 | Autosub In | Valentín Castellanos | FWD | 19 | 5.5 | 3.20 | 8.56 | 13.89 | 8.00 | 57.6 | 87.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 10.4 | 6.70 | 20.17 | 33.40 | 14.00 | 103.2 | 90.0 |
| XI | Bench | Bukayo Saka | MID | 1 | 10.0 | 5.09 | 14.81 | 23.06 | 0.00 | 74.3 | 0.0 |
| XI | XI | Antoine Semenyo | MID | 13 | 8.1 | 5.03 | 14.58 | 23.71 | 6.00 | 82.0 | 57.0 |
| XI | XI | Elliot Anderson | MID | 16 | 5.6 | 3.98 | 12.02 | 19.92 | 2.00 | 90.6 | 64.0 |
| Bench 4 | Bench | Carlos Henrique Casimiro | MID | 14 | 5.9 | 2.85 | 8.40 | 15.10 | 0.00 | 59.1 | 0.0 |