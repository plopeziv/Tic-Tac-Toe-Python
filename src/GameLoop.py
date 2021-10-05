import sys
from TicTacToe import *
from GameClass import GameState
from WinningCombo import checkForWin

def takeTurns(gameClass, winCounter=False):

    print("Welcome to Tic Tac Toe!")

    while winCounter == False:
        gameClass.board, gameClass.possibleInputs = oneTurn(gameClass.board, gameClass.possibleInputs)
        winCounter = checkForWin(gameClass.board)

    if winCounter == True:
        print("Game Over!")
        print(printBoard(gameClass.board))

        sys.exit()

if __name__ == "__main__":
    game = GameState()
    print(game.possibleInputs)
    takeTurns(game)