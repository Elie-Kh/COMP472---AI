
column_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]


# check_adjacent looks at the adjacent cells to see if the winning pattern is present
def check_adjacent(row, column, target, board_game):
    # Checking against the middle of the X to win
    if (row+1) <= len(board_game)-1 and (row-1) >= 0 and (column+1) <= len(column_letters)-1 and (column-1) >= 0:
        if board_game[row-1][column-1] == target[0] and board_game[row-1][column+1] == target[0] and \
                board_game[row+1][column-1] == target[0] and board_game[row+1][column+1] == target[0]:
            return True
    return False


# check_cross checks to see if a player's win has been cancelled by the other player
def check_cross(row, column, target, board_game):
    if board_game[row][column-1] == target[1] and board_game[row][column+1] == target[1]:
        return True
    return False


# win_check loops through the game board to examine all cells with a token
def win_check(board_game, p1_turn):
    # Turn is inverted because the turns will have already switched by the time the win is checked
    if not p1_turn:
        target = ("(X)", "(O)")
    else:
        target = ("(O)", "(X)")

    for row in range(len(board_game)):
        for column in range(len(column_letters)):
            if board_game[row][column] == target[0] and check_adjacent(row, column, target, board_game):
                if not check_cross(row, column, target, board_game):
                    return True
    return False
