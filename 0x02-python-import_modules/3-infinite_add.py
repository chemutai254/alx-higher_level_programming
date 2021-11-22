#!/usr/bin/python3
import sys


if __name__ == '__main__':
    result = sys.argv
    ln = len(result)
    sum = 0

    for n in range(ln - 1):
        sum = sum + int(result[n + 1])
        print('{:d}'.format(sum))
