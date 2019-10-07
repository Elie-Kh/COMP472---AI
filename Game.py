
board_game = [
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
        ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ]
column_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]


# printing a 10 x 12 array to set up the game board
def gameboard():
    # Creating the board
    # Labelling columns with alphabet letters
    for i in range(len(column_letters)):
        if i == 0:
            print('  ' + column_letters[i], end='')
        else:
            print('  ' + column_letters[i], end='')
    print()

    # labelling each row with numbers and printing the board
    for row in range(len(board_game)):
        for col in range(len(board_game[row])):
            if col != 0:
                print(board_game[row][col], end='')
            else:
                print(str(row)+ " " + board_game[row][col], end='')
        print()
    return board_game


def win_check():
    # function to be defined
    return


# Variables below are used in the function
# p_play variables are for getting user input
play_x = 0
play_y = 0
p_play_x = 0
p_play_y = 0
p1_turn = True
p1_tokens = 15
p2_tokens = 15
moves = 0
win = False
validMove = False

while moves != 30 or win is False:
    while validMove is False:
        p_play_x = input("enter X coordinate")
        p_play_y = input("enter Y coordinate")
        try:
            play_x = int(p_play_x)
            play_y = int(p_play_y)
            print(play_x, ' ', play_y)
        except ValueError:
            print("Invalid input")
            continue
        if board_game[play_x][play_y] != "( )" or play_x > 11 or play_y > 9:
            print('invalid Move')
        else:
            validMove = True

    if p1_turn is True:
        board_game[play_x][play_y] = "(X)"
        p1_turn = False
    else:
        board_game[play_x][play_y] = "(O)"
        p1_turn = True
    validMove = False
    gameboard()
