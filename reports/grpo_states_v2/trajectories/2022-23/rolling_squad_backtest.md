# Rolling Squad Backtest Report

- Train seasons in scope: 2019-20, 2020-21, 2021-22, 2022-23, 2023-24, 2024-25, 2025-26, 2026-27
- In-season warm start: 2022-23 GW1-GW1
- Simulated weeks: GW2-GW38
- Total predicted points: 2182.89
- Total actual points: 2032.00
- Average predicted points: 59.00
- Average actual points: 54.92
- Total transfer hits: 0

## Notes

- The feature set includes lagged bonus/BPS/ICT features plus newer xG/xA/xGI/xGC/starts/defensive-contribution features when available.
- Later-era-only features are zero-filled outside their source era and paired with expected_data_source_available / defensive_data_source_available flags so the model can distinguish missing-era zeros from real observations.
- This squad backtest uses a synthetic starting squad at the beginning of the simulated window, approximate price carry-forward, and simple auto-sub handling.
- Bench Boost and Triple Captain are scheduled by an explicit remaining-season optimizer that uses current squad strength plus future schedule opportunity estimates.
- Weekly training expands through the prior deadline, so GW1-GW1 are included before the first simulated week.
- League-average scores were not available for this run.

## GW2

- Train rows: 78237
- Bank: 100.00 -> 0.10
- Free transfers: 1 -> 2
- Captain: Mohamed Salah
- Vice captain: Aleksandar Mitrović
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 64.45
- Actual score: 50.00
- Transfer: none
- Initial squad was constructed synthetically at the start of the backtest from week-level forecasts under a 100.0 budget.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Edouard Mendy | GK | 6 | 5.0 | 4.28 | 11.87 | 18.84 | 1.00 | 110.8 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 5.0 | 3.89 | 10.65 | 16.94 | 1.00 | 97.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 5.21 | 14.60 | 24.18 | 3.00 | 101.2 | 90.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.0 | 4.68 | 13.22 | 21.80 | 11.00 | 101.1 | 90.0 |
| XI | XI | Oleksandr Zinchenko | DEF | 1 | 5.1 | 5.18 | 12.54 | 18.72 | 1.00 | 108.2 | 76.0 |
| XI | XI | Reece James | DEF | 6 | 6.0 | 4.17 | 11.54 | 18.88 | 7.00 | 86.5 | 90.0 |
| Bench 2 | Bench | Lloyd Kelly | DEF | 3 | 4.5 | 2.27 | 9.10 | 15.76 | 0.00 | 96.5 | 90.0 |
| Vice Captain | XI | Aleksandar Mitrović | FWD | 9 | 6.6 | 6.73 | 17.21 | 26.75 | -1.00 | 123.5 | 90.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.5 | 1.90 | 5.10 | 8.13 | 0.00 | 31.4 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.5 | 1.42 | 3.79 | 6.20 | 0.00 | 26.8 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.82 | 21.63 | 35.40 | 2.00 | 126.2 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.0 | 5.88 | 17.22 | 28.23 | 14.00 | 107.5 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.1 | 5.55 | 14.50 | 22.40 | 8.00 | 112.7 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 8.1 | 4.61 | 13.75 | 22.04 | 2.00 | 100.6 | 90.0 |
| XI | XI | Jefferson Lerma Solís | MID | 3 | 5.0 | 2.52 | 9.36 | 15.86 | 0.00 | 94.7 | 90.0 |

## GW3

