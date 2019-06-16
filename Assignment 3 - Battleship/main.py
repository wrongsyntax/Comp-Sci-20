from random import randint
from time import sleep

print("""
Welcome to Battleship!
You will be asked to enter a row and a column to try and sink the ships.
O represents a space you haven't shot at yet.
M means you missed at that space.
X is a hit.
Good luck!
""")

sleep(5)

board = [["    1", "  2", "  3", "  4", "  5", "  6", "  7"]]
row_num = 1

for i in range(7):
    board.append([str(row_num), "[O]", "[O]", "[O]", "[O]", "[O]", "[O]", "[O]", ])
    row_num += 1


def print_board(board_in):
    for row in range(len(board_in)):
        print("  ".join(board_in[row]))


def random_row(board_in):
    return randint(1, len(board_in)-1)


def random_col(board_in):
    return randint(1, len(board_in)-1)


ship_row1 = random_row(board)
ship_col1 = random_col(board)
location1 = [ship_row1, ship_col1]

ship_row2 = random_row(board)
ship_col2 = random_col(board)
location2 = [ship_row2, ship_col2]

ship_row3 = random_row(board)
ship_col3 = random_col(board)
location3 = [ship_row3, ship_col3]

print_board(board)


def guess_row():
    try:
        row = int(input("Guess row: "))
        while row < 1 or row > 7:
            print("Enter a value between 1 and 7.")
            row = int(input("Guess row: "))
        else:
            return row
    except ValueError:
        print("You did not enter a number. Please try again.")
        guess_row()


def guess_col():
    try:
        col = int(input("Guess col: "))
        while col < 1 or col > 7:
            print("Enter a value between 1 and 7.")
            col = int(input("Guess row: "))
        else:
            return col
    except ValueError:
        print("You did not enter a number. Please try again.")
        guess_col()


col_guess = guess_col()
row_guess = guess_row()
guess = [row_guess, col_guess]

guessed = 0
already_guessed1 = False
already_guessed2 = False
already_guessed3 = False

while guessed != 3:
    if guess == location1 and already_guessed1 is False:
        board[ship_row1][ship_col1] = "[X]"
        print_board(board)
        print("You sunk a ship!")
        guessed += 1
        already_guessed1 = True
        col_guess = guess_col()
        row_guess = guess_row()
        guess = [row_guess, col_guess]
    elif guess == location2 and already_guessed2 is False:
        board[ship_row2][ship_col2] = "[X]"
        print_board(board)
        print("You sunk a ship!")
        guessed += 1
        already_guessed2 = True
        col_guess = guess_col()
        row_guess = guess_row()
        guess = [row_guess, col_guess]
    elif guess == location3 and already_guessed3 is False:
        board[ship_row3][ship_col3] = "[X]"
        print_board(board)
        print("You sunk a ship!")
        guessed += 1
        already_guessed3 = True
        col_guess = guess_col()
        row_guess = guess_row()
        guess = [row_guess, col_guess]
    else:
        print("You missed! Guess again.")
        board[row_guess][col_guess] = "[M]"
        print_board(board)
        col_guess = guess_col()
        row_guess = guess_row()
        guess = [row_guess, col_guess]

print("You sunk all the ships!")
