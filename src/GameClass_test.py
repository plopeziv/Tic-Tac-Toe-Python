from GameClass import GameState
import pytest

def test_RunsTicTacToe(capsys):
    game = GameState()
    game.board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]

    game.possibleInputs = []


    with pytest.raises(SystemExit):
        game.PlayTicTacToe()

    captured = capsys.readouterr()

    assert "Welcome to Tic Tac Toe!" in captured.out