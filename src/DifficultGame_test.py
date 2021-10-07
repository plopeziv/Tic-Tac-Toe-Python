import sys
sys.path
sys.path.append("/src/")

from DifficultGame import *

# Tests for Occupying Spot Five
def test_OccupySpotFive():
    gameBoard = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

    returnValue = checkForSpotFive(gameBoard)

    assert returnValue == [
        ["1", "2", "3"],
        ["4", "O", "6"],
        ["7", "8", "9"]]

def test_SpotFiveClosedX():
    gameBoard = [
        ["1", "2", "3"],
        ["4", "X", "6"],
        ["7", "8", "9"]]

    returnValue= checkForSpotFive(gameBoard)

    assert returnValue == None

def test_SpotFiveClosedO():
    gameBoard = [
        ["1", "2", "3"],
        ["4", "O", "6"],
        ["7", "8", "9"]]

    returnValue = checkForSpotFive(gameBoard)

    assert returnValue == None

# Tests for a game winning spot
def test_ForWinningSpot():
    gameBoard = [
        ["O", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "O"]]

    returnValue = checkForGameEnder(gameBoard, "O")

    assert returnValue == [
        ["O", "2", "3"],
        ["4", "O", "6"],
        ["7", "8", "O"]]

def test_ForLosingSpot():
    gameBoard = [
        ["O", "2", "3"],
        ["4", "X", "6"],
        ["X", "8", "O"]]

    returnValue = checkForGameEnder(gameBoard, "X")

    assert returnValue == [
        ["O", "2", "O"],
        ["4", "X", "6"],
        ["X", "8", "O"]]

#Eliminate specific winning combo
def test_winningComboIgnoredOpen():
    gameBoard = [
        ["1", "2", "X"],
        ["4", "O", "6"],
        ["7", "8", "X"]]

    returnValue = eliminateWinningCombo(gameBoard)

    assert returnValue == None

def test_winningCombo():
    gameBoard = [
        ["1", "2", "3"],
        ["4", "O", "6"],
        ["7", "8", "X"]]

    returnValue = eliminateWinningCombo(gameBoard)

    assert returnValue == [
        ["1", "2", "O"],
        ["4", "O", "6"],
        ["7", "8", "X"]]

# Tests To Occupy First Available Spot
def test_firstAvailableSpot():
    gameBoard = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["7", "8", "9"]]

    returnValue = takeFirstAvailableSpot(gameBoard)

    assert returnValue == [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "8", "9"]]

def test_firstAvailableSpotEmptyBoard():
    gameBoard = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

    returnValue = takeFirstAvailableSpot(gameBoard)

    assert returnValue == [
        ["O", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

# Intigration Tests
def test_takeSpotFive():
    gameBoard = [
        ["X", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]]

    returnValue = bestComputerSpot(gameBoard)

    assert returnValue == [
        ["X", "2", "3"],
        ["4", "O", "6"],
        ["7", "8", "9"]]

def test_winGame():
    gameBoard = [
        ["1", "2", "O"],
        ["4", "5", "6"],
        ["7", "8", "O"]]

    returnValue = bestComputerSpot(gameBoard)

    assert returnValue == [
        ["1", "2", "O"],
        ["4", "5", "O"],
        ["7", "8", "O"]]

def test_eliminateLoss():
    gameBoard = [
        ["X", "2", "O"],
        ["O", "X", "6"],
        ["7", "8", "9"]]

    returnValue = bestComputerSpot(gameBoard)

    assert returnValue == [
        ["X", "2", "O"],
        ["O", "X", "6"],
        ["7", "8", "O"]]

def test_eliminateSpecialCombo():
    gameBoard = [
        ["O", "2", "3"],
        ["4", "X", "6"],
        ["7", "8", "X"]]

    returnValue = bestComputerSpot(gameBoard)

    assert returnValue == [
        ["O", "2", "O"],
        ["4", "X", "6"],
        ["7", "8", "X"]]