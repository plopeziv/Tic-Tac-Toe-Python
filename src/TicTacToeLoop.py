import sys
from OneTurn import *
from WinningCombo import checkForWin

def takeTurns(board, possibleInputs):

    print("Welcome to Tic Tac Toe!")

    while checkForWin(board) == False:
        board, possibleInputs = oneTurn(board, possibleInputs)

    if checkForWin(board) == True:
        print("Game Over!")
        print(printBoard(board))

        sys.exit()

