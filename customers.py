# Reflection
#1. I would use .get() for an optional field like for a customers email as I can show a default message if it is not provided or missing. 
#  I would use brackets for a specific required field, a customer tier may go missing which could cause an error that I can catch.
#2.  Exercise 8 remind me of excel pivot table as it groups some transactions by region and then adds up the sales for each group. 
# I think Python is useful for large datasets as it allows me to rerun the same script on new files and generates the summary without me doing calculations. 

# Exercise 1 - One customer 
customer = {
    "name": "Alice", 
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 750.00
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2 - Update and add
customer["phone"] = "555-0100"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3 - Safe lookup
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError as error:
    print(f"KeyError: {error}")

# Exercise 4 - Iterate
for key, value in customer.items():
    print(f"{key}: {value}")

# .items() gives each key and its value. Looping over customer gives only the keys.
for key in customer:
    print(key)

# Exercise 5 -Lookup table
tier_discounts = {
    "bronze": 0,
    "silver": 0.05, 
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount_rate = tier_discounts.get(tier, 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print(f"Tier: {tier}")
print(f"Discount: {discount_rate: .0%}")
print(f"Final price: ${final_price: .2f}")

# Exercise 6 -List of dicts
customers = [
    customer,
    {"name":"Ben", "tier": "silver"},
    {"name":"Maya", "tier": "gold"},
]

for shopper in customers:
    name = shopper ["name"]
    tier = shopper ["tier"]
    discounted_amount = 300 * tier_discounts.get(tier, 0)
    print(f"{name} ({tier}) - Discount: ${discounted_amount: .2f}")

# Exercise 7 -Nested catalog 
catalog = {
    "Widget A": {"price": 9.99,  "stock": 150},
    "Gadget C": {"price": 49.99,  "stock": 8}
}

for product_name, details in catalog.items():
    if details["stock"] <20:
        print(f"LOW STOCK: {product_name}")

# Exercise 8 -Sales by region
transactions =[
    {"region": "South", "amount": 300},
    {"region": "North",  "amount": 150},
    {"region": "South",  "amount": 200}
]
sales_by_region = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount']
    sales_by_region[region] = sales_by_region.get(region,0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: {sales_by_region[region]}")
