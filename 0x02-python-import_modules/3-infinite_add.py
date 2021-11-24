#!/usr/bin/python3
import sys


if __name__ == '__main__':
    result = sys.argv
    ln = len(result)
    sum = 0

    if ln > 1:
        for n in range(1, ln):
            sum += int(result[n])
            print('{}'.format(sum))
        else:
            print('{}'.format(sum))
