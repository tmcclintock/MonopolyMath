"""
The rules for moving a monopoly player via rolling. 
This allows for simulating the roll and action matrices.
"""

class MonopolyRollMover(object):
    """
    An object for moving monopoly players via rolling.

    Args:
       diceroller (:obj: DiceRoller): object for rolling dice
    """
    def __init__(self, diceroller):
        self.diceroller = diceroller
        #Keep track of the number of consecutive doubles rolled
        self.N_doubles = 0
        self.in_jail = False

    def update_position(self, current_position: int,
                        number_of_spaces=40) -> int:
        #Roll the dice roller
        roll, dice_rolls, doubles = self.diceroller.roll()

        #Rule - getting out of jail on doubles
        if self.in_jail:
            if doubles is True:
                self.N_doubles += 1
                new_position = (10 + roll) % number_of_spaces
        else:
            self.in_jail = False
            new_position = (current_position + roll) % number_of_spaces
        #Determine rules about the new position
        #Rule - doubles
        if not doubles:
            N_doubles = 0
        else:
            N_doubles += 1
            if N_doubles == 3:
                new_position = 30 #Go to jail!
                self.in_jail = True
        
        #Rule - chance cards
        if new_position in [7, 22, 36]:
            new_position = new_position

        #Rule - community chest cards
        if new_position in [2, 17, 33]:
            new_position = new_position

        #Rule - going into jail
        if new_position is 30:
            self.in_jail = True
            self.N_doubles = 0 #Reset this
