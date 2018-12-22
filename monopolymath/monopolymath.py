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
        self.sides = 6
        self.number = 2
        self.dice_array = dice_array
        
    def roll(self):
        """
        Roll all the dice present on this object. Rolls either
        each dice of sides self.sides for each self.number of dice,
        or a dice of each integer in the self.dice_array list.
        """
        rolls = []
        if self.dice_array is not None:
            rolls.append(np.random.randint(dice) for dice in dice_array)
        else:
            rolls.append(np.random.randint(self.sides) for _ in range(0,self.number))
        #Fast way from stack overflow to determine if all
        #entries in "rolls" are equal, i.e. when doubles are rolled
        #but for arbitrary number of dice
        doubles = not rolls or [rolls[0]]*len(rolls) == rolls
        return np.sum(rolls), rolls, doubles
