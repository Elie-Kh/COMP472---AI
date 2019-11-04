import random

# if the move gets the AI get closer to an X then +1
# If the move gets the AI is adding to an impossible X the  -1

# TODO - Get function that returns all possible moves for the AI
# TODO - User recursion only list of moves to get a deeper N set of moves


'''
ex -    branches = get_branches(pos, turn)
        branch_evals = [solve(branch) for branch in branches]
'''

board = [
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

# 0-9 across ; 0-7 down -> board[y][x]


# get_starting_pos finds a random starting position for the AI to place its first token
def get_starting_pos(board):
    random.seed(random.randrange(0, 100, 1))
    x = random.randrange(0, 9, 1)
    y = random.randrange(0, 7, 1)
    pos = (x, y)

    # if position is already occupied run function again until it finds a good spot
    if board[y][x] == "( )":
        return pos
    else:
        get_starting_pos(board)


position = get_starting_pos(board)
print(str(position[0]) + "-" + str(position[1]))