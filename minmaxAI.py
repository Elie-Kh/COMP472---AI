import random

# if the move gets the AI get closer to an X then +1
# If the move gets the AI is adding to an impossible X the  -1

# TODO - Get function that returns all possible moves for the AI
# TODO - User recursion only list of moves to get a deeper N set of moves
# TODO - Move the win check logic to its own file
# TODO - Find a way to implement moves in to the decision


'''
ex -    branches = get_branches(pos, turn)
        branch_evals = [solve(branch) for branch in branches]
'''

board = [
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "(X)", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "(O)", "(X)", "(O)", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "(X)", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
]
column_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
# 0-9 across ; 0-7 down -> board[y][x]


# check_adjacent looks at the adjacent cells to see if the winning pattern is present
def check_adjacent(row, column, target):
    # Checking against the middle of the X to win
    if (row+1) <= len(board)-1 and (row-1) >= 0 and (column+1) <= len(column_letters)-1 and (column-1) >= 0:
        if board[row-1][column-1] == target[0] and board[row-1][column+1] == target[0] and \
                board[row+1][column-1] == target[0] and board[row+1][column+1] == target[0]:
            return True
    return False


# check_cross checks to see if a player's win has been cancelled by the other player
def check_cross(row, column, target):
    if board[row][column-1] == target[1] and board[row][column+1] == target[1]:
        return True
    return False


# win_check loops through the game board to examine all cells with a token
def win_check(board, target):
    # Turn is inverted because the turns will have already switched by the time the win is checked
    for row in range(len(board)):
        for column in range(len(column_letters)):
            if board[row][column] == target[0] and check_adjacent(row, column, target):
                if not check_cross(row, column, target):
                    return True
    return False


# get_starting_pos finds a random starting position for the AI to place its first token
def get_starting_pos(board):
    random.seed(random.randrange(0, 100, 1))
    x = random.randrange(0, 10, 1)
    y = random.randrange(0, 8, 1)
    pos = (x, y)

    # if position is already occupied run function again until it finds a good spot
    if board[y][x] == "( )":
        return pos
    else:
        get_starting_pos(board)


# evaluate_potential looks all the AI tokens on the board and decides which token to base move decision on
def evaluate_potential(board, target):
    moves = []
    for y in range(len(board)):
        for x in range(len(column_letters)):
            if board[y][x] == target[0]:
                score = 1
                if check_cross(y, x, target):
                    score = 0
                else:
                    if board[y - 1][x - 1] == target[0]:
                        score += 1
                    if board[y - 1][x + 1] == target[0]:
                        score += 1
                    if board[y + 1][x - 1] == target[0]:
                        score += 1
                    if board[y + 1][x + 1] == target[0]:
                        score += 1
                moves.append({'position': (x, y), 'score': score})

    result = sorted(moves, key=lambda i: i['score'])
    return result[-1]


# get_ai_move evaluates the board and returns the AI's move
def get_ai_move(board, p1_turn):
    if p1_turn:
        target = ("(X)", "(O)")
    else:
        target = ("(O)", "(X)")

    move = evaluate_potential(board, target)
    x = move['position'][0]
    y = move['position'][1]

    

    return move

position = get_starting_pos(board)
print(str(position[0]) + "-" + str(position[1]))

moves = get_ai_move(board, True)
print(moves)