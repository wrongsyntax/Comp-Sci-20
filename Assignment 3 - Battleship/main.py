from random import randint

board = []

for i in range(7):
    board.append(["O", "O", "O", "O", "O", "O", "O", ])


def print_board(board_in):
    for row in range(len(board_in)):
        print(" ".join(board_in[row]))


def random_row(board_in):
  return randint(0, len(board_in)-1)


def random_col(board_in):
  return randint(0, len(board_in)-1)


ship_row = random_row(board)
ship_col = random_col(board)


print_board(board)
