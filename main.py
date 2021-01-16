# two player traditional tic tac toe

game_over = 0

board = ["-","-","-","-","-","-","-","-","-"]

def show_board():
    print(board[0],board[1],board[2])
    print(board[3],board[4],board[5])
    print(board[6],board[7],board[8])

def place(input_value):
    if turn_of_x == 1:
        if board[input_value] == "-":
            board[input_value] = "X"
            show_board()
            control_game_end("X")
        else:
            print("this place is already used")
            new_inp = int(input("please enter a new value: "))
            place(new_inp)

    elif turn_of_x == 0:
        if board[input_value] == "-":
            board[input_value] = "O"
            show_board()
            control_game_end("O")
        else:
            print("this place is already used")
            new_inp = int(input("please enter a new value: "))
            place(new_inp)

def control_game_end(check_for):
    global game_over
    global winner
    # there are 8 possible ways to win the game

    # first i'll check rows
    for i in range(0,3):
        if board[i] == check_for and board[i+1] == check_for and board[i+2] == check_for:
            game_over = 1
            winner = check_for

    # secondly lets check columns
    for i in range(0,3):
        if board[i]== check_for and board[i+3]== check_for and board[i+6] == check_for:
            game_over = 1
            winner = check_for

    # and lastly lets check diagonally
    if board[0] == check_for and board[4] == check_for and board[8] == check_for:
        game_over = 1
        winner = check_for
    elif board[2] == check_for and board[4] == check_for and board[6] == check_for:
        game_over = 1
        winner = check_for

turn_of_x = 0
while game_over != 1:
    if turn_of_x ==1:
        input_val = int(input("where do you want the X: "))
        place(input_val)
        turn_of_x = 0

    elif turn_of_x == 0:
        input_val = int(input("where do you want the O: "))
        place(input_val)
        turn_of_x = 1

print("game over winner is {}".format(winner))
