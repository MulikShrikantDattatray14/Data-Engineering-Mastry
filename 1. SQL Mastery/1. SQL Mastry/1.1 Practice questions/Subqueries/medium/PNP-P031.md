# PNP P031 — Customers who spend more than the average customer

**Topic** Subqueries · **Difficulty** ![MEDIUM](../../../_badges/medium.svg) · **Restart practice** 2026-11-19

[Question and required columns](../../../2.PNP-%20foundations%20and%20practice/6.%20SubQueries/P031.%20Customers%20who%20spend%20more%20than%20the%20average%20customer.md#question-and-image) · [Practice input and expected output](../../../2.PNP-%20foundations%20and%20practice/6.%20SubQueries/P031.%20Customers%20who%20spend%20more%20than%20the%20average%20customer.md#sample-input-and-expected-output) · [Source-colored sample tables](../../assets/question-samples/p031.svg?raw=1)

[Question](#question) · [Your SQLite solution](#final-learner-solution--sqlite) · [Previous / Next walkthrough](../../assets/steps/PNP-P031/01.md) · [SQL Server adaptation](#learner-solution--sql-server) · [Official solutions](#official-solution)

## Question

**Table colors** · 🟩 `Customers` · 🟦 `Orders`

**Business scenario.** The CRM team is building an invite list for an early-access programme. The rule is simple: invite customers whose lifetime spend is above what the average customer spends. Lifetime spend means the sum of Total_Order_Amount across all of a customer's orders. Refunds are not modelled, so this is gross spend.

**Task.** Return every customer whose total spend is greater than the average total spend per customer. Show the customer's spend, the average they were compared against, and how far above it they are in percent. Sort by spend, highest first.

[PNP source question](../../../2.PNP-%20foundations%20and%20practice/6.%20SubQueries/P031.%20Customers%20who%20spend%20more%20than%20the%20average%20customer.md#question-and-image) · *100 SQL Interview Questions*, Q31, pp. 52–54.

### Required output columns

The course asks for one row per ordering customer whose lifetime spend exceeds the average lifetime spend across ordering customers.

| # | Output column | Source | Requirement for one result row | Practice example |
| ---: | --- | --- | --- | --- |
| 1 | `CustomerID` | 🟦 `Orders.CustomerID` | Return the ordering customer's ID. The course excludes orders with a missing ID and preserves known IDs even if their customer record is missing. | 1 |
| 2 | `customer_name` | 🟩 `Customers.FirstName`, `Customers.LastName` | Look up the name for the ordering ID. The course displays the first and last name or `Unknown customer` when no customer row matches. | Asha Rao |
| 3 | `total_spend` | 🟦 `Orders.Total_Order_Amount` | Sum the gross amount of all orders placed by this customer. Multiple orders still contribute a single customer total to the benchmark. | 300 |
| 4 | `avg_customer_spend` | 🟦 Calculated from the customer totals | Course display rule: two decimals. The locked learner query does not round this benchmark, so it returns the unrounded average of one lifetime total per ordering customer. | 200.0 |
| 5 | `pct_above_avg` | 🟦 Calculated from the customer total and benchmark | Course display rule: two decimals. The locked learner query does not `ROUND` this calculation; it computes 100 × (customer total − benchmark) ÷ benchmark and guards against a zero denominator. | 50.0 |

**Selection and ordering.** Compare each customer total with the unrounded benchmark using strict greater-than. Equal spend is excluded. Sort by total spend descending. The course answer uses customer ID ascending as its tie-breaker.

### Practice example · Sample input

<a name="sample-input-and-expected-output"></a>

*The PNP material supplies the output columns. These rows illustrate the invitation rule.*

**🟩 `Customers`**

| 🟩 `CustomerID` | 🟩 `FirstName` | 🟩 `LastName` |
| ---: | --- | --- |
| 1 | Asha | Rao |
| 2 | Ben | Das |
| 3 | Cia | Sen |

**🟦 `Orders`**

| 🟦 `OrderID` | 🟦 `CustomerID` | 🟦 `Total_Order_Amount` |
| ---: | ---: | ---: |
| 10 | 1 | 300 |
| 11 | 2 | 100 |
| 12 | 3 | 200 |

### Expected output

| 🟦 `CustomerID` | 🟩 `customer_name` | 🟦 `total_spend` | 🟦 `avg_customer_spend` | 🟦 `pct_above_avg` |
| ---: | --- | ---: | ---: | ---: |
| 1 | Asha Rao | 300 | 200.00 | 50.00 |

**Precision note.** The expected table follows the course’s two-decimal display. The locked learner query returns unrounded numeric values; for this sample SQLite returns `avg_customer_spend = 200.0` and `pct_above_avg = 50.0`. Other inputs can yield additional decimal places. This documented difference is preserved; the selected SQL is unchanged.



[View the source-colored sample tables](../../assets/question-samples/p031.svg?raw=1)

### How the sample produces this output

The three 🟦 lifetime amounts are **300**, **100** and **200**. Their average is **(300 + 100 + 200) ÷ 3 = 200.00**. 🟩 **Asha Rao** (ID **1**) spent 🟦 **100** above that average, or **(300 − 200) ÷ 200 × 100 = 50.00%**. 🟩 **Ben Das** is below the average. 🟩 **Cia Sen** equals it. Only Asha qualifies.

## Step 1 · Your approach before writing SQL

1. What does one output row represent, and what does each requested column tell the CRM team?
2. Which source would you start with, and why? If you add a source, when would you add it, which join type and keys would you choose, and which rows should survive?
3. Which rows are eligible to contribute to the benchmark, and when should the above-average condition apply?
4. How should repeated orders contribute to one customer total and to the overall average?
5. How should missing IDs, missing names, equality, a zero benchmark, precision and ties behave?
6. Trace Asha and Cia from the sample inputs through their different outcomes.

## Final learner solution — SQLite

Shri selected this exact query as the final SQLite submission on 19 November 2026.

```sql
WITH customer_spend AS (
    SELECT
        o.CustomerID,
        COALESCE(c.FirstName || ' ' || c.LastName, 'Unknown') AS customer_name,
        SUM(o.Total_Order_Amount) AS total_spend
    FROM Orders AS o
    LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
    GROUP BY o.CustomerID, c.FirstName, c.LastName
),
spend_with_avg AS (
    SELECT
        cs.*,
        (SELECT AVG(total_spend) FROM customer_spend) AS avg_customer_spend
    FROM customer_spend AS cs
)
SELECT
    CustomerID,
    customer_name,
    total_spend,
    avg_customer_spend,
    100.0 * (total_spend - avg_customer_spend)
        / NULLIF(avg_customer_spend, 0) AS pct_above_avg
FROM spend_with_avg
WHERE total_spend > avg_customer_spend
ORDER BY total_spend DESC;
```

## Visual walkthrough

[Open the Previous / Next walkthrough](../../assets/steps/PNP-P031/01.md)

![Six stages of the locked SQLite query. The left join preserves the three orders. Customer totals of 300, 100 and 200 average 200. Asha Rao is the only customer above it, at 50 percent.](../../assets/walkthroughs/p031.svg)

[Open the walkthrough at full size](../../assets/walkthroughs/p031.svg?raw=1)

## Step-by-step walkthrough

### 1. Which rows do we start with?

`FROM Orders AS o` supplies one row per purchase because every order amount contributes to lifetime spend, even if the customer name is missing. A customer with no orders contributes no spend row. These are the two sample inputs used throughout the walkthrough. The order below makes the examples easy to follow.

```sql
SELECT OrderID, CustomerID, Total_Order_Amount FROM Orders ORDER BY OrderID;
SELECT CustomerID, FirstName, LastName FROM Customers ORDER BY CustomerID;
```

**🟦 Orders**

| 🟦 OrderID | 🟦 CustomerID | 🟦 Total_Order_Amount |
| --- | --- | --- |
| 10 | 1 | 300 |
| 11 | 2 | 100 |
| 12 | 3 | 200 |

**🟩 Customers**

| 🟩 CustomerID | 🟩 FirstName | 🟩 LastName |
| --- | --- | --- |
| 1 | Asha | Rao |
| 2 | Ben | Das |
| 3 | Cia | Sen |

### 2. How does each order get a name?

The left side starts with the three orders. Each order already carries the customer ID needed for the next lookup. The learner adds Customers here so the matching name is available before grouping. The LEFT JOIN keeps the purchase amount even if the name lookup fails. Order 10 matches customer 1. With one match per order, the join produces three rows. An unmatched order survives with missing customer fields. The name expression in the next step displays `Unknown` for it.

```sql
SELECT o.OrderID, o.CustomerID, o.Total_Order_Amount,
       c.CustomerID, c.FirstName, c.LastName
FROM Orders AS o
LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
ORDER BY o.OrderID;
```

| 🟦 OrderID | 🟦 o.CustomerID | 🟦 Total_Order_Amount | 🟩 c.CustomerID | 🟩 FirstName | 🟩 LastName |
| --- | --- | --- | --- | --- | --- |
| 10 | 1 | 300 | 1 | Asha | Rao |
| 11 | 2 | 100 | 2 | Ben | Das |
| 12 | 3 | 200 | 3 | Cia | Sen |

### 3. What does one customer spend?

The `customer_spend` CTE is prepared from raw `Orders` and `Customers`, not from the preceding joined step. `FROM Orders AS o` supplies every order amount; `LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID` attaches names and preserves orders without a match. `GROUP BY` returns one row per `CustomerID`/name group (including a `NULL`-ID group if present), so several orders contribute to one `total_spend`. The three sample orders produce three groups.

```sql
SELECT
    o.CustomerID,
    COALESCE(c.FirstName || ' ' || c.LastName, 'Unknown') AS customer_name,
    SUM(o.Total_Order_Amount) AS total_spend
FROM Orders AS o
LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
GROUP BY o.CustomerID, c.FirstName, c.LastName;
```

| 🟦 CustomerID | 🟩 customer_name | 🟦 total_spend |
| --- | --- | --- |
| 1 | Asha Rao | 300 |
| 2 | Ben Das | 100 |
| 3 | Cia Sen | 200 |

In a separate check, replacing order 10 with two orders of 100 and 200 for Asha produced the same total of 300 and the same final row.

### 4. Why does every customer get the same average?

The second CTE reads `customer_spend`, which contains one row per `CustomerID`/name group (including a `NULL`-ID group if present). `FROM customer_spend AS cs` supplies those customer totals to the outer query. The scalar subquery separately reads all group totals and returns (300 + 100 + 200) ÷ 3 = 200 for this sample, then attaches it to each group. The locked query includes a `NULL`-ID group in this benchmark; the course answer excludes it.

```sql
SELECT
    cs.*,
    (SELECT AVG(total_spend) FROM customer_spend) AS avg_customer_spend
FROM customer_spend AS cs;
```

| 🟦 CustomerID | 🟩 customer_name | 🟦 total_spend | 🟦 avg_customer_spend |
| --- | --- | --- | --- |
| 1 | Asha Rao | 300 | 200.0 |
| 2 | Ben Das | 100 | 200.0 |
| 3 | Cia Sen | 200 | 200.0 |

### 5. Who passes the filter?

The final query starts with `spend_with_avg`. This diagnostic projection makes its `WHERE` decision visible. In SQLite, 1 means true and 0 means false.

```sql
SELECT customer_name, total_spend, avg_customer_spend,
       total_spend > avg_customer_spend AS qualifies
FROM spend_with_avg
ORDER BY CustomerID;
```

| 🟩 customer_name | 🟦 total_spend | 🟦 avg_customer_spend | 🟦 qualifies |
| --- | --- | --- | --- |
| Asha Rao | 300 | 200.0 | 1 |
| Ben Das | 100 | 200.0 | 0 |
| Cia Sen | 200 | 200.0 | 0 |

The filter keeps Asha. Ben falls below 200. Cia is exactly at 200, so the strict greater-than comparison excludes her.

### 6. How far above average is Asha?

Apply the final projection and sort the surviving rows by descending spend. Asha is 100 above the average. Dividing that difference by 200 and multiplying by 100 gives 50 percent. `NULLIF` guards against dividing by zero.

```sql
SELECT
    CustomerID,
    customer_name,
    total_spend,
    avg_customer_spend,
    100.0 * (total_spend - avg_customer_spend)
        / NULLIF(avg_customer_spend, 0) AS pct_above_avg
FROM spend_with_avg
WHERE total_spend > avg_customer_spend
ORDER BY total_spend DESC;
```

| 🟦 CustomerID | 🟩 customer_name | 🟦 total_spend | 🟦 avg_customer_spend | 🟦 pct_above_avg |
| --- | --- | --- | --- | --- |
| 1 | Asha Rao | 300 | 200.0 | 50.0 |

## Sample verification

Executed in SQLite on the three orders in the practice example. Asha, Ben and Cia spend 300, 100 and 200 respectively. The scalar subquery returns 200. The strict comparison excludes Cia, whose total equals the average.

| 🟦 CustomerID | 🟩 customer_name | 🟦 total_spend | 🟦 avg_customer_spend | 🟦 pct_above_avg |
| ---: | --- | ---: | ---: | ---: |
| 1 | Asha Rao | 300 | 200.0 | 50.0 |

## Comparison with the course answer

- Adding an order worth 1000 with a `NULL` customer ID to the practice data produces a fourth group in the submitted query. SQLite returns that group with a total of 1000 and an average of 400. The course answer excludes orders with a `NULL` customer ID before it calculates the average.
- Giving that same order customer ID 99, which has no customer record, returns `Unknown` in the submission. The course uses `Unknown customer` for an unmatched ID and joins the available name parts for a matched customer. When only one name part is present, the learner's `FirstName || ' ' || LastName` expression also becomes `NULL`, so `COALESCE` returns `Unknown`; the official SQLite adaptation keeps the available part (for example, `Khan` or `Lina`). I verified both partial-name cases with a separate SQLite fixture.
- The submission returns the unrounded average and percentage and sorts by descending spend. The course rounds both displayed calculations to two decimals and uses customer ID to break spending ties. Both compare totals with the unrounded average.

[Official PostgreSQL answer, Q31](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/fa70de6416696e0d6ab94faee964e048f9552ecd/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql#L370-L393)

## Learner solution — SQL Server

This T-SQL adaptation preserves the chosen fallback, grouping, precision policy and ordering. The decimal cast keeps fractional averages if the input column is integral. SQL Server execution is unverified.

```sql
WITH customer_spend AS (
    SELECT
        o.CustomerID,
        COALESCE(c.FirstName + ' ' + c.LastName, 'Unknown') AS customer_name,
        SUM(o.Total_Order_Amount) AS total_spend
    FROM Orders AS o
    LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
    GROUP BY o.CustomerID, c.FirstName, c.LastName
),
spend_with_avg AS (
    SELECT
        cs.*,
        (SELECT AVG(CAST(total_spend AS decimal(28, 8))) FROM customer_spend) AS avg_customer_spend
    FROM customer_spend AS cs
)
SELECT
    CustomerID,
    customer_name,
    total_spend,
    avg_customer_spend,
    100.0 * (total_spend - avg_customer_spend)
        / NULLIF(avg_customer_spend, 0) AS pct_above_avg
FROM spend_with_avg
WHERE total_spend > avg_customer_spend
ORDER BY total_spend DESC;
```

## Official solution

### As supplied — PostgreSQL 16

[PrepNPlaced Q31 in the original answer key](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql#L370-L393)

```sql
WITH customer_spend AS (
    SELECT o.CustomerID,
           SUM(o.Total_Order_Amount) AS total_spend
    FROM Orders AS o
    WHERE o.CustomerID IS NOT NULL
    GROUP BY o.CustomerID
),
benchmark AS (
    SELECT AVG(cs.total_spend) AS avg_customer_spend
    FROM customer_spend AS cs
)
SELECT cs.CustomerID,
       CASE WHEN c.CustomerID IS NULL THEN 'Unknown customer'
            ELSE CONCAT_WS(' ', c.FirstName, c.LastName) END                  AS customer_name,
       cs.total_spend,
       ROUND(b.avg_customer_spend, 2)                                         AS avg_customer_spend,
       ROUND(100.0 * (cs.total_spend - b.avg_customer_spend)
             / NULLIF(b.avg_customer_spend, 0), 2)                            AS pct_above_avg
FROM customer_spend AS cs
CROSS JOIN benchmark AS b
LEFT JOIN Customers AS c ON c.CustomerID = cs.CustomerID
WHERE cs.total_spend > (SELECT avg_customer_spend FROM benchmark)
ORDER BY cs.total_spend DESC, cs.CustomerID;
```

### Official answer — SQLite

The name expression skips missing name parts on a matched customer. It uses the course label for an unmatched ID.

```sql
WITH customer_spend AS (
    SELECT o.CustomerID,
           SUM(o.Total_Order_Amount) AS total_spend
    FROM Orders AS o
    WHERE o.CustomerID IS NOT NULL
    GROUP BY o.CustomerID
),
benchmark AS (
    SELECT AVG(cs.total_spend) AS avg_customer_spend
    FROM customer_spend AS cs
)
SELECT cs.CustomerID,
       CASE WHEN c.CustomerID IS NULL THEN 'Unknown customer'
            WHEN c.FirstName IS NULL THEN COALESCE(c.LastName, '')
            WHEN c.LastName IS NULL THEN c.FirstName
            ELSE c.FirstName || ' ' || c.LastName END                  AS customer_name,
       cs.total_spend,
       ROUND(b.avg_customer_spend, 2)                                         AS avg_customer_spend,
       ROUND(100.0 * (cs.total_spend - b.avg_customer_spend)
             / NULLIF(b.avg_customer_spend, 0), 2)                            AS pct_above_avg
FROM customer_spend AS cs
CROSS JOIN benchmark AS b
LEFT JOIN Customers AS c ON c.CustomerID = cs.CustomerID
WHERE cs.total_spend > (SELECT avg_customer_spend FROM benchmark)
ORDER BY cs.total_spend DESC, cs.CustomerID;
```

### Official answer — SQL Server

This T-SQL adaptation uses a decimal average and the course’s display and ordering rules. SQL Server execution is unverified.

```sql
WITH customer_spend AS (
    SELECT o.CustomerID,
           SUM(o.Total_Order_Amount) AS total_spend
    FROM Orders AS o
    WHERE o.CustomerID IS NOT NULL
    GROUP BY o.CustomerID
),
benchmark AS (
    SELECT AVG(CAST(cs.total_spend AS decimal(28, 8))) AS avg_customer_spend
    FROM customer_spend AS cs
)
SELECT cs.CustomerID,
       CASE WHEN c.CustomerID IS NULL THEN 'Unknown customer'
            ELSE CONCAT_WS(' ', c.FirstName, c.LastName) END                  AS customer_name,
       cs.total_spend,
       ROUND(b.avg_customer_spend, 2)                                         AS avg_customer_spend,
       ROUND(100.0 * (cs.total_spend - b.avg_customer_spend)
             / NULLIF(b.avg_customer_spend, 0), 2)                            AS pct_above_avg
FROM customer_spend AS cs
CROSS JOIN benchmark AS b
LEFT JOIN Customers AS c ON c.CustomerID = cs.CustomerID
WHERE cs.total_spend > (SELECT avg_customer_spend FROM benchmark)
ORDER BY cs.total_spend DESC, cs.CustomerID;
```

## Verification

Both SQLite queries return Asha Rao on the practice sample. On the course CSVs (46,438 orders and 5,072 customer records), the locked query returns 1,317 rows and the course SQLite query returns 1,317 rows. 0 orders have a missing customer ID. The separate edge checks above explain how an unrecognized or missing ID changes the result.
