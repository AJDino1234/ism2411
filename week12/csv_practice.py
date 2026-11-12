# Reflection 1
# Python allows me to repeat the same calculations and filter all of my new sales files
# by running one script. Excel on the other hand makes it easier by inspecting individual rows and trying out formulas and filters directly on the screen. 
# 
# Reflection 2 
# A store may log the date, time, and revenue when it runs a sales report. 
# Append mode keeps the earlier entires so the manager can look at past runs. 

import csv
from datetime import datetime
from pathlib import Path

# Exercise 1: Get the sales file
data_folder=Path(__file__).resolve().parent / "data"
sales_file=data_folder / "sales.csv"

with sales_file.open(encoding="utf-8-sig", newline="") as file:
    reader=csv.reader(file)
    header=next(reader)
    row_count = sum(1 for row in reader)

print(f"Columns: {header}")
print(f"Data rows: {row_count}")

# Exercise 2- Read and print raw rows
print("/nExercise 2 -Raw rows")

with sales_file.open(encoding="utf-8-sig", newline="") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

# Exercise 3 - Skip the header 
print("/nExercise 3 - Header and data")

with sales_file.open(encoding="utf-8-sig", newline="") as file:
    reader= csv.reader(file)
    header=next(reader)
    print(f"Header: {header}")
    
    sales_rows = list(reader)
    for row in sales_rows:
        print(row)

# Exercise 4 -Compute  totals
print("/nExercise 4 - Compute totals")

total_revenue = 0
sales_with_totals = []

for product, price_text, quantity_text in sales_rows:
    price = float(price_text)
    quantity = int(quantity_text)
    total = price * quantity
    total_revenue += total
    sales_with_totals.append((product,price,quantity,total))
    print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

# Exercise 5 Filter and write 
print("/nExercise 5 - Filter and write")

rows_written = 0

with (data_folder / "cleaned.csv").open("w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Product", "Price", "Quantity", "Total"])

    for product, price, quantity, total in sales_with_totals:
        if total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
            rows_written += 1

print(f"Wrote {rows_written} of {len(sales_rows)} data rows.")

# Exercise 6 - csv.DictReader
# Use csv.reader when the file doesn't have a header and you know the column order.
# Use csv.DictReader when you want to access columns by name.
print("/nExercise 6 - csv.DictReader")

dict_total_revenue = 0
dict_row_totals = []

with sales_file.open(encoding="utf-8-sig", newline="") as file:
    reader=csv.DictReader(file)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total_revenue += total
        dict_row_totals.append((product, price, quantity, total))
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"DictReader total revenue: ${dict_total_revenue:.2f}")
print(f"Matches Exercise 4: {dict_row_totals == sales_with_totals}")

# Exercise 7 Sales Summary by product
print("/nExercise 7 - Sales summary by product")

revenue_by_product = {}

for product, price, quantity, total in dict_row_totals:
    revenue_by_product[product]= revenue_by_product.get(product, 0) + total

for product in sorted(revenue_by_product):
    print(f"{product}: ${revenue_by_product[product]:.2f}")

# Exercise 8 - Append mode log
print("/nExercise 8 - Append mode log")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with (data_folder / "run_log.txt") .open("a", encoding="utf-8") as file:
    file.write(f"{timestamp} | Total revenue: ${total_revenue:.2f}\n")

print("Added one entry to data/run_log.txt.")