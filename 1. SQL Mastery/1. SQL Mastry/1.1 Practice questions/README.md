# SQL practice questions

This folder tracks the restart of all 205 PNP SQL questions and the Bosscoder SQL assignment reattempts.

Save one file per verified solution, immediately after the question is complete. Use `PNP-<source-id>.md` or `Bosscoder-<source-id>.md` and include the source question ID, topic, difficulty, final SQL, and the checks used to verify it. Use the same topic and difficulty labels in the study session and here.

Practice topics in the original Bosscoder assignment order. Within each topic, practice PNP questions from Easy to Medium to Hard. Reattempt matching Bosscoder assignments after dinner. Count each PNP source ID once toward the 205-question restart and track Bosscoder separately.

Copy the full question exactly as presented in the study chat, including requirements, sample input, expected output, and the sample explanation. Apply this to every PNP and Bosscoder write-up. Keep the learner solution, walkthrough, and official answer below the complete prompt.

### Walkthrough format

Use the same step-by-step approach during practice and in each PNP or Bosscoder write-up. Identify what one output row represents, then build the query one part at a time using the same example. For each step, explain what to do and why, show the SQL and output, and explain what the output demonstrates. When a join is used, explain why it fits and which unmatched rows it keeps. Explain whether each condition affects input rows, output groups, or one metric.

Preserve the official answer as supplied and add separate SQLite and SQL Server adaptations. Note dialect changes and verify executable versions when the engine is available.

## Practice question index

### SQL Basics

| ID | Question | Set | Difficulty |
| --- | --- | --- | --- |
| P001 | [Brand directory](SQL%20Basics/easy/PNP-P001.md) | PNP | ![EASY](../_badges/easy.svg) |
| P002 | [Ten highest-priced products](SQL%20Basics/easy/PNP-P002.md) | PNP | ![EASY](../_badges/easy.svg) |
| P003 | [Customers in metro cities](SQL%20Basics/easy/PNP-P003.md) | PNP | ![EASY](../_badges/easy.svg) |
| P004 | [Customer emails that cannot be delivered](SQL%20Basics/easy/PNP-P004.md) | PNP | ![EASY](../_badges/easy.svg) |
| P005 | [Orders placed in Q1 2025](SQL%20Basics/easy/PNP-P005.md) | PNP | ![EASY](../_badges/easy.svg) |
| P006 | [Most expensive products sold at full price](SQL%20Basics/easy/PNP-P006.md) | PNP | ![EASY](../_badges/easy.svg) |
| P007 | [Discount amount and percentage per product](SQL%20Basics/easy/PNP-P007.md) | PNP | ![EASY](../_badges/easy.svg) |
| P008 | [Price band labels](SQL%20Basics/easy/PNP-P008.md) | PNP | ![EASY](../_badges/easy.svg) |
| P009 | [Check how Active and Allowed are encoded](SQL%20Basics/easy/PNP-P009.md) | PNP | ![EASY](../_badges/easy.svg) |
| P010 | [Headline order KPIs](SQL%20Basics/easy/PNP-P010.md) | PNP | ![EASY](../_badges/easy.svg) |

### Aggregation

| ID | Question | Set | Difficulty |
| --- | --- | --- | --- |
| P011 | [How much of the catalogue has ever sold?](Aggregation/easy/PNP-P011.md) | PNP | ![EASY](../_badges/easy.svg) |
| P012 | [Price and discount statistics per category](Aggregation/easy/PNP-P012.md) | PNP | ![EASY](../_badges/easy.svg) |

### Sorting and Grouping

| ID | Question | Set | Difficulty |
| --- | --- | --- | --- |
| P013 | [States with at least five customers](Sorting%20and%20Grouping/easy/PNP-P013.md) | PNP | ![EASY](../_badges/easy.svg) |
| P014 | [Orders per month in 2025](Sorting%20and%20Grouping/easy/PNP-P014.md) | PNP | ![EASY](../_badges/easy.svg) |

### Joins

| ID | Question | Set | Difficulty |
| --- | --- | --- | --- |
| P015 | [Product count for every category](Joins/easy/PNP-P015.md) | PNP | ![EASY](../_badges/easy.svg) |
| P016 | [December 2025 orders with customer names](Joins/easy/PNP-P016.md) | PNP | ![EASY](../_badges/easy.svg) |

Add each verified question to its topic, in difficulty order (Easy, Medium, Hard), then by source ID within each difficulty. Use the set column to distinguish PNP practice from Bosscoder reattempts.

## Difficulty rubric

| Rating | Criteria |
| --- | --- |
| ![EASY](../_badges/easy.svg) | One core SQL concept, a direct query, and straightforward output rules. |
| ![MEDIUM](../_badges/medium.svg) | Combines concepts or requires careful reasoning about joins, grouping, query stages, or common edge cases. |
| ![HARD](../_badges/hard.svg) | Requires several dependent steps, advanced SQL patterns, or subtle handling of row grain, ties, NULLs, duplicates, or boundaries. |

Rate the reasoning required for a correct solution based on the question and its edge cases. Time spent and query length alone do not determine difficulty.
