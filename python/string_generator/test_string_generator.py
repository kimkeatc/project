
# -*- coding: utf-8 -*-

import unittest

import string_generator


class TestStringGenerator(unittest.TestCase):

    def test_generate_one_time_password(self):
        password = string_generator.generate_one_time_password()
        self.assertTrue(password.isnumeric())

    def test_generate_password(self):
        length = 6
        password = string_generator.generate_password(length)
        self.assertEqual(len(password), length)
        self.assertTrue(isinstance(password, str))


if __name__ == "__main__":
    unittest.main(verbosity=2)
