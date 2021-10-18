import sys 
import numpy as np

from ComputerTurn import getComputerInput
from UserTurn import getUserMove
from WinningCombo import checkForWin

def takeTurns(board, possibleInputs):

    while checkForWin(board) == False and checkForCatsGame(possibleInputs) ==False:
        board, possibleInputs = oneTurn(board, possibleInputs)

    if checkForWin(board) == True:
        printBoard(board)
        print("Game Over!")

    if checkForCatsGame(possibleInputs) == True:
        printBoard(board)
        print ("Cats Game!")

def checkForCatsGame(inputArray):
    if len(inputArray) == 0:
        return True

    else:
        return False

def oneTurn(gameBoard, inputArray):
    printBoard(gameBoard)
    
    gameBoard, inputArray = getUserMove(gameBoard, inputArray)

    if checkForCatsGame(inputArray) == True:
        return gameBoard, inputArray

    if checkForWin(gameBoard) == True:
        return gameBoard, inputArray

    gameBoard, inputArray = getComputerInput(gameBoard)

    return gameBoard, inputArray

def printBoard(gameBoard):
    print("\n %s | %s | %s \n---+---+---\n %s | %s | %s \n---+---+---\n %s | %s | %s \n" % \
    (gameBoard[0][0], gameBoard[0][1], gameBoard[0][2],
    gameBoard[1][0], gameBoard[1][1], gameBoard[1][2],
    gameBoard[2][0], gameBoard[2][1], gameBoard[2][2]))