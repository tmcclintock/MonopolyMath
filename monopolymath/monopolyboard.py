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
        #names = ["Go","St. James Place","f","m","l","Boardwalk"]
        names = np.arange(20)
        self.number_of_spaces = len(names)
        #Create the spaces on the board
        self.spaces = [MonopolySpace(name, 0) for name in names]
        #SET THE CURRENT POSITION OF AN IMAGINARY PLAYER
        #TODO? - make a MonopolyPlayer object?
        #this seems unreasonable since this board has all the
        #space information...
        self.space_visits = np.zeros(self.number_of_spaces)
        self.position_vector = np.zeros(self.number_of_spaces)
        self._update_position(0)
        self.number_of_rolls = 0
        
    def _update_position(self, new_position):
        if new_position > self.number_of_spaces:
            raise Exception("Something went wrong, can't "+
                            "move to space %d"%new_position)
        self.position = new_position
        self.position_vector *= 0
        self.position_vector[self.position] = 1
        self.space_visits[new_position] += 1
        return

    def get_current_space(self):
        return self.spaces[self.position]
        
    def assign_dice(self,  sides=6, number=2, dice_array=None):
        self.diceroller = DiceRoller(sides, number, dice_array)
        self._compute_roll_matrix()
        return

    def _compute_roll_matrix(self):
        if not hasattr(self, "diceroller"):
            raise Exception("Must assign dice before roll matrix is computed.")
        N = self.number_of_spaces
        self.roll_matrix = np.zeros((N,N))
        p = self.diceroller.probability_array()
        minroll = self.diceroller.minimum_roll()
        #Loop over the current row
        for i in range(N):
            #Add probability to each space that can be reached
            for j in range(minroll, len(p)+minroll):
                self.roll_matrix[i, (i+j)%N] += p[j-minroll]
                continue
            continue
        return

    def move_player(self):
        #make a roll, record the position
        roll, dice_rolls, doubles = self.diceroller.roll()
        new_position = (self.position+roll)%self.number_of_spaces
        self._update_position(new_position)
        return
    
if __name__ == "__main__":
    mb = MonopolyBoard()
    print(mb)
    mb.print_space_names()
    mb.assign_dice()
    print(mb.roll_matrix.shape)
    for i in range(10**5):
        mb.move_player()
    print(mb.space_visits)

    import matplotlib.pyplot as plt
    plt.imshow(mb.roll_matrix)
    plt.colorbar()
    plt.show()
