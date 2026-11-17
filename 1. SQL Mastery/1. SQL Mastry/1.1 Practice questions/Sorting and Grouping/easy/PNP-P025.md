# P025 · Customer sign-ups by year and quarter

**Topic** Sorting and Grouping  
**Difficulty** ![EASY](../../../_badges/easy.svg)

## Question

Using the `Customers` table, count how many customers signed up in each calendar quarter of each year. `DateEntered` is the sign-up date.

Return these three columns.

| Column | Meaning |
|---|---|
| signup_year | The year of the sign-up |
| signup_quarter | The quarter number, from 1 to 4 |
| new_customers | The number of customers in that year and quarter |

Q1 is January–March, Q2 is April–June, Q3 is July–September, and Q4 is October–December. Show only groups that occur in the data. If any customers have a NULL sign-up date, count them in one group with NULL for both year and quarter. Sort by year ascending, then quarter ascending, with the NULL group last.

### Practice example

| CustomerID | DateEntered |
|---:|---|
| 1 | 2024-12-31 |
| 2 | 2025-01-01 |
| 3 | 2025-03-31 |
| 4 | 2025-04-01 |
| 5 | NULL |

### Expected output

| signup_year | signup_quarter | new_customers |
|---:|---:|---:|
| 2024 | 4 | 1 |
| 2025 | 1 | 2 |
| 2025 | 2 | 1 |
| NULL | NULL | 1 |

January 1 and March 31 both fall in Q1 of 2025, so that row has a count of 2. April 1 starts Q2.

## My final solution · SQLite

```sql
SELECT
    CAST(strftime('%Y', DateEntered) AS INTEGER) AS signup_year,
    CASE
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 1
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 3 THEN 1
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 4
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 6 THEN 2
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 7
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 9 THEN 3
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 10
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 12 THEN 4
        ELSE NULL
    END AS signup_quarter,
    COUNT(CustomerID) AS new_customers
FROM Customers
GROUP BY signup_year, signup_quarter
ORDER BY signup_year ASC NULLS LAST,
         signup_quarter ASC NULLS LAST;
```

## My solution · SQL Server

Equivalent adaptation for non-NULL CustomerID values.

```sql
SELECT YEAR(DateEntered) AS signup_year,
       DATEPART(QUARTER, DateEntered) AS signup_quarter,
       COUNT(CustomerID) AS new_customers
FROM Customers
GROUP BY YEAR(DateEntered), DATEPART(QUARTER, DateEntered)
ORDER BY CASE WHEN YEAR(DateEntered) IS NULL THEN 1 ELSE 0 END,
         signup_year, signup_quarter;
```

## Progressive walkthrough

### 1. Define one result row

One result row represents one year and quarter. The sample needs four groups, including the missing-date group. All customers participate, so start from Customers.


```sql
SELECT CustomerID, DateEntered FROM Customers;
```

The output is the five-row practice input above.

### 2. Extract the year and assign a quarter

Extract year with strftime and cast it to an integer. Extract month to decide which CASE range matches. Months 1–3 become quarter 1, and so on. A NULL date matches no range and reaches ELSE NULL.


```sql
SELECT CustomerID, DateEntered,
CAST(strftime('%Y', DateEntered) AS INTEGER) AS signup_year,
    CASE
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 1
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 3 THEN 1
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 4
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 6 THEN 2
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 7
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 9 THEN 3
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 10
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 12 THEN 4
        ELSE NULL
    END AS signup_quarter
FROM Customers;
```

| CustomerID | DateEntered | signup_year | signup_quarter |
|---:|---|---:|---:|
| 1 | 2024-12-31 | 2024 | 4 |
| 2 | 2025-01-01 | 2025 | 1 |
| 3 | 2025-03-31 | 2025 | 1 |
| 4 | 2025-04-01 | 2025 | 2 |
| 5 | NULL | NULL | NULL |

This demonstrates that customer 2 and customer 3 now share both grouping values.

### 3. Group and count

Replace the displayed customer and date with COUNT(CustomerID), then add GROUP BY signup_year, signup_quarter. Use the first part of the final query through GROUP BY.


```sql
SELECT
    CAST(strftime('%Y', DateEntered) AS INTEGER) AS signup_year,
    CASE
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 1
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 3 THEN 1
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 4
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 6 THEN 2
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 7
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 9 THEN 3
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 10
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 12 THEN 4
        ELSE NULL
    END AS signup_quarter,
    COUNT(CustomerID) AS new_customers
FROM Customers
GROUP BY signup_year, signup_quarter
;
```

| signup_year | signup_quarter | new_customers |
|---:|---:|---:|
| NULL | NULL | 1 |
| 2024 | 4 | 1 |
| 2025 | 1 | 2 |
| 2025 | 2 | 1 |

The displayed order is illustrative until ORDER BY is added. NULL grouping values belong to the same group. COUNT(CustomerID) counts those customers because their IDs are present, even when their dates are NULL. COUNT(*) is also suitable when counting every input row.

### 4. Sort the grouped result

Add ORDER BY signup_year ASC NULLS LAST, signup_quarter ASC NULLS LAST, as shown in the final solution. SQLite places NULL values first for an ascending sort by default, so NULLS LAST is needed. The result is the expected output table above.

No WHERE or HAVING condition is needed because every customer and every resulting group is requested.

## Official solution · Source dialect

```sql
SELECT EXTRACT(YEAR FROM c.DateEntered)::int AS signup_year,
       EXTRACT(QUARTER FROM c.DateEntered)::int AS signup_quarter,
       COUNT(*) AS new_customers
FROM Customers AS c
GROUP BY EXTRACT(YEAR FROM c.DateEntered)::int,
         EXTRACT(QUARTER FROM c.DateEntered)::int
ORDER BY signup_year NULLS LAST, signup_quarter NULLS LAST;
```

## Official solution · SQLite adaptation

```sql
SELECT
    CAST(strftime('%Y', DateEntered) AS INTEGER) AS signup_year,
    CASE
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 1
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 3 THEN 1
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 4
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 6 THEN 2
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 7
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 9 THEN 3
        WHEN CAST(strftime('%m', DateEntered) AS INTEGER) >= 10
         AND CAST(strftime('%m', DateEntered) AS INTEGER) <= 12 THEN 4
        ELSE NULL
    END AS signup_quarter,
    COUNT(*) AS new_customers
FROM Customers
GROUP BY signup_year, signup_quarter
ORDER BY signup_year ASC NULLS LAST,
         signup_quarter ASC NULLS LAST;
```

## Official solution · SQL Server adaptation

```sql
SELECT YEAR(DateEntered) AS signup_year,
       DATEPART(QUARTER, DateEntered) AS signup_quarter,
       COUNT(*) AS new_customers
FROM Customers
GROUP BY YEAR(DateEntered), DATEPART(QUARTER, DateEntered)
ORDER BY CASE WHEN YEAR(DateEntered) IS NULL THEN 1 ELSE 0 END,
         signup_year, signup_quarter;
```


## Verification

Executed the learner SQLite solution on the sample and checked all twelve months, with three months per quarter. Both checks passed. SQL Server adaptations were reviewed but were not executed.
