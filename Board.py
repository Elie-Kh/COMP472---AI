from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Nora game")

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
x_dict = dict(A='0', B='1', C='2', D='3', E='4', F='5', G='6', H='7', I='8', J='9', K='10', L='11')


def disable_button():
    button.configure(state=DISABLED)


for r in range(10):
    for c in range(12):
        button = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=2, width=6)
        button.grid(row=r, column=c)

tk.mainloop()


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