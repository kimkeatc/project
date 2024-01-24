
# -*- coding: utf-8 -*-

def is_prime_number(number: int) -> int:
    result = False
    if number <= 1:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                result = False
                break
        else:
            result = True
    return result
        
        
def get_prime_numbers(a: int, b: int) -> list:
    values = []
    for number in range(min(a, b), max(a, b)):
        if is_prime_number(number) is True:
            values.append(number)
    return values
