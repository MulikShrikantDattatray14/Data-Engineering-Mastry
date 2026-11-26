# PNP P035 — Late-delivery rate by shipper

**Topic** Aggregation, conditional aggregation and CTEs · **Difficulty** Medium

> **Record status:** The learner's locked SQLite solution, recorded approach progression, SQL Server adaptation, sourced PostgreSQL course answer, SQLite/SQL Server course adaptations, course comparison and SQLite verification are present below. The approach score remains unrecorded. The two required visuals, generated Previous/Next walkthrough and final completion audit remain pending. Preserve the documented zero-order-shipper counting defect; do not silently change the locked query or mark that edge case passed.

## Question

**Source:** [100 SQL Interview Questions, question 35, pp. 59–61](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/Updated_100_SQL_Interview_Questions.pdf). **Difficulty:** Medium.

**Business scenario.** The logistics team reviews courier performance every quarter and moves volume away from the worst performer. They want each shipper's late-delivery rate. There is no promised delivery date in the data, so the team has agreed a working rule: an order is late when it is delivered more than 7 days after it was placed.

**Task.** For each shipper, count delivered orders, late orders and the late rate. Count orders with no delivery date separately, and keep orders with impossible date sequences out of the rate but visible in their own column. Orders with a missing or unknown ShipperID go under Unknown shipper. Sort by late rate, highest first.

**Table colors:** 🟥 `Shippers` · 🟦 `Orders` · 🟪 derived labels and calculations.

### Required output columns

| Output column | Source / calculation | Meaning for one output row and applicable rule | Example value |
|---|---|---|---:|
| `shipper_name` | 🟥 `Shippers.CompanyName`, fallback 🟪 label | The matched shipper's display name; use `Unknown shipper` when the order-side ShipperID has no matching master row. Groups remain separated by resolved ShipperID even when labels match. | 🟥 FastShip |
| `delivered_orders` | 🟦 `Orders` row-level `is_delivered` flag, summed by shipper | Number of delivered orders in the shipper group. Under the locked expression, a non-NULL DeliveryDate counts unless all three dates are present and their sequence is invalid. | 🟦 2 |
| `late_orders` | 🟦 `OrderDate`, `ShipDate`, `DeliveryDate` row-level `is_late` flag, summed by shipper | Number of orders with all three dates present, a valid chronological sequence, and elapsed delivery time strictly greater than 7 days. | 🟦 1 |
| `late_rate_pct` | 🟪 `SUM(is_late) * 100.0 / NULLIF(SUM(is_delivered), 0)` | Late orders as a percentage of delivered orders, rounded to 2 decimals. A zero delivered denominator produces NULL, not zero. | 🟪 50.00 |
| `not_delivered` | 🟦 `Orders.DeliveryDate` row-level flag, summed by shipper | Number of orders whose DeliveryDate is NULL, regardless of whether other date fields are present. | 🟦 1 |
| `invalid_dates` | 🟦 `OrderDate`, `ShipDate`, `DeliveryDate` row-level flag, summed by shipper | Number of orders where all three dates exist but `OrderDate <= ShipDate <= DeliveryDate` is false. | 🟦 1 |

**Row eligibility and sorting:** The locked query produces one row per resolved ShipperID and shipper label represented by either input, including shippers with no orders and orders with NULL or unmatched ShipperID. It sorts by `late_rate_pct DESC`; ties have no guaranteed secondary order.

### Practice example · Sample input

The source question supplies output-column definitions but no sample rows. The following illustrative fixture was added for practice.

**🟥 `Shippers`**

| 🟥 ShipperID | 🟥 CompanyName |
|---:|---|
| 🟥 1 | 🟥 FastShip |
| 🟥 2 | 🟥 QuickShip |

**🟦 `Orders`**

| 🟦 OrderID | 🟦 ShipperID | 🟦 OrderDate | 🟦 ShipDate | 🟦 DeliveryDate |
|---:|---:|---|---|---|
| 🟦 1 | 🟦 1 | 🟦 2025-01-01 | 🟦 2025-01-02 | 🟦 2025-01-10 |
| 🟦 2 | 🟦 1 | 🟦 2025-01-01 | 🟦 2025-01-02 | 🟦 2025-01-05 |
| 🟦 3 | 🟦 1 | 🟦 2025-01-01 | 🟦 NULL | 🟦 NULL |
| 🟦 4 | 🟦 1 | 🟦 2025-01-05 | 🟦 2025-01-04 | 🟦 2025-01-06 |
| 🟦 5 | 🟦 2 | 🟦 2025-01-01 | 🟦 2025-01-02 | 🟦 2025-01-03 |

