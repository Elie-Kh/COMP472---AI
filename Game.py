
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


def move_check(y,x,turn,moving):
    try:
        play_y_f = int(y)
        try:
            play_x_f = int(x)
        except ValueError:
            if x in x_dict:
                play_x_f = int(x_dict[x])
            else:
                print("Invalid input")
                move_validity = [0, 0, False, False]
                return move_validity
    except ValueError:
        print("Invalid input")
        move_validity = [0, 0, False, False]
        return move_validity
    if play_x_f <= 11 and play_y <= 9:
        if board_game[play_y_f][play_x_f] != "( )":
            if turn is True and moving is False:
                if board_game[play_y_f][play_x_f] == "(O)":
                    print('Invalid Move')
                    move_validity = [0, 0, False, False]
                    return move_validity
                else:
                    print('Are you sure you want to move your token')
                    validmove_f = True
                    move_validity = [play_x_f, play_y_f, validmove_f, True]
                    return move_validity
            elif moving is False:
                if board_game[play_y_f][play_x_f] == "(X)":
                    print('Invalid Move')
                    move_validity = [0, 0, False, False]
                    return move_validity
                else:
                    validmove_f = True
                    move_validity = [play_x_f, play_y_f, validmove_f, True]
                    return  move_validity
        else:
            validmove_f = True
            move_validity = [play_x_f, play_y_f, validmove_f, False]
            return move_validity
    else:
        print('Invalid Move')
        move_validity = [0, 0, False, False]
        return move_validity
    print('Invalid Move')
    move_validity = [0, 0, False, False]
    return move_validity


# Variables below are used in the function
# p_play variables are for getting user input
play_x = 0
play_y = 0
p_play_x = 0
p_play_y = 0
play_x_old = 0
play_y_old = 0
x_dict = dict(A='0', B='1', C='2', D='3', E='4', F='5', G='6', H='7', I='8', J='9', K='10', L='11')
p1_turn = True
p1_tokens = 15
p2_tokens = 15
moves = 0
win = False
validMove = False
mover = False

while moves != 30 or win is False:
    while validMove is False:
        p_play_x = input("enter X coordinate")
        p_play_y = input("enter Y coordinate")
        checker = move_check(p_play_y, p_play_x,p1_turn,False)
        validMove = checker[2]
        mover = checker[3]
        if validMove is True:
            play_x = checker[0]
            play_y = checker[1]
    if mover is True:
        confirm = input('Are you sure you want to move your token? Enter Y or N')
        while confirm not in ("Y","N"):
            confirm = input('Are you sure you want to move your token? Enter Y or N')
        if confirm == "Y":
            print("choose your new position")
            play_x_old = play_x
            play_y_old = play_y
            validMove = False
            mover = True
            while validMove is False:
                p_play_x = input("enter X coordinate")
                p_play_y = input("enter Y coordinate")
                checker = move_check(p_play_y, p_play_x, p1_turn,mover)
                validMove = checker[2]
                if validMove is True:
                    play_x = checker[0]
                    play_y = checker[1]

        else:
            validMove = False
            mover = False
            continue
    if p1_turn is True:
        board_game[play_y][play_x] = "(X)"
        p1_turn = False
    else:
        board_game[play_y][play_x] = "(O)"
        p1_turn = True
    if mover is True:
        board_game[play_y_old][play_x_old] = "( )"
    validMove = False
    mover = False
    # check for win here

    gameboard()
