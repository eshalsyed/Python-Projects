# Build a shopping receipt 

# Asking for product and price
products = input("Enter the names of 3 products you have bought (separated by spaces): ")
price = input("Enter the prices of each product (separate by spaces): ") 

# Correct capitalisation of products
products.title() 

# Splitting to be concentated 
sp = products.split()
pp = price.split()

# Convert price strings to floats
pp = [float(p) for p in pp]

# Adds all prices in pp
total_price = sum(pp)

# List of products and prices side by side
conc_0 = f"{sp[0]}, £{pp[0]:.2f}"
conc_1 = f"{sp[1]}, £{pp[1]:.2f}"
conc_2 = f"{sp[2]}, £{pp[2]:.2f}"


# Checking for discount
discount = 0
if total_price > 50:
    discount = total_price * 0.1
else:
    print(f"Next time spend more than £50 to get a 10% discount!")


heading = "shopping receipt"

# Printing everything
print("_" * 24)
print(heading.upper())
print("_" * 24)

# Displaying the products with the prices
print(f"{conc_0.ljust(24)}") 
print(f"{conc_1.ljust(24)}")
print(f"{conc_2.ljust(24)}")
print("_" * 24)

# Displaying price and discount 
print(f"Total price: £{total_price:.2f}")
print(f"Discount: -£{discount:.2f}")
print("_" * 24)

# Displaying Final price after discount
final_price = total_price - discount
print(f"Final price: £{final_price:.2f}")
print("_" * 24)

# Thank you message
print(" " * 24)
print("Thank you for shopping with us!")
