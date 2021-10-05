import sys
sys.path
sys.path.append("/src/")

from TicTacToe import *
from GameClass import GameState
from unittest import mock
import pytest


def test_catsGameBeforeUser(capsys):
    board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]

    possibleInputs = []

    with pytest.raises(SystemExit):
        oneTurn(board, possibleInputs)

    captured = capsys.readouterr()

    assert "Cat's Game!" in captured.out

@mock.patch("UserTurn.getUserInput", return_value = "4")
def test_catsGameBeforeComputer(userMock, capsys):
    board = [["O", "X","X"],
         ["4", "O", "O"],
         ["X", "O", "X"]]

    possibleInputs = ["4"]

    with pytest.raises(SystemExit):
        oneTurn(board, possibleInputs)

    captured = capsys.readouterr()

    assert "Cat's Game!" in captured.out

@mock.patch("UserTurn.getUserInput", return_value = "4")
def test_GameStateUpdatesPossibleInputs(computerMock):
    originalBoard = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]
    
    inputs = ["1", "2", "3", "4", "5",
        "6", "7", "8", "9"]

    newBoard, newInputs = oneTurn(originalBoard, inputs)

    assert len(newInputs) == 7

@mock.patch("UserTurn.getUserInput", return_value = "4")
def test_GameStateUpdatesGameBoard(computerMock):
    testState = GameState()
    originalBoard = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

    inputs = ["1", "2", "3", "4", "5",
        "6", "7", "8", "9"]

    newBoard, newInputs = oneTurn(originalBoard, inputs)

    assert newBoard == [["1", "2", "3"],
         ["X", "O", "6"],
         ["7", "8", "9"]]

def test_printsCorrectBoard(capsys):
    board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]

    printBoard(board)

    captured = capsys.readouterr()

    assert " 1 | 2 | X \n---+---+---\n 4 | O | 6 \n---+---+---\n X | 8 | 9 " in captured.out