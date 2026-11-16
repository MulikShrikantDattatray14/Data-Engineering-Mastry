# PNP P002 — Ten highest-priced products

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

The merchandising team needs ten products for its **Premium picks** carousel. From the `Products` table, return the ten products with the highest `Sale_Price`, highest first. Exclude products with a `NULL` price. If prices tie, the product with the lower `ProductID` comes first.

Return `ProductID`, `Product`, `Brand`, and `Sale_Price` in that order.

### Sample input

| ProductID | Product | Brand | Sale_Price |
| ---: | --- | --- | ---: |
| 4 | Mug | Home | 100 |
| 20 | Bottle | Home | 100 |
| 30 | Sticker | Home | 0 |
| 31 | Mystery item | Home | `NULL` |
| 101 | Headphones | Nova | 900 |
| 102 | Tablet | Nova | 800 |
| 103 | Monitor | Pixel | 700 |
| 104 | Keyboard | Typeco | 600 |
| 105 | Speaker | Nova | 500 |
| 106 | Router | Netco | 400 |
| 107 | Camera | Pixel | 300 |
| 108 | Mouse | Typeco | 200 |
| 109 | Lamp | Home | 150 |

### Expected output

| ProductID | Product | Brand | Sale_Price |
| ---: | --- | --- | ---: |
| 101 | Headphones | Nova | 900 |
| 102 | Tablet | Nova | 800 |
| 103 | Monitor | Pixel | 700 |
| 104 | Keyboard | Typeco | 600 |
| 105 | Speaker | Nova | 500 |
| 106 | Router | Netco | 400 |
| 107 | Camera | Pixel | 300 |
| 108 | Mouse | Typeco | 200 |
| 109 | Lamp | Home | 150 |
| 4 | Mug | Home | 100 |

In order, the returned `ProductID` values are `101, 102, 103, 104, 105, 106, 107, 108, 109, 4`. Each row includes all four requested columns. Mug takes the last slot because it ties with Bottle on price and has the lower ID.

### Schema

The relevant columns in `Products` are `ProductID` (integer identifier), `Product` and `Brand` (text), and `Sale_Price` (nullable number). Return those four columns in that order.

## Learner solution — SQLite

```sql
select ProductID,Product, Brand, Sale_Price 
from Products
where Sale_Price is not null
order by Sale_Price desc, ProductID asc
limit 10
```

Verified in SQLite on the sample, with fewer than ten priced products including a zero-price row, and with only NULL prices.

## Step-by-step walkthrough

Use the same sample throughout.

### 1. Exclude products without a price

Only Mystery item has a NULL price. Sticker stays eligible at a price of zero. This diagnostic query sorts by product ID to make the remaining rows easy to find in the sample.

```sql
select ProductID,Product, Brand, Sale_Price 
from Products
where Sale_Price is not null
order by ProductID
```

| ProductID | Product | Brand | Sale_Price |
| ---: | --- | --- | ---: |
| 4 | Mug | Home | 100 |
| 20 | Bottle | Home | 100 |
| 30 | Sticker | Home | 0 |
| 101 | Headphones | Nova | 900 |
| 102 | Tablet | Nova | 800 |
| 103 | Monitor | Pixel | 700 |
| 104 | Keyboard | Typeco | 600 |
| 105 | Speaker | Nova | 500 |
| 106 | Router | Netco | 400 |
| 107 | Camera | Pixel | 300 |
| 108 | Mouse | Typeco | 200 |
| 109 | Lamp | Home | 150 |

### 2. Sort by price and break ties by product ID

Switch to descending price, then ascending product ID for equal prices. Mug now appears immediately before Bottle at positions 10 and 11.

```sql
select ProductID,Product, Brand, Sale_Price 
from Products
where Sale_Price is not null
order by Sale_Price desc, ProductID asc
```

| ProductID | Product | Brand | Sale_Price |
| ---: | --- | --- | ---: |
| 101 | Headphones | Nova | 900 |
| 102 | Tablet | Nova | 800 |
| 103 | Monitor | Pixel | 700 |
| 104 | Keyboard | Typeco | 600 |
| 105 | Speaker | Nova | 500 |
| 106 | Router | Netco | 400 |
| 107 | Camera | Pixel | 300 |
| 108 | Mouse | Typeco | 200 |
| 109 | Lamp | Home | 150 |
| 4 | Mug | Home | 100 |
| 20 | Bottle | Home | 100 |
| 30 | Sticker | Home | 0 |

### 3. Keep the first ten rows

Apply the limit to the sorted result. Mug fills the last slot, while Bottle and Sticker fall below the cutoff.

```sql
select ProductID,Product, Brand, Sale_Price 
from Products
where Sale_Price is not null
order by Sale_Price desc, ProductID asc
limit 10
```

| ProductID | Product | Brand | Sale_Price |
| ---: | --- | --- | ---: |
| 101 | Headphones | Nova | 900 |
| 102 | Tablet | Nova | 800 |
| 103 | Monitor | Pixel | 700 |
| 104 | Keyboard | Typeco | 600 |
| 105 | Speaker | Nova | 500 |
| 106 | Router | Netco | 400 |
| 107 | Camera | Pixel | 300 |
| 108 | Mouse | Typeco | 200 |
| 109 | Lamp | Home | 150 |
| 4 | Mug | Home | 100 |

## Learner solution — SQL Server

```sql
SELECT TOP (10) ProductID, Product, Brand, Sale_Price
FROM Products
WHERE Sale_Price IS NOT NULL
ORDER BY Sale_Price DESC, ProductID ASC;
```

The SQL Server version applies `TOP (10)` with the same ordering. It was reviewed by inspection.

## Official solution

The [PNP source notes](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/1.%20Intro%20to%20SQL%20and%20Advanced%20Select/P002.%20Ten%20highest-priced%20products.md) reproduce this query from the PNP answer key.

```sql
SELECT p.ProductID,
       p.Product,
       p.Brand,
       p.Sale_Price
FROM Products AS p
WHERE p.Sale_Price IS NOT NULL
ORDER BY p.Sale_Price DESC,
         p.ProductID
LIMIT 10;
```

The source query uses table aliases and relies on ascending order as the default for `ProductID`. It produces the same ordering as the learner's explicit `ASC`.
