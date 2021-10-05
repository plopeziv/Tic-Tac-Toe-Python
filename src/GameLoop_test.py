import sys
sys.path
sys.path.append("/src/")

from GameLoop import takeTurns
from TicTacToe import GameState
from unittest import mock
import pytest


def test_Greeting(capsys):
    game = GameState()
    game.board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]
    game.possibleInputs = []

    with pytest.raises(SystemExit):
        takeTurns(game)

    captured = capsys.readouterr()

    assert "Welcome to Tic Tac Toe!" in captured.out

def test_CheckForGameOver(capsys):
    game = GameState()
    game.board = [["X", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]

    with pytest.raises(SystemExit):
        takeTurns(game)

    captured = capsys.readouterr()

    assert "Game Over!" in captured.out

@mock.patch("TicTacToe.GameState.getUserMove", return_value = None)
def test_CheckGameLoopRunsWhenFalse(turnMock, capsys):
    game = GameState()

    game.possibleInputs = ["1", "2","3",
         "4", "5", "6",
         "7", "8", "9"]

    with pytest.raises(SystemExit):
        takeTurns(game)

    captured = capsys.readouterr()

    assert "Computer's Turn!" in captured.out