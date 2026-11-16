# PNP P009 — Check how Active and Allowed are encoded

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

Return one result listing the distinct stored values in `Category.Active` and `Payments.Allowed` and the number of rows per value. Return `source_table`, `flag_column`, `raw_value`, and `row_count`. Display nonmissing flag values as text and retain SQL NULL as a group. Output order is flexible.

### Sample input

**Category**

| CategoryID | Active |
| --- | --- |
| 1 | 1 |
| 2 | 1 |
| 3 | 0 |
| 4 | `NULL` |

**Payments**

| PaymentID | Allowed |
| --- | --- |
| 1 | Y |
| 2 | N |
| 3 | N |

### Expected output

| source_table | flag_column | raw_value | row_count |
| --- | --- | --- | --- |
| Category | Active | `NULL` | 1 |
| Category | Active | `'0'` | 1 |
| Category | Active | `'1'` | 2 |
| Payments | Allowed | `'N'` | 2 |
| Payments | Allowed | `'Y'` | 1 |

Category's two rows with Active = 1 form one group. Its missing flag forms another group with a count of one. Payments has two N flags and one Y flag.

## Learner solution — SQLite

```sql
SELECT 'Category' AS source_table,
       'Active' AS flag_column, CAST(Active AS TEXT) AS raw_value , count(*) as row_count
from Category
Group by Active

union all

SELECT 'Payments' AS source_table,
       'Allowed' AS flag_column,
CAST(Allowed AS TEXT) AS raw_value , count(*) as row_count
from Payments
group by Allowed
```

Verified the sample, the output column names and text types, and additional cases with two missing payment flags and a flag value shared by both sources. Chat formatting was removed when assembling the submitted SQL.

## Step-by-step walkthrough

### 1. Summarize Category

Group by Active and label every group with the table and flag names. Casting the flag as text preserves SQL NULL. COUNT(*) counts all rows in each group, including the missing flag row.

```sql
SELECT 'Category' AS source_table,
       'Active' AS flag_column, CAST(Active AS TEXT) AS raw_value , count(*) as row_count
from Category
Group by Active
```

| source_table | flag_column | raw_value | row_count |
| --- | --- | --- | --- |
| Category | Active | `NULL` | 1 |
| Category | Active | `'0'` | 1 |
| Category | Active | `'1'` | 2 |

### 2. Summarize Payments

Apply the same four-column structure to Allowed. Two N flags produce one row with a count of two.

```sql
SELECT 'Payments' AS source_table,
       'Allowed' AS flag_column,
CAST(Allowed AS TEXT) AS raw_value , count(*) as row_count
from Payments
group by Allowed
```

| source_table | flag_column | raw_value | row_count |
| --- | --- | --- | --- |
| Payments | Allowed | `'N'` | 2 |
| Payments | Allowed | `'Y'` | 1 |

### 3. Combine both summaries

The first SELECT supplies the four output column names. UNION ALL appends the Payments summary to the Category summary. The table shows the observed SQLite output order.

```sql
SELECT 'Category' AS source_table,
       'Active' AS flag_column, CAST(Active AS TEXT) AS raw_value , count(*) as row_count
from Category
Group by Active

union all

SELECT 'Payments' AS source_table,
       'Allowed' AS flag_column,
CAST(Allowed AS TEXT) AS raw_value , count(*) as row_count
from Payments
group by Allowed
```

| source_table | flag_column | raw_value | row_count |
| --- | --- | --- | --- |
| Category | Active | `NULL` | 1 |
| Category | Active | `'0'` | 1 |
| Category | Active | `'1'` | 2 |
| Payments | Allowed | `'N'` | 2 |
| Payments | Allowed | `'Y'` | 1 |

## Learner solution — SQL Server

```sql
SELECT 'Category' AS source_table,
       'Active' AS flag_column, CAST(Active AS NVARCHAR(MAX)) AS raw_value , count(*) as row_count
from Category
Group by Active

union all

SELECT 'Payments' AS source_table,
       'Allowed' AS flag_column,
CAST(Allowed AS NVARCHAR(MAX)) AS raw_value , count(*) as row_count
from Payments
group by Allowed;
```

The adaptation uses NVARCHAR(MAX) for text and was reviewed by inspection.

## Official solution

[PNP answer key, Q9](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT 'Category'                  AS source_table,
       'Active'                    AS flag_column,
       CAST(cat.Active AS VARCHAR) AS raw_value,
       COUNT(*)                    AS row_count
FROM Category AS cat
GROUP BY CAST(cat.Active AS VARCHAR)
UNION ALL
SELECT 'Payments',
       'Allowed',
       CAST(pay.Allowed AS VARCHAR),
       COUNT(*)
FROM Payments AS pay
GROUP BY CAST(pay.Allowed AS VARCHAR)
ORDER BY source_table, raw_value NULLS LAST;
```

The answer key groups by the cast text and adds an explicit sort. The learner groups by the stored flag, then casts it for display. Both give the same groups on the sample.
