
# -*- coding: utf-8 -*-

import unittest

import odd_or_even_v1 as v1
import odd_or_even_v2 as v2


class TestOddEven(unittest.TestCase):

    def test_zero(self):
        number = 0

        self.assertTrue(v1.is_even(number))
        self.assertTrue(v2.is_even(number))

        self.assertFalse(v1.is_odd(number))
        self.assertFalse(v2.is_odd(number))

    def test_one(self):
        number = 1

        self.assertFalse(v1.is_even(number))
        self.assertFalse(v2.is_even(number))

        self.assertTrue(v1.is_odd(number))
        self.assertTrue(v2.is_odd(number))


if __name__ == "__main__":
    unittest.main(verbosity=2)
