from WinningCombo import checkForWin
from copy import deepcopy

def bestComputerSpot (gameBoard):
    computerPicks = [checkForGameEnder(deepcopy(gameBoard), "O"),
                    checkForGameEnder(deepcopy(gameBoard), "X"),
                    checkForSpotFive(deepcopy(gameBoard)),
                    eliminateWinningCombo(deepcopy(gameBoard)),
                    takeFirstAvailableSpot(deepcopy(gameBoard))]

    for pick in computerPicks:
        if pick:
            return pick

def checkForSpotFive(gameBoard):
    if gameBoard[1][1] != "X" and gameBoard[1][1] !="O":
        gameBoard[1][1] = "O"
        return gameBoard

def checkForGameEnder(gameboard, XorO):
    for row in range(len(gameboard)):
        for column in range(len(gameboard[row])):
            item = gameboard[row][column]
            if item != "X" and item != "O":
                gameboard[row][column] = XorO
                win = checkForWin(gameboard)

                if win == True:
                    gameboard[row][column] = "O"
                    return gameboard
                
                gameboard[row][column] = item

def eliminateWinningCombo(gameboard):
    itemArray = [gameboard[1][1], gameboard[2][2], gameboard[0][2]]
    spotArray = []

    for item in itemArray:
        if item == "X" or item == "O":
            spotArray.append(True)
        else:
            spotArray.append(False)

    if spotArray == [True, True, False]:
        gameboard[0][2] = "O"
        return gameboard


def takeFirstAvailableSpot(gameboard):
    for row in range(len(gameboard)):
        for column in range(len(gameboard[row])):
            if gameboard[row][column] != "X" and gameboard[row][column] != "O":
                gameboard[row][column] = "O"
                return gameboard