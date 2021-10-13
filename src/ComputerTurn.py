import numpy as np 

from DifficultGame import bestComputerSpot

def findPossibleInputs(gameBoard):
    holdArray = []

    for row in gameBoard:
        holdArray.extend(row)

    holdArray = np.unique(holdArray)
    holdArray = holdArray.tolist()
        
    if holdArray.count("X") > 0:
        holdArray.remove("X")
        
    if holdArray.count("O") > 0:
        holdArray.remove("O")

    return holdArray


def getComputerInput(gameBoard):

    # Difficult Game Choice Module
    newBoard = bestComputerSpot(gameBoard)

    possibleInputs = findPossibleInputs(newBoard)

    print ("\nComputer's Turn!")

    return newBoard, possibleInputs