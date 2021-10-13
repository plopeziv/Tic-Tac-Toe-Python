from TicTacToeLoop import takeTurns

class GameState:
    def __init__ (self):
        self.board = [["1", "2","3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

        self.possibleInputs = ["1", "2","3",
         "4", "5", "6",
         "7", "8", "9"]

    def PlayTicTacToe(self):
        takeTurns(self.board, self.possibleInputs)

if __name__ == "__main__":
    game = GameState()
    game.PlayTicTacToe()