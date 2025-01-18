def calculator():
    print("Simple Calculator!")
    print("You can perform the following operations:")
    print("\nAddition: +\nSubtraction: -\nMultiplication: *\nDivision: /\n")
    print("Type 'quit' to exit.\n")


    while True:

        try:

            num1 = float(input("Enter the first number: "))
            operation = input("Enter an operation (+, -, *, /): ").strip()

            if operation.lower() == "quit":
                print("Goodbye👋")
                break
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation. Please enter symbol from +, -, *, /.\n")
                continue
            num2 = float(input("Enter the second number: "))


            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':

                if num2 == 0:
                    print("Error: Division by zero is not allowed!\n")
                    continue
                result = num1 / num2

            print(f"The result is: {result}\n")

        except ValueError:
            print("Invalid input! Please enter numeric values.\n")


calculator()
