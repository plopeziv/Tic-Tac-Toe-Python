import sys
sys.path
sys.path.append("/src/")

from TicTacToe import GameState
from unittest import mock
import pytest

#Game runner responsibility
def test_catsGameBeforeUser(capsys):
    testState = GameState()
    testState.board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]

    testState.possibleInputs = []

    with pytest.raises(SystemExit):
        testState.oneTurn()

    captured = capsys.readouterr()

    assert "Cat's Game!" in captured.out

@mock.patch("UserTurn.getUserInput", return_value = "4")
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

@mock.patch("UserTurn.getUserInput", return_value = "4")
def test_GameStateUpdatesPossibleInputs(computerMock):
    testState = GameState()
    originalBoard = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

    testState.oneTurn()

    assert len(testState.possibleInputs) == 7

@mock.patch("UserTurn.getUserInput", return_value = "4")
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