# Page 10 — Input and output

PNP Python mentorship practice. Each code block runs separately.

## 1. Ask for two numbers and print their sum

```python
# PNP Python Page 10 — Exercise 1

# Write your solution below
first=float(input("Enter first number"))
second=float(input("Enter Second number"))

final=first+second
print(final)
```

With inputs `10.5` and `20.5`, the sum is `31.0`.

## 2. Print a three-item receipt with right-aligned prices

```python
items = [
    ("Wireless Mouse", 799),
    ("Gel Pens", 149),
    ("Water Bottle", 399)
]

# Print each item with a right-aligned price
for i in items:
    print(f"{i[0]:<20}{i[1]:>10.2f}")
```

```text
Wireless Mouse          799.00
Gel Pens                149.00
Water Bottle            399.00
```

## 3. Enter 3.5 when the code calls int()

```python
raw = input("enter your age")

try:
    number = int(raw)
    print(number)
except ValueError:
    print("Please enter a valid age for number")
```

Typing `3.5` makes `int("3.5")` raise a `ValueError`. The `except` block catches it and prints the message. Typing `25` prints `25`.
