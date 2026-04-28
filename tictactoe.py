"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = 0
    num_o = 0

    for i in board:
        for j in i:
            if j == X:
                num_x += 1
            elif j == O:
                num_o += 1


    initial_board = initial_state()

    if board == initial_board:
        return X
    elif terminal(board) == True:
        return O
    elif num_x > num_o:
        return O
    elif num_o > num_x:
        return X
    elif num_x == num_o:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    count_i = 0
    count_j = 0

    for i in board:
        for j in range(len(i)):
            if count_j == 3:
                count_j = 0

            if i[j] == EMPTY or i[j] == None:
                actions.add((count_i, count_j))
            count_j += 1
        count_i += 1

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)

    turn = player(board)

    if type(action) != tuple:
        raise Exception("Invalid Action value")
    elif len(action) != 2:
        raise Exception("Invalid Action value")

    i, j = action

    if i not in [0,1,2] or j not in [0,1,2]:
        raise Exception("Invalid Action value")
    elif board_copy[i][j] != EMPTY:
        raise Exception("Invalid Action value")


    board_copy[i][j] = turn

    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in [X, O]:
        if board[0][0] == i and board[0][1] == i and board[0][2] == i:
            return i
        elif board[1][0] == i and board[1][1] == i and board[1][2] == i:
            return i
        elif board[2][0] == i and board[2][1] == i and board[2][2] == i:
            return i
        elif board[0][0] == i and board[1][0] == i and board[2][0] == i:
            return i
        elif board[0][1] == i and board[1][1] == i and board[2][1] == i:
            return i
        elif board[0][2] == i and board[1][2] == i and board[2][2] == i:
            return i
        elif board[0][0] == i and board[1][1] == i and board[2][2] == i:
            return i
        elif board[0][2] == i and board[1][1] == i and board[2][0] == i:
            return i

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board) == True:
        return None

    c_player = player(board)

    aval_moves = actions(board)

    if c_player == "X":
        best_score = -math.inf
        best_move = None

        for move in aval_moves:
            resultant = result(board, move)
            score = min_value(resultant)

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    if c_player == "O":
        best_score = math.inf
        best_move = None

        for move in aval_moves:
            resultant = result(board, move)
            score = max_value(resultant)

            if score < best_score:
                best_score = score
                best_move = move

        return best_move


def min_value(board):
    if terminal(board) == True:
        return utility(board)

    v = math.inf

    for move in actions(board):

        v = min(v, max_value(result(board, move)))

    return v

def max_value(board):
    if terminal(board) == True:
        return utility(board)

    v = -math.inf

    for move in actions(board):

        v = max(v, min_value(result(board, move)))

    return v
