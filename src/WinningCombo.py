import numpy as np
# Checks to see if a winning combo has set

# Checks rows 
def checkWinningRows(gameBoard):
    size = np.shape(gameBoard)

    if size != (3,3):
        return "Please enter a 3 by 3 matrix"

    for row in gameBoard:
        spaceTypes = len(np.unique(row))
        if spaceTypes == 1:
            return True

    return False


# Checks columns 
def checkWinningColumns(gameBoard):
    size = np.shape(gameBoard)

    if size != (3,3):
        return "Please enter a 3 by 3 matrix"
    
    shapedGame = np.array(gameBoard)
    columnLists = np.array([[None] * size[1]] * size[0])

    for i in range(len(shapedGame[0])):
        for x in range(len(shapedGame[1])):
            columnLists[x][i] = shapedGame[i][x]

    for row in columnLists:
        spaceTypes = len(np.unique(row))
        if spaceTypes == 1:
            return True

    return False

# Check Diagonals