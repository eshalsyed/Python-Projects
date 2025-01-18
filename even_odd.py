def main():
    print("Even or Odd Checker!")
    print("Enter a number to check if it's even or odd.")
    print("Type 'quit' to exit the program.\n")

    while True:

        user_choice = input("Enter a number: ").strip()

        
        if user_choice.lower() == "quit":
            print("Bye!!")
            break

        try:
            number = int(user_choice)  

            if number % 2 == 0:
                print(f"{number} is Even!\n")
            else:
                print(f"{number} is Odd!\n")


        except ValueError:
            print("Invalid input! Please enter a valid number\n")


main()
