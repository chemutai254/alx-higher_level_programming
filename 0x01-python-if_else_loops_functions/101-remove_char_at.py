#!/usr/bin/python3
def remove_char_at(str, n):
    str_one = ""
    for m in range(len(str)):
        if (m != n):
            str_one += str[m]
            return str_one
