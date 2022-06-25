from tictactoe import initial_state, X, O, check_vertical, check_diagonal

board = initial_state()

# board = [
#     [None, None, O],
#     [None, None, O],
#     [None, None, O]
# ]

# board = [
#     [None, None, None, X, None],
#     [None, None, None, X, None],
#     [None, None, None, X, None],
#     [None, None, None, X, None],
#     [None, None, None, X, None]
# ]

# board = [
#     [None, None, None, None, X],
#     [None, None, None, X, None],
#     [None, None, X, None, None],
#     [None, X, None, None, None],
#     [X, None, None, None, None]
# ]

board = [
    [O, None, None, None, None],
    [None, O, None, None, None],
    [None, None, O, None, None],
    [None, None, None, O, None],
    [None, None, None, None, O]
]

# print(check_vertical(board))
print(check_diagonal(board))

# print(board)