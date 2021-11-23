#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    test_num = 0
    while(my_list > 0):
        remainder = my_list % 10
        test_num = (test_num * 10) + remainder
        my_list = my_list // 10
        print('{:d}'.format(test_num))
