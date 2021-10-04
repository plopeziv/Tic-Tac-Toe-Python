import sys
sys.path
sys.path.append("/src/")

from TicTacToe import GameState
from unittest import mock
import pytest

#Game runner responsibility
@mock.patch("TicTacToe.GameState.getUserInput", return_value = "4")
def test_catsGameBeforeUser(userMock, capsys):
    testState = GameState()
    testState.board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]

    testState.possibleInputs = []

    with pytest.raises(SystemExit):
        testState.oneTurn()

    captured = capsys.readouterr()

    assert "Cat's Game!" in captured.out

@mock.patch("TicTacToe.GameState.getUserInput", return_value = "4")
def test_catsGameBeforeComputer(userMock, capsys):
    testState = GameState()
    testState.board = [["O", "X","X"],
         ["4", "O", "O"],
         ["X", "O", "X"]]

    testState.possibleInputs = ["4"]

    with pytest.raises(SystemExit):
        testState.oneTurn()

    captured = capsys.readouterr()

    assert "Cat's Game!" in captured.out

def test_printsCorrectBoard(capsys):
    testState = GameState()
    testState.board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]

    testState.printBoard()

    captured = capsys.readouterr()

    assert " 1 | 2 | X \n---+---+---\n 4 | O | 6 \n---+---+---\n X | 8 | 9 " in captured.out

@mock.patch("TicTacToe.GameState.getUserInput", return_value = "4")
def test_GameStateUpdatesPossibleInputs(computerMock):
    testState = GameState()
    originalBoard = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

    testState.oneTurn()

    assert len(testState.possibleInputs) == 7

@mock.patch("TicTacToe.GameState.getUserInput", return_value = "4")
def test_GameStateUpdatesGameBoard(computerMock):
    testState = GameState()
    originalBoard = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

    testState.oneTurn()

    assert testState.board == [["1", "2", "3"],
         ["X", "O", "6"],
         ["7", "8", "9"]]
#End of game runner responsibility

#Start of userInput responsibility
def test_findIndex():
    testState = GameState()

    matrix = [["B","C"],
            ["1", "A"],
            ["D", 2]]

    index = testState.findIndex("A", matrix)

    assert index == (1,1)

def test_checkValidInputsReturnsFalse(capsys):
    testState = GameState()

    userInput = "S"
    availableSpots = ["1", "2", "3"]

    inputState = GameState.inputChecker(userInput, availableSpots)

    assert inputState == False

def test_checkValidInputsReturnsTrue(capsys):
    testState = GameState()

    userInput = "2"
    availableSpots = ["1", "2", "3"]

    inputState = GameState.inputChecker(userInput, availableSpots)

    assert inputState == True

@mock.patch("TicTacToe.GameState.getUserInput", return_value = "5")
def test_userInput(userMock):
    testState = GameState()

    userInput = testState.getUserInput()

    assert userInput == "5"

@mock.patch("TicTacToe.GameState.getUserInput", return_value = "5")
def test_getUserMoveChangesBoard(userMock):
    testState = GameState()

    testState.getUserMove()

    assert testState.board[1][1] == "X"

@mock.patch("TicTacToe.GameState.getUserInput", return_value = "5")
def test_getUserMoveChangesBoard(userMock):
    testState = GameState()

    testState.getUserMove()

    assert testState.possibleInputs.count("X") == 0
# End of userInput responsibility 
