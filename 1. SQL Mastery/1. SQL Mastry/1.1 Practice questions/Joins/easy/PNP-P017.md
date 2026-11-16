# PNP P017 — Orders with payment type and shipper

**Topic:** Joins  
**Difficulty:** Easy

## Question

The operations team needs every order from the **last seven calendar days covered by the data**, ending on the latest `OrderDate` in `Orders`.

Return `OrderID`, `OrderDate`, `payment_type`, and `shipper_name`. Use `Payments.PaymentType` and `Shippers.CompanyName`. If an order’s payment or shipper ID is `NULL` or has no match, keep the order and show `Unknown` for that field. Sort by `OrderDate` descending, then `OrderID` descending.

### Sample input

**`Orders`**

| OrderID | OrderDate | PaymentID | ShipperID |
|---:|---|---:|---:|
| 1 | 2025-12-24 | 1 | 1 |
| 2 | 2025-12-25 | 1 | 1 |
| 3 | 2025-12-31 | `NULL` | `NULL` |

**`Payments`**

| PaymentID | PaymentType |
|---:|---|
| 1 | UPI |

**`Shippers`**

| ShipperID | CompanyName |
|---:|---|
| 1 | FastShip |

### Expected output

| OrderID | OrderDate | payment_type | shipper_name |
|---:|---|---|---|
| 3 | 2025-12-31 | Unknown | Unknown |
| 2 | 2025-12-25 | UPI | FastShip |

The latest order date is December 31, so the seven-day window is **December 25–31 inclusive**. Order 3 stays in the report even though both IDs are missing.

## Learner submission — SQLite

```sql
SELECT
    o.OrderID,
    o.OrderDate,
    COALESCE(p.PaymentType, 'Unknown') AS payment_type,
    COALESCE(s.CompanyName, 'Unknown') AS shipper_name
FROM Orders AS o
LEFT JOIN Payments AS p ON o.PaymentID = p.PaymentID
LEFT JOIN Shippers AS s ON o.ShipperID = s.ShipperID
WHERE date(o.OrderDate) >= (
    SELECT date(MAX(OrderDate), '-6 days')
    FROM Orders
)
ORDER BY o.OrderDate DESC, o.OrderID DESC;
```

This was a guided submission. The SQLite checks covered the sample, missing and unmatched lookup IDs, a rolling window crossing into a new year, a first-day timestamp, equal timestamps, and an empty Orders table.

## Step-by-step walkthrough

One output row represents one order in the reporting window. Use the same sample for each step.

### 1. Attach payment and shipper details

**What to do.** Match each lookup directly to its own ID on Orders.

**Why these joins.** Both lookups are optional. Each LEFT JOIN retains the order when its lookup has no match. The two lookups work independently, so an order with an unknown payment may still have a known shipper.

```sql
SELECT o.OrderID, o.OrderDate, p.PaymentType, s.CompanyName
FROM Orders AS o
LEFT JOIN Payments AS p ON o.PaymentID = p.PaymentID
LEFT JOIN Shippers AS s ON o.ShipperID = s.ShipperID
ORDER BY o.OrderID;
```

| OrderID | OrderDate | PaymentType | CompanyName |
|---:|---|---|---|
| 1 | 2025-12-24 | UPI | FastShip |
| 2 | 2025-12-25 | UPI | FastShip |
| 3 | 2025-12-31 | `NULL` | `NULL` |

### 2. Find the data's latest date and window start

**What to do.** Take the maximum order date and subtract six calendar days.

**Why.** The latest day itself counts as one of the seven days. Using MAX makes the window move as new orders arrive.

```sql
SELECT date(MAX(OrderDate)) AS latest_order_date,
       date(MAX(OrderDate), '-6 days') AS window_start
FROM Orders;
```

| latest_order_date | window_start |
|---|---|
| 2025-12-31 | 2025-12-25 |

### 3. Keep orders on or after the start

**What to do.** Use the calculated start in WHERE. Keep the original OrderDate in the output while comparing its calendar date.

**Why.** December 25 is included. No upper bound is needed because no order has a date later than the maximum of the same Orders table.

