#!/usr/bin/python3
for n in range(97, 123):
    if (n != 101 and n != 113):
        print('Prints ASCII except q and e {:c}'.format(n), end='')
