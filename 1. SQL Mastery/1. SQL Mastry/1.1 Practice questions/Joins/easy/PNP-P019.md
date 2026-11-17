# PNP P019 — Units sold per product

**Topic:** Joins and aggregation  
**Difficulty:** Easy

## Question

For each product that appears in `OrderDetails`, show its name and three metrics. Every order line counts as sold.

| Output column | Meaning |
|---|---|
| `ProductID` | Product ID |
| `Product` | Product name |
| `units_sold` | Sum of `Quantity` |
| `order_lines` | Number of order detail rows for the product |
| `orders` | Number of distinct orders containing the product |

Sort by `units_sold` **descending**, then `ProductID` **ascending**.

### Sample input

**`Products`**

| ProductID | Product |
|---:|---|
| 1 | Pen |
| 2 | Bag |
| 3 | Cup |

**`OrderDetails`**

| OrderDetailID | OrderID | ProductID | Quantity |
|---:|---:|---:|---:|
| 1 | 10 | 1 | 2 |
| 2 | 11 | 1 | 3 |
| 3 | 11 | 2 | 1 |

### Expected output

| ProductID | Product | units_sold | order_lines | orders |
|---:|---|---:|---:|---:|
| 1 | Pen | 5 | 2 | 2 |
| 2 | Bag | 1 | 1 | 1 |

Pen sold **5 units across 2 order lines and 2 distinct orders**. Cup has no order lines, so it doesn’t appear.

## Learner solution — SQLite

```sql
select O.ProductID,P.Product,sum (O.Quantity) as units_sold, count(OrderDetailID)  as order_lines, count(distinct(OrderID)) as orders
from OrderDetails as O
left join Products as P on O.ProductID =P.ProductID
group by O.ProductID
order by sum (O.Quantity) desc , O.ProductID asc
```

## Step-by-step walkthrough

One output row represents one product appearing in OrderDetails. The sample stays the same throughout.

### 1. Attach the product name to each order line

**What to do.** Start with OrderDetails and look up the name in Products by ProductID.

**Why this join.** The learner uses LEFT JOIN to preserve every order line even if the catalogue lookup is missing. Cup does not appear because it has no order line. A missing catalogue match gives a NULL name. The official INNER JOIN requires a match in the catalogue.

```sql
SELECT O.OrderDetailID, O.OrderID, O.ProductID, P.Product, O.Quantity
FROM OrderDetails AS O
LEFT JOIN Products AS P ON O.ProductID = P.ProductID
ORDER BY O.OrderDetailID;
```

| OrderDetailID | OrderID | ProductID | Product | Quantity |
|---:|---:|---:|---|---:|
| 1 | 10 | 1 | Pen | 2 |
| 2 | 11 | 1 | Pen | 3 |
| 3 | 11 | 2 | Bag | 1 |

### 2. Group by product and calculate the metrics

**What to do.** Group by the order-line product ID, then sum quantities, count lines, and count distinct order IDs.

**Why.** The metrics answer different questions. Pen's quantities add up to five. Its two lines happen to belong to different orders. If it appears again in order 10, the line count increases and the distinct order count stays at two.

```sql
select O.ProductID,P.Product,sum (O.Quantity) as units_sold, count(OrderDetailID)  as order_lines, count(distinct(OrderID)) as orders
from OrderDetails as O
left join Products as P on O.ProductID =P.ProductID
group by O.ProductID
ORDER BY O.ProductID;
```

| ProductID | Product | units_sold | order_lines | orders |
|---:|---|---:|---:|---:|
| 1 | Pen | 5 | 2 | 2 |
| 2 | Bag | 1 | 1 | 1 |

### 3. Apply the ranking and verify ties

**What to do.** Sort by total quantity descending and by OrderDetails.ProductID ascending for tied totals.

**Why.** Both tables have ProductID, so qualifying the tie-breaker makes it unambiguous. Run the learner query above.

```sql
select O.ProductID,P.Product,sum (O.Quantity) as units_sold, count(OrderDetailID)  as order_lines, count(distinct(OrderID)) as orders
from OrderDetails as O
left join Products as P on O.ProductID =P.ProductID
group by O.ProductID
order by sum (O.Quantity) desc , O.ProductID asc
```

| ProductID | Product | units_sold | order_lines | orders |
|---:|---|---:|---:|---:|
| 1 | Pen | 5 | 2 | 2 |
| 2 | Bag | 1 | 1 | 1 |

SQLite checks covered the sample, a repeated product within one order, tied sales totals, and a missing catalogue match. The repeated-order fixture returned nine units, three lines and two distinct orders for Pen.

## Learner solution — SQL Server

```sql
select O.ProductID,P.Product,sum (O.Quantity) as units_sold, count(OrderDetailID)  as order_lines, count(distinct(OrderID)) as orders
from OrderDetails as O
left join Products as P on O.ProductID =P.ProductID
group by O.ProductID, P.Product
order by sum (O.Quantity) desc , O.ProductID asc;
```

SQL Server requires the selected product name in GROUP BY. Reviewed by inspection.

## Official solution

[PNP answer key, Q19](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT p.ProductID,
       p.Product,
       SUM(od.Quantity)           AS units_sold,
       COUNT(*)                   AS order_lines,
       COUNT(DISTINCT od.OrderID) AS orders
FROM OrderDetails AS od
JOIN Products AS p ON p.ProductID = od.ProductID
GROUP BY p.ProductID, p.Product
ORDER BY units_sold DESC NULLS LAST, p.ProductID;
```

### Official answer — SQLite adaptation

```sql
SELECT p.ProductID,
       p.Product,
       SUM(od.Quantity)           AS units_sold,
       COUNT(*)                   AS order_lines,
       COUNT(DISTINCT od.OrderID) AS orders
FROM OrderDetails AS od
JOIN Products AS p ON p.ProductID = od.ProductID
GROUP BY p.ProductID, p.Product
ORDER BY units_sold DESC, p.ProductID;
```

### Official answer — SQL Server adaptation

```sql
SELECT p.ProductID,
       p.Product,
       SUM(od.Quantity)           AS units_sold,
       COUNT(*)                   AS order_lines,
       COUNT(DISTINCT od.OrderID) AS orders
FROM OrderDetails AS od
JOIN Products AS p ON p.ProductID = od.ProductID
GROUP BY p.ProductID, p.Product
ORDER BY units_sold DESC, p.ProductID;
```

Descending order places NULL totals last in both engines. The SQLite adaptation passed the sample and extended fixture. The SQL Server adaptation was reviewed by inspection.
