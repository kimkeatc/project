
# -*- coding: utf-8 -*-

import configparser  # https://docs.python.org/3/library/configparser.html


def ini_file_parser(filepath: str) -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(filepath)
    return config


if __name__ == "__main__":

    # File directory
    filepath = r"C:\Users\kimkeatc\Downloads\sample.ini"

    parser = ini_file_parser(filepath)
    for section in parser.sections():
        for key in parser[section]:
            value = parser[section][key]
            print(f"[{section}][{key}] {value}")
