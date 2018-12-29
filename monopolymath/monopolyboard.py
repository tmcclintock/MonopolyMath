"""
A specific monopoly board.
"""
from typing import List
from .diceroller import DiceRoller
from .board import Space, Board
import numpy as np

class MonopolySpace(Space):
    """
    Object to represent a space on th Monopoly board. Each space has
    a name, and sometimes a cost and rent.
    """
    def __init__(self, name: str,
                 cost=0, rent=None):
        self.name = name
        self.cost = cost
        self.rent = rent

class MonopolyBoard(Board):
    """
    A monopoly board. Extends the `board` class.
    """
    def __init__(self):
        names = ["Go", "Mediterranean Ave", "Community Chest 1",
                 "Baltic Ave", "Income Tax", "Reading Railroad",
                 "Oriental Ave", "Chance 1", "Vermont Ave",
                 "Connecticut Ave", "Just Visiting", "St. Charles Pl.",
                 "Electic Company", "States Ave", "Virgina Ave",
                 "Pennsylvania Railroad", "St. James Pl.", "Community Chest 2",
                 "Tennessee Ave", "NY Ave", "Free Parking",
                 "Kentucky Ave", "Chance 2", "Indiana Ave",
                 "Illinois Ave", "B&O Railroad", "Atlantic Ave", "Ventnor Ave",
                 "Water Works", "Marvin Gardens", "Go To Jail",
                 "Pacific Ave", "North Carolina Ave", "Community Chest 3",
                 "Pennsylvania Ave", "Short Line", "Chance 3",
                 "Park Place", "Luxury Tax", "Boardwalk"]
        self.number_of_spaces = len(names)
        #Create the spaces on the board
        self.spaces = [MonopolySpace(name, 0) for name in names]
        #Set the current position of an imaginary player to 0 (Go)
        self.space_visits = np.zeros(self.number_of_spaces)
        self.position_vector = np.zeros(self.number_of_spaces)
        self._update_position(0)

    def _space_names(self) -> List[str]:
        return [sp.name for sp in self.spaces]

    def _space_index_from_name(self, name: str) -> int:
        return self._space_names.index(name)

    def _update_from_move(self, move_amount: int) -> None:
        self._update_position(self.position + move_amount)
        return
        
    def _update_position(self, new_position: int) -> None:
        if new_position > self.number_of_spaces:
            raise Exception("Something went wrong, can't "+
                            "move to space %d"%new_position)
        self.position = new_position
        self.position_vector *= 0
        self.position_vector[self.position] = 1
        self.space_visits[new_position] += 1
        return

    def get_total_number_of_moves(self) -> int:
        """
        Get the total number of times a move
        on the board has been made, by summing up
        the number of times spaces have been visited.
        """
        return np.sum(self.space_visits)

    def get_current_space(self) -> MonopolySpace:
        """
        Get the space of the current position.
        """
        return self.spaces[self.position]
        
    def assign_dice(self,  sides=6, number=2, dice_array=None) -> None:
        """
        Assign dice to the board. By default this will be
        the standard monopoly set of two six-sided die.
        """
        self.diceroller = DiceRoller(sides, number, dice_array)
        self._compute_roll_matrix()
        return

    def _compute_roll_matrix(self) -> None:
        """
        Compute the roll matrix (R), which encodes the
        probability of going from one space to any other space
        by rolling the dice assigned to this board.
        """
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

    def _compute_action_matrix(self) -> None:
        """
        Compute the action matrix that encodes rules such as the jail,
        chance, community chest, and doubles. This function simply creates 
        the matrix from a-priori rules, and doesn't actually compute anything, 
        unlike the roll matrix. This is because the action matrix is set by 
        the game rules themselves.

        As more rules are added, this function will get longer. The following
        rules are implemented:
        - None
        The following rules need to be implemented:
        - Chance cards
        - Community chest cards
        - Jail jump
        - Jail doubles
        """
        N = self.number_of_spaces
        A = np.identity(N, dtype=np.int32)
        self.action_matrix = A
        return

    def move_player(self, via_roll=True) -> None:
        """
        Move the player, either via rolling the dice (simulation)
        or by apply the transition matrix to the position vector.
        """
        if via_roll:
            #make a roll, record the position
            roll, dice_rolls, doubles = self.diceroller.roll()
            new_position = (self.position+roll)%self.number_of_spaces
            self._update_position(new_position)
        else:
            #v = self.position_vector
            #T = self.transition_matrix #Roll \dot Action
            raise Exception("Moving via the transition matrix is "+\
                            "not implemented yet.")
        return

def main():
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

if __name__ == "__main__":
    main()
