# PNP P012 — Price and discount statistics per category

**Topic:** Aggregation  
**Difficulty:** Easy  
**Status:** Guided walkthrough verified in SQLite. Final learner submission pending.

## Question

Return **one row per `CategoryID`** from `Products`, sorted by `CategoryID` ascending.

| Output column | What it should show |
|---|---|
| `CategoryID` | Category ID |
| `products` | Number of products in the category |
| `min_price` | Lowest sale price |
| `max_price` | Highest sale price |
| `avg_price` | Average sale price, rounded to two decimals |
| `full_price_products` | Number of products whose sale price equals their market price |
| `avg_discount_pct` | Average of the individual product discount percentages, rounded to two decimals. Exclude products with a `NULL` or zero market price from this average. |

### Sample input — `Products`

| ProductID | CategoryID | Sale_Price | Market_Price |
|---:|---:|---:|---:|
| 1 | 10 | 80 | 100 |
| 2 | 10 | 100 | 100 |

### Expected output

| CategoryID | products | min_price | max_price | avg_price | full_price_products | avg_discount_pct |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 2 | 80 | 100 | 90.00 | 1 | 10.00 |

The two products are discounted by **20%** and **0%**, so their average discount is **10.00%**.

## Guided walkthrough

Start by asking what one output row represents and which products should contribute to each metric. Use one extended example throughout. It includes the original sample, a zero market price, and a second category with a missing market price.

| ProductID | CategoryID | Sale_Price | Market_Price |
|---:|---:|---:|---:|
| 1 | 10 | 80 | 100 |
| 2 | 10 | 100 | 100 |
| 3 | 10 | 30 | 0 |
| 4 | 20 | 150 | 200 |
| 5 | 20 | 120 | `NULL` |

### 1. Get one row per category

**What to do.** Group by CategoryID and count products.

**Why.** Each input row is a product and each output row is a category. All the fields come from Products, so this query reads a single table.

```sql
SELECT CategoryID, COUNT(*) AS products
FROM Products
GROUP BY CategoryID
ORDER BY CategoryID;
```

| CategoryID | products |
|---:|---:|
| 10 | 3 |
| 20 | 2 |

The grouping gives each category its own product count. ORDER BY sorts the two finished rows.

### 2. Add the sale-price statistics

**What to do.** Add MIN, MAX, and the rounded AVG of Sale_Price within each category.

**Why.** These metrics use the sale price. Products 3 and 5 have usable sale prices and still contribute even though their market prices are zero or missing.

```sql
SELECT CategoryID, COUNT(*) AS products,
       MIN(Sale_Price) AS min_price,
       MAX(Sale_Price) AS max_price,
       ROUND(AVG(Sale_Price), 2) AS avg_price
FROM Products
GROUP BY CategoryID
ORDER BY CategoryID;
```

| CategoryID | products | min_price | max_price | avg_price |
|---:|---:|---:|---:|---:|
| 10 | 3 | 30 | 100 | 70.00 |
| 20 | 2 | 120 | 150 | 135.00 |

Category 10 averages 80, 100, and 30. Its minimum remains 30.

### 3. Preview the contribution of each product

**What to do.** Give each full-price product a flag of 1 and each other product a flag of 0. Calculate a discount percentage only for usable market prices.

**Why.** CASE checks each product before the aggregate runs. AVG skips NULL and includes a measured 0%. Multiplying by 100.0 before dividing preserves fractions in SQLite.

```sql
SELECT ProductID, CategoryID,
       CASE WHEN Sale_Price = Market_Price THEN 1 ELSE 0 END AS full_price_flag,
       CASE
           WHEN Market_Price IS NOT NULL AND Market_Price != 0
           THEN (Market_Price - Sale_Price) * 100.0 / Market_Price
       END AS product_discount_pct
FROM Products
ORDER BY ProductID;
```

| ProductID | CategoryID | full_price_flag | product_discount_pct |
|---:|---:|---:|---:|
| 1 | 10 | 0 | 20.00 |
| 2 | 10 | 1 | 0.00 |
| 3 | 10 | 0 | `NULL` |
| 4 | 20 | 0 | 25.00 |
| 5 | 20 | 0 | `NULL` |

Product 2 contributes a real zero to the average and a one to the full-price count. Product 3 contributes no percentage.

### 4. Combine the category metrics

**What to do.** Add SUM around the flags and AVG around the individual percentages. Round that average to two decimals.

**Why.** The flags count products when added. Each eligible product contributes one percentage to the average.

```sql
SELECT CategoryID, COUNT(*) AS products,
       MIN(Sale_Price) AS min_price,
       MAX(Sale_Price) AS max_price,
       ROUND(AVG(Sale_Price), 2) AS avg_price,
       SUM(CASE WHEN Sale_Price = Market_Price THEN 1 ELSE 0 END) AS full_price_products,
       ROUND(AVG(CASE
           WHEN Market_Price IS NOT NULL AND Market_Price != 0
           THEN (Market_Price - Sale_Price) * 100.0 / Market_Price
       END), 2) AS avg_discount_pct
FROM Products
GROUP BY CategoryID
ORDER BY CategoryID;
```

| CategoryID | products | min_price | max_price | avg_price | full_price_products | avg_discount_pct |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 3 | 30 | 100 | 70.00 | 1 | 10.00 |
| 20 | 2 | 120 | 150 | 135.00 | 0 | 25.00 |

Category 10 averages 20% and 0%. Category 20 counts both products, and only product 4 contributes 25% to its discount average. SQLite may display fewer trailing zeros than shown.

### Where to put conditions

| Requirement | Place |
|---|---|
| One summary row per category | GROUP BY CategoryID |
| Exclude products from all metrics | WHERE |
| Exclude an entire category based on a calculated metric | HAVING |
| Ignore unusable market prices in the discount average only | CASE inside AVG |

For this question, a WHERE filter on market price would remove products 3 and 5 from all metrics. In category 10 that would change the count from 3 to 2 and the minimum from 30 to 80.

All four stages were checked in SQLite on the extended example. The final guided query also matches the original sample.
