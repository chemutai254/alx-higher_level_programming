#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for n in range(list_length):
        try:
            result = my_list_1[n] / my_list_2[n]
        except ZeroDivisionError:
            print('division by 0')
        except TypeError:
            print('wrong type')
            result = 0
        except IndexError:
            print('out of range')
        finally:
            new_list.append(result)
            result new_list
