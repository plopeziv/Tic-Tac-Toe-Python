import random 
import numpy as np

from src.DifficultGame import bestComputerSpot

class GameState:
    def __init__ (self):
        self.board = [["1", "2","3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

        self.possibleInputs = ["1", "2","3",
         "4", "5", "6",
         "7", "8", "9"]

    def startGame(self):
        self.printBoard()
        self.getUserMove()

        if len(self.possibleInputs) == 0:
            print("\nNo possible inputs left. Cat's Game!\n")
            quit()
        self.getComputerInput()

    def printBoard(self):
        print("\n %s | %s | %s \n---+---+---\n %s | %s | %s \n---+---+---\n %s | %s | %s \n" % \
        (self.board[0][0], self.board[0][1], self.board[0][2],
        self.board[1][0], self.board[1][1], self.board[1][2],
        self.board[2][0], self.board[2][1], self.board[2][2]))

# Start of User Input Responsibility
    def findIndex(self, element, matrix):
        for row in range(len(matrix)):
            for column in range(len(matrix[row])):
                if matrix[row][column] == element:
                    return (row, column)

    def getUserInput(self):
        userInput = input("Please select a square! \n")
        return userInput

    def getUserMove(self):
        userInput = self.getUserInput()

        userIndex = self.findIndex(str(userInput), self.board)
        self.board[userIndex[0]][userIndex[1]] = "X"

        self.possibleInputs.remove(str(userInput))
#End of User Input Responsibility 

# Start of Computer Input Responsibility
    def findPossibleInputs(self):
        holdArray = []

        for row in self.board:
            holdArray.extend(row)

        holdArray = np.unique(holdArray)
        holdArray = holdArray.tolist()
        
        if holdArray.count("X") > 0:
            holdArray.remove("X")
        
        if holdArray.count("O") > 0:
            holdArray.remove("O")

        self.possibleInputs = holdArray


    def getComputerInput(self):

        print(self.board)

        # Difficult Game Choice Module
        self.board = bestComputerSpot(self.board)

        print(self.board)

        self.findPossibleInputs()

        print ("\nComputer's Turn!")
# End of Computer Input Responsibility