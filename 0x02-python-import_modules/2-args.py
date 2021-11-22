#!/usr/bin/python3
import sys

if __name__ == '__main__':

    counter = len(sys.argv) - 1)
    if (counter) == 0:
        print('0 arguments.{}')
    elif (counter) == 1:
        print('1 argument: {}')
    else:
        print('{} arguments:'.format(counter))
        for n in range(counter):
            print('{}: {}'.format(n + 1, sys.argv[n + 1]))
