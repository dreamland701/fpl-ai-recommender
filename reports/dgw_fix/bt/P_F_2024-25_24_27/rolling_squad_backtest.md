# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2024-25 GW1-GW23
- Simulated weeks: GW24-GW27
- Total predicted points: 308.21
- Total actual points: 262.00
- Average predicted points: 77.05
- Average actual points: 65.50
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW23 are included before the first simulated week.
- League-average scores were not available for this run.

## GW24

- Train rows: 149404
- Bank: 100.00 -> 0.30
- Free transfers: 1 -> 2
- Captain: Trent Alexander-Arnold
- Vice captain: Iliman Ndiaye
- Effective captain: Trent Alexander-Arnold
- Chip used: triple_captain
- Predicted score: 93.32
- Actual score: 75.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (13.96) beats the best remaining Triple Captain opportunity (14.87).
- Chip advisory: bench_boost (0.58): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Chip advisory: triple_captain (0.72): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.
- Chip used: Triple Captain on Trent Alexander-Arnold. Optimizer chose Triple Captain here because the current estimated captain upside (13.96) beats the best remaining Triple Captain opportunity (14.87).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 7.50 | 14.33 | 20.83 | 10.00 | 180.0 | 180.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.92 | 11.24 | 16.56 | 2.00 | 83.3 | 90.0 |
| Captain | Captain | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.13 | 25.70 | 33.93 | 7.00 | 180.0 | 98.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 7.41 | 18.38 | 24.87 | 6.00 | 157.7 | 180.0 |
| XI | XI | Andrew Robertson | DEF | 12 | 5.9 | 5.74 | 14.18 | 19.21 | 8.00 | 128.7 | 158.0 |
| XI | XI | Vitalii Mykolenko | DEF | 8 | 4.4 | 6.38 | 12.07 | 17.56 | 7.00 | 176.1 | 177.0 |
| Bench 3 | Bench | Antonee Robinson | DEF | 9 | 5.1 | 3.41 | 10.70 | 17.81 | 4.00 | 82.5 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.83 | 20.08 | 33.46 | 2.00 | 90.0 | 90.0 |
| Vice Captain | XI | Iliman Ndiaye | FWD | 8 | 5.5 | 7.58 | 14.09 | 20.37 | 9.00 | 172.9 | 114.0 |
| Bench 4 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.46 | 8.15 | 13.50 | 1.00 | 60.8 | 45.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.3 | 7.34 | 19.91 | 33.62 | 6.00 | 90.0 | 89.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 6.06 | 16.51 | 26.85 | 2.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 4.03 | 14.08 | 24.15 | 2.00 | 83.2 | 71.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 4.06 | 12.71 | 20.06 | 2.00 | 89.7 | 90.0 |
| Bench 2 | Bench | Amad Diallo | MID | 14 | 5.6 | 4.01 | 11.85 | 19.36 | 2.00 | 83.8 | 90.0 |

## GW25

