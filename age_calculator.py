from datetime import date

def age():
    print("\nAge Calculator!👴\n")
    print("Enter your birth year to find out your age!")
    print("Enter 'quit' to exit\n")

    now = date.today().year  

    while True:

        user = input("Enter your birth year: ").strip()


        if user.lower() == "quit":
            print("Thanks for using the Age Calculator! Goodbye! 👋")
            break


        try:
            birth_year = int(user)  


            if birth_year > now or birth_year < 0:
                print(f"Invalid year. Please enter a year between 0 and {now}\n")
                continue


            age = now - birth_year
            print(f"You are {age} years old!!\n")

        except ValueError:
            print("Invalid input! Please enter a valid year (e.g 2025)\n")

age()
