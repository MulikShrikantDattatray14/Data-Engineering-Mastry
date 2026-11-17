# PNP P018 — Customers with no order in the last 90 days

**Topic:** Joins  
**Difficulty:** Easy

## Question

The retention team wants one row per registered customer who **placed no order in the last 90 calendar days covered by the data**. The window ends on the latest `OrderDate` in `Orders`, and both boundary days count. Include customers who only ordered before the window and customers who never ordered.

Return `CustomerID`, `customer_name` (first and last name joined with a space), `Email`, and `DateEntered`. Sort by `DateEntered` ascending, then by `CustomerID` ascending.

### Sample input

**`Customers`**

| CustomerID | FirstName | LastName | Email | DateEntered |
|---:|---|---|---|---|
| 1 | Asha | Rao | asha@example.com | 2023-01-01 |
| 2 | Ben | Das | ben@example.com | 2023-02-01 |
| 3 | Cia | Sen | cia@example.com | 2024-01-01 |

**`Orders`**

| OrderID | CustomerID | OrderDate |
|---:|---:|---|
| 10 | 1 | 2025-03-31 |
| 11 | 2 | 2024-12-01 |

### Expected output

| CustomerID | customer_name | Email | DateEntered |
|---:|---|---|---|
| 2 | Ben Das | ben@example.com | 2023-02-01 |
| 3 | Cia Sen | cia@example.com | 2024-01-01 |

Asha ordered within the window. Ben’s only order was before it, and Cia never ordered, so both qualify.

## Final learner submission — SQLite

```sql
WITH reporting_window AS (
    SELECT
        date(MAX(OrderDate)) AS latest_order_date,
        date(MAX(OrderDate), '-89 days') AS window_start
    FROM Orders
)
SELECT
    c.CustomerID,
    c.FirstName || ' ' || c.LastName AS customer_name,
    c.Email,
    c.DateEntered
FROM Customers AS c
LEFT JOIN Orders AS o
    ON o.CustomerID = c.CustomerID
   AND date(o.OrderDate) BETWEEN
       (SELECT window_start FROM reporting_window)
       AND (SELECT latest_order_date FROM reporting_window)
WHERE o.OrderID IS NULL
ORDER BY c.DateEntered ASC, c.CustomerID ASC;
```

Guided submission. This final version uses table aliases and a single-quoted space. Verified on the sample, a first-day timestamp for a customer with an older order, and an empty Orders table.

## Step-by-step walkthrough

### 1. Calculate the 90-day window

**What to do.** Find the latest order date and subtract 89 days.

**Why.** The latest day itself counts toward the 90 days. Customer sign-up dates do not set the window.

```sql
WITH reporting_window AS (
    SELECT date(MAX(OrderDate)) AS latest_order_date,
           date(MAX(OrderDate), '-89 days') AS window_start
    FROM Orders
)
SELECT latest_order_date, window_start FROM reporting_window;
```

| latest_order_date | window_start |
|---|---|
| 2025-03-31 | 2025-01-01 |

### 2. Match only orders inside the window

**What to do.** Join Customers to Orders on customer ID and apply the date range in ON.

**Why this join.** LEFT JOIN retains customers with no qualifying order. The date condition in ON makes Ben's old order ineligible to match while still retaining Ben. Cia also stays because the join preserves customers who never ordered.

```sql
WITH reporting_window AS (
    SELECT date(MAX(OrderDate)) AS latest_order_date,
           date(MAX(OrderDate), '-89 days') AS window_start
    FROM Orders
)
SELECT Customers.CustomerID, Orders.OrderID AS matched_order_id, Orders.OrderDate AS matched_order_date
FROM Customers
LEFT JOIN Orders
    ON Orders.CustomerID = Customers.CustomerID
   AND date(Orders.OrderDate) BETWEEN
       (SELECT window_start FROM reporting_window)
       AND (SELECT latest_order_date FROM reporting_window)
ORDER BY Customers.CustomerID;
```

| CustomerID | matched_order_id | matched_order_date |
|---:|---:|---|
| 1 | 10 | 2025-03-31 |
| 2 | NULL | NULL |
| 3 | NULL | NULL |

### 3. Keep customers with no recent match

**What to do.** Add WHERE Orders.OrderID IS NULL to the preview.

**Why.** Ben and Cia have no matching order inside the window, so their joined order IDs are NULL.

```sql
WITH reporting_window AS (
    SELECT date(MAX(OrderDate)) AS latest_order_date,
           date(MAX(OrderDate), '-89 days') AS window_start
    FROM Orders
)
SELECT Customers.CustomerID, Orders.OrderID AS matched_order_id, Orders.OrderDate AS matched_order_date
FROM Customers
LEFT JOIN Orders
    ON Orders.CustomerID = Customers.CustomerID
   AND date(Orders.OrderDate) BETWEEN
       (SELECT window_start FROM reporting_window)
       AND (SELECT latest_order_date FROM reporting_window)
WHERE Orders.OrderID IS NULL
ORDER BY Customers.CustomerID;
```

