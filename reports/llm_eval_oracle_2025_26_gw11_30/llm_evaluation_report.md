# LLM Decision Evaluation

- Total eval examples: 20
- Matched predictions: 20
- Valid JSON predictions: 20
- Captain accuracy: 1.0000
- Vice-captain accuracy: 1.0000
- Chip accuracy: 1.0000
- Transfer exact-match rate: 1.0000
- Starters Jaccard mean: 1.0000
- Bench-slot accuracy mean: 1.0000
- Avg predicted-policy actual score: 49.2000
- Avg target-policy actual score: 51.7500
- Avg score gap vs target: -2.5500

## Notes

- This evaluator scores strict JSON action bundles week by week.
- Actual-score reconstruction uses the prompt/example metadata, including actual points and minutes for current-squad and shortlist players.
- The score comparison is against the structured backtest policy stored in the training example metadata.

## Weekly Results

| Week | Found | JSON | Captain | Vice | Chip | Transfers | Starters Jaccard | Bench Acc | Pred Score | Target Score | Gap |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 2025-26 GW11 | True | True | True | True | True | True | 1.0000 | 1.0000 | 29.00 | 31.00 | -2.00 |
| 2025-26 GW12 | True | True | True | True | True | True | 1.0000 | 1.0000 | 31.00 | 39.00 | -8.00 |
| 2025-26 GW13 | True | True | True | True | True | True | 1.0000 | 1.0000 | 22.00 | 23.00 | -1.00 |
| 2025-26 GW14 | True | True | True | True | True | True | 1.0000 | 1.0000 | 37.00 | 47.00 | -10.00 |
| 2025-26 GW15 | True | True | True | True | True | True | 1.0000 | 1.0000 | 57.00 | 63.00 | -6.00 |
| 2025-26 GW16 | True | True | True | True | True | True | 1.0000 | 1.0000 | 57.00 | 57.00 | 0.00 |
| 2025-26 GW17 | True | True | True | True | True | True | 1.0000 | 1.0000 | 54.00 | 54.00 | 0.00 |
| 2025-26 GW18 | True | True | True | True | True | True | 1.0000 | 1.0000 | 38.00 | 51.00 | -13.00 |
| 2025-26 GW19 | True | True | True | True | True | True | 1.0000 | 1.0000 | 30.00 | 39.00 | -9.00 |
| 2025-26 GW20 | True | True | True | True | True | True | 1.0000 | 1.0000 | 51.00 | 51.00 | 0.00 |
| 2025-26 GW21 | True | True | True | True | True | True | 1.0000 | 1.0000 | 63.00 | 63.00 | 0.00 |
| 2025-26 GW22 | True | True | True | True | True | True | 1.0000 | 1.0000 | 33.00 | 33.00 | 0.00 |
| 2025-26 GW23 | True | True | True | True | True | True | 1.0000 | 1.0000 | 50.00 | 50.00 | 0.00 |
| 2025-26 GW24 | True | True | True | True | True | True | 1.0000 | 1.0000 | 55.00 | 55.00 | 0.00 |
| 2025-26 GW25 | True | True | True | True | True | True | 1.0000 | 1.0000 | 69.00 | 69.00 | 0.00 |
| 2025-26 GW26 | True | True | True | True | True | True | 1.0000 | 1.0000 | 86.00 | 86.00 | 0.00 |
| 2025-26 GW27 | True | True | True | True | True | True | 1.0000 | 1.0000 | 53.00 | 53.00 | 0.00 |
| 2025-26 GW28 | True | True | True | True | True | True | 1.0000 | 1.0000 | 65.00 | 66.00 | -1.00 |
| 2025-26 GW29 | True | True | True | True | True | True | 1.0000 | 1.0000 | 61.00 | 62.00 | -1.00 |
| 2025-26 GW30 | True | True | True | True | True | True | 1.0000 | 1.0000 | 43.00 | 43.00 | 0.00 |