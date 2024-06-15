import unittest

import main

class TestDragon(unittest.TestCase):

    def test_enter_cave(self):

        self.assertEqual(main.enter_cave("1", 1), "You have entered the cave with the treasure!")
        self.assertEqual(main.enter_cave("2", 2), "You have entered the cave with the treasure!")
        self.assertEqual(main.enter_cave("1", 2), "You have entered the cave with the dragon!")
        self.assertEqual(main.enter_cave("2", 1), "You have entered the cave with the dragon!")


if __name__ == '__main__':
    unittest.main()