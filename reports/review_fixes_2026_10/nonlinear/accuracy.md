# Ridge (current classic) vs gradient-boosted trees, 84 walk-forward weeks

- 1GW (n 65505): ridge: RMSE 1.983, MAE 1.021, bias +0.01, top-decile bias -0.15 | hgb: RMSE 1.929, MAE 0.952, bias -0.02, top-decile bias +0.02
- 3GW (n 63824): ridge: RMSE 4.048, MAE 2.380, bias -0.02, top-decile bias +0.01 | hgb: RMSE 3.956, MAE 2.245, bias +0.00, top-decile bias +0.46
- 5GW (n 60494): ridge: RMSE 5.926, MAE 3.648, bias -0.03, top-decile bias +0.13 | hgb: RMSE 5.801, MAE 3.416, bias -0.01, top-decile bias +0.84
- Appearance AUC: ridge 0.923 | hgb 0.948

Calibration by ridge-forecast decile (1GW): mean forecast vs mean actual

| Decile | Ridge forecast | Trees forecast | Actual |
|---|---|---|---|
| 1 | nan | nan | nan |
| 2 | 0.00 | 0.05 | 0.04 |
| 3 | 0.10 | 0.08 | 0.07 |
| 4 | 0.22 | 0.12 | 0.09 |
| 5 | 0.40 | 0.25 | 0.24 |
| 6 | 0.76 | 0.64 | 0.62 |
| 7 | 1.35 | 1.22 | 1.32 |
| 8 | 2.02 | 2.00 | 2.03 |
| 9 | 2.64 | 2.75 | 2.79 |
| 10 | 3.83 | 3.89 | 3.97 |

price >= 10 (premiums): n 501 | ridge bias -0.01 | trees bias -0.13

price 7.5-10: n 1470 | ridge bias -0.18 | trees bias -0.22
