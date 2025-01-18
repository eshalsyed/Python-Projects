def leap():
    print("\nLeap Year Checker!\n")
    print("Leap year rules:")
    print("- A year is a leap year if it is divisible by 4\n- but not divisible by 100\n- unless it is also divisible by 400\n")
    
    print("Enter a year to check if it's a leap year.")
    print("Enter 'quit' to exit\n")

    while True:

        user = input("Enter a year: ").strip()


        if user.lower() == "quit":
            print("Bye bye!")
            break


        try:
            year = int(user)  
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print(f"{year} is a Leap Year! 🎉\n")
            else:
                print(f"{year} is not a Leap Year :( \n")
        except ValueError:
            print("Invalid input! Please enter a valid year (e.g 2025)\n")


leap()