### Expected output

| 🟪 shipper_name | 🟦 delivered_orders | 🟦 late_orders | 🟪 late_rate_pct | 🟦 not_delivered | 🟦 invalid_dates |
|---|---:|---:|---:|---:|---:|
| 🟥 FastShip | 🟦 2 | 🟦 1 | 🟪 50.00 | 🟦 1 | 🟦 1 |
| 🟥 QuickShip | 🟦 1 | 🟦 0 | 🟪 0.00 | 🟦 0 | 🟦 0 |

Order 4 is invalid because its ship date is before its order date; it is excluded from the delivered-rate denominator. The fixture does not include an unmatched or NULL ShipperID order, so the Unknown shipper branch still needs a dedicated verification fixture.

### How the sample produces this output

- 🟥 **FastShip:** Order 1 took 9 days, so it is delivered and late. Order 2 took 4 days, so it is delivered and on time. Order 3 has no delivery date, so it is counted as not delivered. Order 4 violates the date order because 🟦 `2025-01-04` (ShipDate) is earlier than 🟦 `2025-01-05` (OrderDate), so it is counted as invalid and excluded from the delivered denominator. Rate = 🟪 1 × 100 / 2 = 50.00%.
- 🟥 **QuickShip:** Order 5 took 2 days, so it is delivered and on time. Rate = 🟪 0 × 100 / 1 = 0.00%.

## Step 1 · Your approach before writing SQL

1. What does one output row represent, and what does each measure tell the logistics team?
2. Which source would you start from, and why? Which keys connect the sources and which unmatched rows must survive?
3. How will you classify delivered, late, not-delivered and invalid-date orders?
4. Which dates must be present before calculating elapsed days, and is the seven-day boundary strict?
5. How should missing or unknown ShipperID values be labeled and grouped?
6. How will you calculate the rate when a shipper has zero delivered orders?
7. Trace FastShip orders 1–4 and QuickShip order 5 through the sample.

## Approach review / agreed approach

**Recorded learner progression (preserved):**

1. Started with `Shippers LEFT JOIN Orders` on `ShipperID`, grouping by shipper ID and company name.
2. Identified `COALESCE(CompanyName, 'Unknown shipper')` for the output label.
3. Proposed conditional counting for delivered and late orders, using the date difference threshold of more than 7 days.
4. Identified that both `OrderDate` and `DeliveryDate` must be present to calculate a date difference.
5. Defined the valid chronological sequence as `OrderDate <= ShipDate <= DeliveryDate`; a fully populated sequence that violates it is invalid.
6. Identified `DeliveryDate IS NULL` for `not_delivered`.
7. Learned that `NULLIF(delivered_orders, 0)` prevents division by zero and produces NULL when the denominator is zero.
8. Revisited join preservation after noticing the source explicitly requires missing or unknown ShipperID orders to appear as Unknown shipper. Changed the join to `FULL OUTER JOIN`.
9. Refactored the nested conditional aggregates into a CTE that classifies each order with 0/1 flags, then aggregates those flags.

**Review:** The initial LEFT JOIN retained every shipper but lost order rows with NULL or unmatched ShipperID. FULL OUTER JOIN retains both input populations. The CTE separates per-row classification from shipper-level aggregation.

**Approach score:** Not recorded in the saved learner history; no retrospective score has been invented.

## Final learner solution — SQLite

**Locked learner submission — preserved verbatim**

