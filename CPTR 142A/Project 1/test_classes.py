import classes
import unittest

class DiceTest(unittest.TestCase):
    def test_getside_method(self):
        dice_object = classes.Dice()
        self.assertIn(dice_object.get_side(), [".", "L", "R", "C"])

class PlayerTest(unittest.TestCase):
    def test_displayinfo_method(self):
        player_object = classes.Player("Jaime", 3)
        self.assertEqual(player_object.display_info(), "The name of the player is Jaime and has 3 tokens")

if __name__ == "__main__":
    unittest.main()