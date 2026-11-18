# PNP P026 — List-price value by category

**Topic** Joins and aggregation · **Difficulty** ![MEDIUM](../../../_badges/medium.svg)

## Question

**Business scenario.** The category management team splits next quarter's promotion budget across categories. For each category they want three numbers: how many orders included it, how many units moved, and what those units are worth at list price. Finance will tie the units column back to the order lines, so no line may go missing, even when its product or category reference is broken.

**Task.** For every category, return the number of distinct orders that contained at least one of its products, the units sold, and the list-price value ( Quantity * Sale_Price ). Lines whose product points to a CategoryID with no Category row go under Unmapped . Lines whose ProductID is not in Products go under Unknown product . Sort by list-price value, highest first.

**Expected output (as supplied):**

```text
category_name : CategoryName , Unmapped or Unknown product
orders : distinct orders containing at least one line in the category
units_sold : sum of Quantity
list_price_value : sum of Quantity * Sale_Price
```

### Practice requirements

Return one row per catalogue category, including categories with no sales. Keep order lines with missing product or category references in the appropriate labeled groups. Show zero orders, units and value for an unsold category. Keep the value `NULL` when sales have no known price. Break ties by `category_name` in ascending order and put unknown values last.

### Sample input and expected output

Use this same example throughout the walkthrough. The source book specifies the four output columns. The sample rows illustrate the practice question.

**Input — `Category`**

| CategoryID | CategoryName |
|---:|---|
| 1 | Drinks |
| 2 | Snacks |
| 3 | Stationery |

**Input — `Products`**

| ProductID | CategoryID | Sale_Price |
|---:|---:|---:|
| 10 | 1 | 10 |
| 11 | 1 | 8 |
| 20 | 2 | 5 |
| 30 | 99 | 7 |

**Input — `OrderDetails`**

| OrderDetailID | OrderID | ProductID | Quantity |
|---:|---:|---:|---:|
| 1 | 100 | 10 | 2 |
| 2 | 100 | 11 | 1 |
| 3 | 100 | 20 | 1 |
| 4 | 101 | 30 | 3 |
| 5 | 102 | 999 | 4 |

Here, Stationery has no sales, product `30` points to a missing Category, product `999` is absent from Products, and order `100` has two Drinks lines. These rows form one example used throughout the solution.

**Expected output**

| category_name | orders | units_sold | list_price_value |
|---|---:|---:|---:|
| Drinks | 1 | 3 | 28 |
| Unmapped | 1 | 3 | 21 |
| Snacks | 1 | 1 | 5 |
| Stationery | 0 | 0 | 0 |
| Unknown product | 1 | 4 | NULL |

Order `100` contains two Drinks lines and one Snacks line. It counts once for each of those categories. The two Drinks lines contribute `2 × 10 + 1 × 8 = 28`. Order `101` contributes `3 × 7 = 21` to `Unmapped`. Order `102` contributes four units to `Unknown product` and has no known price. Stationery has no sale lines.

## Visual walkthrough

Follow all five original order lines through the two joins. The full category join adds an unsold category, and grouping turns the six joined rows into five report rows. No row or group filter applies. The zero-value check belongs to the value calculation.

![Seven steps from all three sample input tables to the sorted report. The Drinks lines combine to 28. Stationery has zero sales, and the missing product has four units with unknown value.](../../assets/p026-from-inputs-to-result.svg)

[Open the full-size graphic](../../assets/p026-from-inputs-to-result.svg?raw=1)

## Final learner solution — SQLite

Built from Shri’s submitted clauses with guidance on the category labels, the empty-category value, and the sort syntax.

```sql
SELECT
    CASE
        WHEN c.CategoryID IS NULL AND p.ProductID IS NULL
            THEN 'Unknown product'
        WHEN c.CategoryID IS NULL AND p.ProductID IS NOT NULL
            THEN 'Unmapped'
        WHEN c.CategoryID IS NOT NULL
            THEN c.CategoryName
    END AS category_name,
    COUNT(DISTINCT od.OrderID) AS orders,
    COALESCE(SUM(od.Quantity), 0) AS units_sold,
    CASE
        WHEN COUNT(od.OrderDetailID) = 0 THEN 0
        ELSE SUM(p.Sale_Price * od.Quantity)
    END AS list_price_value
FROM OrderDetails AS od
LEFT JOIN Products AS p
    ON od.ProductID = p.ProductID
FULL OUTER JOIN Category AS c
    ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, category_name
ORDER BY list_price_value DESC NULLS LAST, category_name ASC;
```

