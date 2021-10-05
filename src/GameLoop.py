from src.TicTacToe import GameState
from src.WinningCombo import checkForWin

def takeTurns(game, winCounter=False):

    print("Welcome to Tic Tac Toe!")

    while winCounter == False:
        game.startGame()
        winCounter = checkForWin(game.board)

    if winCounter == True:
        print("Winner!")
        print(game.printBoard())

game = GameState()
takeTurns(game=game)