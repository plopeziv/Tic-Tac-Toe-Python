from src.TicTacToe import GameState
from unittest import mock

def test_printsCorrectBoard(capsys):
    testState = GameState()
    testState.board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]

    testState.printBoard()

    captured = capsys.readouterr()

    assert "\n 1 | 2 | X \n---+---+---\n 4 | O | 6 \n---+---+---\n X | 8 | 9 \n\n" in captured
    
#Start of userInput responsibility
def test_findIndex():
    testState = GameState()

    matrix = [["B","C"],
            ["1", "A"],
            ["D", 2]]

    index = testState.findIndex("A", matrix)

    assert index == (1,1)

@mock.patch("src.TicTacToe.GameState.getUserInput", return_value = "5")
def test_userInput(userMock):
    testState = GameState()

    userInput = testState.getUserInput()

    assert userInput == "5"

@mock.patch("src.TicTacToe.GameState.getUserInput", return_value = "5")
def test_getUserMoveChangesBoard(userMock):
    testState = GameState()

    testState.getUserMove()

    assert testState.board[1][1] == "X"

@mock.patch("src.TicTacToe.GameState.getUserInput", return_value = "5")
def test_getUserMoveChangesBoard(userMock):
    testState = GameState()

    testState.getUserMove()

    assert testState.possibleInputs.count("X") == 0
# End of userInput responsibility 

# Start of getComputerInput
def test_findPossibleInputsReturnsArray():
    testState = GameState()

    testState.board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]


    testState.findPossibleInputs()

    assert testState.possibleInputs == ["1", "2", "4", "6", "8", "9"]

def test_getComputerInputChangesBoard():
    testState = GameState()

    testState.getComputerInput()

    assert testState.board == [["1", "2","3"],
         ["4", "O", "6"],
         ["7", "8", "9"]]

def test_getComputerInputRemovesPossibleInputs():
    testState = GameState()
    testState.board = [["1", "2","X"],
         ["4", "O", "6"],
         ["X", "8", "9"]]

    testState.getComputerInput()

# unique spots are originally 6 and the computer spot makes it 5
    assert len(testState.possibleInputs) == 5 
# End of getComputerInput()
