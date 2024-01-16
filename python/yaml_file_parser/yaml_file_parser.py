
# -*- coding: utf-8 -*-

import yaml  # https://pyyaml.org/wiki/PyYAMLDocumentation


def yaml_file_parser(filepath: str) -> dict:
    with open(filepath, "r") as fh:
        data = yaml.safe_load(fh)
    return data