- Train rows: 150166
- Bank: 0.30 -> 0.30
- Free transfers: 2 -> 2
- Captain: Trent Alexander-Arnold
- Vice captain: Virgil van Dijk
- Effective captain: Trent Alexander-Arnold
- Chip used: bench_boost
- Predicted score: 97.90
- Actual score: 62.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (17.62) beats the best remaining Bench Boost opportunity (14.85).
- Transfer: Amad Diallo -> Morgan Rogers (projected gain 5.29, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (17.62) beats the best remaining Bench Boost opportunity (14.85).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.0 | 5.98 | 11.76 | 14.26 | 4.00 | 171.2 | 180.0 |
| Bench 1 | Bench Boost | Jordan Pickford | GK | 8 | 5.1 | 3.85 | 11.28 | 17.74 | 3.00 | 90.0 | 90.0 |
| Captain | Captain | Trent Alexander-Arnold | DEF | 12 | 7.4 | 10.35 | 20.01 | 24.76 | 13.00 | 179.5 | 128.0 |
| Vice Captain | XI | Virgil van Dijk | DEF | 12 | 6.4 | 10.21 | 18.89 | 22.62 | 2.00 | 180.0 | 180.0 |
| XI | XI | Andrew Robertson | DEF | 12 | 5.9 | 8.18 | 15.25 | 18.38 | 3.00 | 180.0 | 180.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.72 | 11.15 | 18.41 | 2.00 | 86.1 | 90.0 |
| Bench 2 | Bench Boost | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.58 | 10.45 | 16.29 | 2.00 | 90.0 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 5.81 | 18.11 | 24.47 | 2.00 | 88.8 | 89.0 |
| Bench 3 | Bench Boost | Iliman Ndiaye | FWD | 8 | 5.5 | 2.68 | 8.46 | 13.64 | 0.00 | 66.6 | 0.0 |
| Bench 4 | Bench Boost | João Pedro Junqueira de Jesus | FWD | 5 | 5.5 | 2.49 | 7.39 | 12.36 | 1.00 | 52.2 | 17.0 |
| XI | XI | Cole Palmer | MID | 6 | 11.2 | 6.74 | 19.80 | 32.97 | 2.00 | 90.0 | 90.0 |
| XI | XI | Morgan Rogers | MID | 2 | 5.6 | 8.59 | 15.73 | 18.49 | 4.00 | 173.8 | 180.0 |
| XI | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.52 | 15.32 | 25.13 | 3.00 | 82.9 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.8 | 5.78 | 14.58 | 22.54 | 5.00 | 85.5 | 76.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 4.07 | 13.63 | 23.21 | 3.00 | 68.4 | 75.0 |

## GW26

- Train rows: 150945
- Bank: 0.30 -> 0.40
- Free transfers: 2 -> 2
- Captain: Bryan Mbeumo
- Vice captain: Cole Palmer
- Effective captain: Bryan Mbeumo
- Chip used: none
- Predicted score: 59.42
- Actual score: 71.00
- Transfer: Morgan Rogers -> Youri Tielemans (projected gain 1.27, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Emiliano Martínez Romero | GK | 2 | 5.0 | 3.78 | 10.69 | 13.39 | 3.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Jordan Pickford | GK | 8 | 5.1 | 3.70 | 10.40 | 17.07 | 1.00 | 90.0 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.77 | 17.25 | 22.67 | 6.00 | 90.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.71 | 14.05 | 18.00 | 6.00 | 90.0 | 90.0 |
| XI | XI | Andrew Robertson | DEF | 12 | 5.9 | 4.40 | 12.74 | 16.30 | 6.00 | 90.0 | 73.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.70 | 11.25 | 18.20 | 1.00 | 86.6 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 3.18 | 9.10 | 14.86 | 1.00 | 87.2 | 90.0 |
| XI | XI | Alexander Isak | FWD | 15 | 9.5 | 6.12 | 17.95 | 23.97 | 13.00 | 90.0 | 86.0 |
| Bench 3 | Bench | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 2.61 | 7.18 | 12.11 | 12.00 | 40.8 | 90.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.5 | 1.69 | 5.52 | 10.23 | 0.00 | 32.0 | 0.0 |
| Vice Captain | XI | Cole Palmer | MID | 6 | 11.1 | 6.13 | 18.65 | 31.21 | 2.00 | 90.0 | 90.0 |
| Captain | Captain | Bryan Mbeumo | MID | 4 | 7.9 | 6.16 | 16.40 | 26.20 | 14.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 3.85 | 13.16 | 22.14 | 2.00 | 68.7 | 90.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 4.24 | 12.43 | 19.16 | 2.00 | 66.3 | 72.0 |
| XI | XI | Youri Tielemans | MID | 2 | 5.5 | 4.40 | 12.27 | 15.62 | 2.00 | 90.0 | 90.0 |

## GW27

- Train rows: 151728
- Bank: 0.40 -> 0.00
- Free transfers: 2 -> 2
- Captain: Cole Palmer
- Vice captain: Bryan Mbeumo
- Effective captain: Cole Palmer
- Chip used: none
- Predicted score: 57.57
- Actual score: 54.00
- Transfer: Andrew Robertson -> Gabriel dos Santos Magalhães (projected gain 3.63, hit 0)
- Autosub: Youri Tielemans replaced Alexander Isak.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Jordan Pickford | GK | 8 | 5.1 | 3.24 | 9.83 | 16.10 | 2.00 | 90.0 | 90.0 |
| Bench 1 | Bench | Emiliano Martínez Romero | GK | 2 | 5.0 | 2.93 | 5.85 | 11.52 | 1.00 | 90.0 | 45.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.4 | 5.92 | 11.08 | 22.14 | 6.00 | 90.0 | 76.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | 1 | 6.3 | 3.62 | 10.87 | 17.89 | 7.00 | 81.6 | 90.0 |
| XI | XI | Antonee Robinson | DEF | 9 | 5.1 | 3.41 | 10.19 | 16.67 | 0.00 | 83.3 | 18.0 |
| Bench 3 | Bench | Vitalii Mykolenko | DEF | 8 | 4.4 | 2.82 | 8.56 | 13.95 | 6.00 | 85.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.34 | 8.48 | 16.70 | 7.00 | 90.0 | 90.0 |
| XI | Bench | Alexander Isak | FWD | 15 | 9.5 | 5.53 | 11.82 | 23.56 | 0.00 | 90.0 | 0.0 |
| XI | XI | João Pedro Junqueira de Jesus | FWD | 5 | 5.4 | 3.24 | 9.30 | 15.25 | 8.00 | 63.1 | 71.0 |
| Bench 4 | Bench | Iliman Ndiaye | FWD | 8 | 5.4 | 0.94 | 4.70 | 8.85 | 0.00 | 22.4 | 0.0 |
| Captain | Captain | Cole Palmer | MID | 6 | 11.1 | 7.20 | 19.33 | 31.87 | 3.00 | 90.0 | 90.0 |
| Vice Captain | XI | Bryan Mbeumo | MID | 4 | 7.9 | 5.99 | 17.52 | 28.04 | 5.00 | 90.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 9.3 | 4.04 | 12.77 | 21.33 | 1.00 | 70.0 | 16.0 |
| XI | XI | Justin Kluivert | MID | 3 | 5.9 | 3.84 | 11.51 | 18.09 | 10.00 | 64.1 | 90.0 |
| Bench 2 | Autosub In | Youri Tielemans | MID | 2 | 5.5 | 3.24 | 6.66 | 13.23 | 2.00 | 90.0 | 90.0 |