from collections import Counter

import connectfour.Field as fd

class Connect4:
    def __init__(self, playerRed, playerYellow):
        self.field = fd.Field()

        self.playerRedFunction = playerRed
        self.playerYellowFunction = playerYellow

        self.playerRedFunction.set_color(fd.Field.RED_PLAYER)
        self.playerYellowFunction.set_color(fd.Field.YELLOW_PLAYER)
        
        self.playerForTurn = fd.Field.RED_PLAYER
        self.playerFunction = self.playerRedFunction
    
    def play(self):
        while not self.field.winningPlayer() and not self.field.boardIsFull():
            move = self.playerFunction.makeMove(self.field.copy())
            while not self.field.moveIsValid(move):
                move = self.playerFunction.makeMove(self.field.copy())
            self.field.makeMove(move, self.playerForTurn)

            if self.playerForTurn == fd.Field.RED_PLAYER:
                self.playerForTurn = fd.Field.YELLOW_PLAYER
                self.playerFunction = self.playerYellowFunction
            else:
                self.playerForTurn = fd.Field.RED_PLAYER
                self.playerFunction = self.playerRedFunction
        
        if self.field.winningPlayer() == fd.Field.NO_PLAYER:
            self.playerRedFunction.draw(self.field.copy())
            self.playerYellowFunction.draw(self.field.copy())
        else:
            if self.field.winningPlayer() == fd.Field.RED_PLAYER:
                self.playerRedFunction.won(self.field.copy())
                self.playerYellowFunction.lost(self.field.copy())
            else:
                self.playerRedFunction.lost(self.field.copy())
                self.playerYellowFunction.won(self.field.copy())