| CustomerID | matched_order_id | matched_order_date |
|---:|---|---|
| 2 | NULL | NULL |
| 3 | NULL | NULL |

### 4. Select the customer details and sort

**What to do.** Use WHERE to retain rows with a NULL order ID and apply the two ascending sort keys.

**Why.** A NULL order ID indicates the recent-order join found no match. Testing whether an order is outside the window could let a customer with both an old and a recent order through. The customer ID breaks sign-up date ties.

```sql
WITH reporting_window AS (
    SELECT
        date(MAX(OrderDate)) AS latest_order_date,
        date(MAX(OrderDate), '-89 days') AS window_start
    FROM Orders
)
SELECT
    c.CustomerID,
    c.FirstName || ' ' || c.LastName AS customer_name,
    c.Email,
    c.DateEntered
FROM Customers AS c
LEFT JOIN Orders AS o
    ON o.CustomerID = c.CustomerID
   AND date(o.OrderDate) BETWEEN
       (SELECT window_start FROM reporting_window)
       AND (SELECT latest_order_date FROM reporting_window)
WHERE o.OrderID IS NULL
ORDER BY c.DateEntered ASC, c.CustomerID ASC;
```

| CustomerID | customer_name | Email | DateEntered |
|---:|---|---|---|
| 2 | Ben Das | ben@example.com | 2023-02-01 |
| 3 | Cia Sen | cia@example.com | 2024-01-01 |

The SQLite checks covered the original sample, a customer with both old and recent orders, timestamps on both boundary dates, tied sign-up dates, and empty Orders.

## Learner submission — SQL Server adaptation

```sql
;WITH reporting_window AS (
    SELECT CAST(MAX(OrderDate) AS date) AS latest_order_date,
           DATEADD(day, -89, CAST(MAX(OrderDate) AS date)) AS window_start
    FROM Orders
)
SELECT Customers.CustomerID,
       (Customers.FirstName + ' ' + Customers.LastName) AS customer_name,
       Customers.Email,
       Customers.DateEntered
FROM Customers
LEFT JOIN Orders
    ON Orders.CustomerID = Customers.CustomerID
   AND CAST(Orders.OrderDate AS date) BETWEEN
       (SELECT window_start FROM reporting_window)
       AND (SELECT latest_order_date FROM reporting_window)
WHERE Orders.OrderID IS NULL
ORDER BY Customers.DateEntered, Customers.CustomerID ASC;
```

Uses CAST and DATEADD for the calendar boundaries and single quotes for the joining space. Reviewed by inspection.

## Official solution

[PNP answer key, Q18](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT c.CustomerID,
       CONCAT_WS(' ', c.FirstName, c.LastName) AS customer_name,
       c.Email,
       c.DateEntered
FROM Customers AS c
LEFT JOIN Orders AS o
       ON o.CustomerID = c.CustomerID
      AND o.OrderDate >= (SELECT MAX(OrderDate) FROM Orders) - 89
WHERE o.OrderID IS NULL
ORDER BY c.DateEntered, c.CustomerID;
```

### Official answer — SQLite adaptation

```sql
SELECT c.CustomerID,
       CASE WHEN c.FirstName IS NULL THEN COALESCE(c.LastName, '')
            WHEN c.LastName IS NULL THEN c.FirstName
            ELSE c.FirstName || ' ' || c.LastName END AS customer_name,
       c.Email,
       c.DateEntered
FROM Customers AS c
LEFT JOIN Orders AS o
       ON o.CustomerID = c.CustomerID
      AND date(o.OrderDate) >= (SELECT date(MAX(OrderDate), '-89 days') FROM Orders)
WHERE o.OrderID IS NULL
ORDER BY c.DateEntered, c.CustomerID;
```

### Official answer — SQL Server adaptation

```sql
SELECT c.CustomerID,
       CONCAT_WS(' ', c.FirstName, c.LastName) AS customer_name,
       c.Email,
       c.DateEntered
FROM Customers AS c
LEFT JOIN Orders AS o
       ON o.CustomerID = c.CustomerID
      AND o.OrderDate >= (SELECT DATEADD(day, -89, CAST(MAX(OrderDate) AS date)) FROM Orders)
WHERE o.OrderID IS NULL
ORDER BY c.DateEntered, c.CustomerID;
```

The official version needs only a lower-bound check because its window ends on the latest order date in the same table. Its name formatting skips missing name parts. The SQLite adaptation was executed on the sample and extended fixtures. The SQL Server versions were reviewed by inspection.
