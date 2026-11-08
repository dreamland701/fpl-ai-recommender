# Classic ridge with vs without ['out_weeks_3', 'out_weeks_5', 'return_known', 'unknown_return'], 84 walk-forward weeks

- 1GW (n 65505): base: RMSE 1.9491, MAE 0.9972, bias +0.011, top-decile actual 4.053 | mkt: RMSE 1.9475, MAE 0.9945, bias +0.010, top-decile actual 4.055
- 3GW (n 63824): base: RMSE 4.0189, MAE 2.3854, bias +0.031, top-decile actual 11.005 | mkt: RMSE 4.0154, MAE 2.3853, bias +0.040, top-decile actual 11.013
- 5GW (n 60494): base: RMSE 5.8840, MAE 3.6511, bias +0.045, top-decile actual 17.685 | mkt: RMSE 5.8738, MAE 3.6524, bias +0.074, top-decile actual 17.693
- Appearance AUC: base 0.9356 | mkt 0.9365
- 1GW GK+DEF (n 28754): RMSE base 1.8431 | mkt 1.8418
- 1GW MID+FWD (n 36491): RMSE base 1.9658 | mkt 1.9640
- 1GW price >= 10 (n 501): RMSE base 4.6445 | mkt 4.6392
- 1GW minutes_avg high (played 60+ this week) (n 16956): RMSE base 3.3846 | mkt 3.3830
- 1GW RMSE: market model better in 72/84 weeks

GK/DEF who played 60+, by market clean-sheet probability tercile: mean forecast (base / mkt) vs actual

| tercile | n | cs prob | base | mkt | actual |
|---|---|---|---|---|---|
| 1 | 0 | nan | nan | nan | nan |
| 2 | 0 | nan | nan | nan | nan |
| 3 | 8093 | 0.00 | 2.43 | 2.43 | 3.31 |

Mean standardized 1GW ridge coefficient of each market column across the 84 fits:

- out_weeks_3: -0.2066
- out_weeks_5: +0.2682
- return_known: -0.0769
- unknown_return: -0.0547
