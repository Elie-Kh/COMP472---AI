import random
from win_check import check_cross

# TODO - Move the win check logic to its own file

board = [
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "(O)", "(X)", "(O)", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
    ["( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )", "( )"],
]
column_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
# 0-9 across ; 0-7 down -> board[y][x]


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


# get_new_pos finds a new spot for the Ai to place a token (when all potential X's are blocked)
def get_new_pos(board, target):
    random.seed(random.randrange(0, 100, 1))
    x = random.randrange(0, 10, 1)
    y = random.randrange(0, 8, 1)
    pos = (x, y)

    # make sure the position is valid
    if board[y][x] != "( )":
        get_new_pos(board, target)
    elif board[y][x-1] and board[y][x+1] == target[1]:
        get_new_pos(board, target)

    return pos


# evaluate_potential looks all the AI tokens on the board and decides which token to base move decision on
def evaluate_potential(board, target):
    moves = []
    for y in range(len(board)):
        for x in range(len(column_letters)):
            if board[y][x] == target[0]:
                score = 1
                tl = False    # each refers to a relative position in the X (tl = top left, etc...)
                tr = False
                bl = False
                br = False
                # checks to make sure the X hasn't been cancelled by opponent
                if check_cross(y, x, target, board):
                    score = 0
                # checks to make sure an X is still possible and not blocked by opponent
                elif board[y - 1][x - 1] == target[1] or board[y - 1][x + 1] == target[1] or \
                        board[y + 1][x - 1] == target[1] or board[y + 1][x + 1] == target[1]:
                    score = 0
                # score increments by 1 for each part of the X already filled in
                else:
                    if board[y - 1][x - 1] == target[0]:
                        score += 1
                        tl = True
                    if board[y - 1][x + 1] == target[0]:
                        score += 1
                        tr = True
                    if board[y + 1][x - 1] == target[0]:
                        score += 1
                        bl = True
                    if board[y + 1][x + 1] == target[0]:
                        score += 1
                        br = True
                moves.append({'position': (x, y), 'score': score, 'tl': tl, 'tr': tr, 'bl': bl, 'br': br})

    result = sorted(moves, key=lambda i: i['score'])
    return result


# get_possible_token_locations returns a list of possible location for the next token placement/move
def get_possible_token_locations(potential):
    potential_locations = []
    for spot in ['tl', 'tr', 'bl', 'br']:
        if not potential[spot]:
            if spot == 'tl':
                potential_locations.append((potential['position'][0] - 1, potential['position'][1] - 1))
            if spot == 'tr':
                potential_locations.append((potential['position'][0] + 1, potential['position'][1] - 1))
            if spot == 'bl':
                potential_locations.append((potential['position'][0] - 1, potential['position'][1] + 1))
            if spot == 'br':
                potential_locations.append((potential['position'][0] + 1, potential['position'][1] + 1))

    return potential_locations


# get_ai_token evaluates the board and returns the where the AI will place its token
def get_ai_token(board, target):
    potential_tokens = evaluate_potential(board, target)
    if potential_tokens[-1]['score'] != 0:
        chosen_locations = get_possible_token_locations(potential_tokens[-1])
        return chosen_locations[random.randrange(0, len(chosen_locations), 1)]
    if potential_tokens[-1]['score'] == 0:
        return get_new_pos(board, target)


# get_ai_move evaluates the board and returns which token to move where
def get_ai_move(board, target):
    potential_moves = evaluate_potential(board, target)
    source = potential_moves[0]['position']

    if potential_moves[-1]['score'] != 0:
        chosen_locations = get_possible_token_locations(potential_moves[-1])
        # Moves the min location to the max location
        destination = chosen_locations[random.randrange(0, len(chosen_locations), 1)]
        return source, destination

    if potential_moves[-1]['score'] == 0:
        destination = get_new_pos(board, target)
        return source, destination


# returns the AI move selection back to the Game.py main file
def summon_ai_overlord(board, p1_turn, tokens):
    if p1_turn:
        target = ("(X)", "(O)")
    else:
        target = ("(O)", "(X)")

    if tokens == 15:
        return get_starting_pos(board)
    if tokens <= 0:
        return get_ai_move(board, target)
    return get_ai_token(board, target)


move = summon_ai_overlord(board, True, 0)
print(move)
