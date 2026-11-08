# LLM Decision Evaluation

- Total eval examples: 20
- Matched predictions: 20
- Valid JSON predictions: 4
- Captain accuracy: 0.2000
- Vice-captain accuracy: 0.1000
- Chip accuracy: 0.9000
- Transfer exact-match rate: 0.0500
- Starters Jaccard mean: 0.1833
- Bench-slot accuracy mean: 0.0250
- Avg predicted-policy actual score: 6.4500
- Avg target-policy actual score: 51.7500
- Avg score gap vs target: -45.3000

## Notes

- This evaluator scores strict JSON action bundles week by week.
- Actual-score reconstruction uses the prompt/example metadata, including actual points and minutes for current-squad and shortlist players.
- The score comparison is against the structured backtest policy stored in the training example metadata.

## Weekly Results

| Week | Found | JSON | Captain | Vice | Chip | Transfers | Starters Jaccard | Bench Acc | Pred Score | Target Score | Gap |
| --- | --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 2025-26 GW11 | True | True | True | False | True | True | 1.0000 | 0.0000 | 29.00 | 31.00 | -2.00 |
| 2025-26 GW12 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 39.00 | -39.00 |
| 2025-26 GW13 | True | True | True | False | True | False | 0.8333 | 0.0000 | 25.00 | 23.00 | 2.00 |
| 2025-26 GW14 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 47.00 | -47.00 |
| 2025-26 GW15 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 63.00 | -63.00 |
| 2025-26 GW16 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 57.00 | -57.00 |
| 2025-26 GW17 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 54.00 | -54.00 |
| 2025-26 GW18 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 51.00 | -51.00 |
| 2025-26 GW19 | True | True | True | True | True | False | 1.0000 | 0.2500 | 28.00 | 39.00 | -11.00 |
| 2025-26 GW20 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 51.00 | -51.00 |
| 2025-26 GW21 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 63.00 | -63.00 |
| 2025-26 GW22 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 33.00 | -33.00 |
| 2025-26 GW23 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 50.00 | -50.00 |
| 2025-26 GW24 | True | True | True | True | True | False | 0.8333 | 0.2500 | 47.00 | 55.00 | -8.00 |
| 2025-26 GW25 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 69.00 | -69.00 |
| 2025-26 GW26 | True | False | False | False | False | False | 0.0000 | 0.0000 | 0.00 | 86.00 | -86.00 |
| 2025-26 GW27 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 53.00 | -53.00 |
| 2025-26 GW28 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 66.00 | -66.00 |
| 2025-26 GW29 | True | False | False | False | True | False | 0.0000 | 0.0000 | 0.00 | 62.00 | -62.00 |
| 2025-26 GW30 | True | False | False | False | False | False | 0.0000 | 0.0000 | 0.00 | 43.00 | -43.00 |