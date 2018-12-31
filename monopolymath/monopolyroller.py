"""
The rules for moving a monopoly player via rolling. 
This allows for simulating the roll and action matrices.
"""
import numpy.random as rand

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
        self.time_in_jail = 0

    def update_position(self, current_position: int,
                        number_of_spaces=40) -> int:
        #The variable to be output
        new_position = None
        
        #Roll the dice roller
        roll, dice_rolls, doubles = self.diceroller.roll()

        #Rule - getting out of jail on doubles or time
        if self.in_jail:
            self.time_in_jail += 1
            #Roll doubles and you are out now
            if doubles:
                self.N_doubles += 1
                self.in_jail = False
                self.time_in_jail = 0
                new_position = (10 + roll) % number_of_spaces
            #Out on time and you are now just visiting
            if (self.time_in_jail >= 3):
                self.N_doubles = 0
                self.in_jail = False
                self.time_in_jail = 0
                new_position = 10
            else:
                new_position = 30 #still in jail
        else:
            new_position = (current_position + roll) % number_of_spaces
            
        #Determine rules about the new position
        #Rule - doubles
        if not doubles:
            self.N_doubles = 0
        else:
            self.N_doubles += 1
            if self.N_doubles == 3:
                new_position = 30 #Go to jail!
                self.in_jail = True
        
        #Rule - chance cards
        if new_position in [7, 22, 36]:
            draw = rand.randint(0, 16)
            if draw == 0: #Proceed to Go
                new_position = 0
            elif draw == 1: #Illinois Ave
                new_position = 24
            elif draw == 2: #St. Charles Pl.
                new_position = 11
            elif draw == 3: #Nearest Utility
                if new_position == 7:
                    new_position = 12
                else:
                    new_position = 28
            elif draw == 4: #Nearest Railroad
                if new_position == 7:
                    new_position = 5
                elif new_position == 22:
                    new_position = 25
                else:
                    new_position = 35
            elif draw == 7: #Back 3 spaces
                new_position -= 3
            elif draw == 8: #Go to jail
                new_position = 30
            elif draw == 11: #Reading Railroad
                new_position = 5
            elif draw == 12: #Boardwalk
                new_position = 39
            #else do nothing
                
        #Rule - community chest cards
        if new_position in [2, 17, 33]:
            draw = rand.randint(0, 16)
            if draw == 0: #Proceed to Go
                new_position = 0
            elif draw == 5: #Go to Jail
                new_position = 30
            #else do nothing

        #Rule - going into jail
        if new_position == 30:
            self.in_jail = True
            self.N_doubles = 0

        if (new_position < 0) or (new_position > 40):
            raise Exception("Something went wrong. "+\
                            "Roller position = %d."%new_position)

        #Return the new position
        return new_position
