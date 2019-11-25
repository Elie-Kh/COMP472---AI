import random
from win_check import check_cross, win_check
from Board import move_check
column_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
# 0-9 across ; 0-7 down -> board[y][x]
global emptyBoard
emptyBoard = True
global noGood
noGood = False


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
                if 11 > x > 0 and 9 > y > 0:
                    if check_cross(y, x, target, board):
                        score = 0
                    # checks to make sure an X is still possible and not blocked by opponent
                    elif board[y - 1][x - 1] == target[1] or board[y - 1][x + 1] == target[1] or \
                            board[y + 1][x - 1] == target[1] or board[y + 1][x + 1] == target[1]:
                        score = 1
                        continue
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
                        if score == 5:
                            moves.clear()
                            moves.append({'position': (x, y), 'score': score, 'tl': tl, 'tr': tr, 'bl': bl, 'br': br})
                            return moves
                    moves.append({'position': (x, y), 'score': score, 'tl': tl, 'tr': tr, 'bl': bl, 'br': br})
            elif board[y][x] == target[1]:
                score = 1
                tl = False  # each refers to a relative position in the X (tl = top left, etc...)
                tr = False
                bl = False
                br = False
                # checks to make sure the X hasn't been cancelled by opponent
                if 11 > x > 0 and 9 > y > 0:
                    if check_cross(y, x, target, board):
                        score = 0
                    # checks to make sure an X is still possible and not blocked by opponent
                    elif board[y - 1][x - 1] == target[0] or board[y - 1][x + 1] == target[0] or \
                            board[y + 1][x - 1] == target[0] or board[y + 1][x + 1] == target[0]:
                        score = 1
                        continue
                    # score increments by 1 for each part of the X already filled in
                    else:
                        if board[y - 1][x - 1] == target[1]:
                            score += 1
                            tl = True
                        if board[y - 1][x + 1] == target[1]:
                            score += 1
                            tr = True
                        if board[y + 1][x - 1] == target[1]:
                            score += 1
                            bl = True
                        if board[y + 1][x + 1] == target[1]:
                            score += 1
                            br = True
                    moves.append({'position': (x, y), 'score': score, 'tl': tl, 'tr': tr, 'bl': bl, 'br': br})
            else:
                # if emptyBoard is False:
                score = 0
                tl = False  # each refers to a relative position in the X (tl = top left, etc...)
                tr = False
                bl = False
                br = False
                # checks to make sure the X hasn't been cancelled by opponent
                if 11 > x > 0 and 9 > y > 0:
                    if check_cross(y, x, target, board):
                        score = 0
                    # score increments by 1 for each part of the X already filled in
                    else:
                        if board[y - 1][x - 1] == target[0]:
                            score += 1
                            tl = True
                        elif board[y - 1][x - 1] == target[1]:
                            score -= 1
                            tl = False
                        if board[y - 1][x + 1] == target[0]:
                            score += 1
                            tr = True
                        elif board[y - 1][x + 1] == target[1]:
                            score -= 1
                            tl = False
                        if board[y + 1][x - 1] == target[0]:
                            score += 1
                            bl = True
                        elif board[y + 1][x - 1] == target[1]:
                            score -= 1
                            tl = False
                        if board[y + 1][x + 1] == target[0]:
                            score += 1
                            br = True
                        elif board[y + 1][x + 1] == target[1]:
                            score -= 1
                            tl = False
                    if score == 4:
                        moves.clear()
                        moves.append({'position': (x, y), 'score': score, 'tl': tl, 'tr': tr, 'bl': bl, 'br': br})
                        return moves
                    if score == -4:
                        moves.clear()
                        moves.append({'position': (x, y), 'score': score, 'tl': tl, 'tr': tr, 'bl': bl, 'br': br})
                        return moves
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
    if len(potential_locations) == 0:
        global noGood
        noGood = True
    return potential_locations


# get_ai_token evaluates the board and returns the where the AI will place its token
def get_ai_token(board, target, counter):
    potential_tokens = evaluate_potential(board, target)
    if counter == 5:
        return get_new_pos(board, target)
    if len(potential_tokens) == 1:
        chosen_locations = potential_tokens[-1]['position']
        return chosen_locations
    if potential_tokens[-1]['score'] != 0:
        chosen_locations = get_possible_token_locations(potential_tokens[-1])
        global noGood
        if noGood is True:
            noGood = False
            return get_new_pos(board, target)
        if len(chosen_locations) != 0:
            return chosen_locations[random.randrange(0, len(chosen_locations), 1)]
    if potential_tokens[-1]['score'] == 0:
        return get_new_pos(board, target)


# get_ai_move evaluates the board and returns which token to move where
def get_ai_move(board, target, counter):
    potential_moves = evaluate_potential(board, target)
    source = potential_moves[0]['position']

    if counter == 5:
        destination = get_new_pos(board, target)
        return source, destination

    if potential_moves[-1]['score'] != 0:
        chosen_locations = get_possible_token_locations(potential_moves[-1])
        # Moves the min location to the max location
        if len(chosen_locations) != 0:
            destination = chosen_locations[random.randrange(0, len(chosen_locations), 1)]

            return source, destination

    if potential_moves[-1]['score'] == 0:
        destination = get_new_pos(board, target)
        return source, destination


# returns the AI move selection back to the Game.py main file
def summon_ai_overlord(board, p1_turn, player_tokens, ai_tokens, lastAction, counter, bad_moves):
    if p1_turn:
        target = ("(X)", "(O)")
    else:
        target = ("(O)", "(X)")

    if ai_tokens == 15:
        return get_starting_pos(board)

#if tokens <= 0:
        #return get_ai_move(board, target, counter)
    #return get_ai_token(board, target, counter)
    return minimax(board, lastAction, player_tokens, ai_tokens, p1_turn, counter, bad_moves, target)

def minimax(board, lastAction, player_tokens, ai_tokens, player1turn, nply, bad_moves, target):
    if player1turn:
        target = ("(X)", "(O)")
    else:
        target = ("(O)", "(X)")
    if nply == 0 or win_check(board, player1turn) == True:
        return lastAction

    if player1turn:

        if player_tokens <= 0:
            action = get_ai_move(board, target, bad_moves)
            tokens = player_tokens

        else:
            action = get_ai_token(board, target, bad_moves)
            tokens = player_tokens - 1
        minimax(action, tokens, ai_tokens, not player1turn, (nply - 1), bad_moves, target)

    else:
        if player_tokens <= 0:
            action = get_ai_move(board, target, bad_moves)
            tokens = ai_tokens

        else:
            action = get_ai_token(board, target, bad_moves)
            tokens = ai_tokens - 1
        minimax(action, player_tokens, tokens, not player1turn, (nply - 1), bad_moves, target)
