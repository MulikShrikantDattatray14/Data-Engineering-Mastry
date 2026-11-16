# PNP P003 — Customers in metro cities

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

Marketing is launching same-day delivery in **Bengaluru, Mumbai, Delhi, Hyderabad, and Chennai**. From `Customers`, return the customers who live in those cities.

- Match city names regardless of letter case and surrounding spaces.
- Include `Bangalore`, `Bombay`, and `New Delhi` as alternate names for Bengaluru, Mumbai, and Delhi.
- Display `City` with surrounding spaces removed. Keep its original spelling and letter case.
- Sort alphabetically by the displayed city, ignoring case, then by `CustomerID` ascending.

Return `CustomerID`, `FirstName`, `LastName`, `City`, and `State` in that order.

### Sample input

Quotes make surrounding spaces visible.

| CustomerID | FirstName | LastName | City | State |
| ---: | --- | --- | --- | --- |
| 12 | Asha | Rao | `' Bengaluru '` | Karnataka |
| 5 | Nisha | Shah | `'MUMBAI'` | Maharashtra |
| 21 | Riya | Patil | `'Pune'` | Maharashtra |
| 3 | Dev | Kumar | `'Delhi'` | Delhi |
| 7 | Mira | Das | `'Bengaluru'` | Karnataka |
| 9 | Farah | Ali | `' Chennai '` | Tamil Nadu |
| 14 | Isha | Kumar | `'Bangalore'` | Karnataka |
| 6 | Omar | Khan | `' Bombay '` | Maharashtra |
| 8 | Lea | Singh | `'New Delhi'` | Delhi |

### Expected output

| CustomerID | FirstName | LastName | City | State |
| ---: | --- | --- | --- | --- |
| 14 | Isha | Kumar | Bangalore | Karnataka |
| 7 | Mira | Das | Bengaluru | Karnataka |
| 12 | Asha | Rao | Bengaluru | Karnataka |
| 6 | Omar | Khan | Bombay | Maharashtra |
| 9 | Farah | Ali | Chennai | Tamil Nadu |
| 3 | Dev | Kumar | Delhi | Delhi |
| 5 | Nisha | Shah | MUMBAI | Maharashtra |
| 8 | Lea | Singh | New Delhi | Delhi |

Pune is outside the launch area. Both Bengaluru rows qualify, and customer 7 comes before customer 12 because they have the same displayed city.

### Schema

The relevant columns are `CustomerID` (integer identifier), `FirstName`, `LastName`, `City`, and `State` (text). Return them in that order.

## Learner solution — SQLite

```sql
select CustomerID,FirstName,LastName,trim(City) as City,State
from Customers
where trim(lower(City)) in ("bengaluru","mumbai","delhi","hyderabad","chennai","bangalore","bombay","new delhi")
order by trim(lower(City)) asc, CustomerID asc
```

The exact submission passed in SQLite with double-quoted string literal compatibility enabled. Single quotes are the standard spelling for string literals and produce the same result in SQLite. The checks also covered a mixed-case city tied on the sort key, Hyderabad, NULL, and a spaces-only value.

## Step-by-step walkthrough

### 1. Check the displayed value and the matching value

Use `TRIM(City)` for display and `TRIM(LOWER(City))` for comparison. This diagnostic query shows both values for each sample row. Mumbai illustrates the difference between preserving case for display and normalizing it for matching.

```sql
SELECT CustomerID, City AS OriginalCity, TRIM(City) AS City,
       TRIM(LOWER(City)) AS MatchCity
FROM Customers
ORDER BY CustomerID;
```

| CustomerID | OriginalCity | City | MatchCity |
| ---: | --- | --- | --- |
| 3 | `'Delhi'` | Delhi | delhi |
| 5 | `'MUMBAI'` | MUMBAI | mumbai |
| 6 | `' Bombay '` | Bombay | bombay |
| 7 | `'Bengaluru'` | Bengaluru | bengaluru |
| 8 | `'New Delhi'` | New Delhi | new delhi |
| 9 | `' Chennai '` | Chennai | chennai |
| 12 | `' Bengaluru '` | Bengaluru | bengaluru |
| 14 | `'Bangalore'` | Bangalore | bangalore |
| 21 | `'Pune'` | Pune | pune |

### 2. Keep eligible cities

Use the normalized value in the filter and return the trimmed display value. Pune is removed and all three alternate names are retained. This intermediate query still displays the rows in customer ID order for inspection.

```sql
select CustomerID,FirstName,LastName,trim(City) as City,State
from Customers
where trim(lower(City)) in ("bengaluru","mumbai","delhi","hyderabad","chennai","bangalore","bombay","new delhi")
order by CustomerID;
```

| CustomerID | FirstName | LastName | City | State |
| ---: | --- | --- | --- | --- |
| 3 | Dev | Kumar | Delhi | Delhi |
| 5 | Nisha | Shah | MUMBAI | Maharashtra |
| 6 | Omar | Khan | Bombay | Maharashtra |
| 7 | Mira | Das | Bengaluru | Karnataka |
| 8 | Lea | Singh | New Delhi | Delhi |
| 9 | Farah | Ali | Chennai | Tamil Nadu |
| 12 | Asha | Rao | Bengaluru | Karnataka |
| 14 | Isha | Kumar | Bangalore | Karnataka |

### 3. Apply the requested ordering

Use the normalized city as the first sort key and `CustomerID` as the second. The two Bengaluru rows now sit together, with customer 7 before customer 12.

```sql
select CustomerID,FirstName,LastName,trim(City) as City,State
from Customers
where trim(lower(City)) in ("bengaluru","mumbai","delhi","hyderabad","chennai","bangalore","bombay","new delhi")
order by trim(lower(City)) asc, CustomerID asc
```

| CustomerID | FirstName | LastName | City | State |
| ---: | --- | --- | --- | --- |
| 14 | Isha | Kumar | Bangalore | Karnataka |
| 7 | Mira | Das | Bengaluru | Karnataka |
| 12 | Asha | Rao | Bengaluru | Karnataka |
| 6 | Omar | Khan | Bombay | Maharashtra |
| 9 | Farah | Ali | Chennai | Tamil Nadu |
| 3 | Dev | Kumar | Delhi | Delhi |
| 5 | Nisha | Shah | MUMBAI | Maharashtra |
| 8 | Lea | Singh | New Delhi | Delhi |

## Learner solution — SQL Server

```sql
select CustomerID,FirstName,LastName,trim(City) as City,State
from Customers
where trim(lower(City)) in ('bengaluru','mumbai','delhi','hyderabad','chennai','bangalore','bombay','new delhi')
order by trim(lower(City)) asc, CustomerID asc;
```

The SQL Server adaptation uses single-quoted literals. It was reviewed by inspection.

## Official solution

The [PNP source notes](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/1.%20Intro%20to%20SQL%20and%20Advanced%20Select/P003.%20Customers%20in%20metro%20cities.md) reproduce this PostgreSQL query from the answer key.

```sql
SELECT c.CustomerID,
       c.FirstName,
       c.LastName,
       TRIM(c.City) AS City,
       c.State
FROM Customers AS c
WHERE LOWER(TRIM(c.City)) IN ('bengaluru', 'bangalore', 'mumbai', 'bombay',
                                'delhi', 'new delhi', 'hyderabad', 'chennai')
ORDER BY TRIM(c.City), c.CustomerID;
```

The official query orders by the trimmed city using the database collation. The learner query explicitly normalizes case in the sort key to match the exercise's case-insensitive ordering.
