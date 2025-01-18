import random


choices = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissors! 🎮")
print("Choose Rock, Paper or Scissors")
print("If you wish to quit type 'quit'\n")

while True:
    
    player_choice = input("Your choice: ").lower()
    

    if player_choice == "quit":
        print("Thanks for playing! Goodbye! 👋")
        break

    if player_choice not in choices:
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.\n")
        continue


    computer_choice = random.choice(choices)


    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")


    if player_choice == computer_choice:
        print("It's a tie! 🤝\n")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        print("You win! 🎉\n")
    else:
        print("You lose! 😢\n")
