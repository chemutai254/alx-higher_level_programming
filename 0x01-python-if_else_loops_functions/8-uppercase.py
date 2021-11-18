#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for n in range(str):
        char = ord(n)
        if (char <= ord('a') and char <= ord('z')):
            char = char - 32
            new_str = chr(char)
        else:
            new_str = n
            print('{0}'.format(new_str), end='')
            print('')
