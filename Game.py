from minmaxAI import summon_ai_overlord
from win_check import win_check
from Board import board_game,x_dict,column_letters,move_check


# Variables below are used in the function
# p_play variables are for getting user input
play_x = 0
play_y = 0
p_play_x = 0
p_play_y = 0
play_x_old = 0
play_y_old = 0
p1_turn = True
p1_tokens = 15
p2_tokens = 15
current_tokens = 0
moves = 0
win = False
validMove = False
mover = False
ai_mode = True


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


gameboard()
print("\n")
print('Welcome to X-Rudder!')
startingPlayer = input('Do you want to go first? Enter Y or N').upper()
while startingPlayer not in ("Y", "N"):
    startingPlayer = input('Do you want to go first? Enter Y or N').upper()

if startingPlayer == "Y":
    p1_turn = True
else:
    p1_turn = False

while moves != 30 and win is False:
    print("Moves remaining: %d" % (30 - moves))
    if p1_turn:
        player_turn = "Player 1 (X)"
        current_tokens = p1_tokens
    else:
        if not ai_mode:
            player_turn = "Player 2 (O)"
        else:
            player_turn = "AI (O)"
        current_tokens = p2_tokens

    if p1_turn or not ai_mode:
        while validMove is False:
            if p1_turn:
                p_play_x = input("%s: Enter X coordinate" % player_turn).upper()
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
                print("Choose your new position")
                play_x_old = play_x
                play_y_old = play_y
                validMove = False
                mover = True
                while validMove is False:
                    p_play_x = input("%s: Enter X coordinate" % player_turn).upper()
                    p_play_y = input("%s: Enter Y coordinate" % player_turn)
                    checker = move_check(p_play_y, p_play_x, p1_turn, mover, current_tokens)
                    validMove = checker[2]
                    if validMove is True:
                        play_x = checker[0]
                        play_y = checker[1]

            else:
                validMove = False
                mover = False
                continue

    # AI turn logic
    else:
        counter_bad = 0
        while validMove is False:
            counter_bad += 1
            move = summon_ai_overlord(board_game, p1_turn, current_tokens,counter_bad)
            if current_tokens <= 0:
                # validMove = True
                play_y_old = move[0][1]
                play_x_old = move[0][0]
                play_y = move[1][1]
                play_x = move[1][0]
                checker = move_check(play_y, play_x, False, True, current_tokens)
                validMove = checker[2]
                if validMove is False:
                    continue
                mover = True
                moves += 1
                print("\nAI Move: (%s, %s) to (%s, %s)" % (list(x_dict.keys())[list(x_dict.values()).index(str(play_x_old))], str(play_y_old), list(x_dict.keys())[list(x_dict.values()).index(str(play_x))], str(play_y)))
            else:
                play_y = move[1]
                play_x = move[0]
                checker = move_check(play_y, play_x, False, False, current_tokens)
                validMove = checker[2]
                if validMove is False:
                    continue
                p2_tokens = current_tokens - 1
                print("\nAI Token Placed: (%s, %s)" % (list(x_dict.keys())[list(x_dict.values()).index(str(play_x))], str(play_y)))

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

    if win_check(board_game, p1_turn):
        if not p1_turn:
            print("\nThe game has been won by Player 1\n")
        else:
            if ai_mode:
                print("\nThe game has been won by the AI\n")
            else:
                print("\nThe game has been won by Player 2\n")
        win = True
    if moves == 30:
        print("\nThe game has tied\n")
print("Game Over")


