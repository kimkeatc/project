
# -*- coding: utf-8 -*-

def generate(limit):
    sequence = []
    for _ in range(limit):
        if len(sequence) in (0, 1):
            sequence.append(len(sequence))
        else:
            a = sequence[-1]
            b = sequence[-2]
            c = a + b
            sequence.append(c)
    return sequence