- Train rows: 78818
- Bank: 0.10 -> 0.60
- Free transfers: 2 -> 2
- Captain: Gabriel Martinelli Silva
- Vice captain: Mohamed Salah
- Effective captain: Gabriel Martinelli Silva
- Chip used: none
- Predicted score: 62.44
- Actual score: 44.00
- Transfer: Lloyd Kelly -> Neco Williams (projected gain 3.15, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Edouard Mendy | GK | 6 | 5.0 | 3.79 | 10.69 | 17.17 | 2.00 | 92.8 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 5.0 | 3.28 | 9.12 | 14.78 | 6.00 | 80.5 | 90.0 |
| XI | XI | Reece James | DEF | 6 | 6.0 | 5.69 | 15.07 | 23.67 | 1.00 | 106.4 | 90.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.0 | 5.00 | 14.70 | 23.68 | 0.00 | 103.2 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 4.84 | 14.05 | 23.27 | 0.00 | 85.3 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.0 | 4.02 | 10.29 | 15.65 | 1.00 | 89.8 | 90.0 |
| XI | XI | Oleksandr Zinchenko | DEF | 1 | 5.1 | 3.51 | 9.58 | 14.66 | 6.00 | 60.8 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.6 | 3.31 | 10.26 | 16.49 | 6.00 | 67.6 | 90.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.5 | 1.04 | 3.00 | 5.09 | 1.00 | 12.4 | 7.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.5 | 0.80 | 2.22 | 3.68 | 0.00 | 12.0 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 13.0 | 7.16 | 20.69 | 34.10 | 8.00 | 103.4 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.0 | 6.22 | 18.90 | 30.58 | 5.00 | 111.4 | 90.0 |
| Captain | Captain | Gabriel Martinelli Silva | MID | 1 | 6.2 | 7.18 | 18.26 | 27.20 | 6.00 | 125.8 | 74.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 8.1 | 4.54 | 13.01 | 20.92 | 3.00 | 83.8 | 85.0 |
| Bench 2 | Bench | Jefferson Lerma Solís | MID | 3 | 5.0 | 2.19 | 7.16 | 12.00 | 2.00 | 76.3 | 90.0 |

## GW4

- Train rows: 79410
- Bank: 0.60 -> 0.60
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kevin De Bruyne
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 56.95
- Actual score: 53.00
- Transfer: none
- No transfer was applied this week.
- Autosub: Jefferson Lerma Solís replaced Oleksandr Zinchenko.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 5.0 | 3.39 | 10.06 | 15.24 | 2.00 | 81.0 | 90.0 |
| Bench 1 | Bench | Edouard Mendy | GK | 6 | 5.0 | 2.98 | 9.56 | 14.72 | 3.00 | 76.9 | 90.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.0 | 4.76 | 14.01 | 21.61 | 1.00 | 82.1 | 60.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 4.47 | 13.48 | 21.60 | 17.00 | 76.8 | 82.0 |
| XI | XI | Reece James | DEF | 6 | 6.0 | 4.24 | 12.70 | 19.34 | 7.00 | 75.4 | 90.0 |
| XI | Bench | Oleksandr Zinchenko | DEF | 1 | 5.2 | 4.06 | 11.53 | 17.32 | 0.00 | 74.3 | 0.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.0 | 3.20 | 9.33 | 13.74 | 1.00 | 72.8 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.6 | 3.56 | 11.60 | 17.76 | 7.00 | 73.1 | 90.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.5 | 1.01 | 4.12 | 6.14 | 0.00 | 12.6 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.5 | 0.61 | 2.27 | 2.79 | 1.00 | 6.7 | 1.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 7.51 | 21.95 | 34.85 | 3.00 | 103.9 | 90.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.1 | 6.35 | 19.02 | 29.75 | 2.00 | 92.7 | 88.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.2 | 4.30 | 13.08 | 19.28 | 2.00 | 56.4 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 8.1 | 3.63 | 11.91 | 18.75 | 6.00 | 65.5 | 82.0 |
| Bench 2 | Autosub In | Jefferson Lerma Solís | MID | 3 | 5.0 | 2.29 | 7.86 | 11.82 | 2.00 | 76.5 | 90.0 |

## GW5

- Train rows: 80011
- Bank: 0.60 -> 1.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kevin De Bruyne
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.35
- Actual score: 61.00
- Transfer: Oleksandr Zinchenko -> William Saliba (projected gain 3.30, hit 0)
- Autosub: Jefferson Lerma Solís replaced Reece James.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Edouard Mendy | GK | 6 | 5.0 | 3.13 | 9.49 | 15.34 | 2.00 | 83.9 | 90.0 |
| XI | XI | Aaron Ramsdale | GK | 1 | 5.0 | 3.23 | 9.30 | 14.56 | 2.00 | 78.6 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 5.71 | 16.28 | 26.20 | 2.00 | 97.5 | 70.0 |
| XI | Bench | Reece James | DEF | 6 | 6.0 | 4.38 | 12.67 | 20.37 | 0.00 | 85.2 | 0.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.0 | 3.84 | 11.76 | 19.11 | 12.00 | 64.1 | 67.0 |
| XI | XI | William Saliba | DEF | 1 | 4.7 | 3.97 | 10.62 | 15.92 | 1.00 | 83.8 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.0 | 2.83 | 8.81 | 13.68 | -1.00 | 75.8 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.6 | 4.25 | 12.48 | 19.31 | 9.00 | 82.9 | 90.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.5 | 0.95 | 2.78 | 4.50 | 0.00 | 7.1 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.5 | 0.29 | 1.99 | 3.27 | 0.00 | 10.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 5.99 | 18.67 | 30.63 | 10.00 | 83.4 | 90.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.1 | 5.76 | 17.41 | 28.22 | 1.00 | 85.0 | 21.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.2 | 4.58 | 13.03 | 20.27 | 10.00 | 68.0 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 8.1 | 3.83 | 12.01 | 19.22 | 2.00 | 71.5 | 75.0 |
| Bench 2 | Autosub In | Jefferson Lerma Solís | MID | 3 | 5.0 | 2.62 | 7.55 | 11.35 | 3.00 | 76.2 | 90.0 |

## GW6

- Train rows: 80619
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Gabriel Martinelli Silva
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 55.36
- Actual score: 35.00
- Transfer: Jefferson Lerma Solís -> Pascal Groß (projected gain 5.75, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Edouard Mendy | GK | 6 | 5.0 | 3.06 | 9.11 | 15.90 | 2.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 5.0 | 2.27 | 7.69 | 13.95 | 2.00 | 73.5 | 90.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.0 | 5.27 | 14.80 | 24.85 | 2.00 | 85.8 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 4.69 | 14.00 | 23.55 | 1.00 | 78.6 | 58.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.0 | 3.50 | 9.38 | 15.17 | 4.00 | 80.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 4.7 | 2.69 | 8.86 | 15.00 | 0.00 | 73.7 | 90.0 |
| Bench 2 | Bench | Reece James | DEF | 6 | 6.0 | 1.88 | 6.90 | 12.99 | 1.00 | 28.8 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.7 | 4.16 | 12.64 | 20.91 | 5.00 | 87.2 | 90.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.4 | 0.46 | 1.96 | 4.58 | 1.00 | 5.8 | 4.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.4 | 0.01 | 1.15 | 3.00 | 0.00 | 7.1 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 13.0 | 6.44 | 19.54 | 33.90 | 3.00 | 92.2 | 90.0 |
| Vice Captain | XI | Gabriel Martinelli Silva | MID | 1 | 6.3 | 5.73 | 15.85 | 25.94 | 2.00 | 101.1 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.1 | 4.33 | 14.23 | 24.77 | 7.00 | 51.6 | 90.0 |
| XI | XI | Pascal Groß | MID | 5 | 5.9 | 4.84 | 13.55 | 21.20 | 5.00 | 90.2 | 90.0 |
| XI | XI | Dejan Kulusevski | MID | 18 | 8.1 | 4.20 | 12.01 | 20.41 | 1.00 | 70.2 | 12.0 |

## GW7

- Train rows: 81243
- Bank: 0.10 -> 0.00
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kevin De Bruyne
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 44.82
- Actual score: 0.00
- Transfer: Dejan Kulusevski -> Luis Díaz (projected gain 4.67, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Edouard Mendy | GK | 6 | 5.0 | 2.29 | 7.71 | 13.29 | 0.00 | 65.4 | 0.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 5.0 | 2.00 | 6.96 | 12.42 | 0.00 | 60.4 | 0.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 3.98 | 12.74 | 21.78 | 0.00 | 63.8 | 0.0 |
| XI | Bench | João Cancelo | DEF | 13 | 7.0 | 3.90 | 12.38 | 20.80 | 0.00 | 63.7 | 0.0 |
| XI | Bench | Reece James | DEF | 6 | 6.0 | 2.67 | 9.16 | 16.11 | 0.00 | 50.2 | 0.0 |
| XI | Bench | Neco Williams | DEF | 16 | 4.0 | 2.68 | 8.31 | 13.32 | 0.00 | 60.1 | 0.0 |
| Bench 2 | Bench | William Saliba | DEF | 1 | 4.7 | 2.08 | 7.49 | 12.67 | 0.00 | 53.5 | 0.0 |
| XI | Bench | Aleksandar Mitrović | FWD | 9 | 6.7 | 3.07 | 10.01 | 16.58 | 0.00 | 51.5 | 0.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.4 | 0.06 | 1.61 | 3.79 | 0.00 | 0.0 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.4 | 0.00 | 0.02 | 1.03 | 0.00 | 0.0 | 0.0 |
| Captain | Bench | Mohamed Salah | MID | 12 | 13.0 | 5.83 | 18.32 | 30.83 | 0.00 | 77.9 | 0.0 |
| Vice Captain | Bench | Kevin De Bruyne | MID | 13 | 12.1 | 4.33 | 14.63 | 25.20 | 0.00 | 60.0 | 0.0 |
| XI | Bench | Luis Díaz | MID | 12 | 8.2 | 3.82 | 12.25 | 20.07 | 0.00 | 59.2 | 0.0 |
| XI | Bench | Gabriel Martinelli Silva | MID | 1 | 6.3 | 3.85 | 12.16 | 19.64 | 0.00 | 51.3 | 0.0 |
| XI | Bench | Pascal Groß | MID | 5 | 5.9 | 2.57 | 9.45 | 15.70 | 0.00 | 43.6 | 0.0 |

## GW8

- Train rows: 81867
- Bank: 0.00 -> 0.70
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Kevin De Bruyne
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 52.63
- Actual score: 56.00
- Transfer: Reece James -> Kieran Trippier (projected gain 9.58, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 1.60 | 4.91 | 8.52 | 6.00 | 46.2 | 90.0 |
| Bench 1 | Bench | Edouard Mendy | GK | 6 | 5.0 | 1.23 | 4.90 | 8.74 | 0.00 | 32.7 | 0.0 |
| Captain | Captain | Kieran Trippier | DEF | 15 | 5.3 | 6.95 | 16.11 | 23.79 | 5.00 | 119.5 | 90.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.1 | 5.05 | 13.32 | 21.45 | 9.00 | 82.2 | 90.0 |
| XI | Bench | Trent Alexander-Arnold | DEF | 12 | 7.5 | 3.02 | 10.40 | 17.65 | 0.00 | 44.2 | 0.0 |
| XI | XI | William Saliba | DEF | 1 | 4.7 | 2.62 | 7.37 | 11.73 | 15.00 | 59.5 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.0 | 2.57 | 6.46 | 10.01 | 1.00 | 53.5 | 87.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.7 | 5.32 | 13.27 | 20.04 | 2.00 | 83.2 | 89.0 |
| Bench 4 | Bench | Sam Greenwood | FWD | 11 | 4.4 | 0.09 | 1.39 | 3.03 | 0.00 | 0.0 | 0.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 2 | 4.3 | 0.16 | 0.13 | 0.70 | 0.00 | 0.9 | 0.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.1 | 6.34 | 17.13 | 27.27 | 10.00 | 90.3 | 71.0 |
| XI | Bench | Mohamed Salah | MID | 12 | 13.0 | 4.88 | 15.59 | 26.50 | 0.00 | 55.2 | 0.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.3 | 4.54 | 11.81 | 18.63 | 3.00 | 70.1 | 77.0 |
| XI | Bench | Luis Díaz | MID | 12 | 8.2 | 2.79 | 9.29 | 15.56 | 0.00 | 35.9 | 0.0 |
| Bench 2 | Bench | Pascal Groß | MID | 5 | 5.9 | 2.13 | 7.58 | 13.10 | 0.00 | 35.7 | 0.0 |

## GW9

- Train rows: 82498
- Bank: 0.70 -> 0.30
- Free transfers: 2 -> 2
- Captain: João Cancelo
- Vice captain: Gabriel Martinelli Silva
- Effective captain: João Cancelo
- Chip used: none
- Predicted score: 40.69
- Actual score: 35.00
- Transfer: Pascal Groß -> Youri Tielemans (projected gain 2.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 2.72 | 7.28 | 11.89 | 2.00 | 71.9 | 90.0 |
| Bench 1 | Bench | Edouard Mendy | GK | 6 | 4.9 | 0.59 | 2.13 | 4.52 | 0.00 | 21.3 | 0.0 |
| Captain | Captain | João Cancelo | DEF | 13 | 7.1 | 4.27 | 12.18 | 20.48 | 1.00 | 74.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.3 | 3.69 | 9.96 | 15.99 | 7.00 | 59.3 | 82.0 |
| XI | XI | William Saliba | DEF | 1 | 4.8 | 3.69 | 9.66 | 15.53 | 1.00 | 80.8 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.0 | 2.54 | 7.01 | 10.85 | -1.00 | 64.4 | 45.0 |
| Bench 2 | Bench | Trent Alexander-Arnold | DEF | 12 | 7.4 | 1.05 | 5.39 | 10.72 | 0.00 | 13.7 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.7 | 3.70 | 10.41 | 16.37 | 0.00 | 62.9 | 36.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.3 | 0.34 | 0.60 | 1.56 | 0.00 | 1.0 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.3 | 0.27 | 0.21 | 0.77 | 0.00 | 5.6 | 0.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.1 | 3.92 | 12.30 | 21.46 | 8.00 | 47.6 | 74.0 |
| Vice Captain | XI | Gabriel Martinelli Silva | MID | 1 | 6.3 | 3.96 | 10.70 | 16.98 | 4.00 | 61.6 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.8 | 2.04 | 8.57 | 16.49 | 5.00 | 10.4 | 90.0 |
| XI | XI | Youri Tielemans | MID | 10 | 6.3 | 3.35 | 8.46 | 13.12 | 3.00 | 65.8 | 79.0 |
| XI | XI | Luis Díaz | MID | 12 | 8.2 | 2.53 | 7.73 | 13.16 | 4.00 | 35.3 | 45.0 |

## GW10

- Train rows: 83136
- Bank: 0.30 -> 1.50
- Free transfers: 2 -> 2
- Captain: Kevin De Bruyne
- Vice captain: Kieran Trippier
- Effective captain: Kevin De Bruyne
- Chip used: none
- Predicted score: 45.74
- Actual score: 60.00
- Transfer: Trent Alexander-Arnold -> Reece James (projected gain 4.02, hit 0)
- Autosub: Cameron Archer replaced Aleksandar Mitrović.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 2.37 | 6.50 | 10.76 | 1.00 | 70.5 | 90.0 |
| Bench 1 | Bench | Edouard Mendy | GK | 6 | 4.9 | 1.08 | 2.35 | 4.58 | 0.00 | 22.0 | 0.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.1 | 4.98 | 13.22 | 21.37 | 18.00 | 84.9 | 69.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 5.4 | 5.12 | 12.97 | 20.18 | 7.00 | 90.5 | 83.0 |
| XI | XI | Reece James | DEF | 6 | 6.1 | 4.10 | 9.85 | 15.64 | 1.00 | 71.6 | 18.0 |
| XI | XI | William Saliba | DEF | 1 | 4.8 | 3.04 | 8.22 | 13.50 | 1.00 | 72.9 | 90.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.0 | 2.45 | 5.88 | 9.76 | 1.00 | 55.7 | 32.0 |
| XI | Bench | Aleksandar Mitrović | FWD | 9 | 6.7 | 1.43 | 5.46 | 9.75 | 0.00 | 23.1 | 0.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.3 | 0.61 | 0.97 | 1.81 | 0.00 | 8.0 | 0.0 |
| Bench 4 | Autosub In | Cameron Archer | FWD | 2 | 4.3 | 0.44 | 0.45 | 0.86 | 1.00 | 8.3 | 9.0 |
| Captain | Captain | Kevin De Bruyne | MID | 13 | 12.2 | 6.14 | 16.63 | 27.49 | 6.00 | 86.5 | 69.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.7 | 3.43 | 11.47 | 20.30 | 2.00 | 47.6 | 68.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.3 | 3.98 | 10.74 | 17.45 | 12.00 | 69.8 | 90.0 |
| XI | XI | Luis Díaz | MID | 12 | 8.1 | 2.49 | 7.40 | 13.02 | 3.00 | 38.4 | 41.0 |
| XI | XI | Youri Tielemans | MID | 10 | 6.3 | 2.51 | 6.75 | 11.26 | 2.00 | 58.8 | 90.0 |

## GW11

- Train rows: 83777
- Bank: 1.50 -> 1.30
- Free transfers: 2 -> 2
- Captain: Gabriel Martinelli Silva
- Vice captain: João Cancelo
- Effective captain: Gabriel Martinelli Silva
- Chip used: none
- Predicted score: 48.88
- Actual score: 53.00
- Transfer: Luis Díaz -> Phil Foden (projected gain 9.28, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 3.07 | 7.95 | 12.25 | 10.00 | 78.3 | 90.0 |
| Bench 1 | Bench | Edouard Mendy | GK | 6 | 4.9 | 1.06 | 2.45 | 4.25 | 0.00 | 20.3 | 0.0 |
| Vice Captain | XI | João Cancelo | DEF | 13 | 7.1 | 5.30 | 14.51 | 22.99 | 2.00 | 91.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.4 | 5.01 | 13.83 | 21.08 | 6.00 | 87.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 4.9 | 4.09 | 10.50 | 16.22 | 5.00 | 85.2 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.0 | 2.44 | 6.26 | 9.72 | 2.00 | 56.8 | 90.0 |
| Bench 2 | Bench | Reece James | DEF | 6 | 6.1 | 1.39 | 4.53 | 8.30 | 0.00 | 18.0 | 0.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.6 | 1.58 | 4.92 | 9.42 | 7.00 | 19.9 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 2 | 4.3 | 0.74 | 1.49 | 2.29 | 0.00 | 14.8 | 0.0 |
| Bench 4 | Bench | Sam Greenwood | FWD | 11 | 4.3 | 0.29 | 0.82 | 1.17 | 0.00 | 7.5 | 0.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.2 | 4.92 | 15.15 | 25.02 | 2.00 | 71.1 | 90.0 |
| Captain | Captain | Gabriel Martinelli Silva | MID | 1 | 6.3 | 5.74 | 14.52 | 22.68 | 3.00 | 94.0 | 90.0 |
| XI | XI | Phil Foden | MID | 13 | 8.2 | 4.50 | 12.94 | 20.76 | 2.00 | 70.4 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.7 | 3.55 | 11.48 | 20.66 | 8.00 | 55.4 | 89.0 |
| XI | XI | Youri Tielemans | MID | 10 | 6.3 | 2.93 | 7.79 | 12.56 | 3.00 | 71.3 | 81.0 |

## GW12

- Train rows: 84420
- Bank: 1.30 -> 0.90
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kieran Trippier
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 54.74
- Actual score: 37.00
- Transfer: Reece James -> Virgil van Dijk (projected gain 3.90, hit 0)
- Autosub: Neco Williams replaced João Cancelo.
- Autosub: Cameron Archer replaced William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | Bench | Aaron Ramsdale | GK | 1 | 4.9 | 1.85 | 6.55 | 11.56 | 0.00 | 56.3 | 0.0 |
| Bench 1 | Bench | Edouard Mendy | GK | 6 | 4.9 | 0.74 | 2.19 | 3.36 | 0.00 | 17.6 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 5.5 | 5.98 | 15.74 | 23.53 | 9.00 | 101.6 | 90.0 |
| XI | Bench | João Cancelo | DEF | 13 | 7.1 | 4.00 | 12.93 | 21.49 | 0.00 | 63.6 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.22 | 10.66 | 16.04 | 7.00 | 91.9 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 4.9 | 2.59 | 8.69 | 14.24 | 0.00 | 57.6 | 0.0 |
| Bench 2 | Autosub In | Neco Williams | DEF | 16 | 4.0 | 2.58 | 7.03 | 10.54 | 6.00 | 70.1 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.6 | 4.96 | 12.02 | 17.89 | 6.00 | 86.4 | 84.0 |
| Bench 3 | Autosub In | Cameron Archer | FWD | 2 | 4.3 | 0.58 | 1.28 | 1.22 | 1.00 | 11.1 | 9.0 |
| Bench 4 | Bench | Sam Greenwood | FWD | 11 | 4.3 | 0.33 | 0.86 | 1.12 | 0.00 | 9.0 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.7 | 8.20 | 21.18 | 32.44 | 3.00 | 134.1 | 90.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 12.2 | 4.80 | 15.68 | 26.94 | 0.00 | 69.6 | 0.0 |
| XI | Bench | Gabriel Martinelli Silva | MID | 1 | 6.3 | 3.77 | 12.08 | 20.08 | 0.00 | 63.6 | 0.0 |
| XI | Bench | Phil Foden | MID | 13 | 8.2 | 3.03 | 11.25 | 19.49 | 0.00 | 46.3 | 0.0 |
| XI | XI | Youri Tielemans | MID | 10 | 6.3 | 3.13 | 8.02 | 12.33 | 2.00 | 70.7 | 90.0 |

## GW13

- Train rows: 85065
- Bank: 0.90 -> 1.70
- Free transfers: 2 -> 2
- Captain: Phil Foden
- Vice captain: Kieran Trippier
- Effective captain: Phil Foden
- Chip used: none
- Predicted score: 47.88
- Actual score: 49.00
- Transfer: Edouard Mendy -> Danny Ward (projected gain 4.34, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | 10 | 4.1 | 3.81 | 9.87 | 14.92 | 8.00 | 88.9 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 4.9 | 1.97 | 5.69 | 8.76 | 2.00 | 49.2 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 5.5 | 4.59 | 13.58 | 21.27 | 2.00 | 87.9 | 90.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.1 | 4.24 | 12.14 | 19.37 | 2.00 | 65.8 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 3.18 | 8.84 | 13.75 | 2.00 | 74.8 | 90.0 |
| XI | XI | Neco Williams | DEF | 16 | 4.0 | 3.32 | 8.79 | 12.99 | 6.00 | 84.7 | 72.0 |
| XI | XI | William Saliba | DEF | 1 | 4.9 | 3.21 | 8.71 | 12.86 | 2.00 | 62.8 | 90.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.7 | 3.46 | 9.32 | 13.89 | 6.00 | 51.3 | 90.0 |
| Bench 3 | Bench | Cameron Archer | FWD | 2 | 4.3 | 0.93 | 2.73 | 3.59 | 1.00 | 20.9 | 9.0 |
| Bench 4 | Bench | Sam Greenwood | FWD | 11 | 4.3 | 0.84 | 1.71 | 2.20 | 2.00 | 14.3 | 75.0 |
| Captain | Captain | Phil Foden | MID | 13 | 8.3 | 4.96 | 13.72 | 21.05 | 1.00 | 77.5 | 28.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.8 | 4.15 | 13.32 | 21.31 | 2.00 | 53.4 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.1 | 3.60 | 12.12 | 20.28 | 9.00 | 45.8 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.4 | 4.26 | 11.77 | 18.37 | 2.00 | 67.1 | 70.0 |
| XI | XI | Youri Tielemans | MID | 10 | 6.3 | 3.33 | 8.98 | 13.58 | 8.00 | 77.0 | 90.0 |

## GW14

- Train rows: 85713
- Bank: 1.70 -> 2.50
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Kevin De Bruyne
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 58.30
- Actual score: 79.00
- Transfer: Youri Tielemans -> Miguel Almirón Rejala (projected gain 4.87, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | 10 | 4.1 | 3.05 | 9.43 | 15.09 | 3.00 | 89.6 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 4.9 | 2.75 | 7.38 | 11.49 | 6.00 | 71.2 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | 15 | 5.5 | 6.17 | 16.46 | 25.52 | 11.00 | 108.0 | 90.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.2 | 5.14 | 14.78 | 22.85 | 6.00 | 93.0 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.81 | 10.21 | 15.77 | 1.00 | 81.3 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 4.9 | 3.90 | 10.18 | 15.36 | 7.00 | 80.8 | 75.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.0 | 2.97 | 8.52 | 12.90 | 1.00 | 79.6 | 26.0 |
| XI | XI | Aleksandar Mitrović | FWD | 9 | 6.7 | 4.94 | 12.80 | 19.62 | 1.00 | 83.1 | 90.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.2 | 1.23 | 3.87 | 5.46 | 0.00 | 39.5 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.3 | 0.54 | 2.29 | 3.32 | 0.00 | 19.6 | 0.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.2 | 5.83 | 17.00 | 27.43 | 11.00 | 94.9 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.8 | 5.75 | 16.31 | 26.08 | 7.00 | 82.9 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.5 | 5.51 | 13.85 | 20.16 | 12.00 | 97.5 | 85.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.4 | 4.49 | 12.40 | 18.75 | 8.00 | 71.6 | 62.0 |
| XI | XI | Phil Foden | MID | 13 | 8.3 | 3.54 | 11.61 | 17.08 | 1.00 | 45.3 | 13.0 |

## GW15

- Train rows: 86369
- Bank: 2.50 -> 3.80
- Free transfers: 2 -> 2
- Captain: Kevin De Bruyne
- Vice captain: Kieran Trippier
- Effective captain: Kevin De Bruyne
- Chip used: none
- Predicted score: 59.73
- Actual score: 80.00
- Transfer: Phil Foden -> Leandro Trossard (projected gain 6.14, hit 0)
- Autosub: Sam Greenwood replaced Aleksandar Mitrović.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | 10 | 4.1 | 3.36 | 9.56 | 15.49 | 6.00 | 89.5 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 4.9 | 2.65 | 7.68 | 11.95 | 6.00 | 72.1 | 90.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 5.6 | 6.05 | 16.18 | 25.56 | 12.00 | 107.7 | 79.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.2 | 5.94 | 15.65 | 24.46 | -2.00 | 97.1 | 25.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.23 | 9.69 | 15.24 | 2.00 | 81.5 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 4.9 | 3.35 | 9.60 | 15.08 | 8.00 | 73.8 | 90.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.0 | 2.75 | 7.61 | 11.94 | 1.00 | 62.6 | 90.0 |
| XI | Bench | Aleksandar Mitrović | FWD | 9 | 6.7 | 3.49 | 10.65 | 16.87 | 0.00 | 62.7 | 0.0 |
| Bench 3 | Autosub In | Sam Greenwood | FWD | 11 | 4.2 | 0.99 | 2.28 | 3.28 | 9.00 | 19.5 | 36.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.3 | 0.69 | 1.94 | 2.85 | 0.00 | 14.6 | 0.0 |
| Captain | Captain | Kevin De Bruyne | MID | 13 | 12.2 | 6.76 | 18.04 | 29.21 | 7.00 | 99.5 | 90.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.8 | 5.44 | 16.31 | 26.77 | 15.00 | 84.7 | 90.0 |
| XI | XI | Leandro Trossard | MID | 5 | 7.0 | 5.96 | 14.82 | 22.22 | 5.00 | 96.4 | 81.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.4 | 4.46 | 12.96 | 20.40 | 3.00 | 76.0 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.6 | 4.91 | 12.95 | 19.61 | 8.00 | 83.5 | 80.0 |

## GW16

- Train rows: 87030
- Bank: 3.80 -> 1.50
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kevin De Bruyne
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.08
- Actual score: 60.00
- Transfer: Aleksandar Mitrović -> Darwin Núñez Ribeiro (projected gain 6.32, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | 10 | 4.1 | 3.77 | 10.75 | 17.42 | 11.00 | 97.4 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 4.9 | 3.64 | 9.46 | 15.02 | 6.00 | 84.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.6 | 5.79 | 16.37 | 26.09 | 7.00 | 103.3 | 90.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.2 | 4.39 | 12.68 | 21.01 | 1.00 | 65.6 | 85.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 4.70 | 12.13 | 19.44 | 6.00 | 93.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.85 | 10.29 | 16.50 | 2.00 | 84.9 | 90.0 |
| Bench 2 | Bench | Neco Williams | DEF | 16 | 4.0 | 3.28 | 8.70 | 13.77 | 1.00 | 77.7 | 4.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 12 | 9.0 | 4.40 | 11.19 | 17.64 | 13.00 | 69.2 | 86.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.2 | 1.84 | 5.17 | 8.16 | 1.00 | 41.3 | 45.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.44 | 1.33 | 2.23 | 1.00 | 10.9 | 7.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.8 | 7.05 | 19.10 | 31.06 | 2.00 | 103.7 | 90.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.3 | 5.98 | 17.44 | 28.81 | 2.00 | 83.1 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.4 | 5.16 | 13.83 | 22.28 | 6.00 | 86.5 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.6 | 4.55 | 13.18 | 20.49 | 6.00 | 72.4 | 90.0 |
| XI | XI | Leandro Trossard | MID | 5 | 7.0 | 4.39 | 11.95 | 18.49 | 2.00 | 63.3 | 90.0 |

## GW17

- Train rows: 87697
- Bank: 1.50 -> 0.80
- Free transfers: 2 -> 2
- Captain: Kevin De Bruyne
- Vice captain: Mohamed Salah
- Effective captain: Kevin De Bruyne
- Chip used: none
- Predicted score: 61.92
- Actual score: 53.00
- Transfer: Neco Williams -> Timothy Castagne (projected gain 0.74, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | 10 | 4.1 | 4.53 | 12.46 | 19.78 | 1.00 | 110.8 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 4.9 | 3.78 | 9.99 | 15.86 | 3.00 | 86.6 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.6 | 5.23 | 15.61 | 25.46 | 12.00 | 108.0 | 90.0 |
| XI | XI | João Cancelo | DEF | 13 | 7.2 | 4.57 | 12.92 | 21.71 | 1.00 | 72.2 | 22.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 4.27 | 11.65 | 18.59 | 2.00 | 86.9 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 10 | 4.7 | 3.63 | 10.30 | 16.19 | 1.00 | 87.3 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 3.53 | 9.79 | 15.73 | 9.00 | 80.7 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 12 | 9.0 | 5.51 | 14.31 | 22.19 | 2.00 | 86.4 | 87.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.2 | 1.86 | 5.72 | 8.92 | 4.00 | 43.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.59 | 1.93 | 3.25 | 0.00 | 14.5 | 0.0 |
| Captain | Captain | Kevin De Bruyne | MID | 13 | 12.3 | 6.75 | 18.64 | 30.54 | 2.00 | 97.2 | 90.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.8 | 6.27 | 17.84 | 28.76 | 12.00 | 91.2 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.6 | 5.27 | 15.13 | 23.44 | 8.00 | 101.2 | 82.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.4 | 4.91 | 13.55 | 22.21 | 8.00 | 85.1 | 87.0 |
| XI | XI | Leandro Trossard | MID | 5 | 7.0 | 4.23 | 12.04 | 18.98 | 2.00 | 70.5 | 82.0 |

## GW18

- Train rows: 88372
- Bank: 0.80 -> 1.00
- Free transfers: 2 -> 2
- Captain: Kevin De Bruyne
- Vice captain: Mohamed Salah
- Effective captain: Kevin De Bruyne
- Chip used: none
- Predicted score: 53.22
- Actual score: 41.00
- Transfer: Leandro Trossard -> Marcus Rashford (projected gain 2.54, hit 0)
- Autosub: Timothy Castagne replaced João Cancelo.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.1 | 2.26 | 8.94 | 14.52 | 3.00 | 69.0 | 90.0 |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 2.63 | 7.98 | 13.07 | 2.00 | 68.0 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.6 | 5.89 | 16.60 | 26.78 | 8.00 | 92.2 | 90.0 |
| XI | Bench | João Cancelo | DEF | 13 | 7.2 | 4.82 | 10.72 | 18.23 | 0.00 | 33.1 | 0.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 3.66 | 10.07 | 16.48 | 2.00 | 81.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 2.75 | 9.67 | 15.96 | 1.00 | 60.4 | 90.0 |
| Bench 2 | Autosub In | Timothy Castagne | DEF | 10 | 4.7 | 2.01 | 7.70 | 12.56 | 1.00 | 57.9 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 12 | 9.0 | 2.77 | 8.75 | 14.87 | 5.00 | 18.5 | 90.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.2 | 1.80 | 5.29 | 8.53 | 0.00 | 33.4 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.03 | 0.79 | 1.54 | 0.00 | 5.5 | 0.0 |
| Vice Captain | XI | Mohamed Salah | MID | 12 | 12.8 | 5.92 | 16.68 | 27.64 | 2.00 | 65.9 | 90.0 |
| Captain | Captain | Kevin De Bruyne | MID | 13 | 12.3 | 7.48 | 16.36 | 26.59 | 1.00 | 60.4 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.7 | 3.57 | 13.60 | 20.84 | 3.00 | 49.6 | 83.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.4 | 4.16 | 12.60 | 20.88 | 10.00 | 69.6 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 6.8 | 2.08 | 11.07 | 16.77 | 5.00 | 38.1 | 45.0 |

## GW19

- Train rows: 89050
- Bank: 1.00 -> 2.70
- Free transfers: 2 -> 2
- Captain: Mohamed Salah
- Vice captain: Kevin De Bruyne
- Effective captain: Mohamed Salah
- Chip used: none
- Predicted score: 61.70
- Actual score: 41.00
- Transfer: João Cancelo -> Thiago Emiliano da Silva (projected gain 1.08, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Danny Ward | GK | 10 | 4.1 | 4.24 | 10.46 | 17.09 | 2.00 | 97.6 | 90.0 |
| Bench 1 | Bench | Aaron Ramsdale | GK | 1 | 4.9 | 3.33 | 8.70 | 14.20 | 6.00 | 88.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.6 | 5.86 | 16.27 | 26.59 | 8.00 | 112.8 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 4.24 | 10.79 | 17.32 | 7.00 | 91.4 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.03 | 10.32 | 16.84 | 0.00 | 93.3 | 45.0 |
| XI | XI | Thiago Emiliano da Silva | DEF | 6 | 5.4 | 4.55 | 10.08 | 15.51 | 3.00 | 120.5 | 180.0 |
| Bench 2 | Bench | Timothy Castagne | DEF | 10 | 4.7 | 3.91 | 9.10 | 14.57 | 1.00 | 86.4 | 90.0 |
| XI | XI | Darwin Núñez Ribeiro | FWD | 12 | 9.0 | 4.35 | 11.45 | 18.86 | 1.00 | 73.7 | 90.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.2 | 1.84 | 4.58 | 6.97 | 1.00 | 25.5 | 12.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.60 | 1.23 | 2.09 | 0.00 | 7.9 | 0.0 |
| Captain | Captain | Mohamed Salah | MID | 12 | 12.9 | 6.58 | 18.34 | 29.54 | 2.00 | 101.7 | 90.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.2 | 6.01 | 17.07 | 27.77 | 3.00 | 100.8 | 90.0 |
| XI | XI | Gabriel Martinelli Silva | MID | 1 | 6.4 | 5.69 | 14.72 | 23.70 | 3.00 | 102.2 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.7 | 4.94 | 13.79 | 21.93 | 2.00 | 96.6 | 67.0 |
| XI | XI | Marcus Rashford | MID | 14 | 6.8 | 4.64 | 12.45 | 19.88 | 8.00 | 83.8 | 90.0 |

## GW20

- Train rows: 89739
- Bank: 2.70 -> 1.80
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Kevin De Bruyne
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 48.03
- Actual score: 71.00
- Transfer: Gabriel Martinelli Silva -> Wilfried Zaha (projected gain 25.03, hit 0)
- Autosub: Timothy Castagne replaced Virgil van Dijk.
- Autosub: Sam Greenwood replaced Darwin Núñez Ribeiro.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.1 | 2.11 | 14.48 | 16.53 | 2.00 | 50.2 | 90.0 |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 2.85 | 12.67 | 14.10 | 11.00 | 72.9 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | 15 | 5.6 | 5.77 | 18.37 | 26.83 | 9.00 | 96.3 | 90.0 |
| XI | XI | Thiago Emiliano da Silva | DEF | 6 | 5.4 | 3.57 | 16.81 | 18.44 | 8.00 | 84.7 | 90.0 |
| XI | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 1.92 | 14.12 | 14.12 | 0.00 | 33.6 | 0.0 |
| Bench 2 | Autosub In | Timothy Castagne | DEF | 10 | 4.6 | 1.33 | 12.97 | 13.67 | 1.00 | 33.6 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 3.35 | 11.89 | 17.26 | 6.00 | 75.2 | 90.0 |
| Bench 3 | Autosub In | Sam Greenwood | FWD | 11 | 4.2 | 0.23 | 11.36 | 8.02 | 1.00 | 0.0 | 13.0 |
| XI | Bench | Darwin Núñez Ribeiro | FWD | 12 | 8.9 | 0.72 | 7.90 | 15.53 | 0.00 | 5.6 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.00 | 0.00 | 1.54 | 0.00 | 0.0 | 0.0 |
| XI | XI | Wilfried Zaha | MID | 7 | 7.3 | 4.45 | 37.26 | 18.61 | 4.00 | 63.0 | 180.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.2 | 5.56 | 16.49 | 31.19 | 5.00 | 75.8 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.7 | 4.51 | 14.36 | 21.32 | 3.00 | 76.5 | 84.0 |
| XI | XI | Marcus Rashford | MID | 14 | 6.9 | 4.81 | 13.33 | 26.63 | 12.00 | 86.8 | 180.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.9 | 4.73 | 13.24 | 26.66 | 2.00 | 34.1 | 90.0 |

## GW21

- Train rows: 90438
- Bank: 1.80 -> 2.70
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Kevin De Bruyne
- Effective captain: Kieran Trippier
- Chip used: none
- Predicted score: 62.29
- Actual score: 49.00
- Transfer: Darwin Núñez Ribeiro -> Dominic Calvert-Lewin (projected gain 12.03, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.1 | 2.92 | 12.41 | 15.83 | 1.00 | 84.4 | 90.0 |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 3.07 | 6.14 | 15.71 | 1.00 | 89.4 | 90.0 |
| Captain | Captain | Kieran Trippier | DEF | 15 | 5.6 | 8.23 | 18.04 | 27.29 | 8.00 | 110.8 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 10 | 4.6 | 2.47 | 9.46 | 12.52 | 1.00 | 71.6 | 90.0 |
| XI | XI | Thiago Emiliano da Silva | DEF | 6 | 5.4 | 3.76 | 7.00 | 16.12 | 6.00 | 100.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 4.06 | 4.32 | 18.87 | 1.00 | 97.8 | 90.0 |
| Bench 2 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 1.68 | 0.00 | 10.93 | 0.00 | 37.5 | 0.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 8 | 7.9 | 3.31 | 11.72 | 13.87 | 2.00 | 75.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.39 | 0.00 | 1.75 | 0.00 | 5.6 | 0.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.2 | 1.54 | 0.00 | 7.03 | 1.00 | 16.1 | 3.0 |
| XI | XI | Marcus Rashford | MID | 14 | 6.9 | 5.59 | 12.09 | 27.66 | 7.00 | 125.9 | 90.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.2 | 7.75 | 11.65 | 28.15 | 6.00 | 102.5 | 76.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.7 | 5.75 | 9.51 | 20.24 | 3.00 | 92.5 | 85.0 |
| XI | XI | Mohamed Salah | MID | 12 | 12.8 | 5.29 | 5.01 | 26.39 | 3.00 | 89.0 | 90.0 |
| XI | XI | Wilfried Zaha | MID | 7 | 7.3 | 4.80 | 4.99 | 19.66 | 3.00 | 117.1 | 64.0 |

## GW22

- Train rows: 91145
- Bank: 2.70 -> 5.50
- Free transfers: 2 -> 2
- Captain: Bruno Borges Fernandes
- Vice captain: Marcus Rashford
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 65.16
- Actual score: 64.00
- Chip advisory: bench_boost (0.56): Double-gameweek coverage plus usable bench minutes make this a stronger-than-usual Bench Boost spot.
- Transfer: Mohamed Salah -> Bruno Borges Fernandes (projected gain 15.49, hit 0)
- Autosub: Sam Greenwood replaced Wilfried Zaha.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 3.51 | 4.15 | 23.15 | 3.00 | 82.4 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.0 | 3.46 | 1.62 | 22.31 | 2.00 | 84.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.7 | 7.00 | 18.15 | 25.73 | 2.00 | 110.5 | 90.0 |
| XI | XI | Thiago Emiliano da Silva | DEF | 6 | 5.4 | 3.95 | 6.06 | 30.42 | 6.00 | 101.7 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 4.66 | 2.40 | 34.68 | 2.00 | 95.8 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 1.57 | 1.86 | 12.76 | 0.00 | 31.0 | 0.0 |
| XI | XI | Timothy Castagne | DEF | 10 | 4.5 | 2.81 | 0.00 | 25.77 | 0.00 | 74.0 | 90.0 |
| XI | XI | Dominic Calvert-Lewin | FWD | 8 | 7.9 | 2.76 | 6.93 | 18.94 | 2.00 | 74.4 | 61.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.35 | 0.92 | 1.64 | 0.00 | 8.0 | 0.0 |
| Bench 2 | Autosub In | Sam Greenwood | FWD | 11 | 4.1 | 2.69 | 0.00 | 2.20 | 2.00 | 46.5 | 8.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 7.0 | 9.07 | 20.42 | 33.62 | 20.00 | 147.3 | 180.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.2 | 6.35 | 15.55 | 36.82 | 1.00 | 90.0 | 31.0 |
| Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.9 | 9.17 | 15.39 | 37.96 | 12.00 | 152.5 | 180.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.6 | 3.60 | 6.25 | 28.39 | 2.00 | 70.6 | 80.0 |
| XI | Bench | Wilfried Zaha | MID | 7 | 7.2 | 3.09 | 2.29 | 32.73 | 0.00 | 70.9 | 0.0 |

## GW23

- Train rows: 91885
- Bank: 5.50 -> 1.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Marcus Rashford
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 62.57
- Actual score: 72.00
- Chip advisory: triple_captain (0.69): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Dominic Calvert-Lewin -> Erling Haaland (projected gain 15.03, hit 0)
- Autosub: Sam Greenwood replaced Wilfried Zaha.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.0 | 3.71 | 10.25 | 16.13 | 3.00 | 84.1 | 90.0 |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 3.93 | 10.07 | 5.04 | 3.00 | 111.3 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.7 | 5.93 | 21.57 | 22.31 | 2.00 | 106.4 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 5.02 | 12.40 | 6.88 | 3.00 | 118.7 | 180.0 |
| XI | XI | Thiago Emiliano da Silva | DEF | 6 | 5.4 | 3.44 | 10.95 | 0.00 | 2.00 | 84.7 | 90.0 |
| XI | XI | Timothy Castagne | DEF | 10 | 4.5 | 2.72 | 8.12 | 11.96 | 5.00 | 75.3 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 1.35 | 3.35 | 0.00 | 0.00 | 21.5 | 0.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.2 | 9.03 | 22.33 | 38.26 | 10.00 | 158.1 | 135.0 |
| Bench 2 | Autosub In | Sam Greenwood | FWD | 11 | 4.1 | 1.54 | 5.24 | 9.01 | 1.00 | 30.6 | 4.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.00 | 0.66 | 1.18 | 0.00 | 8.7 | 0.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 7.0 | 7.28 | 20.68 | 40.43 | 8.00 | 131.9 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 4.86 | 18.87 | 33.03 | 3.00 | 97.5 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.2 | 5.92 | 17.76 | 25.41 | 15.00 | 103.0 | 176.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.6 | 3.18 | 10.97 | 15.83 | 10.00 | 66.8 | 80.0 |
| XI | Bench | Wilfried Zaha | MID | 7 | 7.2 | 2.20 | 7.52 | 5.97 | 0.00 | 52.9 | 0.0 |

## GW24

- Train rows: 92630
- Bank: 1.20 -> 0.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Kevin De Bruyne
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 68.53
- Actual score: 46.00
- Transfer: Wilfried Zaha -> Bukayo Saka (projected gain 17.19, hit 0)
- Autosub: Sam Greenwood replaced Thiago Emiliano da Silva.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 4.38 | 12.89 | 8.96 | 2.00 | 114.9 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.0 | 3.14 | 9.74 | 0.00 | 2.00 | 80.9 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.7 | 5.81 | 19.81 | 19.37 | 1.00 | 110.3 | 63.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 5.27 | 15.24 | 12.99 | 1.00 | 123.5 | 90.0 |
| XI | Bench | Thiago Emiliano da Silva | DEF | 6 | 5.4 | 3.58 | 10.09 | 0.00 | 0.00 | 83.0 | 0.0 |
| XI | XI | Timothy Castagne | DEF | 10 | 4.4 | 2.25 | 7.94 | 0.00 | 1.00 | 71.9 | 90.0 |
| Bench 3 | Bench | Virgil van Dijk | DEF | 12 | 6.4 | 1.10 | 3.71 | 2.68 | 6.00 | 22.6 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.2 | 9.21 | 21.87 | 2.54 | 2.00 | 148.3 | 90.0 |
| Bench 2 | Autosub In | Sam Greenwood | FWD | 11 | 4.1 | 1.50 | 4.87 | 9.17 | 1.00 | 25.9 | 4.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.11 | 0.66 | 1.04 | 0.00 | 7.3 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.4 | 7.49 | 20.75 | 22.48 | 6.00 | 114.0 | 90.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.2 | 8.30 | 19.59 | 11.47 | 2.00 | 124.7 | 87.0 |
| XI | XI | Marcus Rashford | MID | 14 | 7.0 | 5.38 | 18.07 | 5.18 | 15.00 | 123.1 | 68.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.9 | 4.63 | 16.29 | 19.37 | 12.00 | 94.6 | 90.0 |
| XI | XI | Miguel Almirón Rejala | MID | 15 | 5.5 | 3.03 | 10.59 | 10.74 | 1.00 | 70.3 | 63.0 |

## GW25

- Train rows: 93376
- Bank: 0.00 -> 1.00
- Free transfers: 2 -> 2
- Captain: Bukayo Saka
- Vice captain: Erling Haaland
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 66.15
- Actual score: 91.00
- Chip advisory: triple_captain (0.63): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Thiago Emiliano da Silva -> James Tarkowski (projected gain 5.83, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 4.72 | 11.61 | 19.20 | 13.00 | 121.1 | 180.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.0 | 3.13 | 9.43 | 14.69 | 2.00 | 82.7 | 90.0 |
| XI | Bench | Kieran Trippier | DEF | 15 | 5.7 | 4.75 | 16.22 | 29.18 | 0.00 | 71.9 | 0.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.4 | 6.30 | 13.45 | 20.93 | 0.00 | 121.6 | 180.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 5.25 | 13.25 | 22.41 | 12.00 | 124.0 | 180.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.47 | 9.99 | 15.52 | 24.00 | 93.2 | 180.0 |
| XI | XI | Timothy Castagne | DEF | 10 | 4.4 | 2.52 | 8.02 | 12.63 | 2.00 | 74.8 | 84.0 |
| Vice Captain | XI | Erling Haaland | FWD | 13 | 12.2 | 7.05 | 21.88 | 34.37 | 10.00 | 120.8 | 71.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.1 | 1.90 | 5.32 | 9.26 | 0.00 | 27.5 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.26 | 0.67 | 1.10 | 0.00 | 5.6 | 0.0 |
| Captain | Captain | Bukayo Saka | MID | 1 | 8.4 | 8.06 | 23.50 | 40.54 | 15.00 | 144.9 | 171.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 12.1 | 6.06 | 17.79 | 31.33 | 0.00 | 79.3 | 0.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 9.9 | 4.41 | 16.51 | 32.76 | 0.00 | 73.6 | 0.0 |
| XI | Bench | Marcus Rashford | MID | 14 | 7.0 | 4.50 | 16.21 | 28.01 | 0.00 | 78.4 | 0.0 |
| Bench 2 | Bench | Miguel Almirón Rejala | MID | 15 | 5.5 | 2.19 | 7.93 | 13.42 | 0.00 | 42.9 | 0.0 |

## GW26

- Train rows: 94122
- Bank: 1.00 -> 1.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 60.36
- Actual score: 27.00
- Transfer: Timothy Castagne -> Vitalii Mykolenko (projected gain 3.42, hit 0)
- Autosub: Sam Greenwood replaced Vitalii Mykolenko.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 5.28 | 13.88 | 22.26 | 1.00 | 129.3 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.0 | 3.50 | 9.39 | 15.74 | 11.00 | 84.0 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 6.19 | 16.27 | 26.02 | 1.00 | 137.2 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.37 | 12.52 | 20.88 | 6.00 | 102.1 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.6 | 3.23 | 12.13 | 21.11 | 1.00 | 50.2 | 90.0 |
| XI | Bench | Vitalii Mykolenko | DEF | 8 | 4.3 | 4.29 | 11.32 | 18.04 | 0.00 | 112.0 | 0.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.4 | 3.01 | 9.60 | 15.73 | 0.00 | 81.5 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.2 | 7.82 | 23.20 | 36.62 | 4.00 | 113.9 | 90.0 |
| Bench 2 | Autosub In | Sam Greenwood | FWD | 11 | 4.1 | 0.78 | 2.97 | 5.31 | 1.00 | 13.2 | 10.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.47 | 0.80 | 1.43 | 0.00 | 7.1 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.4 | 7.21 | 21.59 | 35.18 | 2.00 | 123.2 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.1 | 4.82 | 16.07 | 27.85 | 3.00 | 61.3 | 64.0 |
| XI | XI | Marcus Rashford | MID | 14 | 7.0 | 3.87 | 12.91 | 22.96 | 2.00 | 64.7 | 84.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.8 | 2.45 | 10.72 | 21.47 | 2.00 | 42.8 | 90.0 |
| Bench 3 | Bench | Miguel Almirón Rejala | MID | 15 | 5.5 | 0.72 | 4.83 | 8.60 | 2.00 | 24.7 | 76.0 |

## GW27

- Train rows: 94869
- Bank: 1.10 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Kaoru Mitoma
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 59.88
- Actual score: 62.00
- Transfer: Miguel Almirón Rejala -> Kaoru Mitoma (projected gain 5.26, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.0 | 3.38 | 10.06 | 16.30 | 2.00 | 87.0 | 90.0 |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 3.51 | 9.68 | 17.50 | 6.00 | 85.7 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.6 | 5.24 | 14.52 | 23.29 | 5.00 | 87.6 | 90.0 |
| XI | XI | Virgil van Dijk | DEF | 12 | 6.4 | 4.34 | 12.39 | 19.66 | 2.00 | 83.1 | 90.0 |
| XI | XI | William Saliba | DEF | 1 | 5.0 | 4.39 | 12.05 | 21.12 | 7.00 | 90.5 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.3 | 2.86 | 8.78 | 14.01 | 8.00 | 77.7 | 90.0 |
| Bench 2 | Bench | Vitalii Mykolenko | DEF | 8 | 4.3 | 1.91 | 5.76 | 9.33 | 1.00 | 51.2 | 1.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.2 | 7.48 | 21.84 | 36.03 | 6.00 | 110.9 | 90.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.1 | 1.33 | 3.85 | 6.67 | 0.00 | 20.4 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.10 | 0.46 | 0.89 | 0.00 | 5.6 | 0.0 |
| XI | XI | Bukayo Saka | MID | 1 | 8.4 | 5.26 | 15.15 | 26.56 | 3.00 | 78.1 | 71.0 |
| XI | XI | Marcus Rashford | MID | 14 | 7.1 | 5.29 | 15.07 | 26.66 | 3.00 | 86.4 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.0 | 4.61 | 14.74 | 26.09 | 1.00 | 64.5 | 11.0 |
| Vice Captain | XI | Kaoru Mitoma | MID | 5 | 5.5 | 5.77 | 12.38 | 20.00 | 12.00 | 103.4 | 168.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.7 | 3.65 | 12.03 | 24.89 | 3.00 | 71.4 | 90.0 |

## GW28

- Train rows: 95619
- Bank: 1.00 -> 1.50
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bukayo Saka
- Effective captain: Bukayo Saka
- Chip used: none
- Predicted score: 54.15
- Actual score: 47.00
- Transfer: Virgil van Dijk -> Ben Chilwell (projected gain 3.34, hit 0)
- Autosub: Vitalii Mykolenko replaced William Saliba.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 3.82 | 10.06 | 16.32 | 3.00 | 90.1 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.0 | 3.15 | 8.87 | 15.24 | 0.00 | 80.5 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.7 | 5.68 | 15.19 | 24.86 | 2.00 | 98.8 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 6 | 5.9 | 4.92 | 12.69 | 17.67 | 1.00 | 87.3 | 90.0 |
| XI | Bench | William Saliba | DEF | 1 | 5.0 | 4.24 | 11.42 | 18.84 | 0.00 | 88.7 | 0.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.3 | 2.91 | 8.97 | 14.38 | 4.00 | 86.9 | 90.0 |
| Bench 2 | Autosub In | Vitalii Mykolenko | DEF | 8 | 4.2 | 1.29 | 5.45 | 8.63 | 1.00 | 42.8 | 6.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 12.2 | 6.52 | 19.96 | 35.04 | 0.00 | 93.1 | 0.0 |
| Bench 3 | Bench | Sam Greenwood | FWD | 11 | 4.0 | 0.75 | 1.94 | 3.91 | 0.00 | 8.3 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.36 | 0.56 | 1.07 | 0.00 | 4.5 | 0.0 |
| Vice Captain | Captain | Bukayo Saka | MID | 1 | 8.4 | 5.88 | 14.38 | 27.24 | 18.00 | 86.5 | 90.0 |
| XI | Bench | Marcus Rashford | MID | 14 | 7.1 | 4.18 | 13.23 | 23.43 | 0.00 | 69.7 | 0.0 |
| XI | Bench | Kaoru Mitoma | MID | 5 | 5.5 | 3.35 | 11.56 | 17.11 | 0.00 | 61.8 | 0.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 9.7 | 3.38 | 10.50 | 21.34 | 0.00 | 58.7 | 0.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 12.0 | 2.75 | 9.58 | 20.63 | 0.00 | 29.8 | 0.0 |

## GW29

- Train rows: 96370
- Bank: 1.50 -> 0.50
- Free transfers: 2 -> 2
- Captain: Kieran Trippier
- Vice captain: Bukayo Saka
- Effective captain: Kieran Trippier
- Chip used: bench_boost
- Predicted score: 62.10
- Actual score: 89.00
- Chip rationale: Optimizer chose Bench Boost here because the current estimated bench gain (15.42) beats the best remaining Bench Boost opportunity (11.95).
- Chip advisory: triple_captain (0.63): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: Vitalii Mykolenko -> Ben Mee (projected gain 9.28, hit 0)
- Chip used: Bench Boost. Optimizer chose Bench Boost here because the current estimated bench gain (15.42) beats the best remaining Bench Boost opportunity (11.95).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bench 1 | Bench Boost | Aaron Ramsdale | GK | 1 | 4.9 | 3.02 | 9.52 | 14.70 | 3.00 | 79.8 | 90.0 |
| XI | XI | Danny Ward | GK | 10 | 4.0 | 3.36 | 6.87 | 12.29 | 0.00 | 71.0 | 0.0 |
| Captain | Captain | Kieran Trippier | DEF | 15 | 5.7 | 6.54 | 15.91 | 24.80 | 14.00 | 121.7 | 176.0 |
| XI | XI | Ben Mee | DEF | 4 | 5.1 | 4.62 | 11.15 | 17.82 | 3.00 | 113.7 | 180.0 |
| XI | XI | Ben Chilwell | DEF | 6 | 5.9 | 3.63 | 10.98 | 17.26 | 9.00 | 84.1 | 167.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.2 | 2.64 | 6.96 | 12.37 | 2.00 | 72.2 | 90.0 |
| Bench 4 | Bench Boost | William Saliba | DEF | 1 | 4.9 | 1.34 | 5.95 | 10.39 | 0.00 | 30.2 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 12.0 | 3.72 | 11.95 | 22.02 | 0.00 | 32.2 | 0.0 |
| Bench 2 | Bench Boost | Sam Greenwood | FWD | 11 | 4.0 | 1.67 | 2.72 | 4.42 | 0.00 | 36.9 | 0.0 |
| Bench 3 | Bench Boost | Cameron Archer | FWD | 2 | 4.2 | 1.35 | 1.77 | 2.78 | 0.00 | 33.2 | 0.0 |
| Vice Captain | XI | Bukayo Saka | MID | 1 | 8.5 | 5.27 | 15.91 | 24.74 | 1.00 | 80.0 | 30.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.6 | 5.26 | 13.11 | 20.68 | 4.00 | 95.5 | 180.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 5.5 | 5.12 | 13.04 | 18.88 | 14.00 | 95.9 | 180.0 |
| XI | XI | Marcus Rashford | MID | 14 | 7.0 | 4.69 | 12.46 | 20.86 | 12.00 | 84.9 | 180.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.0 | 3.32 | 9.66 | 16.76 | 13.00 | 34.6 | 90.0 |

## GW30

- Train rows: 97124
- Bank: 0.50 -> 4.30
- Free transfers: 2 -> 2
- Captain: Joe Willock
- Vice captain: Kevin De Bruyne
- Effective captain: Joe Willock
- Chip used: none
- Predicted score: 121.68
- Actual score: 41.00
- Transfer: Bukayo Saka -> Joe Willock (projected gain 79.41, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 2.55 | 8.67 | 14.47 | 1.00 | 79.9 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 4.0 | 1.24 | 4.07 | 7.39 | 0.00 | 29.2 | 0.0 |
| XI | XI | Ben Chilwell | DEF | 6 | 5.9 | 10.62 | 46.21 | 61.06 | 0.00 | 142.9 | 22.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.7 | 12.07 | 45.35 | 60.91 | 2.00 | 174.2 | 90.0 |
| XI | XI | Ben Mee | DEF | 4 | 5.1 | 5.12 | 15.09 | 24.12 | 1.00 | 128.0 | 81.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.2 | 3.79 | 14.39 | 20.74 | 1.00 | 90.8 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 4.9 | 0.29 | 3.58 | 8.16 | 0.00 | 16.5 | 0.0 |
| XI | XI | Erling Haaland | FWD | 13 | 12.1 | 5.98 | 16.59 | 27.44 | 12.00 | 68.8 | 68.0 |
| Bench 2 | Bench | Sam Greenwood | FWD | 11 | 4.0 | 0.53 | 1.05 | 1.82 | 0.00 | 1.5 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.22 | 0.35 | 0.89 | 0.00 | 0.2 | 0.0 |
| Captain | Captain | Joe Willock | MID | 15 | 4.7 | 18.95 | 90.02 | 107.64 | 2.00 | 180.0 | 86.0 |
| Vice Captain | XI | Kevin De Bruyne | MID | 13 | 12.0 | 16.20 | 72.27 | 91.57 | 9.00 | 170.6 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 5.5 | 10.94 | 46.45 | 62.00 | 2.00 | 157.6 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 7.0 | 9.22 | 31.64 | 45.68 | 6.00 | 142.9 | 80.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.6 | 7.30 | 26.45 | 37.95 | 3.00 | 116.5 | 90.0 |

## GW31

- Train rows: 97878
- Bank: 4.30 -> 2.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Kieran Trippier
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 46.35
- Actual score: 59.00
- Transfer: Sam Greenwood -> Dominic Solanke (projected gain 66.60, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 2.83 | 9.34 | 16.45 | 1.00 | 85.5 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 3.9 | 0.52 | 3.19 | 5.64 | 0.00 | 22.7 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 5.7 | 5.58 | 38.43 | 66.29 | 1.00 | 97.2 | 90.0 |
| XI | XI | Ben Chilwell | DEF | 6 | 5.9 | 2.30 | 37.03 | 65.16 | 1.00 | 35.2 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.2 | 2.83 | 14.28 | 24.69 | 1.00 | 79.8 | 90.0 |
| XI | XI | Ben Mee | DEF | 4 | 5.1 | 3.14 | 11.31 | 19.88 | 1.00 | 84.4 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 4.8 | 0.52 | 3.03 | 6.85 | 0.00 | 12.5 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 5.5 | 3.09 | 85.64 | 148.17 | 15.00 | 50.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.2 | 6.04 | 17.68 | 30.46 | 12.00 | 78.0 | 45.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.13 | 0.29 | 0.83 | 0.00 | 0.5 | 0.0 |
| XI | XI | Joe Willock | MID | 15 | 4.7 | 2.28 | 75.27 | 131.50 | 2.00 | 35.1 | 67.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.0 | 4.84 | 63.75 | 111.68 | 8.00 | 61.5 | 61.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 5.6 | 3.31 | 37.54 | 65.00 | 2.00 | 63.6 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.6 | 4.06 | 22.91 | 39.32 | 3.00 | 74.1 | 90.0 |
| Bench 2 | Bench | Marcus Rashford | MID | 14 | 7.0 | 1.52 | 19.85 | 36.65 | 0.00 | 20.7 | 0.0 |

## GW32

- Train rows: 98637
- Bank: 2.80 -> 2.90
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Dominic Solanke
- Effective captain: Dominic Solanke
- Chip used: none
- Predicted score: 49.58
- Actual score: 23.00
- Transfer: Ben Mee -> Benjamin White (projected gain 20.32, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 2.79 | 9.29 | 16.45 | 2.00 | 81.5 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 3.9 | 0.93 | 2.59 | 4.77 | 0.00 | 14.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.7 | 5.39 | 34.33 | 62.95 | 2.00 | 100.4 | 69.0 |
| XI | Bench | Ben Chilwell | DEF | 6 | 5.9 | 2.84 | 32.83 | 61.60 | 0.00 | 48.5 | 0.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.0 | 3.61 | 30.84 | 57.71 | 4.00 | 80.1 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.2 | 2.89 | 13.43 | 23.61 | 6.00 | 79.6 | 90.0 |
| Bench 3 | Bench | William Saliba | DEF | 1 | 4.8 | 0.88 | 2.97 | 6.17 | 0.00 | 11.2 | 0.0 |
| Vice Captain | Captain | Dominic Solanke | FWD | 3 | 5.5 | 5.48 | 73.35 | 137.19 | 2.00 | 73.5 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 12.2 | 5.93 | 18.08 | 29.42 | 0.00 | 61.4 | 0.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.00 | 0.02 | 0.18 | 0.00 | 0.0 | 0.0 |
| XI | XI | Joe Willock | MID | 15 | 4.7 | 2.45 | 61.66 | 117.60 | 5.00 | 36.8 | 90.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 12.0 | 4.57 | 52.57 | 99.40 | 0.00 | 47.3 | 0.0 |
| XI | Bench | Kaoru Mitoma | MID | 5 | 5.6 | 3.75 | 33.05 | 60.72 | 0.00 | 62.1 | 0.0 |
| XI | Bench | Bruno Borges Fernandes | MID | 14 | 9.6 | 3.96 | 21.07 | 38.27 | 0.00 | 66.8 | 0.0 |
| Bench 2 | Bench | Marcus Rashford | MID | 14 | 7.0 | 2.01 | 17.70 | 35.71 | 0.00 | 16.2 | 0.0 |

## GW33

- Train rows: 99397
- Bank: 2.90 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Kieran Trippier
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 35.26
- Actual score: 79.00
- Transfer: William Saliba -> Trent Alexander-Arnold (projected gain 9.24, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.9 | 2.20 | 8.46 | 15.36 | 1.00 | 83.4 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 3.9 | 0.77 | 2.39 | 4.21 | 0.00 | 14.8 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 5.7 | 4.13 | 14.25 | 33.79 | 2.00 | 91.7 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 3.38 | 11.50 | 24.13 | 5.00 | 76.8 | 90.0 |
| XI | XI | James Tarkowski | DEF | 8 | 4.2 | 2.66 | 8.50 | 16.07 | 0.00 | 80.5 | 90.0 |
| XI | XI | Benjamin White | DEF | 1 | 5.0 | 1.47 | 8.48 | 25.83 | 0.00 | 77.6 | 90.0 |
| Bench 3 | Bench | Ben Chilwell | DEF | 6 | 5.8 | 0.00 | 3.90 | 19.64 | 1.00 | 26.0 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.2 | 6.68 | 19.30 | 28.80 | 14.00 | 72.1 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 5.5 | 0.53 | 6.76 | 41.59 | 5.00 | 54.3 | 90.0 |
| Bench 2 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.32 | 0.49 | 0.79 | 0.00 | 0.0 | 0.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.0 | 1.78 | 9.79 | 36.98 | 19.00 | 41.4 | 79.0 |
| XI | XI | Marcus Rashford | MID | 14 | 6.9 | 2.06 | 8.00 | 17.18 | 12.00 | 29.8 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.5 | 1.83 | 7.87 | 16.92 | 5.00 | 28.0 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 5.5 | 1.86 | 7.27 | 22.00 | 2.00 | 36.1 | 90.0 |
| Bench 4 | Bench | Joe Willock | MID | 15 | 4.7 | 0.00 | 4.21 | 36.05 | 5.00 | 59.5 | 86.0 |

## GW34

- Train rows: 100158
- Bank: 0.20 -> 0.20
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Kevin De Bruyne
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 74.31
- Actual score: 86.00
- Chip advisory: triple_captain (0.63): Captain projection and fixture volume create a plausible Triple Captain spot.
- Transfer: Benjamin White -> Ben Mee (projected gain 4.34, hit 0)
- Autosub: Ben Chilwell replaced Kevin De Bruyne.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.8 | 2.86 | 8.74 | 14.45 | 3.00 | 78.5 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 3.9 | 0.85 | 2.19 | 3.83 | 0.00 | 11.0 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 6.72 | 14.83 | 24.47 | 11.00 | 121.1 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.7 | 5.86 | 11.67 | 26.71 | 2.00 | 104.0 | 90.0 |
| XI | XI | Ben Mee | DEF | 4 | 5.0 | 3.49 | 9.63 | 15.97 | 2.00 | 80.1 | 90.0 |
| Bench 3 | Bench | James Tarkowski | DEF | 8 | 4.1 | 2.67 | 6.92 | 12.96 | 1.00 | 76.2 | 90.0 |
| Bench 2 | Autosub In | Ben Chilwell | DEF | 6 | 5.7 | 2.82 | 2.37 | 13.79 | 1.00 | 75.7 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.3 | 9.06 | 23.83 | 36.38 | 16.00 | 119.6 | 180.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.00 | 0.35 | 0.64 | 0.00 | 2.2 | 0.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 5.5 | 5.44 | 0.00 | 22.65 | 8.00 | 111.1 | 88.0 |
| XI | XI | Marcus Rashford | MID | 14 | 7.0 | 7.07 | 14.98 | 25.61 | 8.00 | 119.3 | 175.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.4 | 5.71 | 12.88 | 23.39 | 13.00 | 104.5 | 180.0 |
| Vice Captain | Bench | Kevin De Bruyne | MID | 13 | 12.1 | 8.17 | 10.67 | 32.56 | 0.00 | 136.1 | 0.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 5.5 | 5.90 | 8.90 | 21.57 | 4.00 | 112.7 | 124.0 |
| XI | XI | Joe Willock | MID | 15 | 4.7 | 4.96 | 0.00 | 18.24 | 2.00 | 102.8 | 90.0 |

## GW35

- Train rows: 100920
- Bank: 0.20 -> 1.00
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Marcus Rashford
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 58.53
- Actual score: 38.00
- Transfer: Ben Chilwell -> Pervis Estupiñán (projected gain 3.82, hit 0)

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.8 | 2.65 | 8.13 | 13.54 | 10.00 | 79.6 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 3.9 | 0.63 | 1.69 | 2.99 | 0.00 | 7.6 | 0.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.5 | 5.46 | 16.27 | 27.29 | 7.00 | 113.2 | 90.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.7 | 5.27 | 14.96 | 24.72 | 1.00 | 95.2 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 4.9 | 4.73 | 12.39 | 19.62 | 0.00 | 98.3 | 90.0 |
| Bench 2 | Bench | Ben Mee | DEF | 4 | 4.9 | 2.70 | 8.58 | 14.13 | 2.00 | 80.5 | 90.0 |
| Bench 3 | Bench | James Tarkowski | DEF | 8 | 4.1 | 2.34 | 7.12 | 12.47 | 2.00 | 73.9 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.3 | 8.28 | 23.50 | 37.54 | 2.00 | 105.2 | 90.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 5.5 | 3.30 | 9.75 | 16.01 | 2.00 | 66.9 | 89.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.17 | 0.35 | 0.53 | 0.00 | 1.2 | 0.0 |
| Vice Captain | XI | Marcus Rashford | MID | 14 | 7.0 | 5.62 | 16.39 | 24.84 | 2.00 | 89.3 | 90.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.4 | 5.04 | 15.18 | 24.98 | 2.00 | 99.8 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 5.5 | 4.26 | 12.13 | 19.67 | 5.00 | 78.5 | 90.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.1 | 2.80 | 9.95 | 18.59 | 3.00 | 17.7 | 90.0 |
| XI | XI | Joe Willock | MID | 15 | 4.7 | 2.84 | 7.98 | 12.48 | 2.00 | 68.2 | 77.0 |

## GW36

- Train rows: 101683
- Bank: 1.00 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Kieran Trippier
- Effective captain: Erling Haaland
- Chip used: none
- Predicted score: 63.19
- Actual score: 85.00
- Transfer: Joe Willock -> Alexis Mac Allister (projected gain 5.99, hit 0)
- Autosub: Ben Mee replaced Kevin De Bruyne.
- Autosub: James Tarkowski replaced Marcus Rashford.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.8 | 2.83 | 8.23 | 13.55 | 2.00 | 78.4 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 3.8 | 0.22 | 0.96 | 1.67 | 0.00 | 4.0 | 0.0 |
| Vice Captain | XI | Kieran Trippier | DEF | 15 | 5.7 | 6.39 | 16.76 | 27.15 | 11.00 | 128.9 | 180.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.6 | 4.89 | 14.60 | 25.27 | 13.00 | 93.6 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 4.9 | 4.51 | 11.22 | 17.36 | 17.00 | 101.2 | 180.0 |
| Bench 2 | Autosub In | Ben Mee | DEF | 4 | 4.9 | 3.26 | 9.16 | 14.38 | 11.00 | 79.0 | 90.0 |
| Bench 3 | Autosub In | James Tarkowski | DEF | 8 | 4.1 | 1.90 | 6.55 | 11.87 | 1.00 | 76.3 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.3 | 7.72 | 22.83 | 39.57 | 7.00 | 94.6 | 77.0 |
| XI | XI | Dominic Solanke | FWD | 3 | 5.6 | 3.31 | 9.59 | 15.52 | 2.00 | 70.2 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.06 | 0.22 | 0.59 | 0.00 | 2.3 | 0.0 |
| XI | XI | Alexis Mac Allister | MID | 5 | 5.6 | 5.90 | 14.94 | 23.05 | 3.00 | 124.5 | 124.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 12.1 | 4.83 | 14.73 | 24.31 | 0.00 | 68.7 | 0.0 |
| XI | XI | Bruno Borges Fernandes | MID | 14 | 9.4 | 4.94 | 14.31 | 22.62 | 6.00 | 90.5 | 90.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 5.5 | 5.46 | 13.76 | 21.38 | 5.00 | 110.9 | 180.0 |
| XI | Bench | Marcus Rashford | MID | 14 | 7.0 | 4.68 | 13.67 | 21.29 | 0.00 | 75.2 | 0.0 |

## GW37

- Train rows: 102448
- Bank: 0.10 -> 0.10
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Erling Haaland
- Chip used: triple_captain
- Predicted score: 81.19
- Actual score: 69.00
- Chip rationale: Optimizer chose Triple Captain here because the current estimated captain upside (14.57) beats the best remaining Triple Captain opportunity (6.62).
- Chip advisory: triple_captain (0.66): The captain has a double-gameweek profile and a clear projection edge over the rest of the XI.
- Transfer: none
- No transfer was applied this week.
- Chip used: Triple Captain on Erling Haaland. Optimizer chose Triple Captain here because the current estimated captain upside (14.57) beats the best remaining Triple Captain opportunity (6.62).

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.8 | 2.80 | 8.04 | 13.12 | 2.00 | 77.3 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 3.8 | 0.02 | 0.63 | 1.26 | 0.00 | 3.4 | 0.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 4.9 | 6.96 | 17.70 | 27.00 | 4.00 | 157.4 | 180.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.7 | 5.79 | 16.71 | 27.05 | 9.00 | 114.5 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.6 | 5.21 | 15.20 | 24.95 | 1.00 | 102.4 | 90.0 |
| XI | XI | Ben Mee | DEF | 4 | 4.9 | 3.08 | 9.30 | 15.39 | 2.00 | 77.1 | 90.0 |
| Bench 3 | Bench | James Tarkowski | DEF | 8 | 4.1 | 2.45 | 7.20 | 12.00 | 2.00 | 75.2 | 90.0 |
| Captain | Captain | Erling Haaland | FWD | 13 | 12.3 | 9.62 | 24.94 | 39.21 | 6.00 | 135.1 | 106.0 |
| Bench 2 | Bench | Dominic Solanke | FWD | 3 | 5.6 | 2.77 | 8.48 | 14.22 | 2.00 | 71.3 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.00 | 0.00 | 0.26 | 0.00 | 2.2 | 0.0 |
| Vice Captain | XI | Bruno Borges Fernandes | MID | 14 | 9.5 | 7.29 | 17.94 | 28.46 | 11.00 | 137.0 | 175.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 5.6 | 6.55 | 16.90 | 26.01 | 7.00 | 143.6 | 178.0 |
| XI | XI | Alexis Mac Allister | MID | 5 | 5.6 | 5.59 | 15.12 | 23.16 | 6.00 | 115.0 | 128.0 |
| XI | XI | Kevin De Bruyne | MID | 13 | 12.1 | 5.10 | 13.32 | 22.00 | 2.00 | 68.7 | 68.0 |
| XI | XI | Marcus Rashford | MID | 14 | 7.0 | 3.96 | 10.29 | 17.75 | 7.00 | 61.3 | 61.0 |

## GW38

- Train rows: 103223
- Bank: 0.10 -> 0.80
- Free transfers: 2 -> 2
- Captain: Erling Haaland
- Vice captain: Bruno Borges Fernandes
- Effective captain: Bruno Borges Fernandes
- Chip used: none
- Predicted score: 58.70
- Actual score: 47.00
- Transfer: Ben Mee -> Victor Lindelöf (projected gain 2.41, hit 0)
- Autosub: James Tarkowski replaced Kevin De Bruyne.
- Autosub: Dominic Solanke replaced Erling Haaland.

| Selected Role | Realized Role | Player | Pos | Team | Price | Pred 1GW | Pred 3GW | Pred 5GW | Actual 1GW | Pred Min | Actual Min |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| XI | XI | Aaron Ramsdale | GK | 1 | 4.8 | 2.94 | 8.32 | 13.31 | 6.00 | 80.5 | 90.0 |
| Bench 1 | Bench | Danny Ward | GK | 10 | 3.8 | 0.52 | 1.26 | 2.10 | 0.00 | 4.7 | 0.0 |
| XI | XI | Kieran Trippier | DEF | 15 | 5.6 | 5.52 | 15.87 | 26.41 | 0.00 | 102.1 | 90.0 |
| XI | XI | Trent Alexander-Arnold | DEF | 12 | 7.6 | 5.24 | 15.43 | 24.89 | 4.00 | 94.4 | 90.0 |
| XI | XI | Pervis Estupiñán | DEF | 5 | 4.9 | 4.78 | 14.89 | 23.36 | 1.00 | 115.5 | 45.0 |
| XI | XI | Victor Lindelöf | DEF | 14 | 4.1 | 4.01 | 10.88 | 16.37 | 2.00 | 105.0 | 90.0 |
| Bench 2 | Autosub In | James Tarkowski | DEF | 8 | 4.1 | 3.19 | 8.53 | 12.85 | 8.00 | 78.2 | 90.0 |
| Captain | Bench | Erling Haaland | FWD | 13 | 12.3 | 6.02 | 20.75 | 34.90 | 0.00 | 82.2 | 0.0 |
| Bench 3 | Autosub In | Dominic Solanke | FWD | 3 | 5.5 | 2.93 | 8.33 | 13.74 | 1.00 | 69.9 | 90.0 |
| Bench 4 | Bench | Cameron Archer | FWD | 2 | 4.2 | 0.00 | 0.17 | 0.27 | 0.00 | 2.0 | 0.0 |
| Vice Captain | Captain | Bruno Borges Fernandes | MID | 14 | 9.5 | 5.96 | 17.46 | 28.01 | 10.00 | 97.0 | 83.0 |
| XI | XI | Kaoru Mitoma | MID | 5 | 5.6 | 5.51 | 15.90 | 23.81 | 1.00 | 104.3 | 25.0 |
| XI | Bench | Kevin De Bruyne | MID | 13 | 12.0 | 4.46 | 14.77 | 24.68 | 0.00 | 67.7 | 0.0 |
| XI | XI | Alexis Mac Allister | MID | 5 | 5.6 | 4.09 | 12.95 | 20.64 | 2.00 | 82.1 | 90.0 |
| XI | XI | Marcus Rashford | MID | 14 | 7.0 | 4.14 | 11.91 | 20.54 | 2.00 | 51.9 | 76.0 |