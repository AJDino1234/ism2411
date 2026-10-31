# --- Self-Assesment ---
# 1. The first bug was missing a colon in the loop. When I used Chatgpt it told me the error and allowed me to figure it out and fix it myself. 
# I do think I need more practice identifying the error messages to determine what I missed. 
# 2. appply_discount(price, tier) gives us a price and a tier. It re turns the price after either a gold, silver or bronze discout, and doesn't give a discount for any other tier. 
# I think someone could use this if they know their inputs and can figure out it's returnede value. 
# 3. Ai disclosure: I used ai when I made a mistake on exercise 4 as it gave me an explanation for my error and allowed me to fix it myself and clarify if it was good to code. 
# The ai helped me learn more about discounts, loops and how to complete code with no errors. 

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate
print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: $ {apply_discount(200, tier): .2f}")

# ---Exercise 3 ---
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax= calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax
discounted=apply_discount(200, "gold")
total= final_price(200, "gold", 0.07)
print(f"After gold discount:${discounted:.2f}")
print(f"After tax: ${total:.2f}")
print(f'final_price(200, "gold", 0.07)= ${total:.2f}')

#--- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total=final_price(price, tier, 0.07)
    print(f"Price: ${price} Tier: {tier} Final: ${total:.2f}")

# --- Exercise 5 ---
# The for loop needed a colon.
# total += sale adds each sale instead of repacing the total.
# Using < preventsthe while loop from accessing an invalid index.
sales= [120, 80, 250, 175, 90]
total=0
for sale in sales:
    total +=sale
print(f"Total: ${total}")
count =0
for sale in sales:
    count += 1 
print(f"Count: {count}")
i=0
while i < len(sales):
    print(sales[i])
    i += 1

# --- Exercise 6 ---
# The x inside double_it is local so it does not change global x.
# The functions returns 1998,  global x remains at 100. 
x=100
def double_it ():
    x=999
    return x * 2
print(x)
print(double_it())
print(x)