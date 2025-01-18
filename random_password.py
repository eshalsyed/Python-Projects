
import random
import string

def main():
    print("Random Password Generator!")
    print("Strong passwords to keep your accounts safe n secure!")
    print("Type 'exit' to quit\n")

    while True:
        user = input("Enter the password length (Length like 8, 12, 16): ").strip()


        if user.lower() == "exit":
            break



        try:
            length = int(user)

            if length < 4:
                print("Password length must be at least 4 characters\n")
                continue

            letters = string.ascii_letters  
            digits = string.digits          
            symbols = string.punctuation    
            all_characters = letters + digits + symbols


            password = ''.join(random.choice(all_characters) for _ in range(length))

            print(f"Your generated password is: {password} \n")

        except ValueError:
            print("Invalid input! Please enter a valid number\n")


main()
