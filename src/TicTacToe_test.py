from src.TicTacToe import GameState
from unittest.mock import patch

def test_sample():
    assert True == True

def test_findPossibleInputsReturnsArray():
    testState = GameState()

    testState.board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]


    testState.findPossibleInputs()

    assert testState.possibleInputs == ["1", "2", "4", "6", "8", "9"]

def test_getComputerInputChangesBoard():
    testState = GameState()

    testState.getComputerInput()

    assert testState.board == [["1", "2","3"],
         ["4", "O", "6"],
         ["7", "8", "9"]]

def test_getComputerInputRemovesPossibleInputs():
    testState = GameState()
    testState.board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]

    testState.getComputerInput()

# unique spots are originally 6 and the computer spot makes it 5
    assert len(testState.possibleInputs) == 5 

# @patch("src.TicTacToe.GameState.findIndex", return_value = (0,0))
# def test_getComputerInputReplacesBoardSpace():
#     testState = GameState()
#     testState.getComputerInput()

#     print(testState.board)

#     # Assert that board location has been replaced with Input 
