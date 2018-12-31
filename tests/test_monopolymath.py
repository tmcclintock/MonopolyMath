import numpy as np
import numpy.testing as npt
import monopolymath as mm

def test_diceroller_exceptions():
    #Test that sides and number are ints
    with npt.assert_raises(Exception):
        dr = mm.DiceRoller(sides=6.)
    with npt.assert_raises(Exception):
        dr = mm.DiceRoller(number=6.)
    #Check that the probability_array() function raises exceptions
    with npt.assert_raises(Exception):
        dr = mm.DiceRoller(dice_array=[6,6])
        dr.probability_array()
    with npt.assert_raises(Exception):
        dr = mm.DiceRoller(sides=4)
        dr.probability_array()
    with npt.assert_raises(Exception):
        dr = mm.DiceRoller(number=4)
        dr.probability_array()
    return

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
    #Test that the probability array sums to 1
    npt.assert_equal(1., dr.probability_array().sum())
    npt.assert_equal(dr.N_combinations, dr.probability_array(unnormalized=True).sum())
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

def test_monopolyboard():
    #Test that a monopoly board object builds and has attributes
    mb = mm.MonopolyBoard()
    attrs = ["number_of_spaces","spaces","space_visits","position_vector",
             "position"]
    for att in attrs:
        npt.assert_equal(True, hasattr(mb, att))
    #Assign dice and test new attributes and roll matrix size
    mb.assign_dice()
    npt.assert_equal(True, hasattr(mb, "diceroller"))
    npt.assert_equal(True, hasattr(mb, "roll_matrix"))
    npt.assert_equal((40,40), mb.roll_matrix.shape)
    #Make sure that the current space is 0
    npt.assert_equal(1, mb.get_total_number_of_moves())
    npt.assert_equal(0, mb.position)
    npt.assert_equal("Go", mb._space_names()[mb.position])
    #Move 1 space and test everything again
    mb._update_from_move(1)
    npt.assert_equal(2, mb.get_total_number_of_moves())
    npt.assert_equal(1, mb.position)
    npt.assert_equal("Mediterranean Ave", mb._space_names()[mb.position])
    return

def test_monopolyroller():
    dr = mm.DiceRoller()
    mr = mm.MonopolyRollMover(dr)
    #Test 100 times that starting at any spot from 0 to 39
    #we get a new position in that range
    for i in range(0, 100):
        for p in range(0, 40):
            n = mr.update_position(p)
            npt.assert_equal(True, 0 <= n <= 39)
            continue
        continue
    return

if __name__ == "__main__":
    test_diceroller_exceptions()
    test_diceroller_without_dice_array()
    test_diceroller_with_dice_array()
    test_monopolyboard()
    test_monopolyroller()
