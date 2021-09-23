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
        print(spaceTypes)

    return False


# Checks columns 

# Checks diagnols 