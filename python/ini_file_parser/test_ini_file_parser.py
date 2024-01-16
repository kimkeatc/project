
# -*- coding: utf-8 -*-

from os.path import join
import unittest

from ini_file_parser import ini_file_parser


class TestIniFileParser(unittest.TestCase):

    def test_01(self):
        filepath = join("test", "sample_01.ini")
        parser = ini_file_parser(filepath)
        for section in parser.sections():
            for key in parser[section]:
                value = parser[section][key]
                print(f"[{section}][{key}] {value}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
