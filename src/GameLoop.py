import sys
from TicTacToe import GameState
from WinningCombo import checkForWin

def takeTurns(gameClass, winCounter=False):

    print("Welcome to Tic Tac Toe!")

    while winCounter == False:
        gameClass.oneTurn()
        winCounter = checkForWin(gameClass.board)

    if winCounter == True:
        print("Game Over!")
        print(gameClass.printBoard())

        sys.exit()

if __name__ == "__main__":
    game = GameState()
    takeTurns(gameClass=game)