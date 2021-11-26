#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        mult = 0
        suma = 0
        for n in my_list:
            mult += n[0] * n[1]
        for n in my_list:
            suma += n[1]
        return mult/suma