## Step-by-step walkthrough

One result row represents a category. Before aggregating, keep enough detail to tell whether an order line, product and category actually matched.

### 1. Start with each sale line and look for its product

Finance wants every sold unit counted. Start with `OrderDetails`, where one row is one order line. A `LEFT JOIN` to `Products` keeps line 5 even though its product ID `999` has no match. The two product ID columns below distinguish the ID recorded on the order from the product actually found.

```sql
SELECT od.OrderDetailID, od.ProductID AS ordered_product_id,
       p.ProductID AS matched_product_id, p.Sale_Price
FROM OrderDetails AS od
LEFT JOIN Products AS p
    ON od.ProductID = p.ProductID
ORDER BY od.OrderDetailID;
```

| OrderDetailID | 🟦 ordered_product_id | 🟦 matched_product_id | Sale_Price |
| --- | --- | --- | --- |
| 1 | 10 | 10 | 10 |
| 2 | 11 | 11 | 8 |
| 3 | 20 | 20 | 5 |
| 4 | 30 | 30 | 7 |
| 🟨 5 | **999** | **`NULL`** | `NULL` |

### 2. Keep categories with no sales

Sales alone cannot supply a row for Stationery. The `FULL OUTER JOIN` keeps the sale lines from step 1 and adds any category with no matching sale. Follow the last three rows. They show a product with a broken category reference, a sale with no product match, and a category with no sales.

```sql
SELECT od.OrderDetailID, p.ProductID AS matched_product_id,
       c.CategoryID, c.CategoryName
FROM OrderDetails AS od
LEFT JOIN Products AS p
    ON od.ProductID = p.ProductID
FULL OUTER JOIN Category AS c
    ON c.CategoryID = p.CategoryID
ORDER BY od.OrderDetailID NULLS LAST;
```

| 🟦 OrderDetailID | matched_product_id | 🟦 CategoryID | CategoryName |
| --- | --- | --- | --- |
| 1 | 10 | 1 | Drinks |
| 2 | 11 | 1 | Drinks |
| 3 | 20 | 2 | Snacks |
| 🟨 **4** | **30** | **`NULL`** | **`NULL`** |
| 🟨 **5** | **`NULL`** | **`NULL`** | **`NULL`** |
| 🟨 **`NULL`** | **`NULL`** | **3** | **Stationery** |

### 3. Give each joined row its reporting label

Use the catalogue name whenever the category exists. For a missing category, check the product lookup. A matched product earns `Unmapped`, and a missing product earns `Unknown product`. Stationery still has a category ID and retains its own name.

```sql
SELECT od.OrderDetailID, c.CategoryID,
    CASE
        WHEN c.CategoryID IS NULL AND p.ProductID IS NULL
            THEN 'Unknown product'
        WHEN c.CategoryID IS NULL AND p.ProductID IS NOT NULL
            THEN 'Unmapped'
        WHEN c.CategoryID IS NOT NULL
            THEN c.CategoryName
    END AS category_name
FROM OrderDetails AS od
LEFT JOIN Products AS p
    ON od.ProductID = p.ProductID
FULL OUTER JOIN Category AS c
    ON c.CategoryID = p.CategoryID
ORDER BY od.OrderDetailID NULLS LAST;
```

| OrderDetailID | 🟦 CategoryID | 🟪 category_name |
| --- | --- | --- |
| 1 | 1 | Drinks |
| 2 | 1 | Drinks |
| 3 | 2 | Snacks |
| 🟨 4 | **`NULL`** | **Unmapped** |
| 🟨 5 | **`NULL`** | **Unknown product** |
| 🟨 `NULL` | **3** | **Stationery** |

The two broken references both have a `NULL` category ID. Grouping by the category ID **and the calculated label** separates them. Keeping the ID also separates two real catalogue categories that happen to share a name.

### 4. Count orders and add units within each category

Trace the two gold Drinks lines. They share order ID `100`, so Drinks gets one order. Both quantities contribute to units sold, giving `2 + 1 = 3`. Stationery has no matched quantity. `COALESCE` gives it zero units.

