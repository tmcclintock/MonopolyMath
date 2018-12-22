import numpy as np
import numpy.testing as npt
import monopolymath as mm

def test_diceroller_without_dice_array():
    #First, test that it builds
    dr = mm.DiceRoller()
    npt.assert_equal(6, dr.sides)
    npt.assert_equal(2, dr.number)
    npt.assert_equal(None, dr.dice_array)
    #Now, test that it can roll dice
    tot, rolls, doubles = dr.roll()
    npt.assert_equal(np.int64, type(tot))
    npt.assert_equal(list, type(rolls))
    npt.assert_equal(bool, type(doubles))
    #Roll a bunch of times, and make sure the totals
    #are always between 2 and 12, and the individual
    #rolls are in [1,6], and if the rolls are the same
    #then doubles is True and False otherwise.
    for _ in range(1000):
        tot, rolls, doubles = dr.roll()
        npt.assert_equal(True, 2 <= tot <= 12)
        npt.assert_equal(True, 1 <= rolls[0] <= 6)
        npt.assert_equal(True, 1 <= rolls[1] <= 6)
        npt.assert_equal(rolls[0]==rolls[1], doubles)
    return

def test_diceroller_with_dice_array():
    #Make a dice roller with a dice array and test that it builds
    dice_array = [4,5,8]
    dr = mm.DiceRoller(dice_array=dice_array)
    npt.assert_equal(-1, dr.sides)
    npt.assert_equal(len(dice_array), dr.number)
    npt.assert_equal(dice_array, dr.dice_array)
    #Now, test that it can roll dice
    tot, rolls, doubles = dr.roll()
    npt.assert_equal(np.int64, type(tot))
    npt.assert_equal(list, type(rolls))
    npt.assert_equal(bool, type(doubles))
    #Roll a bunch of times, and make sure the totals
    #are always between the expected numbers, and the individual
    #rolls are in the expected range, and if the rolls are the same
    #then doubles is True and False otherwise.
    for _ in range(1000):
        tot, rolls, doubles = dr.roll()
        npt.assert_equal(True, 3 <= tot <= 17)
        npt.assert_equal(True, 1 <= rolls[0] <= 4)
        npt.assert_equal(True, 1 <= rolls[1] <= 5)
        npt.assert_equal(True, 1 <= rolls[2] <= 8)
        npt.assert_equal(rolls[0]==rolls[1]==rolls[2], doubles)
    return

if __name__ == "__main__":
    test_diceroller_without_dice_array()
    test_diceroller_with_dice_array()
