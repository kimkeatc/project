
# -*- coding: utf-8 -*-

def factorial(number: int) -> int:
    value = 1
    for n in range(1, number + 1):
        value *= n
    return value
