import sys 
import numpy as np

from ComputerTurn import getComputerInput

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
        self.getUserMove()

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

# Start of User Input Responsibility
    def findIndex(self, element, matrix):
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == element:
                    return (row, column)

    def inputChecker(input, possibleInputs):
        returnValue = False

        if (input in possibleInputs):
            returnValue = True

        return returnValue

    def getUserInput(self):
        userInput = input("Please select a square! \n")

        inputCheck = self.inputChecker(userInput, self.possibleInputs)

        while inputCheck == False:
            userInput = input("Input not found. Please select a valid space. \n")

        
        return userInput

    def getUserMove(self):
        userInput = self.getUserInput()

        userIndex = self.findIndex(str(userInput), self.board)
        self.board[userIndex[0]][userIndex[1]] = "X"

        self.possibleInputs.remove(str(userInput))
#End of User Input Responsibility 