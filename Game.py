# printing a 10 x 12 array to set up the game board
def GameBoard():

    # Creating the board
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
    return


GameBoard()
