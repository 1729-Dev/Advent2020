import copy
import os
import unittest
from itertools import combinations

dirname = os.path.dirname(__file__)

class Day09(unittest.TestCase):
    def get_input(self, file):
        filename = os.path.join(dirname, file)
        with open(filename) as f:
            return list(map(lambda x: (int(x.strip())), f.readlines()))

    def get_combos(self, lookback):
        combos = list(combinations(lookback, 2))
        combos = list(map(lambda x: (x[0] + x[1]), combos))
        return list(set(combos))

    def get_lookback(self, input, length, position):
        return input[position - length:position]

    def run_data(self, input, length):
        for index in range(length, len(input)):
            combos = self.get_combos(self.get_lookback(input, length, index))
            if input[index] not in combos:
                return input[index]
        raise ValueError('we should not get here')

    def test_get_lookback(self):
        sample = self.get_input('day_09_sample.data')
        expected = [35, 20, 15, 25, 47]
        self.assertEqual(expected, self.get_lookback(sample, 5, 5))

    def test_get_input(self):
        result = self.get_input('day_09_sample.data')
        self.assertEqual(20, len(result))

    def test_get_combos(self):
        sample = [1, 2, 3, 4, 5]
        expected = [3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected, self.get_combos(sample))

    def test_sample_data(self):
        sample = self.get_input('day_09_sample.data')
        self.assertEqual(127, self.run_data(sample, 5))

    def test_real_data(self):
        puzzle = self.get_input('day_09.data')
        print(f"Answer: {self.run_data(puzzle, 25)}")

if __name__ == '__main__':
    unittest.main()
