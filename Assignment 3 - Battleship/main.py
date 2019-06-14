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
    return randint(0, len(board_in)-1)


def random_col(board_in):
    return randint(0, len(board_in)-1)


ship_row = random_row(board)
ship_col = random_col(board)
location = [ship_row, ship_col]

print("Ship located at: ({}, {})".format(ship_row, ship_col))

print_board(board)


def guess_row():
    try:
        row = int(input("Guess row: "))
        return row
    except ValueError:
        print("You did not enter a number. Please try again.")
        guess_row()


def guess_col():
    try:
        col = int(input("Guess col: "))
        return col
    except ValueError:
        print("You did not enter a number. Please try again.")
        exit(guess_col())


row_guess = guess_row()
col_guess = guess_col()
guess = [row_guess, col_guess]

guessed = False

while not guessed:
    if guess == location:
        board[ship_row][ship_col] = "[X]"
        print_board(board)
        print("You sunk a ship!")
        guessed = True
    else:
        print("You missed! Guess again.")
        board[row_guess][col_guess] = "[M]"
        print_board(board)
        guess = [guess_row(), guess_col()]
