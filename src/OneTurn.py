import sys 
import numpy as np

from ComputerTurn import getComputerInput
from UserTurn import getUserMove

#  Game runner Responsibilities
def checkForCatsGame(inputArray):
    if len(inputArray) == 0:
        print("\nCat's Game!\n")
        sys.exit()

def printBoard(gameBoard):
    print("\n %s | %s | %s \n---+---+---\n %s | %s | %s \n---+---+---\n %s | %s | %s \n" % \
    (gameBoard[0][0], gameBoard[0][1], gameBoard[0][2],
    gameBoard[1][0], gameBoard[1][1], gameBoard[1][2],
    gameBoard[2][0], gameBoard[2][1], gameBoard[2][2]))

def oneTurn(gameBoard, inputArray):
    checkForCatsGame(inputArray)

    printBoard(gameBoard)
    gameBoard, inputArray = getUserMove(gameBoard, inputArray)

    checkForCatsGame(inputArray)

    gameBoard, inputArray = getComputerInput(gameBoard)

    return gameBoard, inputArray

