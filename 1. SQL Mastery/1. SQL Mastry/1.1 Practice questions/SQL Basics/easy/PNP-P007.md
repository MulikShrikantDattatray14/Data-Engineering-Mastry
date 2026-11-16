# PNP P007 — Discount amount and percentage per product

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

The pricing team wants to see how much each product is discounted. Return **every product** from `Products` with these columns in order:

`ProductID`, `Product`, `Market_Price`, `Sale_Price`, `discount_amount`, `discount_pct`

- `discount_amount` is the market price minus the sale price.
- `discount_pct` is the discount as a percentage of the market price, rounded to two decimal places.
- If `Market_Price` is `NULL` or zero, return `NULL` for both calculated columns and keep the product in the result.
- Sort by `discount_pct` highest first, with `NULL` values last.

### Sample input

| ProductID | Product | Market_Price | Sale_Price |
| --- | --- | --- | --- |
| 1 | Mug | 100 | 80 |
| 2 | Sticker | 0 | 0 |
| 3 | Lamp | 200 | 150 |

### Expected output

| ProductID | Product | Market_Price | Sale_Price | discount_amount | discount_pct |
| --- | --- | --- | --- | --- | --- |
| 3 | Lamp | 200 | 150 | 50 | 25.00 |
| 1 | Mug | 100 | 80 | 20 | 20.00 |
| 2 | Sticker | 0 | 0 | `NULL` | `NULL` |

Lamp comes first because 50 is 25% of its market price. Sticker stays in the result, with both discount values unknown because its market price is zero.

## Learner solution — SQLite

```sql
select 
ProductID,
Product,
 Market_Price,
Sale_Price,
(
case
when Market_Price is null or Market_Price =0 then Null
else (Market_Price - Sale_Price)
end 
) as discount_amount,
(
case
when Market_Price is null or Market_Price =0 then Null
else round((  ((Market_Price - Sale_Price)*100.0/ Market_Price)),2)
end 
) 

 as discount_pct
from Products
order by discount_pct desc
```

Verified on the sample and additional cases covering missing prices, a zero sale price, a sale price above market price, and a 3.33% discount. SQLite may display a numeric value like 25.00 as 25.0. The tables show two decimal places for readability.

## Step-by-step walkthrough

### 1. Calculate the discount amount

Return every product. The first CASE sets Sticker's discount to NULL because its market price is zero.

```sql
select 
ProductID,
Product,
 Market_Price,
Sale_Price,
(
case
when Market_Price is null or Market_Price =0 then Null
else (Market_Price - Sale_Price)
end 
) as discount_amount
from Products
order by ProductID
```

| ProductID | Product | Market_Price | Sale_Price | discount_amount |
| --- | --- | --- | --- | --- |
| 1 | Mug | 100 | 80 | 20 |
| 2 | Sticker | 0 | 0 | `NULL` |
| 3 | Lamp | 200 | 150 | 50 |

### 2. Calculate the percentage

Multiply the difference by 100.0 before dividing by the market price. In SQLite this promotes the arithmetic to real division. Lamp's calculation is 50 × 100.0 ÷ 200, which rounds to 25.00. The preview is ordered by product ID.

```sql
select 
ProductID,
Product,
 Market_Price,
Sale_Price,
(
case
when Market_Price is null or Market_Price =0 then Null
else (Market_Price - Sale_Price)
end 
) as discount_amount,
(
case
when Market_Price is null or Market_Price =0 then Null
else round((  ((Market_Price - Sale_Price)*100.0/ Market_Price)),2)
end 
) 

 as discount_pct
from Products
order by ProductID
```

| ProductID | Product | Market_Price | Sale_Price | discount_amount | discount_pct |
| --- | --- | --- | --- | --- | --- |
| 1 | Mug | 100 | 80 | 20 | 20.00 |
| 2 | Sticker | 0 | 0 | `NULL` | `NULL` |
| 3 | Lamp | 200 | 150 | 50 | 25.00 |

### 3. Sort the result

Order by discount percentage descending. SQLite puts the NULL percentages last in this order, so Lamp comes first and Sticker appears at the end.

```sql
select 
ProductID,
Product,
 Market_Price,
Sale_Price,
(
case
when Market_Price is null or Market_Price =0 then Null
else (Market_Price - Sale_Price)
end 
) as discount_amount,
(
case
when Market_Price is null or Market_Price =0 then Null
else round((  ((Market_Price - Sale_Price)*100.0/ Market_Price)),2)
end 
) 

 as discount_pct
from Products
order by discount_pct desc
```

| ProductID | Product | Market_Price | Sale_Price | discount_amount | discount_pct |
| --- | --- | --- | --- | --- | --- |
| 3 | Lamp | 200 | 150 | 50 | 25.00 |
| 1 | Mug | 100 | 80 | 20 | 20.00 |
| 2 | Sticker | 0 | 0 | `NULL` | `NULL` |

## Learner solution — SQL Server

```sql
select 
ProductID,
Product,
 Market_Price,
Sale_Price,
(
case
when Market_Price is null or Market_Price =0 then Null
else (Market_Price - Sale_Price)
end 
) as discount_amount,
(
case
when Market_Price is null or Market_Price =0 then Null
else round((  ((Market_Price - Sale_Price)*100.0/ Market_Price)),2)
end 
) 

 as discount_pct
from Products
order by discount_pct desc;
```

The decimal literal also avoids integer division in SQL Server. Descending order puts NULLs last. Reviewed by inspection.

## Official solution

The [PNP source notes](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/1.%20Intro%20to%20SQL%20and%20Advanced%20Select/P007.%20Discount%20amount%20and%20percentage%20per%20product.md) reproduce the answer key query.

```sql
SELECT p.ProductID,
       p.Product,
       p.Market_Price,
       p.Sale_Price,
       NULLIF(p.Market_Price, 0) - p.Sale_Price                                      AS discount_amount,
       ROUND(100.0 * (p.Market_Price - p.Sale_Price) / NULLIF(p.Market_Price, 0), 2) AS discount_pct
FROM Products AS p
ORDER BY discount_pct DESC NULLS LAST,
         p.ProductID;
```
