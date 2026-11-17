# PNP P021 — Top five customers by number of orders

**Topic:** Joins and aggregation  
**Difficulty:** Easy

## Question

The CRM team wants to reward its most frequent buyers. Rank customers by **how many orders they placed**. Order value doesn’t matter.

- Return the **top five customers**, including everyone tied with the customer in fifth place. The result can contain more than five rows.
- If a `CustomerID` appears in `Orders` but has no matching row in `Customers`, keep that ID eligible for the ranking and display `Unknown customer` as its name.
- Return `CustomerID`, `customer_name` (first and last names joined with a space), and `orders_placed`.
- Sort by `orders_placed` descending, then `CustomerID` ascending.

### Extended sample input

**Customers**

| CustomerID | FirstName | LastName |
|---:|---|---|
| 1 | Asha | Rao |
| 2 | Ben | Das |
| 3 | Cia | Sen |
| 4 | Dev | Roy |
| 5 | Ena | Jain |
| 6 | Farah | Ali |
| 7 | Gita | Shah |

**Orders**

| OrderID | CustomerID |
|---:|---:|
| 11 | 1 |
| 12 | 2 |
| 13 | 3 |
| 14 | 4 |
| 15 | 5 |
| 16 | 6 |
| 17 | 99 |
| 18 | 99 |
| 19 | 99 |

### Expected output

| CustomerID | customer_name | orders_placed |
|---:|---|---:|
| 99 | Unknown customer | 3 |
| 1 | Asha Rao | 1 |
| 2 | Ben Das | 1 |
| 3 | Cia Sen | 1 |
| 4 | Dev Roy | 1 |
| 5 | Ena Jain | 1 |
| 6 | Farah Ali | 1 |

ID 99 placed three orders and has no customer record. ID 7 placed none. The fifth row has one order, so everyone tied at that count qualifies.

## Final learner submission — SQLite

```sql
WITH customer_counts AS (
    SELECT
        o.CustomerID,
        COALESCE(c.FirstName || ' ' || c.LastName, 'Unknown customer') AS customer_name,
        COUNT(o.OrderID) AS orders_placed
    FROM Orders AS o
    LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
    GROUP BY o.CustomerID, c.FirstName, c.LastName
)
SELECT CustomerID, customer_name, orders_placed
FROM customer_counts
WHERE orders_placed >= COALESCE(
    (
        SELECT orders_placed
        FROM customer_counts
        ORDER BY orders_placed DESC
        LIMIT 1 OFFSET 4
    ),
    0
)
ORDER BY orders_placed DESC, CustomerID ASC;
```

Guided submission. The learner chose grouping by customer ID, counting orders, and preserving unmatched customer IDs. The cutoff subquery was developed with guidance.

## Step-by-step walkthrough

### 1. Build one row per customer ID that placed an order

**What to do.** Start from Orders, join customer names, and count orders for each customer ID.

**Why this join.** The LEFT JOIN keeps orders for ID 99 even without a catalogue match. ID 7 has no order and never enters the ranking.

```sql
WITH customer_counts AS (
    SELECT
        o.CustomerID,
        COALESCE(c.FirstName || ' ' || c.LastName, 'Unknown customer') AS customer_name,
        COUNT(o.OrderID) AS orders_placed
    FROM Orders AS o
    LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
    GROUP BY o.CustomerID, c.FirstName, c.LastName
)
SELECT * FROM customer_counts
ORDER BY orders_placed DESC, CustomerID ASC;
```

| CustomerID | customer_name | orders_placed |
|---:|---|---:|
| 99 | Unknown customer | 3 |
| 1 | Asha Rao | 1 |
| 2 | Ben Das | 1 |
| 3 | Cia Sen | 1 |
| 4 | Dev Roy | 1 |
| 5 | Ena Jain | 1 |
| 6 | Farah Ali | 1 |

These are the candidate counts before the cutoff. The learner's COALESCE also supplies the fallback when a matched customer's name has a NULL part.

### 2. Find the fifth row's count

**What to do.** Sort the counts descending, skip four rows, and read the next count. Use zero when the fifth row is absent.

**Why.** The fifth row sets the minimum qualifying count. The fallback keeps all eligible customers when there are fewer than five.

```sql
WITH customer_counts AS (
    SELECT
        o.CustomerID,
        COALESCE(c.FirstName || ' ' || c.LastName, 'Unknown customer') AS customer_name,
        COUNT(o.OrderID) AS orders_placed
    FROM Orders AS o
    LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
    GROUP BY o.CustomerID, c.FirstName, c.LastName
)
SELECT COALESCE((SELECT orders_placed FROM customer_counts
                 ORDER BY orders_placed DESC LIMIT 1 OFFSET 4), 0) AS cutoff;
```

| cutoff |
|---:|
| 1 |

### 3. Keep everyone who meets the cutoff and sort

**What to do.** Use the cutoff in the outer WHERE and apply the requested sort.

**Why.** The >= comparison includes everyone tied at the cutoff. CustomerID controls the display order of ties.

