# Self assesment questions
# 1. This assignment helped me learn about negative indexes and let me access items from the end. 
# I originally expected to need the lists's length to find the last item but now know I dont.

# 2. In a finance class, I could use a list to store the companies mon thly business expenses. 
# Python allows me to get the total and average quicker than it could be calculated manually. 

# Exercise 1: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

# Exercise 2: Index practice 
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3: Slicing 
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2 ])

# Exercise 4: Modify
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# Exercise 5: Tuple comparison
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught. Tuples cannot be changed.")
    print("Tuples are useful when you have coordinates as they prevent additional accidental changes.")

print(coords)

# Exercise 6: Average of a list of sales
sales= [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7: Accumulator pattern
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.9, 2))

print("Original:", prices)
print("Discounted:", discounted)

# Exercise 8: Filter above threshold
sales= [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print( "Average:", round(sum(high_sales) / len(high_sales), 2))

