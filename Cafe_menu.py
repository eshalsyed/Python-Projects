# Menu
name = "Cafe".upper()
print(" " * 25)
print(name.center(25, "^"))
print("_" * 25)
print("Menu".ljust(10," ") + "Price".rjust(6," ") )
print("Cofee".ljust(10," ") + "£2".rjust(6, " "))
print("Toast".ljust(10," ") + "£4".rjust(6, " "))
print("Eggs".ljust(10," ") + "£3".rjust(6, " "))
print("Tea".ljust(10," ") + "£3".rjust(6, " "))

# Starting price
price = 0

# Spaces 
print (" " * 25)

# Ask for coffe
print (" " * 25)
coffe = input('Woud you like Coffe?')

if coffe.lower() == "yes": 
    price += 2 
else:
    price +=0

# Ask for Toast
print (" " * 25)
toast = input('Would you likea Toast?')
if toast.lower()== "yes":
    price += 4
else:
    price +=0

# Ask for Eggs
print (" " * 25)
eggs = input("Would you like to order Eggs?")
if eggs.lower() == "yes": 
    price += 4 
else:
    price += 0

# Ask for Tea
print (" " * 25)
tea = input("would you like Tea?")
if tea.lower() == "yes":
    price += 3
else:
    price += 0

# Final price
print (" " * 25)
print (f"Your final price is £{price}")
print("_" * 25)
