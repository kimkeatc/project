
# -*- coding: utf-8 -*-

import unittest

import klse_stock_price


class TestStock(unittest.TestCase):

    def test_stock_get_daily(self):
        dataframe = klse_stock_price.Stock("1818").get_daily()
        print(dataframe)


if __name__ == "__main__":
    unittest.main(verbosity=2)
