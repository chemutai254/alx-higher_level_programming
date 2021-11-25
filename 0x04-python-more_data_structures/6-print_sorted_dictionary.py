#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict = sorted(a_dictionary.items())
    for m, n in dict:
        print('{:d}: {:d}'.format(m, n))
