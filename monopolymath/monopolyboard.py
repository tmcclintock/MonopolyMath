"""
A specific monopoly board.
"""
from diceroller import DiceRoller
from board import Space, Board
import numpy as np

class MonopolySpace(Space):
    def __init__(self, name, cost): #landing info to be added later
        self.name = name
        self.cost = cost

class MonopolyBoard(Board):
    """
    A monopoly board. Extends the `board` class.
    """
    def __init__(self):
        names = ["Go","St. James","f","m","l","Boardwalk"]
        self.number_of_spaces = len(names)
        #Create the spaces on the board
        self.spaces = [MonopolySpace(name, 0) for name in names]

if __name__ == "__main__":
    mb = MonopolyBoard()
    print(mb)
    mb.print_space_names()
