import sys
sys.path
sys.path.append("/src/")

from UserTurn import * 
from unittest import mock

def test_findIndex():

    matrix = [["B","C"],
            ["1", "A"],
            ["D", 2]]

    index = findIndex("A", matrix)

    assert index == (1,1)

def test_checkValidInputsReturnsFalse():
    userInput = "S"
    availableSpots = ["1", "2", "3"]

    inputState = inputChecker(userInput, availableSpots)

    assert inputState == False

def test_checkValidInputsReturnsTrue():
    userInput = "2"
    availableSpots = ["1", "2", "3"]

    inputState = inputChecker(userInput, availableSpots)

    assert inputState == True


@mock.patch("builtins.input", return_value = "5")
def test_userInput(userMock):
    possibleInputs = ["1", "3", "5"]
    userInput = getUserInput(possibleInputs)

    assert userInput == "5"

@mock.patch("builtins.input", return_value = 5)
def test_userInputReturnsString(userMock):
    possibleInputs = ["1", "3", "5"]
    userInput = getUserInput(possibleInputs)

    assert type(userInput) == str
    
@mock.patch("UserTurn.getUserInput", return_value = "5")
def test_getUserMoveChangesBoard(userMock):
    gameBoard = [["1", "2","3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

    possibleInputs = ["1", "2", "3",
        "4", "5", "6", "7", "8", "9"]

    returnBoard, returnInputs = getUserMove(gameBoard, possibleInputs)

    assert returnBoard[1][1] == "X"

@mock.patch("UserTurn.getUserInput", return_value = "5")
def test_getUserMoveChangesInputArray(userMock):
    gameBoard = [["1", "2","3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

    possibleInputs = ["1", "2", "3",
        "4", "5", "6", "7", "8", "9"]

    getUserMove(gameBoard, possibleInputs)

    assert possibleInputs == ["1", "2", "3",
        "4", "6", "7", "8", "9"]