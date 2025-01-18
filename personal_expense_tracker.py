# Personal Expense Tracker 

print("\n💵This is your Personal Expense Tracker!💵 ")

expenses = []

def add_expenses():
    category = input("Enter category: ")
    amount = float(input("Enter amount: ")) 
    store = [category, amount]
    expenses.append(store)
    print("Expenses Added!")

def view_expenses():
    if not expenses:
        print("\n\n\nExpenses list is empty")
    else: 
        print(f"Here are your expenses:\n")
        for objects in expenses:
            print(f"{objects[0]} : £{objects[1]}")
        
    

def total_spendings():
    total = sum(money[1] for money in expenses)
    print(f"\n\n\nTotal Spendings: £{total}")


def menu():
    while True:
       
        # Menu
        print("\n1. Add a New Expenses👗🍕")
        print("2. View All Expenses👀")
        print("3. View Total Spending🛒🛍")
        print("4. Exit👋")
        
        # Asks user input 
        ask_option = int(input("\nSelect an option (1-4): "))

        # User input conditionals
        if ask_option == 1:
            add_expenses()
        elif ask_option == 2:
            view_expenses()
        elif ask_option == 3:
            total_spendings()
        elif ask_option == 4:
            print ("See you next time!")
            break
        else:
            print("\n\n\nInvalid option please select an option from 1 - 4: ")
menu()
