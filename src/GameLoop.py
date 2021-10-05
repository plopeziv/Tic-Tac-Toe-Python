import sys
from TicTacToe import GameState
from WinningCombo import checkForWin

def takeTurns(gameClass):

    print("Welcome to Tic Tac Toe!")

    while checkForWin(gameClass.board) == False:
        gameClass.oneTurn()


    if checkForWin(gameClass.board) == True:
        print("Game Over!")
        print(gameClass.printBoard())

        sys.exit()

if __name__ == "__main__":
    game = GameState()
    takeTurns(gameClass=game)