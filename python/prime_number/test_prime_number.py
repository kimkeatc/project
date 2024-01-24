
# -*- coding: utf-8 -*-

import unittest

from prime_number import is_prime_number, get_prime_numbers


class TestPrimeNumber(unittest.TestCase):

    def test_negative_value(self):
        number = -1
        result = is_prime_number(number)
        self.assertFalse(result)

    def test_zero(self):
        number = 0
        result = is_prime_number(number)
        self.assertFalse(result)

    def test_one(self):
        number = 1
        result = is_prime_number(number)
        self.assertFalse(result)

    def test_two(self):
        number = 2
        result = is_prime_number(number)
        self.assertTrue(result)

    def test_three(self):
        number = 3
        result = is_prime_number(number)
        self.assertTrue(result)

    def test_five(self):
        number = 5
        result = is_prime_number(number)
        self.assertTrue(result)

    def test_get_prime_numbers_from_0_to_100(self):
        a, b = 0, 100
        result = get_prime_numbers(a, b)
        self.assertEqual(len(result), 25)

        a, b = 100, 0
        result = get_prime_numbers(a, b)
        self.assertEqual(len(result), 25)


if __name__ == "__main__":
    unittest.main(verbosity=2)
