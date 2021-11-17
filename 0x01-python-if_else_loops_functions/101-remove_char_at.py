#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = ""
    for m in range(len(str)):
        if (m != n):
            str1 += str[m]
            return str1
