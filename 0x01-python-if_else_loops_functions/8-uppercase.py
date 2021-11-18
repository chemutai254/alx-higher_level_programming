#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for n in range(len(str)):
        if (ord(str[n]) >= 97 and ord(str[n]) <= 122):
            new_str += chr(ord(str[n]) - 32)
        new_str += str[n]
    else:
        new_str = n
        print('{0}'.format(new_str), end='')
