from src import TicTacToe
from src.TicTacToe import GameState
from unittest.mock import patch

def test_sample():
    assert True == True

def random():
    assert 1 == True

def test_getComputerInputRemovesPossibleInputs():
    testState = GameState()

    testState.getComputerInput()

    assert len(testState.possibleInputs) == 8 

# @patch("src.TicTacToe.GameState.findIndex", return_value = (0,0))
# def test_getComputerInputReplacesBoardSpace():
#     testState = GameState()
#     testState.getComputerInput()

#     print(testState.board)

#     # Assert that board location has been replaced with Input 
