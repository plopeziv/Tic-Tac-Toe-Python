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
    userInput = input("Please select a square! \n")

    inputCheck = inputChecker(userInput, possibleInputArray)

    while inputCheck == False:
        userInput = input("Input not found. Please select a valid space. \n")

    
    return userInput

def getUserMove(gameBoard, inputArray):
    userInput = getUserInput()

    userIndex = findIndex(str(userInput), gameBoard)
    gameBoard[userIndex[0]][userIndex[1]] = "X"

    inputArray.remove(str(userInput))

    return gameBoard, inputArray 