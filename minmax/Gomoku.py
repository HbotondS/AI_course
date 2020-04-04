# minmax AI
import math
import numpy as np

ai = -2
human = 2
board = np.zeros((15, 15), dtype=int)


def winnerCheck():
    winner = 0

    #Horizontal check
    for i in range(15):
        for j in range(15):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4]:
                winner = board[i][j]
                return winner

    #vertical check
    for i in range(15):
        for j in range(15):
            if board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] == board[j+4][i]:
                winner = board[j][i]
                return winner

    #diagonal check
    for i in range(11):
        checkdiagonal = board.diagonal(i)
        for j in range(len(checkdiagonal)):
            if checkdiagonal[j] == checkdiagonal[j+1] == checkdiagonal[j+2] == checkdiagonal[j+3] == checkdiagonal[j+4]:
                winner = checkdiagonal[j]
                return winner

    for i in range(11):
        checkdiagonal = board.diagonal(-i)
        for j in range(len(checkdiagonal)):
            if checkdiagonal[j] == checkdiagonal[j+1] == checkdiagonal[j+2] == checkdiagonal[j+3] == checkdiagonal[j+4]:
                winner = checkdiagonal[j]
                return winner

    emptyPlace = 0
    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                emptyPlace += 1

    if emptyPlace == 0:
        return 0


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
    if result == 2:
        return "Player won!"
    elif result == -2:
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
