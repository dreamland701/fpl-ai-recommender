# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26
- In-season warm start: 2022-23 GW1-GW11
- Simulated weeks: GW12-GW30
- Total predicted points: 1286.35
- Total actual points: 1166.00
- Average predicted points: 67.70
- Average actual points: 61.37
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW11 are included before the first simulated week.
- League-average scores were not available for this run.

## GW12

- Train rows: 84420
- Bank: 100.00 -> 0.50
- Free transfers: 1 -> 2
- Captain: Kieran Trippier
- Vice captain: Mohamed Salah
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 52.30
- Actual score: 56.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.4 | 4.03 | 10.48 | 17.02 | 15.00 | 90.8 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 3.76 | 9.67 | 15.06 | 9.00 | 86.4 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.6 | 5.86 | 16.01 | 25.64 | 9.00 | 95.0 | 90.0 |
| XI | Bench | João Cancelo | DEF | -1 | 7.3 | 3.71 | 12.99 | 21.41 | 0.00 | 51.0 | 0.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.63 | 10.51 | 16.83 | 1.00 | 69.4 | 88.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 3.70 | 9.67 | 15.61 | 7.00 | 81.2 | 90.0 |
| Bench 2 | Bench | Fabian Schär | DEF | -1 | 4.8 | 3.58 | 9.20 | 14.46 | 5.00 | 80.4 | 90.0 |
| XI | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 4.76 | 15.90 | 26.03 | 0.00 | 62.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 5.7 | 3.82 | 9.61 | 15.38 | 2.00 | 80.0 | 90.0 |
| Bench 4 | Bench | Patson Daka | FWD | -1 | 5.7 | 3.04 | 7.69 | 11.96 | 1.00 | 55.4 | 26.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 12.7 | 4.92 | 13.59 | 22.72 | 3.00 | 73.5 | 90.0 |
| XI | Bench | Gabriel Martinelli Silva | MID | -1 | 6.6 | 3.62 | 12.73 | 21.08 | 0.00 | 52.1 | 0.0 |
| XI | Bench | James Maddison | MID | -1 | 8.3 | 4.47 | 12.58 | 20.39 | 0.00 | 77.1 | 0.0 |
| Bench 3 | Bench | Phil Foden | MID | -1 | 8.2 | 3.15 | 12.32 | 21.36 | 0.00 | 42.3 | 0.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.2 | 3.91 | 10.32 | 16.53 | 10.00 | 79.3 | 72.0 |

## GW13

