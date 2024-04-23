"""
Tic Tac Toe Player
"""

import math, copy

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
    # variable tmp is odd -> X moves, even -> O moves
    tmp = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                tmp += 1
    if tmp % 2 == 1:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return(actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardCopy = copy.deepcopy(board)
    if boardCopy[action[0]][action[1]] == EMPTY:
        boardCopy[action[0]][action[1]] = player(board)
        return(boardCopy)
    else:
        raise NameError(f"Action {action} is not a valid action for the board!")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Checks rows
    for i in range(3):
        if board[i] == [X, X, X]:
            return X
        if board[i] == [O, O ,O]:
            return O

    # Checks columns
    for i in range(3):
        if [board[0][i], board[1][i], board[2][i]] == [X, X, X]:
            return X
        if [board[0][i], board[1][i], board[2][i]] == [O, O, O]:
            return O

    # Checks diagonals
    if [board[0][0], board[1][1], board[2][2]] == [X, X, X]:
        return X
    if [board[0][0], board[1][1], board[2][2]] == [O, O, O]:
        return O
    if [board[0][2], board[1][1], board[2][0]] == [X, X, X]:
        return X
    if [board[0][2], board[1][1], board[2][0]] == [O, O, O]:
        return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) in (X, O):
        return True

    tmp = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                tmp += 1
    if tmp == 0:
        return True
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0

def MaxValue(board):
    if terminal(board):
        return utility(board)

    max = -100
    for action in actions(board):
        # v = max(v, MinValue(result(board, action)))
        v = MaxValue(result(board, action))
        if v > max:
            max = v
        # Alpha-Beta pruning, there is not action with v > 1, so we do not need to search anymore.
        if max == 1:
            return max
    return max

def MinValue(board):
    if terminal(board):
        return utility(board)

    min = 100
    for action in actions(board):
        # v = min(v, MaxValue(result(board, action)))
        v = MaxValue(result(board, action))
        if v < min:
            min = v
        # Alpha-Beta pruning, there is not action with v < -1, so we do not need to search anymore.
        if min == -1:
            return min
    return min

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    X (MAX player) tries to maximise the score
    O (MIN player) tries to minimise the score
    """
    # If we are trying to maximise:
    if  player(board) == X:
        optimal = (-100, -100)
        v = -100
        for action in actions(board):
            v1 = MinValue(result(board, action))
            if v1 > v:
                v = v1
                optimal = action
                # Alpha-Beta pruning, there is not action with v > 1, so we do not need to search anymore.
                if v == 1:
                    return optimal
        return optimal
    else:
        optimal = (-100, -100)
        v = 100
        for action in actions(board):
            v1 = MaxValue(result(board, action))
            if v1 < v:
                v = v1
                optimal = action
                # Alpha-Beta pruning, there is not action with v < -1, so we do not need to search anymore.
                if v == -1:
                    return optimal
        return optimal
