import copy
import os
import unittest
from itertools import combinations

dirname = os.path.dirname(__file__)

class Day10(unittest.TestCase):
    def test_get_sorted_input(self):
        puzzle = self.get_sorted_input('day_10_a.data')
        self.assertEqual(13, len(puzzle))
        expected = [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
        self.assertEqual(expected, puzzle)

    def get_sorted_input(self, file):
        filename = os.path.join(dirname, file)
        with open(filename) as f:
            puzzle = list(map(lambda x: (int(x.strip())), f.readlines()))
            puzzle.append(0) # charging outlet
            puzzle.sort()
            highest_joltage = puzzle[len(puzzle)-1]
            puzzle.append(highest_joltage + 3)
            return puzzle

    def test_differences(self):
        puzzle = [0, 1, 1, 3, 5]
        expected = [0, 1, 2, 2]
        self.assertEqual(expected, self.differences(puzzle))
        puzzle = [0, 1, 1, 3, 5]
        differences = self.differences(puzzle)
        self.assertEqual(1, differences.count(0))
        self.assertEqual(1, differences.count(1))
        self.assertEqual(2, differences.count(2))
   
    def differences(self, puzzle):
        differences = []
        for index in range(1, len(puzzle)):
            differences.append(puzzle[index]-puzzle[index-1])
        differences.sort()
        return differences

    def test_max_gap(self):
        puzzle = [0, 1, 3, 9]
        self.assertEqual(6, self.max_gap(self.differences(puzzle)))
        puzzle = [1, 9, 11]
        self.assertEqual(8, self.max_gap(self.differences(puzzle)))

    def max_gap(self, differences):
        return differences[len(differences)-1]

    def test_puzzle(self):
        puzzle = self.get_sorted_input('day_10_a.data')
        differences = self.differences(puzzle)
        self.assertGreaterEqual(3, self.max_gap(differences))
        self.assertEqual(7, differences.count(1))
        self.assertEqual(5, differences.count(3))

        puzzle = self.get_sorted_input('day_10_b.data')
        differences = self.differences(puzzle)
        self.assertGreaterEqual(3, self.max_gap(differences))
        self.assertEqual(22, differences.count(1))
        self.assertEqual(10, differences.count(3))

        puzzle = self.get_sorted_input('day_10.data')
        differences = self.differences(puzzle)
        print(f"answer: {differences.count(1) * differences.count(3)}")

if __name__ == '__main__':
    unittest.main()
