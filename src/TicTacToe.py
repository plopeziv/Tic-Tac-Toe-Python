# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random 

class GameState:
    def __init__ (self):
        self.board = ["0", "1","2",
         "3", "4", "5",
         "6", "7", "8"]

        self.possibleInputs = ["0", "1","2",
         "3", "4", "5",
         "6", "7", "8"]

        self.gameWon = False

    def isGameWon(self):
        return True

    def startGame(self):
        print("\n Welcome to Tic Tac Toe!")
        self.printBoard()
        self.getUserInput()
        self.getComputerInput()

    def printBoard(self):
        print("\n %s | %s | %s \n---+---+---\n %s | %s | %s \n---+---+---\n %s | %s | %s \n" % \
        (self.board[0], self.board[1], self.board[2],
        self.board[3], self.board[4], self.board[5],
        self.board[6], self.board[7], self.board[8]))

    def getUserInput(self):
        userInput = input("Please select a square!")

        userIndex = int(userInput)
        self.board[userIndex] = "X"

        self.possibleInputs.remove(userInput)

        self.printBoard()

    def getComputerInput(self):
        list = self.possibleInputs
        computerPick = random.choice(list)
        
        computerIndex = int(computerPick)
        self.board[computerIndex] = "O"

        self.possibleInputs.remove(computerPick)

        print ("Computer Picks " + computerPick + "! \n")
        self.printBoard()
