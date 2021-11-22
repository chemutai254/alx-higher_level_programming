#!/usr/bin/python3
def sum(*args):
    result = 0

    for arg in args:
        result = int(result + arg)

        return result
