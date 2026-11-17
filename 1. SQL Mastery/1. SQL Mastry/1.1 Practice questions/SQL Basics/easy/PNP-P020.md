# PNP P020 — Days to ship and days to deliver

**Topic:** Dates  
**Difficulty:** Easy

## Question

The logistics team wants a report for **every order placed in November 2025**. Return the order ID, all three dates, and two numbers in whole calendar days:

- `days_to_ship` is the number of days from `OrderDate` to `ShipDate`.
- `days_to_deliver` is the number of days from `OrderDate` to `DeliveryDate`.

Keep orders with missing shipping or delivery dates. Return `NULL` for the corresponding calculation. Sort by `OrderDate` ascending, then `OrderID` ascending.

### Sample input · `Orders`

| OrderID | OrderDate | ShipDate | DeliveryDate |
|---:|---|---|---|
| 1 | 2025-11-01 | 2025-11-03 | 2025-11-06 |
| 2 | 2025-11-02 | `NULL` | `NULL` |
| 3 | 2025-10-31 | 2025-11-01 | 2025-11-04 |

### Expected output

| OrderID | OrderDate | ShipDate | DeliveryDate | days_to_ship | days_to_deliver |
|---:|---|---|---|---:|---:|
| 1 | 2025-11-01 | 2025-11-03 | 2025-11-06 | 2 | 5 |
| 2 | 2025-11-02 | `NULL` | `NULL` | `NULL` | `NULL` |

## Learner submission — SQLite

```sql
SELECT OrderID, OrderDate, ShipDate, DeliveryDate,
       CAST(julianday(date(ShipDate)) - julianday(date(OrderDate)) AS INTEGER) AS days_to_ship,
       CAST(julianday(date(DeliveryDate)) - julianday(date(OrderDate)) AS INTEGER) AS days_to_deliver
FROM Orders
WHERE strftime("%m", OrderDate) = '11' AND strftime("%Y", OrderDate) = '2025'
ORDER BY OrderDate ASC, `OrderID` ASC;
```

Guided submission. Chat formatting was cleaned up. The tested SQLite configuration accepts the double-quoted format strings. Single quotes are the standard spelling.

## Step-by-step walkthrough

One final row represents one order. All output fields come from Orders.

### 1. Keep November 2025 orders

**What to do.** Match both the month and year of OrderDate.

**Why.** The reporting period depends on when the order was placed. Order 3 was shipped in November but placed in October. Order 2 stays even though it has no shipping or delivery date.

```sql
SELECT OrderID, OrderDate, ShipDate, DeliveryDate
FROM Orders
WHERE strftime("%m", OrderDate) = '11' AND strftime("%Y", OrderDate) = '2025'
ORDER BY OrderDate ASC, `OrderID` ASC;
```

| OrderID | OrderDate | ShipDate | DeliveryDate |
|---:|---|---|---|
| 1 | 2025-11-01 | 2025-11-03 | 2025-11-06 |
| 2 | 2025-11-02 | `NULL` | `NULL` |

### 2. Calculate the calendar-day differences and sort

**What to do.** Convert the dates to numeric day values, subtract the order day from each later day, and return integers. Sort by order date, then order ID.

**Why.** Subtracting raw date strings in SQLite can subtract just their leading years. The inner date calls discard time, so crossing midnight counts as one calendar day. Each missing date affects only its own metric. The ID breaks order-date ties.

```sql
SELECT OrderID, OrderDate, ShipDate, DeliveryDate,
       CAST(julianday(date(ShipDate)) - julianday(date(OrderDate)) AS INTEGER) AS days_to_ship,
       CAST(julianday(date(DeliveryDate)) - julianday(date(OrderDate)) AS INTEGER) AS days_to_deliver
FROM Orders
WHERE strftime("%m", OrderDate) = '11' AND strftime("%Y", OrderDate) = '2025'
ORDER BY OrderDate ASC, `OrderID` ASC;
```

| OrderID | OrderDate | ShipDate | DeliveryDate | days_to_ship | days_to_deliver |
|---:|---|---|---|---:|---:|
| 1 | 2025-11-01 | 2025-11-03 | 2025-11-06 | 2 | 5 |
| 2 | 2025-11-02 | `NULL` | `NULL` | `NULL` | `NULL` |

SQLite checks covered the sample, each missing date independently, late November orders, a midnight crossing, orders outside the month or year, and ties.

## Learner submission — SQL Server adaptation

```sql
SELECT OrderID, OrderDate, ShipDate, DeliveryDate,
       DATEDIFF(day, OrderDate, ShipDate) AS days_to_ship,
       DATEDIFF(day, OrderDate, DeliveryDate) AS days_to_deliver
FROM Orders
WHERE MONTH(OrderDate) = 11 AND YEAR(OrderDate) = 2025
ORDER BY OrderDate ASC, OrderID ASC;
```

Uses DATEDIFF with day boundaries and the equivalent year and month checks. Reviewed by inspection.

## Official solution

[PNP answer key, Q20](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT o.OrderID,
       o.OrderDate,
       o.ShipDate,
       o.DeliveryDate,
       o.ShipDate::date     - o.OrderDate::date AS days_to_ship,
       o.DeliveryDate::date - o.OrderDate::date AS days_to_deliver
FROM Orders AS o
WHERE o.OrderDate >= DATE '2025-11-01'
  AND o.OrderDate <  DATE '2025-12-01'
ORDER BY o.OrderDate, o.OrderID;
```

### Official answer — SQLite adaptation

```sql
SELECT o.OrderID,
       o.OrderDate,
       o.ShipDate,
       o.DeliveryDate,
       CAST(julianday(date(o.ShipDate)) - julianday(date(o.OrderDate)) AS INTEGER) AS days_to_ship,
       CAST(julianday(date(o.DeliveryDate)) - julianday(date(o.OrderDate)) AS INTEGER) AS days_to_deliver
FROM Orders AS o
WHERE o.OrderDate >= '2025-11-01'
  AND o.OrderDate <  '2025-12-01'
ORDER BY o.OrderDate, o.OrderID;
```

### Official answer — SQL Server adaptation

```sql
SELECT o.OrderID,
       o.OrderDate,
       o.ShipDate,
       o.DeliveryDate,
       DATEDIFF(day, o.OrderDate, o.ShipDate) AS days_to_ship,
       DATEDIFF(day, o.OrderDate, o.DeliveryDate) AS days_to_deliver
FROM Orders AS o
WHERE o.OrderDate >= DATEFROMPARTS(2025, 11, 1)
  AND o.OrderDate <  DATEFROMPARTS(2025, 12, 1)
ORDER BY o.OrderDate, o.OrderID;
```

The official answer uses an inclusive November 1 lower bound and an exclusive December 1 upper bound. The SQLite adaptation was checked against the learner query on the sample and a boundary fixture. The SQL Server versions were reviewed by inspection.
