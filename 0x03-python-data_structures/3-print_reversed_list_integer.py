#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_num = 0
    while(my_list > 0):
        remainder = my_list % 10
        rev_num = (rev_num * 10) + reminder
        my_list = my_list // 10
        print('{:d}'.format(rev_num))
