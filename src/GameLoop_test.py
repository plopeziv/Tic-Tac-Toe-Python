import sys
sys.path
sys.path.append("/src/")

from GameLoop import takeTurns
from GameClass import GameState
from unittest import mock
import pytest


def test_Greeting(capsys):
    board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]
    possibleInputs = []

    with pytest.raises(SystemExit):
        takeTurns(board, possibleInputs, True)


    captured = capsys.readouterr()

    assert "Welcome to Tic Tac Toe!" in captured.out

def test_CheckForGameOver(capsys):
    game = GameState()
    game.board = [["X", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]

    with pytest.raises(SystemExit):
        takeTurns(game.board, game.possibleInputs, True)
  

    captured = capsys.readouterr()

    assert "Game Over!" in captured.out

@mock.patch("builtins.input", side_effect = [3])
def test_CheckGameLoopRunsWhenFalse(turnMock, capsys):
    board = [["O", "X","3"],
         ["X", "5", "O"],
         ["X", "O", "X"]]

    possibleInputs = ["3", "5"]

    with pytest.raises(SystemExit):
        takeTurns(board, possibleInputs)

    captured = capsys.readouterr()

    assert "Computer's Turn!" in captured.out