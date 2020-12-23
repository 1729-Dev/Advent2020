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

    def get_combos(self, input):
        all_combos = []
        for length in range(2, len(input) + 1):
            left = 0
            right = left + length
            while right < len(input) + 1:
                combo = input[left:right]
                all_combos.append(combo)
                left += 1
                right += 1
        return all_combos

    def run_data(self, input, magic_number):
        combos = self.get_combos(input)
        for combo in combos:
            if sum(combo) == magic_number:
                combo.sort()
                return combo[0] + combo[len(combo)-1]
        raise ValueError('we should not get here')

    def test_get_input(self):
        result = self.get_input('day_09_sample.data')
        self.assertEqual(20, len(result))

    def test_get_combos(self):
        sample = [1, 7, 3]
        expected = [[1, 7], [7, 3], [1, 7, 3]]
        actual = self.get_combos(sample)
        self.assertEqual(expected, actual)

    def test_sample_data(self):
        sample = self.get_input('day_09_sample.data')
        magic_number = 127
        self.assertEqual(62, self.run_data(sample, magic_number))

    def test_real_data(self):
        puzzle = self.get_input('day_09.data')
        magic_number = 144381670
        print(f"Answer: {self.run_data(puzzle, magic_number)}")

if __name__ == '__main__':
    unittest.main()
