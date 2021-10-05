from src.TicTacToe import GameState

def test_sample():
    assert True == True

def random():
    assert 1 == True

def test_getComputerInput():
    testState = GameState()

    testState.getComputerInput()

    assert len(testState.possibleInputs) == 8 
