
# -*- coding: utf-8 -*-

import unittest

import klse_screener


class TestScreeners(unittest.TestCase):

    def test_stock_screener(self):
        dataframe = klse_screener.get_stock_screener()
        self.assertFalse(dataframe.empty)

    def test_warrant_screener(self):
        dataframe = klse_screener.get_warrant_screener()
        self.assertFalse(dataframe.empty)


if __name__ == "__main__":
    unittest.main(verbosity=2)
