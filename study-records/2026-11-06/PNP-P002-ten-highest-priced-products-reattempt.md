# PNP P002 — Ten highest-priced products (SQL source reattempt 2)

**Study date:** 2026-11-06 (Asia/Kolkata) · **Status:** Pending independent learner attempt.  
**PNP status:** Already solved previously (October 26); new independent *reattempt* pending; no new source-completion credit.  
**Source:** [Original P002 source record](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/1.%20SQL%20Mastery/1.%20SQL%20Mastry/2.PNP-%20foundations%20and%20practice/1.%20Intro%20to%20SQL%20and%20Advanced%20Select/P002.%20Ten%20highest-priced%20products.md). That record contains an earlier student/source answer; **do not consult it during the reattempt**.

## Independently worded problem statement (no answer spoiler)

A merchandising team needs exactly ten product entries for its **Premium Picks** showcase. Select the ten products with the greatest `Sale_Price`, highest price first. Ignore products with a `NULL` price. When two products have the same sale price, use the **smaller `ProductID` first** so the cut-off decision stays stable. A product priced at zero is not automatically invalid (though it may not rank among the top ten).

Return precisely these columns in order: `ProductID`, `Product`, `Brand`, `Sale_Price`.

## Sample input — Products

This **illustrative** sample is from the earlier P002 source record, not a claim about rows in the full PNP commerce dataset.

| ProductID | Product | Brand | Sale_Price |
|---:|---|---|---:|
| 4 | Mug | Home | 100 |
| 20 | Bottle | Home | 100 |
| 30 | Sticker | Home | 0 |
| 31 | Mystery item | Home | NULL |
| 101 | Headphones | Nova | 900 |
| 102 | Tablet | Nova | 800 |
| 103 | Monitor | Pixel | 700 |
| 104 | Keyboard | Typeco | 600 |
| 105 | Speaker | Nova | 500 |
| 106 | Router | Netco | 400 |
| 107 | Camera | Pixel | 300 |
| 108 | Mouse | Typeco | 200 |
| 109 | Lamp | Home | 150 |

## Expected output

| ProductID | Product | Brand | Sale_Price |
|---:|---|---|---:|
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

## Explain each expected row and exclusion (no SQL algorithm)

- **101–109:** Their prices 900, 800, 700, 600, 500, 400, 300, 200 and 150 are the nine highest priced entries in descending order.
- **Product 4 (Mug):** Its price is 100. It takes the **tenth** slot because it ties with Bottle (ProductID 20) but its ID is smaller.
- **Product 20 (Bottle):** Also priced 100, but loses the final-slot tie break to Product 4.
- **Product 30 (Sticker):** Has a legitimate numeric price of 0, but ranks below the top ten, so it is not selected.
- **Product 31 (Mystery item):** Its price is NULL, so it is ineligible.
- Exactly **ten rows**, **four columns** and fixed price/ID ordering are required.

## Learner workspace — withheld until attempt

**Step 1 student reasoning:** Pending.  
**Original independent SQLite submission:** Pending.  
**Actual executed SQLite output/errors:** Pending.  
**Independently corrected learner versions:** Pending.  
**Assistant-reviewed SQLite reference:** Withheld.  
**Assistant-reviewed SQL Server / T-SQL reference:** Withheld.  
**Earlier source key:** Not shown to avoid spoiling the independent reattempt.  
**Optional new learning Yes/No:** Pending.  
**Question closing checkpoint in both repositories:** Pending.

[Learning repository record](https://github.com/MulikShrikantDattatray14/data-engineering-journey/blob/main/study-records/2026-11-06/PNP-P002-ten-highest-priced-products-reattempt.md) · [Mastry mirror](https://github.com/MulikShrikantDattatray14/Data-Engineering-Mastry/blob/main/study-records/2026-11-06/PNP-P002-ten-highest-priced-products-reattempt.md)
