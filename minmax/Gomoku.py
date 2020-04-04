# minmax AI
import math

#def bestMove():
    # todo


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