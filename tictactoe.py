import random

board = [1,2,3,
         4,5,6,
         7,8,9]


def show(board):
    print("            |            |           ")
    print(f"      {board[0]}     |      {board[1]}     |     {board[2]}     ")
    print("            |            |           ")
    print("-------------------------------------")
    print("            |            |           ")
    print(f"      {board[3]}     |      {board[4]}     |     {board[5]}     ")
    print("            |            |           ")
    print("-------------------------------------")
    print("            |            |           ")
    print(f"      {board[6]}     |      {board[7]}     |     {board[8]}     ")
    print("            |            |           ")


def win(board, player):
    w_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]
        ]
    
    for condition in w_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False 


def draw(board):
    return all(move == 'X' or move == 'O' for move in board)


def milo(board, milo_sym):
    while True:
        place_m = random.randint(1, 9)
        if board[place_m - 1] == str(place_m): 
            board[place_m - 1] =   milo_sym
            print(f"Milo placed {milo_sym} at position {place_m}")
            break


def player_choice(board, player_sym):
    while True:
        try:
            place = int(input("Enter your move (1-9): "))
            if board[place - 1] == str(place):  
                board[place - 1] = player_sym  
                break
            else:
                print("This position is already being used.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")


def choosing_xoro():
    while True:

        x_or = input("Do you want to be X or O? ")

        if x_or.upper() in ['X', 'O']:

            if x_or.upper() == 'X':
                return 'X', 'O'  
            else:
                return 'O', 'X'  
        
        else:
            print("Invalid choice. Please choose X or O.")

def main():

    board = [str(i) for i in range(1, 10)]  

    print("\nTIC TAC TOE!")
    print("In this game of Tic Tac Toe you will be playing against Milo!")
    player_sym, milo_sym = choosing_xoro()
    print(f"You are {player_sym} and Milo is {milo_sym}")

    show(board)

    while True:

        player_choice(board,player_sym)
        show(board)

        if win(board, player_sym):
            print("You WON!!!!")
            break

        elif draw(board):
            print("Draw!")
            break

        milo(board,milo_sym)
        show(board)

        if win(board, milo_sym):
            print("Milo won! Better luck next time.")
            break

        elif draw(board):
            print("Draw!")
            break

main()
