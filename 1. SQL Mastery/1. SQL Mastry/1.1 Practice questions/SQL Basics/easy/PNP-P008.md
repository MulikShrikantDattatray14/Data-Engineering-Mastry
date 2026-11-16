# PNP P008 — Price band labels

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

Return every product with one price band based on `Sale_Price`. Label prices below 200 as Budget, prices from 200 inclusive to 700 exclusive as Mid, prices at or above 700 as Premium, and missing prices as Unknown. Return `ProductID`, `Product`, `Sale_Price`, and `price_band`, sorted by product ID ascending.

### Sample input

| ProductID | Product | Sale_Price |
| --- | --- | --- |
| 1 | Pen | 199 |
| 2 | Book | 200 |
| 3 | Bag | 699.50 |
| 4 | Watch | 700 |
| 5 | Mystery | `NULL` |

### Expected output

| ProductID | Product | Sale_Price | price_band |
| --- | --- | --- | --- |
| 1 | Pen | 199 | Budget |
| 2 | Book | 200 | Mid |
| 3 | Bag | 699.50 | Mid |
| 4 | Watch | 700 | Premium |
| 5 | Mystery | `NULL` | Unknown |

Book is Mid at 200 and Bag remains Mid at 699.50. Watch starts Premium at 700. Mystery stays in the output as Unknown.

## Learner solution — SQLite

```sql
select ProductID,Product,Sale_Price,
(
case
when Sale_Price < 200 then "Budget"
when Sale_Price >=200 and Sale_Price < 700 then "Mid"
when Sale_Price>=700 then"Premium"
else "Unknown"
end
) as 
price_band
from Products
order by ProductID asc
```

The exact query passed in the tested SQLite configuration, which accepts double-quoted string literals. Checks covered the sample, output names and order, NULL, and fractional prices just below each threshold.

## Step-by-step walkthrough

### 1. Label prices below 200

The first branch labels Pen. With only this branch and no ELSE, the other labels are NULL for now.

```sql
SELECT ProductID, Product, Sale_Price,
       CASE
           WHEN Sale_Price < 200 THEN 'Budget'
       END AS price_band
FROM Products
ORDER BY ProductID ASC;
```

| ProductID | Product | Sale_Price | price_band |
| --- | --- | --- | --- |
| 1 | Pen | 199 | Budget |
| 2 | Book | 200 | `NULL` |
| 3 | Bag | 699.50 | `NULL` |
| 4 | Watch | 700 | `NULL` |
| 5 | Mystery | `NULL` | `NULL` |

### 2. Add the Mid range

Book and Bag satisfy both limits. The upper bound is exclusive, so Watch stays outside Mid.

```sql
SELECT ProductID, Product, Sale_Price,
       CASE
           WHEN Sale_Price < 200 THEN 'Budget'
           WHEN Sale_Price >= 200 AND Sale_Price < 700 THEN 'Mid'
       END AS price_band
FROM Products
ORDER BY ProductID ASC;
```

| ProductID | Product | Sale_Price | price_band |
| --- | --- | --- | --- |
| 1 | Pen | 199 | Budget |
| 2 | Book | 200 | Mid |
| 3 | Bag | 699.50 | Mid |
| 4 | Watch | 700 | `NULL` |
| 5 | Mystery | `NULL` | `NULL` |

### 3. Complete the labels

The final query adds Premium for Watch. Mystery's NULL price makes all three numeric conditions unknown, so ELSE supplies Unknown. All five rows remain, sorted by product ID.

```sql
select ProductID,Product,Sale_Price,
(
case
when Sale_Price < 200 then "Budget"
when Sale_Price >=200 and Sale_Price < 700 then "Mid"
when Sale_Price>=700 then"Premium"
else "Unknown"
end
) as 
price_band
from Products
order by ProductID asc
```

| ProductID | Product | Sale_Price | price_band |
| --- | --- | --- | --- |
| 1 | Pen | 199 | Budget |
| 2 | Book | 200 | Mid |
| 3 | Bag | 699.50 | Mid |
| 4 | Watch | 700 | Premium |
| 5 | Mystery | `NULL` | Unknown |

## Learner solution — SQL Server

```sql
select ProductID,Product,Sale_Price,
(
case
when Sale_Price < 200 then 'Budget'
when Sale_Price >=200 and Sale_Price < 700 then 'Mid'
when Sale_Price>=700 then'Premium'
else 'Unknown'
end
) as 
price_band
from Products
order by ProductID asc;
```

The adaptation uses single-quoted text literals and was reviewed by inspection. The same quoting also passed in SQLite.

## Official solution

The [PNP source notes](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/1.%20Intro%20to%20SQL%20and%20Advanced%20Select/P008.%20Price%20band%20labels.md) reproduce this answer key query.

```sql
SELECT p.ProductID,
       p.Product,
       p.Sale_Price,
       CASE
           WHEN p.Sale_Price IS NULL THEN 'Unknown'
           WHEN p.Sale_Price < 200   THEN 'Budget'
           WHEN p.Sale_Price < 700   THEN 'Mid'
           ELSE 'Premium'
       END AS price_band
FROM Products AS p
ORDER BY p.ProductID;
```

The official solution checks NULL first and uses the ordering of the CASE branches to shorten the remaining comparisons. The learner's query expresses the ranges explicitly.
