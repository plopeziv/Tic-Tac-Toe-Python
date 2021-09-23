from src.TicTacToe import GameState

def test_sample():
    assert True == True

def random():
    assert 1 == True

def test_getComputerInput():
    testState = GameState()

    testState.getComputerInput()

    assert len(testState.possibleInputs) == 8 

def test_topRowWinningCombo():
    testState = GameState()
    testState.board = ["X", "X","X",
         "3", "4", "5",
         "6", "7", "8"]
    
    assert testState.isGameWon() == True