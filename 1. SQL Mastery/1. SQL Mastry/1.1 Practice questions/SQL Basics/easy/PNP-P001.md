# PNP P001 — Brand directory

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

Build an alphabetical list of brands for the catalogue's Shop by brand filter. Use `Products` and return one column named `Brand`. Return one row per clean brand name. Ignore surrounding spaces and exclude NULL, empty strings, and names consisting only of spaces.

### Schema

The exercise uses `Products`. The sample shows `ProductID` (integer) and `Brand` (nullable text). Only `Brand` is required to solve the problem.

### Sample input

| ProductID | Brand |
| ---: | --- |
| 1 | `'Nike'` |
| 2 | `' Nike '` |
| 3 | `NULL` |
| 4 | `''` |
| 5 | `'   '` |
| 6 | `'Adidas'` |
| 7 | `'Puma'` |
| 8 | `'Adidas'` |

### Expected output

| Brand |
| --- |
| Adidas |
| Nike |
| Puma |

Products 1 and 2 represent the same brand after removing surrounding spaces. Products 6 and 8 share a brand. Products 3–5 have no usable brand.

## Learner solution — SQLite

```sql
select distinct trim(Brand) as Brand
from Products
where trim(Brand)is not null and length(trim(Brand))>0
order by trim(Brand) asc
```

The exact query was run against all eight sample rows in SQLite. The column name and all three rows matched the expected output in order.

## Learner solution — SQL Server

```sql
SELECT DISTINCT TRIM(Brand) AS Brand
FROM Products
WHERE TRIM(Brand) IS NOT NULL
  AND LEN(TRIM(Brand)) > 0
ORDER BY Brand ASC;
```

This adaptation uses SQL Server's `LEN` and sorts by the output alias. It was reviewed by inspection.

## Official solution

The [repository's PNP P001 source notes](<../../../2.PNP- foundations and practice/0. SQL basics/P001. Brand directory.md>) reproduce this query from the PNP answer key.

```sql
SELECT DISTINCT p.Brand
FROM Products AS p
WHERE NULLIF(TRIM(p.Brand), '') IS NOT NULL
ORDER BY p.Brand;
```

The official query trims brand names for filtering and returns raw brand names. On the illustrative sample, it treats the two Nike spellings as distinct in SQLite.

## Step-by-step walkthrough

1. Read `Brand` from `Products`. Use `TRIM(Brand)` as the cleaned value for both filtering and display. The padded Nike value in product 2 is now comparable to the Nike value in product 1.
2. Build the `WHERE` condition using both `TRIM(Brand) IS NOT NULL` and `LENGTH(TRIM(Brand)) > 0`. The first condition handles product 3. The second removes products 4 and 5, whose cleaned names have length zero.
3. Select `DISTINCT TRIM(Brand) AS Brand` so the duplicate check uses the cleaned text. Products 1 and 2 now count as one brand, and the same rule combines products 6 and 8.
4. Add `ORDER BY TRIM(Brand) ASC`. The final output is the three rows in the expected output table.
