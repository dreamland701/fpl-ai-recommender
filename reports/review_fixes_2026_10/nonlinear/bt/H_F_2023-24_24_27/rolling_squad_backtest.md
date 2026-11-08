# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2023-24 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 256.84
- Total actual points: 254.00
- Average predicted points: 64.21
- Average actual points: 63.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 121022
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Kevin De Bruyne
- Vice captain: Bukayo Saka
- Effective captain: Kevin De Bruyne
- Chip used: none
- Predicted score: 58.76
- Actual score: 47.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | André Onana | GK | 14 | 4.8 | 2.58 | 10.60 | 19.11 | 4.00 | 89.4 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.6 | 3.51 | 10.54 | 18.42 | 2.00 | 88.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.03 | 13.78 | 19.45 | 4.00 | 83.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 11 | 8.6 | 5.25 | 12.81 | 20.13 | 4.00 | 61.3 | 45.0 |
| XI | XI | Destiny Udogie | DEF | 18 | 4.9 | 4.22 | 12.02 | 19.80 | 2.00 | 84.4 | 79.0 |
| Bench 4 | Bench | Pedro Porro | DEF | 18 | 5.9 | 2.96 | 10.95 | 19.88 | 2.00 | 72.4 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 4.63 | 10.70 | 17.86 | 1.00 | 77.4 | 86.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.8 | 4.01 | 13.86 | 20.67 | 2.00 | 68.8 | 76.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 4.03 | 12.45 | 23.25 | 4.00 | 72.6 | 90.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.37 | 10.93 | 20.49 | 0.00 | 58.8 | 0.0 |
| Captain | Captain | Kevin De Bruyne | MID | 13 | 10.8 | 7.03 | 18.98 | 26.44 | 4.00 | 77.6 | 33.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.0 | 5.40 | 15.88 | 25.19 | 15.00 | 76.2 | 66.0 |
| Bench 2 | Bench | Andreas Hoelgebaum Pereira | MID | 10 | 5.3 | 3.97 | 13.51 | 19.69 | 2.00 | 72.0 | 84.0 |
| XI | XI | Phil Foden | MID | 13 | 8.0 | 4.98 | 13.12 | 23.52 | 3.00 | 77.2 | 90.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 4.66 | 12.90 | 22.96 | 2.00 | 85.4 | 90.0 |

## GW25

- Train rows: 121836
- Bank: 0.30 -> 2.50
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Kevin De Bruyne
- Effective captain: Phil Foden
- Chip used: triple_captain
- Predicted score: 88.79
- Actual score: 70.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (15.19) beats the best remaining Triple Captain opportunity (6.71).
- Chip advisory: triple_captain (0.65): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Trent Alexander-Arnold -> Virgil van Dijk (projected gain 8.10, hit 0)
- Chip used: Triple Captain on Phil Foden. Optimizer chose Triple Captain here because the current estimated captain upside (15.19) beats the best remaining Triple Captain opportunity (6.71).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.75 | 10.94 | 20.19 | 3.00 | 88.7 | 90.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.6 | 2.36 | 8.51 | 15.42 | 2.00 | 81.9 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 8.52 | 15.11 | 26.23 | 10.00 | 164.1 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 5.05 | 12.31 | 21.38 | 1.00 | 79.0 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 6.29 | 12.20 | 19.71 | 1.00 | 158.0 | 154.0 |
| Bench 2 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 2.91 | 8.30 | 13.44 | 0.00 | 49.5 | 0.0 |
| Bench 3 | Bench | Pedro Porro | DEF | 18 | 5.8 | 2.85 | 7.86 | 11.66 | 0.00 | 60.8 | 0.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 6.30 | 12.38 | 20.46 | 7.00 | 103.1 | 151.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 6.9 | 3.58 | 12.36 | 24.35 | 12.00 | 72.1 | 90.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 1.57 | 5.49 | 8.97 | 0.00 | 9.4 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 10.94 | 20.67 | 25.31 | 5.00 | 158.4 | 180.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 10.8 | 10.48 | 19.70 | 30.50 | 2.00 | 130.5 | 90.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 5.23 | 13.61 | 24.40 | 15.00 | 58.7 | 68.0 |
| XI | XI | Richarlison de Andrade | MID | 18 | 7.2 | 3.10 | 12.15 | 19.24 | 2.00 | 69.7 | 70.0 |
| XI | XI | Andreas Hoelgebaum Pereira | MID | 10 | 5.3 | 3.67 | 10.28 | 15.03 | 2.00 | 59.2 | 74.0 |

## GW26

