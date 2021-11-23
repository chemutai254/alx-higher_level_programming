#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for n in my_string:
        if n != 'C' and n != 'c':
            new_str += n
            return new_str
