from src.WinningCombo import checkWinningRows, checkWinningColumns

def test_checkBadBoards():
    gameBoard = [
        [],[],[]
    ]

    # Assert some error
    assert checkWinningRows(gameBoard) == "Please enter a 3 by 3 matrix"
    
def test_checkWinningRowsReturnsFalse():
    gameBoard = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

    assert checkWinningRows(gameBoard) == False

def test_checkWinningRowsReturnsWin():
    gameBoard = [
        ["1", "2", "3"],
        ["O", "O", "O"],
        ["7", "8", "9"]]

    assert checkWinningRows(gameBoard) == True

def test_checkWinningColumnsReturnsFalse():
    gameBoard = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

    assert checkWinningColumns(gameBoard) == False

def test_checkWinningColumnsReturnsWin():
    gameBoard = [
        ["1", "X", "3"],
        ["4", "X", "6"],
        ["7", "X", "9"]]

    assert checkWinningColumns(gameBoard) == True