```sql
WITH order_classification AS (

    SELECT
        COALESCE(S.ShipperID, O.ShipperID) AS ShipperID,
        COALESCE(S.CompanyName, 'Unknown shipper') AS shipper_name,

        CASE
            WHEN O.DeliveryDate IS NOT NULL
             AND NOT (
                 O.OrderDate IS NOT NULL
                 AND O.ShipDate IS NOT NULL
                 AND O.DeliveryDate IS NOT NULL
                 AND NOT (
                     O.OrderDate <= O.ShipDate
                     AND O.ShipDate <= O.DeliveryDate
                 )
             )
            THEN 1
            ELSE 0
        END AS is_delivered,

        CASE
            WHEN O.OrderDate IS NOT NULL
             AND O.ShipDate IS NOT NULL
             AND O.DeliveryDate IS NOT NULL
             AND O.OrderDate <= O.ShipDate
             AND O.ShipDate <= O.DeliveryDate
             AND julianday(O.DeliveryDate) -
                 julianday(O.OrderDate) > 7
            THEN 1
            ELSE 0
        END AS is_late,

        CASE
            WHEN O.DeliveryDate IS NULL
            THEN 1
            ELSE 0
        END AS not_delivered,

        CASE
            WHEN O.OrderDate IS NOT NULL
             AND O.ShipDate IS NOT NULL
             AND O.DeliveryDate IS NOT NULL
             AND NOT (
                 O.OrderDate <= O.ShipDate
                 AND O.ShipDate <= O.DeliveryDate
             )
            THEN 1
            ELSE 0
        END AS invalid_dates

    FROM Shippers AS S

    FULL OUTER JOIN Orders AS O
        ON S.ShipperID = O.ShipperID
)

SELECT
    shipper_name,

    SUM(is_delivered) AS delivered_orders,

    SUM(is_late) AS late_orders,

    ROUND(
        SUM(is_late) * 100.0 /
        NULLIF(SUM(is_delivered), 0),
        2
    ) AS late_rate_pct,

    SUM(not_delivered) AS not_delivered,

    SUM(invalid_dates) AS invalid_dates

FROM order_classification

GROUP BY
    ShipperID,
    shipper_name

ORDER BY
    late_rate_pct DESC;
```

**Interpretation to verify:** The submitted `is_delivered` flag counts a row with a non-NULL DeliveryDate unless all three dates are present and their sequence is invalid. Therefore a row with a missing OrderDate or ShipDate can still count as delivered. The submitted `is_late` flag requires all three dates to be present and in sequence. This behavior is preserved as submitted and should be checked against the intended business definition during verification; do not silently rewrite the learner query.

## Important learnings from P035

### 1. Choosing the join from row-preservation requirements

- `Shippers LEFT JOIN Orders` preserves every shipper, including a shipper with no orders. It does **not** preserve Orders rows whose ShipperID is NULL or has no matching Shippers row.
- The task explicitly says orders with a missing or unknown ShipperID go under `Unknown shipper`. That means unmatched rows from Orders must survive too.
- `FULL OUTER JOIN` preserves unmatched rows from both inputs, so it satisfies both requirements: all shippers and all orders with missing/unknown shipper references.
- `COALESCE(S.ShipperID, O.ShipperID)` retains the available key from whichever side matched. `COALESCE(S.CompanyName, 'Unknown shipper')` supplies the fallback label.

### 2. Conditional counting with CASE

`COUNT(CASE WHEN condition THEN 1 END)` counts only rows for which the condition is true. A CASE expression without an ELSE returns NULL for non-matching rows, and COUNT ignores NULL.

### 3. Date difference and strict boundaries

- In SQLite, `julianday(DeliveryDate) - julianday(OrderDate)` calculates the elapsed number of days for supported date values.
- `> 7` means strictly more than seven days. Exactly seven days is not late.
- Both OrderDate and DeliveryDate must be non-NULL to calculate the difference.
- The learner's final late flag additionally requires ShipDate to exist and the full chronological sequence to be valid.

### 4. Date-sequence validation

The agreed complete sequence is:

`OrderDate <= ShipDate <= DeliveryDate`

When all three dates exist, the sequence is invalid if either comparison fails. The final learner query counts these fully populated but out-of-order rows in `invalid_dates`.

### 5. NULL, COUNT and separate classifications

- `DeliveryDate IS NULL` identifies orders with no delivery date.
- `COUNT(column)` ignores NULL values; `COUNT(*)` counts rows regardless of NULLs.
- A missing delivery date is classified separately by `not_delivered`; it is not automatically counted as an invalid sequence by the submitted logic.
- A missing ShipDate with a present DeliveryDate is counted as delivered by the submitted `is_delivered` expression, but is not counted as late. This is a business-rule assumption to validate, not a universal SQL rule.

