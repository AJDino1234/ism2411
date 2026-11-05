# Reflection answers will go here

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
