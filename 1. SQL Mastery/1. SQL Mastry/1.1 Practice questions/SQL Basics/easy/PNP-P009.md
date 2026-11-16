# PNP P009 — Check how Active and Allowed are encoded

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

The data team wants to see how two flag columns are stored before using them in filters. Return **one result** that lists each distinct value in `Category.Active` and `Payments.Allowed`, with the number of rows holding that value.

Return four columns in this order: `source_table`, `flag_column`, `raw_value`, `row_count`. Show nonmissing values as text. Keep SQL `NULL` as its own group and count the rows in that group. Output order is flexible.

### Sample input

**`Category`**

| CategoryID | Active |
| --- | --- |
| 1 | 1 |
| 2 | 1 |
| 3 | 0 |
| 4 | `NULL` |

**`Payments`**

| PaymentID | Allowed |
| --- | --- |
| 1 | Y |
| 2 | N |
| 3 | N |

### Expected output

| source_table | flag_column | raw_value | row_count |
| --- | --- | --- | --- |
| Category | Active | `'1'` | 2 |
| Category | Active | `'0'` | 1 |
| Category | Active | `NULL` | 1 |
| Payments | Allowed | `'Y'` | 1 |
| Payments | Allowed | `'N'` | 2 |

Category has two rows with `Active = 1` and one with a missing flag, so those values get counts of 2 and 1.

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

**How to start.** What is one output row?

Use the same sample throughout and check the output after each step.

### 1. Summarize Category

**What to do.** Summarize Category.

**Why.** One group represents one Active value, including NULL.

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

**What to do.** Summarize Payments.

**Why.** Apply the same output shape to Allowed.

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

**What to do.** Combine both summaries.

**Why.** Appending keeps each source's groups visible.

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

### Official answer — SQLite adaptation

```sql
SELECT 'Category'                  AS source_table,
       'Active'                    AS flag_column,
       CAST(cat.Active AS TEXT) AS raw_value,
       COUNT(*)                    AS row_count
FROM Category AS cat
GROUP BY CAST(cat.Active AS TEXT)
UNION ALL
SELECT 'Payments',
       'Allowed',
       CAST(pay.Allowed AS TEXT),
       COUNT(*)
FROM Payments AS pay
GROUP BY CAST(pay.Allowed AS TEXT)
ORDER BY source_table, raw_value NULLS LAST;
```

### Official answer — SQL Server adaptation

```sql
WITH flag_counts AS (
    SELECT 'Category'                  AS source_table,
           'Active'                    AS flag_column,
           CAST(cat.Active AS NVARCHAR(MAX)) AS raw_value,
           COUNT(*)                    AS row_count
    FROM Category AS cat
    GROUP BY CAST(cat.Active AS NVARCHAR(MAX))
    UNION ALL
    SELECT 'Payments',
           'Allowed',
           CAST(pay.Allowed AS NVARCHAR(MAX)),
           COUNT(*)
    FROM Payments AS pay
    GROUP BY CAST(pay.Allowed AS NVARCHAR(MAX))
)
SELECT source_table, flag_column, raw_value, row_count
FROM flag_counts
ORDER BY source_table, CASE WHEN raw_value IS NULL THEN 1 ELSE 0 END, raw_value;
```

The SQL Server outer sort keeps a missing flag after the nonmissing flags within each source.

SQLite adaptation executed on representative fixtures. SQL Server adaptation reviewed by inspection.
