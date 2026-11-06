# PNP P003 — Customers in metro cities (Day 1 independent SQL reattempt 3)

**Date:** November 6, 2026 (Asia/Kolkata) · **Status:** Not attempted in this session.  
**Origin:** PNP P003, previously solved on October 27, 2026; this is a *source reattempt*, not a new source completion.  
**Existing source file with earlier solutions (DO NOT OPEN until after your own attempt):** [PNP P003 source record](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/1.%20Intro%20to%20SQL%20and%20Advanced%20Select/P003.%20Customers%20in%20metro%20cities.md).

## Independent problem summary (no solution spoilers)

A delivery launch team wants a customer list for the five metro areas Bengaluru, Mumbai, Delhi, Hyderabad and Chennai. Select customers whose entered city belongs to one of those metro areas **ignoring capitalization and extra spaces around the name**.

The provided dataset recognizes alternative spellings `Bangalore` for Bengaluru, `Bombay` for Mumbai, and `New Delhi` for Delhi. Treat these as valid matches too.

Return exactly `CustomerID`, `FirstName`, `LastName`, `City`, `State`, in that order. Display `City` with only the *surrounding spaces removed*, preserving its original letter case. Order by **city name alphabetically without case affecting the comparison**, then by `CustomerID` ascending for ties. Do not change spelling variants in displayed output.

## Sample input — Customers

Illustrative nine-row sample from the existing P003 source record, not the full commerce dataset.

| CustomerID | FirstName | LastName | City (literal text) | State |
|---:|---|---|---|---|
| 12 | Asha | Rao | `' Bengaluru '` | Karnataka |
| 5 | Nisha | Shah | `'MUMBAI'` | Maharashtra |
| 21 | Riya | Patil | `'Pune'` | Maharashtra |
| 3 | Dev | Kumar | `'Delhi'` | Delhi |
| 7 | Mira | Das | `'Bengaluru'` | Karnataka |
| 9 | Farah | Ali | `' Chennai '` | Tamil Nadu |
| 14 | Isha | Kumar | `'Bangalore'` | Karnataka |
| 6 | Omar | Khan | `' Bombay '` | Maharashtra |
| 8 | Lea | Singh | `'New Delhi'` | Delhi |

## Expected output

| CustomerID | FirstName | LastName | City | State |
|---:|---|---|---|---|
| 14 | Isha | Kumar | Bangalore | Karnataka |
| 7 | Mira | Das | Bengaluru | Karnataka |
| 12 | Asha | Rao | Bengaluru | Karnataka |
| 6 | Omar | Khan | Bombay | Maharashtra |
| 9 | Farah | Ali | Chennai | Tamil Nadu |
| 3 | Dev | Kumar | Delhi | Delhi |
| 5 | Nisha | Shah | MUMBAI | Maharashtra |
| 8 | Lea | Singh | New Delhi | Delhi |

## Expected output explanation (no SQL)

- **Isha (14)**: `Bangalore` is an accepted alternative spelling for Bengaluru, so she is included. Alphabetically, `Bangalore` sorts ahead of `Bengaluru`.
- **Mira (7)** and **Asha (12)**: Both are in Bengaluru. Asha's surrounding spaces are removed for display; their cities then tie, so CustomerID 7 appears before 12.
- **Omar (6)**: `' Bombay '` names Mumbai; surrounding spaces are removed and `Bombay` is displayed as entered.
- **Farah (9)**: `' Chennai '` becomes `Chennai` and is included.
- **Dev (3)**: Delhi is a target metro; his record is included.
- **Nisha (5)**: `MUMBAI` matches Mumbai regardless of letter case, while retaining uppercase in the output.
- **Lea (8)**: `New Delhi` is an accepted alternative for Delhi and is included.
- **Riya (21)**: Pune is not among the five metro areas, so she is excluded.

Eight customer rows are expected in exact five-column order; output city values are trimmed but not renamed or recased. Different original city spellings are kept distinct in display/sorting.

## Learner solution and review — pending

- Step 1 reasoning: Pending.
- Learner's original SQLite code and all subsequent versions (verbatim): Not yet submitted.
- Actual SQLite results and errors: Not yet executed.
- Assistant-reviewed SQLite reference: **Withheld until independent learner attempt.**
- Assistant-converted SQL Server/T-SQL reference: **Withheld until after the attempt.**
- Original source provider answer: Stored in P003 source record, **not reproduced now**.
- Learner's optional new-learning Yes/No: Pending.
- Question-closing commits in both repositories: Pending.
- Newly credited PNP source completion: None (P003 was already included in the 20-question baseline).

## Mirrored record links

[Journey P003 reattempt](https://github.com/MulikShrikantDattatray14/data-engineering-journey/blob/main/study-records/2026-11-06/PNP-P003-customers-in-metro-cities-reattempt.md) · [Mastry P003 reattempt](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/study-records/2026-11-06/PNP-P003-customers-in-metro-cities-reattempt.md).


## Third independent attempt — executed SQLite output

Student's exact query:

```sql
select `CustomerID`, `FirstName`, `LastName`, trim(City), `State`
from Customers
where lower(trim(City)) in  ('bangalore','bengaluru','bombay','mumbai','new delhi','delhi','chennai','hyderabad')
order by trim(City) asc , CustomerID asc
```

SQLite 3.46.1 on the nine sample customers returned 8 rows (ID order 14,7,12,6,9,3,5,8), matching expected values and observed row order. The actual fourth column name is `trim(City)`, not `City`. Sorting by `trim(City)` is case-sensitive by default and does not guarantee the requested case-insensitive behavior for new input. Student must independently correct both remaining requirements. No verified P003 reattempt credit yet.
