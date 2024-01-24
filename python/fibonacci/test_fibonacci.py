
# -*- coding: utf-8 -*-

import unittest

from fibonacci import generate


class TestFibonacci(unittest.TestCase):

    def test_sequence_limit_20(self):
        limit = 20
        result = generate(limit)
        self.assertEqual(len(result), limit)
        self.assertEqual(sum(result), 10945)


if __name__ == "__main__":
    unittest.main(verbosity=2)
