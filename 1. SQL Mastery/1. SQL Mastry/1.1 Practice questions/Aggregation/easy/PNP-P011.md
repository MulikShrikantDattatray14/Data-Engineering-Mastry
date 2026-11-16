# PNP P011 — How much of the catalogue has ever sold?

**Topic:** Aggregation  
**Difficulty:** Easy

## Question

Start with every product in `Products` and attach its matching `OrderDetails` rows by `ProductID`. Keep products that have never sold. Return **one summary row** with these five metrics:

| Column | What it should show |
|---|---|
| `rows_after_join` | Total rows after joining, including unsold products |
| `sale_lines` | Number of order lines that matched a product |
| `listed_products` | Number of distinct products in the catalogue |
| `products_sold` | Number of distinct products with at least one matching order line |
| `pct_sold` | Percentage of listed products that sold, rounded to two decimal places |

### Sample input

**`Products`**

| ProductID | Product |
|---:|---|
| 1 | Pen |
| 2 | Bag |
| 3 | Cup |

**`OrderDetails`**

| OrderDetailID | OrderID | ProductID |
|---:|---:|---:|
| 1 | 10 | 1 |
| 2 | 11 | 1 |
| 3 | 11 | 2 |

### Expected output

| rows_after_join | sale_lines | listed_products | products_sold | pct_sold |
|---:|---:|---:|---:|---:|
| 4 | 3 | 3 | 2 | 66.67 |

Pen contributes two joined rows, Bag contributes one, and the unsold Cup still contributes one. Two of the three listed products have sold.

## Learner solution — SQLite

```sql
SELECT COUNT(*) AS rows_after_join,
       COUNT(O.ProductID) AS sale_lines,
       COUNT(DISTINCT P.ProductID) AS listed_products,
       COUNT(DISTINCT (O.ProductID)) AS products_sold,
       ROUND(COUNT(DISTINCT O.ProductID) * 100.0 / COUNT(DISTINCT P.ProductID), 2) AS pct_sold
FROM Products AS P
LEFT JOIN OrderDetails AS O ON P.ProductID = O.ProductID;
```

Verified the sample, an order line for an unlisted product, a catalogue with no sales, and an empty catalogue. The submitted SQL was reformatted to remove chat markup.

## Step-by-step walkthrough

**How to start.** Which population defines the denominator?

Use the same sample throughout and check the output after each step.

### 1. Join from the catalogue

**What to do.** Join from the catalogue.

**Why.** Unsold items still belong to the catalogue.

**Golden rule.** Ask “Out of what?” to find the denominator. For “What percentage of listed products have sold?”, the denominator is all distinct listed products, and the numerator is the distinct listed products with a sale.

Choose the join by asking which unmatched rows must stay. Use `LEFT JOIN` with the required population on the left when its unmatched rows must stay. Use `INNER JOIN` when only matches belong in the result, and `FULL OUTER JOIN` when unmatched rows on both sides belong. Here, all three catalogue products must stay, so start from `Products` and left join `OrderDetails`. Count distinct product IDs because one product can match several order lines.

**Why `LEFT JOIN`?** The denominator is the entire catalogue, so every row from `Products` must survive even when no order line matches. An `INNER JOIN` would drop Cup, shrinking the denominator from three products to two and raising the sample percentage to 100%. A `FULL OUTER JOIN` could also retain order lines for products absent from the catalogue. `LEFT JOIN` keeps every catalogue product and attaches only its matching order lines.

Pen matches two lines, Bag matches one, and Cup retains a row with NULLs on the order-line side.

```sql
SELECT P.ProductID, P.Product, O.OrderDetailID, O.ProductID AS matched_product_id
FROM Products AS P
LEFT JOIN OrderDetails AS O ON P.ProductID = O.ProductID
ORDER BY P.ProductID, O.OrderDetailID;
```

| ProductID | Product | OrderDetailID | matched_product_id |
| ---: | --- | ---: | ---: |
| 1 | Pen | 1 | 1 |
| 1 | Pen | 2 | 1 |
| 2 | Bag | 3 | 2 |
| 3 | Cup | `NULL` | `NULL` |

### 2. Count rows, sale lines, and distinct products

