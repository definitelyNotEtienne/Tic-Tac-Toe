"""
This code is referred and learned from Jannatul. Her TestCase was used as a reference.
"""
import main_mvc_pattern
import random
import unittest


class TestModel(unittest.TestCase):

    def test_spot_available(self):
        model = main_mvc_pattern.Model()
        for row in range(main_mvc_pattern.BOARD_ROW):
            for col in range(main_mvc_pattern.BOARD_COL):
                number = random.randint(1, 2)
                self.assertTrue(model.spot_available(row, col), "No spot available to be claim.")
                model.spot_claim(row, col, number)
                self.assertFalse(model.spot_available(row, col), "The spot was not claimed.")
                

    def test_board_full(self):
        model = main_mvc_pattern.Model()
        for row in range(main_mvc_pattern.BOARD_ROW):
            for col in range(main_mvc_pattern.BOARD_COL):
                number = random.randint(1, 2)
                self.assertFalse(model.board_full(), "The board is full")
                model.spot_claim(row, col, number)
            self.assertTrue(model.board_full(), "The board is not filled")


if __name__ == '__main__':
    unittest.main()