- Train rows: 85065
- Bank: 0.50 -> 1.80
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Fernando de Jesus
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 54.76
- Actual score: 37.00
- Transfer: James Maddison -> Leandro Trossard (projected gain 2.22, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.4 | 4.16 | 11.47 | 18.34 | 4.00 | 95.1 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 3.79 | 10.04 | 15.32 | 8.00 | 87.8 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.7 | 5.94 | 17.27 | 27.04 | 2.00 | 103.1 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.3 | 4.37 | 12.29 | 19.44 | 2.00 | 63.2 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.80 | 10.68 | 16.63 | 1.00 | 71.7 | 29.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.4 | 3.72 | 10.46 | 16.31 | 2.00 | 82.8 | 90.0 |
| Bench 3 | Bench | Fabian Schär | DEF | -1 | 4.8 | 3.45 | 10.18 | 15.50 | 2.00 | 81.3 | 90.0 |
| Vice Captain | XI | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 5.61 | 15.64 | 24.11 | 2.00 | 72.8 | 90.0 |
| Bench 2 | Bench | Dominic Solanke | FWD | -1 | 5.8 | 3.60 | 10.34 | 16.39 | 1.00 | 77.5 | 44.0 |
| Bench 4 | Bench | Patson Daka | FWD | -1 | 5.7 | 2.81 | 7.52 | 11.71 | 2.00 | 48.6 | 60.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.7 | 5.40 | 16.40 | 25.59 | 2.00 | 70.6 | 90.0 |
| XI | XI | Leandro Trossard | MID | -1 | 6.9 | 3.98 | 12.49 | 18.82 | 7.00 | 68.2 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 4.30 | 12.03 | 18.90 | 2.00 | 62.0 | 70.0 |
| XI | XI | Phil Foden | MID | -1 | 8.2 | 3.79 | 11.45 | 18.24 | 1.00 | 55.2 | 28.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.2 | 3.75 | 11.06 | 16.97 | 10.00 | 77.8 | 90.0 |

## GW14

- Train rows: 85713
- Bank: 1.80 -> 0.70
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Fernando de Jesus
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 57.88
- Actual score: 81.00
- Transfer: Patson Daka -> Aleksandar Mitrović (projected gain 3.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Alisson Ramses Becker | GK | -1 | 5.4 | 3.71 | 10.91 | 17.80 | 2.00 | 88.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 3.39 | 10.27 | 16.08 | 3.00 | 90.2 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.7 | 6.10 | 17.15 | 27.15 | 11.00 | 104.7 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.3 | 4.85 | 14.43 | 22.51 | 6.00 | 82.4 | 90.0 |
| XI | XI | Fabian Schär | DEF | -1 | 4.9 | 3.81 | 10.34 | 16.50 | 6.00 | 84.3 | 82.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | -1 | 6.4 | 3.53 | 9.76 | 15.58 | 1.00 | 78.8 | 90.0 |
| Bench 3 | Bench | Ivan Perišić | DEF | -1 | 5.5 | 3.37 | 9.59 | 15.50 | 4.00 | 60.1 | 27.0 |
| Vice Captain | XI | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 5.70 | 15.74 | 25.55 | 9.00 | 81.1 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 6.8 | 5.17 | 13.53 | 21.47 | 1.00 | 83.9 | 90.0 |
| Bench 4 | Bench | Dominic Solanke | FWD | -1 | 5.8 | 3.30 | 9.48 | 15.57 | 2.00 | 64.4 | 88.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.35 | 14.83 | 24.12 | 7.00 | 73.9 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.7 | 4.59 | 13.10 | 20.50 | 8.00 | 67.9 | 62.0 |
| XI | XI | Phil Foden | MID | -1 | 8.4 | 3.78 | 12.72 | 20.32 | 1.00 | 46.8 | 13.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.3 | 4.41 | 12.16 | 19.00 | 12.00 | 81.2 | 85.0 |
| XI | XI | Leandro Trossard | MID | -1 | 6.8 | 4.31 | 11.99 | 19.39 | 7.00 | 69.0 | 86.0 |

## GW15

- Train rows: 86369
- Bank: 0.70 -> 0.80
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Fernando de Jesus
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 59.23
- Actual score: 67.00
- Transfer: Alisson Ramses Becker -> Nick Pope (projected gain 0.05, hit 0)
- Autosub outfielders: Dominic Solanke.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | -1 | 5.3 | 3.69 | 9.78 | 15.02 | 3.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 3.55 | 9.75 | 15.41 | 6.00 | 86.1 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.8 | 6.52 | 17.84 | 27.88 | 12.00 | 109.5 | 79.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.4 | 5.62 | 15.18 | 23.30 | -2.00 | 86.1 | 25.0 |
| XI | XI | Fabian Schär | DEF | -1 | 4.9 | 3.85 | 10.25 | 15.87 | 2.00 | 81.1 | 90.0 |
| Bench 3 | Bench | Ivan Perišić | DEF | -1 | 5.5 | 3.20 | 9.47 | 15.14 | 1.00 | 58.3 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | -1 | 6.5 | 3.15 | 9.19 | 14.22 | 2.00 | 80.0 | 90.0 |
| Vice Captain | XI | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 5.91 | 16.93 | 27.01 | 2.00 | 89.6 | 90.0 |
| XI | Bench | Aleksandar Mitrović | FWD | -1 | 6.9 | 4.45 | 13.06 | 20.50 | 0.00 | 75.1 | 0.0 |
| Bench 2 | Autosub In | Dominic Solanke | FWD | -1 | 5.8 | 3.42 | 9.47 | 14.64 | 6.00 | 70.7 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.24 | 15.24 | 24.25 | 15.00 | 78.4 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.5 | 4.59 | 13.29 | 21.55 | 8.00 | 74.0 | 80.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 4.46 | 13.05 | 20.40 | 3.00 | 71.0 | 90.0 |
| XI | XI | Leandro Trossard | MID | -1 | 6.8 | 4.69 | 12.21 | 18.59 | 5.00 | 73.1 | 81.0 |
| XI | XI | Phil Foden | MID | -1 | 8.5 | 3.70 | 10.87 | 17.44 | 1.00 | 42.4 | 26.0 |

## GW16

- Train rows: 87030
- Bank: 0.80 -> 1.00
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Fernando de Jesus
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 60.68
- Actual score: 56.00
- Transfer: Phil Foden -> James Maddison (projected gain 2.37, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.1 | 3.83 | 10.36 | 16.11 | 11.00 | 90.9 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 3.35 | 9.17 | 14.55 | 5.00 | 79.2 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.9 | 6.37 | 17.66 | 27.95 | 7.00 | 108.7 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.4 | 4.55 | 12.65 | 20.30 | 1.00 | 64.7 | 85.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 4.05 | 10.33 | 16.12 | 1.00 | 70.0 | 90.0 |
| Bench 4 | Bench | Fabian Schär | DEF | -1 | 4.9 | 3.44 | 9.30 | 14.88 | 7.00 | 81.4 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | -1 | 6.5 | 3.50 | 9.11 | 14.25 | 2.00 | 78.3 | 90.0 |
| Vice Captain | XI | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 6.30 | 17.32 | 27.74 | 2.00 | 91.4 | 90.0 |
| Bench 2 | Bench | Aleksandar Mitrović | FWD | -1 | 6.9 | 3.51 | 9.96 | 16.27 | 0.00 | 39.0 | 0.0 |
| XI | XI | Dominic Solanke | FWD | -1 | 5.7 | 3.75 | 9.95 | 15.36 | 5.00 | 78.0 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 6.19 | 16.47 | 26.11 | 2.00 | 86.1 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.7 | 4.91 | 14.34 | 23.25 | 6.00 | 76.5 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 5.12 | 13.64 | 21.53 | 6.00 | 80.7 | 90.0 |
| XI | XI | Leandro Trossard | MID | -1 | 7.0 | 4.67 | 12.68 | 19.90 | 2.00 | 65.5 | 90.0 |
| XI | XI | James Maddison | MID | -1 | 8.2 | 4.57 | 11.98 | 19.14 | 6.00 | 81.3 | 24.0 |

## GW17

- Train rows: 87697
- Bank: 1.00 -> 0.60
- Free transfers: 2 -> 2
- Captain: Gabriel Fernando de Jesus
- Vice captain: Kieran Trippier
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 61.46
- Actual score: 70.00
- Transfer: Fabian Schär -> William Saliba (projected gain 0.70, hit 0)
- Autosub outfielders: Dominic Solanke, Virgil van Dijk.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.1 | 4.08 | 11.02 | 17.21 | 1.00 | 93.7 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 3.47 | 9.64 | 15.25 | 6.00 | 82.4 | 90.0 |
| Vice Captain | Captain | Kieran Trippier | DEF | -1 | 5.9 | 6.09 | 17.45 | 27.95 | 12.00 | 109.2 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.4 | 4.98 | 13.71 | 22.10 | 1.00 | 74.8 | 22.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.17 | 11.00 | 17.43 | 2.00 | 82.1 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.76 | 10.33 | 16.23 | 1.00 | 73.9 | 90.0 |
| Bench 3 | Autosub In | Virgil van Dijk | DEF | -1 | 6.5 | 3.54 | 9.69 | 15.35 | 9.00 | 82.5 | 90.0 |
| Captain | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 6.47 | 17.61 | 28.01 | 0.00 | 92.2 | 0.0 |
| Bench 2 | Autosub In | Dominic Solanke | FWD | -1 | 5.8 | 3.57 | 10.19 | 16.06 | 2.00 | 77.8 | 90.0 |
| Bench 4 | Bench | Aleksandar Mitrović | FWD | -1 | 6.8 | 2.67 | 8.14 | 14.48 | 15.00 | 24.6 | 84.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.71 | 16.15 | 25.87 | 12.00 | 82.7 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.8 | 5.55 | 15.68 | 24.76 | 8.00 | 91.4 | 82.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 5.41 | 14.33 | 22.72 | 8.00 | 86.1 | 87.0 |
| XI | XI | Leandro Trossard | MID | -1 | 7.1 | 4.93 | 13.19 | 20.32 | 2.00 | 78.4 | 82.0 |
| XI | Bench | James Maddison | MID | -1 | 8.2 | 3.83 | 10.78 | 17.69 | 0.00 | 59.3 | 0.0 |

## GW18

- Train rows: 88372
- Bank: 0.60 -> 2.10
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Miguel Almirón Rejala
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 54.13
- Actual score: 47.00
- Transfer: James Maddison -> Marcus Rashford (projected gain 2.53, hit 0)
- Autosub outfielders: Dominic Solanke, Ivan Perišić.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 2.56 | 12.47 | 21.20 | 3.00 | 70.4 | 90.0 |
| XI | XI | Nick Pope | GK | -1 | 5.3 | 3.55 | 11.26 | 20.23 | 6.00 | 66.8 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.9 | 6.43 | 18.75 | 33.84 | 8.00 | 102.1 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | -1 | 6.5 | 3.58 | 12.05 | 20.32 | 2.00 | 79.3 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 3.29 | 11.69 | 20.71 | 1.00 | 60.0 | 90.0 |
| Bench 3 | Autosub In | Ivan Perišić | DEF | -1 | 5.5 | 3.10 | 11.67 | 21.62 | 1.00 | 63.1 | 87.0 |
| XI | Bench | João Cancelo | DEF | -1 | 7.4 | 3.79 | 11.46 | 22.48 | 0.00 | 36.2 | 0.0 |
| XI | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 3.40 | 11.87 | 24.27 | 0.00 | 23.2 | 0.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 6.8 | 3.96 | 11.07 | 21.13 | 0.00 | 31.8 | 90.0 |
| Bench 2 | Autosub In | Dominic Solanke | FWD | -1 | 5.8 | 3.28 | 10.95 | 19.11 | 1.00 | 56.2 | 90.0 |
| Vice Captain | XI | Miguel Almirón Rejala | MID | -1 | 5.8 | 5.66 | 16.82 | 29.96 | 3.00 | 66.2 | 83.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.43 | 16.80 | 29.41 | 2.00 | 50.4 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 4.68 | 15.63 | 27.24 | 10.00 | 68.4 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.7 | 3.91 | 13.62 | 24.81 | 5.00 | 44.7 | 45.0 |
| Bench 4 | Bench | Leandro Trossard | MID | -1 | 7.1 | 2.89 | 12.47 | 23.56 | 1.00 | 52.6 | 59.0 |

## GW19

- Train rows: 89050
- Bank: 2.10 -> 0.40
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Gabriel Martinelli Silva
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 62.17
- Actual score: 56.00
- Transfer: Dominic Solanke -> Ivan Toney (projected gain 1.51, hit 0)
- Autosub outfielders: Virgil van Dijk, João Cancelo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.1 | 4.38 | 13.37 | 22.09 | 2.00 | 96.6 | 90.0 |
| Bench 1 | Bench | Nick Pope | GK | -1 | 5.3 | 3.74 | 13.31 | 20.28 | 10.00 | 94.8 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 5.9 | 6.55 | 22.34 | 34.99 | 8.00 | 121.3 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 4.13 | 13.89 | 22.31 | 10.00 | 88.0 | 85.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.17 | 13.57 | 20.66 | 7.00 | 90.2 | 90.0 |
| Bench 2 | Autosub In | Virgil van Dijk | DEF | -1 | 6.5 | 3.78 | 12.77 | 20.50 | 0.00 | 92.8 | 45.0 |
| Bench 3 | Autosub In | João Cancelo | DEF | -1 | 7.4 | 3.40 | 11.57 | 18.29 | 1.00 | 49.9 | 45.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 7.0 | 5.29 | 14.49 | 21.24 | 5.00 | 94.8 | 90.0 |
| XI | Bench | Ivan Toney | FWD | -1 | 7.5 | 4.67 | 14.22 | 22.04 | 0.00 | 87.4 | 0.0 |
| Bench 4 | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 3.33 | 10.99 | 17.97 | 0.00 | 41.7 | 0.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.9 | 5.60 | 19.15 | 29.32 | 2.00 | 103.7 | 67.0 |
| Vice Captain | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 6.07 | 18.59 | 28.26 | 3.00 | 100.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.66 | 17.95 | 27.53 | 2.00 | 90.2 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.8 | 4.80 | 15.31 | 24.41 | 8.00 | 77.0 | 90.0 |
| XI | Bench | Leandro Trossard | MID | -1 | 7.0 | 4.30 | 13.68 | 22.74 | 0.00 | 70.6 | 0.0 |

## GW20

- Train rows: 89739
- Bank: 0.40 -> 0.70
- Free transfers: 2 -> 2
- Captain: Martin Ødegaard
- Vice captain: Kieran Trippier
- Effective captain: Martin Ødegaard
- Chip used: none
- Predicted score: 61.14
- Actual score: 60.00
- Transfer: Leandro Trossard -> Martin Ødegaard (projected gain 14.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Nick Pope | GK | -1 | 5.3 | 4.26 | 13.82 | 21.58 | 5.00 | 93.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 1.65 | 7.56 | 11.54 | 2.00 | 46.3 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | -1 | 5.9 | 6.79 | 24.83 | 40.45 | 9.00 | 111.7 | 90.0 |
| XI | XI | João Cancelo | DEF | -1 | 7.3 | 4.38 | 16.37 | 27.27 | 1.00 | 80.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 3.26 | 12.84 | 20.08 | 6.00 | 79.2 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.17 | 12.29 | 18.55 | 2.00 | 73.2 | 82.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | -1 | 6.5 | 2.02 | 8.34 | 13.51 | 0.00 | 48.9 | 0.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 7.1 | 3.48 | 14.48 | 23.87 | 0.00 | 70.1 | 90.0 |
| Bench 3 | Bench | Gabriel Fernando de Jesus | FWD | -1 | 8.0 | 2.56 | 9.42 | 16.81 | 0.00 | 32.3 | 0.0 |
| Bench 2 | Bench | Ivan Toney | FWD | -1 | 7.5 | 2.68 | 6.25 | 11.18 | 9.00 | 13.5 | 81.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.9 | 5.43 | 20.16 | 32.75 | 3.00 | 89.6 | 84.0 |
| Captain | Captain | Martin Ødegaard | MID | -1 | 6.6 | 7.45 | 19.43 | 31.99 | 9.00 | 105.9 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 4.89 | 17.92 | 28.16 | 2.00 | 80.7 | 78.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.9 | 5.61 | 16.60 | 27.11 | 2.00 | 74.2 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 6.9 | 4.97 | 15.34 | 23.84 | 12.00 | 86.1 | 180.0 |

## GW21

- Train rows: 90438
- Bank: 0.70 -> 1.20
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Martin Ødegaard
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 70.61
- Actual score: 47.00
- Transfer: Nick Pope -> David De Gea Quintana (projected gain 2.96, hit 0)
- Autosub outfielders: Ivan Toney.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David De Gea Quintana | GK | -1 | 4.9 | 4.29 | 12.82 | 19.56 | 1.00 | 121.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 2.74 | 9.86 | 15.53 | 1.00 | 78.7 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 6.0 | 8.37 | 20.66 | 34.01 | 8.00 | 120.6 | 90.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 4.30 | 12.43 | 21.67 | 6.00 | 76.8 | 90.0 |
| XI | Bench | João Cancelo | DEF | -1 | 7.2 | 5.27 | 11.71 | 20.11 | 0.00 | 78.3 | 0.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.16 | 10.71 | 16.81 | 1.00 | 90.2 | 90.0 |
| Bench 4 | Bench | Virgil van Dijk | DEF | -1 | 6.5 | 1.59 | 5.74 | 10.27 | 0.00 | 37.1 | 0.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 7.2 | 4.25 | 11.57 | 20.27 | 2.00 | 84.4 | 90.0 |
| Bench 2 | Autosub In | Ivan Toney | FWD | -1 | 7.4 | 3.97 | 7.80 | 14.99 | 1.00 | 68.1 | 90.0 |
| Bench 3 | Bench | Gabriel Fernando de Jesus | FWD | -1 | 7.9 | 2.63 | 6.09 | 11.69 | 0.00 | 34.2 | 0.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.0 | 6.77 | 18.97 | 31.63 | 7.00 | 125.1 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 6.07 | 17.02 | 27.77 | 2.00 | 80.4 | 81.0 |
| Vice Captain | XI | Martin Ødegaard | MID | -1 | 6.7 | 7.03 | 14.76 | 26.52 | 5.00 | 106.5 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.9 | 6.28 | 14.69 | 24.56 | 3.00 | 100.0 | 85.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.9 | 5.46 | 12.90 | 23.73 | 3.00 | 83.3 | 90.0 |

## GW22

- Train rows: 91145
- Bank: 1.20 -> 2.50
- Free transfers: 2 -> 2
- Captain: Marcus Rashford
- Vice captain: Kieran Trippier
- Effective captain: Marcus Rashford
- Chip used: none
- Predicted score: 66.91
- Actual score: 67.00
- Transfer: Virgil van Dijk -> Luke Shaw (projected gain 3.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David De Gea Quintana | GK | -1 | 4.9 | 4.93 | 11.79 | 17.66 | 3.00 | 122.9 | 180.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.1 | 3.50 | 9.84 | 15.69 | 2.00 | 81.2 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | -1 | 6.0 | 7.61 | 21.48 | 36.02 | 2.00 | 107.8 | 90.0 |
| XI | XI | Luke Shaw | DEF | -1 | 5.2 | 5.01 | 12.14 | 18.22 | 6.00 | 113.8 | 180.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.79 | 11.63 | 20.19 | 5.00 | 82.2 | 78.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.17 | 10.73 | 16.95 | 2.00 | 85.0 | 90.0 |
| Bench 3 | Bench | João Cancelo | DEF | -1 | 7.2 | 2.88 | 9.08 | 15.00 | 0.00 | 41.6 | 0.0 |
| XI | XI | Aleksandar Mitrović | FWD | -1 | 7.1 | 3.42 | 10.90 | 18.59 | 2.00 | 75.4 | 90.0 |
| Bench 2 | Bench | Ivan Toney | FWD | -1 | 7.6 | 3.36 | 9.09 | 15.50 | 1.00 | 49.9 | 90.0 |
| Bench 4 | Bench | Gabriel Fernando de Jesus | FWD | -1 | 7.9 | 2.30 | 7.05 | 12.48 | 0.00 | 28.3 | 0.0 |
| Captain | Captain | Marcus Rashford | MID | -1 | 7.1 | 8.15 | 21.14 | 32.31 | 20.00 | 137.5 | 180.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.8 | 5.90 | 16.02 | 26.17 | 1.00 | 75.5 | 58.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.8 | 5.49 | 15.45 | 26.65 | 2.00 | 87.1 | 76.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.9 | 5.22 | 14.19 | 23.39 | 2.00 | 85.8 | 80.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 5.06 | 14.03 | 24.49 | 2.00 | 79.3 | 90.0 |

## GW23

- Train rows: 91885
- Bank: 2.50 -> 5.40
- Free transfers: 2 -> 2
- Captain: Marcus Rashford
- Vice captain: Kieran Trippier
- Effective captain: Marcus Rashford
- Chip used: none
- Predicted score: 66.48
- Actual score: 76.00
- Chip advisory: bench_boost (0.60): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Gabriel Fernando de Jesus -> Wilfried Gnonto (projected gain 0.51, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David De Gea Quintana | GK | -1 | 5.0 | 4.69 | 13.13 | 19.98 | 10.00 | 126.5 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.0 | 3.68 | 9.54 | 15.78 | 3.00 | 80.9 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | -1 | 6.1 | 6.60 | 20.36 | 33.13 | 2.00 | 106.0 | 90.0 |
| XI | XI | Luke Shaw | DEF | -1 | 5.3 | 4.99 | 15.40 | 23.67 | 12.00 | 119.9 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.82 | 11.87 | 18.28 | 3.00 | 111.8 | 180.0 |
| XI | XI | Ivan Perišić | DEF | -1 | 5.5 | 3.76 | 11.83 | 18.97 | 1.00 | 81.7 | 74.0 |
| Bench 4 | Bench | João Cancelo | DEF | -1 | 7.1 | 2.12 | 6.18 | 12.35 | 0.00 | 40.4 | 0.0 |
| XI | XI | Wilfried Gnonto | FWD | -1 | 5.0 | 4.40 | 11.92 | 19.34 | 2.00 | 105.7 | 90.0 |
| Bench 2 | Bench | Ivan Toney | FWD | -1 | 7.7 | 3.46 | 11.47 | 18.81 | 9.00 | 70.6 | 90.0 |
| Bench 3 | Bench | Aleksandar Mitrović | FWD | -1 | 7.0 | 3.12 | 10.43 | 19.17 | 2.00 | 71.8 | 83.0 |
| Captain | Captain | Marcus Rashford | MID | -1 | 7.2 | 8.71 | 25.58 | 38.98 | 8.00 | 152.0 | 90.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.9 | 5.88 | 17.01 | 26.51 | 4.00 | 113.8 | 180.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.7 | 5.41 | 15.28 | 25.31 | 5.00 | 100.6 | 136.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.7 | 4.26 | 13.57 | 24.30 | 11.00 | 77.0 | 89.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.8 | 4.24 | 12.65 | 21.18 | 10.00 | 76.6 | 80.0 |

## GW24

- Train rows: 92630
- Bank: 5.40 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Martin Ødegaard
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 68.08
- Actual score: 57.00
- Transfer: Aleksandar Mitrović -> Erling Haaland (projected gain 13.91, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David De Gea Quintana | GK | -1 | 5.0 | 3.32 | 10.72 | 17.17 | 7.00 | 100.0 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.0 | 3.18 | 9.21 | 15.44 | 2.00 | 80.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.1 | 6.74 | 19.85 | 31.79 | 1.00 | 112.1 | 63.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.86 | 13.86 | 21.85 | 1.00 | 116.3 | 90.0 |
| XI | XI | Luke Shaw | DEF | -1 | 5.3 | 4.22 | 13.35 | 21.30 | 6.00 | 104.1 | 68.0 |
| Bench 2 | Bench | Ivan Perišić | DEF | -1 | 5.5 | 3.94 | 11.01 | 18.10 | 0.00 | 74.6 | 12.0 |
| Bench 4 | Bench | João Cancelo | DEF | -1 | 7.1 | 1.04 | 3.50 | 7.47 | 0.00 | 7.2 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.2 | 8.45 | 23.41 | 39.36 | 2.00 | 144.9 | 90.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.6 | 4.34 | 12.34 | 20.49 | 2.00 | 79.4 | 90.0 |
| Bench 3 | Bench | Wilfried Gnonto | FWD | -1 | 5.0 | 3.64 | 9.92 | 16.91 | 1.00 | 88.5 | 90.0 |
| Vice Captain | XI | Martin Ødegaard | MID | -1 | 7.0 | 6.98 | 19.69 | 30.76 | 8.00 | 124.0 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.2 | 6.30 | 19.66 | 33.62 | 15.00 | 129.1 | 68.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 5.59 | 15.80 | 24.70 | 6.00 | 94.8 | 22.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.7 | 4.76 | 13.73 | 22.79 | 6.00 | 75.1 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | -1 | 5.7 | 4.07 | 12.13 | 20.22 | 1.00 | 80.0 | 63.0 |

## GW25

- Train rows: 93376
- Bank: 0.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Martin Ødegaard
- Vice captain: Erling Haaland
- Effective captain: Martin Ødegaard
- Chip used: none
- Predicted score: 63.43
- Actual score: 97.00
- Transfer: João Cancelo -> Trent Alexander-Arnold (projected gain 6.61, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.0 | 3.15 | 10.13 | 16.43 | 2.00 | 83.4 | 90.0 |
| Bench 1 | Bench | David De Gea Quintana | GK | -1 | 5.0 | 2.31 | 8.84 | 15.22 | 0.00 | 64.1 | 0.0 |
| XI | Bench | Kieran Trippier | DEF | -1 | 6.1 | 4.95 | 17.21 | 26.71 | 0.00 | 66.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.3 | 6.09 | 14.12 | 20.83 | 13.00 | 112.6 | 159.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 5.12 | 12.82 | 19.29 | 12.00 | 122.3 | 180.0 |
| XI | Bench | Luke Shaw | DEF | -1 | 5.4 | 3.02 | 10.55 | 17.59 | 0.00 | 55.9 | 0.0 |
| Bench 2 | Bench | Ivan Perišić | DEF | -1 | 5.5 | 2.61 | 7.74 | 13.90 | 0.00 | 47.9 | 0.0 |
| Vice Captain | XI | Erling Haaland | FWD | -1 | 12.2 | 6.65 | 19.49 | 34.68 | 10.00 | 111.2 | 71.0 |
| XI | XI | Wilfried Gnonto | FWD | -1 | 5.0 | 3.53 | 9.55 | 15.91 | 1.00 | 85.8 | 60.0 |
| Bench 3 | Bench | Ivan Toney | FWD | -1 | 7.7 | 2.24 | 9.52 | 16.50 | 0.00 | 44.2 | 0.0 |
| Captain | Captain | Martin Ødegaard | MID | -1 | 7.0 | 7.06 | 17.79 | 28.21 | 11.00 | 130.3 | 173.0 |
| XI | Bench | Marcus Rashford | MID | -1 | 7.3 | 5.36 | 17.34 | 30.39 | 0.00 | 80.5 | 0.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.6 | 6.27 | 15.72 | 24.31 | 11.00 | 104.0 | 180.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 5.17 | 13.75 | 20.60 | 26.00 | 89.5 | 180.0 |
| Bench 4 | Bench | Miguel Almirón Rejala | MID | -1 | 5.6 | 1.94 | 8.64 | 15.52 | 0.00 | 35.1 | 0.0 |

## GW26

- Train rows: 94122
- Bank: 0.00 -> 0.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Gabriel Martinelli Silva
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 68.70
- Actual score: 63.00
- Transfer: Ivan Perišić -> Gabriel dos Santos Magalhães (projected gain 6.52, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.0 | 3.58 | 10.14 | 16.27 | 11.00 | 82.7 | 90.0 |
| Bench 1 | Bench | David De Gea Quintana | GK | -1 | 5.0 | 1.89 | 6.54 | 11.70 | -1.00 | 51.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.3 | 5.59 | 16.32 | 25.96 | 6.00 | 109.0 | 90.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 5.86 | 15.46 | 23.60 | 1.00 | 132.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 5.43 | 14.78 | 22.74 | 1.00 | 131.8 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.1 | 4.74 | 14.41 | 23.85 | 1.00 | 69.5 | 90.0 |
| Bench 2 | Bench | Luke Shaw | DEF | -1 | 5.4 | 2.68 | 8.38 | 14.22 | -1.00 | 50.8 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.2 | 7.39 | 21.54 | 35.56 | 4.00 | 107.2 | 90.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.7 | 3.03 | 8.68 | 14.16 | 8.00 | 41.6 | 90.0 |
| Bench 3 | Bench | Wilfried Gnonto | FWD | -1 | 5.1 | 2.02 | 6.45 | 10.67 | 1.00 | 58.9 | 22.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.7 | 6.69 | 21.07 | 32.77 | 21.00 | 111.4 | 90.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 7.0 | 7.06 | 19.54 | 31.15 | 2.00 | 131.1 | 90.0 |
| Vice Captain | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 7.10 | 19.50 | 29.75 | 2.00 | 125.4 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.3 | 4.84 | 15.12 | 25.86 | 2.00 | 68.7 | 84.0 |
| Bench 4 | Bench | Miguel Almirón Rejala | MID | -1 | 5.6 | 1.99 | 7.24 | 12.53 | 2.00 | 43.7 | 76.0 |

## GW27

- Train rows: 94869
- Bank: 0.30 -> 2.30
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Mohamed Salah
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 71.05
- Actual score: 68.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (9.81) beats the best remaining Triple Captain opportunity (19.75).
- Transfer: Ivan Toney -> Brennan Johnson (projected gain 1.93, hit 0)
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (9.81) beats the best remaining Triple Captain opportunity (19.75).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.0 | 3.57 | 10.65 | 17.75 | 2.00 | 87.4 | 90.0 |
| Bench 1 | Bench | David De Gea Quintana | GK | -1 | 5.0 | 2.95 | 8.85 | 15.00 | 8.00 | 72.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.0 | 5.55 | 15.89 | 26.54 | 5.00 | 86.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.3 | 4.64 | 13.37 | 22.46 | 2.00 | 88.8 | 64.0 |
| XI | XI | William Saliba | DEF | -1 | 5.3 | 4.36 | 11.38 | 17.72 | 7.00 | 90.3 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.82 | 10.36 | 16.54 | 14.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Luke Shaw | DEF | -1 | 5.3 | 3.29 | 9.86 | 17.35 | 5.00 | 65.1 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | -1 | 12.2 | 7.31 | 21.24 | 34.21 | 6.00 | 101.1 | 90.0 |
| XI | XI | Brennan Johnson | FWD | -1 | 5.7 | 3.81 | 11.59 | 18.81 | 2.00 | 86.4 | 66.0 |
| Bench 4 | Bench | Wilfried Gnonto | FWD | -1 | 5.1 | 1.77 | 5.45 | 10.15 | 4.00 | 46.1 | 24.0 |
| Vice Captain | XI | Mohamed Salah | MID | -1 | 12.7 | 6.58 | 19.32 | 33.01 | 0.00 | 104.1 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.3 | 5.76 | 17.36 | 29.96 | 3.00 | 84.1 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 5.36 | 15.86 | 25.20 | 8.00 | 82.7 | 76.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 7.0 | 5.68 | 15.67 | 25.69 | 7.00 | 91.7 | 90.0 |
| Bench 3 | Bench | Miguel Almirón Rejala | MID | -1 | 5.5 | 2.81 | 8.11 | 14.39 | 9.00 | 54.2 | 22.0 |

## GW28

- Train rows: 95619
- Bank: 2.30 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Martin Ødegaard
- Effective captain: Martin Ødegaard
- Chip used: none
- Predicted score: 58.00
- Actual score: 17.00
- Transfer: Brennan Johnson -> Ivan Toney (projected gain 5.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Danny Ward | GK | -1 | 4.0 | 3.20 | 8.96 | 14.68 | 0.00 | 78.4 | 0.0 |
| Bench 1 | Bench | David De Gea Quintana | GK | -1 | 5.0 | 1.83 | 8.24 | 14.85 | 0.00 | 47.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.0 | 5.79 | 16.51 | 26.71 | 2.00 | 92.7 | 90.0 |
| XI | Bench | William Saliba | DEF | -1 | 5.3 | 4.68 | 11.91 | 18.60 | 0.00 | 96.1 | 0.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 4.48 | 11.61 | 18.68 | 2.00 | 97.0 | 85.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | -1 | 7.3 | 2.84 | 10.69 | 18.11 | 0.00 | 46.8 | 0.0 |
| Bench 4 | Bench | Luke Shaw | DEF | -1 | 5.2 | 1.98 | 8.77 | 15.98 | 0.00 | 42.1 | 0.0 |
| Captain | Bench | Erling Haaland | FWD | -1 | 12.2 | 5.89 | 19.55 | 33.13 | 0.00 | 72.3 | 0.0 |
| XI | XI | Ivan Toney | FWD | -1 | 7.8 | 5.22 | 15.49 | 25.63 | 2.00 | 96.3 | 90.0 |
| Bench 3 | Bench | Wilfried Gnonto | FWD | -1 | 5.0 | 2.19 | 6.31 | 11.06 | 5.00 | 46.3 | 60.0 |
| Vice Captain | Captain | Martin Ødegaard | MID | -1 | 6.9 | 5.89 | 16.40 | 27.45 | 2.00 | 97.8 | 90.0 |
| XI | Bench | Mohamed Salah | MID | -1 | 12.8 | 4.31 | 16.12 | 28.07 | 0.00 | 60.9 | 0.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.5 | 5.53 | 15.47 | 25.50 | 7.00 | 87.0 | 82.0 |
| XI | Bench | Marcus Rashford | MID | -1 | 7.4 | 4.29 | 15.20 | 26.86 | 0.00 | 61.2 | 0.0 |
| Bench 2 | Bench | Miguel Almirón Rejala | MID | -1 | 5.4 | 2.62 | 8.04 | 14.65 | 0.00 | 45.9 | 0.0 |

## GW29

- Train rows: 96370
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Ivan Toney
- Effective captain: Kieran Trippier
- Chip used: bench_boost
- Predicted score: 72.89
- Actual score: 94.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (20.27) beats the best remaining Bench Boost opportunity (8.41).
- Transfer: Miguel Almirón Rejala -> Kaoru Mitoma (projected gain 4.15, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (20.27) beats the best remaining Bench Boost opportunity (8.41).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | -1 | 4.0 | 3.56 | 7.86 | 12.10 | 0.00 | 72.7 | 0.0 |
| Bench 1 | Bench Boost | David De Gea Quintana | GK | -1 | 5.0 | 3.12 | 7.85 | 12.71 | 8.00 | 76.7 | 180.0 |
| Captain | Captain | Kieran Trippier | DEF | -1 | 6.1 | 7.12 | 18.04 | 27.46 | 14.00 | 124.5 | 176.0 |
| Bench 2 | Bench Boost | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 3.30 | 10.00 | 16.47 | 2.00 | 78.3 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | -1 | 7.3 | 3.51 | 9.40 | 15.18 | 0.00 | 70.6 | 90.0 |
| XI | XI | Luke Shaw | DEF | -1 | 5.2 | 3.46 | 8.46 | 13.62 | 1.00 | 74.5 | 126.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | -1 | 5.3 | 2.21 | 7.20 | 12.80 | 0.00 | 46.9 | 0.0 |
| XI | XI | Erling Haaland | FWD | -1 | 12.2 | 5.47 | 16.74 | 28.40 | 0.00 | 65.9 | 0.0 |
| Vice Captain | XI | Ivan Toney | FWD | -1 | 7.8 | 5.88 | 15.92 | 24.68 | 11.00 | 114.4 | 180.0 |
| Bench 3 | Bench Boost | Wilfried Gnonto | FWD | -1 | 4.9 | 3.14 | 8.05 | 13.02 | 0.00 | 83.0 | 0.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.9 | 4.84 | 15.06 | 25.28 | 6.00 | 88.7 | 84.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.4 | 5.53 | 14.89 | 24.36 | 12.00 | 92.3 | 180.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 5.05 | 14.48 | 23.80 | 5.00 | 78.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 4.60 | 13.59 | 23.52 | 7.00 | 78.0 | 94.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 5.5 | 4.99 | 12.49 | 19.56 | 14.00 | 91.0 | 180.0 |

## GW30

- Train rows: 97124
- Bank: 0.20 -> 6.70
- Free transfers: 2 -> 2
- Captain: Dominic Solanke
- Vice captain: Ivan Toney
- Effective captain: Dominic Solanke
- Chip used: none
- Predicted score: 156.48
- Actual score: 50.00
- Transfer: Erling Haaland -> Dominic Solanke (projected gain 87.28, hit 0)
- Autosub outfielders: Trent Alexander-Arnold.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | David De Gea Quintana | GK | -1 | 5.0 | 6.88 | 20.06 | 28.68 | 6.00 | 130.6 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | -1 | 4.0 | 1.56 | 5.01 | 8.85 | 0.00 | 33.4 | 0.0 |
| XI | XI | Kieran Trippier | DEF | -1 | 6.1 | 14.31 | 43.05 | 57.61 | 2.00 | 180.0 | 90.0 |
| XI | XI | Gabriel dos Santos Magalhães | DEF | -1 | 5.2 | 6.75 | 22.21 | 30.39 | 1.00 | 115.0 | 90.0 |
| XI | Bench | Luke Shaw | DEF | -1 | 5.2 | 5.81 | 16.92 | 24.71 | 0.00 | 94.7 | 0.0 |
| Bench 2 | Autosub In | Trent Alexander-Arnold | DEF | -1 | 7.3 | 4.74 | 16.27 | 24.32 | 5.00 | 87.0 | 90.0 |
| Bench 4 | Bench | William Saliba | DEF | -1 | 5.2 | 1.02 | 5.34 | 10.87 | 0.00 | 30.5 | 0.0 |
| Captain | Captain | Dominic Solanke | FWD | -1 | 5.5 | 27.95 | 91.01 | 110.36 | 2.00 | 180.0 | 87.0 |
| Vice Captain | XI | Ivan Toney | FWD | -1 | 7.9 | 15.45 | 48.56 | 64.45 | 4.00 | 180.0 | 90.0 |
| Bench 3 | Bench | Wilfried Gnonto | FWD | -1 | 4.9 | 1.58 | 4.88 | 8.89 | 0.00 | 34.9 | 30.0 |
| XI | XI | Kaoru Mitoma | MID | -1 | 5.6 | 13.92 | 44.34 | 59.07 | 2.00 | 180.0 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | -1 | 6.6 | 12.73 | 40.89 | 53.92 | 13.00 | 153.9 | 90.0 |
| XI | XI | Marcus Rashford | MID | -1 | 7.3 | 10.76 | 31.92 | 45.96 | 6.00 | 153.9 | 80.0 |
| XI | XI | Mohamed Salah | MID | -1 | 12.8 | 7.00 | 24.12 | 36.61 | 5.00 | 100.7 | 90.0 |
| XI | XI | Martin Ødegaard | MID | -1 | 6.8 | 6.98 | 23.18 | 34.81 | 2.00 | 111.9 | 79.0 |