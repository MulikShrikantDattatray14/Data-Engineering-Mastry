# PNP P005 — Orders placed in Q1 2025

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

From `Orders`, return every order placed from **January 1 through March 31, 2025**, inclusive. Return `OrderID`, `CustomerID`, `OrderDate`, and `Total_Order_Amount`. Sort by `OrderDate` ascending, then by `OrderID` ascending.

### Sample input

| OrderID | CustomerID | OrderDate | Total_Order_Amount |
| ---: | ---: | --- | ---: |
| 1 | 10 | 2024-12-31 | 50 |
| 2 | 11 | 2025-01-01 | 100 |
| 3 | 12 | 2025-03-31 | 200 |
| 4 | 13 | 2025-04-01 | 300 |

### Expected output

| OrderID | CustomerID | OrderDate | Total_Order_Amount |
| ---: | ---: | --- | ---: |
| 2 | 11 | 2025-01-01 | 100 |
| 3 | 12 | 2025-03-31 | 200 |

Both boundary dates qualify. December 31 and April 1 fall outside the quarter.

## Learner solution — SQLite

```sql
select OrderID, CustomerID, OrderDate,Total_Order_Amount
from Orders
where OrderDate>= '2025-01-01' and OrderDate < '2025-04-01'
order by OrderDate asc , OrderID asc
```

The query passed the sample and additional checks for March 31 timestamps, April 1 at midnight, and equal timestamps ordered by order ID. The SQLite comparisons use ISO-formatted date and timestamp text.

## Step-by-step walkthrough

**How to start.** Which dates begin this quarter and the next?

Use the same sample throughout and check the output after each step.

### 1. Keep orders from the start of the quarter

**What to do.** Keep orders from the start of the quarter.

**Why.** The first day belongs to the quarter.

The lower bound includes January 1 and removes order 1. Order 4 remains until the upper bound is applied. The preview uses the final ordering so the rows are easy to compare.

```sql
select OrderID, CustomerID, OrderDate,Total_Order_Amount
from Orders
where OrderDate>= '2025-01-01'
order by OrderDate asc , OrderID asc
```

| OrderID | CustomerID | OrderDate | Total_Order_Amount |
| ---: | ---: | --- | ---: |
| 2 | 11 | 2025-01-01 | 100 |
| 3 | 12 | 2025-03-31 | 200 |
| 4 | 13 | 2025-04-01 | 300 |

### 2. Exclude the start of the next quarter

**What to do.** Exclude the start of the next quarter.

**Why.** The next quarter is excluded while all March 31 timestamps remain eligible.

The exclusive April 1 boundary removes order 4 and keeps all of March 31, including timestamps such as `2025-03-31 15:00:00`. For orders with identical dates or timestamps, the lower order ID comes first.

```sql
select OrderID, CustomerID, OrderDate,Total_Order_Amount
from Orders
where OrderDate>= '2025-01-01' and OrderDate < '2025-04-01'
order by OrderDate asc , OrderID asc
```

| OrderID | CustomerID | OrderDate | Total_Order_Amount |
| ---: | ---: | --- | ---: |
| 2 | 11 | 2025-01-01 | 100 |
| 3 | 12 | 2025-03-31 | 200 |

## Learner solution — SQL Server

```sql
select OrderID, CustomerID, OrderDate,Total_Order_Amount
from Orders
where OrderDate>= '2025-01-01' and OrderDate < '2025-04-01'
order by OrderDate asc , OrderID asc;
```

The same range works with a SQL Server date or timestamp-valued column such as `datetime2`. Reviewed by inspection.

## Official solution

The [PNP source notes](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/1.%20Intro%20to%20SQL%20and%20Advanced%20Select/P005.%20Orders%20placed%20in%20Q1%202025.md) reproduce this PostgreSQL answer key query.

```sql
SELECT o.OrderID,
       o.CustomerID,
       o.OrderDate,
       o.Total_Order_Amount
FROM Orders AS o
WHERE o.OrderDate >= DATE '2025-01-01'
  AND o.OrderDate <  DATE '2025-04-01'
ORDER BY o.OrderDate, o.OrderID;
```

The official solution uses typed date literals with the same inclusive start and exclusive end as the learner's query.
