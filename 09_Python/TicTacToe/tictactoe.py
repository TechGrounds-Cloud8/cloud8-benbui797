"""
Tic Tac Toe Player
"""

import copy
import math
import random

X = "X"
O = "O"
EMPTY = None

scale = 3

def depth_limit(actions):
    """
    Increase depth limit based on the amount of actions available vs the size of the board.
    """
    action_pool = len(actions)

    action_ratio = action_pool / 9

    # Return depth-limit in steps based on ratio vs 9 actions (AI is quick at that level and can go unlimited depth)
    if action_ratio == 1:
        return math.inf
    elif action_ratio <= 2:
        return 5
    elif action_ratio <= 3:
        return 4
    elif action_ratio <= 3.5:
        return 3
    else:
        return 2


def initial_state():
    """
    Returns starting state of the board.
    """
    board = []

    for r in range(scale):
        row = []
        for c in range(scale):
            row.append(EMPTY)
        board.append(row)
    
    return board


def player(board):
    """
    Returns player who has the next turn on a board.

    Count amount of X's and O's to determine who's turn it is.

    Return X in case of draw.
    """

    x = 0
    o = 0

    for row in board:
        for cell in row:
            if cell == X:
                x += 1
            elif cell == O:
                o += 1

    if o < x:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.

    Loop through board and store EMPTY cells as tuple where i = row and j = column.
    """
    actions = set()

    for i in range(scale):
        for j in range(scale):
            if board[i][j] == EMPTY:
                actions.add(tuple([i, j]))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.

    If cell is not empty, else raise error
    Else return deepcopy of board with the action applied to it
    """

    i, j = action
    
    if board[i][j] is not EMPTY:
        raise Exception("Invalid Action")
        
    new_board = copy.deepcopy(board)
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_horizontal(board) is not None:
        return check_horizontal(board)
    elif check_vertical(board) is not None:
        return check_vertical(board)
    elif check_diagonal(board) is not None:
        return check_diagonal(board)
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.

    Return True if there is a winner
    Else check if no EMPTY cells on board.
    """

    if winner(board) or not actions(board):
        return True
    else:
        return False
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def alpha_beta_pruning(board, depth, alpha, beta, max_player):
    """
    Minimax function with Alpha-Beta pruning and depth limit to optimize the AI.
    """

    if depth == 0 or terminal(board):
        return utility(board)
    
    if max_player == True:
        v = -math.inf

        for action in actions(board):
            v = max(v, alpha_beta_pruning(result(board, action), depth - 1, alpha, beta, False))

            if v >= beta:
                break

            alpha = max(alpha, v)

        return v

    else: 
        v = math.inf

        for action in actions(board):
            v = min(v, alpha_beta_pruning(result(board, action), depth - 1, alpha, beta, True))

            if v <= alpha:
                break

            beta = min(beta, v)

        return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    X wins if Utility returns 1, optimum move for X is worst move for O.
    (blocking O is most important, perfect games always end up as a tie)

    If the AI starts as X, often it would place first move on an edge (0,1), which is not optimal...
    So I import random and let the AI pick either center or corner randomly.
    
    This also speeds up the first move a lot!
    """  
    move = None

    # check if board is empty (first move)
    if board == initial_state():
        return first_move()

    if terminal(board):
        return None

    # if player = X -> Optimum = 1 -> Pick highest minimum v
    if player(board) == X:    
        v = -math.inf

        for action in actions(board):
            action_v = alpha_beta_pruning(
                result(board, action),
                depth_limit(actions(board)),
                -math.inf,
                math.inf,
                False
            )

            if action_v > v:
                v = action_v
                move = action

    # else player = O -> optimum = -1 -> max_v as small as possible
    else:
        v = math.inf

        for action in actions(board):
            action_v = alpha_beta_pruning(
                result(board, action),
                depth_limit(actions(board)),
                -math.inf,
                math.inf,
                True
            )

            if action_v < v:
                v = action_v
                move = action
    
    return move

def first_move():
    """
    Generate first moves, make random choice from set.

    1. Add all corners
    2. If scale is odd, add middle
    """
    endpoint = scale - 1

    moves = [
        (0,0),
        (0, endpoint),
        (endpoint, 0),
        (endpoint, endpoint)
    ]
    
    if scale % 2 != 0:
        mid = scale // 2
        moves.append((mid, mid))

    return random.choice(moves)
 

def check_horizontal(board):
    """
    Check horizontal axis for scale in a row.
    """

    for i in range(scale):
        if board[i].count(X) == scale:
            return X
        elif board[i].count(O) == scale:
            return O

    return None        


def check_vertical(board):
    """
    Check vertical axis for scale in a row.
    """

    for i in range(scale):
        buffer = []

        for j in range(scale):
            if board[j][i] is not EMPTY:
                buffer.append(board[j][i])
        
        if buffer.count(X) == scale:
            return X
        if buffer.count(O) == scale:
            return O        

    return None


def check_diagonal(board):
    """
    Check diagonal axis for scale in a row.
    """

    buffer1 = []
    buffer2 = []

    for i in range(scale):
        buffer1.append(board[i][i])
        buffer2.append(board[i][scale - 1 - i])
    
    if buffer1.count(X) == scale or buffer2.count(X) == scale:
        return X
    elif buffer1.count(O) == scale or buffer2.count(O) == scale:
        return O
    else:
        return None
