import sys
from TicTacToe import *
from GameClass import GameState
from WinningCombo import checkForWin


def takeTurns(board, possibleInputs, winCounter=False):

    print("Welcome to Tic Tac Toe!")

    while winCounter == False:
        board, possibleInputs = oneTurn(board, possibleInputs)
        winCounter = checkForWin(board)


    if checkForWin(gameClass.board) == True:
        print("Game Over!")
        print(printBoard(board))

        sys.exit()

if __name__ == "__main__":
    game = GameState()
    print(game.possibleInputs)
    takeTurns(game)