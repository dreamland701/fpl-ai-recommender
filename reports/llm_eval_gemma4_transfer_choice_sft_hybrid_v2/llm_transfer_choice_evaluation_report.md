# LLM Transfer-Choice Evaluation

- Total eval examples: 19
- Matched predictions: 19
- Valid JSON predictions: 19
- Option accuracy: 0.7368
- Avg predicted-option actual score: 50.2632
- Avg target-option actual score: 51.6842
- Avg score gap vs target: -1.4211

## Notes

- This evaluator scores selected transfer options against outcome-labeled candidate choices.
- Target options are the best realized weekly choices among the legal candidate set exported for each pre-deadline week.

## Weekly Results

| Week | Found | JSON | Match | Pred Opt | Target Opt | Pred Score | Target Score | Gap |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 2025-26 GW12 | True | True | True | 0 | 0 | 31.00 | 31.00 | 0.00 |
| 2025-26 GW13 | True | True | True | 1 | 1 | 22.00 | 22.00 | 0.00 |
| 2025-26 GW14 | True | True | True | 1 | 1 | 37.00 | 37.00 | 0.00 |
| 2025-26 GW15 | True | True | True | 1 | 1 | 57.00 | 57.00 | 0.00 |
| 2025-26 GW16 | True | True | True | 1 | 1 | 57.00 | 57.00 | 0.00 |
| 2025-26 GW17 | True | True | True | 1 | 1 | 54.00 | 54.00 | 0.00 |
| 2025-26 GW18 | True | True | True | 1 | 1 | 38.00 | 38.00 | 0.00 |
| 2025-26 GW19 | True | True | False | 1 | 0 | 30.00 | 37.00 | -7.00 |
| 2025-26 GW20 | True | True | True | 1 | 1 | 51.00 | 51.00 | 0.00 |
| 2025-26 GW21 | True | True | True | 1 | 1 | 63.00 | 63.00 | 0.00 |
| 2025-26 GW22 | True | True | True | 1 | 1 | 33.00 | 33.00 | 0.00 |
| 2025-26 GW23 | True | True | False | 1 | 0 | 50.00 | 54.00 | -4.00 |
| 2025-26 GW24 | True | True | False | 1 | 0 | 55.00 | 60.00 | -5.00 |
| 2025-26 GW25 | True | True | False | 1 | 0 | 69.00 | 77.00 | -8.00 |
| 2025-26 GW26 | True | True | True | 1 | 1 | 86.00 | 86.00 | 0.00 |
| 2025-26 GW27 | True | True | False | 1 | 0 | 53.00 | 56.00 | -3.00 |
| 2025-26 GW28 | True | True | True | 1 | 1 | 65.00 | 65.00 | 0.00 |
| 2025-26 GW29 | True | True | True | 0 | 0 | 61.00 | 61.00 | 0.00 |
| 2025-26 GW30 | True | True | True | 1 | 1 | 43.00 | 43.00 | 0.00 |