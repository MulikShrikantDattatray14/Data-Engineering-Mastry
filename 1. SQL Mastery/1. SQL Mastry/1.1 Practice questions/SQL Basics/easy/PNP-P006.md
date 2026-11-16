# PNP P006 — Most expensive products sold at full price

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

The promotions team needs up to ten of the most expensive products that currently sell at full price. Use the `Products` table.

- Calculate the discount as `Market_Price - Sale_Price`. Represent a zero discount as `NULL`.
- Exclude any product with a missing sale price or market price. Its discount is unknown.
- Keep only full-price products and show `Full price` in `discount_display`.
- Sort by `Sale_Price` descending, then `ProductID` ascending. Return up to ten rows.

### Sample input

| ProductID | Product | Brand | Sale_Price | Market_Price |
| --- | --- | --- | --- | --- |
| 1 | Mug | Home | 100 | 100 |
| 2 | Lamp | Home | 150 | 150 |
| 3 | Mystery | Home | `NULL` | 100 |
| 4 | Bottle | Home | 90 | 100 |

### Expected output

| ProductID | Product | Brand | Sale_Price | Market_Price | discount_display |
| --- | --- | --- | --- | --- | --- |
| 2 | Lamp | Home | 150 | 150 | Full price |
| 1 | Mug | Home | 100 | 100 | Full price |

Lamp comes first because it has the higher sale price. Mystery has a missing price, and Bottle has a discount. Only two rows qualify.

## Learner solution — SQLite

```sql
SELECT ProductID, Product, Brand, Sale_Price, Market_Price,
       'Full price' AS discount_display
FROM Products
WHERE Market_Price = Sale_Price
ORDER BY Sale_Price DESC, ProductID ASC
LIMIT 10;
```

The equality filter returns the requested rows directly. The original exercise also asks for an intermediate zero-to-NULL discount calculation, which is shown in the official solution below. SQLite checks covered the sample, missing prices, a sale price above market price, ties, and the ten-row limit.

## Step-by-step walkthrough

### 1. Compare the two prices on each row

This preview shows what SQLite evaluates for each product. It returns 1 for equal prices, 0 for unequal prices, and NULL when either price is missing.

```sql
SELECT ProductID, Product, Sale_Price, Market_Price,
       Market_Price = Sale_Price AS prices_match
FROM Products
ORDER BY ProductID;
```

| ProductID | Product | Sale_Price | Market_Price | prices_match |
| --- | --- | --- | --- | --- |
| 1 | Mug | 100 | 100 | 1 |
| 2 | Lamp | 150 | 150 | 1 |
| 3 | Mystery | `NULL` | 100 | `NULL` |
| 4 | Bottle | 90 | 100 | 0 |

### 2. Keep products with equal prices

The `WHERE` clause keeps only comparisons that are true. Mug and Lamp pass. Mystery drops out because its comparison is unknown, and Bottle drops out because its prices differ.

```sql
SELECT ProductID, Product, Brand, Sale_Price, Market_Price
FROM Products
WHERE Market_Price = Sale_Price
ORDER BY ProductID;
```

| ProductID | Product | Brand | Sale_Price | Market_Price |
| --- | --- | --- | --- | --- |
| 1 | Mug | Home | 100 | 100 |
| 2 | Lamp | Home | 150 | 150 |

### 3. Label and rank the full-price products

Every remaining row qualifies for the constant `Full price` label. Sort by sale price descending and use product ID ascending for ties. Apply the ten-row limit after sorting. Only two rows qualify in this sample.

```sql
SELECT ProductID, Product, Brand, Sale_Price, Market_Price,
       'Full price' AS discount_display
FROM Products
WHERE Market_Price = Sale_Price
ORDER BY Sale_Price DESC, ProductID ASC
LIMIT 10;
```

| ProductID | Product | Brand | Sale_Price | Market_Price | discount_display |
| --- | --- | --- | --- | --- | --- |
| 2 | Lamp | Home | 150 | 150 | Full price |
| 1 | Mug | Home | 100 | 100 | Full price |

## Learner solution — SQL Server

