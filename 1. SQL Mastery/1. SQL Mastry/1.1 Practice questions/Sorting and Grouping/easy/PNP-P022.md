# PNP P022 — Orders with more than eight line items

**Topic:** Sorting and Grouping  
**Difficulty:** Easy

## Question

The fulfilment team sends orders with **more than eight line items** to a separate packing station. From `OrderDetails`, return one row per qualifying order with:

| Output column | Meaning |
|---|---|
| `OrderID` | Order identifier |
| `line_items` | Number of rows for that order |
| `distinct_products` | Number of different product IDs in the order |
| `total_units` | Sum of quantities across all its lines |

Sort by `line_items` **descending**, then `OrderID` **ascending**.

### Sample input · `OrderDetails`

| OrderDetailID | OrderID | ProductID | Quantity |
|---:|---:|---:|---:|
| 1 | 10 | 1 | 1 |
| 2 | 10 | 2 | 1 |
| 3 | 10 | 3 | 1 |
| 4 | 10 | 4 | 1 |
| 5 | 10 | 5 | 1 |
| 6 | 10 | 6 | 1 |
| 7 | 10 | 7 | 1 |
| 8 | 10 | 8 | 1 |
| 9 | 10 | 1 | 1 |
| 10 | 11 | 2 | 1 |

### Expected output

| OrderID | line_items | distinct_products | total_units |
|---:|---:|---:|---:|
| 10 | 9 | 8 | 9 |

Order 10 qualifies because it has **9 lines**, even though product 1 appears twice and it has only **8 distinct products**. Order 11 has one line, so it’s excluded.

## Learner solution — SQLite

```sql
select OrderID,count(OrderID)  as line_items, count(distinct(ProductID)) as distinct_products,
sum(Quantity) as total_units
from OrderDetails
group by OrderID
having count(OrderID) > 8
order by count(OrderID) desc ,OrderID asc
```

## Step-by-step walkthrough

### 1. Define and check one row per order

**What to do.** Group the detail rows by OrderID and calculate each metric for the whole group.

**Why.** Several detail rows can belong to one order. Count the lines, count each distinct product once, and add the quantities. All three metrics come from OrderDetails.

```sql
select OrderID,count(OrderID)  as line_items, count(distinct(ProductID)) as distinct_products,
sum(Quantity) as total_units
from OrderDetails
group by OrderID
order by OrderID;
```

| OrderID | line_items | distinct_products | total_units |
|---:|---:|---:|---:|
| 10 | 9 | 8 | 9 |
| 11 | 1 | 1 | 1 |

Order 10 has nine rows. Product 1 repeats, so there are eight different product IDs. Each quantity is 1, so the total is nine units.

### 2. Apply the cutoff and sort

**What to do.** Keep groups with a line count greater than eight and sort by line count descending, then order ID ascending.

**Why.** HAVING checks the group count after aggregation. The order ID gives a consistent result for tied counts.

```sql
select OrderID,count(OrderID)  as line_items, count(distinct(ProductID)) as distinct_products,
sum(Quantity) as total_units
from OrderDetails
group by OrderID
having count(OrderID) > 8
order by count(OrderID) desc ,OrderID asc
```

| OrderID | line_items | distinct_products | total_units |
|---:|---:|---:|---:|
| 10 | 9 | 8 | 9 |

Verified in SQLite on the sample and an extended case. An order with exactly eight lines and 20 units was excluded. Two nine-line orders were sorted by ID even though their unit totals differed.

## Learner solution — SQL Server

```sql
select OrderID,count(OrderID)  as line_items, count(distinct(ProductID)) as distinct_products,
sum(Quantity) as total_units
from OrderDetails
group by OrderID
having count(OrderID) > 8
order by count(OrderID) desc ,OrderID asc;
```

Reviewed by inspection.

## Official solution

[PNP answer key, Q22](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT od.OrderID,
       COUNT(*)                     AS line_items,
       COUNT(DISTINCT od.ProductID) AS distinct_products,
       SUM(od.Quantity)             AS total_units
FROM OrderDetails AS od
GROUP BY od.OrderID
HAVING COUNT(*) > 8
ORDER BY line_items DESC, od.OrderID;
```

### Official answer — SQLite adaptation

```sql
SELECT od.OrderID,
       COUNT(*)                     AS line_items,
       COUNT(DISTINCT od.ProductID) AS distinct_products,
       SUM(od.Quantity)             AS total_units
FROM OrderDetails AS od
GROUP BY od.OrderID
HAVING COUNT(*) > 8
ORDER BY line_items DESC, od.OrderID;
```

### Official answer — SQL Server adaptation

```sql
SELECT od.OrderID,
       COUNT(*)                     AS line_items,
       COUNT(DISTINCT od.ProductID) AS distinct_products,
       SUM(od.Quantity)             AS total_units
FROM OrderDetails AS od
GROUP BY od.OrderID
HAVING COUNT(*) > 8
ORDER BY line_items DESC, od.OrderID;
```

The official answer counts rows with COUNT(*). The learner uses COUNT(OrderID), which gives the same result when OrderID is non-NULL. The SQL Server versions were reviewed by inspection.
