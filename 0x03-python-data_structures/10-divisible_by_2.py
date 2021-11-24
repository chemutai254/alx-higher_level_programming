#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for n in range(len(new_list)):
        if new_list[n] % 2 == 0:
            new_list[n] = True
        else:
            new_list[n] = False
    return new_list
