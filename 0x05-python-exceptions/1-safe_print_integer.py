#!/usr/bin/python3
def safe_print_integer(value):
    integer = 0
    try:
        if value == integer:
            print('{:d} True'.format(value))
        else:
            print('{:d} False'.format(value))
    except value:
        print('the value is neither true or false')
