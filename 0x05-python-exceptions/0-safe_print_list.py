#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if x > my_list:
            print(my_list)
    except x:
        print('Failed to print the list')
