import sys
sys.path
sys.path.append("/src/")

from TicTacToeLoop import takeTurns
from GameClass import GameState
from unittest import mock
import pytest


def test_Greeting(capsys):
    game = GameState()
    game.board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]
    game.possibleInputs = []

    with pytest.raises(SystemExit):
        takeTurns(game.board, game.possibleInputs)

    captured = capsys.readouterr()

    assert "Welcome to Tic Tac Toe!" in captured.out

def test_CheckForGameOver(capsys):
    game = GameState()
    game.board = [["X", "X", "X"],
        ["X", "O", "O"],
        ["X", "O", "X"]]

    with pytest.raises(SystemExit):
        takeTurns(game.board, game.possibleInputs)

    captured = capsys.readouterr()

    assert "Game Over!" in captured.out

@mock.patch("builtins.input", side_effect = [5])
def test_CheckGameLoopRunsWhenFalse(turnMock, capsys):
    game = GameState()
    game.board = [["O", "O", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

    game.possibleInputs = ["3",
         "4", "5", "6",
         "7", "8", "9"]

    with pytest.raises(SystemExit):
        takeTurns(game.board, game.possibleInputs)

    captured = capsys.readouterr()

    assert "Computer's Turn!" in captured.out