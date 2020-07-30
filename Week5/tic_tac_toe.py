#----- Global Variables -------

# Game board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-", ]

# If game is still going
game_still_going = True

#Who won? Or tie?
winner = None

# Whos turn is it
current_player = "X"

# Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Play game of tic tac toe
def play_game():

    #Display intial board
    display_board()

    # While the game is still going
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to other player
        flip_player()

    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")

# handle a single turn of an arbitrary turn player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    #Checking if user has a valid input
    while not valid:

        #If one of the valid positions are not chosen, input correct number
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1
        #Checks if there is already an input in the space
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again")


    board[position] = player

    display_board()

def check_if_game_over():
    check_if_winner()
    check_if_tie()

def check_if_winner():

    # Set up global variables
    global winner

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return

def check_rows():
    # Set up global variable
    global game_still_going
    # check if any of the rows have all the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner X or O
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return  board[6]
    return

def check_columns():
    # Set up global variable
    global game_still_going
    # check if any of the columns have all the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return the winner X or O
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return

def check_diagonals():
    # Set up global variable
    global game_still_going
    # check if any of the diagonal have all the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    # If
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # Return the winner X or O
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return
    return

def flip_player():
    # global variables we need
    global current_player
    # if the current player was x, then change it to O
    if current_player == "X":
        current_player = "O"
        # If current player was O, then change it to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()