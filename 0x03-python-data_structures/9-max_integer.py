#!/usr/bin/python3
def max_integer(my_list=[]):
    count = len(my_list)
    if count == 0:
        return None
    v_max = my_list[0]
    for n in my_list:
        if n > v_max:
            v_max = n
    return v_max
