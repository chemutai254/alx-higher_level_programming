#!/usr/bin/python3
def element_at(my_list, idx):
    for n in my_list:
        if idx == "-":
            return 'None'
        elif idx != n:
            return 'None'
