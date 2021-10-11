from GameClass import GameState
from unittest import mock
# Start of PlayTicTacToe tests
@mock.patch("builtins.input", return_value = "n")
def test_Greeting(usermock, capsys):
    game = GameState()
    game.board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]
    game.possibleInputs = []

    game.PlayTicTacToe()

    captured = capsys.readouterr()

    assert "Welcome to Tic Tac Toe!" in captured.out

@mock.patch("builtins.input", return_value = "n")
def test_TicTacToeInitiatesTakeTurns(usermock, capsys):
    game = GameState()
    game.board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]
    game.possibleInputs = []

    game.PlayTicTacToe()

    captured = capsys.readouterr()

    assert "Cats Game!" in captured.out
# End of PlayTicTacToe tests

# Start of Helper Functions
@mock.patch("builtins.input", return_value = "n")
def test_gatherInput(inputMock):
     game = GameState()
     return_value = game._gatherInput()

     assert return_value == "N"

def test_formatText():
     game = GameState()

     formattedString = game._formatText("tHis TeXt")

     assert formattedString == "THIS TEXT"

def test_inputCheckerReturnsTrue():
     game = GameState()

     checkerReturn = game._inputChecker("Y", ["Y", "N"])

     assert checkerReturn == True

def test_inputCheckerReturnsFalse():
     game = GameState()

     checkerReturn = game._inputChecker("5", ["Y", "N"])

     assert checkerReturn == False

def test_checkLoopReturnsValue():
     game = GameState()

     loopReturn = game._checkLoop("Y", ["Y", "N"])
      
     assert loopReturn == "Y"

@mock.patch("builtins.input", return_value = "2")
def test_checkLoopInitiatesSecondInput(inputMock, capsys):
     game = GameState()

     loopReturn = game._checkLoop("S", ["1", "2"])

     captured = capsys.readouterr()

     assert loopReturn == "2"
# End of Helper Functions