# minmax AI
import math
import numpy as np
import random
import sys

ai = -2
human = 2
board = np.zeros((15, 15), dtype=int)
maxDepth = 5


def winnerCheck():
    winner = 0

    #Horizontal check
    for i in range(15):
        for j in range(11):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4] != 0:
                winner = board[i][j]
                return winner

    #vertical check
    for i in range(15):
        for j in range(11):
            if board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] == board[j+4][i] != 0:
                winner = board[j][i]
                return winner

    #diagonal check
    for i in range(11):
        checkdiagonal = board.diagonal(i)
        for j in range(len(checkdiagonal)-4):
            if checkdiagonal[j] == checkdiagonal[j+1] == checkdiagonal[j+2] == checkdiagonal[j+3] == checkdiagonal[j+4] != 0:
                winner = checkdiagonal[j]
                return winner

    for i in range(11):
        checkdiagonal = board.diagonal(-i)
        for j in range(len(checkdiagonal)-4):
            if checkdiagonal[j] == checkdiagonal[j+1] == checkdiagonal[j+2] == checkdiagonal[j+3] == checkdiagonal[j+4] != 0:
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
    print('The AI move: {}'.format(move))


def minmax(board, depth, isMax):
    result = winnerCheck()
    if result == human:
        return human
    elif result == ai:
        return ai
    elif result == 0:
        return 0

    if depth == maxDepth:
        return random.choice([ai, human])

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


def printBoard():
    for i in range(15):
        print(board[i])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        maxDepth = sys.argv[1]

    printBoard()
    bestMove()
    printBoard()
    while True:
        score = winnerCheck()
        if score != None:
            print('tie')
            break

        print("Your next move: ")
        row = input("row: ")
        column = input("column: ")
        board[row][column] = human
