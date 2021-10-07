import sys
sys.path
sys.path.append("/src/")

from ComputerTurn import *

def test_findPossibleInputsReturnsArray():

    board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]


    possibleInputArray = findPossibleInputs(board)

    assert possibleInputArray == ["1", "2", "4", "6", "8", "9"]

def test_getComputerInputReturnsNewBoard():

    originalBoard = [["1", "2","3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

    returnBoard, inputReturnArray = getComputerInput(originalBoard)

    assert returnBoard == [["1", "2","3"],
         ["4", "O", "6"],
         ["7", "8", "9"]]

def test_getComputerInputRemovesPossibleInputs():

    board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]

    returnBoard, inputReturnArray = getComputerInput(board)

    assert len(inputReturnArray) == 5 