
# -*- coding: utf-8 -*-

import unittest

from factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_zero(self):
        number = 0
        result = factorial(number)
        self.assertEqual(result, 1)

    def test_one(self):
        number = 1
        result = factorial(number)
        self.assertEqual(result, 1)

    def test_two(self):
        number = 2
        result = factorial(number)
        self.assertEqual(result, 2)

    def test_three(self):
        number = 3
        result = factorial(number)
        self.assertEqual(result, 6)

    def test_five(self):
        number = 5
        result = factorial(number)
        self.assertEqual(result, 120)


if __name__ == "__main__":
    unittest.main(verbosity=2)
