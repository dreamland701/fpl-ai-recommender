# LLM Transfer-Choice Evaluation

- Total eval examples: 19
- Matched predictions: 19
- Valid JSON predictions: 4
- Option accuracy: 0.2105
- Avg predicted-option actual score: 10.3684
- Avg target-option actual score: 51.6842
- Avg score gap vs target: -41.3158

## Notes

- This evaluator scores selected transfer options against outcome-labeled candidate choices.
- Target options are the best realized weekly choices among the legal candidate set exported for each pre-deadline week.

## Weekly Results

| Week | Found | JSON | Match | Pred Opt | Target Opt | Pred Score | Target Score | Gap |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 2025-26 GW12 | True | True | True | 0 | 0 | 31.00 | 31.00 | 0.00 |
| 2025-26 GW13 | True | False | False |  | 1 | 0.00 | 22.00 | -22.00 |
| 2025-26 GW14 | True | False | False |  | 1 | 0.00 | 37.00 | -37.00 |
| 2025-26 GW15 | True | False | False |  | 1 | 0.00 | 57.00 | -57.00 |
| 2025-26 GW16 | True | False | False |  | 1 | 0.00 | 57.00 | -57.00 |
| 2025-26 GW17 | True | False | False |  | 1 | 0.00 | 54.00 | -54.00 |
| 2025-26 GW18 | True | True | True | 1 | 1 | 38.00 | 38.00 | 0.00 |
| 2025-26 GW19 | True | False | False |  | 0 | 0.00 | 37.00 | -37.00 |
| 2025-26 GW20 | True | False | False |  | 1 | 0.00 | 51.00 | -51.00 |
| 2025-26 GW21 | True | True | True | 1 | 1 | 63.00 | 63.00 | 0.00 |
| 2025-26 GW22 | True | False | False |  | 1 | 0.00 | 33.00 | -33.00 |
| 2025-26 GW23 | True | False | False |  | 0 | 0.00 | 54.00 | -54.00 |
| 2025-26 GW24 | True | False | False |  | 0 | 0.00 | 60.00 | -60.00 |
| 2025-26 GW25 | True | False | False |  | 0 | 0.00 | 77.00 | -77.00 |
| 2025-26 GW26 | True | False | False |  | 1 | 0.00 | 86.00 | -86.00 |
| 2025-26 GW27 | True | False | False |  | 0 | 0.00 | 56.00 | -56.00 |
| 2025-26 GW28 | True | True | True | 1 | 1 | 65.00 | 65.00 | 0.00 |
| 2025-26 GW29 | True | False | False |  | 0 | 0.00 | 61.00 | -61.00 |
| 2025-26 GW30 | True | False | False |  | 1 | 0.00 | 43.00 | -43.00 |