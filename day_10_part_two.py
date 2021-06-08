import os
import unittest

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

    def test_iterations_a(self):
        puzzle = self.get_sorted_input('day_10_a.data')
        successes = self.iterations(puzzle)
        self.assertEqual(8, len(successes))

    def test_iterations_b(self):
        puzzle = self.get_sorted_input('day_10_b.data')
        self.assertEqual(19208, self.iterations(puzzle))

    def iterations(self, puzzle):
        max_gap = self.max_gap(self.differences(puzzle))
        if max_gap > 3:
            return None
        if len(puzzle) < 4: # e.g. [0, 2, 5]
            return puzzle
        successes = []
        successes.append(puzzle)
        for index in range(1, len(puzzle)-1):
            smaller_puzzle = self.smaller_puzzle(puzzle, index)
            if self.max_gap(self.differences(smaller_puzzle)) < 4:
                other_successes = self.iterations(smaller_puzzle)
                for o_s in other_successes:
                    successes.append(o_s)
        dedupe_successes = []
        [dedupe_successes.append(x) for x in successes if x not in dedupe_successes]
        print(f"about to return: {dedupe_successes}")
        return dedupe_successes

    def test_smaller_puzzle(self):
        puzzle = [0, 1, 3, 6]
        expected = [0, 3, 6]
        self.assertEqual(expected, self.smaller_puzzle(puzzle, 1))

    def smaller_puzzle(self, puzzle, index):
        smaller_puzzle = []
        for i in range(0, len(puzzle)):
            if i != index:
                smaller_puzzle.append(puzzle[i])
        return smaller_puzzle

    def test_puzzle(self):
        print('not yet')

if __name__ == '__main__':
    unittest.main()
