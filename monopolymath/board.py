"""
A generalized board class for a dice-based board game.
It has a set of spaces that can be landed on that can have attributes.
"""
import numpy as np

class Space(object):
    """
    A boardgame space.

    Args:
        name (:obj:str): the name of the space
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

class Board(object):
    """
    A boardgame board.

    Args:
        number_of_spaces (int): number of spaces on the board
    """
    def __init__(self, number_of_spaces, names=None):
        if type(number_of_spaces) is not int:
            raise Exception("'number_of_spaces' must be an integer")
        assert number_of_spaces > 0
        self.number_of_spaces = number_of_spaces
        if names is None:
            names = np.arange(number_of_spaces) #just use numbers
        if len(names) != number_of_spaces:
            raise Exception("Must supply a name for every space.")
        #Create the spaces on the board
        self.spaces = [Space(name) for name in names]

    def print_space_names(self):
        print("Space names:")
        for i,s in enumerate(self.spaces):
            print("\tSpace %d: %s"%(i,s))
        return

if __name__ == "__main__":
    b = Board(5, ["a","b","c","d","e"])
    print(b)
    b.print_space_names()
