#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for m in my_list:
        length += 1

        for n in range(x):
            try:
                print('{:d}'.format(my_list[n]), end="")
            except:
                print('')
                return length
            print("")