### 6. NULLIF protects a division denominator

`NULLIF(SUM(is_delivered), 0)` returns NULL when there are zero delivered orders. Dividing by that NULL produces NULL rather than a divide-by-zero error. The percentage is rounded to two decimal places.

### 7. CTEs simplify nested logic

- The `order_classification` CTE creates one intermediate row per joined shipper/order row and computes reusable 0/1 flags.
- The outer query uses `SUM(flag)` to count each classification by shipper.
- This separates row-level business rules from group-level aggregation and avoids repeating long CASE expressions inside the final percentage calculation.
- A 0/1 flag plus SUM is a useful alternative to repeating `COUNT(CASE...)` expressions when multiple metrics share the same input rows.

### 8. Grouping keys

The query groups by both the resolved ShipperID and shipper_name. Keeping the ID in the grouping key helps keep distinct shipper records separate even if their company names happen to be identical.

## Visual walkthrough

**Pending.** Required dual visuals have not yet been created: (A) a query architecture / row-preservation flowchart and (B) a progressive visual walkthrough tracing the exact fixture through the saved CTE query. They must be added and verified before this record can be marked complete.

## Step-by-step walkthrough

**Pending detailed trace.** The walkthrough must trace the exact five sample OrderIDs through the FULL OUTER JOIN, each classification flag, grouping, SUM aggregation, NULLIF percentage and final sort. It must also include a separate unmatched/NULL ShipperID fixture to demonstrate the Unknown shipper group.

## Learner solution — SQL Server adaptation

**Learner-query SQL Server adaptation (not executed on SQL Server):**

This keeps the locked flag conditions and grouping. It assumes the date columns represent calendar dates. SQL Server `DATEDIFF(day, ...)` counts date boundaries; if the columns are DATETIME values, that can differ from SQLite's elapsed-day `julianday()` difference.

```sql
WITH order_classification AS (
    SELECT
        COALESCE(S.ShipperID, O.ShipperID) AS ShipperID,
        COALESCE(S.CompanyName, 'Unknown shipper') AS shipper_name,
        CASE
            WHEN O.DeliveryDate IS NOT NULL
             AND NOT (
                 O.OrderDate IS NOT NULL AND O.ShipDate IS NOT NULL AND O.DeliveryDate IS NOT NULL
                 AND NOT (O.OrderDate <= O.ShipDate AND O.ShipDate <= O.DeliveryDate)
             ) THEN 1 ELSE 0
        END AS is_delivered,
        CASE
            WHEN O.OrderDate IS NOT NULL AND O.ShipDate IS NOT NULL AND O.DeliveryDate IS NOT NULL
             AND O.OrderDate <= O.ShipDate AND O.ShipDate <= O.DeliveryDate
             AND DATEDIFF(day, O.OrderDate, O.DeliveryDate) > 7
            THEN 1 ELSE 0
        END AS is_late,
        CASE WHEN O.DeliveryDate IS NULL THEN 1 ELSE 0 END AS not_delivered,
        CASE
            WHEN O.OrderDate IS NOT NULL AND O.ShipDate IS NOT NULL AND O.DeliveryDate IS NOT NULL
             AND NOT (O.OrderDate <= O.ShipDate AND O.ShipDate <= O.DeliveryDate)
            THEN 1 ELSE 0
        END AS invalid_dates
    FROM Shippers AS S
    FULL OUTER JOIN Orders AS O ON S.ShipperID = O.ShipperID
)
SELECT shipper_name,
       SUM(is_delivered) AS delivered_orders,
       SUM(is_late) AS late_orders,
       ROUND(SUM(is_late) * 100.0 / NULLIF(SUM(is_delivered), 0), 2) AS late_rate_pct,
       SUM(not_delivered) AS not_delivered,
       SUM(invalid_dates) AS invalid_dates
FROM order_classification
GROUP BY ShipperID, shipper_name
ORDER BY CASE WHEN SUM(is_delivered) = 0 THEN 1 ELSE 0 END,
         late_rate_pct DESC;
```

No SQL Server execution is claimed. The explicit NULL-last expression matches the SQLite display intent; ties remain unspecified.

