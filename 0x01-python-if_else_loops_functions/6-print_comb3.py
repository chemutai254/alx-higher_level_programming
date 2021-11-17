#!/usr/bin/python3
for n in range(10):
    for m in range(10):
        if (n != m and n < m) and n < 9:
            if (n == 8 and m == 9):
                print('{0}{1}'.format(n, m))
            else:
                print('{0}{1}, '.format(n, m), end='')
