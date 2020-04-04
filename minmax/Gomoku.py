# minmax AI
import math
from sys import maxsize
import numpy as np

ai = 'X'
human = 'O'
currentPlayer = human
board = np.chararray((15, 15))
board[:] = ''

def bestMove():
    # AI turn
    bestScore = -maxsize
    for i in range(15):
        for j in range(15):
            if board[i][j] == '':
                board[i][j] = ai
                score = minmax(board, 0, False)
                board[i][j] = ''
                if score > bestScore:
                    bestScore = score
                    move = (i, j)

    board[move[0]][move[1]] = ai
    currentPlayer = human


def minmax(board, depth, isMax):
    result = CheckWinner()
    if result == 1:
        return "Player won!"
    elif result == -1:
        return "Computer won"
    elif result == 0:
        return "Tie"

    if isMax:
        bestScore = -math.inf
        for i in range(16):
            for j in range(16):
                if board[i][j] == 0:
                    board[i][j] = -2
                    score = minmax(board, depth + 1, False)
                    board[i][j] = 0
                    bestScore = max(score, bestScore)

        return bestScore
    else:
        bestScore = math.inf
        for i in range(16):
            for j in range(16):
                if board[i][j] == 0:
                    board[i][j] = 2
                    score = minmax(board, depth + 1, True)
                    board[i][j] = 0
                    bestScore = min(score, bestScore)
        return bestScore