## Official solution

### Original course answer — PostgreSQL

**Source:** [`all_100_solutions.sql`, Q35, lines 435–459](../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql#L435-L459). Transcribed from the supplied repository source; PostgreSQL syntax is preserved.

```sql
WITH classified AS (
    SELECT COALESCE(sh.CompanyName, 'Unknown shipper') AS shipper_name,
           CASE
               WHEN o.DeliveryDate IS NULL THEN 'Not delivered'
               WHEN o.DeliveryDate < o.OrderDate
                 OR o.ShipDate < o.OrderDate
                 OR o.DeliveryDate < o.ShipDate THEN 'Invalid dates'
               WHEN o.DeliveryDate::date - o.OrderDate::date > 7 THEN 'Late'
               ELSE 'On time'
           END AS delivery_status
    FROM Orders AS o
    LEFT JOIN Shippers AS sh ON sh.ShipperID = o.ShipperID
)
SELECT shipper_name,
       COUNT(*) FILTER (WHERE delivery_status IN ('Late', 'On time')) AS delivered_orders,
       COUNT(*) FILTER (WHERE delivery_status = 'Late') AS late_orders,
       ROUND(100.0 * COUNT(*) FILTER (WHERE delivery_status = 'Late')
             / NULLIF(COUNT(*) FILTER (WHERE delivery_status IN ('Late', 'On time')), 0), 2) AS late_rate_pct,
       COUNT(*) FILTER (WHERE delivery_status = 'Not delivered') AS not_delivered,
       COUNT(*) FILTER (WHERE delivery_status = 'Invalid dates') AS invalid_dates
FROM classified
GROUP BY shipper_name
ORDER BY late_rate_pct DESC NULLS LAST, shipper_name;
```

### Official-answer SQLite adaptation

```sql
WITH classified AS (
    SELECT COALESCE(sh.CompanyName, 'Unknown shipper') AS shipper_name,
           CASE
               WHEN o.DeliveryDate IS NULL THEN 'Not delivered'
               WHEN date(o.DeliveryDate) < date(o.OrderDate)
                 OR date(o.ShipDate) < date(o.OrderDate)
                 OR date(o.DeliveryDate) < date(o.ShipDate) THEN 'Invalid dates'
               WHEN julianday(o.DeliveryDate) - julianday(o.OrderDate) > 7 THEN 'Late'
               ELSE 'On time'
           END AS delivery_status
    FROM Orders AS o
    LEFT JOIN Shippers AS sh ON sh.ShipperID = o.ShipperID
)
SELECT shipper_name,
       SUM(CASE WHEN delivery_status IN ('Late', 'On time') THEN 1 ELSE 0 END) AS delivered_orders,
       SUM(CASE WHEN delivery_status = 'Late' THEN 1 ELSE 0 END) AS late_orders,
       ROUND(100.0 * SUM(CASE WHEN delivery_status = 'Late' THEN 1 ELSE 0 END)
             / NULLIF(SUM(CASE WHEN delivery_status IN ('Late', 'On time') THEN 1 ELSE 0 END), 0), 2) AS late_rate_pct,
       SUM(CASE WHEN delivery_status = 'Not delivered' THEN 1 ELSE 0 END) AS not_delivered,
       SUM(CASE WHEN delivery_status = 'Invalid dates' THEN 1 ELSE 0 END) AS invalid_dates
FROM classified
GROUP BY shipper_name
ORDER BY late_rate_pct DESC NULLS LAST, shipper_name;
```

### Official-answer SQL Server adaptation

```sql
WITH classified AS (
    SELECT COALESCE(sh.CompanyName, 'Unknown shipper') AS shipper_name,
           CASE
               WHEN o.DeliveryDate IS NULL THEN 'Not delivered'
               WHEN CAST(o.DeliveryDate AS date) < CAST(o.OrderDate AS date)
                 OR CAST(o.ShipDate AS date) < CAST(o.OrderDate AS date)
                 OR CAST(o.DeliveryDate AS date) < CAST(o.ShipDate AS date) THEN 'Invalid dates'
               WHEN DATEDIFF(day, CAST(o.OrderDate AS date), CAST(o.DeliveryDate AS date)) > 7 THEN 'Late'
               ELSE 'On time'
           END AS delivery_status
    FROM Orders AS o
    LEFT JOIN Shippers AS sh ON sh.ShipperID = o.ShipperID
)
SELECT shipper_name,
       SUM(CASE WHEN delivery_status IN ('Late', 'On time') THEN 1 ELSE 0 END) AS delivered_orders,
       SUM(CASE WHEN delivery_status = 'Late' THEN 1 ELSE 0 END) AS late_orders,
       ROUND(100.0 * SUM(CASE WHEN delivery_status = 'Late' THEN 1 ELSE 0 END)
             / NULLIF(SUM(CASE WHEN delivery_status IN ('Late', 'On time') THEN 1 ELSE 0 END), 0), 2) AS late_rate_pct,
       SUM(CASE WHEN delivery_status = 'Not delivered' THEN 1 ELSE 0 END) AS not_delivered,
       SUM(CASE WHEN delivery_status = 'Invalid dates' THEN 1 ELSE 0 END) AS invalid_dates
FROM classified
GROUP BY shipper_name
ORDER BY CASE WHEN SUM(CASE WHEN delivery_status IN ('Late', 'On time') THEN 1 ELSE 0 END) = 0 THEN 1 ELSE 0 END,
         late_rate_pct DESC, shipper_name;
```

The dialect adaptations assume date-valued columns. No SQL Server execution is claimed.

## Comparison with the course answer

The learner's locked SQLite query remains verbatim; the course answer is a separate PostgreSQL query.

| Area | Locked learner query | Course answer |
|---|---|---|
| Starting population | Shippers FULL OUTER JOIN Orders | Orders LEFT JOIN Shippers |
| Row preservation | Retains shippers and all orders, including NULL/unmatched ShipperID orders | Retains orders but omits shippers with no orders |
| Unknown IDs | Groups by resolved ShipperID and label, so unknown IDs remain distinct | Groups by label only, merging unmatched and NULL IDs |
| Output grain | One row per resolved ShipperID + shipper_name | One row per shipper_name |
| Date classification | Independent flags; late requires all dates and a valid sequence | Status CASE: not delivered, invalid comparisons, late > 7 days, else on time |
| Missing ShipDate with present DeliveryDate | Delivered, but not late | Can be Late when DeliveryDate − OrderDate > 7 and no invalid comparison is true |
| Zero-order shipper | Preserved, but currently miscounted as one not-delivered order by the NULL-extended row | Not represented because Orders drives the query |
| Ordering | Rate descending only; ties unspecified | Rate descending NULLS LAST, then shipper_name |

**Discovered locked-query defect:** the FULL OUTER JOIN creates a NULL-extended Orders row for a shipper with no orders. Since `not_delivered` tests only `O.DeliveryDate IS NULL`, it counts that synthetic row as one order. The learner query is preserved; this edge case is not marked passed. The course answer has a different population and grouping grain, so the two answers should not be silently normalized.

## Verification

- **Learner SQLite query:** executed verbatim with SQLite 3.46.1 against the five-order practice fixture. Output matched: FastShip (2 delivered, 1 late, 50.00%, 1 not delivered, 1 invalid) and QuickShip (1, 0, 0.00%, 0, 0).
- **Unknown/NULL ShipperID edge fixture:** executed. Unmatched ID 99 and NULL ID survive as separate Unknown shipper groups. A delivered row with missing ShipDate is counted as delivered but not late.
- **Discovered defect:** a shipper with no Orders row receives `not_delivered = 1` because the FULL OUTER JOIN's NULL-extended row satisfies the flag. The locked query remains unchanged; this case is not passed.
- **Zero delivered orders:** percentage returns NULL through NULLIF. The no-order shipper still exposes the not_delivered defect.
- **Strict boundary:** exactly seven days is not late; the saved condition is `> 7`.
- **Official SQLite adaptation:** executed on the five-order sample and matched its expected output.
- **SQL Server adaptations:** written separately; not executed on SQL Server.
- **Visuals and progressive stages:** still pending. No flowchart, progressive SVG or generated Previous/Next pages are claimed.
- **Approach score:** absent from saved history; not invented.
- **Status:** learner solution and source comparison saved; full PNP-P026 completion gate remains pending.
