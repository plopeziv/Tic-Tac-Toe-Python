import sys
sys.path
sys.path.append("/src/")

from GameClass import GameState
from TicTacToeLoop import *
from unittest import mock

def test_catsGameReturnsFalse():
    return_value = checkForCatsGame(["5"])
    assert return_value == False

def test_catsGameReturnsTrue():
    return_value = checkForCatsGame([])
    assert return_value == True

def test_printsCorrectBoard(capsys):
    board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]

    printBoard(board)

    captured = capsys.readouterr()

    assert " 1 | 2 | X \n---+---+---\n 4 | O | 6 \n---+---+---\n X | 8 | 9 " in captured.out

@mock.patch("src.UserTurn.getUserInput", return_value = "4")
def test_oneTurnUpdatesPossibleInputs(computerMock):
    originalBoard = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]
    
    inputs = ["1", "2", "3", "4", "5",
        "6", "7", "8", "9"]

    newBoard, newInputs = oneTurn(originalBoard, inputs)

    assert len(newInputs) == 7

@mock.patch("src.UserTurn.getUserInput", return_value = "4")
def test_oneTurnUpdatesGameBoard(useMock):
    originalBoard = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

    inputs = ["1", "2", "3", "4", "5",
        "6", "7", "8", "9"]

    newBoard, newInputs = oneTurn(originalBoard, inputs)

    assert newBoard == [["1", "2", "3"],
         ["X", "O", "6"],
         ["7", "8", "9"]]

def test_CheckForGameOver(capsys):
    game = GameState()
    board = [["X", "X", "X"],
        ["X", "O", "O"],
        ["X", "O", "X"]]

    possibleInputs = []

    takeTurns(board, possibleInputs)

    captured = capsys.readouterr()

    assert "Game Over!" in captured.out

@mock.patch("src.UserTurn.getUserInput", return_value = "4")
def test_CheckCatsGameInitiates(userMock, capsys):
    originalBoard = [["X", "O", "X"],
         ["4", "X", "O"],
         ["O", "X", "O"]]

    inputs = ["4"]

    takeTurns(originalBoard, inputs)

    captured = capsys.readouterr()

    assert "Cats Game!" in captured.out

@mock.patch("builtins.input", side_effect = [5])
def test_CheckGameLoopRunsWhenFalse(turnMock, capsys):
    game = GameState()
    board = [["O", "O", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

    possibleInputs = ["3",
         "4", "5", "6",
         "7", "8", "9"]

    takeTurns(board, possibleInputs)

    captured = capsys.readouterr()

    assert "Computer's Turn!" in captured.out