#!/usr/bin/python3

def print_list_integer(my_list):
    my_list = [1, 2, 3, 4, 5]
    str = "The number is {}"
    print(str.format(*my_list))
