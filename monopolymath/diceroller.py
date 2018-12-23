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

    def minimum_roll(self):
        """
        The minimum possible roll given the dice on this roller.

        Returns:
            int: the minimum roll
        """
        return self.number

    def maximum_roll(self):
        """
        The maximum possible roll given the dice on this roller.

        Returns:
            int: the maximum roll
        """
        if self.dice_array is None:
            return self.number * self.sides
        else:
            return np.sum(self.dice_array)
            
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

    def get_possible_rolls(self):
        return np.arange(self.number, self.number*self.sides+1)

    def probability_array(self, unnormalized=False):
        """
        Return the multinomial disribution given the dice that this
        dice roller rolls. That is, the probability of being rolled 
        for each number that can be rolled.

        Returns:
            float array: Probability of each possible roll.
        """
        if self.dice_array is not None:
            raise Exception("P-array when using a dice_array not implemented yet.")
        else:
            if (self.sides is not 6) and (self.number is not 2):
                raise Exception("Anything but two six-sided dice not supported yet.")
            N_combinations = self.sides**self.number
            #Hack for 2d6
            combinations = np.array([1,2,3,4,5,6,5,4,3,2,1])
            probability = combinations/float(N_combinations)
        self.N_combinations = N_combinations
        if unnormalized:
            probability = combinations #don't do the divide
        return probability