![In the two highlighted Drinks rows the OrderID is 100.](../../assets/p026-orders-focus.svg)

```sql
SELECT
    CASE
        WHEN c.CategoryID IS NULL AND p.ProductID IS NULL
            THEN 'Unknown product'
        WHEN c.CategoryID IS NULL AND p.ProductID IS NOT NULL
            THEN 'Unmapped'
        WHEN c.CategoryID IS NOT NULL
            THEN c.CategoryName
    END AS category_name,
    COUNT(DISTINCT od.OrderID) AS orders,
    COALESCE(SUM(od.Quantity), 0) AS units_sold
FROM OrderDetails AS od
LEFT JOIN Products AS p
    ON od.ProductID = p.ProductID
FULL OUTER JOIN Category AS c
    ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, category_name
ORDER BY category_name ASC;
```

| category_name | 🟪 orders | 🟪 units_sold |
| --- | --- | --- |
| 🟨 Drinks | **1** | **3** |
| Snacks | 1 | 1 |
| 🟨 Stationery | **0** | **0** |
| Unknown product | 1 | 4 |
| Unmapped | 1 | 3 |

### 5. Value each line and distinguish an empty category from an unknown price

Multiply quantity by the price on that line before summing. To decide whether zero is justified, count `od.OrderDetailID`. The outer join gives Stationery a placeholder with a `NULL` line ID, so its count is zero. For `Unknown product`, order line 5 exists. Multiplication by its missing price gives `NULL`, and its group has no priced line to add.

```sql
SELECT
    CASE
        WHEN c.CategoryID IS NULL AND p.ProductID IS NULL
            THEN 'Unknown product'
        WHEN c.CategoryID IS NULL AND p.ProductID IS NOT NULL
            THEN 'Unmapped'
        WHEN c.CategoryID IS NOT NULL
            THEN c.CategoryName
    END AS category_name,
    COUNT(od.OrderDetailID) AS matching_lines,
    CASE
        WHEN COUNT(od.OrderDetailID) = 0 THEN 0
        ELSE SUM(p.Sale_Price * od.Quantity)
    END AS list_price_value
FROM OrderDetails AS od
LEFT JOIN Products AS p
    ON od.ProductID = p.ProductID
FULL OUTER JOIN Category AS c
    ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, category_name
ORDER BY category_name ASC;
```

| category_name | 🟦 matching_lines | 🟪 list_price_value |
| --- | --- | --- |
| Drinks | 2 | 28 |
| Snacks | 1 | 5 |
| 🟨 Stationery | **0** | **0** |
| 🟨 Unknown product | **1** | **`NULL`** |
| Unmapped | 1 | 21 |

The zero check changes only `list_price_value`. The row for the unknown product still contributes one order and four units.

### 6. Sort the report and reconcile the totals

Apply the following clause to the complete learner query. Highest known value comes first. Equal values sort by category name, and unknown values come last.

```sql
ORDER BY list_price_value DESC NULLS LAST, category_name ASC;
```

| category_name | orders | units_sold | 🟪 list_price_value |
| --- | --- | --- | --- |
| 🟨 Drinks | 1 | 3 | **28** |
| Unmapped | 1 | 3 | 21 |
| Snacks | 1 | 1 | 5 |
| Stationery | 0 | 0 | 0 |
| 🟨 Unknown product | 1 | 4 | **`NULL`** |

All **11 units** are accounted for. The five order lines contain `2 + 1 + 1 + 3 + 4 = 11` units. The output contains `3 + 3 + 1 + 0 + 4 = 11`.

## Learner solution — SQL Server adaptation

The CTE makes `category_name` available as an input column for `GROUP BY`. In SQL Server a descending numeric sort places `NULL` last.

