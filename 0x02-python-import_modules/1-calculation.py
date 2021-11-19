#!/usr/bin/python3
from calculator_1 import sub, add, mul, div


if __name__ == "__main__":
    """

    Prints the results of subtraction, addition, multiplication and dividsion

    """
        a = 10
        b = 5
        print('{:d} - {:d}'.format(a, b, sub(a, b)))
        print('{:d} + {:d}'.format(a, b, add(a, b)))
        print('{:d} * {:d}'.format(a, b, mul(a, b)))
        print('{:d} / {:d}'.format(a, b, div(a, b)))
