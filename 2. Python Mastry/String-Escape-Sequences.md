# String escape sequences and triple quotes

## Newline and tab

`\n` starts a new line. `\t` inserts a tab. The visible width of a tab depends on where it appears and how the output is displayed.

~~~python
print("orders\npayments")
print("Product\tPrice")
print("Keyboard\t1499")
~~~

## Multiline SQL strings

Triple quotes preserve the line breaks typed inside the string. Printing the string displays the SQL. A database cursor can execute it with `cursor.execute(query)`.

~~~python
query = """SELECT product_name, price
FROM products
WHERE price > 1000
ORDER BY price DESC"""

print(query)
~~~

## Verified learner checkpoint

~~~python
print("A\tB\nC")
~~~

A and B appear on the first line with a tab between them. C appears on the second line.