```sql
SELECT TOP (10) ProductID, Product, Brand, Sale_Price, Market_Price,
       'Full price' AS discount_display
FROM Products
WHERE Market_Price = Sale_Price
ORDER BY Sale_Price DESC, ProductID ASC;
```

The SQL Server adaptation uses `TOP (10)` and was reviewed by inspection.

## Method 2 — Explicit CASE (SQLite)

```sql
select ProductID, Product, Brand,Sale_Price,Market_Price,
(
case when  (Sale_Price is not null and Market_Price is not null) and (Market_Price - Sale_Price)=0 then 'Full price'
end 
) as discount_display
from Products
where  (Sale_Price is not null and Market_Price is not null) and (
    CASE
        WHEN Market_Price - Sale_Price = 0 THEN NULL
        ELSE Market_Price - Sale_Price
    END
) IS NULL
order by Sale_Price desc , ProductID asc
limit 10
```

### 1. Keep products with both prices

The two price checks exclude Mystery. Otherwise a missing price would also yield a NULL discount and pass the later NULL test.

```sql
SELECT ProductID, Sale_Price, Market_Price FROM Products WHERE Sale_Price IS NOT NULL AND Market_Price IS NOT NULL ORDER BY ProductID;
```

| ProductID | Sale_Price | Market_Price |
| ---: | ---: | ---: |
| 1 | 100 | 100 |
| 2 | 150 | 150 |
| 4 | 90 | 100 |

### 2. Calculate the discount and convert zero to NULL

Mug and Lamp have equal prices, so their zero discounts become NULL. Bottle keeps its discount of 10.

```sql
SELECT ProductID, CASE WHEN Market_Price - Sale_Price = 0 THEN NULL
                       ELSE Market_Price - Sale_Price END AS discount
FROM Products
WHERE Sale_Price IS NOT NULL AND Market_Price IS NOT NULL
ORDER BY ProductID;
```

| ProductID | discount |
| ---: | ---: |
| 1 | `NULL` |
| 2 | `NULL` |
| 4 | 10 |

### 3. Keep NULL discounts, label, and sort

The final SQLite query above applies `IS NULL` to the computed discount. Bottle drops out. The SELECT expression labels the remaining rows `Full price`. Lamp sorts ahead of Mug, and the limit allows up to ten rows.

| ProductID | Product | Brand | Sale_Price | Market_Price | discount_display |
| --- | --- | --- | --- | --- | --- |
| 2 | Lamp | Home | 150 | 150 | Full price |
| 1 | Mug | Home | 100 | 100 | Full price |

### Method 2 — SQL Server

```sql
SELECT TOP (10) ProductID, Product, Brand,Sale_Price,Market_Price,
(
case when  (Sale_Price is not null and Market_Price is not null) and (Market_Price - Sale_Price)=0 then 'Full price'
end 
) as discount_display
from Products
where  (Sale_Price is not null and Market_Price is not null) and (
    CASE
        WHEN Market_Price - Sale_Price = 0 THEN NULL
        ELSE Market_Price - Sale_Price
    END
) IS NULL
order by Sale_Price desc , ProductID asc;
```

This adaptation uses `TOP (10)` and was reviewed by inspection.

## Official solution

The [PNP source notes](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/11.%20NULL%20Logic/P006.%20Most%20expensive%20products%20that%20are%20never%20discounted.md) reproduce this PostgreSQL answer key query.

```sql
SELECT p.ProductID,
       p.Product,
       p.Brand,
       p.Sale_Price,
       p.Market_Price,
       COALESCE(NULLIF(p.Market_Price - p.Sale_Price, 0)::text, 'Full price') AS discount_display
FROM Products AS p
WHERE p.Sale_Price IS NOT NULL
  AND p.Market_Price IS NOT NULL
  AND NULLIF(p.Market_Price - p.Sale_Price, 0) IS NULL
ORDER BY p.Sale_Price DESC, p.ProductID
LIMIT 10;
```

The key uses `NULLIF` for the zero-to-NULL conversion. The learner uses equality directly to produce the same final rows.
