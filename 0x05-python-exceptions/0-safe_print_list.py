#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0

    try:
        for n in my_list:
            if length < x:
                print('{:d}'.format(my_list[length]), end='')
                length += 1

                print()
    except:
        pass
    return length
