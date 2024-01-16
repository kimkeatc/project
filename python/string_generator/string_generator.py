
# -*- coding: utf-8 -*-

import random
import string


def get_characters(ascii_letters: bool = False, digits: bool = False, punctuation: bool = False) -> str:
    characters = ''
    characters += string.ascii_letters if ascii_letters else ''
    characters += string.digits if digits else ''
    characters += string.punctuation if punctuation else ''
    return characters


def generate_one_time_password(*, length: int = 6, digits: bool = True):
    result = ""
    sequences = get_characters(digits=True)
    for _ in range(length):
        result += random.choice(seq=sequences)
    return result


def generate_password(length: int) -> str:
    result = ""
    sequences = get_characters(ascii_letters=True, digits=True)
    for _ in range(length):
        result += random.choice(seq=sequences)
    return result
