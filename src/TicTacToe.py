import sys 
import numpy as np

from ComputerTurn import getComputerInput
from UserTurn import getUserMove

class GameState:
    def __init__ (self):
        self.board = [["1", "2","3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

        self.possibleInputs = ["1", "2","3",
         "4", "5", "6",
         "7", "8", "9"]

#  Game runner Responsibilities
    def oneTurn(self):
        self.checkForCatsGame()

        self.printBoard()
        self.board, self.possibleInputs = getUserMove(self.board, self.possibleInputs)

        self.checkForCatsGame()

        self.board, self.possibleInputs = getComputerInput(self.board)

    def checkForCatsGame(self):
        if len(self.possibleInputs) == 0:
            print("\nCat's Game!\n")
            sys.exit()

    def printBoard(self):
        print("\n %s | %s | %s \n---+---+---\n %s | %s | %s \n---+---+---\n %s | %s | %s \n" % \
        (self.board[0][0], self.board[0][1], self.board[0][2],
        self.board[1][0], self.board[1][1], self.board[1][2],
        self.board[2][0], self.board[2][1], self.board[2][2]))
# End of Game Runner Responsibilities