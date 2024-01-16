
# -*- coding: utf-8 -*-

from os.path import join
import unittest

from yaml_file_parser import yaml_file_parser


class TestYamlFileParser(unittest.TestCase):

    def test_01(self):
        filepath = join("test", "sample_01.yaml")
        data = yaml_file_parser(filepath)
        self.assertTrue(isinstance(data, dict))


if __name__ == "__main__":
    unittest.main(verbosity=2)
