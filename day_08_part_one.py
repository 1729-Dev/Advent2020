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
            if instructions[index] is None:
                return accumulator
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

    def test_sample_data(self):
        instructions = self.get_instructions('day_08_sample.data')
        self.assertEqual(9, len(instructions))
        self.assertEqual(5, self.follow_instructions(instructions))

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
        print(f"Answer: {self.follow_instructions(instructions)}")

if __name__ == '__main__':
    unittest.main()
