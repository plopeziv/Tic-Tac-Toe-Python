def findIndex(element, matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == element:
                return (row, column)

def inputChecker(input, possibleInputs):
    returnValue = False

    if (input in possibleInputs):
        returnValue = True

    return returnValue

def getUserInput(possibleInputArray):
    userInput = str(input("Please select a square! \n"))

    while inputChecker(userInput, possibleInputArray) == False:
        userInput = str(input("Input not found. Please select a valid space. \n"))


    return userInput

def getUserMove(gameBoard, inputArray):
    userInput = getUserInput(inputArray)

    userIndex = findIndex(str(userInput), gameBoard)
    gameBoard[userIndex[0]][userIndex[1]] = "X"

    inputArray.remove(str(userInput))

    return gameBoard, inputArray 