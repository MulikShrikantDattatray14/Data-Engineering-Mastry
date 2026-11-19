# PNP P004 — Customer emails that cannot be delivered

**Topic:** SQL Basics  
**Difficulty:** Easy

## Question

**Table colors** · 🟦 `Customers`

**Business scenario.** The marketing operations team is about to send a re-engagement campaign. Every hard bounce hurts the sender reputation, so they want to catch addresses that cannot work before the send. A valid address here has no spaces and the shape `something@something.something`.

**Task.** Return every customer whose 🟦 `Email` is missing, contains a space, or does not match the shape `_@_._` (at least one character, an @, at least one character, a dot, at least one character). Label the problem. Sort by `CustomerID`.

[PNP source question](../../../2.PNP-%20foundations%20and%20practice/8.%20Advance%20string%20functions%2C%20regex%20and%20clause/P004.%20Customer%20emails%20that%20cannot%20be%20delivered.md#question-and-image)

### Required output columns

One output row represents one customer whose stored email fails at least one of the specified checks.

| Output column | Source or calculation | Meaning and applicable rules | Example value |
| --- | --- | --- | --- |
| `CustomerID` | 🟦 `Customers.CustomerID` | Customer identifier. | 1 |
| `FirstName` | 🟦 `Customers.FirstName` | Customer’s first name. | Asha |
| `LastName` | 🟦 `Customers.LastName` | Customer’s last name. | Rao |
| `Email` | 🟦 `Customers.Email` | Email address as stored. | `NULL` |
| `issue` | 🟦 `Customers` | One of `Missing`, `Contains a space` or `Not in name@domain.tld form`. | Missing |

### Practice example · Sample input

**🟦 `Customers`**

| 🟦 CustomerID | 🟦 FirstName | 🟦 LastName | 🟦 Email |
| ---: | --- | --- | --- |
| 1 | Asha | Rao | `NULL` |
| 2 | Ben | Das | `ben das@example.com` |
| 3 | Cia | Sen | `cia.example.com` |
| 4 | Dev | Roy | `dev@example.com` |

### Expected output

| 🟦 CustomerID | 🟦 FirstName | 🟦 LastName | 🟦 Email | 🟦 issue |
| ---: | --- | --- | --- | --- |
| 1 | Asha | Rao | `NULL` | Missing |
| 2 | Ben | Das | `ben das@example.com` | Contains a space |
| 3 | Cia | Sen | `cia.example.com` | Not in name@domain.tld form |

[View sample inputs and output with colored cells](../../assets/question-samples/p004.svg?raw=1)

### How the sample produces this output

🟦 Asha (ID 1) has a missing address and receives `Missing`. Ben’s stored address contains a space between `ben` and `das`, so ID 2 receives `Contains a space`. Cia’s address has no `@`, so ID 3 receives `Not in name@domain.tld form`.

🟦 Dev’s address satisfies the stated shape and has no spaces. The three customers with issues appear in ID order with their original email values.

## Step 1 · Your approach before writing SQL

1. What does one row of the final output represent?
2. Which table would you put in `FROM`? If you need other tables, which comes second, third, and so on, and why?
3. Would you use a join at any step? For each join you choose, name its type and matching columns and explain why it fits the question.

<details>
<summary>Notes from the saved attempt</summary>

When an address has multiple issues, the saved attempt gives priority to `Missing`, followed by `Contains a space`, then `Not in name@domain.tld form`.

</details>

## Learner solution — SQLite

```sql
SELECT CustomerID, FirstName, LastName, Email,
       (CASE
          WHEN Email IS NULL OR LENGTH(Email) == 0 THEN 'Missing'
          WHEN Email LIKE '% %' THEN 'Contains a space'
          WHEN Email NOT LIKE '%_@_%._%' THEN 'Not in name@domain.tld form'
        END) AS issue
FROM Customers
WHERE Email IS NULL OR LENGTH(Email) == 0 OR Email LIKE '% %'
   OR Email NOT LIKE '%_@_%._%'
ORDER BY CustomerID ASC;
```

The learner's query logic is preserved. The saved version removes chat escaping and link formatting, uses regular spaces in the issue text, and uses single quotes for SQL string literals. SQLite checks covered the sample, empty emails, incomplete address parts, and label precedence.

## Visual walkthrough

[Open the Previous / Next walkthrough](../../assets/steps/PNP-P004/01.md)

Follow the sample rows through each query step. **Predict the result.** What happens to a valid address when the CASE checks find no issue?

![Customer emails that cannot be delivered. Only IDs 1, 2 and 3 remain. The final query orders the flagged customers by ID.](../../assets/walkthroughs/p004.svg)

[Open the full-size walkthrough](../../assets/walkthroughs/p004.svg?raw=1)

## Step-by-step walkthrough

🟦 **FROM Customers · one table is enough** · The contact list needs one decision per person. The stored email and the identity of the person to contact are already on the same customer row.

**How to start.** Which issue should win when several apply?

Use the same sample throughout and check the output after each step.

### 1. Assign the issue to each customer

**What to do.** Assign the issue to each customer.

**Why.** Each customer needs the first applicable label.

Run the `CASE` without the filter. Asha's missing email matches the first rule, Ben's space matches the second, and Cia's email fails the shape check. Dev's email matches none of the branches, so its issue is NULL.

```sql
SELECT CustomerID, FirstName, LastName, Email,
       (CASE
          WHEN Email IS NULL OR LENGTH(Email) == 0 THEN 'Missing'
          WHEN Email LIKE '% %' THEN 'Contains a space'
          WHEN Email NOT LIKE '%_@_%._%' THEN 'Not in name@domain.tld form'
        END) AS issue
FROM Customers
ORDER BY CustomerID ASC;
```

| CustomerID | FirstName | LastName | Email | issue |
| ---: | --- | --- | --- | --- |
| 1 | Asha | Rao | `NULL` | Missing |
| 2 | Ben | Das | ben das@example.com | Contains a space |
| 3 | Cia | Sen | cia.example.com | Not in name@domain.tld form |
| 4 | Dev | Roy | dev@example.com | `NULL` |

### 2. Keep only rows that fail a check

**What to do.** Keep only rows that fail a check.

**Why.** The report includes only rows with an issue.

Add the `WHERE` clause. Its alternatives keep a row when any issue applies. Dev drops out and the result remains in customer ID order.

```sql
SELECT CustomerID, FirstName, LastName, Email,
       (CASE
          WHEN Email IS NULL OR LENGTH(Email) == 0 THEN 'Missing'
          WHEN Email LIKE '% %' THEN 'Contains a space'
          WHEN Email NOT LIKE '%_@_%._%' THEN 'Not in name@domain.tld form'
        END) AS issue
FROM Customers
WHERE Email IS NULL OR LENGTH(Email) == 0 OR Email LIKE '% %'
   OR Email NOT LIKE '%_@_%._%'
ORDER BY CustomerID ASC;
```

| CustomerID | FirstName | LastName | Email | issue |
| ---: | --- | --- | --- | --- |
| 1 | Asha | Rao | `NULL` | Missing |
| 2 | Ben | Das | ben das@example.com | Contains a space |
| 3 | Cia | Sen | cia.example.com | Not in name@domain.tld form |

## Learner solution — SQL Server

```sql
SELECT CustomerID, FirstName, LastName, Email,
       (CASE
          WHEN Email IS NULL OR DATALENGTH(Email) = 0 THEN 'Missing'
          WHEN Email LIKE '% %' THEN 'Contains a space'
          WHEN Email NOT LIKE '%_@_%._%' THEN 'Not in name@domain.tld form'
        END) AS issue
FROM Customers
WHERE Email IS NULL OR DATALENGTH(Email) = 0 OR Email LIKE '% %'
   OR Email NOT LIKE '%_@_%._%'
ORDER BY CustomerID ASC;
```

The SQL Server adaptation uses `DATALENGTH` for the empty-string check because it counts trailing spaces. This assumes a variable-length email column and preserves the distinction between empty and spaces-only email values. Reviewed by inspection.

## Official solution

[PNP source notes](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/8.%20Advance%20string%20functions,%20regex%20and%20clause/P004.%20Customer%20emails%20that%20cannot%20be%20delivered.md)

```sql
SELECT c.CustomerID,
       c.FirstName,
       c.LastName,
       c.Email,
       CASE WHEN c.Email IS NULL OR TRIM(c.Email) = '' THEN 'Missing'
            WHEN c.Email LIKE '% %'                    THEN 'Contains a space'
            ELSE 'Not in name@domain.tld form'
       END AS issue
FROM Customers AS c
WHERE c.Email IS NULL
   OR TRIM(c.Email) = ''
   OR c.Email LIKE '% %'
   OR c.Email NOT LIKE '%_@_%._%'
ORDER BY c.CustomerID;
```

The official solution treats spaces-only emails as `Missing`. The learner solution labels them `Contains a space`, following the exercise's stated rule that NULL or empty values are missing.

### Official answer — SQLite adaptation

```sql
SELECT c.CustomerID,
       c.FirstName,
       c.LastName,
       c.Email,
       CASE WHEN c.Email IS NULL OR TRIM(c.Email) = '' THEN 'Missing'
            WHEN c.Email LIKE '% %'                    THEN 'Contains a space'
            ELSE 'Not in name@domain.tld form'
       END AS issue
FROM Customers AS c
WHERE c.Email IS NULL
   OR TRIM(c.Email) = ''
   OR c.Email LIKE '% %'
   OR c.Email NOT LIKE '%_@_%._%'
ORDER BY c.CustomerID;
```

### Official answer — SQL Server adaptation

```sql
SELECT c.CustomerID,
       c.FirstName,
       c.LastName,
       c.Email,
       CASE WHEN c.Email IS NULL OR TRIM(c.Email) = '' THEN 'Missing'
            WHEN CHARINDEX(' ', c.Email) > 0                    THEN 'Contains a space'
            ELSE 'Not in name@domain.tld form'
       END AS issue
FROM Customers AS c
WHERE c.Email IS NULL
   OR TRIM(c.Email) = ''
   OR CHARINDEX(' ', c.Email) > 0
   OR c.Email NOT LIKE '%_@_%._%'
ORDER BY c.CustomerID;
```

SQLite adaptation executed on representative fixtures. SQL Server adaptation reviewed by inspection.

## Verification

The saved learner query ran in SQLite on the [walkthrough fixture](../../assets/steps/PNP-P004/walkthrough.json). The column names and all 3 expected rows matched in the displayed order.
