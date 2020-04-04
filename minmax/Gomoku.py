# minmax AI
import math
import numpy as np

ai = -2
human = 2
board = np.zeros((15, 15), dtype=int)

def bestMove():
    # AI turn
    bestScore = -math.inf
    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                board[i][j] = ai
                score = minmax(board, 0, False)
                board[i][j] = 0
                if score > bestScore:
                    bestScore = score
                    move = (i, j)

    board[move[0]][move[1]] = ai


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
        for i in range(15):
            for j in range(15):
                if board[i][j] == 0:
                    board[i][j] = ai
                    score = minmax(board, depth + 1, False)
                    board[i][j] = 0
                    bestScore = max(score, bestScore)

        return bestScore
    else:
        bestScore = math.inf
        for i in range(15):
            for j in range(15):
                if board[i][j] == 0:
                    board[i][j] = human
                    score = minmax(board, depth + 1, True)
                    board[i][j] = 0
                    bestScore = min(score, bestScore)
        return bestScore