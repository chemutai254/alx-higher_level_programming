#!/usr/bin/python3
from calculator_1 import add, sub


def magic_calculation(a, b):
    if (a < b):
        c = add(a, b)

        for n in range(4, 6):
            c = add(c, n)

            return c
        else:
            return sub(a, b)