```sql
SELECT o.OrderID, o.OrderDate, p.PaymentType, s.CompanyName
FROM Orders AS o
LEFT JOIN Payments AS p ON o.PaymentID = p.PaymentID
LEFT JOIN Shippers AS s ON o.ShipperID = s.ShipperID
WHERE date(o.OrderDate) >= (
    SELECT date(MAX(OrderDate), '-6 days')
    FROM Orders
)
ORDER BY o.OrderID;
```

| OrderID | OrderDate | PaymentType | CompanyName |
|---:|---|---|---|
| 2 | 2025-12-25 | UPI | FastShip |
| 3 | 2025-12-31 | `NULL` | `NULL` |

### 4. Label missing values and sort newest first

**What to do.** Apply COALESCE to each lookup label and sort by date descending, then ID descending. Run the final SQLite query above.

**Why.** Missing lookups should be visible as Unknown. Order ID resolves a tie on OrderDate.

| OrderID | OrderDate | payment_type | shipper_name |
|---:|---|---|---|
| 3 | 2025-12-31 | Unknown | Unknown |
| 2 | 2025-12-25 | UPI | FastShip |

## Learner submission — SQL Server adaptation

```sql
SELECT
    o.OrderID,
    o.OrderDate,
    COALESCE(p.PaymentType, 'Unknown') AS payment_type,
    COALESCE(s.CompanyName, 'Unknown') AS shipper_name
FROM Orders AS o
LEFT JOIN Payments AS p ON o.PaymentID = p.PaymentID
LEFT JOIN Shippers AS s ON o.ShipperID = s.ShipperID
WHERE CAST(o.OrderDate AS date) >= (
    SELECT DATEADD(day, -6, CAST(MAX(OrderDate) AS date))
    FROM Orders
)
ORDER BY o.OrderDate DESC, o.OrderID DESC;
```

Uses DATEADD and a date cast. Reviewed by inspection.

## Official solution

[PNP answer key, Q17](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT o.OrderID,
       o.OrderDate,
       COALESCE(pay.PaymentType, 'Unknown') AS payment_type,
       COALESCE(sh.CompanyName, 'Unknown')  AS shipper_name
FROM Orders AS o
LEFT JOIN Payments AS pay ON pay.PaymentID = o.PaymentID
LEFT JOIN Shippers AS sh  ON sh.ShipperID  = o.ShipperID
WHERE o.OrderDate >= (SELECT MAX(latest.OrderDate)::date - 6 FROM Orders AS latest)
ORDER BY o.OrderDate DESC, o.OrderID DESC;
```

### Official answer — SQLite adaptation

```sql
SELECT o.OrderID,
       o.OrderDate,
       COALESCE(pay.PaymentType, 'Unknown') AS payment_type,
       COALESCE(sh.CompanyName, 'Unknown')  AS shipper_name
FROM Orders AS o
LEFT JOIN Payments AS pay ON pay.PaymentID = o.PaymentID
LEFT JOIN Shippers AS sh  ON sh.ShipperID  = o.ShipperID
WHERE date(o.OrderDate) >= (SELECT date(MAX(latest.OrderDate), '-6 days') FROM Orders AS latest)
ORDER BY o.OrderDate DESC, o.OrderID DESC;
```

### Official answer — SQL Server adaptation

```sql
SELECT o.OrderID,
       o.OrderDate,
       COALESCE(pay.PaymentType, 'Unknown') AS payment_type,
       COALESCE(sh.CompanyName, 'Unknown')  AS shipper_name
FROM Orders AS o
LEFT JOIN Payments AS pay ON pay.PaymentID = o.PaymentID
LEFT JOIN Shippers AS sh  ON sh.ShipperID  = o.ShipperID
WHERE o.OrderDate >= (SELECT DATEADD(day, -6, CAST(MAX(latest.OrderDate) AS date)) FROM Orders AS latest)
ORDER BY o.OrderDate DESC, o.OrderID DESC;
```

The SQLite adaptation passed the sample and extended fixture. The SQL Server adaptations were reviewed by inspection.