```sql
WITH customer_counts AS (
    SELECT
        o.CustomerID,
        COALESCE(c.FirstName || ' ' || c.LastName, 'Unknown customer') AS customer_name,
        COUNT(o.OrderID) AS orders_placed
    FROM Orders AS o
    LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
    GROUP BY o.CustomerID, c.FirstName, c.LastName
)
SELECT CustomerID, customer_name, orders_placed
FROM customer_counts
WHERE orders_placed >= COALESCE(
    (
        SELECT orders_placed
        FROM customer_counts
        ORDER BY orders_placed DESC
        LIMIT 1 OFFSET 4
    ),
    0
)
ORDER BY orders_placed DESC, CustomerID ASC;
```

| CustomerID | customer_name | orders_placed |
|---:|---|---:|
| 99 | Unknown customer | 3 |
| 1 | Asha Rao | 1 |
| 2 | Ben Das | 1 |
| 3 | Cia Sen | 1 |
| 4 | Dev Roy | 1 |
| 5 | Ena Jain | 1 |
| 6 | Farah Ali | 1 |

In an extended boundary test with counts 9, 8, 7, 6, 5, 5, and 4, the cutoff was 5 and six customers qualified. SQLite also passed the original sample, fewer than five candidates, and an empty Orders table.

## Learner submission — SQL Server adaptation

```sql
WITH customer_counts AS (
    SELECT
        o.CustomerID,
        COALESCE(c.FirstName + ' ' + c.LastName, 'Unknown customer') AS customer_name,
        COUNT(o.OrderID) AS orders_placed
    FROM Orders AS o
    LEFT JOIN Customers AS c ON o.CustomerID = c.CustomerID
    GROUP BY o.CustomerID, c.FirstName, c.LastName
)
SELECT CustomerID, customer_name, orders_placed
FROM customer_counts
WHERE orders_placed >= COALESCE(
    (
        SELECT orders_placed
        FROM customer_counts
        ORDER BY orders_placed DESC
        OFFSET 4 ROWS FETCH NEXT 1 ROW ONLY
    ),
    0
)
ORDER BY orders_placed DESC, CustomerID ASC;
```

Uses OFFSET and FETCH for the cutoff. Reviewed by inspection.

## Official solution

[PNP answer key, Q21](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT top5.CustomerID,
       top5.customer_name,
       top5.orders_placed
FROM (
    SELECT o.CustomerID,
           CASE WHEN c.CustomerID IS NULL THEN 'Unknown customer'
                ELSE CONCAT_WS(' ', c.FirstName, c.LastName)
           END      AS customer_name,
           COUNT(*) AS orders_placed
    FROM Orders AS o
    LEFT JOIN Customers AS c ON c.CustomerID = o.CustomerID
    GROUP BY o.CustomerID, c.CustomerID, c.FirstName, c.LastName
    ORDER BY orders_placed DESC
    FETCH FIRST 5 ROWS WITH TIES
) AS top5
ORDER BY top5.orders_placed DESC, top5.CustomerID;
```

### Official answer — SQLite adaptation

```sql
WITH customer_counts AS (
    SELECT o.CustomerID,
           CASE WHEN c.CustomerID IS NULL THEN 'Unknown customer'
                WHEN c.FirstName IS NULL THEN COALESCE(c.LastName, '')
                WHEN c.LastName IS NULL THEN c.FirstName
                ELSE c.FirstName || ' ' || c.LastName END AS customer_name,
           COUNT(*) AS orders_placed
    FROM Orders AS o
    LEFT JOIN Customers AS c ON c.CustomerID = o.CustomerID
    GROUP BY o.CustomerID, c.CustomerID, c.FirstName, c.LastName
), ranked AS (
    SELECT *, RANK() OVER (ORDER BY orders_placed DESC) AS order_rank
    FROM customer_counts
)
SELECT CustomerID, customer_name, orders_placed
FROM ranked
WHERE order_rank <= 5
ORDER BY orders_placed DESC, CustomerID ASC;
```

### Official answer — SQL Server adaptation

```sql
SELECT top5.CustomerID,
       top5.customer_name,
       top5.orders_placed
FROM (
    SELECT TOP (5) WITH TIES o.CustomerID,
           CASE WHEN c.CustomerID IS NULL THEN 'Unknown customer'
                ELSE CONCAT_WS(' ', c.FirstName, c.LastName)
           END      AS customer_name,
           COUNT(*) AS orders_placed
    FROM Orders AS o
    LEFT JOIN Customers AS c ON c.CustomerID = o.CustomerID
    GROUP BY o.CustomerID, c.CustomerID, c.FirstName, c.LastName
    ORDER BY orders_placed DESC
) AS top5
ORDER BY top5.orders_placed DESC, top5.CustomerID;
```

The official versions distinguish unmatched customer IDs from matched customers with missing name parts. The SQLite adaptation was executed on the sample and boundary fixtures. SQL Server versions were reviewed by inspection.
