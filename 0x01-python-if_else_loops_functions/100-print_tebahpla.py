#!/usr/bin/python3
for n in reversed(range(97, 123)):
    if (n % 2 == 0):
        print('{:c}'.format(n), end='')
    else:
        print('{:c}'.format(n - 32), end='')
