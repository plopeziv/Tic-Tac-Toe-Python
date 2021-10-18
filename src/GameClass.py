from TicTacToeLoop import takeTurns
import numpy as np
import itertools

class GameState:
    def __init__ (self):
        pass

    def PlayTicTacToe(self):
        print("Welcome to Tic Tac Toe!")  
        takeTurns(self._createGameboard(3), self._createInputArray(3))
        self.PlayAgain()

    def _createInputArray(self, gameWidth):
        Indexed = (gameWidth * gameWidth)
        possibleInputs = list()
        
        for position in range(Indexed):
            possibleInputs.append(str(position + 1))
        return possibleInputs

    def _createGameboard(self, gameWidth):
        gameBoard = list()
        positionSpot = itertools.count(1)
        
        for widthPosition in range(gameWidth):
            gameRow = list()
            
            for horizontalPosition in range(gameWidth):
                gameRow.append(str(next(positionSpot)))
            
            gameBoard.append(gameRow)

        return gameBoard

    def PlayAgain(self):
        possibleInputs = ["Y", "N"]

        userInput = self._gatherInput()
        userInput = self._checkLoop(userInput, possibleInputs)

        while userInput == "Y":
            newBoard = [["1", "2","3"],
                ["4", "5", "6"],
                ["7", "8", "9"]]
            newSpaces = ["1", "2","3",
                "4", "5", "6",
                "7", "8", "9"]

            takeTurns(newBoard, newSpaces)

            userInput = self._gatherInput()
            userInput = self._checkLoop(userInput, possibleInputs)


    def _gatherInput(self):
        userInput = input("\nWould you like to play again? Y/N\n")
        userInput = self._formatText(userInput)
        return userInput 

    def _formatText(self, input):
        input = str(input).upper()
        return input

    def _inputChecker(self, input, possibleInputs):
        returnValue = False

        if (input in possibleInputs):
            returnValue = True

        return returnValue

    def _checkLoop(self, userInput, possibleInputs):
        while self._inputChecker(userInput, possibleInputs) == False:
            userInput = str(input("Input not found. Please select Y/N. \n"))
            userInput = self._formatText(userInput)

        return userInput

if __name__ == "__main__":
    game = GameState()
    game.PlayTicTacToe()