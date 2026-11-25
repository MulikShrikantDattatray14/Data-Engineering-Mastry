# PNP P035 — Late-delivery rate by shipper

**Topic** Aggregation, conditional aggregation and CTEs · **Difficulty** Medium

> **Record status:** Learner solution and learning notes saved. Full PNP-P026 completion audit, both required visuals, SQL Server adaptation, official-answer comparison and execution verification remain pending. Do not mark this question solved or add it to the solved index yet.

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

**Learner's approach and progression**

1. Started with `Shippers LEFT JOIN Orders` on `ShipperID`, grouping by shipper ID and company name.
2. Identified `COALESCE(CompanyName, 'Unknown shipper')` for the output label.
3. Proposed conditional counting for delivered and late orders, using the date difference threshold of more than 7 days.
4. Identified that both `OrderDate` and `DeliveryDate` must be present to calculate a date difference.
5. Defined the valid chronological sequence as `OrderDate <= ShipDate <= DeliveryDate`; a fully populated sequence that violates it is invalid.
6. Identified `DeliveryDate IS NULL` for `not_delivered`.
7. Learned that `NULLIF(delivered_orders, 0)` prevents division by zero and produces NULL when the denominator is zero.
8. Revisited join preservation after noticing the source explicitly requires missing or unknown ShipperID orders to appear as Unknown shipper. Changed the join to `FULL OUTER JOIN`.
9. Refactored the nested conditional aggregates into a CTE that classifies each order with 0/1 flags, then aggregates those flags.

**Approach review:** The initial LEFT JOIN was reasonable for retaining every shipper, but insufficient for retaining unmatched Orders rows. The revised FULL OUTER JOIN satisfies both row-preservation requirements. The final CTE makes row classification separate from shipper-level aggregation.

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

**Pending.** The saved query is SQLite-specific because it uses `julianday()`. A SQL Server adaptation must use an appropriate date-difference expression and be reviewed separately. No SQL Server execution is claimed.

## Official solution

**Pending source extraction.** The official answer is retained in the supplied PDF / source archive. It has not yet been transcribed here, so no official SQL is invented.

## Comparison with the course answer

**Pending** until the exact official answer is extracted and compared with the learner's query. Preserve the learner solution and official answer as separate artifacts.

## Verification

- **Learner query:** saved verbatim; not yet executed in a SQLite engine.
- **Sample arithmetic:** manually traced against the illustrative five-order fixture; FastShip has 2 valid delivered orders, 1 late, 1 not delivered and 1 invalid; QuickShip has 1 delivered and 0 late.
- **FULL OUTER JOIN:** SQLite requires version 3.39.0 or later. Confirm the actual runtime version during execution.
- **Unknown / NULL ShipperID:** required by the source task but absent from the current illustrative fixture; add a dedicated test before verification.
- **Zero delivered orders:** test that late_rate_pct returns NULL through NULLIF.
- **Missing OrderDate / ShipDate:** test and explicitly agree whether a delivered row with incomplete date sequence belongs in delivered_orders and whether it can be late.
- **Ties:** ORDER BY late_rate_pct DESC does not define a secondary order for equal rates; add a tie-breaker only if the source requires deterministic tie ordering.
- **Status:** solution saved; full verification and PNP-P026 completion gate pending.
