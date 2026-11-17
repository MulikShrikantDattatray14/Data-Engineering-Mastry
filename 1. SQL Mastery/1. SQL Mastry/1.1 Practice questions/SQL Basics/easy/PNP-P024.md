# P024 · Suppliers outside India or with no email

**Topic** SQL Basics  
**Difficulty** ![EASY](../../../_badges/easy.svg)

## Question

Using `Suppliers`, return every supplier with at least one of these issues.

- `Country missing` when `Country` is SQL `NULL`.
- `Outside India` when `Country` is present and differs from India after trimming spaces and ignoring case.
- `No email` when `Email` is SQL `NULL`, empty, or contains only spaces.

Return `SupplierID`, `CompanyName`, `Country`, `Email`, and `issue`. Preserve the original values in the first four columns. When both issues apply, put the country issue first and separate the labels with `; `. Sort by `SupplierID` ascending.

### Sample input

| SupplierID | CompanyName | Country | Email |
|---:|---|---|---|
| 1 | Local Foods | India | local@example.com |
| 2 | Global Goods | USA | NULL |
| 3 | Mystery Supply | NULL | mystery@example.com |

### Expected output

| SupplierID | CompanyName | Country | Email | issue |
|---:|---|---|---|---|
| 2 | Global Goods | USA | NULL | Outside India; No email |
| 3 | Mystery Supply | NULL | mystery@example.com | Country missing |

Local Foods has neither issue. Global Goods is outside India and has no email. Mystery Supply has a missing country and a present email.

## My final solution · SQLite

```sql
SELECT SupplierID, CompanyName, Country, Email,
    CASE
        WHEN Country IS NULL
             AND (TRIM(Email) IS NULL OR LENGTH(TRIM(Email)) = 0)
            THEN 'Country missing; No email'
        WHEN TRIM(LOWER(Country)) != 'india'
             AND (TRIM(Email) IS NULL OR LENGTH(TRIM(Email)) = 0)
            THEN 'Outside India; No email'
        WHEN Country IS NULL THEN 'Country missing'
        WHEN TRIM(LOWER(Country)) != 'india' THEN 'Outside India'
        WHEN TRIM(Email) IS NULL OR LENGTH(TRIM(Email)) = 0 THEN 'No email'
    END AS issue
FROM Suppliers
WHERE Country IS NULL
   OR TRIM(LOWER(Country)) != 'india'
   OR TRIM(Email) IS NULL
   OR LENGTH(TRIM(Email)) = 0
ORDER BY SupplierID ASC;
```

## My solution · SQL Server

```sql
SELECT SupplierID, CompanyName, Country, Email,
    CASE
        WHEN Country IS NULL
             AND (TRIM(Email) IS NULL OR LEN(TRIM(Email)) = 0)
            THEN 'Country missing; No email'
        WHEN TRIM(LOWER(Country)) != 'india'
             AND (TRIM(Email) IS NULL OR LEN(TRIM(Email)) = 0)
            THEN 'Outside India; No email'
        WHEN Country IS NULL THEN 'Country missing'
        WHEN TRIM(LOWER(Country)) != 'india' THEN 'Outside India'
        WHEN TRIM(Email) IS NULL OR LEN(TRIM(Email)) = 0 THEN 'No email'
    END AS issue
FROM Suppliers
WHERE Country IS NULL
   OR TRIM(LOWER(Country)) != 'india'
   OR TRIM(Email) IS NULL
   OR LEN(TRIM(Email)) = 0
ORDER BY SupplierID ASC;
```

## Walkthrough

### 1. Decide what one output row represents

Read one row per supplier from `Suppliers`. Select the four original fields so any spaces or casing in the stored data remain visible. At this point the sample shows suppliers 1, 2, and 3.

### 2. Keep suppliers with any issue

Add the `WHERE` conditions. Check `Country IS NULL` explicitly because a comparison with a NULL country evaluates to unknown. Trim the country and lowercase it for comparison with `'india'`. Trim the email so a string of spaces becomes empty. Use `OR` because any issue qualifies the supplier.

| SupplierID | Country check | Email check | Result |
|---:|---|---|---|
| 1 | India | Present | Excluded |
| 2 | Outside India | Missing | Kept |
| 3 | Country missing | Present | Kept |

### 3. Build the issue text

Add `CASE` to the select list. SQLite returns the first matching branch, so check the two-issue combinations first. Supplier 2 reaches the second branch and gets both labels. Supplier 3 reaches the single missing-country branch and gets one label.

| SupplierID | Matching branch | issue |
|---:|---|---|
| 2 | Outside India and missing email | Outside India; No email |
| 3 | Missing country | Country missing |

### 4. Sort and check the edge cases

Add `ORDER BY SupplierID ASC` to guarantee the sample order of 2, then 3. The SQLite checks also covered a NULL country with a spaces-only email, a padded mixed-case India with an empty email, a padded foreign country with a present email, and a padded India with a present email.

## Official answer · Source dialect

```sql
SELECT s.SupplierID,
       s.CompanyName,
       s.Country,
       s.Email,
       CONCAT_WS('; ',
           CASE WHEN s.Country IS NULL                 THEN 'Country missing'
                WHEN UPPER(TRIM(s.Country)) <> 'INDIA' THEN 'Outside India'
           END,
           CASE WHEN s.Email IS NULL OR TRIM(s.Email) = '' THEN 'No email'
           END) AS issue
FROM Suppliers AS s
WHERE s.Country IS NULL
   OR UPPER(TRIM(s.Country)) <> 'INDIA'
   OR s.Email IS NULL
   OR TRIM(s.Email) = ''
ORDER BY s.SupplierID;
```

## Official answer · SQLite adaptation

```sql
SELECT s.SupplierID,
       s.CompanyName,
       s.Country,
       s.Email,
       RTRIM(
           COALESCE(CASE WHEN s.Country IS NULL                 THEN 'Country missing'
                WHEN UPPER(TRIM(s.Country)) <> 'INDIA' THEN 'Outside India'
           END || '; ', '') ||
           COALESCE(CASE WHEN s.Email IS NULL OR TRIM(s.Email) = '' THEN 'No email'
           END, ''), '; ') AS issue
FROM Suppliers AS s
WHERE s.Country IS NULL
   OR UPPER(TRIM(s.Country)) <> 'INDIA'
   OR s.Email IS NULL
   OR TRIM(s.Email) = ''
ORDER BY s.SupplierID;
```

## Official answer · SQL Server adaptation

```sql
SELECT s.SupplierID,
       s.CompanyName,
       s.Country,
       s.Email,
       CONCAT_WS('; ',
           CASE WHEN s.Country IS NULL                 THEN 'Country missing'
                WHEN UPPER(TRIM(s.Country)) <> 'INDIA' THEN 'Outside India'
           END,
           CASE WHEN s.Email IS NULL OR TRIM(s.Email) = '' THEN 'No email'
           END) AS issue
FROM Suppliers AS s
WHERE s.Country IS NULL
   OR UPPER(TRIM(s.Country)) <> 'INDIA'
   OR s.Email IS NULL
   OR TRIM(s.Email) = ''
ORDER BY s.SupplierID;
```

The official SQL Server form uses `CONCAT_WS` and `TRIM`, available in SQL Server 2017 and later.