**What to do.** Count rows, sale lines, and distinct products.

**Why.** Joined rows and distinct products answer different questions.

COUNT(*) counts all four joined rows. COUNT(O.ProductID) counts the three matched lines. The distinct catalogue IDs are 1, 2, and 3. The distinct matched IDs are 1 and 2.

```sql
SELECT COUNT(*) AS rows_after_join,
       COUNT(O.ProductID) AS sale_lines,
       COUNT(DISTINCT P.ProductID) AS listed_products,
       COUNT(DISTINCT (O.ProductID)) AS products_sold
FROM Products AS P
LEFT JOIN OrderDetails AS O ON P.ProductID = O.ProductID;
```

| rows_after_join | sale_lines | listed_products | products_sold |
| ---: | ---: | ---: | ---: |
| 4 | 3 | 3 | 2 |

### 3. Calculate the percentage

**What to do.** Calculate the percentage.

**Why.** The fraction measures sold products out of all listed products.

Divide the distinct sold count by the distinct listed count. Multiplying by 100.0 before dividing preserves the fractional part. The complete SQLite query above computes 2 × 100.0 ÷ 3 and rounds it to 66.67.

| rows_after_join | sale_lines | listed_products | products_sold | pct_sold |
| ---: | ---: | ---: | ---: | ---: |
| 4 | 3 | 3 | 2 | 66.67 |

## Learner solution — SQL Server

```sql
SELECT COUNT(*) AS rows_after_join,
       COUNT(O.ProductID) AS sale_lines,
       COUNT(DISTINCT P.ProductID) AS listed_products,
       COUNT(DISTINCT (O.ProductID)) AS products_sold,
       ROUND(COUNT(DISTINCT O.ProductID) * 100.0 / NULLIF(COUNT(DISTINCT P.ProductID), 0), 2) AS pct_sold
FROM Products AS P
LEFT JOIN OrderDetails AS O ON P.ProductID = O.ProductID;
```

The adaptation uses NULLIF to return NULL for an empty catalogue and avoid division by zero. It was reviewed by inspection.

## Official solution

[PNP answer key, Q11](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT COUNT(*)                                       AS rows_after_join,
       COUNT(od.OrderDetailID)                        AS sale_lines,
       COUNT(DISTINCT p.ProductID)                    AS listed_products,
       COUNT(DISTINCT od.ProductID)                   AS products_sold,
       ROUND(100.0 * COUNT(DISTINCT od.ProductID)
             / NULLIF(COUNT(DISTINCT p.ProductID), 0), 2) AS pct_sold
FROM Products AS p
LEFT JOIN OrderDetails AS od ON od.ProductID = p.ProductID;
```

The answer key counts the order line ID for sale_lines. Counting the matched product ID gives the same result when order line IDs are non-NULL. Both approaches count distinct order-side product IDs for products_sold.

### Official answer — SQLite adaptation

```sql
SELECT COUNT(*)                                       AS rows_after_join,
       COUNT(od.OrderDetailID)                        AS sale_lines,
       COUNT(DISTINCT p.ProductID)                    AS listed_products,
       COUNT(DISTINCT od.ProductID)                   AS products_sold,
       ROUND(100.0 * COUNT(DISTINCT od.ProductID)
             / NULLIF(COUNT(DISTINCT p.ProductID), 0), 2) AS pct_sold
FROM Products AS p
LEFT JOIN OrderDetails AS od ON od.ProductID = p.ProductID;
```

### Official answer — SQL Server adaptation

```sql
SELECT COUNT(*)                                       AS rows_after_join,
       COUNT(od.OrderDetailID)                        AS sale_lines,
       COUNT(DISTINCT p.ProductID)                    AS listed_products,
       COUNT(DISTINCT od.ProductID)                   AS products_sold,
       ROUND(100.0 * COUNT(DISTINCT od.ProductID)
             / NULLIF(COUNT(DISTINCT p.ProductID), 0), 2) AS pct_sold
FROM Products AS p
LEFT JOIN OrderDetails AS od ON od.ProductID = p.ProductID;
```

SQLite adaptation executed on representative fixtures. SQL Server adaptation reviewed by inspection.
