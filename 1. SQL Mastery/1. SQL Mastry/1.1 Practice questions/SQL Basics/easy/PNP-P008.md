# PNP P008 — Price band labels

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

Merchandising is adding a **Shop by budget** filter. Return every row from `Products` with exactly one label based on `Sale_Price`.

| Price band | Rule |
|---|---|
| `Budget` | Below 200 |
| `Mid` | At least 200 and below 700 |
| `Premium` | 700 or above |
| `Unknown` | `NULL` price |

Return `ProductID`, `Product`, `Sale_Price`, and `price_band`, sorted by `ProductID` ascending.

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

`699.50` is still Mid. Premium starts at exactly `700`.

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

**How to start.** Which label owns each threshold?

Use the same sample throughout and check the output after each step.

### 1. Label prices below 200

**What to do.** Label prices below 200.

**Why.** Budget ends immediately before 200.

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

**What to do.** Add the Mid range.

**Why.** Mid includes fractional prices below 700.

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

**What to do.** Complete the labels.

**Why.** A missing price still needs its own label.

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

### Official answer — SQLite adaptation

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

### Official answer — SQL Server adaptation

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

SQLite adaptation executed on representative fixtures. SQL Server adaptation reviewed by inspection.
