from src.TicTacToe import GameState
from src.WinningCombo import checkForWin

def takeTurns(gameClass, winCounter=False):

    print("Welcome to Tic Tac Toe!")

    while winCounter == False:
        gameClass.startGame()
        winCounter = checkForWin(gameClass.board)

    if winCounter == True:
        print("Winner!")
        print(gameClass.printBoard())

if __name__ == "__main__":
    game = GameState()
    takeTurns(gameClass=game)