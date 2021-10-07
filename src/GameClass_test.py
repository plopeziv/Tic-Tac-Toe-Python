from GameClass import GameState

def test_Greeting(capsys):
    game = GameState()
    game.board = [["O", "X","X"],
         ["X", "O", "O"],
         ["X", "O", "X"]]
    game.possibleInputs = []

    game.PlayTicTacToe()

    captured = capsys.readouterr()

    assert "Welcome to Tic Tac Toe!" in captured.out