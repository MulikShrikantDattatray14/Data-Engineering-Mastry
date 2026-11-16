# PNP P015 — Product count for every category

**Topic:** Joins  
**Difficulty:** Easy

## Question

Return **every category** from `Category` with the number of products assigned to it. A category with no products must still appear with a count of `0`.

Return `CategoryID`, `CategoryName`, and `product_count`. Sort by `product_count` ascending, then by `CategoryID` ascending.

### Sample input

**`Category`**

| CategoryID | CategoryName |
|---:|---|
| 1 | Snacks |
| 2 | Toys |

**`Products`**

| ProductID | CategoryID |
|---:|---:|
| 10 | 1 |
| 11 | 1 |

### Expected output

| CategoryID | CategoryName | product_count |
|---:|---|---:|
| 2 | Toys | 0 |
| 1 | Snacks | 2 |

## Learner solution — SQLite

```sql
SELECT c.CategoryID, c.CategoryName, COUNT(p.ProductID) AS product_count
FROM Category AS c
LEFT JOIN Products AS p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID
ORDER BY COUNT(p.ProductID) ASC, c.CategoryID ASC;
```

Chat markup and formatting were cleaned up. The SQLite checks covered the sample, tied counts, categories sharing a name, and products without a matching category.

## Step-by-step walkthrough

One final row represents one category. Use the same sample throughout.

### 1. Attach matching products to every category

**What to do.** Start with Category and match Products by CategoryID.

**Why this join.** Every category must stay, including Toys. A LEFT JOIN retains Toys with a NULL product ID. An INNER JOIN would drop it. A FULL OUTER JOIN could bring in products outside the required category list.

```sql
SELECT c.CategoryID, c.CategoryName, p.ProductID
FROM Category AS c
LEFT JOIN Products AS p ON c.CategoryID = p.CategoryID
ORDER BY c.CategoryID, p.ProductID;
```

| CategoryID | CategoryName | ProductID |
|---:|---|---:|
| 1 | Snacks | 10 |
| 1 | Snacks | 11 |
| 2 | Toys | `NULL` |

Snacks contributes two matched rows. Toys gets one unmatched row.

### 2. Group the rows and count matched products

**What to do.** Group by the unique category ID and count ProductID from the Products side. Sort by category ID temporarily to check the grouped results.

**Why.** COUNT(ProductID) counts non-NULL product IDs. COUNT(*) would count Toys' unmatched join row and incorrectly report one product.

```sql
SELECT c.CategoryID, c.CategoryName, COUNT(p.ProductID) AS product_count
FROM Category AS c
LEFT JOIN Products AS p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID
ORDER BY c.CategoryID;
```

| CategoryID | CategoryName | product_count |
|---:|---|---:|
| 1 | Snacks | 2 |
| 2 | Toys | 0 |

### 3. Sort the report

**What to do.** Sort by product count ascending, then category ID ascending.

**Why.** This puts empty categories first and resolves ties consistently.

```sql
SELECT c.CategoryID, c.CategoryName, COUNT(p.ProductID) AS product_count
FROM Category AS c
LEFT JOIN Products AS p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID
ORDER BY COUNT(p.ProductID) ASC, c.CategoryID ASC;
```

| CategoryID | CategoryName | product_count |
|---:|---|---:|
| 2 | Toys | 0 |
| 1 | Snacks | 2 |

## Learner solution — SQL Server

```sql
SELECT c.CategoryID, c.CategoryName, COUNT(p.ProductID) AS product_count
FROM Category AS c
LEFT JOIN Products AS p ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, c.CategoryName
ORDER BY COUNT(p.ProductID) ASC, c.CategoryID ASC;
```

The adaptation includes CategoryName in GROUP BY because it is selected and is neither aggregated nor otherwise grouped. Reviewed by inspection.

## Official solution

[PNP answer key, Q15](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/Source%20Materials/PrepNPlaced_SQL_100_v2/sql/all_100_solutions.sql)

```sql
SELECT cat.CategoryID,
       cat.CategoryName,
       COUNT(p.ProductID) AS product_count
FROM Category AS cat
LEFT JOIN Products AS p ON p.CategoryID = cat.CategoryID
GROUP BY cat.CategoryID, cat.CategoryName
ORDER BY product_count, cat.CategoryID;
```

### Official answer — SQLite adaptation

```sql
SELECT cat.CategoryID,
       cat.CategoryName,
       COUNT(p.ProductID) AS product_count
FROM Category AS cat
LEFT JOIN Products AS p ON p.CategoryID = cat.CategoryID
GROUP BY cat.CategoryID, cat.CategoryName
ORDER BY product_count, cat.CategoryID;
```

### Official answer — SQL Server adaptation

```sql
SELECT cat.CategoryID,
       cat.CategoryName,
       COUNT(p.ProductID) AS product_count
FROM Category AS cat
LEFT JOIN Products AS p ON p.CategoryID = cat.CategoryID
GROUP BY cat.CategoryID, cat.CategoryName
ORDER BY product_count, cat.CategoryID;
```

The answer key runs unchanged in SQLite and passed the extended test. The SQL Server version was reviewed by inspection.
