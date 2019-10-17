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
current_tokens = 0
moves = 0
win = False
validMove = False
mover = False


# printing a 10 x 12 array to set up the game board
def gameboard():
    # Creating the board
    # Labelling columns with alphabet letters
    for i in range(len(column_letters)):
        if i == 0:
            print('   ' + column_letters[i], end='')
        else:
            print('  ' + column_letters[i], end='')
    print()

    # labelling each row with numbers and printing the board
    for row in range(len(board_game)):
        for col in range(len(board_game[row])):
            if col != 0:
                print(board_game[row][col], end='')
            else:
                print(str(row) + " " + board_game[row][col], end='')
        print()
    return board_game


# check_adjacent looks at the adjacent cells to see if the winning pattern is present
def check_adjacent(row, column, target):
    # Checking against the middle of the X to win
    if (row+1) <= len(board_game)-1 and (row-1) >= 0 and (column+1) <= len(column_letters)-1 and (column-1) >= 0:
        if board_game[row-1][column-1] == target and board_game[row-1][column+1] == target and \
                board_game[row+1][column-1] == target and board_game[row+1][column+1] == target:
            return True
    return False


# check_cross checks to see if a player's win has been cancelled by the other player
def check_cross(row, column):
    if p1_turn:
        target = "(X)"
    else:
        target = "(O)"

    if board_game[row][column-1] == target and board_game[row][column+1] == target:
        return True
    return False


# win_check loops through the game board to examine all cells with a token
def win_check():
    # Turn is inverted because the turns will have already switched by the time the win is checked
    if not p1_turn:
        target = "(X)"
    else:
        target = "(O)"

    for row in range(len(board_game)):
        for column in range(len(column_letters)):
            if board_game[row][column] == target and check_adjacent(row, column, target):
                if not check_cross(row, column):
                    return True
    return False


def move_check(y, x, turn, moving, token_num):

    try:
        play_y_f = int(y)
        try:
            play_x_f = int(x)
        except ValueError:
            if x in x_dict:
                play_x_f = int(x_dict[x])
            else:
                print("Invalid input")
                move_validity = [0, 0, False, False, token_num]
                return move_validity
    except ValueError:
        print("Invalid input")
        move_validity = [0, 0, False, False, token_num]
        return move_validity
    if play_x_f <= 11 and play_y_f <= 9:
        if board_game[play_y_f][play_x_f] != "( )":
            if turn is True and moving is False:
                if board_game[play_y_f][play_x_f] == "(O)":
                    print('Invalid Move')
                    move_validity = [0, 0, False, False, token_num]
                    return move_validity
                else:
                    # print('Are you sure you want to move your token')
                    validmove_f = True
                    move_validity = [play_x_f, play_y_f, validmove_f, True, token_num]
                    return move_validity
            elif moving is False:
                if board_game[play_y_f][play_x_f] == "(X)":
                    print('Invalid Move')
                    move_validity = [0, 0, False, False, token_num]
                    return move_validity
                else:
                    validmove_f = True
                    move_validity = [play_x_f, play_y_f, validmove_f, True, token_num]
                    return move_validity
        else:
            if token_num == 0 and moving is False:
                print("You are out of tokens. Please move tokens already on the board")
                move_validity = [0, 0, False, False, token_num]
                return move_validity
            else:
                token_num -= 1
            validmove_f = True
            move_validity = [play_x_f, play_y_f, validmove_f, False, token_num]
            return move_validity

    else:
        print('Invalid Move')
        move_validity = [0, 0, False, False, token_num]
        return move_validity
    print('Invalid Move')
    move_validity = [0, 0, False, False, token_num]
    return move_validity


while moves != 30 and win is False:
    print("Moves remaining: %d" % (30 - moves))
    if p1_turn:
        player_turn = "Player 1 (X)"
        current_tokens = p1_tokens
    else:
        player_turn = "Player 2 (O)"
        current_tokens = p2_tokens

    while validMove is False:

        p_play_x = input("%s: Enter X coordinate" % player_turn)
        p_play_y = input("%s: Enter Y coordinate" % player_turn)
        checker = move_check(p_play_y, p_play_x, p1_turn, False, current_tokens)
        validMove = checker[2]
        mover = checker[3]
        if p1_turn:
            p1_tokens = checker[4]
        else:
            p2_tokens = checker[4]
        if validMove is True:
            play_x = checker[0]
            play_y = checker[1]
    if mover is True:
        confirm = input('Are you sure you want to move your token? Enter Y or N').upper()
        while confirm not in ("Y", "N"):
            confirm = input('Are you sure you want to move your token? Enter Y or N').upper()

        if confirm == "Y":
            moves += 1
            print("choose your new position")
            play_x_old = play_x
            play_y_old = play_y
            validMove = False
            mover = True
            while validMove is False:
                p_play_x = input("%s: Enter X coordinate" % player_turn)
                p_play_y = input("%s: Enter X coordinate" % player_turn)
                checker = move_check(p_play_y, p_play_x, p1_turn, mover, current_tokens)
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

    print("\n")
    gameboard()
    print("\n")

    if win_check():
        if not p1_turn:
            print("\nThe game has been won by Player 1\n")
        else:
            print("\nThe game has been won by Player 2\n")
        win = True
    if moves == 30:
        print("\nThe game has tied\n")
print("Game Over")