def main():
    print("Word Counter! 📝")
    print("Enter a sentence or paragraph to count the words.")
    print("Type 'exit' to exit\n")

    while True:
        
        user = input("Enter your text: ").strip()


        if user.lower() == "exit":
            break


        if user == "":
            print("You didn't enter any text. Please try again!\n")
        else:
            words = user.split()  
            amount = len(words)    
            print(f"The text contains {amount} word(s)\n")


main()
