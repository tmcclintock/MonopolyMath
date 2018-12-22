"""
A tool used to simulate a player playing the game Monopoly. This tool tracks the rolls that the player makes.
"""

import numpy as np

class DiceRoller(object):
    """
    An object used to roll the dice during the game.

    Args:
        sides (int): number of sides on the dice to roll
        number (int): number of dice to roll
        dice_array (list of ints): a specialized array of dice

    Returns:
        (int, list of ints, boolean): total of rolls, list of rolls, 
            and whether doubles were rolled
    """
    def __init__(self, sides=6, number=2, dice_array=None):
        if type(sides) is not int:
            raise Exception("'sides' must be an integer.")
        if type(number) is not int:
            raise Exception("'number' must be an integer.")
        self.sides = 6
        self.number = 2
        self.dice_array = dice_array
        if self.dice_array is not None:
            self.sides = -1
            self.number = len(dice_array)
        
    def roll(self):
        """
        Roll all the dice present on this object. Rolls either
        each dice of sides self.sides for each self.number of dice,
        or a dice of each integer in the self.dice_array list.
        """
        rolls = []
        if self.dice_array is not None:
            for dice in self.dice_array:
                rolls.append(np.random.randint(1, dice+1))
        else:
            for _ in range(0,self.number):
                rolls.append(np.random.randint(1, self.sides+1))
        #Fast way from stack overflow to determine if all
        #entries in "rolls" are equal, i.e. when doubles are rolled
        #but for arbitrary number of dice
        doubles = not rolls or [rolls[0]]*len(rolls) == rolls
        return np.sum(rolls), rolls, doubles
