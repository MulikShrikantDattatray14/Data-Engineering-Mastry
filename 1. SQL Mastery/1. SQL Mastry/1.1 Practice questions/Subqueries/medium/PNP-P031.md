# PNP P031 — Customers who spend more than the average customer

**Topic** Subqueries · **Difficulty** ![MEDIUM](../../../_badges/medium.svg) · **Restart practice** 2026-11-19

[Question and required columns](../../../2.PNP-%20foundations%20and%20practice/6.%20SubQueries/P031.%20Customers%20who%20spend%20more%20than%20the%20average%20customer.md#question-and-image) · [Practice input and expected output](../../../2.PNP-%20foundations%20and%20practice/6.%20SubQueries/P031.%20Customers%20who%20spend%20more%20than%20the%20average%20customer.md#sample-input-and-expected-output) · [Source-colored sample tables](../../assets/question-samples/p031.svg?raw=1)

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

## Sample verification

Executed in SQLite on the three orders in the practice example. Asha, Ben and Cia spend 300, 100 and 200 respectively. The scalar subquery returns 200. The strict comparison excludes Cia, whose total equals the average.

| 🟦 CustomerID | 🟩 customer_name | 🟦 total_spend | 🟦 avg_customer_spend | 🟦 pct_above_avg |
| ---: | --- | ---: | ---: | ---: |
| 1 | Asha Rao | 300 | 200.0 | 50.0 |

## Comparison with the course answer

- Adding an order worth 1000 with a `NULL` customer ID to the practice data produces a fourth group in the submitted query. SQLite returns that group with a total of 1000 and an average of 400. The course answer excludes orders with a `NULL` customer ID before it calculates the average.
- Giving that same order customer ID 99, which has no customer record, returns `Unknown` in the submission. The course uses `Unknown customer` for an unmatched ID and joins the available name parts for a matched customer.
- The submission returns the unrounded average and percentage and sorts by descending spend. The course rounds both displayed calculations to two decimals and uses customer ID to break spending ties. Both compare totals with the unrounded average.

[Official PostgreSQL answer, Q31](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/fa70de6416696e0d6ab94faee964e048f9552ecd/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql#L370-L393)
