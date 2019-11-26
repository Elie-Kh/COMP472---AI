import random

from win_check import check_cross, win_check

# get_starting_pos finds a random starting position for the AI to place its first token
def get_starting_pos(board):
    global emptyBoard
    emptyBoard = False
    random.seed(random.randrange(0, 100, 1))
    x = random.randrange(1, 10, 1)
    y = random.randrange(1, 8, 1)
    pos = (x, y)

    # if position is already occupied run function again until it finds a good spot
    if board[y][x] == "( )":
        return pos
    else:
        get_starting_pos(board)


# get_new_pos finds a new spot for the Ai to place a token (when all potential X's are blocked)
def get_new_pos(board, target):
    global emptyBoard
    emptyBoard = False
    random.seed(random.randrange(0, 100, 1))
    x = random.randrange(1, 10, 1)
    y = random.randrange(1, 8, 1)
    pos = (x, y)

    # make sure the position is valid
    if board[y][x] != "( )":
        get_new_pos(board, target)
    elif board[y][x-1] and board[y][x+1] == target[1]:
        get_new_pos(board, target)

    return pos


def minmax(board, turn, nply):