```sql
WITH labeled_rows AS (
    SELECT
        c.CategoryID AS category_id,
        CASE
            WHEN c.CategoryID IS NULL AND p.ProductID IS NULL
                THEN 'Unknown product'
            WHEN c.CategoryID IS NULL AND p.ProductID IS NOT NULL
                THEN 'Unmapped'
            WHEN c.CategoryID IS NOT NULL
                THEN c.CategoryName
        END AS category_name,
        od.OrderDetailID,
        od.OrderID,
        od.Quantity,
        p.Sale_Price
    FROM OrderDetails AS od
    LEFT JOIN Products AS p
        ON od.ProductID = p.ProductID
    FULL OUTER JOIN Category AS c
        ON c.CategoryID = p.CategoryID
)
SELECT
    category_name,
    COUNT(DISTINCT OrderID) AS orders,
    COALESCE(SUM(Quantity), 0) AS units_sold,
    CASE
        WHEN COUNT(OrderDetailID) = 0 THEN 0
        ELSE SUM(Sale_Price * Quantity)
    END AS list_price_value
FROM labeled_rows
GROUP BY category_id, category_name
ORDER BY list_price_value DESC, category_name ASC;
```

## Official solution

The published answer starts with order lines and uses two left joins. On this sample it returns Drinks, Unmapped, Snacks and Unknown product. The practice requirement to include every catalogue category also calls for Stationery’s zero row. The learner solution covers that case. [Source question and answer](<../../../2.PNP-%20foundations%20and%20practice/2.%20Joins/P026.%20List-price%20value%20by%20category.md>) · [PrepNPlaced, question 26, pp. 44–45](<../../../2.PNP-%20foundations%20and%20practice/Source%20Materials/Updated_100_SQL_Interview_Questions.pdf>)

### As supplied — PostgreSQL

```sql
SELECT CASE
    WHEN p.ProductID IS NULL THEN 'Unknown product'
    WHEN cat.CategoryID IS NULL THEN 'Unmapped'
    ELSE cat.CategoryName
END AS category_name,
COUNT(DISTINCT od.OrderID) AS orders,
SUM(od.Quantity) AS units_sold,
SUM(od.Quantity * p.Sale_Price) AS list_price_value
FROM OrderDetails AS od
LEFT JOIN Products AS p ON p.ProductID = od.ProductID
LEFT JOIN Category AS cat ON cat.CategoryID = p.CategoryID
GROUP BY category_name
ORDER BY list_price_value DESC NULLS LAST, category_name;
```

### Official answer — SQLite adaptation

The source query also runs as written in SQLite. Its order-line starting point produces four rows on this sample.

```sql
SELECT CASE
    WHEN p.ProductID IS NULL THEN 'Unknown product'
    WHEN cat.CategoryID IS NULL THEN 'Unmapped'
    ELSE cat.CategoryName
END AS category_name,
COUNT(DISTINCT od.OrderID) AS orders,
SUM(od.Quantity) AS units_sold,
SUM(od.Quantity * p.Sale_Price) AS list_price_value
FROM OrderDetails AS od
LEFT JOIN Products AS p ON p.ProductID = od.ProductID
LEFT JOIN Category AS cat ON cat.CategoryID = p.CategoryID
GROUP BY category_name
ORDER BY list_price_value DESC NULLS LAST, category_name;
```

### Official answer — SQL Server adaptation

Compute the source label in a CTE, group on it, and sort the value descending. This retains the published answer’s set of rows.

```sql
WITH labeled_lines AS (
    SELECT
        CASE
            WHEN p.ProductID IS NULL THEN 'Unknown product'
            WHEN c.CategoryID IS NULL THEN 'Unmapped'
            ELSE c.CategoryName
        END AS category_name,
        od.OrderID,
        od.Quantity,
        p.Sale_Price
    FROM OrderDetails AS od
    LEFT JOIN Products AS p ON p.ProductID = od.ProductID
    LEFT JOIN Category AS c ON c.CategoryID = p.CategoryID
)
SELECT
    category_name,
    COUNT(DISTINCT OrderID) AS orders,
    SUM(Quantity) AS units_sold,
    SUM(Quantity * Sale_Price) AS list_price_value
FROM labeled_lines
GROUP BY category_name
ORDER BY list_price_value DESC, category_name ASC;
```

## Verification

Ran the learner and official SQLite queries on SQLite 3.53.1. All five expected rows, output names and ordering matched for the learner query. The published query returned four rows. Additional learner checks covered an empty `OrderDetails` table, two catalogue categories with the same name, a real category named `Unmapped`, tied values, and a category whose sold products all had missing prices. The SQL Server adaptations were checked against the same sample using their SQLite-compatible statements. A native SQL Server run is pending.

[Practice index](../../README.md)
