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
    numX = 0
    numO = 0

    for row in board:
        numX += row.count(X)
        numO += row.count(O)

    #Next player will be the one with least moves done
    if (numX > numO):
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    #Init empty set
    possible_actions = set()

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    #Check if move is valid
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception('Not a valid move! Please try again!')

    #If it is valid, make a copy and execute move
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if isRow(board, X) or isCol(board, X) or isDiag(board, X):
        return X
    elif isRow(board, O) or isCol(board, O) or isDiag(board, O):
        return O
    else: 
        return None
    
def isRow(board, player):
    for row in range(3):
        player_count = 0
        for col in range(3):
            if board[row][col] == player:
                player_count += 1
        if player_count == 3:
            return True
    return False

def isCol(board, player):
    for col in range(3):
        player_count = 0
        for row in range(3):
            if board[row][col] == player:
                player_count += 1
        if player_count == 3:
            return True
    return False

def isDiag(board, player):
    diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    for diagonal in diagonals:
        if all(board[row][col] == player for (row, col) in diagonal):
            return True
    return False



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) != None:
        return True

    #Check if moves are still possible
    for row in board:
        if EMPTY in row:
            return False
    
    #No possible moves, stalemate
    return True


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    #X trying to maximize, O trying to minimize

    if terminal(board):
        return None

    if player(board) == X:
        max_v = float('-inf')
        for action in actions(board):
            v = min_value(result(board, action))
            if (v > max_v):
                max_v = v
                optimal_action = action
    
    elif player(board) == O:
        min_v = float('inf')
        for action in actions(board):
            v = max_value(result(board, action))
            if (v < min_v):
                min_v = v
                optimal_action = action
    
    return optimal_action
    
def max_value(board):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v