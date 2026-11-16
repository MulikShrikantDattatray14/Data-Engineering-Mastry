# PNP P006 — Most expensive products sold at full price

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

From `Products`, calculate the discount as `Market_Price - Sale_Price` and represent a zero discount as SQL NULL. Exclude products missing either price. Keep up to ten known full-price products, sorted by sale price descending and product ID ascending. Return the five sample columns and `discount_display` containing `Full price`.

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

Lamp and Mug have equal sale and market prices. Lamp sells for more. Mystery has an unknown discount and Bottle has a discount of 10.

## Learner solution — SQLite

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

SQLite checks covered the sample, each missing-price case, a negative discount, ties, and the ten-row limit. The learner used an explicit `CASE` expansion after guidance on `NULLIF` and missing-price handling.

## Step-by-step walkthrough

### 1. Keep products with both prices

Check both columns. Mystery drops out because its sale price is missing.

```sql
SELECT ProductID, Product, Brand, Sale_Price, Market_Price
FROM Products
WHERE Sale_Price IS NOT NULL AND Market_Price IS NOT NULL
ORDER BY ProductID;
```

| ProductID | Product | Brand | Sale_Price | Market_Price |
| --- | --- | --- | --- | --- |
| 1 | Mug | Home | 100 | 100 |
| 2 | Lamp | Home | 150 | 150 |
| 4 | Bottle | Home | 90 | 100 |

### 2. Calculate the discount and replace zero with NULL

The subtraction is zero for Mug and Lamp. Bottle retains its discount of 10. At this stage every row has both prices, so a NULL discount means full price.

```sql
SELECT ProductID,
       CASE WHEN Market_Price - Sale_Price = 0 THEN NULL
            ELSE Market_Price - Sale_Price
       END AS discount
FROM Products
WHERE Sale_Price IS NOT NULL AND Market_Price IS NOT NULL
ORDER BY ProductID;
```

| ProductID | discount |
| ---: | ---: |
| 1 | `NULL` |
| 2 | `NULL` |
| 4 | 10 |

### 3. Keep full-price rows, label them, and take the top ten

Apply the learner's NULL filter and `CASE` label, then sort before applying the limit. Bottle drops out and Lamp comes before Mug.

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

| ProductID | Product | Brand | Sale_Price | Market_Price | discount_display |
| --- | --- | --- | --- | --- | --- |
| 2 | Lamp | Home | 150 | 150 | Full price |
| 1 | Mug | Home | 100 | 100 | Full price |

## Learner solution — SQL Server

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

The adaptation uses `TOP (10)` with the same ordering and was reviewed by inspection.

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

The key uses `NULLIF` for the zero-to-NULL conversion. The learner expands that logic using `CASE`.