- Train rows: 122659
- Bank: 2.50 -> 2.00
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Jarrod Bowen
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 44.70
- Actual score: 59.00
- Transfer: Richarlison de Andrade -> Jarrod Bowen (projected gain 12.02, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | André Onana | GK | 14 | 4.8 | 3.97 | 10.38 | 19.05 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Norberto Murara Neto | GK | 3 | 4.6 | 2.90 | 9.96 | 14.78 | 3.00 | 88.2 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 11 | 6.4 | 0.06 | 9.53 | 15.42 | 0.00 | 3.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 3.17 | 8.69 | 19.89 | 0.00 | 89.0 | 90.0 |
| Bench 4 | Bench | Alfie Doughty | DEF | 12 | 4.6 | 0.00 | 6.57 | 17.07 | 0.00 | 2.1 | 0.0 |
| Bench 3 | Bench | Destiny Udogie | DEF | 18 | 4.9 | 0.00 | 4.69 | 8.32 | 0.00 | 1.5 | 0.0 |
| XI | Bench | Pedro Porro | DEF | 18 | 5.8 | 0.14 | 3.65 | 9.27 | 0.00 | 3.4 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 3.63 | 13.78 | 18.88 | 2.00 | 88.5 | 90.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.7 | 4.50 | 11.74 | 22.36 | 1.00 | 68.6 | 15.0 |
| Bench 2 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 0.87 | 3.91 | 7.38 | 0.00 | 11.0 | 0.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.32 | 16.36 | 26.76 | 11.00 | 82.4 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.8 | 4.88 | 15.97 | 22.25 | 0.00 | 58.5 | 6.0 |
| XI | XI | Bukayo Saka | MID | 1 | 9.0 | 3.96 | 15.48 | 26.28 | 10.00 | 73.6 | 75.0 |
| Vice Captain | XI | Jarrod Bowen | MID | 19 | 7.7 | 5.36 | 14.87 | 21.59 | 20.00 | 89.3 | 90.0 |
| XI | XI | Andreas Hoelgebaum Pereira | MID | 10 | 5.3 | 2.39 | 9.61 | 19.05 | 2.00 | 70.4 | 67.0 |

## GW27

- Train rows: 123487
- Bank: 2.00 -> 1.70
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Bukayo Saka
- Effective captain: Phil Foden
- Chip used: bench_boost
- Predicted score: 64.59
- Actual score: 78.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (7.27) beats the best remaining Bench Boost opportunity (0.00).
- Transfer: Andreas Hoelgebaum Pereira -> Leon Bailey (projected gain 2.57, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (7.27) beats the best remaining Bench Boost opportunity (0.00).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | André Onana | GK | 14 | 4.8 | 2.46 | 11.36 | 19.58 | 2.00 | 85.8 | 90.0 |
| XI | XI | Norberto Murara Neto | GK | 3 | 4.6 | 4.29 | 10.39 | 17.40 | 8.00 | 87.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 6.8 | 4.65 | 10.70 | 19.78 | 1.00 | 83.7 | 51.0 |
| XI | XI | Virgil van Dijk | DEF | 11 | 6.4 | 4.03 | 10.67 | 21.58 | 6.00 | 81.0 | 90.0 |
| XI | XI | Alfie Doughty | DEF | 12 | 4.6 | 3.43 | 9.55 | 16.69 | 5.00 | 78.0 | 90.0 |
| Bench 2 | Bench Boost | Pedro Porro | DEF | 18 | 5.7 | 2.08 | 5.81 | 9.27 | 0.00 | 40.7 | 0.0 |
| Bench 3 | Bench Boost | Destiny Udogie | DEF | 18 | 4.9 | 2.04 | 5.49 | 12.81 | 2.00 | 38.9 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 7.0 | 5.04 | 13.99 | 22.88 | 2.00 | 85.2 | 88.0 |
| XI | XI | Julián Álvarez | FWD | 13 | 6.6 | 3.79 | 12.57 | 19.52 | 4.00 | 52.6 | 31.0 |
| Bench 4 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.3 | 0.70 | 3.58 | 7.88 | 0.00 | 22.0 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 9.1 | 5.94 | 20.43 | 28.70 | 7.00 | 71.0 | 45.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.0 | 6.37 | 14.78 | 24.16 | 15.00 | 86.5 | 90.0 |
| XI | XI | Leon Bailey | MID | 2 | 5.6 | 4.93 | 13.13 | 22.23 | 4.00 | 76.6 | 78.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 10.7 | 4.25 | 12.84 | 25.74 | 2.00 | 29.2 | 90.0 |
| XI | XI | Jarrod Bowen | MID | 19 | 7.7 | 4.22 | 10.88 | 19.45 | 5.00 | 86.6 | 90.0 |