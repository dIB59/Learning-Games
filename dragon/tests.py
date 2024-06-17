import unittest

import cave


class TestDragon(unittest.TestCase):

    def test_enter_cave(self):
        self.assertIsNotNone(cave.enter("1", "1"))

    def test_enter_cave_with_dragon(self):
        self.assertTrue("dragon" in cave.enter("2", "1"))

    def test_enter_cave_with_treasure(self):
        self.assertTrue("treasure" in cave.enter("1", "1"))


if __name__ == '__main__':
    unittest.main()
