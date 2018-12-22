import numpy.testing as npt
import monopolymath as mm

def test_diceroller():
    #First, test that it builds
    dr = mm.DiceRoller()
    npt.assert_equal(6, dr.sides)
    npt.assert_equal(2, dr.number)
    npt.assert_equal(None, dr.dice_array)
    return
