import copy
import os
import unittest

dirname = os.path.dirname(__file__)

class Day08(unittest.TestCase):
    def get_instructions(self, file):
        filename = os.path.join(dirname, file)
        with open(filename) as f:
            lines = map(lambda x: (x.strip()), f.readlines())
            instructions = list(map(lambda x: (tuple(x.split(' '))), lines))

        return instructions

    def parse_amount(self, acc):
        if type(acc) is not str:
            raise ValueError
        if len(acc) < 2:
            raise ValueError
        if not acc[0] in '+-':
            raise ValueError
        amount = int(acc[1:])
        if acc[0] == '-':
            amount = amount * -1
        return amount

    def follow_instructions(self, instructions):
        index = 0
        accumulator = 0
        while True:
            if index == len(instructions):
                return accumulator
            if index > len(instructions):
                raise ValueException('did not expect this')
            if instructions[index] is None:
                return None
            inst = instructions[index][0]
            amount = self.parse_amount(instructions[index][1])
            instructions[index] = None
            if inst == 'jmp':
                index += amount
                continue
            if inst == 'acc':
                accumulator += amount
                index += 1
                continue
            if inst == 'nop':
                index += 1
                continue
            raise ValueException('what???')

    def deep_copy_instructions(self, instructions):
        new_instructions = []
        for instruction in instructions:
            new_instructions.append(instruction)
        return new_instructions

    def generate_permutations(self, instructions):
        nop_spots = [i for i, n in enumerate(instructions) if n[0] == 'nop']
        nop_permutations = []
        for _ in range(len(nop_spots)):
            nop_permutations.append(self.deep_copy_instructions(instructions))
        for index in range(len(nop_spots)):
                nop_permutations[index][nop_spots[index]] = ('jmp', nop_permutations[index][nop_spots[index]][1])

        jmp_spots = [i for i, n in enumerate(instructions) if n[0] == 'jmp']
        jmp_permutations = []
        for _ in range(len(jmp_spots)):
            jmp_permutations.append(self.deep_copy_instructions(instructions))
        for index in range(len(jmp_spots)):
                jmp_permutations[index][jmp_spots[index]] = ('nop', jmp_permutations[index][jmp_spots[index]][1])

        return nop_permutations + jmp_permutations

    def test_generate_permutations(self):
        instructions = self.get_instructions('day_08_sample.data')
        permutations = self.generate_permutations(instructions)
        self.assertEqual(4, len(permutations))
        for i in range(0, 4):
            expected = self.get_instructions(f"day_08_sample_expected_{i}.data")
            self.assertEqual(expected, permutations[i])

    def test_sample_data(self):
        instructions = self.get_instructions('day_08_sample.data')
        self.assertEqual(9, len(instructions))
        permutations = self.generate_permutations(instructions)
        self.assertEqual(4, len(permutations))
        for index in range(0, 3):
            self.assertEqual(None, self.follow_instructions(permutations[index]))
        self.assertEqual(8, self.follow_instructions(permutations[3]))

    def test_parse_amount(self):
        with self.assertRaises(ValueError):
            self.parse_amount('')
            self.parse_amount('-')
            self.parse_amount('1')
            self.parse_amount('+foo')
        self.assertEqual(1, self.parse_amount('+1'))
        self.assertEqual(-420, self.parse_amount('-420'))

    def test_actual(self):
        instructions = self.get_instructions('day_08.data')
        permutations = self.generate_permutations(instructions)
        print(f"actual perms: {len(permutations)}")
        for perm in permutations:
            answer = self.follow_instructions(perm)
            if answer: print(f"Answer: {answer}")

if __name__ == '__main__':
    unittest.main()
